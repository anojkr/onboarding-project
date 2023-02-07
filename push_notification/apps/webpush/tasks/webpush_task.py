import logging
from celery import shared_task
from pywebpush import WebPushException
from apps.subscriber.api_services.subscriber import SubscriberAPIService
from ..utils.webpush_utils import WebPushRequestUtils

logger = logging.getLogger(__name__)


@shared_task()
def task_send_notification(subscription_id, notification_data):
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
        logger.error(
            msg="Failed to send push notification, exception={} for subscriber_id={} with notification_data {}"
            .format(e, subscription_id, notification_data)
        )
