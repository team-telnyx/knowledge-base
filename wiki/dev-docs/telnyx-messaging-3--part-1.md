---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS
  messages with support for rich cards, carousels, scheduled delivery, smart encoding,
  short codes, and real-time webhooks for delivery tracking and inbound messages.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
  content_hash: 05da4e4eb5d10dd154487b8e67ca136f1bbcfbf7f7de156f06ac5e13014b0401
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
  content_hash: 2e1995853edc0ab2cb589197a11b54130f2c785a5f1baa7edc0ae1e4f375e818
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
  content_hash: b5ccb6bbd6241d1b677c7bfc53468f30f1d1a1d3123832a1d7c0b45fa92316e5
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
  content_hash: 728d80ce83761805e34536d2ec6f669da68942caa7e767339ceeecc06d24130d
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
  content_hash: 957bfe7bee137096df33ff98caf2cd713fd9c32f8a287bf2941b8da394f40e3a
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
  content_hash: 36359117d95c50cbce6d2af17942d3bddc30e6acacdbcd63170026928860963e
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
  content_hash: eeb2ca5acac5e5b3f49aa1a1dcdbeaa6ab91dfcde2f23ab0b6e62e28b3a14dc5
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
  content_hash: 0b42282c41f8b66ad4c7f2a13bf391d805b79cfab6caf28257929c8b0f15c77b
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
  content_hash: ee5892ca0fa233a524bc37d02292ee2a58073fb2bcc60ed7b4d0daa69bd049cd
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
  content_hash: 4c16c305d4d7cbccad5fa699312b3a47ec8c24c87536698f777232d6e2eac621
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
  content_hash: c3fe9b411598ec07a222db78bd9ce02104f758e1372a05ca524326e1146c4f40
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
  content_hash: 36255be2fe2cf05288b3248175bf48fe33ea2e9ecf886d05bb07a7e4296c68c3
updated_at: 2026-06-11T10:37:31Z
---

# Telnyx Messaging

*Part 1 of 4 — see also: [Part 2](telnyx-messaging-3--part-2.md), [Part 3](telnyx-messaging-3--part-3.md), [Part 4](telnyx-messaging-3--part-4.md)*

Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS messages with support for rich cards, carousels, scheduled delivery, smart encoding, short codes, and real-time webhooks for delivery tracking and inbound messages.

## Sending SMS and MMS

Send messages with `POST /v2/messages`. Phone numbers must be in E.164 format (`+15551234567`).

**SMS:**

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Hello, world!"
  }'
```

**MMS:** Include `media_urls` (up to 10 files, publicly accessible HTTPS URLs):

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Check out this image!",
    "subject": "Picture",
    "media_urls": ["https://example.com/image.jpg"]
  }'
```

MMS supported media types include JPEG, PNG, GIF, BMP, WebP (images, max 1 MB), MP4/3GP (video), MP3/AMR/WAV/OGG (audio), vCard, and PDF (max 600 KB each for non-image media). Telnyx automatically transcodes oversized media when possible. A `messaging_profile_id` can be included or inferred from the `from` number's assigned profile.

## Sending RCS Messages

RCS (Rich Communication Services) delivers app-like experiences in the native messaging app — rich cards, carousels, suggested replies, read receipts, typing indicators, and high-resolution media. RCS is currently supported on Android devices with Google Messages; Apple announced support in iOS 18.

Send RCS messages with `POST /v2/messages/rcs`. You need a verified RCS `agent_id` and a messaging profile.

**Text message:**

```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {
      "content_message": {
        "text": "Hi! How can we help you today?"
      }
    }
  }'
```

**Rich card:** Standalone cards display media, text, and action buttons:

```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {
      "content_message": {
        "rich_card": {
          "standalone_card": {
            "card_orientation": "VERTICAL",
            "card_content": {
              "title": "Order Shipped!",
              "description": "Your order #12345 is on its way.",
              "media": {
                "height": "MEDIUM",
                "content_info": { "file_url": "https://example.com/shipping.jpg" }
              },
              "suggestions": [
                { "action": { "text": "Track Order", "open_url_action": { "url": "https://example.com/track/12345" } } },
                { "reply": { "text": "Contact Support", "postback_data": "support_request" } }
              ]
            }
          }
        }
      }
    }
  }'
```

Card options: `card_orientation` (`VERTICAL`/`HORIZONTAL`), `thumbnail_image_alignment` (`LEFT`/`RIGHT`, horizontal only), `media.height` (`SHORT`/`MEDIUM`/`TALL`).

**Carousel:** Swipeable cards (2–10 cards, same `card_width`):

```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {
      "content_message": {
        "rich_card": {
          "carousel_card": {
            "card_width": "MEDIUM",
            "card_contents": [
              {
                "title": "Classic Burger",
                "description": "$8.99 — Our signature burger",
                "media": { "height": "MEDIUM", "content_info": { "file_url": "https://example.com/burger.jpg" } },
                "suggestions": [ { "action": { "text": "Order Now", "open_url_action": { "url": "https://example.com/order/burger" } } } ]
              }
            ]
          }
        }
      }
    }
  }'
```

**Suggested actions** appear as tappable buttons:

| Type | JSON key | Purpose |
|---|---|---|
| Suggested reply | `suggestions[].reply` | Quick reply with `postback_data` |
| Open URL | `suggestions[].action.open_url_action` | Open a website |
| Dial | `suggestions[].action.dial_action` | Initiate a phone call |
| View location | `suggestions[].action.view_location_action` | Open a map location |

**SMS fallback:** For non-RCS devices, include a `fallback` object:

```json
"fallback": {
  "from": "+15551234567",
  "text": "Your order #12345 has shipped!"
}
```

The `fallback.from` number must be a Telnyx number on your messaging profile with SMS capability. Fallback messages are plain text only.

### RCS vs SMS/MMS comparison

| Feature | RCS | SMS | MMS |
|---|---|---|---|
| Rich cards | ✅ | ❌ | ❌ |
| Carousels | ✅ | ❌ | ❌ |
| Suggested actions | ✅ | ❌ | ❌ |
| Read receipts | ✅ | ❌ | ❌ |
| Typing indicators | ✅ | ❌ | ❌ |
| Images/video | ✅ High-res | ❌ | ✅ Compressed |
| Character limit | None | 160/segment | None |
| Device support | Android (+ iOS 18) | Universal | Universal |
| Encoding | UTF-8 | GSM-7/UTF-16 | UTF-8 |

## RCS Agent Setup and Approval

RCS requires agent registration and carrier approval before sending to the general public.

1. **Submit your RCS Agent** — Contact Telnyx sales to start onboarding. Provide brand details, use case, and sample messages.
2. **Testing stage** — Telnyx moves your agent into testing. You can invite beta test numbers via the API and send test messages.
3. **Carrier approval** — Carriers review and approve your agent. This typically takes **4–6 weeks**.
4. **Go live** — Once approved, your agent can message any RCS-capable device.

You need a messaging profile and API key. Create a profile in the [Mission Control Portal](https://portal.telnyx.com/#/app/messaging), then copy the Messaging Profile ID.
