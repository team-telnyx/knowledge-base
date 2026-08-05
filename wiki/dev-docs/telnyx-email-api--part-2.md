---
title: Telnyx Email API
summary: The Telnyx Email API is a full email platform combining transactional sending,
  bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure
  that powers Telnyx's global messaging network. This page covers the API's capabilities,
  architecture, getting-started paths, inboxes, migration from other ESPs, and rate
  limits and quotas.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/inboxes/index
- url: https://developers.telnyx.com/docs/messaging/email/migrate-to-telnyx
- url: https://developers.telnyx.com/docs/messaging/email/overview
- url: https://developers.telnyx.com/docs/messaging/email/quickstart
- url: https://developers.telnyx.com/docs/messaging/email/rate-limits
updated_at: 2026-08-05T13:51:25Z
---

# Telnyx Email API

*Part 2 of 5 — see also: [Part 1](telnyx-email-api--part-1.md), [Part 3](telnyx-email-api--part-3.md), [Part 4](telnyx-email-api--part-4.md), [Part 5](telnyx-email-api--part-5.md)*

The Telnyx Email API is a full email platform combining transactional sending, bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure that powers Telnyx's global messaging network. This page covers the API's capabilities, architecture, getting-started paths, inboxes, migration from other ESPs, and rate limits and quotas.

## Getting started

The quickest path to your first send:

1. **[Quickstart: Send Your First Email](quickstart-send-your-first-email.md)** — two-minute send with a shared domain, or full custom domain setup
2. **[Sending Email with the Telnyx API](sending-email-with-the-telnyx-api--part-1.md)** — complete send guide with attachments, templates, scheduling, idempotency, tracking, and batch sending
3. **[Manage Inboxes](manage-inboxes.md)** — receive, read, reply, forward, and organize email through the API
4. **[Webhooks & Events](webhooks-events.md)** — subscribe to real-time delivery and engagement events

### Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up) (free to create)
- An API key from [API Keys](https://portal.telnyx.com/#/app/api-keys) in the portal (the **Auth** section)

All requests use the production base URL `https://api.telnyx.com/v2` and an `Authorization` header with the Bearer authentication scheme. Replace `YOUR_API_KEY` in the examples with your key.

### Option A: Send in two minutes with a shared domain

Telnyx provides a shared sending domain (`mail.telnyx.com`) that's already verified and ready to use — no DNS setup required. Sends must use `onboarding@mail.telnyx.com` as the `from` address, and recipients are limited to the account owner's verified email address.

```bash
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "onboarding@mail.telnyx.com",
    "to": ["your-email@example.com"],
    "subject": "Hello from Telnyx",
    "text_body": "This is a test email sent with the Telnyx shared domain — no DNS setup required."
  }'
```

The shared domain is perfect for testing and onboarding. When you're ready to send to arbitrary recipients from your own branded address, switch to a custom domain (Option B below).

Shared-domain sends are limited to the account owner's verified email address as the recipient. To send to any recipient, add and verify your own domain.

### Option B: Use a custom domain

**1. Add a sending domain.** Emails must be sent from a domain you control so recipients can authenticate the sender (SPF, DKIM, and DMARC). Add your domain with one request:

```bash
curl -X POST https://api.telnyx.com/v2/email_domains \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "domain": "example.com"
  }'
```

The `201` response returns the domain with a `status` of `pending` and an `id` you'll use in the next steps. Save that `id`.

Telnyx also provides **shared sending domains** as a restricted zero-setup option. Shared domains are visible to all accounts in `GET /email_domains` (look for `"type": "shared"`) and need no DNS setup, but sends must use `onboarding@<shared-domain>` as the `from` address and every recipient must match the verified email address of the account owner. Use a custom domain for arbitrary recipients, your own `from` address, and control over sender authentication and domain reputation.

**Trial accounts** are restricted to the account owner's verified email address as the recipient, even with a custom domain. Sending to any other recipient returns `403` with code `10007`. Upgrade the account to send to arbitrary recipients.

**2. Verify the domain.** DNS records are generated for every domain you add. Fetch them and add them at your registrar.

Fetch the DNS records:

```bash
curl https://api.telnyx.com/v2/email_domains/{domain_id}/dns_records \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The response includes records for ownership (TXT), SPF (TXT), DKIM (TXT), MX, and DMARC (TXT), each with `host`, `value`, and a `required` flag.

Add each record's `host` and `value` at your registrar or DNS host. Ownership and DKIM are required. MX is required only when `inbound_enabled` is `true`; SPF and DMARC are optional but recommended for deliverability.

Trigger verification:

```bash
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A `200` returns the updated domain. Sending is enabled only when `data.status` is `verified`; the same `200` can also report `pending` (records not yet observed) or `failed` (a required record is missing or wrong). Inspect the `verification` map, wait for propagation, and retry.

**3. Send your first email.** With a verified domain, send a message with a minimal payload — `from`, `to`, `subject`, and `text_body`:

```bash
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Idempotency-Key: 8e03978e-40d5-43e8-bc93-6894a57f9326" \
  -d '{
    "from": "sender@example.com",
    "to": ["recipient@example.com"],
    "subject": "Hello from Telnyx",
    "text_body": "This is a test email."
  }'
```

Replace the placeholders:

- `from`: an address on a domain you've verified. For a shared domain, use only `onboarding@<shared-domain>`.
- `to`: the recipient address (an array, even for a single recipient). Shared-domain sends are limited to the account owner's verified email address. Trial accounts are limited to the account owner's verified email address on any domain, including custom domains.

The optional `Idempotency-Key` header makes retries safe. Generate a unique UUID v4 for each logical send, then reuse the same key and request body if a network error leaves the result uncertain. Do not put the key in the JSON body.

**4. Check the result.** A successful send returns `202 Accepted` with the created message:

```json
{
  "data": {
    "record_type": "email_message",
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "status": "queued",
    "from": {
      "email": "sender@example.com"
    },
    "to": [
      {
        "email": "recipient@example.com"
      }
    ],
    "subject": "Hello from Telnyx",
    "created_at": "2026-07-06T12:00:00.000000Z"
  }
}
```

The `status: "queued"` means your message is on its way. Save the `id` to look it up and track delivery.

If this request is retried after a successful send, Telnyx returns the original status and response body with `Idempotent-Replayed: true` in the response headers. The first response does not include that header.

Retrieve the message:

```bash
curl https://api.telnyx.com/v2/email_messages/{id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

List events for the message — `queued`, `sent`, `delivered`, `bounced`, `opened`, `clicked`, and more as delivery progresses:

```bash
curl https://api.telnyx.com/v2/email_messages/{id}/events \
  -H "Authorization: Bearer YOUR_API_KEY"
```
