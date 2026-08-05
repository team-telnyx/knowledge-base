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

*Part 6 of 6 — see also: [Part 1](receiving-webhooks-for-messaging--part-1.md), [Part 2](receiving-webhooks-for-messaging--part-2.md), [Part 3](receiving-webhooks-for-messaging--part-3.md), [Part 4](receiving-webhooks-for-messaging--part-4.md), [Part 5](receiving-webhooks-for-messaging--part-5.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Retry behavior and error handling

### Retry policy

| Behavior | Detail |
| --- | --- |
| **Timeout** | Your endpoint must respond within **2 seconds** (API v2) |
| **Retries** | Up to **3 attempts** per URL with exponential backoff |
| **Failover** | If all retries fail, Telnyx tries the failover URL (if configured) |
| **Total attempts** | Up to 6 total (3 primary + 3 failover) |
| **Success response** | Any `2xx` status code |
| **Failure response** | Any non-`2xx` response, including `3xx` redirects |

### Best practices for reliability

1. **Respond immediately** — Return `200` before processing the event. Offload heavy logic to a background queue.
2. **Handle duplicates** — Webhooks may be delivered more than once. Use the `data.id` field as an idempotency key.
3. **Handle out-of-order delivery** — Events may arrive in a different order than they occurred. Use `data.occurred_at` timestamps to sequence events.
4. **Use HTTPS** — Always use TLS-encrypted endpoints in production.
5. **Verify signatures** — Validate `telnyx-signature-ed25519` headers to prevent spoofing.
6. **Implement SMS fallback for delivery failures** — When an RCS message fails (`delivery_failed` status), automatically fall back to SMS to ensure message delivery. Check the `to[].status` field in `message.finalized` events.
7. **Use read receipts strategically** — Read receipts provide valuable engagement data but aren't guaranteed. Don't make critical business logic dependent on receiving a `message.read` event — some users disable read receipts.

## Webhook IP allowlist

If your server uses a firewall or ACL, allowlist the following Telnyx subnet:

| CIDR | Description |
| --- | --- |
| `192.76.120.192/27` | Telnyx webhook delivery IPs |

## Troubleshooting

**Webhooks not arriving**

1. **Check your messaging profile** — Confirm a webhook URL is configured in the [Portal](https://portal.telnyx.com/#/app/messaging) or via the API.
2. **Test your endpoint** — Send a test POST request with `curl` to ensure your server is accessible:

   ```bash
   curl -X POST https://your-endpoint.com/webhooks \
     -H "Content-Type: application/json" \
     -d '{"test": true}'
   ```
3. **Check ngrok** — If using ngrok, verify the tunnel is running and the URL matches your profile configuration.
4. **Check firewall** — Ensure `192.76.120.192/27` is allowlisted.
5. **Check Message Detail Records** — Events are logged regardless of webhook delivery. Check [Message Detail Records](message-detail-records.md) in the portal.

**Getting duplicate webhooks**

This is expected behavior. Telnyx may deliver the same webhook more than once, especially during retries. Track processed event IDs (`data.id`) and skip duplicates:

```javascript
const processedEvents = new Set();

app.post('/webhooks', (req, res) => {
  const eventId = req.body.data.id;
  if (processedEvents.has(eventId)) {
    return res.sendStatus(200); // Already processed
  }
  processedEvents.add(eventId);
  // Process event...
  res.sendStatus(200);
});
```

For production, use a persistent store (Redis, database) instead of in-memory sets.

**Webhooks arriving out of order**

Telnyx does not guarantee delivery order. For example, `message.finalized` may arrive before `message.sent`. Use the `data.occurred_at` timestamp to determine event sequence, and design your logic to handle any arrival order.

**Signature verification failing**

1. **Ensure you're reading the raw body** — Parse the signature against the raw request body, not a re-serialized JSON object.
2. **Check your public key** — Verify you're using the correct public key from the [Portal](https://portal.telnyx.com/#/app/api-keys).
3. **Check timestamp tolerance** — If you're rejecting stale timestamps, ensure your server clock is synchronized (NTP).

**Webhook timeouts (retries happening unexpectedly)**

Your endpoint must respond within **2 seconds**. If your processing takes longer:

- Return `200` immediately
- Process the event asynchronously (use a message queue like Redis, RabbitMQ, or SQS)

## Next steps

- [Send RCS Messages](send-rcs-messages.md) — Send rich cards, carousels, and suggested actions via RCS
- [RCS Capabilities](rcs-capabilities.md) — Check device support and RCS feature availability
- [RCS Getting Started](rcs-getting-started--part-1.md) — Set up your RCS Agent and start messaging
- [Receive Messages Tutorial](receive-messages-tutorial.md) — Step-by-step guide to building a webhook server
- [Send Your First Message](send-your-first-message.md) — Send SMS and MMS with the Messaging API
- [Webhook Fundamentals](webhook-fundamentals.md) — Platform-wide webhook concepts, signing, and retry behavior
- [Message Detail Records](message-detail-records.md) — Query historical message data and delivery statuses
