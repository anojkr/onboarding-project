import {getServerPublicKey, getBaseUrl, logError} from "./utils.js"

export function makeHttpRequest(method, url, headers, body) {
    return fetch(url, {
        method: method,
        body: body,
        headers: headers,
    }).then((response) => {
        return response.json()
    }).catch((error) => logError(error));
}

export function registerSubscriber(subscriptionData){
    console.log(subscriptionData)
    const subscription = subscriptionData.toJSON()
    let url = getBaseUrl() + '/api/v1/subscriber/'
    let body = JSON.stringify({
        endpoint:subscription["endpoint"],
        public_key:subscription["keys"]["p256dh"],
        auth_key:subscription["keys"]["auth"],
    })
    let headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    return makeHttpRequest('POST', url, headers, body)
        .then((responseJson) => {
            if (responseJson){
                alert("User subscribed successfully")
            } else {
                alert("Failed to subscribe user")
            }
            return responseJson
        }).catch(error => console.error('Error: ', error))
}

export function createNotification(notificationData){
    const formInputs = notificationData.elements
    let url = getBaseUrl() + '/api/v1/notification/'
    let body = JSON.stringify({
        title: formInputs['title'].value,
        description: formInputs['description'].value,
    })
    let headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    return makeHttpRequest('POST', url, headers, body)
    .then((responseJson) => {
            if (responseJson){
                alert("Notification created successfully")
            } else {
                alert("Failed to create notification")
            }
        notificationData.reset()
        return responseJson
    }).catch(error => console.error('Error: ', error))
}

export function getAllNotifications() {
    let url = getBaseUrl() + '/api/v1/notification/'
    let headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    return makeHttpRequest('GET', url, headers)
        .then((responseJson) => {
            return responseJson
        }).catch(error => console.error('Error: ', error))
}

export function sendNotification(notification_id) {
    let url = getBaseUrl() + '/api/v1/notification/send/?id='+notification_id
    let headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    return makeHttpRequest('POST', url, headers)
        .then((responseJson) => {
            if (responseJson['success']){
                alert("Notification is scheduled to be sent successfully.")
            } else {
                alert("Failed to send notification")
            }
            return responseJson
        }).catch(error => console.error('Error: ', error))
}