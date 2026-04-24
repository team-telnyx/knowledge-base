---
title: Send WhatsApp Messages
summary: Send template, text, media, interactive, and location messages via the Telnyx WhatsApp API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
    content_hash: ac409d9bcb59576c875fca1ba5f802629a090f754453353471b6e8680109f29f
updated_at: 2026-04-10T00:00:00Z
---

# Send WhatsApp Messages

Send template, text, media, interactive, and location messages via the Telnyx WhatsApp API.

Send WhatsApp messages using `POST /v2/messages/whatsapp`. All message types use the same endpoint — the `whatsapp_message` object determines the message type.

```
POST https://api.telnyx.com/v2/messages/whatsapp
```

### Request Structure

Every request requires these fields:

| Field              | Type   | Required | Description                                |
| ------------------ | ------ | -------- | ------------------------------------------ |
| `from`             | string | Yes      | Your WhatsApp-enabled phone number (E.164) |
| `to`               | string | Yes      | Recipient phone number (E.164)             |
| `whatsapp_message` | object | Yes      | Message content — structure varies by type |
| `webhook_url`      | string | No       | URL for delivery status callbacks          |

> **Note:** The messaging profile is automatically resolved from the `from` number. You do not need to pass `messaging_profile_id`.

The `whatsapp_message` object must include a `type` field and the corresponding content object. Supported types: `text`, `template`, `image`, `video`, `document`, `audio`, `sticker`, `location`, `contacts`, `interactive`, `reaction`.

***

## Template Messages

Template messages are required to start conversations outside the 24-hour window. Templates must be pre-approved by Meta.

> **Warning:** Error code `40008` indicates the template could not be used for sending. Possible causes include: the template is still pending review, was rejected by Meta, has been paused due to quality issues, or was disabled. Check template status in the Telnyx Portal or via `GET /v2/whatsapp/message_templates`.

> **Note:** Text, media, and interactive messages can only be sent within a 24-hour conversation window. The window opens when the recipient sends a message to the business number. Outside this window, use an approved template message to initiate the conversation.

For comprehensive template creation guidance, see the [Message Template Best Practices](https://developers.telnyx.com/docs/messaging/whatsapp/message-templates) guide.

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages/whatsapp \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "from": "+15551234567",
      "to": "+15557654321",
      "whatsapp_message": {
        "type": "template",
        "template": {
          "name": "order_confirmation",
          "language": {
            "policy": "deterministic",
            "code": "en_US"
          },
          "components": [
            {
              "type": "body",
              "parameters": [
                {"type": "text", "text": "John"},
                {"type": "text", "text": "ORD-12345"}
              ]
            }
          ]
        }
      }
    }'
  ```

  ```python
  from telnyx import Telnyx
  client = Telnyx(api_key="YOUR_API_KEY")

  client.messages.send_whatsapp(
      from_="+15551234567",
      to="+15557654321",
      whatsapp_message={
          "type": "template",
          "template": {
              "name": "order_confirmation",
              "language": {"policy": "deterministic", "code": "en_US"},
              "components": [
                  {
                      "type": "body",
                      "parameters": [
                          {"type": "text", "text": "John"},
                          {"type": "text", "text": "ORD-12345"}
                      ]
                  }
              ]
          }
      }
  )
  ```

  ```javascript Node.js theme={null}
  import Telnyx from 'telnyx';
  const client = new Telnyx({apiKey: 'YOUR_API_KEY'});

  const message = await client.messages.sendWhatsapp({
    from: '+15551234567',
    to: '+15557654321',
    whatsapp_message: {
      type: 'template',
      template: {
        name: 'order_confirmation',
        language: { policy: 'deterministic', code: 'en_US' },
        components: [
          {
            type: 'body',
            parameters: [
              { type: 'text', text: 'John' },
              { type: 'text', text: 'ORD-12345' }
            ]
          }
        ]
      }
    }
  });
  ```

### Sending by Template ID

Instead of specifying `name` and `language`, you can reference a template by its Telnyx UUID (`template_id`). The name and language are resolved automatically from the database.

```bash
curl -X POST https://api.telnyx.com/v2/messages/whatsapp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "+15551234567",
    "to": "+15557654321",
    "whatsapp_message": {
      "type": "template",
      "template": {
        "template_id": "019cd44b-3a1c-781b-956e-bd33e9fd2ac6",
        "components": [
          {
            "type": "body",
            "parameters": [
              {"type": "text", "text": "John"},
              {"type": "text", "text": "ORD-12345"}
            ]
          }
        ]
      }
    }
  }'
