from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Hit
from .forms import HitForm


class HitMixin(PermissionRequiredMixin):
    model = Hit
    form_class = HitForm
    success_url = reverse_lazy("hits")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Successfully saved")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "An error has occurred")
        return super().form_invalid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial["creator"] = self.request.user
        return initial

    def has_permission(self):
        user = self.request.user
        if user.id == 1:
            return True
        lackeys = list(user.lackeys.values_list("id", flat=True).all())
        if not lackeys:
            return False
        if self.kwargs.get("pk"):
            self.object = self.get_object()
            return self.object.assignee_id in lackeys or self.object.assignee_id == user.id
        return self.request.user.lackeys.all().count()