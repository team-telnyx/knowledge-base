---
title: "Setting up and troubleshooting Telnyx Email webhooks"
summary: "Use an Email webhook when your application needs delivery, engagement, inbound, or sending-domain updates without polling. This guide shows you how to create a focused event subscription, test it with a new message, and interpret the payload correctly."
sources:
- url: "https://support.telnyx.com/en/articles/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks"
updated_at: 2026-09-21T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16099889-setting-up-and-troubleshooting-telnyx-email-webhooks.md -->

# Setting up and troubleshooting Telnyx Email webhooks

Use an Email webhook when your application needs delivery, engagement, inbound, or sending-domain updates without polling. This guide shows you how to create a focused event subscription, test it with a new message, and interpret the payload correctly.

---

## **Before you start**

You need a Telnyx API key, the ID of your sending domain, and a publicly reachable HTTPS endpoint. Your endpoint must accept JSON POST requests.

Choose only the events your application handles. A webhook subscription is an explicit allowlist; there is no default that subscribes you to every event.

---

## **Step 1: Create the webhook**

Create the webhook under the sending domain. This example covers the most useful outbound lifecycle events:

```
curl -X POST "https://api.telnyx.com/v2/email_domains/{domain_id}/webhooks" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/webhooks/telnyx-email",
    "events": [
      "email.queued",
      "email.sent",
      "email.delivered",
      "email.deferred",
      "email.bounced",
      "email.failed",
      "email.complained",
      "email.cancelled",
      "email.daily_limit_exceeded"
    ]
  }'
```

A successful request returns `201 Created`. Save the webhook `id` from the response.

`email.injection_timeout` is not accepted by the current webhook subscription
allowlist. Observe that ambiguous outcome through `GET /v2/email_events` or the
per-message events endpoint instead.

---

## **Step 2: Confirm the saved subscription**

List the webhooks attached to the domain and confirm that the URL and event allowlist are correct:

```
curl "https://api.telnyx.com/v2/email_domains/{domain_id}/webhooks" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

To change the destination or event list, update the webhook by ID:

```
curl -X PATCH "https://api.telnyx.com/v2/email_domains/{domain_id}/webhooks/{webhook_id}" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "events": [
      "email.sent",
      "email.delivered",
      "email.bounced",
      "email.complained",
      "email.opened",
      "email.clicked"
    ]
  }'
```

**Important:** webhook settings are snapshotted when a message is accepted. A change affects new messages, not messages that were already queued or scheduled.

---

## **Step 3: Trigger a new event**

Send a new message from the domain after the webhook is saved or updated:

```
curl -X POST "https://api.telnyx.com/v2/email_messages" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "sender@mail.yourcompany.com",
    "to": ["recipient@example.com"],
    "subject": "Telnyx webhook test",
    "text_body": "Testing my Telnyx Email webhook."
  }'
