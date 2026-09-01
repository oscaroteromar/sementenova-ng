from pathlib import Path

from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models


class Score(models.Model):
    class Category(models.TextChoices):
        RONDALLA = "rondalla", "Rondalla"
        BAILE = "baile", "Baile galego"
        GAITA = "gaita", "Gaita, pandeireta e percusión"
        OUTROS = "outros", "Outros"

    title = models.CharField("título", max_length=200)
    category = models.CharField(
        "categoría", max_length=20, choices=Category.choices, default=Category.OUTROS
    )
    file = models.FileField(
        "ficheiro",
        upload_to="scores/%Y/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        help_text="Só se admiten ficheiros PDF.",
    )
    preview_image = models.ImageField(
        "vista previa", upload_to="scores_previews/%Y/", blank=True, editable=False
    )
    notes = models.CharField("notas", max_length=300, blank=True)
    uploaded_at = models.DateTimeField("data de subida", auto_now_add=True)

    class Meta:
        ordering = ["category", "title"]
        verbose_name = "partitura"
        verbose_name_plural = "partituras"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        previous_file = None
        if self.pk:
            previous_file = (
                Score.objects.filter(pk=self.pk).values_list("file", flat=True).first()
            )
        super().save(*args, **kwargs)
        if self.file and self.file.name != previous_file:
            self._generate_preview()

    def _generate_preview(self):
        import pymupdf

        self.file.open("rb")
        try:
            document = pymupdf.open(stream=self.file.read(), filetype="pdf")
            pixmap = document.load_page(0).get_pixmap(matrix=pymupdf.Matrix(0.8, 0.8))
            png_bytes = pixmap.tobytes("png")
        finally:
            self.file.close()

        preview_name = Path(self.file.name).with_suffix(".png").name
        self.preview_image.save(preview_name, ContentFile(png_bytes), save=False)
        Score.objects.filter(pk=self.pk).update(preview_image=self.preview_image.name)
