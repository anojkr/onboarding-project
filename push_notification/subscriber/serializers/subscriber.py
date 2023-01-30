from rest_framework import serializers
from subscriber.models.subscriber import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
        read_only_fields = [
            "id",
            "created_at",
        ]
