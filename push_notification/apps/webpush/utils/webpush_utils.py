from pywebpush import webpush
from pywebpush import WebPushException
import json
import datetime
from django.conf import settings


class WebPushRequestUtils(object):

    vapid_private_key = settings.VAPID['PRIVATE_KEY']
    vapid_claim_email = settings.VAPID['EMAIL']
    expiry_duration_in_minutes = settings.NOTIFICATION_EXPIRE_AFTER_MINS

    @classmethod
    def vapid_auth_token_claims(cls):
        return {"sub": f"mailto:{cls.vapid_claim_email}", "exp": cls._compute_vapid_auth_token_expiry()}

    @classmethod
    def _compute_vapid_auth_token_expiry(cls):

        def get_epoch_seconds(date_time):
            return int(date_time.timestamp())

        now = datetime.datetime.now()
        expire_after_mins = datetime.timedelta(minutes=cls.expiry_duration_in_minutes)
        expiry = now + expire_after_mins

        return get_epoch_seconds(expiry)

    @classmethod
    def send(cls, subscription_data, notification_data):
        try:
            response = webpush(
                subscription_info=subscription_data,
                data=json.dumps(notification_data),
                vapid_private_key=cls.vapid_private_key,
                vapid_claims=cls.vapid_auth_token_claims()
            )
            if response.ok:
                return response
            raise WebPushException("Web push error {}".format(response.text))
        except WebPushException as e:
            raise WebPushException("Web push error {}".format(e))

