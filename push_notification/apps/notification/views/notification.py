from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.notification.services.notification_service import NotificationService
from ..exceptions import NotificationNotFound
from ..serializers.notification import NotificationSerializer
import logging

logger = logging.getLogger(__name__)


class NotificationView(APIView):

    def get(self, request):
        logger.info("NotificationView:POST: Get all notification")
        notifications = NotificationService().get_all_notification()
        return Response(NotificationSerializer(notifications, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        logger.info(msg="NotificationView:POST: payload:{}".format(request.data))
        serialized_data = NotificationSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        notification = NotificationService().create(serialized_data.validated_data)
        return Response(NotificationSerializer(notification).data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        notification_id = self.request.query_params.get('id')
        logger.info(msg="NotificationView:DELETE: notification_id={}".format(notification_id))
        try:
            NotificationService().delete_by_id(notification_id)
            return Response({"success": True}, status=status.HTTP_200_OK)
        except NotificationNotFound as e:
            logger.error(
                "NotificationView.NotificationView: notification_id={}, exception={}".format(notification_id, e))
            return Response({"success": False, "reason": "invalid notification_id"},
                            status=status.HTTP_400_BAD_REQUEST)
