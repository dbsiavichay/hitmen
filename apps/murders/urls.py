from django.urls import path

from .views import HitListView, HitCreateView, HitDetailView

urlpatterns = [
    path(
        route="hits/",
        view=HitListView.as_view(),
        name="hits",
    ),
    path(
        route="hits/create/",
        view=HitCreateView.as_view(),
        name="create_hit",
    ),
    path(
        route="hits/<int:pk>/",
        view=HitDetailView.as_view(),
        name="detail_hit",
    ),
]