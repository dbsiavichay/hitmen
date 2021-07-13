from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView

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
]