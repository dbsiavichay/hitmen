from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import RegisterForm, HitmenForm

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserListView(FormMixin, ListView):
    model = User
    form_class = HitmenForm


class AssignHitmenView(FormView):
    form_class = HitmenForm

    def form_valid(self, form):
        hitmen = form.cleaned_data.get("hitmen")
        manager = form.cleaned_data.get("manager")
        hitmen = hitmen.exclude(pk=manager.id)
        if hitmen:
            hitmen.update(manager=manager)
            manager.manager = None
            manager.save()
        return redirect(reverse_lazy("hitmen"))

    def form_invalid(self, form):
        return redirect(reverse_lazy("hitmen"))
    