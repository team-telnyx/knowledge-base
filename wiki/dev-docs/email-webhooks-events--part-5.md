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

*Part 5 of 5 — see also: [Part 1](email-webhooks-events--part-1.md), [Part 2](email-webhooks-events--part-2.md), [Part 3](email-webhooks-events--part-3.md), [Part 4](email-webhooks-events--part-4.md)*

Telnyx email events flow through three consumption surfaces — recipient-scoped webhooks, the Events API for polling, and per-message lookups — covering the full lifecycle from queued through delivered, bounced, and engagement signals, plus domain lifecycle events. This page documents the event model, webhook payload envelope, signature verification, polling endpoints, and how to combine both surfaces in production.

## Choosing and combining both

Most production setups use both surfaces together:

1. **Webhooks for real-time reactions** — subscribe each domain to the event types your app cares about (`email.delivered`, `email.bounced`, `email.complained` are the common minimum). Verify signatures, return `2xx` fast, and process asynchronously. Remember each callback is **one recipient**: key your handler on `payload.recipient_id`, not on `payload.id`.
2. **Polling for reconciliation and backfill** — run a periodic `GET /email_events` (or `GET /email_events/stats` for dashboards) to recover overlapping stored outbound message events missed during webhook downtime and to compute aggregate metrics. It cannot recover `email.received` or `email_domain.*` webhooks, and it does not return `error_evidence`.
3. **Per-message lookups for support** — use `GET /email_messages/{email_id}/events` to show a single message’s delivery timeline on demand.
4. **The inbound WebSocket for received mail** — use `/email_events/ws` only for inbound `email.received` streaming; it carries no outbound delivery events.

Keep your webhook `events` allowlist tight. Subscribing to every event type is valid, but most applications only need a handful — filtering at the subscription reduces your endpoint’s load and the noise you have to sift through. Because delivery webhooks are recipient-scoped, a broad allowlist on a large multi-recipient send multiplies your callback volume by the recipient count.
