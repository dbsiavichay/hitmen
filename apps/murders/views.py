from apps.murders.forms import HitForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Hit

class HitListView(ListView):
    model = Hit


class HitCreateView(CreateView):
    model = Hit
    form_class = HitForm
    success_url = reverse_lazy("hits")

    def get_initial(self):
        initial = super().get_initial()
        initial["creator"] = self.request.user
        return initial


class HitDetailView(DetailView):
    model = Hit