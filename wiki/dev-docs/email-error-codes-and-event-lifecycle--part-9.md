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

*Part 9 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Troubleshooting

### "Domain is not verified"

1. Check `GET /v2/email_domains` to see the domain status.
2. Ensure all required DNS records — ownership and DKIM, plus MX if `inbound_enabled` is true — are published and match the records returned by `GET /v2/email_domains/{domain_id}/dns_records`.
3. Call `POST /v2/email_domains/{domain_id}/verify` after DNS propagates.
4. For a controlled zero-setup test, use `onboarding@<shared-domain>` and send only to the account owner's verified email address.

### "sender address is not allowed"

The `from` address must be on a verified domain you own. Shared-domain sends must use `onboarding@<shared-domain>` and can target only the account owner's verified email address.

### "Idempotency-Key header is invalid"

- Generate a UUID v4 (`uuidgen` or `crypto.randomUUID()`).
- Pass it as an HTTP header: `Idempotency-Key: 8e03978e-40d5-43e8-bc93-6894a57f9326`.
- Do **not** include it in the JSON body — it's a header only.
- One key per logical request. Reuse only for exact retries.

### Sending suspended (`reputation_suspended`)

Your domain's reputation band dropped to `poor` — usually from high bounce or complaint rates. See [Deliverability and Domain Warm-up](deliverability-and-domain-warm-up.md) for recovery guidance.

### Choosing a retry strategy

Retry decisions belong on the **error code**, not the HTTP status. Two errors that share a status can need opposite handling.

| Error | Status | Retry? | How |
| --- | --- | --- | --- |
| `10011` (daily send limit) | 429 | Yes | The limit resets at midnight UTC. Queue the work locally and resume after the reset — backing off in seconds will not help. |
| `reputation_suspended` | 429 | **No** | Waiting does not clear it. Stop sending on that domain, reduce bounce and complaint rates, then confirm the band recovered. |
| `10036` (idempotency in flight) | 409 | Yes | Retry with the **same** key and body. A new key would send a duplicate. |
| `10027` (idempotency fingerprint) | 422 | No | The body differs from the original. Fix the body or use a new key. |
| `10016` (service unavailable) | 503 | Yes | Retry the same request with the same `Idempotency-Key`, with exponential backoff. |
| `10019` / `10000` / `500` | 500 | Yes | Retry with the same `Idempotency-Key`. Contact support if persistent. |
| `10015` (validation / size) | 400, 413, 422 | No | The request is malformed or too large. Retrying it unchanged always fails. |
| `10007` / `20012` (forbidden / inactive) | 403 | No | Fix domain verification, sender authorization, scope, or account balance first. |
| `recipient_suppressed` | 422 | No | Every recipient is suppressed. Remove them or send to different addresses. |

Never retry a `4xx` other than `409` and `429` without changing the request — the outcome is deterministic. And when you do retry a send, always reuse the original `Idempotency-Key` so a retry that races a slow success cannot deliver the message twice.

### Delivery failed after a `202 Accepted`

A `202` only confirms acceptance for sending. If the message never arrived, the failure is asynchronous — look at the [30xxx delivery error](error-codes-and-event-lifecycle-the-30xxx-taxonomy.md) on the recipient's webhook or event, not at the HTTP response. Start with `error_evidence.code`:

- `30001` — permanent rejection. Remove the address.
- `30002` — temporary; Telnyx is already retrying. Do not resubmit.
- `30004` — the recipient was suppressed before any attempt.
- `30005` — retries were exhausted; the recipient status is `expired`.

## Related

- [Webhooks & Events](webhooks-events.md) — subscribe, verify signatures, poll, paginate
- [Deliverability](deliverability.md) — reputation, authentication, and bounce handling
- [Suppressions](suppressions.md) — how auto-suppression works and how to manage the list
- [Send an email](send-an-email.md) — the send API and its fields
