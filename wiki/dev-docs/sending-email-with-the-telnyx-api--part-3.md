---
title: Sending Email with the Telnyx API
summary: Covers the Telnyx Email API sending surface — single and batch sends, templates,
  scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups,
  and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope,
  CRUD operations, CSV import/export, and send-time override behavior.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/send-email/index
- url: https://developers.telnyx.com/docs/messaging/email/suppressions
updated_at: 2026-08-05T13:55:17Z
---

# Sending Email with the Telnyx API

*Part 3 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Errors

API errors return structured JSON. The standard error envelope:

```
{
  "errors": [
    {
      "code": "10015",
      "title": "Bad Request",
      "detail": "subject is required when not using a template"
    }
  ]
}
```

### Common error codes

| HTTP | Code | Meaning |
| --- | --- | --- |
| 400 | `10015` | Validation failed — missing or invalid fields. |
| 400 | `10015` | Invalid `Idempotency-Key` header — empty, duplicate, malformed, or overlong. |
| 401 | `10006` | Authentication failed — check your API key. |
| 403 | `10007` | Forbidden — the Email API's general sending-policy error. Covers an unverified, degraded, or suspended sending domain, a domain with no active DKIM key, a sender that doesn't match the domain's sending profile, and trial-account recipient restrictions. Inspect `detail` for the specific reason. |
| 404 | `10001` | Not found — the message, domain, or resource doesn't exist. |
| 409 | `10036` | A request with the same idempotency key is still being processed. |
| 413 | `10015` | Request body exceeds 8,000,000 bytes. |
| 422 | `10015` | Validation error (changeset). |
| 422 | `10027` | The idempotency key was already used for a different request. |
| 422 | `recipient_suppressed` | All recipients suppressed. Returns a top-level `suppressed` array. |
| 429 | `reputation_suspended` | Sending suspended — the sending domain's reputation band is `poor`. |
| 503 | `10016` | Service unavailable — an upstream dependency or Edge idempotency protection is unavailable. |

`recipient_suppressed` (422) uses a non-standard envelope with the `suppressed` array alongside `errors`:

```
{
  "errors": [
    {
      "code": "recipient_suppressed",
      "title": "Recipient Suppressed",
      "detail": "All recipients are suppressed. The email was not sent."
    }
  ],
  "suppressed": [
    {
      "to": "suppressed@example.com",
      "reason": "hard_bounce",
      "scope": "global",
      "override_allowed": false
    }
  ]
}
```

`reputation_suspended` (429) uses a string code rather than a numeric Telnyx code:

```
{
  "errors": [
    {
      "code": "reputation_suspended",
      "title": "Sending Suspended",
      "detail": "Sender domain reputation is too low. Sending has been suspended. Please contact support to resolve deliverability issues."
    }
  ]
}
```

## Batch sending

Send up to 50 messages in a single request with `POST /email_messages/batch`. Each item in the `messages` array is a full `CreateEmailRequest` payload.

```
curl -X POST https://api.telnyx.com/v2/email_messages/batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Idempotency-Key: 20dbec69-bc70-4fed-aec7-2a70af37a8a6" \
  -d '{
    "messages": [
      {
        "from": "sender@example.com",
        "to": ["recipient1@example.com"],
        "subject": "Hello 1",
        "text_body": "Message 1"
      },
      {
        "from": "sender@example.com",
        "to": ["recipient2@example.com"],
        "subject": "Hello 2",
        "text_body": "Message 2"
      }
    ]
  }'
```

The `Idempotency-Key` applies to the entire batch request. Reuse it only when retrying the same batch body; do not add per-message idempotency keys inside `messages`.

- **`207`** — all batch responses use `207 Multi-Status`. When all messages succeed, `errors` is empty and every item is in `data`. When one or more fail, the response contains a `data` array for successes (which may be empty) and an `errors` array for failures.

The `errors` array for a batch uses a per-item shape — each entry has `index` (zero-based position in the request array), `code`, and `message` (not `detail`):

```
{
  "data": [
    {
      "record_type": "email_message",
      "id": "11111111-1111-1111-1111-111111111111",
      "status": "queued"
    }
  ],
  "errors": [
    {
      "index": 1,
      "code": "bad_request",
      "message": "from, to, and subject are required"
    }
  ],
  "meta": {
    "total": 2,
    "succeeded": 1,
    "failed": 1
  }
}
```

Batch item error codes: `bad_request`, `unprocessable_entity`, `not_found`, `forbidden`, `service_unavailable`, `validation_error`, `recipient_suppressed`, and `reputation_suspended`. `unprocessable_entity` is returned when an individual message exceeds the size limits — the rest of the batch still processes.

## Suppression model

A suppression (block) is a record that prevents email from being sent to a recipient address. Telnyx creates suppressions automatically in response to deliverability signals, and you can create them manually via the API. Every suppression has a **reason** — the canonical enum string that describes why the block exists — and a **source** that records how it was created.

### Reasons

| Reason | Created by | Overridable with `ignore_suppression`? |
| --- | --- | --- |
| `hard_bounce` | Auto — permanent bounce or soft-bounce escalation | **No** |
| `spam_complaint` | Auto — ARF feedback (complaint) | **No** |
| `invalid` | Import (SendGrid `invalid_emails`, generic) or internal | **No** |
| `unsubscribe` | Auto — recipient unsubscribed (RFC 8058 or link), or manual group opt-out | **Yes** |
| `manual_block` | Manual — public API `POST /email_blocks`, or CSV import (SendGrid `blocks`, generic `manual_block`) | **Yes** |

The three non-overridable reasons (`hard_bounce`, `spam_complaint`, `invalid`) can never be bypassed by `ignore_suppression` — Telnyx will not deliver to those recipients regardless of the flag. The two overridable reasons (`unsubscribe`, `manual_block`) can be bypassed when you send with `ignore_suppression: true` and an API key that has the `email:override` scope.

### Sources

| Source | Meaning |
| --- | --- |
| `system` | Auto-created by Telnyx (bounce, complaint, or unsubscribe workers) |
| `manual` | Created via the public API or group suppressions sub-resource |
| `import` | Created via CSV import |
| `feedback` | Created from feedback-loop data |

### How auto-suppressions are created

Telnyx's delivery event pipeline classifies incoming KumoMTA log records and enqueues a suppression worker for suppressible events:

- **Spam complaint** — an ARF `Feedback` record creates a `spam_complaint` suppression.
- **Hard bounce** — a `Bounce` or `OOB` record with a `5.1.x` or `5.2.x` enhanced status code, or a `5xx` SMTP code with no enhanced code, creates a `hard_bounce` suppression.
- **Soft-bounce escalation** — repeated `TransientFailure` (deferred) records for the same recipient increment a counter; when the threshold is breached, Telnyx escalates to a `hard_bounce` suppression.
- **Expiration** — a KumoMTA `Expiration` record (system gave up retrying) creates a `hard_bounce` suppression.
- **Unsubscribe** — a recipient unsubscribes via the RFC 8058 one-click flow or the unsubscribe link, creating an `unsubscribe` suppression.

`AdminBounce` records, `5.7.x` enhanced codes (sender-side policy), and other unclassified records are **not** suppressed.

The public API can only create `manual_block` suppressions. Any `reason` value you send to `POST /email_blocks` is ignored — the server forces `reason: manual_block` and `source: manual`. Auto-suppressions (`hard_bounce`, `spam_complaint`, `unsubscribe`) are created by Telnyx internally. CSV import is the one other path that can produce `manual_block` rows, with `source: import`.
