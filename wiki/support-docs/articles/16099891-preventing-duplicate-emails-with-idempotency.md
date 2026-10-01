---
title: "Preventing duplicate emails with idempotency"
summary: "Network timeouts can leave you unsure whether an email send succeeded. Add an Idempotency-Key header so you can safely retry the same logical send without creating a second message."
sources:
- url: "https://support.telnyx.com/en/articles/16099891-preventing-duplicate-emails-with-idempotency"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16099891-preventing-duplicate-emails-with-idempotency.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16099891-preventing-duplicate-emails-with-idempotency.md -->

# Preventing duplicate emails with idempotency

Network timeouts can leave you unsure whether an email send succeeded. Add an `Idempotency-Key` header so you can safely retry the same logical send without creating a second message.

---

## **Send with an idempotency key**

Generate one unique key for each logical send. UUID v4 values are a good choice. Put the key in the HTTP header—not in the JSON body:

```
curl -i -X POST "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 7e85df5e-9f71-4ce9-a57a-811dd96c031a" \
  -d '{
    "from": "sender@mail.yourcompany.com",
    "to": ["recipient@example.com"],
    "subject": "Your receipt",
    "text_body": "Thanks for your order."
  }'
```

If the client times out or loses the response, repeat the same request with the same key and the same body:

```
curl -i -X POST "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 7e85df5e-9f71-4ce9-a57a-811dd96c031a" \
  -d '{
    "from": "sender@mail.yourcompany.com",
    "to": ["recipient@example.com"],
    "subject": "Your receipt",
    "text_body": "Thanks for your order."
  }'
```

When Edge replays a stored successful response, the response includes `Idempotent-Replayed: true`. The original HTTP status and body are replayed; a successful replay is not automatically changed to `200`.

---

## **Follow these key rules**

- Use 1 to 255 letters, numbers, hyphens, or underscores.
- Use one key per logical operation.
- Reuse a key only for the same method, path, query, and request body.
- Retry uncertain outcomes with the same key; use a new key for an intentionally new email.
- Successful responses are retained for 24 hours. After that window, the same key may no longer prevent a duplicate.

**Do not send `idempotency_key` in the JSON body.** The Email API ignores the legacy body field, so two direct requests with only that field can create two different messages.

---

## **Handle key-related responses**

|  |  |
| --- | --- |
| **Response** | **Meaning and action** |
| `Idempotent-Replayed: true` | The stored successful response was replayed. Do not create another send. |
| `400 / 10015` | The header was empty, duplicated, malformed, or longer than 255 bytes. Generate one valid value. |
| `409 / 10036` | The same key is still being processed. Retry later with the same key and unchanged request. |
| `422 / 10027` | The key was already used with a different request. Do not force a retry; use a new key only if you intend to create a new operation. |
| `413 Payload Too Large` | A keyed request body exceeded the 8,000,000-byte Edge replay-protection cap. Reduce the request before retrying. |

Only successful 2xx responses are stored for replay. If the API returns a normal validation or authorization error, fix the error before deciding whether the corrected operation needs a new key.

---

## **Use one key for the whole batch**

For a batch send, the header protects the complete request. It does not assign a separate key to each item:

```
curl -i -X POST "https://api.telnyx.com/v2/email_messages/batch" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 1c5c7c41-1bf0-463e-a99a-47c5620cc699" \
  -d '{
    "messages": [
      {
        "from": "sender@mail.yourcompany.com",
        "to": ["one@example.com"],
        "subject": "First message",
        "text_body": "Hello one"
      },
      {
        "from": "sender@mail.yourcompany.com",
        "to": ["two@example.com"],
        "subject": "Second message",
        "text_body": "Hello two"
      }
    ]
  }'
```

Reusing the original key replays the stored whole-batch response. If a batch response contains failed items and you want to retry only those items, create a new batch containing only the failed items and use a new key.

---

## **Avoid the most common duplicate-send bugs**

- Do not generate a new key for every network retry.
- Do not reuse one static key for different emails.
- Do not change whitespace, recipients, content, or query parameters while retrying the same key.
- Do not rely on a key after the 24-hour retention window.

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
- [Understanding Telnyx Email errors and message size limits](https://support.telnyx.com/en/articles/16099890-understanding-telnyx-email-errors-and-message-size-limits)
- [Creating and sending email templates](https://support.telnyx.com/en/articles/16099893-creating-and-sending-email-templates)
- [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send)
