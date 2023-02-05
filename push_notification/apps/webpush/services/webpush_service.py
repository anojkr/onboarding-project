import logging
from pywebpush import WebPushException
from apps.subscriber.api_services.subscriber import SubscriberAPIService
from apps.notification.api_services.notification import NotificationAPIService
from ..utils.webpush_utils import WebPushRequestUtils
from ..tasks.webpush_task import task_send_notification

logger = logging.getLogger(__name__)


class WebPushService(object):

    @classmethod
    def get_notification_data(cls, notification):
        return {
            "title": notification.get('title', None),
            "description": notification.get('description', None)
        }

    @classmethod
    def get_subscriber_ids(cls, subscribers):
        return [_.get('id') for _ in subscribers]

    @classmethod
    def send_notification_to_all_subscriber(cls, notification_id):
        notification = NotificationAPIService().get_notification_by_id(notification_id)
        notification_data = cls.get_notification_data(notification)
        subscribers = SubscriberAPIService().get_all_subscribers()
        subscriber_ids = cls.get_subscriber_ids(subscribers)
        logger.info("subscriber-ids: [{}]".format(subscriber_ids))
        for subscriber_id in subscriber_ids:
            task_send_notification.delay(subscriber_id, notification_data)
