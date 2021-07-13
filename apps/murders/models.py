from django.db import models

from django_fsm import FSMIntegerField, transition


class Hit(models.Model):
    class Status(models.IntegerChoices):
        ASSIGNED = 2, "Asignado"
        FAILDED = 3, "Fallido"
        COMPLETED = 4, "Completado"

    target = models.CharField(max_length=128, verbose_name="target name")
    description = models.TextField(verbose_name="mission description")
    assignee = models.ForeignKey(
        "users.User", null=True, on_delete=models.PROTECT,
        related_name="assignee_hits"
    )
    creator = models.ForeignKey(
        "users.User", null=True, on_delete=models.PROTECT,
        related_name="creator_hits"
    )
    status = FSMIntegerField(
        choices=Status.choices, default=Status.ASSIGNED,
        protected=True, verbose_name="estado"
    )

    def __iter__(self):
        for field in self._meta.fields:
            if not field.name in ("id", "status"):
                yield (field.verbose_name, field.value_to_string(self))