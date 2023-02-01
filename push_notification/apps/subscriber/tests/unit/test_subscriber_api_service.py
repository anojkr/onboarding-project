from rest_framework.test import APITestCase
from ....subscriber.services.subscriber_service import SubscriberService
from ....subscriber.api_services.subscriber import SubscriberAPIService


class TestSubscriberApiService(APITestCase):

    def setUp(self):
        self.payload = {
            "endpoint": "https://fcm.googleapis.com/fcm/send/c1Nsz7N4gO8:APA91bExyTlmumh-",
            "public_key": "BBckLc4pAr2pEwjx6Ho3tigyayn2XpuRc9JFHkQ-CghTevxk8HYmZAALlmChkfuHq6og9JlfDBPUAHBQ0OGwBiA",
            "auth_key": "RbNu_79slmjxSMZOmyYzgQ"
        }
        self.url = "/api/v1/subscriber/"
        self.subscriber_id = SubscriberService.create(self.payload).id

    def test_create_subscriber(self):
        subscriber = SubscriberAPIService.create_subscriber(self.payload)
        self.assertEqual(self.payload.get('endpoint'), subscriber.get('endpoint'))

    def test_get_subscriber_by_id(self):
        subscriber = SubscriberAPIService.get_subscriber_by_id(self.subscriber_id)
        self.assertEqual(subscriber.get('id'), self.subscriber_id)

    def test_get_all_subscriber(self):
        subscribers = SubscriberAPIService.get_all_subscribers()
        self.assertNotEqual(len(subscribers), 0)

    def test_unsubscribe_subscriber(self):
        response = SubscriberAPIService.unsubscribe_subscription(self.subscriber_id)
        self.assertEqual(response, True)
