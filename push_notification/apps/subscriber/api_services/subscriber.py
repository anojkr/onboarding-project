import logging
from ..services.subscriber_service import SubscriberService
from ..serializers.subscriber import SubscriberSerializer
from ..exceptions import SubscriberNotFound

logger = logging.getLogger(__name__)


class SubscriberAPIService(object):

    @classmethod
    def get_all_subscribers(cls):
        logger.info("SubscriberAPIService.get_all_subscribers")
        subscribers = SubscriberService().get_all_subscribers()
        return SubscriberSerializer(subscribers, many=True).data

    @classmethod
    def get_subscriber_by_id(cls, subscriber_id):
        try:
            logger.info("SubscriberAPIService.get_subscriber_by_id: subscription_id={}".format(subscriber_id))
            subscriber = SubscriberService().get_by_id(subscriber_id)
        except SubscriberNotFound as e:
            logger.error(
                "SubscriberAPIService.get_subscriber_by_id: exception={}, subscriber_id={}".format(e, subscriber_id))
            return None
        return SubscriberSerializer(subscriber).data

    @classmethod
    def create_subscriber(cls, subscriber_data):
        logger.info("SubscriberAPIService.create_subscriber: subscription_data={}".format(subscriber_data))
        subscriber = SubscriberService.create(subscriber_data)
        return SubscriberSerializer(subscriber).data

    @classmethod
    def get_active_subscriber(cls):
        logger.info("SubscriberAPIService.get_active_subscriber")
        subscribers = SubscriberService().get_active_subscribers()
        return SubscriberSerializer(subscribers, many=True).data

    @classmethod
    def unsubscribe_subscription(cls, subscriber_id):
        try:
            logger.info("SubscriberAPIService.unsubscribe_subscriber: subscriber_id={}".format(subscriber_id))
            return SubscriberService().unsubscribe(subscriber_id)
        except SubscriberNotFound as e:
            logger.error("SubscriberView.unsubscribe_subscriber: subscriber_id={}, exception={}".format(subscriber_id, e))
            return None

    @classmethod
    def get_subscriber_subscription_data(cls, subscriber_id):
        try:
            logger.info("SubscriberAPIService.get_subscriber_subscription_data: subscriber_id={}".format(subscriber_id))
            return SubscriberService().get_subscriber_subscription_data(subscriber_id)
        except SubscriberNotFound as e:
            logger.error("SubscriberView.unsubscribe_subscriber: subscriber_id={}, exception={}".format(subscriber_id, e))
            return None