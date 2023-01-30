from django.db import models
from common.models.base_entity import BaseEntity
import enum


class SubscriberStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DISCARDED = "DISCARDED"


class Subscriber(BaseEntity):
    endpoint = models.CharField("push service url", null=False, blank=False, max_length=255)
    public_key = models.CharField("subscription public-key", null=False, blank=False, max_length=255)
    auth_key = models.CharField("subscription auth-key", null=False, blank=False, max_length=255)
    status = models.CharField('status', null=False, blank=False, default=SubscriberStatus.ACTIVE, max_length=100)

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ("-created_at",)
