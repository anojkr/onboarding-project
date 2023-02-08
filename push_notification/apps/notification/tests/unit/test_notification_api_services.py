from rest_framework.test import APITestCase
from ...services.notification_service import NotificationService
from ...api_services.notification import NotificationAPIService
from django.urls import reverse

class TestNotificationAPIServices(APITestCase):

    def setUp(self):
        self.payload = {
            "title": "Winter discount sale started",
            "description": "Enter coupon-code to get flat 10% discount"
        }
        self.notification_id = NotificationService().create(self.payload).id
        self.url = reverse("notification")

    def test_create_notification(self):
        data = {
            "title": "Summer discount sale started",
            "description": "Enter coupon-code to get flat 10% discount"
        }
        notification = NotificationAPIService().create_notification(data)
        self.assertEqual(notification.get('title'), data.get('title'))

    def test_get_all_notification(self):
        notifications = NotificationAPIService().get_all_notification()
        self.assertNotEqual(len(notifications), 0)

    def test_get_notification_by_id(self):
        notification = NotificationAPIService().get_notification_by_id(self.notification_id)
        self.assertEqual(notification.get('id'), self.notification_id)

    def test_delete_notification_by_id(self):
        response = NotificationAPIService().delete_notification(self.notification_id)
        self.assertEqual(response, True)
