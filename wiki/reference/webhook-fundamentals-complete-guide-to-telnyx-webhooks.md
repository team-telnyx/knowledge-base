---
title: Webhook Fundamentals - Complete Guide to Telnyx Webhooks
summary: Learn how to receive, handle, and secure webhooks from Telnyx APIs.
sources:
  - url: https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks
    content_hash: 82b01d96d809fba8f689aa469a509d69e652794a6fca82e8e57731474625fafa
updated_at: 2026-04-10T00:00:00Z
---

# Webhook Fundamentals - Complete Guide to Telnyx Webhooks

Learn how to receive, handle, and secure webhooks from Telnyx APIs. Complete guide covering setup, security, payload structure, and best practices for Voice, SMS, and Fax webhooks.

One application can provide another application with real-time updates via a webhook (also referred to as a web callback or HTTP push API). A webhook delivers data to other applications as it happens, meaning you get data immediately. In the past, APIs would typically need to poll for data very frequently to get it promptly. This makes webhooks much more efficient for both providers and consumers. The only drawback to webhooks is the difficulty of initially setting them up - [this](../runbooks/send-receive-mms.md) tutorial walks through how to consume webhooks.

Webhooks are sometimes referred to as "Reverse APIs," as they give you what amounts to an API spec, and you must design an API for the webhook to use. The webhook will make an HTTP request to your app (typically a POST), and you will then be charged with interpreting it.

Telnyx can send webhook events that notify your application any time an event happens on your account. This is especially useful for events like receiving an SMS or MMS message and getting feedback on Voice API events. The [messaging webhooks](../runbooks/receiving-webhooks-for-messaging.md) section goes into a bit more detail on how SMS and MMS webhooks work.

## Universal Webhook Behavior

Across all Telnyx services, webhooks follow consistent patterns:

* **Primary/Failover URLs**: Webhooks are delivered to the primary URL specified in your application configuration. If that URL doesn't respond successfully, the webhook is sent to the failover URL (if configured)
* **Response Requirements**: Your endpoint must return a 2xx HTTP status code to indicate successful receipt
* **Retry Logic**: Failed webhook deliveries are automatically retried with exponential backoff

## Webhook Setup Options

Choose one of the following options based on your development stage:

### Option A: Local Development with ngrok (Recommended for Testing)

1. Install ngrok following our [ngrok setup guide](ngrok.md).
2. Start your local webhook server (see example below).
3. Create a tunnel: `ngrok http 3000`.
4. Use the provided HTTPS URL (e.g., `https://abc123.ngrok.io/webhooks`).

### Option B: Quick Testing with webhook.site

