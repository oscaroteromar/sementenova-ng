from django.contrib import admin
from django.utils.html import format_html

from .models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "title", "category", "uploaded_at")
    list_filter = ("category",)
    search_fields = ("title",)

    @admin.display(description="")
    def thumbnail(self, obj):
        if not obj.preview_image:
            return ""
        return format_html(
            '<img src="{}" style="height:48px;border-radius:4px" />', obj.preview_image.url
        )
