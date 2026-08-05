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

*Part 3 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Batch-specific errors

Batch requests (`POST /email_messages/batch`, up to 50 messages) return `207 Multi-Status` when one or more messages fail — including an all-failed batch — with per-message errors:

```
{
  "data": [/* successful messages */],
  "errors": [
    {
      "index": 1,
      "code": "forbidden",
      "message": "Domain is not verified"
    }
  ],
  "meta": {
    "total": 2,
    "failed": 1,
    "succeeded": 1
  }
}
```

Each batch error entry has `index` (position in your `messages` array), `code`, and `message`:

| Error code | Cause |
| --- | --- |
| `bad_request` | Malformed message entry, missing required fields, a template render error, or a field validation failure for that message. |
| `validation_error` | Field validation failed for that message. |
| `unprocessable_entity` | That message exceeded a size limit — either the 1 MB decoded body or the 25 MB total message ceiling. Note this is a **per-message** failure: the rest of the batch still processes. See [Request and message size limits](error-codes-and-event-lifecycle-request-and-message-size-limits.md). |
| `forbidden` | Domain not verified or from-address not allowed. |
| `not_found` | Template ID or domain not found (for template sends). |
| `recipient_suppressed` | All recipients of that message are suppressed. |
| `reputation_suspended` | Sending suspended for the domain's reputation band. |
| `service_unavailable` | Upstream dependency unavailable for that message. |

## Codes owned by other services

The Telnyx email product spans several services. A few codes documented here are returned by services **other than** the Email API, which means their exact status, code, and detail can change independently of this page. Verify these against the owning service's API reference before depending on the precise shape:

| Area | Owning service | Notes |
| --- | --- | --- |
| Shared-domain mutation (`10008`) | telnyx-email-domains | Returned as `403 Forbidden` when mutating a shared domain you don't own. |
| Unsubscribe-group deletion conflict (`40901`) | email-blocks | Returned by the suppressions/unsubscribe-group surface. |
| `/v2/email_domains` troubleshooting and domain verification errors | telnyx-email-domains | Domain registration, DNS record generation, verification, and drift monitoring all live in the domains service. |
| Webhook CRUD (`/email_domains/{domain_id}/webhooks`) | telnyx-email-domains | The Email API only resolves webhook targets at publish time; it does not serve these routes. |

**Error codes are not globally unique across Telnyx email services.** `10008` is the clearest example: the email-domains service returns it as a `403 Forbidden` for shared-domain mutation, while the Email API returns the same code as a `503 Service Unavailable` when diagnostics authentication is unavailable. Always interpret a code together with **both** the HTTP status and the endpoint that returned it — never on the code alone.

## The two-layer model

Telnyx tracks an outbound email at two levels, and conflating them is the most common source of confusion.

| Layer | What it tracks | Values written by the outbound path |
| --- | --- | --- |
| **Message** (`email_messages.status`) | Request lifecycle — did we accept and process your API call? | `queued`, `scheduled`, `sandbox`, `sending`, `completed`, `cancelled`, `failed` |
| **Recipient** (`email_recipients.status`) | Delivery outcome — what happened to this one address? | `queued`, `sent`, `gw_reject`, `deferred`, `delivered`, `bounced`, `failed`, `expired`, `cancelled`, `injection_timeout` |

The message layer answers "did Telnyx take the job?". The recipient layer answers "did the mail arrive?". A message reaches `completed` when every one of its recipients has reached a terminal state — `completed` means *finished*, not *delivered*. The message layer moves to `failed` only on a pre-dispatch rejection that stops the whole request, such as a scheduled send that exceeds your daily send limit at fire time. Transport outcomes — `delivered`, `bounced`, `deferred` — are **never** written onto the message row.

Treat the message-level values as a description of current behavior, not a frozen enum. The authoritative delivery state is always the recipient row, and that is what every delivery webhook and every Email Detail Record describes. Build your logic on the recipient layer.

The recipient status `sending` exists in the schema and the transition table, but the current outbound path never writes it — recipients go from `queued` straight to an injection outcome. Don't build branching that waits to observe it.
