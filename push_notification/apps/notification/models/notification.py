from django.db import models
from apps.common.models.base_entity import DateTimeEntity


class Notification(DateTimeEntity):
    title = models.CharField("Title", null=False, blank=False, max_length=100)
    description = models.CharField("Description", null=False, blank=True, max_length=500)

    class Meta:
        unique_together = (
            "title",
            "description",
        )
        verbose_name = "notification"
        verbose_name_plural = "notifications"
        db_table = 'notifications'
        ordering = ("-created_at",)
