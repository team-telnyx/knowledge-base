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

*Part 3 of 3 — see also: [Part 1](rcs-messaging-on-telnyx--part-1.md), [Part 2](rcs-messaging-on-telnyx--part-2.md)*

RCS (Rich Communication Services) on Telnyx enables rich, interactive messaging beyond SMS, with support for rich cards, carousels, suggested actions, AI-powered assistants, capability lookups, deeplinks, and carrier-specific throughput considerations.

## Rate Limits and Throughput

RCS throughput is governed by both account-level and sender-level rate limits. For API request limits (separate from message throughput), see [API Rate Limiting](api-rate-limiting.md).

### Account-level limits

| Message Type | Default Rate Limit | Max Queue Length |
| --- | --- | --- |
| SMS | 50 messages/second | 720,000 |
| MMS | 15 messages/second | 216,000 |
| RCS | 1 message/second | 14,400 |

### Sender-level limits

| Sender Type | Rate Limit | Per | Max Queue Length |
| --- | --- | --- | --- |
| Long Code | 0.1 MPS | Number | 1,440 |
| Toll-Free | 20 MPS | Number | 288,000 |
| Short Code | 1,000 MPS | Number | 14,400,000 |
| Alphanumeric | 0.1 MPS | Sender ID | 1,440 |

The default Long Code rate limit applies to non-US destinations. For US destinations, throughput is determined at the campaign level based on your 10DLC registration. If you need an increased rate limit, contact [Telnyx sales](mailto:sales@telnyx.com).

### 10DLC carrier-specific limits

When using US long codes for A2P messaging, throughput is determined by mobile network operators (MNOs) based on your registered 10DLC campaign. Each carrier has different throughput systems.

**AT&T** assigns throughput per campaign based on "Message Class," determined by use case type and vetting score:

| Message Class | Use Case Type | Vetting Score | SMS TPM | MMS TPM |
| --- | --- | --- | --- | --- |
| A | Standard (Dedicated) | 75-100 | 4,500 | 2,400 |
| B | Standard (Mixed/Marketing) | 75-100 | 4,500 | 2,400 |
| C | Standard (Dedicated) | 50-74 | 2,400 | 1,200 |
| D | Standard (Mixed/Marketing) | 50-74 | 2,400 | 1,200 |
| E | Standard (Dedicated) | 1-49 | 240 | 150 |
| F | Standard (Mixed/Marketing) | 1-49 | 240 | 150 |
| T | Low Volume Mixed | - | 75 | 50 |
| K | Political | - | 4,500 | 2,400 |
| P | Charity | - | 2,400 | 1,200 |
| S | Social | - | 9,000 | 2,400 |
| X | Emergency / Public Safety | - | 4,500 | 2,400 |
| W | Sole Proprietor | - | 15 | 50 |
| G | Proxy | - | 60/number | 50/number |
| N | Agents and Franchises | - | 60/number | 50/number |

TPM = Throughput Per Minute. For standard use cases, the vetting score from your 10DLC brand registration determines which message class (and throughput) your campaign receives. Special use cases have fixed throughput regardless of vetting score.

**T-Mobile** assigns daily message caps at the brand level, shared across all campaigns under that brand:

| Brand Tier | Vetting Score | Daily Cap |
| --- | --- | --- |
| Top | 75-100 | 200,000 |
| High Mid | 50-74 | 40,000 |
| Low Mid | 25-49 | 10,000 |
| Low | 1-24 | 2,000 |

Unvetted brands default to Low tier unless listed on the Russell 3000. Sole Proprietor campaigns have a 1,000 daily cap.

**Verizon** has not published specific throughput limits but uses content filtering for 10DLC traffic.

### Queuing

When you send messages faster than your rate limit allows, excess messages are automatically queued for delivery:

1. **Message submitted** — Request validated against your Messaging Profile
2. **Rate limit check** — Under limit: sent immediately. Over limit: queued
3. **Queue processing** — Messages held up to 4 hours, released in FIFO order
4. **Delivery** — Sent to carrier, webhook fired, visible in MDR search

Each sender type and message type combination has its own queue. The maximum queue length is:

```
Max Queue Length = Rate Limit (MPS) × 14,400 seconds (4 hours)
```

When a queue is full, additional messages return error code `40318`. See [API Errors](api-errors.md) for details.

### Client-side rate limiting

Implementing rate limiting in your application prevents queue buildup, avoids `40318` errors, and gives you control over message pacing. A token bucket rate limiter works for any sender type. Set the `rate` parameter to match your sender type:

| Sender Type | Rate Parameter | Example |
| --- | --- | --- |
| Long Code | `0.1` | `RateLimiter(0.1)` |
| Toll-Free | `20` | `RateLimiter(20)` |
| Short Code | `1000` | `RateLimiter(1000)` |
| Alphanumeric | `0.1` | `RateLimiter(0.1)` |

For [Number Pool](number-pool.md) configurations, the effective rate is the per-number limit multiplied by the number of numbers in the pool. For example, 10 Long Codes at 0.1 MPS each gives an effective 1 MPS pool rate.

### Handling rate limit errors

When your sending rate exceeds limits, the API returns specific error codes. Handle them gracefully with retry logic using exponential backoff on error `40318` (queue full).

## Related Resources

- [API Rate Limiting](api-rate-limiting.md) — HTTP API request rate limits (separate from message throughput)
- [10DLC Rate Limits](10dlc-rate-limits.md) — Carrier-specific throughput for 10DLC campaigns
- [Number Pool](number-pool.md) — Distribute messages across multiple numbers for higher throughput
- [Message Detail Records](message-detail-records.md) — Monitor delivery status and diagnose throughput issues
- [RCS Getting Started](rcs-getting-started--part-1.md) — Set up your RCS agent and get approved
- [RCS Rich Cards](rcs-rich-cards.md) — Send interactive rich cards
- [RCS Webhooks](rcs-webhooks.md) — Handle inbound RCS messages and delivery events
- [RCS API Reference](rcs-api-reference.md) — Full API reference for RCS messaging
- [AI Assistant Docs](ai-assistant-docs.md) — Deep dive into AI Assistant configuration
