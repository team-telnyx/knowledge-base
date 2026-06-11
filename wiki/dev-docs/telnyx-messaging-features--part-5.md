---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: d29aa01a72d9457e2c15bca36d1a114fad0d8a8fd2d7b721484dbeb7d7ea9663
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
  content_hash: b60693e817349ec8df4be29ac868e8661434934e8c3047b7acc28151d7d666ae
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
  content_hash: 4c488d1b1e1c401b24857bbee9b2dc380feeb3307e7bce07ecaa412fe56d304f
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
  content_hash: aad83743cb42ebbc89f6978b6f626af75781bd0d86f1dc76eec2c92463a1daa1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: 4252b4aba3308d22e312c4bfc31ff2bf8b9dad3363bc6fa0d6dd8cc1765f4379
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: 73f55d4531a2ff98fb6c9a7234dfb34e6b4429f9a1fdbc66b6c62d286cb29463
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
  content_hash: 2ed927e07af5e37713ddd6b340998cd8842b6303ef28e2428218537475463b8c
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
  content_hash: bb93e5d911b134f7064cd7997b82d901cca70eae5ee880c925434e16bb05f284
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
  content_hash: ed0efe6efb4a082f13f54662244ee901249886ad4eed11780a77d535efca8e89
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
  content_hash: abd0f4264c0b578171e98a4800bc241b283f1640a411eb55d283297c41637ae9
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
  content_hash: 6c916c387118b87a1258ad874d5461c0bf493edb141be63764cac4cb36a2cdcb
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
