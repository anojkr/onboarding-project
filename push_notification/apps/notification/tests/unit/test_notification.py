from rest_framework.test import APITestCase
from ...services.notification_service import NotificationService
from django.urls import reverse


class TestNotificationAPI(APITestCase):

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
        notification = self.client.post(self.url, data=data, format='json')
        self.assertEqual(notification.data.get('title'), data.get('title'))

    def test_get_all_notification(self):
        notification = self.client.get(self.url)
        self.assertNotEqual(len(notification.data), 0)

    def test_get_notification_by_id(self):
        notification = NotificationService().get_by_id(self.notification_id)
        self.assertEqual(notification.id, self.notification_id)

    def test_delete_notification_by_id(self):
        response = self.client.delete(self.url+"?id={}".format(self.notification_id), data={}, format='json')
        self.assertEqual(response.data.get('success'), True)


