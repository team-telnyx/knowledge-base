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

*Part 4 of 8 — see also: [Part 1](sending-email-with-the-telnyx-api--part-1.md), [Part 2](sending-email-with-the-telnyx-api--part-2.md), [Part 3](sending-email-with-the-telnyx-api--part-3.md), [Part 5](sending-email-with-the-telnyx-api--part-5.md), [Part 6](sending-email-with-the-telnyx-api--part-6.md), [Part 7](sending-email-with-the-telnyx-api--part-7.md), [Part 8](sending-email-with-the-telnyx-api--part-8.md)*

Covers the Telnyx Email API sending surface — single and batch sends, templates, scheduling, idempotency, attachments, tracking, suppressions, unsubscribe groups, and the RFC 8058 one-click unsubscribe flow — including the suppression model, scope, CRUD operations, CSV import/export, and send-time override behavior.

## Scope

A suppression's **scope** determines which sends it blocks. Scope is derived server-side from the suppression's `domain_id` and `from` fields — it's never trusted from the client. There are exactly three scopes:

| Scope | Condition | Blocks |
| --- | --- | --- |
| `account` | `domain_id` is null | All sends to the recipient address, across all domains and senders. If `from` is also set, send-time matching still restricts the block to that sender. |
| `domain` | `domain_id` is set, `from` is null | Sends to the recipient from the specified domain |
| `address` | Both `domain_id` and `from` are set | Sends to the recipient from the specified sender address on the specified domain |

At send time, Telnyx checks the recipient against all matching active suppressions. Account-scoped blocks match across all domains, but a non-null `from` still restricts matching to that sender. Domain-scoped blocks match when the send's domain matches. Address-scoped blocks match when both domain and sender match.

### `group_id` is a filter, not a scope

`group_id` is **not** a fourth scope — it's an independent association that narrows *which sends* a suppression applies to, and it combines with whichever of the three scopes the record already has. A suppression with `group_id: null` applies to every send regardless of group; a suppression with `group_id` set applies only to sends that carry the same `group_id`.
