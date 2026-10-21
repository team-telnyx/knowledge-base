---
title: "Scheduling and cancelling an email send"
summary: "Add scheduledat when Telnyx should accept an email now and queue it for a future time. This guide shows you how to schedule, confirm, reschedule, and cancel a send, and interpret terminal failures."
sources:
- url: "https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16099894-scheduling-and-cancelling-an-email-send.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16099894-scheduling-and-cancelling-an-email-send.md -->

# Scheduling and cancelling an email send

Add `scheduled_at` when Telnyx should accept an email now and queue it for a future time. This guide shows you how to schedule, confirm, reschedule, and cancel a send, and interpret terminal failures.

---

## **Step 1: Schedule with a future timestamp**

Use the canonical `scheduled_at` field with a valid ISO 8601 timestamp in the future:

```
curl -X POST "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "sender@mail.yourcompany.com",
    "to": ["recipient@example.com"],
    "subject": "Scheduled maintenance reminder",
    "text_body": "Maintenance starts in one hour.",
    "scheduled_at": "2030-01-15T15:00:00Z"
  }'
```

A successful request returns `202 Accepted` with `status: "scheduled"` and the stored `scheduled_at` timestamp.

**Use `scheduled_at` for new integrations.** `send_at` remains a deprecated request alias for backward compatibility, but responses use `scheduled_at`.

---

## **Avoid accidental immediate sends**

The timestamp must parse as ISO 8601 and be later than the current time. An invalid, non-ISO, or past `scheduled_at` returns `422` with field detail; it does not create an immediate send. Omitting the schedule on a normal send request still requests an immediate send.

Always check both response fields before assuming the schedule was saved:

- `status` must be `scheduled`.
- `scheduled_at` must be present and match the intended instant.

---

## **Step 2: Confirm the schedule**

Retrieve the message by ID:

```
curl "https://api.telnyx.com/v2/email_messages/{message_id}" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Before the send fires, the message should remain `scheduled`. The `scheduled_at` field remains on the message after processing or cancellation, so use `status` to determine what happened most recently.

---

## **Step 3: Cancel before it is queued**

Cancel the schedule with the message ID:

```
curl -X DELETE "https://api.telnyx.com/v2/email_messages/{message_id}/schedule" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A successful cancellation returns `200` with `status: "cancelled"`. Cancelling a message that is no longer scheduled returns `400`; once delivery processing has begun, the schedule endpoint cannot recall the message.

---

## **Change the scheduled time**

Reschedule a still-scheduled message in place:

```sh
curl -X PATCH "https://api.telnyx.com/v2/email_messages/{message_id}/schedule" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"scheduled_at":"2030-01-15T16:00:00Z"}'
```

Success returns `200` with updated message data and preserves the message ID. A missing, invalid, or past `scheduled_at` returns `422`; a message that is no longer scheduled or a conflicting schedule change returns `409`; an unknown message returns `404`. Retrieve the message after a conflict before deciding what to do next.

---

## **Check fire-time failures**

Scheduled sends are accepted before they enter the delivery queue and are exempt from the submission-time recipient quota. Telnyx rechecks account eligibility and enforces the daily recipient limit when the schedule fires. Fire-time rejections and queue-publication exhaustion have different status outcomes.

If a scheduled message did not queue at the expected time, retrieve its events:

```
curl "https://api.telnyx.com/v2/email_messages/{message_id}/events" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A `daily_limit_exceeded` event means the recipient quota was unavailable at fire time. The parent message becomes `failed`, while its recipient rows may remain `queued`. If account eligibility fails instead, recipient rows become `failed` and the parent message rolls up to `completed`. Neither path reaches the mail queue. Inspect the parent `status`, `recipient_statuses`, and event reason together; `completed` means all recipients are terminal, not that delivery succeeded.

---

## **When scheduled queue publication exhausts its retries**

If publication to the delivery queue (Kafka) keeps failing, the scheduled worker makes three attempts over roughly 15 minutes: the retries wait five minutes and then ten minutes. This is retry timing, not a delivery-time guarantee.

After the last failed attempt, still-nonterminal recipients become non-billable `failed`. Telnyx stores a recipient failure event with reason `kafka_publish_exhausted` and publishes `email.failed` after the event commits. Event polling and webhooks preserve the same event and recipient identities. The parent normally rolls up to `completed`, meaning all recipients are terminal, not delivered. Inspect recipient outcomes and the failure reason before submitting another send.

---

## **Troubleshooting summary**

|  |  |
| --- | --- |
| **Symptom** | **Cause and next step** |
| The response says `queued` | No schedule was supplied on the send request. Invalid or past timestamps return `422` instead of queueing an immediate send. |
| Schedule creation or editing returns `422` | Supply a valid future ISO 8601 `scheduled_at`; it is required for PATCH. |
| Reschedule returns `409` or `404` | Retrieve the current state after a conflict; check the message ID and account for `404`. |
| The response omits `scheduled_at` | No future schedule was stored. Do not assume it will wait. |
| Cancel returns `400` | The message is not currently scheduled. Retrieve the message and inspect its status. |
| The parent message becomes `failed` at fire time | This is the daily-limit rejection path. Inspect events for `daily_limit_exceeded` and check `recipient_statuses`; recipient rows may remain `queued` even though the parent is `failed`. The message was not injected for delivery. |
| The parent is `completed`, but no delivery occurred | Account-eligibility rejection or exhausted queue publication can leave recipients `failed`. Inspect `recipient_statuses` and event reasons, including `kafka_publish_exhausted`. `Completed` means all recipients are terminal, not delivered. |

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Why didn't my email arrive?](https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive)
- [Setting up and troubleshooting Telnyx Email webhooks](https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks)
- [Preventing duplicate emails with idempotency](https://support.telnyx.com/en/articles/16099891-preventing-duplicate-emails-with-idempotency)
- [Creating and sending email templates](https://support.telnyx.com/en/articles/16099893-creating-and-sending-email-templates)
