from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Hit
from .mixins import HitMixin


class HitListView(ListView):
    model = Hit

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if not user.id == 1:
            lackeys = list(user.lackeys.values_list("id", flat=True).all())
            lackeys.append(user.id)
            queryset = queryset.filter(assignee_id__in=lackeys)
        return queryset


class HitCreateView(HitMixin, CreateView):
    pass


class HitUpdateView(HitMixin, UpdateView):
    pass


class HitDetailView(PermissionRequiredMixin, DetailView):
    model = Hit

    def has_permission(self):
        user = self.request.user
        if user.id == 1:
            return True
        lackeys = list(user.lackeys.values_list("id", flat=True).all())
        lackeys.append(user.id)
        return self.get_object().assignee_id in lackeys
        
