---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
updated_at: 2026-06-11T10:38:14Z
---

# Telnyx Messaging

*Part 3 of 5 — see also: [Part 1](telnyx-messaging-2--part-1.md), [Part 2](telnyx-messaging-2--part-2.md), [Part 4](telnyx-messaging-2--part-4.md), [Part 5](telnyx-messaging-2--part-5.md)*

Telnyx Messaging provides APIs and infrastructure for sending and receiving SMS, MMS, and RCS messages globally. This page covers phone number configuration, messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international compliance, and RCS with AI integration.

## Rate Limiting and Queuing

Rate limits control message delivery throughput. They apply at both the account level and the per-sender level.

### Account-level limits

| Message Type | Default Rate Limit | Max Queue Length |
|---|---|---|
| SMS | 50 messages/second | 720,000 |
| MMS | 15 messages/second | 216,000 |
| RCS | 1 message/second | 14,400 |

### Per-sender limits

| Sender Type | Rate Limit | Per | Max Queue Length |
|---|---|---|---|
| Long Code | 0.1 MPS | Number | 1,440 |
| Toll-Free | 20 MPS | Number | 288,000 |
| Short Code | 1,000 MPS | Number | 14,400,000 |
| Alphanumeric | 0.1 MPS | Sender ID | 1,440 |

The default long code rate applies to non-US destinations. For US long codes, throughput is determined by 10DLC campaign registration.

### 10DLC carrier throughput

**AT&T** assigns throughput per campaign based on message class and vetting score:

| Message Class | Use Case | Vetting Score | SMS TPM | MMS TPM |
|---|---|---|---|---|
| A | Standard (Dedicated) | 75–100 | 4,500 | 2,400 |
| B | Standard (Mixed/Marketing) | 75–100 | 4,500 | 2,400 |
| C | Standard (Dedicated) | 50–74 | 2,400 | 1,200 |
| D | Standard (Mixed/Marketing) | 50–74 | 2,400 | 1,200 |
| E | Standard (Dedicated) | 1–49 | 240 | 150 |
| F | Standard (Mixed/Marketing) | 1–49 | 240 | 150 |
| T | Low Volume Mixed | — | 75 | 50 |
| K | Political | — | 4,500 | 2,400 |
| P | Charity | — | 2,400 | 1,200 |
| S | Social | — | 9,000 | 2,400 |
| X | Emergency/Public Safety | — | 4,500 | 2,400 |
| W | Sole Proprietor | — | 15 | 50 |
| G | Proxy | — | 60/number | 50/number |
| N | Agents and Franchises | — | 60/number | 50/number |

**T-Mobile** assigns daily message caps at the brand level:

| Brand Tier | Vetting Score | Daily Cap |
|---|---|---|
| Top | 75–100 | 200,000 |
| High Mid | 50–74 | 40,000 |
| Low Mid | 25–49 | 10,000 |
| Low | 1–24 | 2,000 |

Unvetted brands default to Low tier. Sole Proprietor campaigns have a 1,000 daily cap.

**Verizon** has not published specific throughput limits but uses content filtering for 10DLC traffic.

### Queuing

When you send faster than rate limits allow, excess messages are queued (up to 4 hours, FIFO order). Max queue length = rate limit × 14,400 seconds. Both sender-level and account-level queues apply simultaneously. When the more restrictive queue fills, additional messages return error `40318`.

Queued messages return `queued` status and won't appear in MDR search until delivered. Monitor queue depth in the Mission Control Portal.

### Client-side rate limiting

Implement a token bucket rate limiter in your application to prevent queue buildup. Set the `rate` parameter to match your sender type: `0.1` for long code or alphanumeric, `20` for toll-free, `1000` for short code. For number pool configurations, effective rate = per-number limit × number count (e.g., 10 long codes at 0.1 MPS each = 1 MPS pool rate).

### Handling rate limit errors

