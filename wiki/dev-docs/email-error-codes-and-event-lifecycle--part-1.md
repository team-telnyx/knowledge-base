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

*Part 1 of 9 — see also: [Part 2](email-error-codes-and-event-lifecycle--part-2.md), [Part 3](email-error-codes-and-event-lifecycle--part-3.md), [Part 4](email-error-codes-and-event-lifecycle--part-4.md), [Part 5](email-error-codes-and-event-lifecycle--part-5.md), [Part 6](email-error-codes-and-event-lifecycle--part-6.md), [Part 7](email-error-codes-and-event-lifecycle--part-7.md), [Part 8](email-error-codes-and-event-lifecycle--part-8.md), [Part 9](email-error-codes-and-event-lifecycle--part-9.md)*

Reference for the Telnyx Email API's two error families — synchronous HTTP errors (10xxx) returned on the API request itself, and asynchronous delivery errors (30xxx) reported later via webhooks and Email Detail Records — together with the per-recipient event lifecycle that drives them.

## Overview

The Telnyx Email API surfaces failures in two distinct families that are not interchangeable:

- **Synchronous HTTP errors** — returned in the response to your API request. These use the `10xxx` taxonomy (plus a few string codes such as `recipient_suppressed` and `reputation_suspended`).
- **Asynchronous delivery errors** — reported later via webhooks and Email Detail Records (EDRs) after a `202 Accepted`. These use the `30xxx` taxonomy.

A `30xxx` code never appears in an HTTP response body, and an HTTP code never appears in `error_evidence`. For endpoint-specific errors, see the response examples in each endpoint's API reference.

## Error response format

Most errors follow the standard Telnyx v2 error shape. Exceptions: batch errors use `{index, code, message}` (see [Batch-specific errors](error-codes-batch-specific-errors.md)), and some template render errors use `{code, message}`.

```
{
  "errors": [
    {
      "code": "10015",
      "title": "Validation Failed",
      "detail": "subject can't be blank"
    }
  ]
}
```

| Field | Description |
| --- | --- |
| `code` | Machine-readable error code (see table below). |
| `title` | Short human-readable summary. |
| `detail` | Specific error message with context. |

## Request and message size limits

Size failures are a common source of confusion because three different ceilings apply at three different layers. They are not the same number.

| Limit | Value | Enforced by | Failure mode |
| --- | --- | --- | --- |
| Message body (`html_body` + `text_body`, decoded) | 1 MB | Email API | `422` with code `10015`, title "Bad Request", detail "body exceeds size limit (maximum 1 MB)" |
| Total message (decoded body + decoded attachments) | 25 MB | Email API | `422` with code `10015`, title "Bad Request", detail "message exceeds size limit (maximum 25 MB)" |
| HTTP request body | 150 MB | Phoenix request parser | `413` with code `10015` |
| Idempotency-keyed replay capture | 8 MB | Telnyx Edge (API gateway) | `413 Payload Too Large` — an idempotency-keyed request over 8 MB is rejected at Edge before reaching the Email API. Unkeyed requests are not subject to this cap. |

**8 MB is not a request-body limit.** It is the Edge gateway's `request_body_cap_bytes` for **idempotency-keyed replay** only. A keyed request over 8 MB is rejected at the Edge with `413 Payload Too Large` — it never reaches the Email API. Unkeyed requests bypass this cap entirely. The limits that actually reject a message body are the 1 MB body and 25 MB total enforced by the Email API, which return `422`.

Attachments are base64-encoded in the request, so a 25 MB message occupies roughly 33 MB on the wire. The Email API measures **decoded** bytes.

## HTTP status codes

| Status | Meaning | When |
| --- | --- | --- |
| 200 | OK | Successful request or idempotent replay. |
| 201 | Created | Resource created (e.g. template creation). |
| 202 | Accepted | Email accepted for sending (queued). |
| 207 | Multi-Status | All batch responses (including all-success). `data` contains successes, `errors` contains failures. |
| 400 | Bad Request | Validation error, malformed body, or invalid `Idempotency-Key` header. |
| 401 | Unauthorized | Missing or invalid API key. |
| 403 | Forbidden | Domain not verified/suspended/degraded, sender address not allowed, shared domain is read-only, or the account is inactive. |
| 404 | Not Found | Resource (email, template, domain) not found. |
| 409 | Conflict | A request with the same `Idempotency-Key` is still being processed, or a resource conflict (e.g. deleting an unsubscribe group with active suppressions). |
| 413 | Payload Too Large | Request body exceeds the 150 MB Phoenix parser ceiling. Responses use code `10015` with detail "The request payload exceeds the maximum allowed size". |
| 422 | Unprocessable Entity | Changeset validation error, message/body size limit exceeded, idempotency fingerprint conflict, or all recipients suppressed. |
| 429 | Too Many Requests | Daily send limit exceeded, or sending suspended due to poor domain reputation. |
| 500 | Internal Server Error | Unexpected server error. |
| 503 | Service Unavailable | Upstream dependency or Edge idempotency protection unavailable. |
