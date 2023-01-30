import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from subscriber.models.subscriber import Subscriber
from subscriber.serializers.subscriber import SubscriberSerializer
from subscriber.services.subscriber_service import SubscriberService


class SubscriberView(APIView):

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.subscriber_service = SubscriberService(Subscriber, SubscriberSerializer)

    def get(self, request):
        subscribers = self.subscriber_service.get_all_subscriber()
        self.log.info("SubscriberView:GET: All subscriber:{}".format(subscribers))
        return Response(subscribers, status=status.HTTP_200_OK)

    def post(self, request):
        subscriber = self.subscriber_service.add_subscriber(request.data)
        self.log.info("SubscriberView:POST: payload:{}".format(request.data))
        return Response(subscriber, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        self.subscriber_service.remove_subscriber(pk=pk)
        return Response({"success": True}, status=status.HTTP_200_OK)
