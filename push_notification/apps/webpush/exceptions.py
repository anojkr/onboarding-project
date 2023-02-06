class NotificationNotFound(Exception):
    def __init__(self, notification_id=None):
        self.notification_id = notification_id
        self.message = "Notification not found"

    def __str__(self):
        return f"{self.notification_id} -> {self.message}"
