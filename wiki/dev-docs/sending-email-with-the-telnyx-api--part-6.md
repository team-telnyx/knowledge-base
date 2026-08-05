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

*Part 6 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 4](sending-email-with-the-telnyx-api--part-4.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## CSV import & export

Migrate an existing suppression list from SendGrid, Mailgun, or Amazon SES, or import a generic CSV. Export your Telnyx suppressions as CSV for backup or transfer.

### Import a CSV

`POST /email_blocks/import` accepts a multipart upload with a CSV file and returns `202` with an async import job. The provider format is auto-detected from the CSV header row.

```
curl -X POST https://api.telnyx.com/v2/email_blocks/import \
  -H "Authorization: Bearer ***" \
  -F "file=@blocks.csv" \
  -F "block_ttl_days=30"
```

| Form field | Type | Notes |
| --- | --- | --- |
| `file` | binary (required) | The CSV file. |
| `block_ttl_days` | int (default 30) | TTL applied to imported `manual_block` rows only. All other reasons get indefinite (`expires_at: null`). Invalid or missing falls back to 30. |

**Limits:** decoded CSV up to 25 MiB and 250,000 data rows. Exceeding either returns `413`.

All imported suppressions are account-scoped (`scope: account`, `domain_id: null`, `from: null`).

### Provider auto-detection

The importer detects the provider from the CSV header row (normalized to lowercase, trimmed):

| Provider | Detected by | Reason mapping |
| --- | --- | --- |
| **SendGrid** | Header has `email` + `type` | `blocks`→`manual_block`, `bounces`→`hard_bounce`, `spam_reports`→`spam_complaint`, `unsubscribes`→`unsubscribe`, `invalid_emails`→`invalid` |
| **Mailgun** | Header has `recipient` | `bounces`→`hard_bounce`, `complains`→`spam_complaint`, `unsubscribes`→`unsubscribe` |
| **Amazon SES** | Header has `email` + (`bounce_type` or `complaint_type` or `diagnostic`) | Non-blank `bounce_type`→`hard_bounce`, non-blank `complaint_type`→`spam_complaint` |
| **Generic** | Header has `email`, `to`, or `to_address` | `reason` column must be one of: `hard_bounce`, `spam_complaint`, `unsubscribe`, `invalid`, `manual_block` |

Detection order is SendGrid → Mailgun → SES → generic. An undetectable or header-only CSV returns `400`.

Rows with a missing or blank email address, or an unmappable reason, are skipped and recorded in the import's `errors` map (keyed by row number, 1-indexed with the header as row 1).

### Poll an import job

`GET /email_blocks/import/{id}` returns the current state of an import job. Poll this until `status` is `completed` or `failed`.

```
curl -X GET https://api.telnyx.com/v2/email_blocks/import/2c3d4e5f-... \
  -H "Authorization: Bearer ***"
```

```
{
  "data": {
    "id": "2c3d4e5f-...",
    "record_type": "email_block_import",
    "status": "completed",
    "total": 2,
    "provider": "sendgrid",
    "created_at": "2026-07-06T13:00:00.000000Z",
    "updated_at": "2026-07-06T13:00:05.000000Z",
    "completed_at": "2026-07-06T13:00:05.00Z",
    "processed_rows": 2,
    "created_count": 2,
    "existing_count": 0,
    "skipped_count": 0,
    "error_count": 0
  }
}
```

| `status` | Meaning |
| --- | --- |
| `pending` | Job enqueued, not yet started. |
| `processing` | Worker is importing rows. |
| `completed` | Import finished. Counts and `completed_at` are present. |
| `failed` | Import failed. `failure_reason` is present. |

When `status` is `completed`, the response includes `processed_rows`, `created_count`, `existing_count`, `skipped_count`, and `error_count`. Rejected rows are counted in `skipped_count` and detailed in an `errors` object that maps row numbers to skip reasons. `error_count` tracks a separate failure class that the importer does not currently populate, so it stays `0` even when rows were rejected:

```
{
  "data": {
    "id": "...",
    "status": "completed",
    "total": 3,
    "provider": "generic",
    "processed_rows": 3,
    "created_count": 2,
    "existing_count": 0,
    "skipped_count": 1,
    "error_count": 0,
    "errors": {
      "3": "unmapped reason: deferred"
    }
  }
}
```

Use `skipped_count` and `errors` — not `error_count` — to detect rows the importer rejected. A row with a missing/blank email address or an unmappable reason increments `skipped_count` and gets an entry in `errors`; `error_count` remains `0`.

Also note `block_ttl_days` only writes an `expires_at` value onto imported `manual_block` rows; because `expires_at` is not enforced, those rows keep blocking after the TTL date passes until you delete them.

### Export suppressions as CSV

`GET /email_blocks/export` streams the account's suppressions as a chunked CSV response with `Content-Type: text/csv`. Filters affect which rows are exported; `sort` and `page` parameters are accepted but ignored.

```
curl -X GET "https://api.telnyx.com/v2/email_blocks/export?filter[reason]=manual_block" \
  -H "Authorization: Bearer ***" \
  -H "Accept: text/csv" \
  -o email_blocks_export.csv
```

The CSV columns, in order: `id,to,from,reason,source,scope,status,domain_id,created_at,updated_at,expires_at,group_id`.

```
id,to,from,reason,source,scope,status,domain_id,created_at,updated_at,expires_at,group_id
a1b2c3d4-e5f6-7890-abcd-ef1234567890,spammer@bad.tld,,manual_block,manual,account,active,,2026-07-06T12:30:00.000000Z,2026-07-06T12:30:00.000000Z,2026-12-31T23:59:59Z,
```

**Export → import is lossy — it is not a round-trip.** The export writes all twelve columns, but the generic importer only consumes `to`/`to_address`/`email` and `reason`. Everything else in the file is discarded: `from`, `domain_id`, `group_id`, `source`, `status`, `id`, and the exported `expires_at` are all dropped on re-import.

Consequences of re-importing your own export:

- **Domain- and address-scoped suppressions are broadened to account scope.** Every imported row is written with `from_address: null`, `domain_id: null`, `scope: account`, so a block that previously applied to one sending domain now blocks that recipient across your whole account.
- **Group-scoped opt-outs become global.** `group_id` is not read on import, so a newsletter-only unsubscribe re-imports as a suppression that blocks every send to that recipient, including transactional mail.
- **Expiry metadata is not preserved.** Imported `manual_block` rows get a fresh `expires_at` derived from `block_ttl_days`; every other reason gets `expires_at: null`.
- **Removed rows come back active.** `status` is ignored, so an exported tombstone re-imports as an active suppression.

Use the export for backup, reporting, or migration to another system — not as a way to restore Telnyx state. To recreate scoped or group-scoped suppressions faithfully, replay them through `POST /email_blocks` (with `domain_id` / `from`) or `POST /email_unsubscribe_groups/{id}/suppressions`.
