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

*Part 3 of 4 — see also: [Part 1](telnyx-messaging-3--part-1.md), [Part 2](telnyx-messaging-3--part-2.md), [Part 4](telnyx-messaging-3--part-4.md)*

Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS messages with support for rich cards, carousels, scheduled delivery, smart encoding, short codes, and real-time webhooks for delivery tracking and inbound messages.

## Webhooks

Telnyx sends webhooks for messaging events in real time. Configure a webhook URL on your messaging profile via the Portal or API (`PATCH /v2/messaging_profiles/{id}`).

### Webhook URL hierarchy

Telnyx determines where to send webhooks using this priority:

1. **Per-message URLs** — `webhook_url` and `webhook_failover_url` in the send request body (outbound delivery receipts only)
2. **Messaging profile URLs** — Configured on the profile
3. **No webhook** — If neither is set, events are still logged in Message Detail Records

For RCS, inbound message webhooks are configured on the **RCS Agent** (not the messaging profile). Outbound status webhooks follow the same priority as SMS/MMS.

### Event types

| Event | Trigger | Direction |
|---|---|---|
| `message.received` | Inbound message arrives | Inbound |
| `message.sent` | Outbound message accepted by carrier | Outbound |
| `message.finalized` | Message reaches terminal state (delivered, failed) | Outbound |
| `message.read` | Recipient reads the message (RCS only) | Outbound |

### Delivery statuses

| Status | Description |
|---|---|
| `queued` | Queued on Telnyx's side |
| `sending` | Being sent to upstream carrier |
| `sent` | Sent to upstream carrier |
| `delivered` | Carrier confirmed delivery |
| `read` | Message read on device (RCS only) |
| `sending_failed` | Failed to send to carrier |
| `delivery_failed` | Carrier could not deliver |
| `delivery_unconfirmed` | No delivery confirmation received |

Read receipts (`message.read`) are unique to RCS. Use them for engagement tracking, follow-up triggers, analytics, and UI indicators. Not all devices or carriers support read receipts — a missing `message.read` event doesn't mean the message wasn't read.

### Signature verification

All webhooks are signed using **Ed25519** public key cryptography. Two headers are included:

| Header | Description |
|---|---|
| `telnyx-signature-ed25519` | Base64-encoded signature |
| `telnyx-timestamp` | Unix timestamp when signed |

The signature is computed over `{timestamp}|{json_payload}`. Get your public key from the Mission Control Portal under **Account Settings > Keys & Credentials > Public Key**. Reject webhooks where the timestamp is more than 5 minutes old to prevent replay attacks.

### Retry behavior

| Behavior | Detail |
|---|---|
| Timeout | Endpoint must respond within **2 seconds** (API v2) or 5 seconds (API v1) |
| Retries | Up to 3 attempts per URL with exponential backoff |
| Failover | If all retries fail, tries the failover URL (up to 3 more attempts) |
| Total attempts | Up to 6 (3 primary + 3 failover) |
| Success | Any `2xx` status code |

### IP allowlist

Allowlist the Telnyx webhook source subnet: `192.76.120.192/27`.

### Best practices

- **Respond immediately** — Return `200` before processing; offload heavy logic to a background queue.
- **Handle duplicates** — Use `data.id` as an idempotency key; the same webhook may be delivered more than once.
- **Handle out-of-order delivery** — Use `data.occurred_at` timestamps to sequence events.
- **Use HTTPS** — Always use TLS-encrypted endpoints in production.
- **Verify signatures** — Validate `telnyx-signature-ed25519` headers.
- **Implement SMS fallback** — When RCS delivery fails (`delivery_failed`), automatically fall back to SMS.

## Scheduled Messaging

Schedule SMS and MMS messages with the `send_at` parameter (ISO 8601 format, UTC).

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Reminder: Your appointment is tomorrow at 10 AM.",
    "send_at": "2026-02-15T14:30:00Z"
  }'
```

You can also use the dedicated endpoint `POST /v2/messages/schedule` with identical parameters.

**Constraints:**

- `send_at` must be at least **5 minutes** in the future
- `send_at` must be no more than **5 days** in the future
- Scheduling accuracy is up to **1 minute**
- Maximum of **1 million** scheduled messages at any time

**Retrieve:** `GET /v2/messages/{id}` (only messages from the last 10 days; use MDR reports for older messages).

**Cancel:** `DELETE /v2/messages/{id}` — the message must still be `scheduled` and the `send_at` time must be more than 1 minute in the future. Once a message begins sending, it cannot be cancelled.

Scheduled messages trigger the same webhooks (`message.sent`, `message.finalized`) as immediate messages when the scheduled time arrives.

## Smart Encoding

Smart encoding automatically replaces Unicode characters with visually similar GSM-7 characters, keeping messages in the more efficient GSM-7 encoding (160 chars/segment vs 70 chars/segment for UTF-16). A single smart quote or em dash can more than double messaging costs by forcing UTF-16.

Smart encoding applies to **SMS only**. MMS and RCS use UTF-8 by default and are not affected.

**Enable on a messaging profile:**

```bash
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{ "smart_encoding": true }'
```

Or toggle it in the Portal under Messaging > Messaging Profiles.

**Per-request override** with the `encoding` parameter:

| Value | Behavior |
|---|---|
| `auto` | Follow profile's `smart_encoding` setting (default) |
| `gsm7` | Force GSM-7; smart encoding applied; returns `400` if non-convertible characters exist |
| `ucs2` | Force UCS-2; smart encoding skipped entirely |

The request-level `encoding` parameter takes precedence over the profile setting.

**Response metadata** includes `smart_encoding_applied`, `final_encoding`, `segment_count`, `character_count`, `replaced_character_count`, and `length_change`. Webhooks return the original (pre-transformation) text.

**Precedence rules:**

| Profile `smart_encoding` | Request `encoding` | Behavior |
|---|---|---|
| `true` | *(not set)* | Smart encoding applied |
| `false` | *(not set)* | Smart encoding not applied |
| `true` or `false` | `auto` | Follows profile setting |
| `true` or `false` | `gsm7` | Smart encoding applied, must result in GSM-7 |
| `true` or `false` | `ucs2` | Smart encoding skipped |

**Common substitutions** include: curly quotes → straight quotes, em/en dashes → hyphens, ellipsis → three periods, no-break spaces → regular spaces, fullwidth characters → ASCII equivalents, and 200+ other Unicode-to-GSM-7 mappings. Tab characters (U+0009) convert to 7 spaces, which can significantly increase message length. Zero-width characters are removed entirely; if a message becomes empty after transformation, the API returns `400`.

**Edge cases:** Some substitutions increase message length (e.g., `…` → `...`). If a message contains both replaceable and non-replaceable characters (like emoji), smart encoding still applies substitutions — fewer Unicode characters means a shorter UTF-16 message. Extended GSM-7 characters (`~`, `^`, `|`, `\`, `{`, `}`, `[`, `]`) count as 2 characters each.
