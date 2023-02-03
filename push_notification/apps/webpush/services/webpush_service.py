import logging
from pywebpush import WebPushException
from apps.subscriber.api_services.subscriber import SubscriberAPIService
from apps.notification.api_services.notification import NotificationAPIService
from ..utils.webpush_utils import WebPushRequestUtils

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
            cls.task_send_push_notification(subscriber_id, notification_data)

    @classmethod
    def task_send_push_notification(cls, subscriber_id, notification_data):
        WebPushService().send_notification(subscriber_id, notification_data)

    @classmethod
    def send_notification(cls, subscription_id, notification_data):
        subscriber_data = SubscriberAPIService().get_subscriber_subscription_data(subscription_id)
        logger.info(
            msg="Creating webpush request for subscriber_id={} with notification_data {}"
            .format(subscription_id, notification_data)
        )
        try:
            WebPushRequestUtils().send(
                subscription_data=subscriber_data,
                notification_data=notification_data
            )
            logger.info(
                msg="Successfully send push notification for subscriber_id={} with notification_data {}"
                .format(subscription_id, notification_data)
            )
        except WebPushException as e:
            logger.info(
                msg="Failed to send push notification, exception={} for subscriber_id={} with notification_data {}"
                .format(e, subscription_id, notification_data)
            )
