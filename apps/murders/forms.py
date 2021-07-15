from django import forms

from .models import Hit
from apps.users.models import User

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
            queryset = queryset.filter(status=queryset.model.Status.ACTIVE)
            if creator.id == 1:
                queryset = queryset.exclude(id__in=[creator.id])
            else:
                queryset = creator.lackeys.filter(
                    status=queryset.model.Status.ACTIVE
                ).exclude(
                    id__in=[1, creator.id], 
                )
            self.fields["assignee"].queryset = queryset


class BulkAssignForm(forms.Form):
    hits = forms.ModelMultipleChoiceField(
        queryset=Hit.objects.filter(
            status=Hit.Status.ASSIGNED
        ),
        label="Available hits"
    )
    assignee = forms.ModelChoiceField(
        queryset=User.objects.filter(status=User.Status.ACTIVE).exclude(id=1),
    )