from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import RegisterForm, HitmenForm

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Successfully registered")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "An error has occurred")
        return super().form_valid(form)



class UserListView(PermissionRequiredMixin ,FormMixin, ListView):
    model = User
    form_class = HitmenForm

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.id == 1:
            queryset = queryset.filter(Q(id=user.id) | Q(manager=user))
        return queryset

    def has_permission(self):
        user = self.request.user
        return user.id == 1 or user.lackeys.all().count()


class UserDetailView(DetailView):
    model = User


class AssignHitmenView(PermissionRequiredMixin ,FormView):
    form_class = HitmenForm

    def form_valid(self, form):
        hitmen = form.cleaned_data.get("hitmen")
        manager = form.cleaned_data.get("manager")
        hitmen = hitmen.exclude(pk=manager.id)
        if hitmen:
            hitmen.update(manager=manager)
            manager.manager = None
            manager.save()
        messages.add_message(self.request, messages.SUCCESS, "Successfully assignment")
        return redirect(reverse_lazy("hitmen"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "An error has occurred")
        return redirect(reverse_lazy("hitmen"))

    def has_permission(self):
        return self.request.user.id == 1
    