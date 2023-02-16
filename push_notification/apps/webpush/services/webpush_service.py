import logging
from apps.subscriber.api_services.subscriber import SubscriberAPIService
from apps.notification.api_services.notification import NotificationAPIService
from ..tasks.webpush_task import task_send_notification
from ..exceptions import NotificationNotFound

logger = logging.getLogger(__name__)


class WebPushService(object):

    @classmethod
    def get_subscriber_ids(cls, subscribers):
        return [_.get('id') for _ in subscribers]

    @classmethod
    def send_notification_to_all_subscriber(cls, notification_id):
        notification_data = NotificationAPIService().get_notification_data(notification_id)
        if notification_data is None:
            raise NotificationNotFound(notification_id=notification_id)
        subscribers = SubscriberAPIService().get_active_subscriber()
        subscriber_ids = cls.get_subscriber_ids(subscribers)
        logger.info("subscriber-ids: [{}]".format(subscriber_ids))
        for subscriber_id in subscriber_ids:
            task_send_notification.delay(subscriber_id, notification_data)
