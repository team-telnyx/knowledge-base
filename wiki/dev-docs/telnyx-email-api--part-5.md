---
title: Telnyx Email API
summary: The Telnyx Email API is a full email platform combining transactional sending,
  bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure
  that powers Telnyx's global messaging network. This page covers the API's capabilities,
  architecture, getting-started paths, inboxes, migration from other ESPs, and rate
  limits and quotas.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/inboxes/index
- url: https://developers.telnyx.com/docs/messaging/email/migrate-to-telnyx
- url: https://developers.telnyx.com/docs/messaging/email/overview
- url: https://developers.telnyx.com/docs/messaging/email/quickstart
- url: https://developers.telnyx.com/docs/messaging/email/rate-limits
updated_at: 2026-08-05T13:51:25Z
---

# Telnyx Email API

*Part 5 of 5 — see also: [Part 1](telnyx-email-api--part-1.md), [Part 2](telnyx-email-api--part-2.md), [Part 3](telnyx-email-api--part-3.md), [Part 4](telnyx-email-api--part-4.md)*

The Telnyx Email API is a full email platform combining transactional sending, bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure that powers Telnyx's global messaging network. This page covers the API's capabilities, architecture, getting-started paths, inboxes, migration from other ESPs, and rate limits and quotas.

## Rate limits and quotas

Rate limits protect the platform and ensure fair resource allocation. This page covers request and sending limits enforced by the Email API, and how to request increases.

### Request and message size limits

Three different ceilings apply at three different layers. They are frequently confused — only the first two reject a message.

| Limit | Value | Enforced by | Failure |
| --- | --- | --- | --- |
| Message body (`html_body` + `text_body`, decoded) | 1 MB | Email API | `422` with code `10015`, detail "body exceeds size limit (maximum 1 MB)" |
| Total message (decoded body + decoded attachments) | 25 MB | Email API | `422` with code `10015`, detail "message exceeds size limit (maximum 25 MB)" |
| HTTP request body | 150 MB | Phoenix request parser | `413` with code `10015` |
| Idempotency-keyed replay capture | 8 MB | Telnyx Edge (API gateway) | `413 Payload Too Large` — keyed request over 8 MB is rejected at Edge. Unkeyed requests bypass this cap. |
| Batch messages per request (`POST /email_messages/batch`) | 50 | Email API | `400` with code `10015` |
| Batch validations per request (`POST /email_validations/batch`) | 1,000 | Email API | `400` with code `10015` |

**8 MB is not the request body limit.** It is the Edge gateway's replay cap for idempotency-keyed requests. A keyed request over 8 MB is rejected at the Edge with `413 Payload Too Large` — it never reaches the Email API. Unkeyed requests bypass this cap entirely. The limits that actually reject a message are the **1 MB decoded body** and **25 MB total message**, enforced by the Email API, which return `422`.

Attachments are base64-encoded in the request, so a 25 MB message occupies roughly 33 MB on the wire. The Email API measures **decoded** bytes, so budget against the decoded size, not the encoded payload.

A batch send with more than 50 messages is rejected with `400`:

```json
{
  "errors": [
    {
      "code": "10015",
      "title": "Bad Request",
      "detail": "messages must contain at most 50 items"
    }
  ]
}
```

### Request rate limits

API requests are rate-limited at the Telnyx API edge. Exact per-endpoint rates depend on your account tier and are not fixed platform-wide constants — if you need a specific sustained request rate, contact support to confirm or raise your account's limits.

When you exceed the limit, you'll receive `429 Too Many Requests`.

**Do not assume a `Retry-After` header is present.** The Email API's own `429` responses — daily send limit and reputation suspension — do **not** set `Retry-After`. Honor the header when it is present (edge-level rate limiting may supply it) and fall back to exponential backoff with jitter when it is absent. Never block on parsing a header that may not be there.

**Not every 429 is a rate limit.** Two very different conditions return `429`, and they need opposite handling. Branch on the **error code**, never on the status alone.

