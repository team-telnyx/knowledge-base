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

*Part 1 of 6 — see also: [Part 2](receiving-webhooks-for-messaging--part-2.md), [Part 3](receiving-webhooks-for-messaging--part-3.md), [Part 4](receiving-webhooks-for-messaging--part-4.md), [Part 5](receiving-webhooks-for-messaging--part-5.md), [Part 6](receiving-webhooks-for-messaging--part-6.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Overview

Telnyx sends webhooks to notify your application about messaging events in real time — inbound messages, delivery status updates, errors, read receipts, and suggestion responses. Webhooks are HTTP `POST` requests with JSON payloads delivered to a publicly accessible HTTPS endpoint you configure.

## Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up) with a phone number assigned to a [messaging profile](messaging-profile.md) (and an [RCS Agent](rcs-agent.md) for RCS messaging)
- A publicly accessible HTTPS endpoint (or [ngrok](ngrok-setup.md) for local development)
- Your [API key](https://portal.telnyx.com/#/app/api-keys) and [public key](https://portal.telnyx.com/#/app/api-keys) (for signature verification)

## How webhook delivery works

1. **An event occurs** — A message is received by your number, or a sent message changes status (queued → sent → delivered).
2. **Telnyx sends a POST request** — An HTTP `POST` with a JSON payload is sent to your configured webhook URL.
3. **Your server responds** — Return a `2xx` status code within **2 seconds** to acknowledge receipt.
4. **Failover and retries** — If your server doesn't respond in time, Telnyx retries (up to 3 attempts per URL) and then tries your failover URL if configured.

### Webhook URL hierarchy

Telnyx determines where to send webhooks using this priority order:

1. **Per-message URLs** — `webhook_url` and `webhook_failover_url` in the send message request body
2. **Messaging profile URLs** — Configured on the messaging profile
3. **No webhook** — If neither is set, no webhook is delivered (events are still available in [Message Detail Records](message-detail-records.md))

For RCS, inbound message webhooks (`message.received`) are configured on the **RCS Agent**, while outbound status webhooks follow the per-request → messaging profile priority above.

## Webhook event types

| Event Type | Trigger | Direction |
| --- | --- | --- |
| `message.received` | An inbound SMS/MMS/RCS message arrives | Inbound |
| `message.sent` | An outbound message has been accepted and sent to the carrier | Outbound |
| `message.finalized` | An outbound message has reached a terminal state (delivered, failed, etc.) | Outbound |
| `message.read` | Recipient read the RCS message on their device | Outbound (RCS only) |

## Payload structure

All messaging webhooks share this top-level structure:

```json
{
  "data": {
    "event_type": "message.received",
    "id": "unique-event-id",
    "occurred_at": "2024-01-15T20:16:07.588+00:00",
    "payload": { },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

| Field | Description |
| --- | --- |
| `data.event_type` | The event type (`message.received`, `message.sent`, `message.finalized`, `message.read`) |
| `data.id` | Unique identifier for this webhook event |
| `data.occurred_at` | ISO 8601 timestamp of when the event occurred |
| `data.payload` | Message details (see examples below) |
| `data.record_type` | Always `"event"` |
| `meta.attempt` | Delivery attempt number (starts at 1) |
| `meta.delivered_to` | The URL this webhook was delivered to |

## RCS vs SMS/MMS webhooks

RCS webhooks have significant structural differences from SMS/MMS. Understanding these is critical when building a multi-channel messaging application.

| Feature | SMS/MMS | RCS |
| --- | --- | --- |
| **Message body** | `payload.text` (string) | `payload.body.text` (nested object) |
| **Media format** | `payload.media[]` with Telnyx URLs | `payload.body.user_file` with GCS URLs |
| **Sender identifier** | `from.phone_number` | `from.phone_number` (inbound) or `from.agent_id` + `from.agent_name` (outbound) |
| **Recipient identifier** | `to[].phone_number` | `to[].phone_number` (outbound) or `to[].agent_id` + `to[].agent_name` (inbound) |
| **Read receipts** | Not supported | ✅ `message.read` event |
| **Suggestion responses** | Not applicable | ✅ `body.suggestion_response` |
| **Location sharing** | Not supported | ✅ `body.location` |
| **JSON schema** | Telnyx messaging schema | Snake-case schema based on [Google RCS API](https://developers.google.com/business-communications/rcs-business-messaging/guides/build/messages/receive) |
| **Webhook URL source** | Messaging profile or per-request | RCS Agent config (inbound) + messaging profile (outbound status) |
