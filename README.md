# Azure-EventGrid-WebHook-Validator
Autoresponder for echoing back the Azure Event Grid WebHook validation code.

When you register your own WebHook endpoint with Event Grid, it sends you a POST request with a simple validation code to prove endpoint ownership. Your app needs to respond by echoing back the validation code. Event Grid doesn't deliver events to WebHook endpoints that haven't passed the validation.

## Validation details
* At the time of event subscription creation/update, Event Grid posts a "SubscriptionValidationEvent" event to the target endpoint.
* The event contains a header value "Aeg-Event-Type: SubscriptionValidation".
* The event body has the same schema as other Event Grid events.
* The event data includes a "validationCode" property with a randomly generated string. For example, "validationCode: acb13…".
* The array contains only the validation event. Other events are sent in a separate request after you echo back the validation code.

## Usage
Just run it using Python3 interpreter. By default it runs on port 8080. You need to have a reverse proxy with SSL enabled (https is obligatory for Azure Event Grid WebHooks).