| Code | Condition | What to do |
| --- | --- | --- |
| `10011` | The account's **daily send limit** was exceeded. The detail names the limit and states that it resets at **midnight UTC**. | Queue the work and resume after the daily reset. Exponential backoff over seconds or minutes will not help — the counter is daily. |
| `reputation_suspended` | The sending domain's reputation band dropped to `poor`. | **Stop and remediate.** Retrying never succeeds and continued attempts worsen the signal. Reduce bounce and complaint rates, then confirm the band recovered. |
| *(no email-specific code)* | Edge-level request rate limiting. | Back off exponentially with jitter and retry. |

Both `10011` and `reputation_suspended` are rejected **before message creation** — no message record, no billing, no MTA injection.

**Reputation-based suspension.** Separate from request rate limiting, sending can be suspended when a domain's reputation band drops to `poor`. This returns `429` with code `reputation_suspended`:

```json
{
  "errors": [
    {
      "code": "reputation_suspended",
      "title": "Sending Suspended",
      "detail": "Sender domain reputation is too low. Sending has been suspended. Please contact support to resolve deliverability issues."
    }
  ]
}
```

See [Deliverability and Domain Warm-up](deliverability-and-domain-warm-up.md) for reputation guidance and recovery steps.

**Daily send limit.** When an account exceeds its daily send quota, the send is rejected with `429` and code `10011`:

```json
{
  "errors": [
    {
      "code": "10011",
      "title": "Too Many Requests",
      "detail": "Daily send limit of 1000 recipients exceeded. The limit resets at midnight UTC."
    }
  ]
}
```

The quota is counted in **recipients**, not API requests — a single request to five addresses consumes five slots. Suppressed recipients are filtered out before the count, so they don't consume quota. Sandbox sends are exempt.

### Destination provider throttling

Beyond the limits above (which protect the Telnyx platform), receiving providers like Gmail, Outlook, and Yahoo impose their own rate limits on incoming mail. The Telnyx outbound MTA handles destination-side pacing automatically — you do not need to build client-side throttling for provider rate limits.

When you send faster than a destination provider accepts, the MTA automatically queues the overflow in its local queue and delivers it as the rate window opens. Queued messages are not returned as failures — they remain in the queue and deliver once the receiving provider accepts them.