```

Use a new send for every subscription test. Updating a webhook and then waiting on an older in-flight message can make a correct setup look broken.

---

## **Choose the right event**

|  |  |
| --- | --- |
| **Event** | **What it means** |
| `email.queued` | Telnyx accepted the message for processing. |
| `email.sent` | The recipient was accepted into the Telnyx mail queue. |
| `email.delivered` | The receiving mail server accepted the recipient. |
| `email.deferred` | Delivery was temporarily delayed and remains retryable. |
| `email.bounced` | Delivery ended without success. Read `canonical_event_type` and `error_evidence` to distinguish a hard bounce from queue expiry. |
| `email.failed` | A terminal system or pre-queue failure prevented delivery. Publication follows the stored event commit. |
| `email.cancelled` | A scheduled send was cancelled. |
| `email.daily_limit_exceeded` | A scheduled send was rejected by the daily recipient limit at fire time. |
| `email_domain.dkim_rotated` | A sending domain's DKIM key was rotated; update the returned DNS record. |
| `email.opened` / `email.clicked` | Engagement was detected when the corresponding tracking feature was enabled. |
| Other `email_domain.*` events | Domain creation, verification, degradation, suspension, or deletion. Subscribe to the specific event names you need. |

`email.injection_timeout` is a polling-only ambiguous outcome and is not a
webhook subscription value. Observe it through the Events API before deciding
whether a retry is safe.

**Do not subscribe to `email.sending` for application logic.** The value is accepted by the subscription API for compatibility, but it is not currently published as a webhook.

---

## **Interpret outbound payloads correctly**

Normal outbound delivery webhooks are recipient-scoped: one recipient produces one event. Do not expect message-level arrays of every `to`, `cc`, or `bcc` address.

|  |  |
| --- | --- |
| **Field** | **How to use it** |
| Event envelope `id` | Stable deduplication ID for this webhook delivery. For normal recipient-scoped events that also appear in account polling, the same event ID is available there. Scheduled webhooks are an exception: each recipient callback has a derived ID while polling retains one message-scoped stored ID. Domain lifecycle events do not appear in account event polling. |
| Payload `id` | The parent email message ID. |
| `event_type` / `canonical_event_type` | Compatibility event name and the more specific canonical outcome. |
| `recipient_id` | The durable recipient ID. Store it with the event for correlation. |
| `to`, `cc`, or `bcc` | Exactly one recipient projection. BCC addresses are intentionally redacted. |
| `status` | The webhook event slug, not the authoritative recipient-state value. |
| `error_evidence` | For error events, use the normalized `code`, SMTP evidence, source, and `retryable` flag to decide the next action. |

Phase 1 preserves compatibility event names while adding `canonical_event_type` on webhooks and event polling:

| Outcome | Compatibility `event_type` / webhook name | `canonical_event_type` |
| --- | --- | --- |
| Gateway rejection | `email.failed` | `email.gw_reject` |
| Ambiguous injection timeout | `email.injection_timeout` | `email.injection_timeout` |
| Queue expiry | `email.bounced` | `email.expired` |
| Other system failure | `email.failed` | `email.failed` |

The compatibility name alone cannot distinguish gateway rejection from another system failure, or expiry from a bounce. Use `canonical_event_type` together with `error_evidence`. Older records without enough recorded evidence may retain a generic canonical name; do not infer a more specific outcome.

For example, queue expiry is terminal `expired`, with compatibility webhook `email.bounced`, canonical type `email.expired`, and delivery code `30005`.

`bounce_category` is not part of the normal public webhook contract. Do not make retry or suppression decisions from that field.

---

## **Deduplicate and reconcile events**

Webhook delivery is at-least-once. Store the event envelope ID and deduplicate
that webhook by its ID before applying it again. A replay of the same callback
preserves its identity. Keep the payload's message ID, recipient ID, event type,
and occurrence time separately for correlation.

For normal recipient-scoped outcomes that overlap account polling, the webhook
and polling event IDs match. **Scheduled events are different:** polling keeps
one stored message-scoped `scheduled` row, while webhook publication derives one
recipient-scoped ID per callback. Reconcile scheduled events by payload message
ID, event type, recipient, and occurrence time rather than requiring ID equality.
Domain lifecycle events are webhook-only and are not returned by
`GET /v2/email_events`.

Publication into Telnyx's event dispatcher is separate from successful delivery
to your HTTPS URL. A downstream endpoint failure does not erase the stored
outbound event. Use `GET /v2/email_events` to reconcile the overlapping stored
recipient events if your endpoint was unavailable; use your webhook record for
domain lifecycle events, and preserve all correlation fields when contacting
support.

---

## **If your webhook appears silent**

- List the webhook and confirm its URL and explicit event allowlist.
- Send a new message after the webhook was created or updated.
- Confirm you subscribed to `email.sent`, `email.delivered`, or another event that is actually published—not `email.sending`.
- Log the event envelope ID, payload message `id`, `recipient_id`, `canonical_event_type`, `status`, `occurred_at`, and `error_evidence`. Do not log API keys or message content.

---

Related Articles

- [Getting started with Telnyx Email](https://support.telnyx.com/en/articles/15853622-getting-started-with-telnyx-email)
- [Setting up your email sending domain](https://support.telnyx.com/en/articles/15853623-setting-up-your-email-sending-domain)
- [Why didn't my email arrive?](https://support.telnyx.com/en/articles/15853625-why-didn-t-my-email-arrive)
- [Managing email suppressions and unsubscribes](https://support.telnyx.com/en/articles/15853626-managing-email-suppressions-and-unsubscribes)
- [Scheduling and cancelling an email send](https://support.telnyx.com/en/articles/16099894-scheduling-and-cancelling-an-email-send)
- [Testing Telnyx Email safely with sandbox recipients](https://support.telnyx.com/en/articles/16823822-testing-telnyx-email-safely-with-sandbox-recipients)
