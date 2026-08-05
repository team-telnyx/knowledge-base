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

*Part 7 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Send-time behavior

When you send an email, Telnyx checks every recipient against the suppression list before creating the message. Suppressed recipients are reported in the response — they're never silently dropped.

### Partial suppression (202)

When **some** recipients are suppressed but others are not, the send proceeds for the non-suppressed recipients. The `202` response includes a top-level `suppressed` array describing each suppressed recipient:

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
      "scope": "account",
      "override_allowed": false
    }
  ]
}
```

Each entry in the `suppressed` array has:

| Field | Type | Notes |
| --- | --- | --- |
| `to` | string | The suppressed recipient address. |
| `reason` | string | The suppression reason (e.g. `hard_bounce`). |
| `scope` | string | The scope that matched (e.g. `account`, `domain`, `address`). |
| `override_allowed` | boolean | `true` if the suppression is overridable (`unsubscribe`, `manual_block`); `false` if non-overridable (`hard_bounce`, `spam_complaint`, `invalid`). |

### All recipients suppressed (422)

When **every** recipient is suppressed, the request returns `422` with a `recipient_suppressed` error code and the `suppressed` array:

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
      "scope": "account",
      "override_allowed": false
    }
  ]
}
```

### Batch sends

In a batch (`POST /email_messages/batch`), suppression is checked per message. A message whose recipients are all suppressed produces a per-item error with `code: "recipient_suppressed"` in the batch response's `errors` array (indexed by position in the request).

### Overriding suppressions

Set `ignore_suppression: true` on a send to bypass **overridable** suppressions (`unsubscribe` and `manual_block`). This requires an API key with the `email:override` scope — without it, the request returns `403`:

```
{
  "errors": [
    {
      "code": "10007",
      "title": "Forbidden",
      "detail": "This action requires the email:override scope"
    }
  ]
}
```

When `ignore_suppression: true` is honored:

- Recipients with only **overridable** suppressions (`override_allowed: true`) proceed — the send goes through and an `override_used` audit event is recorded on each bypassed suppression.
- Recipients with any **non-overridable** suppression (`override_allowed: false`) remain blocked — `ignore_suppression` cannot bypass `hard_bounce`, `spam_complaint`, or `invalid`.

The scope hierarchy grants `email:override` to keys with `full_access` or `email:admin`. Keys with only `email:send` or `email:read` cannot override.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "from": "sender@example.com",
    "to": ["unsubscribed@example.com", "new@example.com"],
    "subject": "Transactional update",
    "text_body": "Your account was updated.",
    "ignore_suppression": true
  }'
```

`ignore_suppression` can only bypass `unsubscribe` and `manual_block`. It will never override a `hard_bounce`, `spam_complaint`, or `invalid` suppression — those recipients stay blocked and appear in the `suppressed` array even when the flag is set.

## Unsubscribe groups

Unsubscribe groups let you suppress a recipient for one category of email without blocking all your sends to them. This is the standard pattern for separating newsletter opt-outs from transactional email. For example, a recipient who unsubscribes from your "Weekly Newsletter" group should still receive password-reset emails. Group-scoped suppressions only block sends that specify the same `group_id`.

### Create a group

`POST /email_unsubscribe_groups` creates a group.

```
curl -X POST https://api.telnyx.com/v2/email_unsubscribe_groups \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "name": "Newsletter",
    "description": "Weekly digest"
  }'
```

| Field | Type | Notes |
| --- | --- | --- |
| `name` | string (required, 1–255) | Group name. |
| `description` | string | Optional description. |

```
{
  "data": {
    "id": "g2...",
    "record_type": "email_unsubscribe_group",
    "name": "Newsletter",
    "description": "Weekly digest",
    "created_at": "2026-07-06T14:00:00.000000Z",
    "updated_at": "2026-07-06T14:00:00.000000Z"
  }
}
```

### List, retrieve, update, and delete groups

- `GET /email_unsubscribe_groups` — list groups (offset pagination, `page[size]` default 25, max 100).
- `GET /email_unsubscribe_groups/{id}` — retrieve a group.
- `PATCH /email_unsubscribe_groups/{id}` — update `name` and/or `description`. `PUT` is not supported.
- `DELETE /email_unsubscribe_groups/{id}` — delete a group. If the group has active suppressions, the request returns `409` unless you pass `?force=true`, which soft-deletes the suppressions first.

### Manage suppressions in a group

- `GET /email_unsubscribe_groups/{id}/suppressions` — list suppressions in a group (offset pagination).
- `POST /email_unsubscribe_groups/{id}/suppressions` — add a recipient to the group's suppression list. The server forces `reason: unsubscribe`, `source: manual`, and `group_id: <this group>`. Only `to` is read from the request body.
- `DELETE /email_unsubscribe_groups/{id}/suppressions/{email}` — remove a recipient from the group's suppression list. Returns `204`.

```
curl -X POST https://api.telnyx.com/v2/email_unsubscribe_groups/g2.../suppressions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{ "to": "opted.out@example.com" }'
```

### Send with a group

Pass `group_id` on a send to scope the suppression check to that group. The send will check account-, domain-, and address-scoped suppressions as usual. Records with `group_id: null` apply to every send regardless of group; records with `group_id` set additionally require the same `group_id` to match.

```
curl -X POST https://api.telnyx.com/v2/email_messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "from": "news@example.com",
    "to": ["subscriber@example.com"],
    "subject": "This week\'s updates",
    "text_body": "Here\'s what happened this week.",
    "group_id": "g2..."
  }'
```

The `group_id` you set on a send is persisted on the message. When the recipient later unsubscribes via the RFC 8058 one-click flow, the resulting suppression is scoped to that same group — so the opt-out only affects future sends to that group, not your transactional email.
