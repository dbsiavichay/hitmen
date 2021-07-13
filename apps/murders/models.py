from django.db import models


class Hit(models.Model):
    class Status(models.IntegerChoices):
        ASSIGNED = 1, "Asignado"
        TAKEN = 2, "Tomado"
        SUCCESS = 2, "Existoso"
        FAILDED = 3, "Fallido"

    target = models.CharField(max_length=128, verbose_name="nombre del objetivo")
    description = models.TextField(verbose_name="descripción de la misión")
    hitman = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.ASSIGNED,
        verbose_name="estado"
    )