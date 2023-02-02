from rest_framework import serializers
from ..models.notification import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