1. Visit [webhook.site](https://webhook.site).
2. Copy your unique URL.
3. Use this for initial testing (note: this won't allow you to respond to webhooks).

### Option C: Production Deployment

Deploy your webhook handler to a cloud service like:

* AWS Lambda with API Gateway.
* Google Cloud Functions.
* Heroku.
* DigitalOcean App Platform.

## Webhook Delivery Characteristics

To minimize webhook delivery time across all services, Telnyx:

* **Does not guarantee delivery order**: Webhooks may arrive out of sequence
* **Implements automatic retries**: Failed deliveries are retried with exponential backoff
* **Delivers concurrently**: Multiple webhooks may arrive simultaneously

As a result, your application should be prepared to handle:

* **Out-of-order webhooks**: Events may not arrive in chronological order
* **Simultaneous webhooks**: Multiple events may be delivered at the same time
* **Duplicate webhooks**: The same event may be delivered more than once

## Handling Duplicate Events

Duplicate webhooks can cause your application to process the same event multiple times. To prevent this:

* **Use idempotency keys**: Include unique identifiers in your API requests (such as `command_id`, `idempotency_key`, etc.)
* **Implement deduplication**: Track processed webhook IDs to avoid duplicate processing
* **Design idempotent operations**: Ensure that processing the same event multiple times has no adverse effects

## Webhook Payload Structure

All Telnyx webhooks contain common identification fields:

* **Event ID**: Unique identifier for the webhook event
* **Timestamp**: When the event occurred
* **Resource IDs**: Identifiers that correlate the webhook with your resources (calls, messages, etc.)
* **Event Type**: Describes what action triggered the webhook

## Security & Protocols

### HTTP and HTTPS

* Unsecure (HTTP) URLs are allowed for webhooks.
* If HTTPS (TLS) is used, the certificate will be validated.

### Event type naming

Where possible, events map to the C(R)UD operations, but this is certainly not always be applicable.

* resource.created
* resource.updated
* resource.deleted

When the CRUD operations are not applicable, events will be named with past tense verbs.

* message.created
* message.deleted
* message.delivered
* message.received
* porting\_sub\_request.ported
* porting\_sub\_request.closed

## Webhook Structure

The top-level structure of the webhook will vary by product, but not by type of event received. For example, Voice API webhooks have a different top-level structure than Messaging webhooks however, the webhook structure across all Voice API commands is consistent. The `payload` of the webhook contains the most valuable information for your application.

### Voice API top-level structure

```json theme={null}
{
  "call_leg_id": "e97d8d4c-1a25-11cd-bc67-02620a0f6d42",
  "call_session_id": "e97da4f0-1a25-11bd-909f-02620a0f6d642",
  "event_timestamp": "2019-11-10T22:25:27.521992Z",
  "metadata": {
    "attempt": 1,
    "delivered_to": "https://www.example.com/callback",
    "event": {
      "event_type": "call.initiated",
      "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
      "occurred_at": "2019-11-10T22:25:27.521992Z",
      "payload": {
        ...
      },
      "record_type": "event"
    },
    "status": "delivered"
  },
  "name": "call.initiated",
  "organization_id": null,
  "type": "webhook",
  "user_id": "901dbc74-1597-4d15-aad2-xxxxxxxxxxxx"
}
```

| FIELD NAME        | DESCRIPTION                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `call_leg_id`     | ID that is unique to the call and can be used to correlate webhook events.                                                                                         |
| `call_session_id` | ID that is unique to the call session and can be used to correlate webhook events.                                                                                 |
| `event_timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime of when the event occurred.                                                                            |
| `attempt`         | The number of attempts made to deliver the webhook. Multiple attempts will occur if your application does not send Telnyx `HTTP 200 OK` on receipt of the webhook. |
| `delivered_to`    | URL that the webhook was sent to.                                                                                                                                  |
| `event_type`      | The type of event being delivered which also determines the structure of the `payload`.                                                                            |
| `id`              | Unique ID of the event.                                                                                                                                            |
| `occurred_at`     | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime of when the event occurred.                                                                            |
| `record_type`     | Will always be `event`.                                                                                                                                            |
| `status`          | Status of the webhook for debugging purposes.                                                                                                                      |
| `name`            | Event name.                                                                                                                                                        |
| `organization_id` | ID of the organization.                                                                                                                                            |

### Messaging top-level structure

```json theme={null}
{
"data": {
   "event_type": "message.finalized",
   "id": "4ef8c3a6-4195-4389-b3a6-38e3cb9eb4ae",
   "occurred_at": "2019-11-10T22:30:14.148+00:00",
   "payload": {
     ...
   },
   "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://www.example.com/messaging"
  }
}
```

| FIELD NAME     | DESCRIPTION                                                                                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_type`   | The type of event being delivered which also determines the structure of the `payload`.                                                                                                 |
| `id`           | Unique ID of the event.                                                                                                                                                                 |
| `occurred_at`  | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime of when the event occurred.                                                                                                 |
| `payload`      | The main data for the event. The structure is denoted by the `event_type`.                                                                                                              |
| `record_type`  | Will always be `event`.                                                                                                                                                                 |
| `attempt`      | The number of attempts made to deliver the webhook. Multiple attempts will occur if your application does not send Telnyx a `2xx` HTTP status code within 2s of receipt of the webhook. |
| `delivered_to` | URL that the webhook was sent to.                                                                                                                                                       |

## Example: Receiving a Webhook

When you place an incoming call to a number associated with your Voice API Application, you will receive a callback for the incoming call. It should look something like the JSON below:

```json theme={null}
{
  "data": {
    "record_type": "event",
    "event_type": "call.initiated",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "call_leg_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "from": "+1-202-555-0133",
      "to": "+12025550131",
      "direction": "incoming",
      "state": "parked"
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://example.com/webhooks"
  }
}
```

> **Note:** After pasting the above content, Kindly check and remove any new line added

<table>
  <tbody>
    <tr>
      <td>Field</td>
      <td>Value</td>
    </tr>

    <tr>
      <td>record\_type</td>
      <td>Description of the record.</td>
    </tr>

    <tr>
      <td>event\_type</td>
      <td>The type of event detected by the Telnyx system</td>
    </tr>

    <tr>
      <td>id</td>
      <td>unique id for the webhook</td>
    </tr>

    <tr>
      <td>occurred\_at</td>
      <td>ISO-8601 datetime of when event occured</td>
    </tr>

    <tr>
      <td>call\_control\_id</td>
      <td>call id used to issue commands via Voice API</td>
    </tr>

    <tr>
      <td>connection\_id</td>
      <td>Voice API App ID (formerly Telnyx connection ID) used in the call.</td>
    </tr>

    <tr>
      <td>call\_leg\_id</td>
      <td>ID that is unique to the call and can be used to correlate webhook events</td>
    </tr>

    <tr>
      <td>call\_session\_id</td>
      <td>ID that is unique to the call session and can be used to correlate webhook events. Call session is a group of related call legs that logically belong to the same phone call, e.g. an inbound and outbound leg of a transferred call.</td>
    </tr>

    <tr>
      <td>client\_state</td>
      <td>State received from a command</td>
    </tr>

    <tr>
      <td>from</td>
      <td>Number or SIP URI placing the call</td>
    </tr>

    <tr>
      <td>to</td>
      <td>Destination number or SIP URI of the call</td>
    </tr>

    <tr>
      <td>direction</td>
      <td>Whether the call is 'incoming' or 'outgoing'</td>
    </tr>

    <tr>
      <td>state</td>
      <td>Whether the call is in 'bridging' or 'parked' state</td>
    </tr>
  </tbody>
</table>

### Full Voice API example

```json theme={null}
{
  "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
  "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
  "event_timestamp": "2019-11-10T22:26:27.521992Z",
  "metadata": {
    "attempt": 1,
    "delivered_to": "https://www.example.com/callback",
    "event": {
      "event_type": "call.answered",
      "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
      "occurred_at": "2019-11-10T22:26:27.521992Z",
      "payload": {
        "call_control_id": "v2:F5_vIJVqrosogeY_2L_JhCEHd2Dh-x4xz7tROTbh34tg6Zsk4JJc-w",
        "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
        "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
        "client_state": null,
        "connection_id": "7267xxxxxxxxxxxxxx",
        "from": "+8005550199",
        "start_time": "2019-11-10T22:26:26.521992Z",
        "to": "+8005550100"
      },
      "record_type": "event"
    },
    "status": "delivered"
  },
  "name": "call.answered",
  "organization_id": null,
  "type": "webhook",
  "user_id": "901dbc74-1597-4d15-aad2-xxxxxxxxxxxx"
}
```

## Responding to a webhook

To acknowledge receipt of a webhook, your endpoint should return a `2xx` HTTP status code. Any other information returned in the request headers or request body is ignored. All response codes outside this range, including `3xx` codes, will indicate to Telnyx that you did not receive the webhook. URL redirection or a "Not Modified" response will be treated as a failure.

## Retries

Webhooks will be retried to each of the supplied URLs if your application does not respond in 2000 milliseconds.

## Best practices

If your webhook script performs complex logic or makes network calls, it's possible the script would timeout before Telnyx sees its complete execution. For that reason, you may want to have your webhook endpoint immediately acknowledge receipt by returning a `2xx` HTTP status code, and then perform the rest of its duties.

Webhook endpoints may occasionally receive the same event more than once. We advise you to guard against duplicated event receipts by making your event processing idempotent. One way of doing this is logging the events you've processed, and then not processing already-logged events. Additionally, we recommend verifying webhook signatures to confirm that received events are being sent from Telnyx.

## Webhook signing

Telnyx signs the webhook events it sends to clients so that the authenticity of the request can be verified. Webhook signing in API V2 uses public key encryption. Telnyx stores a public-private key pair and uses the private key to sign the payload. The public key is available to you so that you can verify the request.

The public key can be viewed in the [Mission Control Portal](https://portal.telnyx.com/#/api-keys/public-key).

The signature for the payload is calculated by building a string that is the combination of the timestamp of when the request was initiated, the pipe `|` character and the JSON payload. The signature is then `Base64` encoded.

```ruby theme={null}
Base64.encode64("#{timestamp}|#{payload}")
```

The signature (`Base64` encoded) and the timestamp (in Unix format) are assigned to the request headers `telnyx-signature-ed25519` and `telnyx-timestamp` respectively.

You can then use cryptographic libraries in your language of choice to verify the signature using the public key. Refer to the [Telnyx SDKs](https://developers.telnyx.com/development/sdk) for implementation examples in your preferred language.
