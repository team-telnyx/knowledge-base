---
title: RCS Messaging on Telnyx
summary: RCS (Rich Communication Services) on Telnyx enables rich, interactive messaging
  beyond SMS, with support for rich cards, carousels, suggested actions, AI-powered
  assistants, capability lookups, deeplinks, and carrier-specific throughput considerations.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
updated_at: 2026-08-05T13:55:58Z
---

# RCS Messaging on Telnyx

*Part 1 of 3 — see also: [Part 2](rcs-messaging-on-telnyx--part-2.md), [Part 3](rcs-messaging-on-telnyx--part-3.md)*

RCS (Rich Communication Services) on Telnyx enables rich, interactive messaging beyond SMS, with support for rich cards, carousels, suggested actions, AI-powered assistants, capability lookups, deeplinks, and carrier-specific throughput considerations.

## Overview

RCS (Rich Communication Services) is the modern successor to SMS, offering rich cards, carousels, suggested actions, and read receipts. Telnyx provides a full RCS stack including agent provisioning, capability lookups, deeplinks, AI Assistant integration, and adaptive fallback to SMS/MMS when RCS is unavailable.

## RCS Capabilities

Before sending RCS, you can check whether a recipient's device supports RCS and which features it supports. This lets you adapt your message format (rich card vs. plain text) and fall back to SMS when needed.

### Query a single number

Check RCS capabilities for a single phone number:

```
curl -s https://api.telnyx.com/v2/messaging/rcs/capabilities/{agent_id}/{phone_number} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The response includes a `features` array describing what the device supports. If `features` is empty or null, the device does not support RCS and you should fall back to SMS/MMS.

### Response examples

Full RCS support:

```json
{
  "data": {
    "record_type": "rcs.capabilities",
    "phone_number": "+15559876543",
    "agent_id": "your_agent_id",
    "agent_name": "Acme Bot",
    "features": [
      "ACTION_CREATE_CALENDAR_EVENT",
      "ACTION_DIAL",
      "ACTION_OPEN_URL",
      "ACTION_OPEN_URL_IN_WEBVIEW",
      "ACTION_SHARE_LOCATION",
      "ACTION_VIEW_LOCATION",
      "RICHCARD_CAROUSEL",
      "RICHCARD_STANDALONE"
    ],
    "status": "Success"
  }
}
```

Generic RCS (limited features):

```json
{
  "data": {
    "features": ["GENERIC_RCS_FEATURE"],
    "status": "Success"
  }
}
```

The device supports RCS but specific features couldn't be determined. Send basic RCS text and avoid rich cards.

No RCS support:

```json
{
  "data": {
    "features": null,
    "status": "RCS is disabled or agent is not provisioned for the carrier"
  }
}
```

Fall back to SMS/MMS for this recipient.

### Feature reference

| Feature | Description | Use for |
| --- | --- | --- |
| `RICHCARD_STANDALONE` | Single rich card support | Product cards, order updates |
| `RICHCARD_CAROUSEL` | Swipeable carousel cards | Product listings, menus |
| `ACTION_OPEN_URL` | Open URL button | Links to websites |
| `ACTION_OPEN_URL_IN_WEBVIEW` | Open URL in webview | In-app browsing |
| `ACTION_DIAL` | Phone call button | Click-to-call |
| `ACTION_VIEW_LOCATION` | View map location | Directions, store locator |
| `ACTION_SHARE_LOCATION` | Share user's location | Delivery tracking |
| `ACTION_CREATE_CALENDAR_EVENT` | Add calendar event | Appointment booking |
| `ACTION_COMPOSE` | Compose message | Message drafting |
| `GENERIC_RCS_FEATURE` | Basic RCS (details unknown) | Text-only RCS |

### Bulk capability query

Check up to 100 numbers at once to efficiently segment your audience:

```
curl -X POST https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "phone_numbers": ["+15551234567", "+15559876543", "+15550001111"]
  }'
```

RCS capability queries can be slow (several seconds per request). For time-sensitive applications, cache results and refresh periodically rather than querying before every message.

### Send with automatic fallback

Use capability queries to send the best possible message format. If the recipient supports rich cards and you have an image, send a rich card; if they support RCS only as text, send RCS text; otherwise fall back to SMS. The `fallback` field on the RCS send API lets you specify an SMS body and `from` number to use when RCS delivery fails.

## RCS Deeplinks

Deeplinks let users start an RCS conversation from a website, email, or QR code without having your number saved.

### Generate a deeplink

```
curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B15554443333&body=hello%20world' \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response:

```json
{
  "data": {
    "url": "sms:+18445550001?service_id=agent_id%40rbm.goog&body=hello%20world"
  }
}
```

The deeplink uses the standard Google RCS `sms:` scheme with an `@rbm.goog` address. You can pass an optional `phone_number` for SMS fallback and a `body` to prefill the message.

### Use deeplinks

- **Website button**: Embed the deeplink in an HTML `<a>` tag or button. The URL won't open directly in a browser — it must be triggered by a click.
- **QR code**: Convert the deeplink URL to a QR code for print materials, in-store signage, or business cards. Users scan with their camera to open an RCS conversation.
- **Email campaigns**: Include the deeplink in marketing emails as a CTA button. When tapped on Android with Google Messages, it opens the RCS conversation directly.

### Requirements

| Requirement | Details |
| --- | --- |
| **Device** | Android with Google Messages installed |
| **OS version** | `messages.android_20241029_00` or later |
| **Fallback** | Use `phone_number` parameter for non-RCS devices (opens SMS instead) |
