from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import RegisterView, UserListView, UserDetailView, AssignHitmenView

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
        route="hitmen/<int:pk>/",
        view=login_required(UserDetailView.as_view()),
        name="hitmen_detail",
    ),
     path(
        route="assign/hitmen/",
        view=login_required(AssignHitmenView.as_view()),
        name="assign_hitmen",
    ),
]