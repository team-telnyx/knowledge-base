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

*Part 2 of 9 — see also: [Part 1](email-error-codes-and-event-lifecycle--part-1.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Synchronous error code reference

Every code in this section is a **synchronous** error — returned in the HTTP response to your API request. Delivery failures that happen after a `202 Accepted` use the separate [30xxx taxonomy](error-codes-and-event-lifecycle-asynchronous-delivery-errors-30xxx.md).

### 400 — Bad Request

| Code | Title | Cause |
| --- | --- | --- |
| `10015` | Bad Request / Validation Failed | Missing or invalid fields in the request body (e.g. `email is required`, `subject must be a non-empty string`). |
| `10015` | Invalid Idempotency-Key | The `Idempotency-Key` header is empty, duplicated, malformed, or exceeds the length limit. Generate a UUID v4 and pass it as a single header, not a body field. |

### 401 — Unauthorized

| Code | Title | Cause |
| --- | --- | --- |
| `10006` | Not authorized | The `Authorization` header is missing or the API key is invalid, expired, or revoked. |

### 403 — Forbidden

| Code | Title | Cause |
| --- | --- | --- |
| `10007` | Forbidden | Domain is not verified, suspended, degraded, or missing DKIM — or the `from` address is not authorized on the sending domain. |
| `10007` | Forbidden | The request requires the `email:override` scope (used to send to a suppressed recipient) and your API key does not have it. |
| `20012` | Account inactive | The account has been deactivated — commonly out of funds. This is a billing state, not a domain or permission problem. Resolve the account balance before retrying. |
| `10008` | Forbidden | Attempted to `PATCH`, `DELETE`, or `POST …/verify` on a shared domain you don't own. Shared domains are read-only for non-owners. **Owned by the email-domains service** — see [Codes owned by other services](error-codes-and-event-lifecycle-codes-owned-by-other-services.md). |

### 404 — Not Found

| Code | Title | Cause |
| --- | --- | --- |
| `10001` | Not Found | Email message, template, or domain not found. Check the ID and your account scope. Both explicit application 404s and framework-level routing 404s return `10001` — there is no string `"404"` fallback code. |

### 409 — Conflict

| Code | Title | Cause |
| --- | --- | --- |
| `10036` | Resource is being processed | A request with the same `Idempotency-Key` is **still being processed**. Retry later with the same key and the same request body. |
| `40901` | Conflict | Deleting an unsubscribe group that has active suppressions (without `?force=true`). Remove the suppressions first or pass `force=true`. **Owned by the email-blocks service** — see [Codes owned by other services](error-codes-and-event-lifecycle-codes-owned-by-other-services.md). |

### 422 — Unprocessable Entity

| Code | Title | Cause |
| --- | --- | --- |
| `10015` | Validation Failed | Changeset validation error (e.g. `subject can't be blank`, invalid `webhook_url`, bad address format). |
| `10015` | Bad Request | Message size limit exceeded — 1 MB decoded body or 25 MB total message. See [Request and message size limits](error-codes-and-event-lifecycle-request-and-message-size-limits.md). |
| `10027` | Idempotency Conflict | The `Idempotency-Key` was already used for a **different** request body. Use a new key for a new request; reuse keys only for exact retries. |
| `recipient_suppressed` | Recipient Suppressed | All recipients are suppressed — the email was not sent. The response includes a top-level `suppressed` array alongside `errors`, each entry carrying `to`, `reason`, `scope`, and `override_allowed`. |

### 429 — Too Many Requests

| Code | Title | Cause | Retry? |
| --- | --- | --- | --- |
| `10011` | Too Many Requests | The account's **daily send limit** was exceeded. The detail names the limit and states that it resets at midnight UTC. The send is rejected before message creation — no message record, no billing, no MTA injection. | Yes, after the daily reset. |
| `reputation_suspended` | Sending Suspended | The sending domain's reputation band is `poor` — sending is suspended until reputation recovers. Rejected before message creation. | **No.** See [Deliverability](deliverability.md). |

**Do not treat every `429` as a transient rate limit.** Branch on the error code, not the status. `10011` clears on its own at midnight UTC. `reputation_suspended` does **not** clear by waiting — retrying it in a backoff loop will never succeed and worsens the reputation signal. Stop sending on that domain and remediate the underlying bounce/complaint rates first.

### 500 — Internal Server Error

| Code | Title | Cause |
| --- | --- | --- |
| `10019` | Internal Server Error | Unexpected server-side error (e.g. `Failed to create batch validation`). Retry with the same `Idempotency-Key`. If persistent, contact support. |
| `10000` | Internal Server Error | Returned by specific internal-failure paths, including a failed GDPR email-data deletion and email trace retrieval. Same handling as `10019`. |
| `500` | Internal Server Error | Framework fallback error response. Same handling as `10019`. |

### 503 — Service Unavailable

| Code | Title | Cause |
| --- | --- | --- |
| `10016` | Service Unavailable | An upstream dependency (e.g. the email domain service) or Edge idempotency protection is temporarily unavailable. Retry with the same `Idempotency-Key`. |

## Idempotency-specific errors

When using the `Idempotency-Key` header, idempotency is enforced at the Telnyx Edge (API gateway) before the request reaches the Email API. The same key can produce **three distinct outcomes**, and they must be handled differently:

| Outcome | HTTP | Code | What happened | Action |
| --- | --- | --- | --- | --- |
| Original still in flight | 409 | `10036` | The first request with this key is **still being processed**. No second send occurred. | Wait and retry with the **same** key and the **same** body. Do not generate a new key — that would send twice. |
| Same key, different body | 422 | `10027` | The key was already used with a **different request fingerprint**. The new request was rejected without sending. | Generate a new key. Reuse a key only for byte-identical retries of the same logical request. |
| Original already completed | *original 2xx* | *original body* | The first request finished. The gateway **replays its stored response verbatim** — including the original status and body — and adds an `idempotent-replayed: true` response header. | Nothing. The message was sent exactly once. Check for the `idempotent-replayed` header if you need to distinguish a replay from a fresh send. |

Two further failure modes are specific to the idempotency layer itself:

| Code | HTTP | Cause | Action |
| --- | --- | --- | --- |
| `10015` | 400 | Malformed key (empty, duplicate header, overlong) | Generate a valid UUID v4 and pass it as a single `Idempotency-Key` header. |
| `10016` | 503 | Idempotency protection unavailable (fail-closed) | Retry the same request with the same key. The gateway fails closed rather than risking a duplicate send. |

A replay only works while the gateway holds the stored response. Requests whose body exceeds the Edge 8 MB replay cap are rejected at the Edge with `413 Payload Too Large` before reaching the Email API — see [Request and message size limits](error-codes-and-event-lifecycle-request-and-message-size-limits.md).
