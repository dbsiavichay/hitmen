"""User model."""
#  Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "usuario"
        

    def __str__(self):
        """Return username."""
        return self.email