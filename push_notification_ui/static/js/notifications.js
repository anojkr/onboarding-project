import {getAllNotifications} from "./requests.js"

export function getNotificationItems(notification_items) {
    notification_items.innerHTML = ''
    getAllNotifications()
        .then(data => {
            data.forEach(notification => render(notification, notification_items))
        });
}

function render(notification, notification_items) {
    const option = document.createElement('option')
    option.id = notification.id
    option.appendChild(document.createTextNode(`${notification.title}`))
    notification_items.appendChild(option)
}