import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.webpush_service import WebPushService
from pywebpush import WebPushException
from ..exceptions import NotificationNotFound

logger = logging.getLogger(__name__)


class WebPushView(APIView):

    def post(self, request):
        notification_id = self.request.query_params.get('id')
        logger.info("Notification-id {}, attempting to send push notification to subscribers".format(id))
        try:
            WebPushService().send_notification_to_all_subscriber(notification_id=notification_id)
            return Response({"success": True}, status=status.HTTP_200_OK)
        except NotificationNotFound as e:
            logger.error("Attempt to send push-notification failed with exception={}".format(e))
            return Response({"success": False, "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except WebPushException as e:
            logger.error("Attempt to send push-notification failed with exception={}".format(e))
            return Response({"success": False, "reason": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
