from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Score

PAGE_SIZE = 9


def score_list(request):
    queryset = Score.objects.all()

    category = request.GET.get("category")
    if category and category in Score.Category.values:
        queryset = queryset.filter(category=category)

    search = request.GET.get("search", "").strip()
    if search:
        queryset = queryset.filter(title__icontains=search)

    available_categories = list(
        Score.objects.order_by().values_list("category", flat=True).distinct()
    )

    paginator = Paginator(queryset, PAGE_SIZE)
    page = paginator.get_page(request.GET.get("page"))

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
        for s in page.object_list
    ]

    return JsonResponse(
        {
            "results": data,
            "page": page.number,
            "num_pages": paginator.num_pages,
            "count": paginator.count,
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
            "available_categories": available_categories,
        }
    )
