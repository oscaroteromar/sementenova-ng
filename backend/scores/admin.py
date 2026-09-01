import zipfile
from pathlib import Path

from django import forms
from django.contrib import admin, messages
from django.core.files.base import ContentFile
from django.shortcuts import redirect, render
from django.urls import path
from django.utils.html import format_html

from .models import Score


class ZipImportForm(forms.Form):
    zip_file = forms.FileField(label="Ficheiro ZIP")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "title", "category", "uploaded_at")
    list_display_links = ("title",)
    list_filter = ("category",)
    search_fields = ("title",)
    change_list_template = "admin/scores/score/change_list.html"

    @admin.display(description="")
    def thumbnail(self, obj):
        if not obj.preview_image:
            return ""
        return format_html(
            '<img src="{}" style="height:48px;border-radius:4px" />', obj.preview_image.url
        )

    def get_urls(self):
        custom = [
            path(
                "import-zip/",
                self.admin_site.admin_view(self.import_zip_view),
                name="scores_score_import_zip",
            ),
        ]
        return custom + super().get_urls()

    def import_zip_view(self, request):
        if request.method == "POST":
            form = ZipImportForm(request.POST, request.FILES)
            if form.is_valid():
                self._process_zip(request, form.cleaned_data["zip_file"])
                return redirect("admin:scores_score_changelist")
        else:
            form = ZipImportForm()

        context = {
            **self.admin_site.each_context(request),
            "form": form,
            "title": "Importar partituras dende ZIP",
            "opts": self.model._meta,
        }
        return render(request, "admin/scores/import_zip.html", context)

    def _process_zip(self, request, zip_file):
        if not zipfile.is_zipfile(zip_file):
            messages.error(request, "O ficheiro non é un ZIP válido.")
            return

        imported = []
        errors = []
        with zipfile.ZipFile(zip_file) as archive:
            for info in archive.infolist():
                base_name = Path(self._decode_zip_filename(info)).name
                if info.is_dir() or not base_name.lower().endswith(".pdf"):
                    continue
                if base_name.startswith("."):
                    continue  # e.g. macOS __MACOSX/._foo.pdf resource forks

                try:
                    data = archive.read(info)
                    score = Score(title=Path(base_name).stem, category=Score.Category.OUTROS)
                    score.file.save(base_name, ContentFile(data), save=True)
                    imported.append(base_name)
                except Exception:
                    errors.append(base_name)

        if imported:
            messages.success(request, f"Importáronse {len(imported)} partitura(s): {', '.join(imported)}")
        if errors:
            messages.warning(request, f"Non se puideron importar: {', '.join(errors)}")
        if not imported and not errors:
            messages.warning(request, "Non se atopou ningún PDF dentro do ZIP.")

    @staticmethod
    def _decode_zip_filename(info):
        # zipfile decodes names as cp437 unless the entry's UTF-8 flag bit is
        # set; many zip tools (e.g. macOS's `zip` CLI) write UTF-8 bytes
        # without setting that flag, so accented filenames come out mangled.
        # Undo the wrong cp437 decode and recover the real UTF-8 bytes.
        if info.flag_bits & 0x800:
            return info.filename
        try:
            return info.filename.encode("cp437").decode("utf-8")
        except UnicodeError:
            return info.filename
