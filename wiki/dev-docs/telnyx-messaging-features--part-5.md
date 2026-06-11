---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-06-11T10:38:44Z
---

# Telnyx Messaging Features

*Part 5 of 5 — see also: [Part 1](telnyx-messaging-features--part-1.md), [Part 2](telnyx-messaging-features--part-2.md), [Part 3](telnyx-messaging-features--part-3.md), [Part 4](telnyx-messaging-features--part-4.md)*

Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky Sender, URL Shortening, Zapier integration, toll-free verification, and the full WhatsApp Business messaging workflow from embedded signup through template management and message sending.

## Sending WhatsApp Messages

All WhatsApp message types use `POST /v2/messages/whatsapp`. The `whatsapp_message` object's `type` field determines the message content.

Required fields: `from` (E.164), `to` (E.164), and `whatsapp_message` (object). The messaging profile is auto-resolved from the `from` number.

### Template Messages

Templates are required to start conversations outside the 24-hour window. Send by template name or by Telnyx UUID (`template_id`).

Template components map dynamic content to header, body, and button slots:

| Component `type` | `sub_type` | Use |
|---|---|---|
| `header` | — | Media or text for template header |
| `body` | — | Variable substitution in body text |
| `button` | `quick_reply` | Quick reply button payload |
| `button` | `url` | Dynamic URL suffix for CTA buttons |

Media headers support `image`, `document`, and `video` types with `{link, caption, filename}` structure.

### Text Messages

Send plain text within the 24-hour window. Body: 1–4096 bytes. Set `preview_url: true` to render link previews.

### Media Messages

Send images, videos, documents, audio, and stickers. Each media object requires exactly one of `link` (URL) or `id` (Meta media ID). Captions are optional (max 1024 bytes). Stickers and audio do not support captions. Only one media type per message.

### Location Messages

Share a location pin with latitude and longitude as strings. Latitude: -90 to 90; longitude: -180 to 180.

### Contact Messages

Share 1–257 contact cards with name, phones, and emails.

### Interactive Messages

| Type | Description |
|---|---|
| `button` | Up to 3 quick reply buttons |
| `cta_url` | Call-to-action URL button |
| `list` | Selectable list with sections and rows |
| `location_request_message` | Request the recipient's location |
| `carousel` | Scrollable cards with media and buttons |

When a recipient taps a button, you receive an inbound webhook with the button's `id`.

### Reactions

React to a received message with an emoji by providing the `message_id` and `emoji`.

### Reply Context

Reply to a specific message by including `context.message_id` with the original message's WhatsApp ID.

### Callback Tracking

Use `biz_opaque_callback_data` to attach tracking data returned in delivery webhooks.

### Validation Rules

| Constraint | Limit |
|---|---|
| Text body | 1–4096 bytes |
| Media caption | Max 1024 bytes |
| Header text | Max 1024 bytes |
| Contacts per message | 1–257 |
| Location latitude | -90 to 90 (string) |
| Location longitude | -180 to 180 (string) |
| Media per message | Exactly 1 |
| Media source | Exactly one of `link` or `id` |

### Error Handling

Common WhatsApp errors return code `40008`, a catch-all covering template issues (pending, rejected, paused, disabled) and delivery failures. Check template status in the Portal or via `GET /v2/whatsapp/message_templates`.
