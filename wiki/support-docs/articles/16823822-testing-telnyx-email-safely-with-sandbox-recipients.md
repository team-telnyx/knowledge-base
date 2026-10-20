---
title: "Testing Telnyx Email safely with sandbox recipients"
summary: "Use sandboxmode: true to test your integration without delivering real mail through the MTA. Sandbox sends are non-billable, consume no sending quota, and their outcomes are excluded from production deliverability statistics and reputation scoring."
sources:
- url: "https://support.telnyx.com/en/articles/16823822-testing-telnyx-email-safely-with-sandbox-recipients"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--16823822-testing-telnyx-email-safely-with-sandbox-recipients.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--16823822-testing-telnyx-email-safely-with-sandbox-recipients.md -->

# Testing Telnyx Email safely with sandbox recipients

Use `sandbox_mode: true` to test your integration without delivering real mail through the MTA. Sandbox sends are non-billable, consume no sending quota, and their outcomes are excluded from production deliverability statistics and reputation scoring.

## Send a sandbox message

Use your API key and an authorized sender, and explicitly enable sandbox mode:

```sh
curl -X POST "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "sender@mail.yourcompany.com",
    "to": ["delivered@test.telnyx.com"],
    "subject": "Sandbox delivery test",
    "text_body": "Exercise my event handler safely.",
    "sandbox_mode": true
  }'
```

The accepted single-send response returns `202` and parent status `sandbox`. Save its message ID. Sandbox still validates your request and sender permissions; it is not an authentication bypass.

The reserved addresses below simulate outcomes **only in sandbox mode**. An address alone does not enable sandbox: always set `sandbox_mode: true`. Do not use these recipients for a production delivery test.

## Choose a deterministic recipient

Use these exact eight addresses at `test.telnyx.com`:

| Recipient | Simulated outcome |
| --- | --- |
| `delivered@test.telnyx.com` | Successful delivery (`email.delivered`). |
| `hard-bounce@test.telnyx.com` | Permanent bounce (`email.bounced`, recipient status `bounced`, simulated SMTP `550`, enhanced code `5.1.1`) and a queued `hard_bounce` suppression. |
| `soft-bounce@test.telnyx.com` | Soft bounce (`email.bounced`, simulated SMTP `450`, enhanced code `4.2.0`). This is a synthetic soft-bounce outcome, not queue expiry. |
| `complaint@test.telnyx.com` | Complaint event (`email.complained`); the recipient status remains `sent`, and a `spam_complaint` suppression is queued. |
| `suppressed@test.telnyx.com` | Suppression (`email.suppressed`, reason `suppressed_recipient`). |
| `invalid@test.telnyx.com` | Failure (`email.failed`, reason `invalid_recipient`). |
| `dkim-fail@test.telnyx.com` | Failure (`email.failed`, reason `dkim_unavailable`). |
| `rate-limit@test.telnyx.com` | Failure (`email.failed`, reason `rate_limit_exceeded`). This simulates an outcome, not an actual quota or request-rate rejection. |

These are simulated recipient events on an accepted sandbox message, not real delivery attempts or promises about production failure timing. The parent remains a sandbox message; inspect recipient events for the selected outcome.

The hard-bounce and complaint simulations enqueue real auto-suppression work that creates `hard_bounce` or `spam_complaint` records. In sandbox mode, the eight recognized test addresses receive an admission-only exemption from an existing suppression so repeated tests remain deterministic. Other recipients, and every non-sandbox send, keep the normal suppression checks.

## Check polling and webhooks

Retrieve the message with `GET /v2/email_messages/{message_id}` and its history with `GET /v2/email_messages/{message_id}/events`. For event IDs and recipient correlation, use account event polling filtered to the message:

```sh
curl --get "https://api.telnyx.com/v2/email_events" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --data-urlencode 'filter[message_id]={message_id}'
```

Simulated events are stored and pollable. Supported event classes are also delivered to the message's configured webhooks when the subscription includes the matching value, such as `email.delivered`, `email.bounced`, `email.complained`, or `email.failed`. The simulated `email.suppressed` outcome is available through event polling but is not a webhook subscription value. Subscribe to `email.sandbox` if you also want the sandbox acceptance event. `email.sending` is not published as a webhook.

Create or update your subscription before sending a new test message. Webhook settings are snapshotted when a message is accepted. For events delivered on both surfaces, the event and recipient IDs stay stable across account event polling and webhook delivery; use the event envelope ID for deduplication and the payload message/recipient IDs for correlation. Webhooks are at-least-once, so your handler must tolerate duplicate deliveries.

For several outcomes in one request, use [batch sending](https://support.telnyx.com/en/articles/16823821-sending-email-in-batches-limits-results-and-safe-retries) and set `sandbox_mode: true` on the **batch envelope**, not on each item:

```json
{
  "sandbox_mode": true,
  "messages": [
    { "from": "sender@mail.yourcompany.com", "to": ["delivered@test.telnyx.com"], "subject": "Delivered test", "text_body": "Test" },
    { "from": "sender@mail.yourcompany.com", "to": ["complaint@test.telnyx.com"], "subject": "Complaint test", "text_body": "Test" }
  ]
}
```

The top-level value is applied to every item and overwrites any item-level value. One batch therefore cannot mix sandbox and production messages. A processed sandbox batch returns `207` with per-item results, including sandbox statuses for accepted items.

## Related articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
- [Understanding Telnyx Email errors and message size limits](https://support.telnyx.com/en/articles/16099890-understanding-telnyx-email-errors-and-message-size-limits)
