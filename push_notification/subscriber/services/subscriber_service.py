from subscriber.models.subscriber import Subscriber


class SubscriberService(object):

    def __init__(self, subscriber, serializer):
        self.subscriber = subscriber
        self.serializer = serializer

    def get_subscriber(self, pk=None):
        if pk is not None:
            queryset = self.subscriber.objects.get(id=pk)
            response = self.serializer(queryset, many=False)
            return response.data
        return None

    def get_all_subscriber(self):
        queryset = self.subscriber.objects.all()
        response = self.serializer(queryset, many=True)
        return response.data

    def add_subscriber(self, data):
        subscriber = self.serializer(data=data)
        if subscriber.is_valid(raise_exception=True):
            subscriber.save()
            return subscriber
        return None

    def remove_subscriber(self, pk=None):
        if pk is not None:
            queryset = self.subscriber.objects.get(id=pk)
            queryset.delete()
            return True
        return False

    def get_subscriber_subscription_data(self, subscriber: Subscriber):
        return {
            "endpoint": subscriber.get("endpoint"),
            "keys": {
                "auth": subscriber.get("auth_key"),
                "p256dh": subscriber.get("public_key")
            }
        }

    def get_all_subscriber_ids(self):
        return self.subscriber.objects.values_list("id", flat=True)
