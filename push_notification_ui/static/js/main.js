import {grantingNotificationPermission} from "./register-subscriber.js"
import {createNotification} from "./requests.js"
import {getNotificationItems} from "./notifications.js"

const subscribe_notification_btn = document.getElementById("subscriber_notification_btn")
const notification_form = document.getElementById('notification-form')
const reload_notification = document.getElementById('refresh-notifications-btn')
const notification_items = document.getElementById('notifications-items')

getNotificationItems(notification_items)

subscribe_notification_btn.addEventListener('click', function(event) {
    event.preventDefault()
    grantingNotificationPermission()
});

notification_form.addEventListener('submit', function(event) {
    event.preventDefault()
    createNotification(notification_form)
});

reload_notification.addEventListener('click', function(event) {
    event.preventDefault()
    getNotificationItems(notification_items)
})
