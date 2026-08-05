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

*Part 5 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Manage suppressions

### List suppressions

`GET /email_blocks` returns the account's suppressions with offset or cursor pagination, sort, and filters.

```
curl -X GET "https://api.telnyx.com/v2/email_blocks?page[number]=1&page[size]=25&filter[reason]=manual_block&sort=-created_at" \
  -H "Authorization: Bearer ***"
```

| Parameter | Type | Notes |
| --- | --- | --- |
| `page[number]` | int (≥1, default 1) | Offset pagination page number. |
| `page[size]` | int (1–100, default 25) | Page size for offset mode. |
| `page[after]` | string (cursor) | Cursor for forward pagination. Mutually exclusive with `page[number]` and `page[before]`. |
| `page[before]` | string (cursor) | Cursor for backward pagination. |
| `sort` | string | `created_at` (asc) or `-created_at` (desc, default). Only `created_at` is sortable. |
| `filter[reason]` | enum | `hard_bounce`, `spam_complaint`, `unsubscribe`, `invalid`, or `manual_block`. |
| `filter[domain_id]` | uuid | Filter by domain. |
| `filter[created_after]` | date-time | Suppressions created after this timestamp. |
| `filter[created_before]` | date-time | Suppressions created before this timestamp. |

Offset-mode response (default):

```
{
  "data": [
    {
      "id": "5f3e2a1c-7b8d-4e2f-9a1c-3d5e7f9a1b2c",
      "record_type": "email_block",
      "domain_id": null,
      "group_id": null,
      "from": null,
      "to": "user@example.com",
      "reason": "manual_block",
      "source": "manual",
      "scope": "account",
      "status": "active",
      "created_at": "2026-07-06T12:00:00.000000Z",
      "updated_at": "2026-07-06T12:00:00.000000Z",
      "expires_at": null
    }
  ],
  "meta": {
    "page_number": 1,
    "page_size": 25,
    "total_pages": 1,
    "total_results": 1
  }
}
```

Cursor-mode response (when you use `page[after]` or `page[before]`):

```
{
  "data": [
    {
      "id": "5f3e2a1c-7b8d-4e2f-9a1c-3d5e7f9a1b2c",
      "record_type": "email_block",
      "domain_id": null,
      "group_id": null,
      "from": null,
      "to": "user@example.com",
      "reason": "manual_block",
      "source": "manual",
      "scope": "account",
      "status": "active",
      "created_at": "2026-07-06T12:00:00.000000Z",
      "updated_at": "2026-07-06T12:00:00.000000Z",
      "expires_at": null
    }
  ],
  "meta": {
    "page_size": 25,
    "next_cursor": "eyJjcm...Ijoi...",
    "previous_cursor": "eyJjcm...Ijoy...",
    "has_next": true,
    "has_previous": true
  }
}
```

Cursor `meta` always carries `page_size`, `next_cursor`, `previous_cursor`, `has_next`, and `has_previous`. All five keys are always present in the response; when there is no next or previous page, the corresponding cursor is `null` (not omitted).

### Retrieve a suppression

`GET /email_blocks/{id}` returns a single suppression by ID.

```
curl -X GET https://api.telnyx.com/v2/email_blocks/5f3e2a1c-7b8d-4e2f-9a1c-3d5e7f9a1b2c \
  -H "Authorization: Bearer ***"
```

Returns `200` with the suppression in `data`, or `404` if the ID doesn't exist or belongs to another account.

### Create a manual suppression

`POST /email_blocks` creates a `manual_block` suppression. The server forces `reason: manual_block` and `source: manual` regardless of any values you send.

```
curl -X POST https://api.telnyx.com/v2/email_blocks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ***" \
  -d '{
    "to": "spammer@bad.tld",
    "expires_at": "2026-12-31T23:59:59Z"
  }'
```

| Field | Type | Notes |
| --- | --- | --- |
| `to` | string (required) | The recipient address. Normalized to lowercase, trimmed. |
| `from` | string | Sender address. When null, the suppression is account- or domain-scoped. |
| `domain_id` | uuid | When null, the suppression is account-scoped. |
| `expires_at` | date-time | Stored as metadata on the suppression. **Not currently enforced** — see the note below. |

```
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "record_type": "email_block",
    "domain_id": null,
    "group_id": null,
    "from": null,
    "to": "spammer@bad.tld",
    "reason": "manual_block",
    "source": "manual",
    "scope": "account",
    "status": "active",
    "created_at": "2026-07-06T12:30:00.000000Z",
    "updated_at": "2026-07-06T12:30:00.000000Z",
    "expires_at": "2026-12-31T23:59:59Z"
  }
}
```

**`expires_at` is not currently enforced.** The field is accepted, stored, and returned, but no expiration process runs against it: the send-time suppression check matches on `status = "active"` alone and never compares `expires_at` to the current time. A suppression with a past `expires_at` keeps blocking sends. Treat `expires_at` as informational metadata and remove suppressions explicitly with `DELETE /email_blocks/{id}` when you want them to stop applying.

Creating a suppression that already exists and is still **active** (same account, scope, recipient, reason, domain, from, and group) is idempotent — the API returns `200` with the existing record and creates no new audit event.

If the matching record was previously removed, the create **reactivates** it instead: the existing row flips back to `status: "active"`, the request's `expires_at` is re-applied, a fresh `created` audit event is appended, and the API returns `201`. The row is reused rather than duplicated, so the audit trail reads `created → removed → created` on the same suppression ID.

| Existing record | Response | Audit event |
| --- | --- | --- |
| None | `201 Created` | `created` |
| Active duplicate | `200 OK` | none |
| Previously removed | `201 Created` (reactivated) | `created` |

### Delete a suppression

`DELETE /email_blocks/{id}` soft-deletes a suppression. The record is retained with `status: "removed"` and a `removed` audit event is appended.

```
curl -X DELETE https://api.telnyx.com/v2/email_blocks/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H "Authorization: Bearer ***"
```

Returns `200` with the suppression (now `status: "removed"`). Deleting an already-removed suppression is idempotent — returns `200` with no new event.

### Suppression audit events

`GET /email_blocks/{id}/events` lists the audit trail for a suppression. Each event records a lifecycle transition.

```
curl -X GET "https://api.telnyx.com/v2/email_blocks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/events?page[size]=50" \
  -H "Authorization: Bearer ***"
```

```
{
  "data": [
    {
      "id": "e1...",
      "record_type": "email_block_event",
      "event_type": "created",
      "reason": "manual_block",
      "source": "manual",
      "actor": "user-123",
      "meta": {},
      "occurred_at": "2026-07-06T12:30:00.000000Z"
    }
  ],
  "meta": {
    "page_number": 1,
    "page_size": 50,
    "total_pages": 1,
    "total_results": 1
  }
}
```

| `event_type` | When |
| --- | --- |
| `created` | The suppression was created, or a previously removed suppression was reactivated by a new create. |
| `removed` | The suppression was deleted. |
| `expired` | Reserved. No process currently emits this event — `expires_at` is not enforced, so suppressions do not transition to `expired` on their own. |
| `override_used` | A send bypassed this suppression via `ignore_suppression` (overridable reasons only). |

Uses offset pagination (`page[number]` default 1, `page[size]` default 50, max 100). Events are ordered by `occurred_at` descending.
