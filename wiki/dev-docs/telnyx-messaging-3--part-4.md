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

*Part 4 of 4 — see also: [Part 1](telnyx-messaging-3--part-1.md), [Part 2](telnyx-messaging-3--part-2.md), [Part 3](telnyx-messaging-3--part-3.md)*

Telnyx Messaging provides APIs for sending and receiving SMS, MMS, and RCS messages with support for rich cards, carousels, scheduled delivery, smart encoding, short codes, and real-time webhooks for delivery tracking and inbound messages.

## Short Codes

Short codes are 5- or 6-digit numbers for high-volume A2P messaging with throughput up to **1,000 messages per second**.

**When to use:** High-volume alerts, 2FA, marketing campaigns with keyword opt-in, voting/polling, emergency notifications.

**Consider alternatives** for low volume (< 1,000 msgs/day), quick setup, or budget-conscious use cases — see 10DLC or toll-free instead.

| Feature | Short Code | Toll-Free | 10DLC Long Code |
|---|---|---|---|
| Throughput | Up to 1,000 MPS | 20 MPS | Varies by campaign |
| Setup time | 8–12 weeks | 1–2 weeks | Days |
| Cost | Higher | Moderate | Lowest |
| Carrier trust | Highest | High | Varies by vetting score |

### Provisioning

1. **Request** a short code in the Portal (random: 8–10 weeks; vanity: 10–12 weeks).
2. **Complete application** — company info, use case, message samples, volume estimates, opt-in/opt-out flow.
3. **Carrier certification** — Each major US carrier (AT&T, T-Mobile, Verizon, US Cellular) reviews independently. This takes 8–12 weeks.
4. **Start messaging** — Once approved, send using the same `POST /v2/messages` endpoint with `from: "12345"`.

### Required keyword handling

| Keyword | Purpose | Telnyx handling |
|---|---|---|
| STOP (UNSUBSCRIBE, END, QUIT, CANCEL) | Opt-out | Automatic — user blocked from receiving messages |
| HELP (INFO) | Help/support | Automatic — sends configured help message |
| Campaign keyword | Opt-in | Automatic — sends configured keyword response |

STOP handling cannot be disabled. HELP and campaign keyword auto-responses can be disabled after certification by contacting support, so you can handle them via webhook instead.

## Error Handling

API errors return structured JSON:

```json
{
  "errors": [
    {
      "code": "40300",
      "title": "Forbidden",
      "detail": "The from number is not assigned to a messaging profile."
    }
  ]
}
```

### HTTP error codes

| Status | Meaning | Retryable |
|---|---|---|
| `400` | Bad Request | No |
| `401` | Unauthorized | No |
| `402` | Payment Required | No |
| `403` | Forbidden | No |
| `404` | Not Found | No |
| `422` | Unprocessable Entity | No |
| `429` | Too Many Requests | **Yes** |
| `500` | Internal Server Error | **Yes** |
| `503` | Service Unavailable | **Yes** |

### Messaging-specific error codes

| Code | Description |
|---|---|
| `40001` | Phone number not in E.164 format |
| `40002` | Missing required field |
| `40300` | Number not assigned to messaging profile |
| `40301` | Sender registration required |
| `40302` | Messaging profile disabled |
| `42200` | Invalid `from` number |
| `42201` | Invalid `to` number |
| `42202` | Message body too long |
| `42203` | Invalid media URL |
| `42204` | Too many media attachments |
| `42205` | Media file too large |

### Delivery failure error codes

These appear in `errors[]` in `message.finalized` webhooks:

| Code | Description |
|---|---|
| `30003` | Unreachable destination |
| `30004` | Message blocked by carrier |
| `30005` | Unknown destination |
| `30006` | Landline or unreachable |
| `30007` | Carrier violation |
| `30008` | Destination capacity exceeded |

## Rate Limiting

When you exceed the rate limit, the API returns `429 Too Many Requests` with a `retry-after` header.

**Response headers:**

| Header | Description |
|---|---|
| `x-ratelimit-limit` | Max requests in current window |
| `x-ratelimit-remaining` | Requests remaining |
| `x-ratelimit-reset` | Unix timestamp when window resets |
| `retry-after` | Seconds to wait before retrying |

**Best practices for high-volume sending:**

- Implement exponential backoff with jitter: `wait = 2^attempt * (0.5 + random())`
- Set a max retry count (3–5 attempts)
- Use a message queue (Redis, RabbitMQ, SQS) to buffer outbound messages
- Monitor `x-ratelimit-remaining` and slow down before hitting the limit
