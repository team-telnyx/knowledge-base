---
title: Receiving Webhooks for Messaging
summary: Telnyx delivers webhooks to notify applications about messaging events in
  real time, including inbound messages, delivery status updates, read receipts, and
  suggestion responses. This page covers webhook event types, payload structures for
  SMS/MMS and RCS, signature verification, retry behavior, and best practices for
  production webhook handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
updated_at: 2026-08-05T14:01:55Z
---

# Receiving Webhooks for Messaging

*Part 2 of 6 — see also: [Part 1](receiving-webhooks-for-messaging--part-1.md), [Part 3](receiving-webhooks-for-messaging--part-3.md), [Part 4](receiving-webhooks-for-messaging--part-4.md), [Part 5](receiving-webhooks-for-messaging--part-5.md), [Part 6](receiving-webhooks-for-messaging--part-6.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Event examples

### Inbound message (`message.received`) — SMS

Triggered when your Telnyx number receives an SMS:

```json
{
  "data": {
    "event_type": "message.received",
    "id": "b301ed3f-1490-491f-995f-6e64e69674d4",
    "occurred_at": "2024-01-15T20:16:07.588+00:00",
    "payload": {
      "completed_at": null,
      "cost": { "amount": "0.0000", "currency": "USD" },
      "direction": "inbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "T-Mobile USA",
        "line_type": "long_code",
        "phone_number": "+13125550001"
      },
      "id": "84cca175-9755-4859-b67f-4730d7f58aa3",
      "media": [],
      "messaging_profile_id": "740572b6-099c-44a1-89b9-6c92163bc68d",
      "organization_id": "47a530f8-4362-4526-829b-bcee17fd9f7a",
      "parts": 1,
      "received_at": "2024-01-15T20:16:07.503+00:00",
      "record_type": "message",
      "sent_at": null,
      "tags": [],
      "text": "Hello from Telnyx!",
      "to": [
        {
          "carrier": "Telnyx",
          "line_type": "Wireless",
          "phone_number": "+17735550002",
          "status": "webhook_delivered"
        }
      ],
      "type": "SMS",
      "valid_until": null,
      "webhook_failover_url": null,
      "webhook_url": "https://example.com/webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Inbound message (`message.received`) — MMS

MMS messages include a `media` array with URLs, content types, and file sizes:

```json
{
  "media": [
    {
      "url": "https://media.telnyx.com/example-image.png",
      "content_type": "image/png",
      "sha256": "ab1c2d3e4f...",
      "size": 102400
    }
  ],
  "type": "MMS"
}
```

MMS media links expire after **30 days**. Download and store media files if you need long-term access.

### Inbound message (`message.received`) — RCS

When someone sends an RCS message to your agent, Telnyx delivers a `message.received` webhook to the URL configured on your RCS Agent. RCS supports richer inbound message types than SMS/MMS: text, file/image, location, and suggestion response.

Text:

```json
{
  "data": {
    "event_type": "message.received",
    "id": "b301ed3f-1490-491f-995f-6e64e69674d4",
    "occurred_at": "2024-12-09T20:16:07.588+00:00",
    "payload": {
      "body": {
        "text": "Hello from Telnyx!"
      },
      "direction": "inbound",
      "from": {
        "carrier": "T-Mobile USA",
        "line_type": "long_code",
        "phone_number": "+13125000000",
        "status": "webhook_delivered"
      },
      "id": "84cca175-9755-4859-b67f-4730d7f58aa3",
      "messaging_profile_id": "740572b6-099c-44a1-89b9-6c92163bc68d",
      "to": [
        {
          "agent_id": "e4448a5c0670c2a9",
          "agent_name": "My RCS Agent"
        }
      ],
      "type": "RCS"
    },
    "record_type": "event"
  }
}
```

File/Image — unlike MMS where media URLs are in `payload.media[]`, RCS file attachments are nested under `payload.body.user_file` with both a full-resolution `payload` and a `thumbnail`:

```json
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "body": {
        "user_file": {
          "payload": {
            "file_name": "photo.jpg",
            "file_size_bytes": 179099,
            "file_uri": "https://rcs-inbound.us-central-1.telnyxcloudstorage.com/rcs/.../photo.jpg",
            "mime_type": "image/jpeg"
          },
          "thumbnail": {
            "file_name": "photo_thumb.jpg",
            "file_size_bytes": 12074,
            "file_uri": "https://rcs-inbound.us-central-1.telnyxcloudstorage.com/rcs/.../photo_thumb.jpg",
            "mime_type": "image/jpeg"
          }
        }
      },
      "direction": "inbound",
      "type": "RCS"
    }
  }
}
```

Location:

```json
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "body": {
        "location": {
          "latitude": 38.24961321640261,
          "longitude": -85.78378468751907
        }
      },
      "direction": "inbound",
      "type": "RCS"
    }
  }
}
```

Suggestion response — when a user taps a suggested action or reply that you included in a previous message:

```json
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "body": {
        "suggestion_response": {
          "postback_data": "action_visit_store",
          "text": "Explore the online store"
        }
      },
      "direction": "inbound",
      "type": "RCS"
    }
  }
}
```

Use `postback_data` for programmatic routing and `text` for the user-visible label.

### Message sent (`message.sent`)

Triggered when an outbound message has been accepted by the downstream carrier:

```json
{
  "data": {
    "event_type": "message.sent",
    "id": "a1b2c3d4-5678-9012-abcd-ef1234567890",
    "occurred_at": "2024-01-15T21:32:13.596+00:00",
    "payload": {
      "completed_at": null,
      "cost": { "amount": "0.0051", "currency": "USD" },
      "direction": "outbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "Telnyx",
        "line_type": "Wireless",
        "phone_number": "+13125550001"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "media": [],
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "organization_id": "9d76d591-1b7d-405d-8c64-1320ee070245",
      "parts": 1,
      "received_at": "2024-01-15T21:32:13.552+00:00",
      "record_type": "message",
      "sent_at": "2024-01-15T21:32:13.596+00:00",
      "text": "Hello there!",
      "to": [
        {
          "carrier": "T-MOBILE USA, INC.",
          "line_type": "Wireless",
          "phone_number": "+13125550002",
          "status": "sent"
        }
      ],
      "type": "SMS",
      "valid_until": "2024-01-15T22:32:13.552+00:00",
      "webhook_url": "https://example.com/webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Delivery receipt (`message.finalized`)

Triggered when a message reaches a terminal delivery state:

```json
{
  "data": {
    "event_type": "message.finalized",
    "id": "4ee8c3a6-4995-4309-a3c6-38e3db9ea4be",
    "occurred_at": "2024-01-15T21:32:14.148+00:00",
    "payload": {
      "completed_at": "2024-01-15T21:32:14.148+00:00",
      "cost": {
        "amount": "0.0051",
        "currency": "USD"
      },
      "cost_breakdown": {
        "carrier_fee": { "amount": "0.00305", "currency": "USD" },
        "rate": { "amount": "0.00205", "currency": "USD" }
      },
      "direction": "outbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "Telnyx",
        "line_type": "Wireless",
        "phone_number": "+13125550001",
        "status": "webhook_delivered"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "media": [],
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "organization_id": "9d76d591-1b7d-405d-8c64-1320ee070245",
      "parts": 1,
      "received_at": "2024-01-15T21:32:13.552+00:00",
      "record_type": "message",
      "sent_at": "2024-01-15T21:32:13.596+00:00",
      "tags": ["tag-a", "tag-b"],
      "text": "Hello there!",
      "to": [
        {
          "carrier": "T-MOBILE USA, INC.",
          "line_type": "Wireless",
          "phone_number": "+13125550002",
          "status": "delivered"
        }
      ],
      "type": "SMS",
      "valid_until": "2024-01-15T22:32:13.552+00:00",
      "webhook_url": "https://example.com/webhooks",
      "tcr_campaign_billable": true,
      "tcr_campaign_id": "CNZO3VL",
      "tcr_campaign_registered": "REGISTERED"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### RCS delivery receipt (`message.finalized`)

RCS delivery receipts use the nested `body` structure and identify the sender as an agent:

```json
{
  "data": {
    "event_type": "message.finalized",
    "id": "4ee8c3a6-4995-4309-a3c6-38e3db9ea4be",
    "occurred_at": "2024-12-09T21:32:14.148+00:00",
    "payload": {
      "body": {
        "text": "Hello there!"
      },
      "completed_at": "2024-12-09T21:32:14.148+00:00",
      "cost": null,
      "direction": "outbound",
      "errors": [],
      "from": {
        "agent_id": "e4448a5c0670c2a9",
        "agent_name": "My RCS Agent"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "organization_id": "9d76d591-1b7d-405d-8c64-1320ee070245",
      "received_at": "2024-12-09T21:32:13.552+00:00",
      "record_type": "message",
      "sent_at": "2024-12-09T21:32:13.596+00:00",
      "tags": [],
      "to": [
        {
          "carrier": "T-MOBILE USA, INC.",
          "line_type": "Wireless",
          "phone_number": "+13125000000",
          "status": "delivered"
        }
      ],
      "type": "RCS",
      "valid_until": "2024-12-09T22:32:13.552+00:00",
      "webhook_failover_url": "",
      "webhook_url": "http://webhook.site/af3a92e7-e150-442c-9fe6-61658ce26b1a"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://webhook.site/af3a92e7-e150-442c-9fe6-61658ce26b1a"
  }
}
```

### RCS read receipt (`message.read`)

RCS uniquely supports read receipts — a `message.read` event is sent when the recipient opens and views your message. This is not available with SMS/MMS.

```json
{
  "data": {
    "event_type": "message.read",
    "id": "7bc4d2e1-3f89-4a12-b5c7-9e8d1a2f3b4c",
    "occurred_at": "2024-12-09T21:35:22.000+00:00",
    "payload": {
      "body": {
        "text": "Hello there!"
      },
      "direction": "outbound",
      "from": {
        "agent_id": "e4448a5c0670c2a9",
        "agent_name": "My RCS Agent"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "to": [
        {
          "phone_number": "+13125000000",
          "status": "read"
        }
      ],
      "type": "RCS"
    },
    "record_type": "event"
  }
}
```

Use read receipts to:

- **Track engagement** — Know which messages were actually read vs. just delivered
- **Trigger follow-ups** — Send a follow-up if a message was delivered but not read after a threshold
- **Analytics** — Calculate read rates for different message types or campaigns
- **UI updates** — Show "read" indicators in your chat interface (like blue checkmarks)

Not all devices or carriers support read receipts. A missing `message.read` event doesn't necessarily mean the message wasn't read — the user may have disabled read receipts on their device.
