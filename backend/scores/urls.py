from django.urls import path

from . import views

urlpatterns = [
    path("scores/", views.score_list, name="score-list"),
]
