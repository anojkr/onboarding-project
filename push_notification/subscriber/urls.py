from django.urls import path
from subscriber.views.subscriber import SubscriberView

urlpatterns = [
    path("subscriber", SubscriberView.as_view(), name="subscriber"),
]
