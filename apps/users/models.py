"""User model."""
#  Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html

from django_fsm import FSMIntegerField, transition


class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    class Status(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1

    email = models.EmailField(
        unique=True,
        verbose_name="Correo electrónico",
        error_messages={"unique": "Un usuario con ese correo ya existe."},
    )
    manager = models.ForeignKey(
        "self", on_delete=models.PROTECT,
        null=True, related_name="lackeys",
        verbose_name="manager"
    )

    status = FSMIntegerField(
        choices=Status.choices, default=Status.ACTIVE,
        protected=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "usuario"
        

    def __str__(self):
        """Return username."""
        return self.email

    @property
    def get_status(self):
        status = (
            (self.Status.ACTIVE, "primary"), (self.Status.INACTIVE, "danger")
        )
        html = f'<span class="badge badge-{dict(status)[self.status]}">{dict(self.Status.choices)[self.status].upper()}</span>'
        return format_html(html)

    @transition(
        field="status", source=Status.ACTIVE, target=Status.INACTIVE,
        custom=dict(
            verbose="Disable user", tag="danger",
            app="users", model="user",
        )
    )
    def disable(self):
        pass