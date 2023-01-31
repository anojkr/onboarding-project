from django.db import models


class SubscriberStatus(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNSUBSCRIBED = "UNSUBSCRIBED"
