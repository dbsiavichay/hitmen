from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

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
        view=login_required(UserListView.as_view()),
        name="hitmen",
    ),
     path(
        route="assign/hitmen/",
        view=login_required(AssignHitmenView.as_view()),
        name="assign_hitmen",
    ),
]