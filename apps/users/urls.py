from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, UserListView, AssignHitmenView

urlpatterns = [
    path(
        route="register/",
        view=RegisterView.as_view(),
        name="register",
    ),
    path(
        route="login/",
        view=auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        route="hitmen/",
        view=UserListView.as_view(),
        name="hitmen",
    ),
     path(
        route="assign/hitmen/",
        view=AssignHitmenView.as_view(),
        name="assign_hitmen",
    ),
]