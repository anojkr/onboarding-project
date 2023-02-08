from rest_framework import serializers
from ..models.subscriber import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            "id",
            "endpoint",
            "public_key",
            "auth_key",
            "status",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]
