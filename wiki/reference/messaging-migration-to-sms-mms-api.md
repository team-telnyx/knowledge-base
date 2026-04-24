---
title: Messaging migration to SMS/MMS API
summary: Telnyx provides developers with an easy to follow messaging migration guide when upgrading from Api v1 to Api v2.
sources:
  - url: https://developers.telnyx.com/development/migration/messaging-migration-guide/index
    content_hash: 5b3417c4f1e93c1651329c2fa32d9a8db7ea02fad57848e631829252c23d1f2c
updated_at: 2026-04-10T00:00:00Z
---

# Messaging migration to SMS/MMS API

Telnyx provides developers with an easy to follow messaging migration guide when upgrading from Api v1 to Api v2. The guide covers all aspects of the migration process, including the differences between the two APIs and how to migrate your code.

The SMS/MMS API v2 has been designed to make migration from Messaging v1 smooth. This guide highlights the main changes to be aware of when migrating your Messaging application from API v1 to API v2.

SMS/MMS in API v2 offers the same great messaging functionality but with some changes aimed at making it even easier to have granular-level control over your messaging metrics and deliverability. For new Telnyx users, [server SDKs](https://developers.telnyx.com/development/sdk) are available in multiple languages to help you get started quickly. For users with an existing API v1 application, we'll cover the main changes you should make to migrate to our latest API version.

There are three main areas that require minor changes:

1. API v2 Authentication
2. Webhook Structure and Signature Validation
3. Endpoints for Sending Messages

## 1. API v2 Authentication

SMS/MMS API v2 utilizes a different authentication strategy that will require you to generate a new API key for your messaging application. You can do that easily via the [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/auth/v2).

Once you have logged into your Mission Control Portal account, in the left navigation click “Auth”. Then, ensure that Auth v2 is selected in the horizontal navigation.

<img alt="API Key View" />

Click “Create Key”. You will be presented with a pop-up reminding you to store your new API key securely. Click “Create” to confirm. You will then be presented with your new v2 key. You will not be able to see the full key again after this point.

Once a key has been successfully created, you can disable or delete it easily from the main Auth v2 page. Information on creation and recent usage of each key is also available.

## 2. Webhook Structure and Signature Validation

Next, let’s compare the webhook response for when a message is sent in both API v1 and v2 so that we can see the differences:

**API v1:**

```json theme={null}
{
  "type": "SMS",
  "sms_id": "403171cc-e934-4978-bada-2701bbdb69e7",
  "sms_gw_id": "403171cc-e934-4978-bada-2701bbdb69e7",
  "user_id": "d63fjl62-0003-4dab-7832-29b7b22628d8",
  "profile_id": "3dgnn65-7f81-4b71-b4g6-64a65ac29e8d",
  "created": 1588280767640,
  "updated": 1588280767727,
  "date_created": "2020-04-30T21:06:07.640000",
  "date_updated": "2020-04-30T21:06:07.727000",
  "to": "+18005550199",
  "from": "+18005550100",
  "cost": null,
  "currency": null,
  "direction": "outbound",
  "status": "sent",
  "delivery_status": "",
  "on_net": false,
  "carrier": "OMNIPOINT COMMUNICATIONS MIDWEST OPERATIONS LLC",
  "line_type": "Wireless",
  "errors": [],
  "body": {
    "text": "Hello, World!",
    "text_hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "coding": 0,
    "num_chars": 4,
    "num_bytes": 4,
    "bytes_hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "parts": 1
  }
}
```

**API v2:**

```json theme={null}
{
  "data": {
    "record_type": "event",
    "event_type": "message.sent",
    "id": "1f1243a9-93a5-48d1-bf4b-d680b03565a0",
    "occurred_at": "2020-04-30T20:58:39.421+00:00",
    "payload": {
      "id": "403171cc-e25d-45cc-96b2-f3c54cfc3747",
      "record_type": "message",
      "type": "SMS",
      "to": [
        {
          "carrier": "OMNIPOINT COMMUNICATIONS MIDWEST OPERATIONS LLC",
          "line_type": "Wireless",
          "phone_number": "+18005550199",
          "status": "sent"
        }
      ],
      "from": "+18005550100",
      "text": "Hello, World!",
      "completed_at": null,
      "cost": null,
      "direction": "outbound",
      "encoding": "GSM-7",
      "media": [],
      "parts": 1,
      "tags": [],
      "webhook_url": "https://hookb.in/G9J9pghfoeZJcpadWdQoxm",
      "webhook_failover_url": "",
      "valid_until": "2020-04-30T21:58:39.342+00:00",
      "sent_at": "2020-04-30T20:58:39.421+00:00",
      "received_at": "2020-04-30T20:58:39.342+00:00",
      "messaging_profile_id": "3edefe37-7f02-4b71-b2a6-64a65ac29e8d",
      "organization_id": "d63fjl62-0003-4dab-7832-29b7b22628d8",
      "errors": [],
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://hookb.in/G9J9pghfoeZJcpadWdQoxm"
  }
}
```

#### Data Object

Firstly, you will notice that the structure of the payload has changed. There is a top-level `data` object that contains all subsequent information about the webhook. You will also notice that the top level `created` field in API v1 has been renamed `occurred_at` - this is the time that the event occurred.

#### Event Type Naming Convention

The naming convention of the `event_type` field has also changed for SMS/MMS API v2. While the field names remain in `snake_case`, for `event_type` the call event being described will be in `dot.case` for all call events. Events can contain multiple dots to indicate a relationship.

For example, in API v1 when sending an SMS,  if the send is successful, your application will receive a webhook containing `"event_type":"delivered"`. In SMS/MMS API v2, your application would receive `"event_type": "message.finalized"` for this webhook event.

#### Enabling SMS/MMS API v2 Webhooks

API v2 webhook structures are not enabled by default. To begin receiving webhooks in the new format, you will need to update your [Messaging Profile](https://portal.telnyx.com/#/app/messaging) settings for any application you wish to migrate to SMS/MMS API v2.

<img alt="Messaging Webhook Version" />

#### Webhook Signatures

Each messaging webhook event that we send you will include a Telnyx signature. The signature allows you to validate that webhooks were not sent by a third-party.

While API v1 uses an HMAC with the SHA256 hash function to sign webhooks, SMS/MMS API v2 uses the [EdDSA](https://en.wikipedia.org/wiki/EdDSA) digital signature scheme with a public key.

In API v1, webhooks can be validated using information in the `X-Telnyx-Signature` header and the raw request payload of the webhook in bytes.

Webhook signing in SMS/MMS API V2 uses public key encryption. Telnyx stores a public-private key pair and uses the private key to sign the payload. The public key is available to you so that you can verify the request.

Your public key can be viewed in the [Mission Control Portal](https://portal.telnyx.com/#/app/account/public-key).

The signature for the payload is calculated by building a string that is the combination of the timestamp of when the request was initiated, the pipe `|` character and the JSON payload. The signature is then `Base64` encoded.

```
Base64.encode64("#{timestamp}|#{payload}")
```

The signature (`Base64` encoded) and the timestamp (in Unix format) are assigned to the request headers `telnyx-signature-ed25519` and `telnyx-timestamp` respectively.

You can then use cryptographic libraries in your language of choice to verify the signature using the public key. Refer to the [Telnyx SDKs](https://developers.telnyx.com/development/sdk) for implementation examples in your preferred language.

## 3. Endpoints for Messages

SMS/MMS API v2 requests have different endpoints to API v1 commands. The base URL for SMS/MMS API v2 is `https://api.telnyx.com/v2/`

The endpoints carry out the same functions, just at a different URL.

To send a message in API v1:
`https://sms.telnyx.com/messages`

To send a message in API v2:
`https://api.telnyx.com/v2/messages`

For further reading, view the [Messaging API Reference](https://developers.telnyx.com/api-reference/profiles/create-a-messaging-profile#create-a-messaging-profile) and the [quickstart guide](https://developers.telnyx.com/docs/messaging/messages/send-message).
