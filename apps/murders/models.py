from django.db import models
from django.utils.html import format_html

from django_fsm import FSMIntegerField, transition


class Hit(models.Model):
    class Status(models.IntegerChoices):
        ASSIGNED = 2
        FAILDED = 3
        COMPLETED = 4

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
        protected=True
    )

    @property
    def get_status(self):
        status = (
            (self.Status.ASSIGNED, "primary"), (self.Status.FAILDED, "danger"), (self.Status.COMPLETED, "success")
        )
        html = f'<span class="badge badge-{dict(status)[self.status]}">{dict(self.Status.choices)[self.status].upper()}</span>'
        return format_html(html)

    @property
    def get_status_label(self):
        return dict(self.Status.choices)[self.status]


    @transition(
        field="status", source=Status.ASSIGNED, target=Status.COMPLETED,
        custom=dict(
            verbose="Mark to completed", tag="success",
            app="murders", model="hit",
        )
    )
    def to_completed(self):
        pass

    @transition(
        field="status", source=Status.ASSIGNED, target=Status.FAILDED,
        custom=dict(
            verbose="Mark to failed", tag="danger",
            app="murders", model="hit"
        )
    )
    def to_failed(self):
        pass
            
