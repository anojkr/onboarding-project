import logging
from ..services.notification_service import NotificationService
from ..serializers.notification import NotificationSerializer
from ..exceptions import NotificationNotFound

logger = logging.getLogger(__name__)


class NotificationAPIService(object):

    @classmethod
    def create_notification(cls, data):
        logger.info("NotificationAPIService.create_notification: payload={}".format(data))
        serialized_data = NotificationSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        notification = NotificationService().create(data)
        return NotificationSerializer(notification).data

    @classmethod
    def get_all_notification(cls):
        logger.info("NotificationAPIService.get_all_notification")
        notifications = NotificationService().get_all_notification()
        return NotificationSerializer(notifications, many=True).data

    @classmethod
    def get_notification_by_id(cls, notification_id):
        try:
            logger.info("NotificationAPIService.get_all_notification: notification_id={}".format(notification_id))
            notification = NotificationService().get_by_id(notification_id)
        except NotificationNotFound as e:
            logger.error(
                "NotificationAPIService.get_notification_by_id: exception={}, notification_id={}"
                .format(e, notification_id)
            )
            return None
        return NotificationSerializer(notification).data

    @classmethod
    def delete_notification(cls, notification_id):
        try:
            notification = NotificationService().delete_by_id(notification_id=notification_id)
        except NotificationNotFound as e:
            logger.error(
                "NotificationAPIService.delete_notification: exception={}, notification_id={}"
                .format(e, notification_id)
            )
            return None
        return notification

