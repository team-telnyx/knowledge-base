---
title: Email Deliverability, Domain Warm-up, and Domain Management
summary: How mailbox providers evaluate mail, how to authenticate and warm up a sending
  domain with Telnyx, how to read delivery events and error codes, and how to register,
  verify, and manage email domains.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/deliverability-best-practices
- url: https://developers.telnyx.com/docs/messaging/email/deliverability/index
- url: https://developers.telnyx.com/docs/messaging/email/domains/index
updated_at: 2026-08-05T13:54:17Z
---

# Email Deliverability, Domain Warm-up, and Domain Management

*Part 5 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 2](email-deliverability-domain-warm-up-and-domain-management--part-2.md), [Part 3](email-deliverability-domain-warm-up-and-domain-management--part-3.md), [Part 4](email-deliverability-domain-warm-up-and-domain-management--part-4.md), [Part 6](email-deliverability-domain-warm-up-and-domain-management--part-6.md), [Part 7](email-deliverability-domain-warm-up-and-domain-management--part-7.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Keep bounce rates low

- **Hard bounces** (permanent failures like `5.1.1 User unknown`): Remove the recipient immediately. High hard-bounce rates destroy reputation.
- **Soft bounces** (temporary failures like `4.2.1 Mailbox full`): Telnyx retries deferred deliveries automatically. Do not resubmit the message in response to an `email.deferred` event.

**`email.bounced` is broader than "the receiver permanently rejected it."** Four distinct outcomes publish the same event: an ordinary bounce, a queue expiration (retries exhausted), an administrative bounce, and an asynchronous out-of-band bounce. The per-recipient `status` and `error_evidence.code` tell you which actually happened — expiration resolves the recipient to `expired` (code `30005`), an administrative bounce to `failed`, and the others to `bounced` (code `30001`). Don't infer "invalid address" from the event type alone; read the evidence. See [Webhooks & Events](webhooks-events.md) and the [30xxx taxonomy](/docs/messaging/email/error-codes#asynchronous-delivery-errors-30xxx).

### What actually gets auto-suppressed

Telnyx does **not** suppress every bounced recipient. Auto-suppression is deliberately conservative so a transient or sender-side failure doesn't permanently block a valid address:

| Outcome | Auto-suppressed? | Reason recorded |
| --- | --- | --- |
| Spam complaint (feedback loop report) | **Yes**, always | `spam_complaint` |
| Queue expiration (retries exhausted) | **Yes** | `hard_bounce` |
| Bounce or OOB with a `5.1.x` or `5.2.x` enhanced code (bad or unavailable mailbox) | **Yes** | `hard_bounce` |
| Bounce or OOB with no enhanced code but a 5xx SMTP status | **Yes** (fallback) | `hard_bounce` |
| Bounce or OOB with a `5.7.x` enhanced code (security/policy) | **No** — sender-side policy, the address may be valid | — |
| Bounce or OOB with any other enhanced code | **No** — not on the suppression allowlist | — |
| Administrative bounce | **No** — operator-initiated, not a deliverability signal | — |

So a recipient can bounce, be recorded with `status: "bounced"`, and still **not** be added to your suppression list. Check the [Suppressions](suppressions.md) list rather than assuming a bounce implies suppression, and remove invalid addresses from your own source of truth regardless.

## Handle complaints

When Telnyx receives an individual spam feedback report from a participating mailbox provider, Telnyx:

1. Records an `email.complained` event.
2. Auto-suppresses the recipient (added to suppression list).
3. Fires a webhook if configured.

Not every mailbox provider supplies individual feedback reports, so `email.complained` events may not capture every user spam report. Monitor provider dashboards in addition to Telnyx events. Treat a provider-reported spam rate approaching 0.1% as a signal to stop increasing volume and investigate. Gmail and Yahoo require senders to remain below 0.3%, but operating close to that limit puts deliverability at risk.

## Monitor sending volume

Sudden spikes in volume trigger spam filters. Use `scheduled_at` to schedule sends across time windows rather than blasting everything at once. See [Scheduled sending](/docs/messaging/email/rate-limits#scheduled-sending).

## Content best practices

### Include a plain-text alternative

Provide a plain-text version for accessibility and email clients that prefer it. Keep the HTML and plain-text versions consistent:

```
{
  "html_body": "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
  "text_body": "Welcome! Thanks for signing up."
}
```

### Use a recognizable from name

Recipients who recognize the sender don't mark mail as spam. Use a consistent `from` address and name:

```
{
  "from": {
    "email": "notifications@yourdomain.com",
    "name": "YourApp Notifications"
  }
}
```

### Include an unsubscribe link

Every marketing email must include a visible, working unsubscribe link. Telnyx supports RFC 8058 one-click unsubscribe — when a recipient clicks unsubscribe in their email client, Telnyx:

1. Records an `email.unsubscribed` event.
2. Auto-suppresses the recipient.
3. Fires a webhook if configured.

### Keep content clear and recognizable

- Use an honest subject line that matches the message content.
- Avoid deceptive formatting, misleading links, and artificial urgency.
- Use accessible layouts, descriptive link text, and alt text for meaningful images.
- Keep branding and sender identity consistent so recipients recognize the message.
- Test rendering across the email clients your recipients use.

## The delivery lifecycle and where it fails

A Telnyx send passes through distinct stages, and knowing which stage failed determines what — if anything — you should do about it.

| Stage | What happened | Event |
| --- | --- | --- |
| Acceptance | The API validated and persisted the message for sending | `email.queued` |
| Handoff | Accepted by the Telnyx outbound MTA | `email.sent` |
| Delivery | The remote MX returned SMTP success | `email.delivered` |
| Transient failure | The remote MX returned a 4xx — will be retried | `email.deferred` |
| Permanent failure | The remote MX returned a 5xx | `email.bounced` |
| Expiration | Retries exhausted; the MTA gave up | `email.bounced` |
| Complaint | A feedback report (ARF) arrived from the provider | `email.complained` |

**`email.queued` does not mean the message reached the MTA.** It fires as soon as the API has validated the request and persisted the message — before the message is produced to the internal queue and before the outbound MTA has seen it. **`email.sent` does not mean the recipient received the message** either: it means the MTA accepted the message for delivery. Remote acceptance is reported separately by `email.delivered`. Treating `queued` or `sent` as success is the most common source of inflated delivery numbers.

Two boundaries are worth internalizing:

- **Deferred is not failure.** A 4xx response means "not now" — the remote server is throttling, greylisting, or temporarily unavailable. Telnyx retries automatically. Resubmitting a deferred message creates duplicates and worsens the throttling that caused the deferral.
- **Delivered is not "in the inbox."** A 250 response means the receiving server accepted custody. Placement — inbox, promotions, or spam — happens after acceptance and is never reported back over SMTP. This is why provider-side tools like Google Postmaster Tools show you something your delivery events structurally cannot.

### Suppression: the send that never happens

When a recipient is on your suppression list, the message is not attempted at all — and the recipient is removed from the send *before* any per-recipient record exists. Telnyx suppresses automatically after a qualifying hard bounce or a spam complaint, so the platform enforces the list hygiene that protects your reputation.

Suppressed addresses are stripped from `to`, `cc`, and `bcc` during request handling, so they never get a recipient row and never produce a delivery attempt. If *every* recipient on the request is suppressed, the API rejects the request with `recipient_suppressed` and no message, recipient row, or detail record is created at all. The response includes a top-level `suppressed` array naming the blocked addresses.
