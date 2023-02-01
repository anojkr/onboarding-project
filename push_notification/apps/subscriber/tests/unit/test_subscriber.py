from rest_framework.test import APITestCase
from ....subscriber.services.subscriber_service import SubscriberService


class TestSubscriberAPI(APITestCase):
    def setUp(self):
        self.payload = {
            "endpoint": "https://fcm.googleapis.com/fcm/send/c1Nsz7N4gO8:APA91bExyTlmumh-",
            "public_key": "BBckLc4pAr2pEwjx6Ho3tigyayn2XpuRc9JFHkQ-CghTevxk8HYmZAALlmChkfuHq6og9JlfDBPUAHBQ0OGwBiA",
            "auth_key": "RbNu_79slmjxSMZOmyYzgQ"
        }
        self.url = "/api/v1/subscriber/"
        self.subscriber_id = SubscriberService.create(self.payload).id

    def test_create_subscriber(self):
        subscriber = self.client.post(self.url, data=self.payload, format='json').data
        self.assertEqual(self.payload.get('endpoint'), subscriber.get('endpoint'))

    def test_get_subscriber_by_id(self):
        subscriber = SubscriberService().get_by_id(self.subscriber_id)
        self.assertEqual(subscriber.id, self.subscriber_id)

    def test_get_all_subscribers(self):
        subscribers = self.client.get(self.url, format='json')
        self.assertNotEqual(len(subscribers.data), 0)

    def test_unsubscribe_subscriber(self):
        subscriber = self.client.delete(self.url, data={"subscriber_id": self.subscriber_id})
        self.assertEqual(subscriber.data.get('success'), True)
