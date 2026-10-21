---
title: "Getting started with Telnyx Email"
summary: "Telnyx Email lets you send transactional and application email over a simple HTTP API, on the same platform you already use for voice and messaging."
sources:
- url: "https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/15853622-getting-started-with-telnyx-email.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/15853622-getting-started-with-telnyx-email.md -->

# Getting started with Telnyx Email

Telnyx Email lets you send transactional and application email over a simple HTTP API, on the same platform you already use for voice and messaging. This guide walks you through everything you need to send your first email: creating an account, getting an API key, adding and verifying a sending domain, sending a message, and confirming it was delivered.

**Email is currently managed through the Telnyx API.** There is no dedicated email dashboard yet, so every step below uses a simple `curl` command. If you can copy and paste into a terminal, you can complete this guide.

---

## Step 1: Create your account and get an API key

If you do not already have one, sign up for a free account at [telnyx.com/sign-up](https://telnyx.com/sign-up). Once you are signed in:

- Open the **API Keys** section of the Telnyx Mission Control Portal.
- Create a new API key and copy it somewhere safe. You will use it as a bearer token on every request.

Every example in this guide sends your key in an `Authorization` header. Replace `YOUR_API_KEY` with your real key:

```
Authorization: Bearer YOUR_API_KEY
```

**Keep your API key secret.** Treat it like a password — never commit it to source control or share it in a support ticket.

---

## Step 2: Add a sending domain

Telnyx sends your email using a domain you control, such as `mail.yourcompany.com`. This is what recipients and inbox providers use to confirm the mail really came from you. Add your domain with a single request:

```
curl -X POST https://api.telnyx.com/v2/email_domains \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "mail.yourcompany.com"}'
```

The response includes an `id` for the domain and an initial `status` of `pending`. Telnyx automatically schedules the first DNS verification about five minutes after registration and also checks pending domains every 30 minutes, so the status may change without a manual verification request. Add the DNS records in the next step; use the verify endpoint when you want an immediate, on-demand check.

For a full walkthrough of DNS setup, see **Setting up your email sending domain**.

---

## Step 3: Verify your domain

Fetch the DNS records Telnyx generated for your domain:

```
curl https://api.telnyx.com/v2/email_domains/{domain_id}/dns_records \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Add each record at your DNS provider (your domain registrar or hosting provider). Then ask Telnyx to check them:

```
curl -X POST https://api.telnyx.com/v2/email_domains/{domain_id}/verify \
  -H "Authorization: Bearer YOUR_API_KEY"
```

When your DNS has propagated and the records match, the domain `status` becomes `verified` and you can start sending. DNS changes can take anywhere from a few minutes to a few hours to propagate — if verification does not pass immediately, wait and try again.

---

## Step 4: Send your first email

With a verified domain, send a message. The `from` address must use your verified domain:

**Trial-account restriction:** Trial accounts can send only to the Telnyx account owner's email address. Every `to`, `cc`, and `bcc` recipient must use that address. Use the owner address for this first test, and upgrade your account before sending to anyone else.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "you@mail.yourcompany.com",
    "to": ["account-owner@example.com"],
    "subject": "Hello from Telnyx",
    "text_body": "This is my first email sent with Telnyx."
  }'
```

A successful request returns `202 Accepted` with a message `id` and a `status` of `queued`. Save the `id` — you use it to track delivery. You can send plain text with `text_body`, HTML with `html_body`, or both.

---

## Step 5: Check delivery

Look up the message resource at any time. Its parent `status` tracks message-wide processing, not delivery success. A parent status of `completed` means all recipients reached a terminal state; it does not mean every recipient was delivered. To confirm delivery, inspect the response's recipient-scoped `recipient_statuses` counts and the recipient events below:

```
curl https://api.telnyx.com/v2/email_messages/{message_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

For the full history of what happened to a message, request its events:

```
curl https://api.telnyx.com/v2/email_messages/{message_id}/events \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Delivery outcomes are recipient-scoped. In a message with multiple recipients, each recipient can follow a different path. Common recipient states and events include:

|  |  |
| --- | --- |
| **Event** | **What it means** |
| queued | Telnyx accepted the message and will send it shortly. |
| sent | Telnyx's MTA accepted the recipient into its outbound delivery queue. This does not mean the recipient's server accepted it. |
| delivered | The recipient's remote MX accepted the message (normally with a `250 OK` response). |
| bounced | The message could not be delivered (for example, the address does not exist). |
| opened | The recipient opened the message (when open tracking is on). |
| clicked | The recipient clicked a tracked link (when click tracking is on). |

You can also receive these events in real time by configuring a webhook, or poll `GET /v2/email_events` for recent activity across your account.

---

## Organize and find sent messages

Add `tags` and a `metadata` object when sending to retain application labels and reference values. Both are returned by `GET /v2/email_messages/{message_id}` and `GET /v2/email_messages`.

List filters accept comma-separated tags and metadata as a JSON object string or comma-separated `key=value` pairs:

```sh
curl --get "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --data-urlencode 'filter[tags]=receipts,orders' \
  --data-urlencode 'filter[metadata]={"order_id":"12345"}'
```

The equivalent pair form is `filter[metadata]=order_id="12345"`. You can combine pairs with commas, such as `campaign=receipts,order_id="12345"`. Preserve value types when filtering: an unquoted `12345` is numeric, while `"12345"` is a string.

---

## Next steps

- **Setting up your email sending domain** — a deeper walkthrough of DNS records and what each one does.
- **Troubleshooting email domain verification** — what to do if verification does not pass.
- **Why didn't my email arrive?** — how to triage a message that was not delivered.
- **Managing email suppressions and unsubscribes** — how Telnyx protects your sender reputation.

---

Related Articles

- [Setting up your email sending domain](https://support.telnyx.com/en/articles/15853623-setting-up-your-email-sending-domain)
- [Why didn't my email arrive?](https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive)
- [Managing email suppressions and unsubscribes](https://support.telnyx.com/en/articles/15853626-managing-email-suppressions-and-unsubscribes)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
- [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send)
- [Testing Telnyx Email safely with sandbox recipients](https://support.telnyx.com/en/articles/16823822-testing-telnyx-email-safely-with-sandbox-recipients)
- [Sending email in batches: limits, results, and safe retries](https://support.telnyx.com/en/articles/16823821-sending-email-in-batches-limits-results-and-safe-retries)