```

  You can find a template's UUID by listing templates via `GET /v2/whatsapp/message_templates`. The `id` field in the response is the `template_id` you can use when sending.

### Template Components

Templates use `components` to pass dynamic content into header, body, and button slots:

| Component `type` | `sub_type`    | Use                                |
| ---------------- | ------------- | ---------------------------------- |
| `header`         | —             | Media or text for template header  |
| `body`           | —             | Variable substitution in body text |
| `button`         | `quick_reply` | Quick reply button payload         |
| `button`         | `url`         | Dynamic URL suffix for CTA buttons |

### Media Header Template

To send a template with an image header:

```json theme={null}
{
  "from": "+15551234567",
  "to": "+15557654321",
  "whatsapp_message": {
    "type": "template",
    "template": {
      "name": "promo_with_image",
      "language": {"policy": "deterministic", "code": "en_US"},
      "components": [
        {
          "type": "header",
          "parameters": [
            {"type": "image", "image": {"link": "https://example.com/promo.jpg"}}
          ]
        },
        {
          "type": "body",
          "parameters": [
            {"type": "text", "text": "20%"}
          ]
        }
      ]
    }
  }
}
```

Header parameters also support `document` and `video` types with the same `{link, caption, filename}` structure.

***

## Text Messages

Send plain text within the 24-hour conversation window. Body must be 1–4096 bytes.

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages/whatsapp \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "from": "+15551234567",
      "to": "+15557654321",
      "whatsapp_message": {
        "type": "text",
        "text": {
          "body": "Thanks for reaching out! How can we help?",
          "preview_url": false
        }
      }
    }'
  ```

  ```python
  from telnyx import Telnyx
  client = Telnyx(api_key="YOUR_API_KEY")

  client.messages.send_whatsapp(
      from_="+15551234567",
      to="+15557654321",
      whatsapp_message={
          "type": "text",
          "text": {
              "body": "Thanks for reaching out! How can we help?",
              "preview_url": False
          }
      }
  )
  ```

  ```javascript Node.js theme={null}
  import Telnyx from 'telnyx';
  const client = new Telnyx({apiKey: 'YOUR_API_KEY'});

  const message = await client.messages.sendWhatsapp({
    from: '+15551234567',
    to: '+15557654321',
    whatsapp_message: {
      type: 'text',
      text: {
        body: 'Thanks for reaching out! How can we help?',
        preview_url: false
      }
    }
  });
  ```

Set `preview_url: true` to render link previews when the message body contains a URL.

***

## Media Messages

Send images, videos, documents, audio, and stickers. Each media object requires exactly one of `link` (URL) or `id` (Meta media ID). Captions are optional and limited to 1024 bytes.

### Image

```json theme={null}
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

```json theme={null}
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

```json theme={null}
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

```json theme={null}
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

```json theme={null}
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

> **Note:** Stickers do not support captions. Audio does not support captions. Only one media type per message.

***

## Location Messages

Share a location pin. Latitude and longitude are passed as **strings** (decimal format).

```json theme={null}
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

***

## Contact Messages

Share one or more contact cards (1–257 contacts per message).

```json theme={null}
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

***

## Interactive Messages

Interactive messages let recipients tap buttons, select from lists, or open URLs. Supported `interactive.type` values:

| Type                       | Description                             |
| -------------------------- | --------------------------------------- |
| `button`                   | Up to 3 quick reply buttons             |
| `cta_url`                  | Call-to-action URL button               |
| `list`                     | Selectable list with sections and rows  |
| `location_request_message` | Request the recipient's location        |
| `carousel`                 | Scrollable cards with media and buttons |

### Quick Reply Buttons

```json theme={null}
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

```json theme={null}
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

```json theme={null}
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

```json theme={null}
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

***

## Reactions

React to a received message with an emoji.

```json theme={null}
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

***

## Reply Context

Reply to a specific message by including `context.message_id`:

```json theme={null}
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

***

## Callback Tracking

Use `biz_opaque_callback_data` to attach tracking data that will be returned in delivery webhooks:

```json theme={null}
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

***

## API Response

All message types return the same response structure:

```json theme={null}
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

***

## Validation Rules

| Constraint           | Limit                         |
| -------------------- | ----------------------------- |
| Text body            | 1–4096 bytes                  |
| Media caption        | Max 1024 bytes                |
| Header text          | Max 1024 bytes                |
| Contacts per message | 1–257                         |
| Location latitude    | -90 to 90 (string)            |
| Location longitude   | -180 to 180 (string)          |
| Media per message    | Exactly 1                     |
| Media source         | Exactly one of `link` or `id` |

***

## Error Handling

Common WhatsApp errors return error code `40008`. This is a catch-all code covering template issues (pending, rejected, paused, disabled) and delivery failures. For general API errors, see the [Error Codes Reference](../reference/api-error-codes.md).

> **Note:** Template, text, media, and interactive messages all use the same endpoint. The `type` field inside `whatsapp_message` determines which content object is required.

***

## Next Steps

  - [Quickstart](https://developers.telnyx.com/docs/messaging/whatsapp/quickstart) — Send your first WhatsApp message end-to-end

  - [Embedded Signup](https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup) — Set up your WhatsApp Business Account and verify your number

  - [Receiving Webhooks](receiving-webhooks-for-messaging.md) — Handle inbound messages and delivery status callbacks


## Related Pages

- [Send RCS Messages](../runbooks/send-rcs-messages.md)
- [Send Your First Message](../runbooks/send-your-first-message.md)
