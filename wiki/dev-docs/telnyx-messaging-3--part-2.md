---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS
  messages with support for rich cards, carousels, scheduled delivery, smart encoding,
  short codes, and real-time webhooks for delivery tracking and inbound messages.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
updated_at: 2026-06-11T10:37:31Z
---

# Telnyx Messaging

*Part 2 of 4 — see also: [Part 1](telnyx-messaging-3--part-1.md), [Part 3](telnyx-messaging-3--part-3.md), [Part 4](telnyx-messaging-3--part-4.md)*

Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS messages with support for rich cards, carousels, scheduled delivery, smart encoding, short codes, and real-time webhooks for delivery tracking and inbound messages.

## RCS Capabilities

Check whether a recipient's device supports RCS before sending, so you can adapt message format and fall back to SMS when needed.

**Query a single number:**

```bash
curl -s https://api.telnyx.com/v2/messaging/rcs/capabilities/{agent_id}/{phone_number} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Responses:

- **Full RCS support** — `features` array includes capabilities like `RICHCARD_STANDALONE`, `RICHCARD_CAROUSEL`, `ACTION_OPEN_URL`, etc.
- **Generic RCS** — `features: ["GENERIC_RCS_FEATURE"]`. Device supports RCS but specific features are unknown; send basic text only.
- **No RCS support** — `features: null` with status `"RCS is disabled or agent is not provisioned for the carrier"`. Fall back to SMS/MMS.

### Feature reference

| Feature | Use for |
|---|---|
| `RICHCARD_STANDALONE` | Product cards, order updates |
| `RICHCARD_CAROUSEL` | Product listings, menus |
| `ACTION_OPEN_URL` | Links to websites |
| `ACTION_OPEN_URL_IN_WEBVIEW` | In-app browsing |
| `ACTION_DIAL` | Click-to-call |
| `ACTION_VIEW_LOCATION` | Directions, store locator |
| `ACTION_SHARE_LOCATION` | Delivery tracking |
| `ACTION_CREATE_CALENDAR_EVENT` | Appointment booking |
| `ACTION_COMPOSE` | Message drafting |
| `GENERIC_RCS_FEATURE` | Text-only RCS |

**Bulk capability query:** Check up to 100 numbers at once:

```bash
curl -X POST https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "phone_numbers": ["+15551234567", "+15559876543"]
  }'
```

RCS capability queries can be **slow** (several seconds per request). Cache results and refresh periodically rather than querying before every message.

### Adaptive sending pattern

Use capability queries to send the best format: if the device supports rich cards and you have an image, send a rich card; if RCS is enabled but no rich card support, send RCS text; otherwise send SMS directly. Include `fallback` in RCS requests for automatic SMS fallback on delivery failure.

## RCS Deeplinks

Deeplinks let users start an RCS conversation from a website, email, or QR code without having your number saved.

**Generate a deeplink:**

```bash
curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B15554443333&body=hello%20world' \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response:

```json
{ "data": { "url": "sms:+18445550001?service_id=agent_id%40rbm.goog&body=hello%20world" } }
```

The `phone_number` parameter provides a fallback for non-RCS devices (opens SMS instead). Omit it for RCS-only deeplinks.

**Usage patterns:**

- **Website button** — Embed the deeplink in an `<a>` tag. The URL won't open directly in a browser; it must be a user click.
- **QR code** — Convert the URL to a QR code for print materials or signage. Users scan with their camera.
- **Email campaigns** — Include as a CTA button. When tapped on Android with Google Messages, it opens the RCS conversation.

**Requirements:** Android with Google Messages (`messages.android_20241029_00` or later).

## Receiving Inbound Messages

When someone texts your Telnyx number, Telnyx sends an HTTP `POST` request to your configured webhook URL.

### SMS/MMS inbound webhooks

The `message.received` event has `payload.text` for the message body, `payload.media[]` for MMS attachments, and `payload.type` (`SMS` or `MMS`).

MMS media URLs expire after **30 days** — download and store media files immediately. Media downloads require authentication with your API key in the `Authorization` header.

Supported inbound MMS media types: `image/jpeg`, `image/png`, `image/gif`, `image/bmp`, `image/webp`, `video/mp4`, `video/3gpp`, `audio/mpeg`, `audio/ogg`, `audio/amr`, `application/pdf`, `text/vcard`, `text/calendar`.

### RCS inbound webhooks

RCS inbound messages have a different payload structure. The body is nested under `payload.body` as an object, and different message types use different keys:

| Type | Key in `payload.body` | Notes |
|---|---|---|
| Text | `body.text` | Plain text string |
| File/Image | `body.user_file` | Contains `payload` (full file) and `thumbnail` objects, each with `file_uri`, `file_name`, `mime_type`, `file_size_bytes` |
| Location | `body.location` | `latitude` and `longitude` |
| Suggestion response | `body.suggestion_response` | `text` (user-visible label) and `postback_data` (for programmatic routing) |

For outbound RCS messages, `from` includes `agent_id` and `agent_name`; for inbound, `from` is a `phone_number` and `to` contains `agent_id`/`agent_name`.

### Unified SMS + RCS handler

To handle both channels, normalize the payload differences. RCS uses `payload.body.text` (nested) while SMS uses `payload.text` (flat). RCS media is in `payload.body.user_file`; SMS/MMS media is in `payload.media[]`.
