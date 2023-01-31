import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.subscriber import SubscriberSerializer
from ..services.subscriber_service import SubscriberService
from ..exceptions import SubscriberNotFound

logger = logging.getLogger(__name__)


class SubscriberView(APIView):

    def get(self, request):
        subscribers = SubscriberService().get_all_subscribers()
        logger.info("SubscriberView:GET: All subscriber={}".format([_.id for _ in subscribers]))
        return Response(SubscriberSerializer(subscribers, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        logger.info("SubscriberView:POST: payload={}".format(request.data))
        serialized_data = SubscriberSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        subscriber = SubscriberService().create(serialized_data.validated_data)
        return Response(SubscriberSerializer(subscriber).data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            subscriber_id = request.data.get('subscriber_id', None)
            logger.info("SubscriberView.delete: Request to delete subscriber_id={}".format(subscriber_id))
            SubscriberService().unsubscribe(subscriber_id=subscriber_id)
        except SubscriberNotFound as e:
            logger.error("SubscriberView.delete: subscriber_id={}, exception={}".format(subscriber_id, e))
            return Response({"success": False, "reason": "invalid subscriber_id"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"success": True}, status=status.HTTP_200_OK)

