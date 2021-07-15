from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Hit
from .mixins import HitMixin
from .forms import BulkAssignForm


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
    def has_permission(self):
        perm =  super().has_permission()
        if perm:
            self.object = self.get_object()
            return self.object.status == self.object.Status.ASSIGNED
        return perm


class HitDetailView(PermissionRequiredMixin, DetailView):
    model = Hit

    def has_permission(self):
        user = self.request.user
        if user.id == 1:
            return True
        lackeys = list(user.lackeys.values_list("id", flat=True).all())
        lackeys.append(user.id)
        return self.get_object().assignee_id in lackeys
        

class HitBulkReassignView(PermissionRequiredMixin, FormView):
    form_class = BulkAssignForm
    template_name = "murders/hit_bulk.html"

    def form_valid(self, form):
        hits = form.cleaned_data.get("hits")
        assignee = form.cleaned_data.get("assignee")
        hits.update(assignee=assignee)
        messages.add_message(self.request, messages.SUCCESS, "Successfully assignment")
        return redirect(reverse_lazy("hits"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "An error has occurred")
        return redirect(reverse_lazy("bulk_hit"))

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        if not user.id == 1:
            lackeys = list(user.lackeys.values_list("id", flat=True).all())
            assignee_queryset = form.fields["assignee"].queryset
            form.fields["assignee"].queryset = assignee_queryset.filter(id__in=lackeys)
            lackeys.append(user.id)
            hits_queryset = form.fields["hits"].queryset
            form.fields["hits"].queryset = hits_queryset.filter(assignee_id__in=lackeys)
        return form

    def has_permission(self):
        user = self.request.user
        return user.id == 1 or user.lackeys.all()