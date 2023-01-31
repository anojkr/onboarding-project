from django.urls import path
from .views.subscriber import SubscriberView

urlpatterns = [
    path("subscriber/", SubscriberView.as_view(), name="subscriber"),
]
