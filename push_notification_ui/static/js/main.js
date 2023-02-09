import {getServerPublicKey, getBaseUrl, logError} from "./utils.js"
import {registerSubscriber} from "./requests.js"
import {grantingNotificationPermission} from "./register-subscriber.js"

var subscribe_notification_btn = document.getElementById("subscriber_notification_btn")

subscribe_notification_btn.addEventListener('click', function(event) {
    event.preventDefault()
    var permission = grantingNotificationPermission()
    console.log(permission)
});

