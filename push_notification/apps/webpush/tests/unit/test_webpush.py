from rest_framework.test import APITestCase
from apps.notification.api_services.notification import NotificationAPIService


class TestWebPushAPI(APITestCase):
    def setUp(self):
        data = {
            "title": "Winter clearance sale discount",
            "description": "Enter coupon-code to avail 25% discount on apparel"
        }
        self.id = NotificationAPIService.create_notification(data).get('id')
        self.url = "/api/v1/notification/send/?id={}".format(self.id)

    def test_send_push_notification(self):
        response = self.client.post(self.url, data={}, format='json').data
        self.assertEqual(response.get('success'), True)

    def test_send_push_notification_with_invalid_notification_id(self):
        url = "/api/v1/notification/send/?id={}".format(-1)
        response = self.client.post(url, data={}, format='json').data
        self.assertEqual(response.get('success'), False)
