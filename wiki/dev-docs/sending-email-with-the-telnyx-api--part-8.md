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

*Part 8 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## RFC 8058 one-click unsubscribe

RFC 8058 defines a one-click unsubscribe mechanism: supporting email clients (Gmail, Yahoo, Apple Mail, and others) send an automatic `POST` to a unsubscribe URL when the recipient clicks the unsubscribe button, without the recipient having to visit a web page.

### How it works

1. **Headers on outgoing mail.** When the sending domain has `unsubscribe_tracking` enabled (the default), Telnyx adds two headers to every outgoing message:
   - `List-Unsubscribe: <https://...tracking/unsubscribe/{token}>` — a signed, unguessable URL.
   - `List-Unsubscribe-Post: List-Unsubscribe=One-Click` — signals RFC 8058 support to the mailbox provider.
2. **Recipient unsubscribes.** A recipient can unsubscribe two ways:
   - **One-click (`POST`)** — the email client sends an automatic `POST` to the unsubscribe URL (RFC 8058). Telnyx records the unsubscribe with `method: "one_click"`.
   - **Link (`GET`)** — the recipient clicks the unsubscribe link and lands on a confirmation page. Telnyx records the unsubscribe with `method: "link"`.
3. **Suppression created.** Telnyx enqueues a worker that creates an `unsubscribe` suppression for the recipient. When the original send specified a `group_id`, the suppression is scoped to that group.
4. **Event recorded.** Telnyx records an `email.unsubscribed` event on the message (with the `method` — `link` or `one_click`). These events also flow to configured webhooks.

Both `POST` and `GET` always return `200`, even for invalid tokens, to avoid leaking information about which message IDs exist (per RFC 8058 §3).

### Enabled by default

`unsubscribe_tracking` defaults to `true` for every email domain. This is intentional: Gmail and Yahoo require RFC 8058 one-click unsubscribe support for bulk senders. You can disable it per domain if you handle unsubscribes yourself, but doing so risks deliverability problems with those providers.

```
curl -X PATCH https://api.telnyx.com/v2/email_domains/{domain_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "tracking": {
      "unsubscribe_tracking": true,
      "open_tracking": false,
      "click_tracking": false
    }
  }'
```

Open and click tracking default to `false`; unsubscribe tracking defaults to `true`. The one-click unsubscribe flow only fires when the sending domain has `unsubscribe_tracking` enabled.

The `List-Unsubscribe` URL carries a signed HMAC token, not a bare message ID. If the signing key is missing or misconfigured, Telnyx omits the unsubscribe headers entirely rather than emitting an invalid token — recipients can't unsubscribe from a message with no headers, but they also won't see a broken unsubscribe button.
