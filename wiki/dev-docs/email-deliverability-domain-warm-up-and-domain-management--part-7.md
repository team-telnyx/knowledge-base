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

*Part 7 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 2](email-deliverability-domain-warm-up-and-domain-management--part-2.md), [Part 3](email-deliverability-domain-warm-up-and-domain-management--part-3.md), [Part 4](email-deliverability-domain-warm-up-and-domain-management--part-4.md), [Part 5](email-deliverability-domain-warm-up-and-domain-management--part-5.md), [Part 6](email-deliverability-domain-warm-up-and-domain-management--part-6.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Tracking and monitoring

Telnyx provides delivery events across the message lifecycle. Key events for deliverability monitoring:

| Event | When | Webhook event type |
| --- | --- | --- |
| `queued` | Message accepted and queued for delivery | `email.queued` |
| `sent` | Accepted by the Telnyx outbound MTA for delivery | `email.sent` |
| `delivered` | Receiving server accepted the message | `email.delivered` |
| `bounced` | Terminal non-delivery — ordinary bounce, queue expiry, admin bounce, or OOB bounce | `email.bounced` |
| `expired` | Retries exhausted before delivery (recipient status; publishes `email.bounced`) | `email.bounced` |
| `deferred` | Temporary failure, MTA will retry | `email.deferred` |
| `complained` | Telnyx received an individual provider feedback report | `email.complained` |
| `opened` | Recipient opened the message (tracking pixel) | `email.opened` |
| `clicked` | Recipient clicked a tracked link | `email.clicked` |
| `unsubscribed` | Recipient unsubscribed | `email.unsubscribed` |

Delivery webhooks are **recipient-scoped**: one recipient produces one callback with its own `recipient_id` and its own status. A send to five addresses produces five `email.delivered` callbacks, not one. See [Webhooks & Events](webhooks-events.md).

### Webhooks

Configure webhooks on your sending domain to receive delivery events in real time. See [Webhooks & Events](webhooks-events.md).

### Event polling

Poll delivery events with `GET /v2/email_events` — useful for agents and services without a public webhook URL:

```
curl "https://api.telnyx.com/v2/email_events?email_id=EMAIL_ID" \
  -H "Authorization: Bearer ***"
```

The message filter parameter is `email_id`, not `message_id` or `email_message_id`. Unrecognized query parameters are **silently ignored**, so a wrong name returns every event for the account rather than an error.

## Message size limits

Oversized messages are rejected before sending, and large messages hurt deliverability regardless. Three ceilings apply:

| Limit | Value | Failure |
| --- | --- | --- |
| Message body (`html_body` + `text_body`, decoded) | 1 MB | `422` |
| Total message (decoded body + decoded attachments) | 25 MB | `422` |
| HTTP request body | 150 MB | `413` |

Attachments are base64-encoded in transit, so a 25 MB message occupies roughly 33 MB on the wire — Telnyx measures the **decoded** size. Keep production messages far below these ceilings: large images inflate spam scores and slow rendering. Host images and link to them rather than attaching them. See [Error Codes](error-codes.md) for the full breakdown.

## Best practices and the reasoning behind them

- **Authentication** — Publish SPF, DKIM, and DMARC, and verify your domain. DMARC is what makes the other two meaningful to a receiver evaluating the `From:` header your recipient reads.
- **Reputation** — Increase volume gradually and keep bounce and complaint rates low. Providers evaluate rate, not count: a hundred bounces out of a hundred sends is catastrophic, while a hundred out of a million is unremarkable.
- **Content** — Always send a plain-text alternative alongside HTML, keep subject lines honest, and avoid obscuring links. Filters are detecting evasion; give them nothing to detect.
- **List hygiene** — Remove hard bounces, honor unsubscribes including RFC 8058 one-click, and let suppression lists do their job. Every send to a dead address is evidence that your consent process is weak.
- **Monitoring** — Subscribe to bounce and complaint webhooks *before* your first production send. Deliverability problems compound: by the time you notice degraded delivery without instrumentation, the reputation damage is already done.

## What to do when delivery fails

| Signal | What it means | Response |
| --- | --- | --- |
| `email.deferred` | Temporary 4xx; retries in progress | Nothing — do not resend. Persistent deferrals against one provider indicate throttling; reduce volume to that provider |
| `bounce_category: permanent` | The MTA classified the failure as a permanent bounce | Check `error_evidence.enhanced_code` before concluding the address is bad. Qualifying bounces (`5.1.x`, `5.2.x`, or a 5xx with no enhanced code) are auto-suppressed asynchronously — a suppression may not be visible the instant the webhook arrives |
| `bounce_category: transient` | Retries exhausted | Check whether the provider was throttling you; this is a volume or reputation signal |
| `bounce_category: oob` | Accepted, then asynchronously rejected | Treat as a hard bounce; the same enhanced-code suppression rules apply |
| `error_evidence.enhanced_code` starting `5.7` | Security or policy rejection | Not auto-suppressed. Read `error_evidence.message` to tell authentication failure apart from reputation or content policy, then fix the indicated cause |
| `email.complained` | A recipient reported the message as spam | Auto-suppressed (asynchronously). Review consent, targeting, and frequency |
| `reputation_suspended` | Reputation band dropped to `poor` | Sending is halted. Contact support after correcting list quality |

The general rule: **4xx means wait, 5xx means stop.** Telnyx handles the waiting for you, and handles the stopping by suppressing recipients whose bounces qualify under the enhanced-code rules above. Your job is the layer neither of those can address — understanding why the address was bad or the content unwanted in the first place.

## Troubleshooting

### Verification fails to reach `verified`

If `POST /verify` returns a domain that's still `pending` or `failed`, check the `verification` map and the `dns_records` array:

- **Propagation delay** — DNS changes can take minutes to hours to propagate. Wait and retry. The `actual_value` field shows what Telnyx last observed; if it's `null`, the record hasn't been seen yet.
- **Wrong host format** — publish the record under the exact `host` shown (e.g. `telnyx1._domainkey.example.com` for DKIM, not `_domainkey.example.com`). Don't append your domain to an already-fully-qualified host.
- **Missing required records** — ownership and DKIM must verify (plus MX if `inbound_enabled`). SPF and DMARC are optional but recommended.
- **SPF with multiple providers** — if you already have an SPF record, merge the `include:spf.telnyx.com` directive into it. Two SPF records invalidate each other.
- **DMARC** — Telnyx verifies any valid `v=DMARC1` record, so a custom policy (e.g. `p=reject` with your own `rua`) verifies fine. A malformed record reports `failed`.

### Recovering from `degraded`

A `degraded` domain was verified but its DNS drifted. To recover:

1. Fetch the records: `GET /email_domains/{id}/dns_records`.
2. Compare each record's `value` (expected) against `actual_value` (observed) — any `status: "failed"` record has drifted.
3. Correct the record at your DNS provider.
4. Re-verify: `POST /email_domains/{id}/verify`. On success the domain returns to `verified`.

The drift monitor also re-checks degraded domains periodically and will auto-recover them once DNS matches.

A `suspended` domain cannot be recovered via verification — the verifier short-circuits and won't unsuspend. Suspension is an admin action; contact Telnyx support if your domain is suspended.

## Related documentation

- [Deliverability and Domain Warm-up](deliverability-and-domain-warm-up.md) — setup and warm-up procedures
- [Error Codes](error-codes.md) — complete error reference
- [Webhooks & Events](webhooks-events.md) — event types and payloads
- [Domains & DKIM](domains-dkim.md) — domain registration and DNS records
- [Suppressions](suppressions.md) — suppression list behavior
