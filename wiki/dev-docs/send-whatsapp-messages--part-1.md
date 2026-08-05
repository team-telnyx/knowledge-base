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

*Part 1 of 3 — see also: [Part 2](send-whatsapp-messages--part-2.md), [Part 3](send-whatsapp-messages--part-3.md)*

Send WhatsApp messages via the Telnyx API using `POST /v2/messages/whatsapp`. The same endpoint handles every message type — template, text, media, location, contacts, interactive, and reactions — with the `whatsapp_message.type` field selecting the payload shape. Templates are required to start conversations outside the 24-hour customer service window; text, media, and interactive messages are only allowed inside that window.

## Overview

All WhatsApp messages are sent through a single endpoint:

```
POST https://api.telnyx.com/v2/messages/whatsapp
```

Every request requires `from` (your WhatsApp-enabled phone number in E.164), `to` (recipient in E.164), and a `whatsapp_message` object whose `type` field selects the payload shape. An optional `webhook_url` field can be supplied for delivery status callbacks. The messaging profile is automatically resolved from the `from` number — you do not need to pass `messaging_profile_id`.

Supported `whatsapp_message.type` values: `text`, `template`, `image`, `video`, `document`, `audio`, `sticker`, `location`, `contacts`, `interactive`, `reaction`.

## Prerequisites

Before sending WhatsApp messages, ensure you have:

- **Telnyx Account** — [Sign up](https://telnyx.com/sign-up) and verify your account
- **Meta Business Manager Account** — Required for WhatsApp Business Platform access
- **WhatsApp Business Account (WABA)** — Connected via Telnyx's Embedded Signup
- **Verified phone number** — Added to your WABA and verified with Meta

WhatsApp Business Platform requires business verification through Meta's process. Personal WhatsApp accounts cannot send template messages via the API.

## Template Messages

Template messages are required to start conversations outside the 24-hour window. Templates must be pre-approved by Meta. Text, media, and interactive messages can only be sent within a 24-hour conversation window — the window opens when the recipient sends a message to the business number. Outside this window, use an approved template message to initiate the conversation.

Error code `40008` indicates the template could not be used for sending. Possible causes include: the template is still pending review, was rejected by Meta, has been paused due to quality issues, or was disabled. Check template status in the Telnyx Portal or via `GET /v2/whatsapp/message_templates`.

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

```javascript
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

| Component `type` | `sub_type` | Use |
| --- | --- | --- |
| `header` | — | Media or text for template header |
| `body` | — | Variable substitution in body text |
| `button` | `quick_reply` | Quick reply button payload |
| `button` | `url` | Dynamic URL suffix for CTA buttons |

### Media Header Template

To send a template with an image header:

```json
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

```javascript
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
