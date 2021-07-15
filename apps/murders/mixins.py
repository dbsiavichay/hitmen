from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Hit
from .forms import HitForm


class HitMixin(PermissionRequiredMixin):
    model = Hit
    form_class = HitForm
    success_url = reverse_lazy("hits")

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
            return self.get_object().assignee_id in lackeys
        return self.request.user.lackeys.all().count()