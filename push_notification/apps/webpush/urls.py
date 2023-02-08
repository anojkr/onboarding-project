from django.urls import path
from .views.webpush import WebPushView

urlpatterns = [
    path("notification/send/", WebPushView.as_view(), name="send_notification"),
]
