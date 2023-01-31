from ..models.subscriber import Subscriber
from ..exceptions import SubscriberNotFound
from ..models.subscriber import SubscriberStatus


class SubscriberService(object):

    @classmethod
    def get_by_id(cls, subscriber_id):
        "Return subscriber details by given subscriber_id"
        try:
            subscriber = Subscriber.objects.get(id=subscriber_id)
        except Subscriber.DoesNotExist:
            raise SubscriberNotFound(subscriber_id=subscriber_id)
        return subscriber

    @classmethod
    def get_all_subscribers(cls):
        """Return all subscriber registered"""
        return Subscriber.objects.all()

    @classmethod
    def get_active_subscribers(cls):
        return Subscriber.objects.filter(status=SubscriberStatus.ACTIVE)

    @classmethod
    def create(cls, data):
        """Create subscriber with given data"""
        return Subscriber.objects.create(**data)

    @classmethod
    def unsubscribe(cls, subscriber_id):
        """Delete subscriber by given subscriber_id"""
        try:
            subscriber = Subscriber.objects.get(id=subscriber_id)
            cls.__update_subscriber_record(subscriber=subscriber,
                                           subscriber_data={"status": SubscriberStatus.UNSUBSCRIBED})
        except Subscriber.DoesNotExist:
            raise SubscriberNotFound(subscriber_id=subscriber_id)
        return True

    @classmethod
    def __update_subscriber_record(cls, subscriber, subscriber_data):
        """Update subscriber attributes"""
        for key, value in subscriber_data.items():
            setattr(subscriber, key, value)
        subscriber.save()
        return subscriber

    @classmethod
    def get_subscriber_subscription_data(cls, subscriber_id):
        """Return subscription-data for subscriber"""
        subscriber = cls.get_by_id(subscriber_id)
        return {
            "endpoint": subscriber.get("endpoint"),
            "keys": {
                "auth": subscriber.get("auth_key"),
                "p256dh": subscriber.get("public_key")
            }
        }
