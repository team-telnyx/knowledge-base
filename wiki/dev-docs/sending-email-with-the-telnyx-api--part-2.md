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

*Part 2 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Response

A successful send returns `202 Accepted` with the message in `data`:

```
{
  "data": {
    "record_type": "email_message",
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "status": "queued",
    "from": { "email": "sender@example.com" },
    "to": [{ "email": "recipient@example.com" }],
    "subject": "Welcome",
    "created_at": "2026-07-06T12:00:00.000000Z"
  }
}
```

Key response fields:

- `status` — the **message** lifecycle status (see below).
- `id` — the message UUID. Use it with `GET /email_messages/{id}`, `GET /email_messages/{id}/events`, and `DELETE /email_messages/{id}/schedule`.
- `created_at` — when the message was created.
- `scheduled_at` — present when a future send was scheduled.
- `recipient_statuses` — a map of per-recipient status to count, present once recipient rows exist.
- `sandbox` — present when the message was created in sandbox mode.

Message status, recipient status, and event types are **three different taxonomies**. A message is a request; each recipient has its own delivery outcome; engagement signals such as opens and clicks are events, never message statuses.

### Message status

The parent message status is request-lifecycle only — it does not describe delivery.

| Status | Meaning |
| --- | --- |
| `queued` | Accepted and waiting to be processed. |
| `scheduled` | Held for a future `scheduled_at` time. |
| `sending` | Being injected into the delivery pipeline. |
| `completed` | Every recipient has reached a terminal state (not necessarily success). |
| `cancelled` | A scheduled message was cancelled before sending. |
| `sandbox` | Created in sandbox mode; never actually delivered. |
| `failed` | The message failed before delivery injection, such as when a scheduled send exceeds the daily limit at fire time. |

### Recipient status

Each recipient carries its own delivery outcome. These are surfaced in `recipient_statuses` and through the recipients endpoints. The Events API uses a separate event-type taxonomy — several recipient statuses map lossily to a different stored event type (for example, `expired`, `gw_reject`, and `injection_timeout` all produce a `failed` stored event). For exact recipient status, use `recipient_statuses` or the recipient endpoints.

| Status | Terminal | Meaning |
| --- | --- | --- |
| `queued` | No | Accepted, not yet injected. |
| `sending` | No | Injection in progress. |
| `sent` | No | Accepted by the delivery gateway. |
| `deferred` | No | Temporary failure (4xx); will be retried. |
| `delivered` | Yes | The receiving mail server accepted the message. |
| `bounced` | Yes | Permanently rejected by the receiving server (5xx or out-of-band bounce). |
| `failed` | Yes | Terminal system or operator-caused non-delivery. |
| `expired` | Yes | Retries were abandoned after the maximum queue age. |
| `gw_reject` | Yes | The delivery gateway refused the recipient before queueing. |
| `cancelled` | Yes | Cancelled before delivery. |
| `injection_timeout` | Yes | The injection attempt timed out with an ambiguous result. |

### Event types

Events record what happened and when. Query them with `GET /email_messages/{id}/events` or `GET /email_events`.

| Event type | Meaning |
| --- | --- |
| `queued`, `scheduled`, `sending`, `sent`, `cancelled`, `sandbox` | Lifecycle progress. |
| `delivered`, `deferred`, `bounced`, `failed`, `rejected` | Delivery outcomes. |
| `opened`, `clicked`, `unsubscribed`, `complained` | Engagement and feedback signals. |
| `daily_limit_exceeded` | The account's daily send limit blocked the send. |

### Suppressed recipients

When one or more recipients are suppressed at send time, the `202` response includes a top-level `suppressed` array describing each suppressed recipient. The message is still created for the non-suppressed recipients (if any).

```
{
  "data": {
    "record_type": "email_message",
    "id": "...",
    "status": "queued"
  },
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

If **all** recipients are suppressed, the request returns `422` with a `recipient_suppressed` error and the `suppressed` array (see [Errors](errors.md)).

## Tracking

Open, click, and unsubscribe tracking are configured through the `tracking` object on an email domain:

```
curl -X PATCH https://api.telnyx.com/v2/email_domains/{domain_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "tracking": {
      "open_tracking": true,
      "click_tracking": true,
      "unsubscribe_tracking": true
    }
  }'
```

**Tracking is scoped to the sending profile, not to an individual domain.** The domain endpoint is the API surface, but the setting is stored on your account's default sending profile. Every domain that shares that profile shares one tracking configuration, so updating tracking through one domain changes it for all of them. Registering a domain with `tracking` in `POST /email_domains` therefore only works for the first domain on the account — once a profile exists, the request is rejected with a validation error and you must use `PATCH /email_domains/{id}` instead.

Defaults for a new domain: `open_tracking: false`, `click_tracking: false`, `unsubscribe_tracking: true`. Open and click tracking are opt-in; one-click unsubscribe is on by default because Gmail and Yahoo bulk-sender rules require RFC 8058 unsubscribe support — disable it only if you handle unsubscribes yourself.

The tracking endpoints themselves are public (no auth) because email clients and browsers hit them directly.

### Open tracking

When `open_tracking` is enabled, messages with an HTML body get a 1×1 transparent tracking pixel injected before the closing `</body>` tag (or appended to the HTML when there is no `</body>`). When the recipient's email client loads the image, Telnyx records an `email.opened` event.

### Click tracking

When `click_tracking` is enabled, Telnyx rewrites `href` links in the HTML body to point through a tracking redirect. When a recipient clicks, Telnyx records an `email.clicked` event and redirects (HTTP 302) to the original URL. Links already pointing to the tracking service are not double-wrapped.

### Unsubscribe tracking

When `unsubscribe_tracking` is enabled (the default), Telnyx adds `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058) headers to outgoing messages, with a signed, unguessable unsubscribe URL. A recipient can unsubscribe via a link (`GET`) or one-click (`POST`, sent automatically by supporting email clients). On unsubscribe, Telnyx records an `email.unsubscribed` event and creates a suppression for the recipient.

### Tracking events

Tracking events — `email.opened`, `email.clicked`, and `email.unsubscribed` — are stored as message events and delivered to configured webhooks. Query them per message:

```
curl https://api.telnyx.com/v2/email_messages/{id}/events \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Or list events across the account:

```
curl https://api.telnyx.com/v2/email_events \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The `email.opened` event payload includes a `first_open` boolean that is `true` for the first open and `false` for subsequent opens. The `email.clicked` payload includes the clicked `url`, and `email.unsubscribed` includes the `method` (`link` or `one_click`).
