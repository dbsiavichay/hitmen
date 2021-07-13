from django import forms
from django.db.models import query
from django.forms import fields, widgets

from .models import Hit

class HitForm(forms.ModelForm):
    class Meta:
        model = Hit
        fields = ("target", "description", "assignee", "creator")
        widgets = {
            "creator": forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        creator = self.initial.get("creator")
        if creator:
            queryset = self.fields["assignee"].queryset
            self.fields["assignee"].queryset = queryset.exclude(id__in=[1, creator.id])