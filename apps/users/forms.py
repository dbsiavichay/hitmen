from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo electrónico",
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        exists = self.Meta.model.objects.filter(email=email).count()
        if exists:
            raise ValidationError(
                "Ya existe un usuario con este correo"
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get("email")
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user

