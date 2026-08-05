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

*Part 4 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## The lifecycle

An email is handed to **KumoMTA**, the outbound mail transfer agent. Telnyx injects the message over HTTP, and KumoMTA reports back asynchronously with log records — one per event, per recipient. Those records drive the state machine.

### Per-recipient states

Callbacks are not ordered, so `queued` also accepts a `Delivery`, `TransientFailure`, `Bounce`, `OOB`, `AdminBounce`, or `Expiration` that arrives before the injection outcome is recorded — going straight to `delivered`, `deferred`, `bounced`, `failed`, or `expired` respectively.

Terminal states are `delivered`, `bounced`, `failed`, `expired`, `gw_reject`, `cancelled`, and `injection_timeout`. Once a recipient is terminal it does not regress — a late `TransientFailure` arriving after a `delivered` is logged for diagnostics and ignored, never applied. There is exactly **one deliberate exception**: `injection_timeout → sent`. See [Ambiguous injection](error-codes-and-event-lifecycle-ambiguous-injection-the-honest-unknown.md) below.

### The message-level track

The parent message runs on its own short track, and it is not part of the per-recipient state machine above. When the consumer picks the message up it sets the **message** to `sending` and records a message-scoped `sending` event. That event is stored but deliberately does **not** publish a webhook — the per-recipient webhooks are published separately once the MTA responds. Recipient rows stay `queued` throughout; they only move once injection is accepted, refused, times out, or a callback arrives.

### What each recipient state means

**queued** — accepted, not yet handed to the MTA. The API validated your request, persisted the message, and returned `202`. Nothing has been transmitted yet. **Fires:** `email.queued` (also `email.scheduled` for a future `send_at`, or `email.sandbox` in sandbox mode — neither attempts delivery). **Not yet billable.** Acceptance by our API is not acceptance by the MTA.

**sent** — KumoMTA accepted the recipient into its queue. The message is now the MTA's responsibility. It will attempt delivery to the recipient's MX, retrying on transient failures. **Fires:** `email.sent` on a successful HTTP injection. A `Reception` callback also lands the recipient here but does not publish a duplicate event. **Billable from this point** — queue acceptance is the billing trigger. `sent` does **not** mean the recipient received it. Remote acceptance is reported separately as `email.delivered`.

**delivered** — the receiving server accepted the message. KumoMTA got a `250 OK` from the recipient's MX. This is the successful terminal state. **Fires:** `email.delivered`. **EDR records:** `delivered_at`. Delivered means *accepted by the receiving server* — it does not guarantee inbox placement. The mail can still be filed as spam by the recipient's provider after acceptance, which is invisible to SMTP. See [Deliverability](deliverability.md).

**deferred** — temporary failure, will retry. The receiving server returned a 4xx transient response (greylisting, rate limiting, "try again later"). KumoMTA backs off and retries. **Fires:** `email.deferred`. **EDR records:** `deferred_at`, plus `error_evidence` carrying code `30002`. A recipient can be deferred many times before resolving. `deferred_at` is stamped on the **first** deferral and locked — it is not a "most recent attempt" field. Repeated deferrals for the same address escalate an internal soft-bounce counter, which can eventually auto-suppress the address as a hard bounce.

**bounced** — permanent rejection by the receiver. The receiving server refused the message outright (5xx), or an asynchronous bounce report arrived after the fact. **Fires:** `email.bounced`. **EDR records:** `bounced_at` and `error_evidence` (code `30001`, or `30002` when KumoMTA reports a bounce carrying a 4xx code). Bounces with a `5.1.x` or `5.2.x` enhanced code (bad or disabled mailbox) auto-suppress the address. Bounces with `5.7.x` (sender policy/authentication) do **not** — the address may be perfectly valid, and the problem is on your side.

**expired** — KumoMTA exhausted its retry window. The MTA retried until its queue expiry deadline and gave up. Nothing about the recipient address was rejected; the remote server simply never accepted the message in time. **Fires:** `email.bounced` — the webhook event type for the `Expiration` callback is still the canonical bounce type. **EDR records:** `expired_at`, `expired: true`, and `error_evidence` with code `30005` (Queue expiry, source `mta`). **Billable** — the message was accepted into the MTA queue, which is the billing trigger. Expiration is provisionally treated as a hard bounce for suppression purposes.

**failed** — non-delivery caused by us or an operator. Distinct from `bounced` and `expired`: nothing about the recipient address was rejected and the MTA did not run out of retries. Either an internal/system failure occurred (e.g. the message could not be published to the send pipeline, or the account became ineligible before dispatch), or an operator cancelled the in-flight message (`AdminBounce`). **Fires:** `email.bounced` on the `AdminBounce` callback path. System failures insert a stored `failed` event but do **not** publish an `email.failed` webhook — see [System failures](error-codes-and-event-lifecycle-system-failures-stored-but-not-pushed.md). **EDR records:** `failed_at` and `error_evidence` (code `30003` when an SMTP status is present, otherwise `30099`). Because `failed` is not a recipient-side signal, it does not suppress the address.

**gw_reject** — KumoMTA refused the injection. The MTA rejected the message at the HTTP injection boundary, before it ever entered a queue. This is pre-queue, so it is **never billable**. **Fires:** `email.failed`. **EDR records:** `error_evidence` and `errors[]` with code `30006` (Gateway rejection, source `api`).

**injection_timeout** — we genuinely do not know. The injection HTTP call timed out with no response. KumoMTA may or may not have accepted the message. **Fires:** `email.injection_timeout`. **Not billable.** No EDR is published — the outcome is ambiguous, and a later `Reception` callback would publish one on reconciliation. See [Ambiguous injection](error-codes-and-event-lifecycle-ambiguous-injection-the-honest-unknown.md).

**cancelled** — withdrawn before it was queued. A scheduled or queued message was cancelled before injection. Only `queued` and `sending` recipients can be cancelled; anything already accepted by the MTA is past the point of recall and is left untouched. **Never billable.**