When sending exceeds limits, handle error `40318` (queue full) with exponential backoff retry logic. Contact [Telnyx sales](mailto:sales@telnyx.com) if you need increased rate limits.

## Message Detail Records

A Message Detail Record (MDR) describes a message request — including status, cost, and metadata. Telnyx creates an MDR when a message is submitted and updates it as delivery progresses.

### Use cases

- **Delivery tracking**: Check if a message was delivered, failed, or is in progress.
- **Debugging**: Investigate delivery issues via status and error codes.
- **Cost verification**: Confirm message costs after delivery.
- **Audit trail**: Retrieve message history for compliance.

### Retrieving an MDR

Fetch a record using the UUID returned when you send a message or included in webhook events:

```
curl -X GET "https://api.telnyx.com/v2/messages/834f3d53-8a3c-4aa0-a733-7f2d682a72df" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### MDR schema

| Field | Type | Description |
|---|---|---|
| `id` | UUID | Unique identifier |
| `direction` | string | `inbound` or `outbound` |
| `type` | string | `SMS`, `MMS`, or `RCS` |
| `messaging_profile_id` | UUID | Profile used to send/receive |
| `from` | object | Sender details (phone_number, carrier, line_type) |
| `to` | array | Recipients (phone_number, status, updated_at) |
| `text` | string | Message body |
| `media_urls` | array | Media attachment URLs (MMS only) |
| `encoding` | string | `GSM-7` or `UCS-2` |
| `parts` | integer | Number of segments |
| `cost` | object | `amount` and `currency` (may be `null` until finalized) |
| `errors` | array | Error details if delivery failed |
| `webhook_url` | string | Webhook URL for delivery status |
| `created_at` | ISO 8601 | When the message was submitted |
| `updated_at` | ISO 8601 | Last status update |
| `valid_until` | ISO 8601 | Expiration time for pending messages |

**Cost may be null** immediately after sending because pricing is calculated asynchronously. The final cost appears in the `message.finalized` webhook event.

### Message status lifecycle

**Outbound statuses**:

| Status | Description | Final? |
|---|---|---|
| `queued` | Accepted and queued | No |
| `sent` | Delivered to carrier gateway | No |
| `delivered` | Carrier confirmed delivery to handset | Yes |
| `failed` | Delivery failed (check `errors`) | Yes |
| `gw_timeout` | No response from gateway | Yes |
| `dlr_timeout` | No delivery receipt from carrier | Yes |

**Inbound statuses**: `received` (message received by Telnyx) and `delivered` (delivered to your webhook).

### Common error codes

| Error Code | Description | Resolution |
|---|---|---|
| `40300` | Invalid destination | Verify phone number format |
| `40301` | Destination blocked | Recipient opted out — remove from list |
| `40310` | Carrier rejected | Content may have triggered spam filters |
| `40311` | Undeliverable | Number unreachable (landline, disconnected) |
| `40400` | Sender not registered | Register for 10DLC or toll-free verification |
| `40500` | Rate limit exceeded | Slow down sending or request higher limits |
| `40318` | Queue full | Back off and retry |
| `40333` | Spend limit reached | Daily spend limit exceeded |

### MDR best practices

- **Use webhooks instead of polling**: Configure `webhook_url` on your messaging profile to receive `message.sent`, `message.delivered`, and `message.finalized` events in real time.
- **Store message IDs**: Save the `id` returned when sending for later retrieval.
- **Handle null cost**: Wait for `message.finalized` webhook or retrieve the MDR after a few seconds.

### MDR troubleshooting

- **404 Not Found**: Invalid UUID format, message ID from a different account, or request was rejected at validation (no MDR created).
- **Status stuck on 'queued'**: Rate-limited or gateway issue. Wait 5 minutes; check system status if still stuck.
- **Cost shows null**: Asynchronous calculation — wait for the `message.finalized` webhook or retry after 5–10 seconds.
