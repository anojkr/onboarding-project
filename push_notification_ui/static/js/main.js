import {grantingNotificationPermission} from "./register-subscriber.js"
import {createNotification, sendNotification} from "./requests.js"
import {getNotificationItems} from "./notifications.js"

const subscribe_notification_btn = document.getElementById("subscriber_notification_btn")
const notification_form = document.getElementById('notification-form')
const reload_notification = document.getElementById('refresh-notifications-btn')
const notification_items = document.getElementById('notifications-items')
const send_notification_btn = document.getElementById('send-notification-btn')

getNotificationItems(notification_items)

subscribe_notification_btn.addEventListener('click', function(event) {
    grantingNotificationPermission()
});

notification_form.addEventListener('submit', function(event) {
    event.preventDefault()
    createNotification(notification_form)
});

reload_notification.addEventListener('click', function(event) {
    getNotificationItems(notification_items)
})

send_notification_btn.addEventListener('click', function(event) {
    sendNotification(notification_items.options[notification_items.selectedIndex].id)
});
