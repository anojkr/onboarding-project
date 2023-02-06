from django.db import models
from apps.common.models.base_entity import DateTimeEntity
from ..constants import SubscriberStatus


class Subscriber(DateTimeEntity):
    endpoint = models.CharField("push service url", null=False, blank=False, max_length=4096)
    public_key = models.CharField("subscriber public-key", null=False, blank=False, max_length=1024)
    auth_key = models.CharField("subscriber auth-key", null=False, blank=False, max_length=1024)
    status = models.CharField(choices=SubscriberStatus.choices, default=SubscriberStatus.ACTIVE, max_length=255)

    class Meta:
        verbose_name = "subscriber"
        verbose_name_plural = "subscribers"
        ordering = ("-created_at",)
