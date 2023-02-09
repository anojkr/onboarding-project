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
            console.log("Response")
            if (responseJson){
                alert("User subscribed successfully")
            } else {
                alert("Failed to subscribe user")
            }
            return responseJson
        }).catch(error => console.error('Error: ', error))
}