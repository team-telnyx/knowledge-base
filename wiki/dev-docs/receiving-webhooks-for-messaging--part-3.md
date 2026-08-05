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

*Part 3 of 6 — see also: [Part 1](receiving-webhooks-for-messaging--part-1.md), [Part 2](receiving-webhooks-for-messaging--part-2.md), [Part 4](receiving-webhooks-for-messaging--part-4.md), [Part 5](receiving-webhooks-for-messaging--part-5.md), [Part 6](receiving-webhooks-for-messaging--part-6.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Delivery statuses

The `to[].status` field in `message.finalized` events indicates the final delivery outcome:

| Status | Description |
| --- | --- |
| `queued` | Message is queued on Telnyx's side |
| `sending` | Message is being sent to an upstream carrier |
| `sent` | Message has been sent to the upstream carrier |
| `delivered` | Carrier has confirmed delivery to the recipient |
| `read` | Message read on the recipient's device (RCS only) |
| `sending_failed` | Telnyx failed to send the message to the carrier |
| `delivery_failed` | The carrier failed to deliver the message to the recipient |
| `delivery_unconfirmed` | No delivery confirmation was received from the carrier |

### Common delivery failure error codes

When a message fails, the `errors` array in the payload contains details:

```json
{
  "errors": [
    {
      "code": "40300",
      "title": "Destination number unreachable",
      "detail": "The destination number is not reachable on the carrier network.",
      "source": { "pointer": "/to/0/phone_number" }
    }
  ]
}
```

Common error codes:

| Code | Meaning |
| --- | --- |
| `40001` | Destination number invalid |
| `40002` | Destination number not in service |
| `40300` | Destination unreachable |
| `40008` | Message filtered by carrier |
| `40010` | Message blocked (spam/content filter) |
| `47000` | 10DLC campaign required |

For a complete list, see the [Error Codes reference](/development/api-fundamentals/api-errors).
