---
title: Email Error Codes and Event Lifecycle
summary: Reference for the Telnyx Email API's two error families — synchronous HTTP
  errors (10xxx) returned on the API request itself, and asynchronous delivery errors
  (30xxx) reported later via webhooks and Email Detail Records — together with the
  per-recipient event lifecycle that drives them.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/error-codes
- url: https://developers.telnyx.com/docs/messaging/email/event-lifecycle
updated_at: 2026-08-05T13:54:42Z
---

# Email Error Codes and Event Lifecycle

*Part 8 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Consuming the lifecycle

Three surfaces expose the outbound lifecycle. Pick based on your infrastructure — but note that they do **not** carry identical fields (see the warning above).

| Surface | Endpoint | Use when |
| --- | --- | --- |
| **Webhooks** | Your HTTPS endpoint | You want push delivery in real time and can host a public endpoint |
| **Polling** | `GET /v2/email_events` | You have no public endpoint, or you're reconciling after an outage. Returns a sanitized payload — internal correlation fields are stripped, and `bounce_category` is not present |
| **Stats** | `GET /v2/email_events/stats` | You want aggregate recipient-level counts and rates, not individual events |

**The WebSocket endpoint is inbound-only.** It is a best-effort real-time stream of **inbound** `email.received` events for your account. It does not carry the outbound delivery lifecycle — no `email.sent`, `email.delivered`, `email.bounced`, or any other outbound event is broadcast on it. Use webhooks or polling for outbound.

Webhooks fire **per event, per recipient**, and each subscription carries an allowlist — you receive only the event types you asked for. A subscription listing only `email.bounced` gets bounces and nothing else. See the [Webhooks & Events](webhooks-events.md) guide for subscription setup, payload envelopes, Ed25519 signature verification, cursor pagination, and retry behavior.

The polling API and the webhook allowlist use **different taxonomies**. Polling filters accept bare event names (`delivered`, `bounced`); webhook subscriptions use the prefixed form (`email.delivered`). The stored taxonomy has no `expired` or `injection_timeout` member — both are recorded as `failed` — and it excludes webhook-only types such as `email.injection_timeout` entirely. Don't assume a name valid in one is valid in the other.

### Designing a consumer

A few properties of the stream are worth designing around:

- **Events are not ordered.** A `Delivery` callback can arrive before the `Reception` that logically precedes it. The state machine handles this — `queued → delivered` is a legal edge — and your consumer should too. Use the timestamps, not arrival order.
- **Events are idempotent, and replays happen.** The same callback redelivered produces no second state transition and no duplicate stored event. Your handler should be equally tolerant: key on the event ID.
- **Terminal is not always final.** `delivered → bounced` via an out-of-band report is legitimate and will happen in production. Don't build logic that assumes a delivered message can never bounce.
- **Scope everything by recipient.** A three-recipient message produces three parallel event streams. Aggregating them into one message-level status will lose information the moment one recipient bounces and another delivers.
- **Don't count from webhooks alone.** Some outcomes are stored without a webhook (pre-dispatch system failures), and one webhook type covers several statuses (`email.bounced` for bounced, expired, and admin-bounced). Reconcile against `GET /v2/email_events`, the stats API, or the authoritative per-recipient status endpoint. Note that system failures do not publish an EDR, so the EDR alone will not close that gap.

## Delivery failures come in two layers

When something goes wrong, the layer tells you where to look.

### Layer 1 — API errors (`10xxx`)

The request was rejected synchronously. No message was created, no event fires, nothing is billed. You get an HTTP error with a Telnyx error code — `10015` for validation failures, `10007` for an unverified domain or unauthorized sender, `10006` for a bad API key. These are **your** bugs, and they are fixable before you retry. Full list in the [Synchronous error code reference](error-codes-and-event-lifecycle-synchronous-error-code-reference.md).

### Layer 2 — Delivery failures (`30xxx`)

The request succeeded and delivery failed downstream. These surface asynchronously as events, and the detail lives in `error_evidence`:

- `error_evidence.code` — the **normalized** taxonomy code (`"30001"`, `"30002"`, `"30005"`), never a raw SMTP code
- `error_evidence.source` — where it originated (`smtp`, `mta`, `api`, …)
- `error_evidence.retryable` — whether retrying this address could succeed
- `error_evidence.smtp_status` — the raw SMTP status, preserved for triage (`550`, `421`)
- `error_evidence.enhanced_code` — the RFC 3463 enhanced status code (`"5.1.1"`)
- `error_evidence.message` — what the receiving server actually said (null when nothing reached SMTP)

**Route on `code` and `retryable`, triage on `smtp_status` and `enhanced_code`.** `30002` is temporary (you'll see `email.deferred`, and the MTA is already retrying — do nothing). `30001` is permanent (you'll see `email.bounced`, and retrying the same address will fail again). `30005` means we ran out of retry window, and `30003`/`30006`/`30099` mean the failure was on our side of the wire, not the recipient's.

Within a hard bounce, the enhanced code tells you whose problem it is. `5.1.x` and `5.2.x` are recipient problems — bad or full mailbox, and the address is auto-suppressed. `5.7.x` is a **sender** problem — authentication or policy rejection — and the address is deliberately *not* suppressed, because it is probably fine. A rise in `5.7.x` means you should be checking SPF, DKIM, and DMARC, not cleaning your list.
