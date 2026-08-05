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

*Part 1 of 8 — see also: [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Overview

The Telnyx Email API is a full email platform: transactional and marketing sending with attachments, templates, scheduling, and batch operations — plus open/click/unsubscribe tracking, automatic suppressions, group-scoped unsubscribe management, and a complete event lifecycle from queued to delivered.

All requests use the production base URL `https://api.telnyx.com/v2` and an `Authorization: Bearer YOUR_API_KEY` header.

## Send a message

Send an email with `POST /email_messages`. The only required fields are `from` and `to`; `subject` is required unless you're sending with `template_id`.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": {
      "email": "sender@example.com",
      "name": "Telnyx Notifications"
    },
    "to": [
      {
        "email": "recipient@example.com",
        "name": "Ada Lovelace"
      }
    ],
    "subject": "Welcome",
    "html_body": "<h1>Welcome, Ada!</h1><p>Thanks for signing up.</p>",
    "text_body": "Welcome, Ada! Thanks for signing up."
  }'
```

### Address fields

| Field | Type | Notes |
| --- | --- | --- |
| `from` | string \| object | A plain email string or `{email, name}`. |
| `from_name` | string | Optional display name when `from` is a string; overrides `from.name`. |
| `to` | array (min 1) | Each item is a string or `{email, name}`. |
| `cc` | array | Same item shape as `to`. |
| `bcc` | array | Same item shape as `to`. |
| `reply_to` | string \| object | Reply-to address. When provided as an object, only the email is stored. |

### Body, headers, and attachments

| Field | Type | Notes |
| --- | --- | --- |
| `subject` | string | Required unless `template_id` is supplied. |
| `html_body` | string | HTML body. Omitted from create and list responses; returned by `GET /email_messages/{id}`. |
| `text_body` | string | Plain-text body. Omitted from create and list responses; returned by `GET /email_messages/{id}`. |
| `headers` | object of string keys to string values | Custom headers. Write-only — not returned in responses. |
| `tags` | array of strings | Tags for categorization. Write-only. |
| `metadata` | object | Custom metadata. Write-only. |
| `attachments` | array | See below. |

Send an attachment by base64-encoding its content:

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "subject": "Invoice attached",
    "text_body": "Your invoice is attached.",
    "attachments": [
      {
        "filename": "invoice.pdf",
        "content_type": "application/pdf",
        "content": "JVBERi0xLjQK..."
      }
    ]
  }'
```

**Request** `attachments[]` fields:

| Field | Default | Notes |
| --- | --- | --- |
| `filename` | `"attachment"` | Attachment file name. |
| `content_type` | `application/octet-stream` | MIME type. |
| `content` | `""` | Base64-encoded file content. |
| `disposition` | `"attachment"` | Use `inline` for images referenced from the HTML body. |
| `content_id` | `null` | Content-ID for an inline attachment, referenced as `cid:<content_id>` in the HTML body. |

**Response** `attachments[]` returns `filename`, `content_type`, `url`, `sha256`, `size_bytes`, `disposition`, and `content_id`. The base64 `content` you submitted is never returned — fetch the stored file from `url` instead.

## Templates

Send with a stored template instead of inline bodies. Provide `template_id` and optional `template_variables` for Liquid rendering. When you use a template, `subject` is optional — the template's subject is rendered; if the template has no subject or renders empty, the request returns `400`.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "template_id": "7a7c1a2b-1111-4c72-8c21-2bbf3d40c123",
    "template_variables": {
      "first_name": "Ada"
    }
  }'
```

Non-object `template_variables` values may cause a 422 validation error on message creation. Pass an object.

## Schedule a send

Set `scheduled_at` to an ISO 8601 timestamp in the future to schedule the message. The response returns `202` with `"status": "scheduled"` and a `scheduled_at` field.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "subject": "Scheduled reminder",
    "text_body": "This was scheduled.",
    "scheduled_at": "2026-08-01T09:00:00Z"
  }'
```

Invalid or past `scheduled_at` timestamps are silently ignored and the email is sent immediately.

`send_at` is a deprecated alias for `scheduled_at`. It is still accepted on requests for backward compatibility, but responses always return `scheduled_at`. When both are supplied, `scheduled_at` wins. Use `scheduled_at` in new integrations.

Cancel a scheduled message before it sends with `DELETE /email_messages/{email_id}/schedule`:

```
curl -X DELETE https://api.telnyx.com/v2/email_messages/{email_id}/schedule \
  -H "Authorization: Bearer ***"
```

A successful cancel returns `200` with the message in `"status": "cancelled"`. The `scheduled_at` value persists on the record even after cancellation.

## Idempotency

Pass an optional `Idempotency-Key` HTTP header to safely retry a send without creating duplicates. Generate a unique UUID v4 for each logical request, then reuse the same key only when retrying that operation with the same request body. Keys are retained for up to 24 hours, and only successful responses are replayed. Do not include sensitive data in the key.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Idempotency-Key: 8e03978e-40d5-43e8-bc93-6894a57f9326" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "subject": "Order confirmation",
    "text_body": "Order #12345 confirmed."
  }'
```

The first successful request returns its normal status and response body. A retry with the same key and request returns the stored status and body and adds this response header:

```
Idempotent-Replayed: true
```

The header is omitted for first-time requests and error responses. Reusing a key with a different request returns `422` with code `10027`; sending the same key while the original request is still running returns `409` with code `10036`. Empty, duplicate, malformed, or overlong key headers return `400` with code `10015`. If Edge cannot provide idempotency protection for a keyed request, it fails closed with `503` and code `10016`.

`idempotency_key` is not a request-body field. Put the key only in the `Idempotency-Key` HTTP header.