Destination throttling is automatic, but it is not a substitute for good sending practices. You still need to warm up new domains, monitor your reputation, and stay within your [account sending quota](#sending-quotas) and [API request rate limits](#request-rate-limits). A sustained burst that exceeds the 72-hour queue lifetime will cause messages to expire undelivered.

**Per-provider delivery rates.** The MTA paces outbound delivery based on the recipient's domain:

| Recipient domain | Maximum delivery rate | Retry interval | Max interval between retries |
| --- | --- | --- | --- |
| `gmail.com`, `googlemail.com` | 500 messages/hour | 10 minutes | 4 hours |
| `outlook.com`, `hotmail.com`, `live.com` | 500 messages/hour | 10 minutes | 4 hours |
| All other domains | 1,000 messages/hour | 5 minutes | 2 hours |

The retry interval is the delay between delivery attempts when a transient failure occurs. The max interval between retries is the upper bound for exponential backoff — the delay grows between retries up to this cap. Messages remain in the queue for up to **72 hours** total; only messages that exceed this lifetime are expired.

**These caps match recipient domains, not the email provider behind them.** A company that uses Google Workspace on their own domain (e.g., `user@company.com`) is paced at the default rate (1,000/hour), not the Gmail rate — because the recipient domain is `company.com`, not `gmail.com`.

**What this means for senders.** The API accepts messages that pass validation and applicable limits (single sends return `202 Accepted`; batch sends return `207 Multi-Status` with per-message results). The actual delivery pace is managed downstream by the MTA — you can submit messages without worrying about exceeding destination-side rate limits.

Rate-cap overflow is silent — the MTA holds excess messages in its local queue and delivers them as the rate window opens, following the normal `email.queued` → `email.sending` → `email.sent` → `email.delivered` event sequence. No separate event is emitted for queue pacing.

If a receiving server returns a transient failure (e.g., a `4xx` SMTP response), the MTA retries automatically using exponential backoff (up to the max interval between retries in the table above) and emits an `email.deferred` event. Successful retry then emits `email.delivered`. If the message ultimately cannot be delivered within the 72-hour queue lifetime, it expires and emits an `email.bounced` event (the recipient status is `expired`, but the webhook event type is `bounced`). Do not resubmit deferred messages — the MTA handles retries automatically.

**Destination throttling and your account sending quota operate on different time scales.** The per-provider caps above are hourly delivery rates; the [daily send limit](#daily-send-limit) is a 24-hour recipient count. Both apply independently — a provider cap doesn't reduce your daily quota, and your daily quota doesn't raise the provider cap. See [Sending quotas](#sending-quotas) for account-level limits.

**Reputation-based throttling stacks on top of provider caps.** If your sending domain's reputation band drops to `warn`, the MTA halves the delivery rate for queues carrying that domain's mail. At `poor`, new sends are rejected at the API with `429 reputation_suspended` before reaching the MTA. See [Reputation-based suspension](#reputation-based-suspension) above and [Deliverability & Warm-up](deliverability-warm-up.md) for reputation guidance.

### Sending quotas

Sending quotas vary by account tier. Contact your account manager for your current quota.

Sandbox mode (`sandbox_mode: true`) lets you test the full send flow — validation, event creation, webhook firing — without actually delivering the message. Sandbox sends do not consume daily quota and are not billed.

**Billing.** Outbound messages are billed **per recipient accepted into the outbound MTA queue**. A message addressed to five recipients is therefore *up to* five billable sends — one for each recipient the MTA accepts.

Recipients that fail before reaching the queue are **not** billable:

- Suppressed recipients (filtered before the send).
- Gateway rejections — the MTA refused the recipient at injection.
- Sandbox sends — nothing is delivered.
- System failures and cancellations that occur while the recipient is still pre-queue.

So a five-recipient send where two addresses are suppressed and one is rejected at injection bills for two, not five. Recipient-level outcomes are visible in the `recipient_statuses` counts on the message resource and in [per-recipient webhooks](/docs/messaging/email/webhooks-events). See your rate card or contact your account manager for pricing details.

### High-volume sending patterns

**Batch sending.** For high-volume sending, use the batch endpoint to reduce API calls:

```bash
curl -X POST https://api.telnyx.com/v2/email_messages/batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Idempotency-Key: 20dbec69-bc70-4fed-aec7-2a70af3b9524" \
  -d '{
    "messages": [
      {
        "from": "notifications@example.com",
        "to": [{"email": "user1@example.com"}],
        "subject": "Welcome",
        "text_body": "Welcome to our service!"
      },
      {
        "from": "notifications@example.com",
        "to": [{"email": "user2@example.com"}],
        "subject": "Welcome",
        "text_body": "Welcome to our service!"
      }
    ]
  }'
```

- Up to **50 messages** per batch request.
- The `Idempotency-Key` header applies to the entire batch — reuse it only for exact retries of the same batch body.
- Partial success returns `207 Multi-Status` with per-message results. See [Error Codes](error-codes.md).

**Scheduled sending.** Spread load over time using `scheduled_at`:

```json
{
  "from": "notifications@example.com",
  "to": ["user@example.com"],
  "subject": "Scheduled message",
  "text_body": "This was scheduled.",
  "scheduled_at": "2027-03-14T09:00:00Z"
}
```

The message is saved with `status: "scheduled"` and dispatched at the specified time.

**`scheduled_at` must be a future ISO 8601 timestamp.** A value in the past, or one that fails to parse, is **silently ignored** — the message is sent immediately as a normal send, with no error and no `scheduled` status. There is no validation error to catch, so validate the timestamp client-side before submitting. The legacy field name `send_at` is still accepted as a fallback, but `scheduled_at` is the canonical name.

**Scheduled sends do not consume daily quota at request time.** Quota is reserved when the scheduled worker actually fires, not when you submit the request. This means a scheduled send can be accepted today and still be rejected at fire time if the daily limit is exhausted then — in which case the message is marked `failed` and a `daily_limit_exceeded` event is recorded rather than a `429` being returned to you. Poll for that event type via `GET /email_events` to detect it; it is **not** available as a webhook subscription. Sandbox sends are likewise exempt from request-time quota reservation.

### Requesting limit increases

To increase your sending quotas or request rates:

1. Contact your account manager or Telnyx support.
2. Provide your expected sending volume (messages/day, messages/second).
3. Have your domain(s) verified and warmed up (see [Deliverability](deliverability.md)).

Contact your account manager for current quotas, pricing, and increase timelines.
