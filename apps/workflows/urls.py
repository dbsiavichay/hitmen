# Django
from django.urls import path

# Views
from .views import TransitionView

urlpatterns = [
    path(
        route="workflow/<slug:app>/<slug:model>/<slug:transition>/<int:pk>/change/",
        view=TransitionView.as_view(),
        name="workflow_transition",
    ),
]
