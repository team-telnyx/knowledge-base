---
title: Send WhatsApp Messages
summary: Send WhatsApp messages via the Telnyx API using `POST /v2/messages/whatsapp`.
  The same endpoint handles every message type — template, text, media, location,
  contacts, interactive, and reactions — with the `whatsapp_message.type` field selecting
  the payload shape. Templates are required to start conversations outside the 24-hour
  customer service window; text, media, and interactive messages are only allowed
  inside that window.
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-08-05T13:59:07Z
---

# Send WhatsApp Messages

*Part 2 of 3 — see also: [Part 1](send-whatsapp-messages--part-1.md), [Part 3](send-whatsapp-messages--part-3.md)*

Send WhatsApp messages via the Telnyx API using `POST /v2/messages/whatsapp`. The same endpoint handles every message type — template, text, media, location, contacts, interactive, and reactions — with the `whatsapp_message.type` field selecting the payload shape. Templates are required to start conversations outside the 24-hour customer service window; text, media, and interactive messages are only allowed inside that window.

## Media Messages

Send images, videos, documents, audio, and stickers. Each media object requires exactly one of `link` (URL) or `id` (Meta media ID). Captions are optional and limited to 1024 bytes.

### Image

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "image",
    "image": {
      "link": "https://example.com/receipt.png",
      "caption": "Your receipt for order #12345"
    }
  }
}
```

### Document

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "document",
    "document": {
      "link": "https://example.com/invoice.pdf",
      "filename": "invoice_12345.pdf",
      "caption": "Invoice for March 2026"
    }
  }
}
```

### Video

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "video",
    "video": {
      "link": "https://example.com/tutorial.mp4",
      "caption": "Setup walkthrough"
    }
  }
}
```

### Audio

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "audio",
    "audio": {
      "link": "https://example.com/voicenote.ogg"
    }
  }
}
```

### Sticker

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "sticker",
    "sticker": {
      "link": "https://example.com/sticker.webp"
    }
  }
}
```

Stickers do not support captions. Audio does not support captions. Only one media type per message.

## Location Messages

Share a location pin. Latitude and longitude are passed as **strings** (decimal format).

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "location",
    "location": {
      "latitude": "40.7128",
      "longitude": "-74.0060",
      "name": "Telnyx HQ",
      "address": "311 W 43rd St, New York, NY"
    }
  }
}
```

Latitude must be between -90 and 90. Longitude must be between -180 and 180.

## Contact Messages

Share one or more contact cards (1–257 contacts per message).

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "contacts",
    "contacts": [
      {
        "name": {
          "formatted_name": "Jane Smith",
          "first_name": "Jane",
          "last_name": "Smith"
        },
        "phones": [
          {"phone": "+15559876543", "type": "WORK"}
        ],
        "emails": [
          {"email": "jane@example.com", "type": "WORK"}
        ]
      }
    ]
  }
}
```

## Interactive Messages

Interactive messages let recipients tap buttons, select from lists, or open URLs. Supported `interactive.type` values:

| Type | Description |
| --- | --- |
| `button` | Up to 3 quick reply buttons |
| `cta_url` | Call-to-action URL button |
| `list` | Selectable list with sections and rows |
| `location_request_message` | Request the recipient's location |
| `carousel` | Scrollable cards with media and buttons |

### Quick Reply Buttons

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "interactive",
    "interactive": {
      "type": "button",
      "body": {"text": "Would you like to schedule a callback?"},
      "action": {
        "buttons": [
          {"type": "reply", "reply": {"id": "yes_callback", "title": "Yes, call me"}},
          {"type": "reply", "reply": {"id": "no_thanks", "title": "No thanks"}}
        ]
      }
    }
  }
}
```

When a recipient taps a button, you receive an inbound webhook with the button's `id` in the payload.

### CTA URL Button

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "interactive",
    "interactive": {
      "type": "cta_url",
      "body": {"text": "Track your shipment"},
      "action": {
        "name": "cta_url",
        "parameters": {
          "display_text": "Track Order",
          "url": "https://example.com/track/12345"
        }
      }
    }
  }
}
```

### List Messages

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "interactive",
    "interactive": {
      "type": "list",
      "body": {"text": "Select a support topic:"},
      "action": {
        "button": "Choose topic",
        "sections": [
          {
            "title": "Account",
            "rows": [
              {"id": "billing", "title": "Billing", "description": "Payment and invoice questions"},
              {"id": "access", "title": "Account Access", "description": "Login and permissions"}
            ]
          },
          {
            "title": "Technical",
            "rows": [
              {"id": "api", "title": "API Issues", "description": "Integration and endpoint help"},
              {"id": "webhooks", "title": "Webhooks", "description": "Delivery and configuration"}
            ]
          }
        ]
      }
    }
  }
}
```

### Location Request

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "interactive",
    "interactive": {
      "type": "location_request_message",
      "body": {"text": "Share your location so we can find the nearest store."},
      "action": {"name": "send_location"}
    }
  }
}
```

## Reactions

React to a received message with an emoji.

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "reaction",
    "reaction": {
      "message_id": "wamid.ABGGFlA5FpafAgo6tHcNmNjXhvRm",
      "emoji": "👍"
    }
  }
}
```

## Reply Context

Reply to a specific message by including `context.message_id`:

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "text",
    "context": {
      "message_id": "wamid.ABGGFlA5FpafAgo6tHcNmNjXhvRm"
    },
    "text": {
      "body": "Thanks for your order! It will ship tomorrow."
    }
  }
}
```

## Callback Tracking

Use `biz_opaque_callback_data` to attach tracking data that will be returned in delivery webhooks:

```json
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "text",
    "biz_opaque_callback_data": "order_12345_confirmation",
    "text": {
      "body": "Your order has been confirmed."
    }
  }
}
```

## API Response

All message types return the same response structure:

```json
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "type": "WHATSAPP",
    "from": {"phone_number": "+15551234567"},
    "to": [{"phone_number": "+15557654321", "status": "queued"}],
    "webhook_url": "https://example.com/webhooks"
  }
}
```

## Validation Rules

| Constraint | Limit |
| --- | --- |
| Text body | 1–4096 bytes |
| Media caption | Max 1024 bytes |
| Header text | Max 1024 bytes |
| Contacts per message | 1–257 |
| Location latitude | -90 to 90 (string) |
| Location longitude | -180 to 180 (string) |
| Media per message | Exactly 1 |
| Media source | Exactly one of `link` or `id` |

## Error Handling

Common WhatsApp errors return error code `40008`. This is a catch-all code covering template issues (pending, rejected, paused, disabled) and delivery failures. For general API errors, see the [Error Codes Reference](https://developers.telnyx.com/docs/development/api-fundamentals/api-errors).

Template, text, media, and interactive messages all use the same endpoint. The `type` field inside `whatsapp_message` determines which content object is required.
