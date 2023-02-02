from ..exceptions import NotificationNotFound
from ..models.notification import Notification


class NotificationService(object):

    @classmethod
    def get_by_id(cls, notification_id):
        """Return notification details by given id"""
        try:
            notification = Notification.objects.get(id=notification_id)
        except Notification.DoesNotExist:
            raise NotificationNotFound(notification_id=notification_id)
        return notification

    @classmethod
    def create(cls, data):
        """Create notification with given data"""
        return Notification.objects.create(**data)

    @classmethod
    def delete_by_id(cls, notification_id):
        """Delete notification with given id"""
        notification = cls.get_by_id(notification_id)
        notification.delete()
        return True

    @classmethod
    def get_all_notification(cls):
        """Return all notification"""
        return Notification.objects.all()

    @classmethod
    def get_notification_data(cls, notification_id):
        """Return prepare notification data"""
        notification = cls.get_by_id(notification_id)
        return {
            "title": notification.get('title', None),
            "description": notification.get('description', None)
        }
