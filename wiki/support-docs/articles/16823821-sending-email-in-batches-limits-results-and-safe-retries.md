---
title: "Sending email in batches: limits, results, and safe retries"
summary: "Send multiple messages with POST /v2/emailmessages/batch. Each item in the messages array is validated independently. Read the result of every item before deciding whether to retry."
sources:
- url: "https://support.telnyx.com/en/articles/16823821-sending-email-in-batches-limits-results-and-safe-retries"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--16823821-sending-email-in-batches-limits-results-and-safe-retries.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--16823821-sending-email-in-batches-limits-results-and-safe-retries.md -->

# Sending email in batches: limits, results, and safe retries

Send multiple messages with `POST /v2/email_messages/batch`. Each item in the `messages` array is validated independently. Read the result of every item before deciding whether to retry.

## Limits and request shape

A batch contains **1 to 1,000 messages**. A request with 1,001 messages, an empty array, or a malformed batch envelope returns `400`. The item cap counts messages, while your daily sending quota counts recipients; these are separate limits.

Each message still has the decoded size limits described in [Understanding Telnyx Email errors and message size limits](https://support.telnyx.com/en/articles/16099890-understanding-telnyx-email-errors-and-message-size-limits). Keep attachment-heavy batches small enough for the applicable request-size limits as well.

```sh
curl -X POST "https://api.telnyx.com/v2/email_messages/batch" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: YOUR_UNIQUE_BATCH_KEY" \
  -d '{
    "messages": [
      {
        "from": "sender@mail.yourcompany.com",
        "to": ["first@example.com"],
        "subject": "Order update",
        "text_body": "Your first order has shipped."
      },
      {
        "from": "sender@mail.yourcompany.com",
        "to": ["second@example.com"],
        "subject": "Order update",
        "text_body": "Your second order has shipped."
      }
    ]
  }'
```

Use your verified sender and permitted recipients. Trial-account recipient restrictions still apply to production sends.

## Always inspect the 207 results

Once the batch is processed, the response is always **`207 Multi-Status`**, whether every item succeeds, some fail, or every item fails. Request-level rejections, such as the 1,001-item validation failure, are separate from this per-item result contract.

- `data` contains the created messages and their IDs/statuses. It may be empty.
- `errors` contains failed items with a zero-based `index`, `code`, and `message`. Map each index back to the original `messages` array, not to the shorter `data` array.
- `meta.total`, `meta.succeeded`, and `meta.failed` summarize the result.

For example, if the first item was accepted and the second had missing required fields:

```json
{
  "data": [
    {
      "record_type": "email_message",
      "id": "11111111-1111-4111-8111-111111111111",
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
  "meta": {"total": 2, "succeeded": 1, "failed": 1}
}
```

Acceptance is not delivery. Save the IDs from `data` and check recipient events or webhooks. A scheduled item is accepted as `scheduled` for a future send, an immediate item as `queued`, and a sandbox item as `sandbox` without real delivery. These variants keep their own status and lifecycle semantics inside the batch's `207` response.

## Retry without duplicating accepted messages

1. Generate one `Idempotency-Key` HTTP header for each logical batch request. The key covers the **whole request**, not individual items; there are no per-message keys inside `messages`.
2. If the response is lost, retry the identical body with the same key. A successful replay preserves the original HTTP status and body. Replaying a recorded `207` does not rerun its failed items.
3. After receiving results, keep all accepted message IDs. Correct the failed items and submit only those items in a **new batch with a new key**. The new array has its own zero-based indexes; retain your original-to-retry mapping.
4. Inspect each failure before retrying. Invalid fields need correction; suppressed recipients and policy failures need remediation. Do not resubmit accepted messages merely because another item failed.

See [Preventing duplicate emails with idempotency](https://support.telnyx.com/en/articles/16099891-preventing-duplicate-emails-with-idempotency) for replay behavior and key errors.

## Related articles

- [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send)
- [Testing Telnyx Email safely with sandbox recipients](https://support.telnyx.com/en/articles/16823822-testing-telnyx-email-safely-with-sandbox-recipients)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
