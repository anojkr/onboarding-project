import {getServerPublicKey, getBaseUrl, logError} from "./utils.js"
import {registerSubscriber} from "./requests.js"

export function grantingNotificationPermission() {
    if (Notification.permission === 'granted') {
        alert("You are already subscribed!")
        return Notification.permission
    }
    Notification.requestPermission()
    .then((permissionResult) => {
        if (permissionResult === 'granted') {
            console.log("Notification Permission granted!")
            return subscriberUser()
        } else {
            throw new Error("Notification permission not granted!")
        }
    }).catch((error) => logError(error))
}

function getServiceWorkerState(registration){
        var serviceWorker;
        if (registration.installing) {
            serviceWorker = registration.installing;
            console.log('Service worker installing');
        } else if (registration.waiting) {
            serviceWorker = registration.waiting;
            console.log('Service worker installed & waiting');
        } else if (registration.active) {
            serviceWorker = registration.active;
            console.log('Service worker active');
        }
        return serviceWorker
}

function subscriberUser() {
    registerServiceWorker().then((registration) => {
        var serviceWorker = getServiceWorkerState(registration)
        if (serviceWorker) {
            console.log("sw current state", serviceWorker.state);
            if (serviceWorker.state == "activated") {
                return subscriberPushNotification(registration)
            }
            serviceWorker.addEventListener("statechange", function(e) {
                console.log("sw statechange : ", e.target.state);
                if (e.target.state == "activated") {
                    console.log("Just now activated. now we can subscribe for push notification")
                        subscriberPushNotification(registration).then((pushSubscription) => {
                        registerSubscriber(pushSubscription)
                    });
                }
            });
        }
    }).then((pushSubscription) => {
        console.log('Received PushSubscription: ', JSON.stringify(pushSubscription));
        return registerSubscriber(pushSubscription)
    }).catch((error) => logError(error))
}

function registerServiceWorker() {
    return new Promise(function (resolve, reject) {
        if ('serviceWorker' in navigator && 'PushManager' in window) {
            return navigator.serviceWorker.register('./static/js/service-worker.js')
                .then((registration) => {
                    console.log('Service worker successfully registered!');
                    return resolve(registration)
                }).catch((err) => {
                    console.error('Unable to register service worker.', err);
                    return resolve(err)
                });
        } else {
            let msg = 'The browser does not support service workers or push messages.'
            console.error(msg);
            return reject(msg)
        }
    })
}

function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
}

function subscriberPushNotification(registration) {
    console.log(registration)
    const subscribeOptions = {
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(getServerPublicKey()),
    };
    return registration.pushManager.subscribe(subscribeOptions);
}