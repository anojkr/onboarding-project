import {grantingNotificationPermission} from "./register-subscriber.js"
import {createNotification} from "./requests.js"

const subscribe_notification_btn = document.getElementById("subscriber_notification_btn")
const notification_form = document.getElementById('notification-form')

subscribe_notification_btn.addEventListener('click', function(event) {
    event.preventDefault()
    grantingNotificationPermission()
});

notification_form.addEventListener('submit', function(event) {
    event.preventDefault()
    createNotification(notification_form)
});

