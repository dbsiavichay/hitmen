from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    HitListView, HitCreateView, HitUpdateView, HitDetailView
)

urlpatterns = [
    path(
        route="hits/",
        view=login_required(HitListView.as_view()),
        name="hits",
    ),
    path(
        route="hits/create/",
        view=login_required(HitCreateView.as_view()),
        name="create_hit",
    ),
    path(
        route="hits/<int:pk>/update/",
        view=login_required(HitUpdateView.as_view()),
        name="update_hit",
    ),
    path(
        route="hits/<int:pk>/",
        view=login_required(HitDetailView.as_view()),
        name="detail_hit",
    ),
]