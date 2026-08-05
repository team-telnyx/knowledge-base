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

*Part 6 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Event reference

| Event | Trigger | Recipient status | EDR timestamp | Billable |
| --- | --- | --- | --- | --- |
| `email.queued` | API accepted the request | `queued` → `sent` | `created_at` | No (API acceptance is not billable) |
| `email.scheduled` | Accepted with a future `send_at` | `queued` | `scheduled_at` | No |
| `email.sandbox` | Accepted in sandbox mode; no delivery attempted | `queued` | `created_at` | No (`billable` forced false) |
| `email.sent` | KumoMTA accepted the HTTP injection | `sent` | `sent_at` | **Yes** |
| `email.delivered` | KumoMTA `Delivery` (250 from remote MX) | `delivered` | `delivered_at` | Yes |
| `email.deferred` | KumoMTA `TransientFailure` (4xx) | `deferred` | `deferred_at` (first deferral) | Yes |
| `email.bounced` | KumoMTA `Bounce` / `OOB` | `bounced` | `bounced_at` | Yes |
| `email.bounced` | KumoMTA `Expiration` | **`expired`** | `expired_at` | Yes |
| `email.bounced` | KumoMTA `AdminBounce` | `failed` | `failed_at` | Yes |
| `email.complained` | KumoMTA `Feedback` (ARF report) | unchanged | — | Unchanged |
| `email.failed` | KumoMTA refused the injection | `gw_reject` | — | No |
| `email.injection_timeout` | Ambiguous transport timeout on injection | `injection_timeout` | — | No |
| `email.opened` | Tracking pixel loaded | unchanged | — | No |
| `email.clicked` | Tracked link followed | unchanged | — | No |
| `email.unsubscribed` | Tracked unsubscribe link used | unchanged | — | No |

A pre-dispatch system failure produces a stored `failed` event with **no** corresponding webhook; its billability depends on whether queue acceptance had already occurred. See [System failures](error-codes-and-event-lifecycle-system-failures-stored-but-not-pushed.md).

**Billing is derived from the source event, never from the resulting status.** A recipient is billable the moment it is proven to have been accepted into the MTA queue — by `Reception`, `Delivery`, `TransientFailure`, `Bounce`, `AdminBounce`, `OOB`, `Expiration`, or a successful injection. This is why a **bounce is still billable**: the message was transmitted; the receiver rejected it. And why `gw_reject`, `cancelled`, `injection_timeout`, and pre-queue system failures are **never** billable — nothing was ever transmitted. A message that fails on our side before reaching the queue costs you nothing.

### Bounce categories

Bounce-family callbacks are classified with a `bounce_category`:

| Category | Meaning | Recipient status | Auto-suppresses? |
| --- | --- | --- | --- |
| `permanent` | Hard bounce — 5xx from the receiving MX (mailbox not found, domain invalid) | `bounced` | Yes, on `5.1.x` / `5.2.x` |
| `oob` | Out-of-band — an asynchronous bounce report arriving after the message left our system | `bounced` | Yes, on `5.1.x` / `5.2.x` |
| `transient` | KumoMTA exhausted its retry window and gave up (`Expiration`) | `expired` | Yes (provisional) |
| `admin` | Operator-initiated bounce (`AdminBounce`) | `failed` | No |

`bounce_category` is **internal**. It is computed when the callback is handled and is used to drive auto-suppression, but it is **not** forwarded into the published webhook payload **and not** written into the recipient-scoped event row that `GET /v2/email_events` returns — that payload is built from correlation fields plus the recipient address only. Treat it as absent from both surfaces. Do not write handlers that branch on `bounce_category` on either surface. Use `error_evidence.code` (`30001` hard bounce, `30005` queue expiry, `30003`/`30099` system failure, `30006` gateway rejection) together with `error_evidence.enhanced_code` to distinguish the failure modes. The recipient `status` (`bounced` vs `expired` vs `failed`) on the authoritative recipient-status endpoint carries the same distinction the category was standing in for.

An out-of-band bounce is the reason a `delivered` recipient can later become `bounced`: the receiving server accepted the message, then generated a bounce afterwards. It is the only correction edge out of `delivered`, and it is genuinely common with forwarding setups and catch-all domains.
