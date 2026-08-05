---
title: Email Webhooks & Events
summary: Telnyx email events flow through three consumption surfaces — recipient-scoped
  webhooks, the Events API for polling, and per-message lookups — covering the full
  lifecycle from queued through delivered, bounced, and engagement signals, plus domain
  lifecycle events. This page documents the event model, webhook payload envelope,
  signature verification, polling endpoints, and how to combine both surfaces in production.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/webhooks-events/index
updated_at: 2026-08-05T13:53:18Z
---

# Email Webhooks & Events

*Part 2 of 5 — see also: [Part 1](email-webhooks-events--part-1.md), [Part 3](email-webhooks-events--part-3.md), [Part 4](email-webhooks-events--part-4.md), [Part 5](email-webhooks-events--part-5.md)*

Telnyx email events flow through three consumption surfaces — recipient-scoped webhooks, the Events API for polling, and per-message lookups — covering the full lifecycle from queued through delivered, bounced, and engagement signals, plus domain lifecycle events. This page documents the event model, webhook payload envelope, signature verification, polling endpoints, and how to combine both surfaces in production.

## Event model

An email message moves through a series of states. Each transition emits an event carrying the event type, a timestamp, the email message ID, and an optional payload with delivery/engagement details.

### Lifecycle of a message

Outbound emails typically progress:

```
email.scheduled → email.queued → email.sent → email.delivered
                                                  ↘ email.deferred (temporary) → email.delivered
                                                  ↘ email.bounced (terminal non-delivery)
                                                  ↘ email.failed
              ↘ email.sandbox   (sandbox mode only — no delivery attempted)
```

`email.bounced` is **not** limited to a permanent remote rejection. Four distinct MTA outcomes — an ordinary bounce, a queue expiration, an administrative bounce, and an asynchronous out-of-band (OOB) bounce — all publish the same `email.bounced` webhook. The webhook event type alone does not tell you which one happened. Read `payload.error_evidence.code` (the 30xxx normalized error code) to distinguish them. The recipient’s authoritative `status` on the recipient row may differ from the webhook’s `status` field, which carries the event slug.

The per-recipient status recorded on the recipient row can diverge from the webhook event type. Expiration resolves the recipient to `expired`, while an administrative bounce resolves it to `failed` — both still publish `email.bounced`:

| MTA outcome | Webhook event type | Recipient `status` | `error_evidence.code` |
| --- | --- | --- | --- |
| Ordinary bounce | `email.bounced` | `bounced` | `30001` (or `30002` on a 4xx) |
| Queue expiration | `email.bounced` | `expired` | `30005` |
| Administrative bounce | `email.bounced` | `failed` | `30003` (or `30099` without SMTP status) |
| Out-of-band (OOB) bounce | `email.bounced` | `bounced` | `30001` |

There is no `email.expired` webhook event type — `expired` is a recipient status, not an event type.

After delivery, engagement events fire as recipients interact:

```
email.delivered → email.opened → email.clicked
                                ↘ email.complained
                                ↘ email.unsubscribed
```

Inbound emails (messages received at a domain with inbound enabled) emit a single `email.received` event.

Separately, your email domains emit lifecycle events — `email_domain.created` when a domain is registered, `email_domain.verified` when its DNS records validate, and `email_domain.degraded` / `email_domain.suspended` / `email_domain.deleted` as its health changes.

### Webhook event-type reference

Email webhook subscriptions accept **19 event types**: 13 outbound/tracking `email.*` events handled by the email API (12 published plus `email.sending` which is accepted but never delivered), `email.received` published by the inbound pipeline, and 5 `email_domain.*` domain-lifecycle events published by the domains service. This is the complete webhook subscription allowlist. The polling API uses a separate 16-type message-event taxonomy described under [#Consume via polling](consume-via-polling.md).

`email.sending` is accepted by the subscription allowlist but **never published** as a webhook. The service records a stored `sending` event when a message is handed to the outbound MTA, but explicitly suppresses its webhook publication (`skip_webhook: true`). You can subscribe to it, but you will never receive an `email.sending` callback. The `sending` event *is* returned by the Events API — see [#Consume via polling](consume-via-polling.md). Only **18** of the 19 allowed event types are actually delivered as webhooks.

#### Message lifecycle (`email.*`)

| Event type | Trigger | Payload highlights |
| --- | --- | --- |
| `email.scheduled` | A message with a future `scheduled_at` has been accepted and queued for later sending. | `scheduled_at` timestamp. |
| `email.queued` | The message has entered the outbound queue. | Recipient-scoped snapshot: `id`, `recipient_id`, `status`, `occurred_at`, `from`, the single recipient field, and `subject`. |
| `email.sandbox` | A message was accepted in sandbox mode — no delivery is attempted. | Recipient-scoped snapshot with `status: "sandbox"`. |
| `email.sent` | The recipient was accepted by the Telnyx outbound MTA for delivery. Remote acceptance is reported by `email.delivered`. | Recipient-scoped snapshot. |
| `email.delivered` | The receiver accepted the message for this recipient (SMTP success). | Recipient-scoped snapshot with `status: "delivered"`. |
| `email.deferred` | Delivery temporarily failed; the MTA will retry. | Recipient-scoped snapshot with `status: "deferred"`, plus `error_evidence` and `errors[]`. |
| `email.bounced` | Terminal non-delivery for this recipient — an ordinary bounce, queue expiration, administrative bounce, or OOB bounce. | Recipient-scoped snapshot with `status: "bounced"` (always the event slug, not the recipient status), plus `error_evidence` and `errors[]`. Use `error_evidence.code` to distinguish bounce subtypes. |
| `email.failed` | The message could not be sent for this recipient (sender-side failure). | Recipient-scoped snapshot with `status: "failed"`, plus `error_evidence` and `errors[]`. |
| `email.received` | An inbound message arrived at one of your enabled inbound domains. | Inbound sender, recipients, subject, and stored-content references. |

#### Engagement & tracking (`email.*`)

| Event type | Trigger | Payload highlights |
| --- | --- | --- |
| `email.opened` | A recipient opened the message (tracking pixel fired). | Recipient, first-open flag, IP address, user-agent. |
| `email.clicked` | A recipient clicked a tracked link in the message. | Recipient, link URL, user-agent. |
| `email.complained` | Telnyx received an individual spam feedback report from a participating mailbox provider. | Recipient. |
| `email.unsubscribed` | The recipient unsubscribed via a tracked unsubscribe link. | Recipient, IP address, user-agent, unsubscribe method. |

#### Domain lifecycle (`email_domain.*`)

| Event type | Trigger | Payload highlights |
| --- | --- | --- |
| `email_domain.created` | A new email domain was registered to your account. | Domain resource snapshot (`id`, `domain`, `status`, DNS and configuration fields). |
| `email_domain.verified` | The domain’s DNS records passed verification and it’s ready for sending. | Domain resource snapshot. |
| `email_domain.degraded` | A previously verified domain failed a later DNS drift check. | Domain resource snapshot. |
| `email_domain.suspended` | The domain was suspended (reputation or policy). | Domain resource snapshot. |
| `email_domain.deleted` | The domain was deleted. | Domain resource snapshot. |

The five `email_domain.*` events are emitted by the Telnyx email-domains service, `email.received` is emitted by the inbound pipeline, and the other thirteen `email.*` events are handled by the email API (twelve are published as webhooks; `email.sending` is accepted by the subscription schema but never delivered). A webhook subscription can span the full 19-type allowlist; only 18 types are actually delivered. `GET /email_events` stores and returns only its separate outbound message-event taxonomy; it does not return domain lifecycle events or `email.received`.
