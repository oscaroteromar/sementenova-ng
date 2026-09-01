from django.http import JsonResponse

from .models import Score


def score_list(request):
    data = [
        {
            "id": s.id,
            "title": s.title,
            "category": s.category,
            "category_display": s.get_category_display(),
            "notes": s.notes,
            "file_url": request.build_absolute_uri(s.file.url),
            "preview_url": (
                request.build_absolute_uri(s.preview_image.url) if s.preview_image else None
            ),
            "uploaded_at": s.uploaded_at.isoformat(),
        }
        for s in Score.objects.all()
    ]
    return JsonResponse({"results": data})
