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

*Part 3 of 5 — see also: [Part 1](telnyx-email-api--part-1.md), [Part 2](telnyx-email-api--part-2.md), [Part 4](telnyx-email-api--part-4.md), [Part 5](telnyx-email-api--part-5.md)*

The Telnyx Email API is a full email platform combining transactional sending, bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure that powers Telnyx's global messaging network. This page covers the API's capabilities, architecture, getting-started paths, inboxes, migration from other ESPs, and rate limits and quotas.

## Manage Inboxes

Email inboxes let your application receive, read, and reply to email messages through the Telnyx API. Each inbox is an address on a verified sending domain that you own, or on Telnyx's shared inbound subdomain for instant setup with no DNS configuration.

### Create an inbox

Create an inbox by specifying a local part (username) and a domain you've already verified for inbound email. You can also omit `domain_id` to use the account's shared inbound subdomain — no DNS setup required.

```bash
curl -X POST https://api.telnyx.com/v2/email_inboxes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "username": "support",
    "domain_id": "{domain_id}"
  }'
```

The response returns the inbox object with its full email address (e.g. `support@yourdomain.com`), status, and settings.

To create an instant inbox on the shared subdomain, omit both fields:

```bash
curl -X POST https://api.telnyx.com/v2/email_inboxes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{}'
```

### List and search messages

List messages in an inbox with optional search and filtering:

```bash
curl -X GET "https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages?filter[search]=invoice" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

You can filter by:

- **Search text** — `filter[search]` matches subject and message body
- **Sender** — `filter[from]` matches the sender address
- **Labels** — only messages with specific labels
- **Date range** — messages received within a time window
- **Read/unread** — filter by read status

Results are cursor-paginated, newest first.

Message bodies are returned as `text_body_url` and `html_body_url` — URLs you fetch separately. Headers, attachments, and labels are included inline.

### Reply to a message

Reply to a message with a single call. The original message's `In-Reply-To` and `References` headers are set automatically:

```bash
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages/{message_id}/actions/reply \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "text": "Thanks for reaching out. We will get back to you within 24 hours.",
    "html": "<p>Thanks for reaching out. We will get back to you within 24 hours.</p>"
  }'
```

Use the `reply_all` action to reply to all recipients. Both `text` and `html` are optional, but at least one must be present.

### Forward a message

Forward a message to new recipients. The forwarded message body is prepended with your optional note:

```bash
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages/{message_id}/actions/forward \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "to": [{"email": "billing@company.com"}],
    "text": "Forwarding this for your review."
  }'
```

### Drafts

Create a draft, update it, and send it when ready:

```bash
# Create a draft
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/drafts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "to": [{"email": "client@example.com"}],
    "subject": "Proposal follow-up",
    "text_body": "Hi, following up on our discussion..."
  }'

# Send the draft
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/drafts/{draft_id}/send \
  -H "Authorization: Bearer YOUR_API_KEY"
```

You can also create a reply draft linked to a specific message using the `POST /email_inboxes/{inbox_id}/messages/{message_id}/drafts` endpoint.

### Threads

Messages are grouped into threads by conversation. List threads in an inbox:

```bash
curl -X GET https://api.telnyx.com/v2/email_inboxes/{inbox_id}/threads \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Get a thread with a page of its messages:

```bash
curl -X GET https://api.telnyx.com/v2/email_inboxes/{inbox_id}/threads/{thread_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

You can also list threads across all inboxes in the account with `GET /email_threads`.

### Labels

Organize messages and threads with labels:

```bash
# Add labels to a message
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages/{message_id}/labels \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"labels": ["urgent", "billing"]}'

# Remove labels
curl -X DELETE https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages/{message_id}/labels \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"labels": ["urgent"]}'
```

Labels are mutable string tags — use them for categories, priority, workflow state, or anything your application needs. Thread labels are managed with the equivalent `/threads/{thread_id}/labels` endpoints.

### Sender filters

Control which senders can deliver to an inbox. Set a top-level `type` of `allowlist` or `blocklist`, and provide `entries` as an array of strings — exact email addresses or `@domain` wildcards:

```bash
# Allow only specific senders
curl -X POST https://api.telnyx.com/v2/email_inboxes/{inbox_id}/filters \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "type": "allowlist",
    "entries": [
      "trusted@partner.com",
      "@partner-domain.com"
    ]
  }'
```

Use `PUT` to replace all filters at once, or `DELETE` to remove specific entries.

### Mark messages as read or unread

Update the read state of a message. Set `read_at` to `true` for the current timestamp, an ISO-8601 string for a specific time, or `null` to mark as unread:

```bash
curl -X PATCH https://api.telnyx.com/v2/email_inboxes/{inbox_id}/messages/{message_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"read_at": true}'
```
