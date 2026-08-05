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

*Part 5 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## How MTA callbacks map to events

KumoMTA emits typed log records. Each record type maps to exactly one canonical event type, and — separately — drives the recipient state machine.

| KumoMTA record | Webhook published | Recipient status | Stored event type | Internal `bounce_category` |
| --- | --- | --- | --- | --- |
| `Reception` | — (no duplicate event) | `sent` | `queued` | — |
| `Delivery` | `email.delivered` | `delivered` | `delivered` | — |
| `TransientFailure` | `email.deferred` | `deferred` | `deferred` | — |
| `Bounce` | `email.bounced` | `bounced` | `bounced` | `permanent` |
| `OOB` | `email.bounced` | `bounced` | `bounced` | `oob` |
| `Expiration` | `email.bounced` | **`expired`** | `failed` | `transient` |
| `AdminBounce` | `email.bounced` | `failed` | `failed` | `admin` |
| `Feedback` | `email.complained` | *(no change)* | `complained` | — |

**`bounce_category` is an internal classification and is not part of any public contract.** It is computed during callback handling and drives auto-suppression, but it is not forwarded into the published webhook, and it is never written into the recipient-scoped event row that `GET /v2/email_events` returns — that row's payload is built from correlation fields plus the recipient address only. Do not build consumer logic that reads it from either surface — use `error_evidence.code` to distinguish failure modes.

**`Expiration` diverges three ways, and you need all three to reason about it.**

- The **webhook event type** is `email.bounced` — the canonical bounce family type.
- The **recipient status** (and therefore the EDR `status`) is `expired`, with `expired_at` and error code `30005`.
- The **stored event type** returned by `GET /v2/email_events` is `failed` — the polling taxonomy has no `expired` member.

Only `AdminBounce` maps the recipient to `failed`. `Bounce` and `OOB` map to `bounced`. If you are building suppression or list-hygiene logic, treat `permanent` and `oob` as recipient signals; treat `transient` and `admin` as operational signals about your sending, not about the address.

The `status` field inside a webhook payload is the **event type**, not the recipient status. An expired recipient produces a payload with `"status": "bounced"` while its EDR reads `"status": "expired"`. Read `error_evidence.code` to tell the failure modes apart: `30001` is a hard bounce, `30005` is queue expiry, `30003`/`30099` are system failures, `30006` is a gateway rejection.

### Reception callbacks

`email.queued` fires from two different places, meaning two different things:

1. **API acceptance** — we persisted your request. The recipient stays `queued`. Pre-queue, not billable.
2. **KumoMTA `Reception`** — the MTA logged reception of the message. This moves the recipient to `sent` and **is** billable. No duplicate `email.queued` event is published — the API-level event already recorded acceptance.

**Count sends using `email.sent` webhooks.** A `Reception` callback updates the recipient to `sent` and billable, but does not publish a duplicate `email.queued` event — the API-level `email.queued` event already recorded acceptance. Counting `email.sent` is sufficient. Count from the recipient EDR instead — `billable: true`, or a non-null `sent_at` — or use `GET /v2/email_events/stats`, which aggregates at the recipient level. If you derive counts from the raw event stream, count `email.sent` events — each represents one accepted recipient.

### System failures: stored, but not pushed

When the message cannot be handed to the send pipeline at all — a publish failure into the send queue after the request has already been committed, or an account that became ineligible before a scheduled send fires — every still-non-terminal recipient is driven to `failed` and a **stored** `failed` event is written for each one. That path does not publish an `email.failed` webhook, **and it does not publish an EDR either** — `mark_system_failure` updates the recipient rows and inserts stored events directly, without invoking the EDR publisher. For a failure before queue acceptance there may be no EDR at all; for a recipient already accepted, the existing EDR is **not** updated to reflect the failure.

If you rely exclusively on webhooks, these failures are invisible. Reconcile with `GET /v2/email_events` or the authoritative per-recipient status endpoint — **not** the EDR. The `email.failed` webhook is published for a *definite injection refusal* by the MTA (recipient status `gw_reject`, error code `30006`).

System failures also do not blanket-reset billability. The transition is permitted from `queued`, `sending`, `sent`, and `deferred`; a recipient that had already been accepted into the MTA queue (`sent` or `deferred`) keeps its `billable: true`, because the message really was transmitted. Only pre-queue recipients (`queued`, `sending`) end up non-billable.

### Complaints are additive, not a state change

`email.complained` fires when a mailbox provider forwards an ARF spam report (the recipient hit "mark as spam"). By definition this arrives *after* delivery. It does not move the recipient out of `delivered` or `bounced` — the delivery already happened, and that fact is not retracted. The complaint is recorded alongside it and auto-suppresses the address. Because it is a no-op for the state machine, it does not produce a new EDR.

### Ambiguous injection: the honest unknown

If the injection call times out, retrying risks delivering the message twice; not retrying risks losing it. Telnyx chooses **loss over duplication** — the industry-standard trade-off for transactional mail. The recipient moves to the terminal `injection_timeout` state and `email.injection_timeout` fires. If KumoMTA *did* accept the message, its `Reception` callback arrives moments later and reconciles the recipient forward to `sent`, from where the normal lifecycle resumes. This is the only terminal-to-non-terminal edge in the entire state machine, and it is safe precisely because the callback is authoritative proof of acceptance.

`email.injection_timeout` is a **webhook-only** event type. It is not part of the stored event taxonomy returned by `GET /v2/email_events`, and the underlying recipient transition is recorded as `failed` in the persisted event row. If you rely on polling rather than webhooks, ambiguous injections surface as failures.
