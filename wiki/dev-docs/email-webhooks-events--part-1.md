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

*Part 1 of 5 — see also: [Part 2](email-webhooks-events--part-2.md), [Part 3](email-webhooks-events--part-3.md), [Part 4](email-webhooks-events--part-4.md), [Part 5](email-webhooks-events--part-5.md)*

Telnyx email events flow through three consumption surfaces — recipient-scoped webhooks, the Events API for polling, and per-message lookups — covering the full lifecycle from queued through delivered, bounced, and engagement signals, plus domain lifecycle events. This page documents the event model, webhook payload envelope, signature verification, polling endpoints, and how to combine both surfaces in production.

## Overview

Every email sent through Telnyx emits events as it moves through the delivery lifecycle — from `queued` to `sent` to `delivered` (or `bounced`/`failed`), plus engagement signals like `opened` and `clicked`. Email domains also emit lifecycle webhooks (`email_domain.verified`, `email_domain.suspended`, …). This guide covers three related surfaces: **webhooks** (push, real time, recipient-scoped), **message-event polling** (pull, on demand, mixed cardinality), and **per-message event history** (scoped to a single email).

Polling is a first-class option for stored outbound message events: if you don’t have a publicly reachable HTTPS endpoint — common for agents, batch jobs, and on-prem services — you can query `GET /email_events` with no webhook infrastructure. Polling and webhooks overlap, but their event taxonomies and payload shapes are not identical — see [#Event schemas by surface](event-schemas-by-surface.md).

## Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up) with an [email domain](domains-dkim.md) configured and verified
- Your [API key](https://portal.telnyx.com/#/app/api-keys)
- For webhooks: a publicly accessible HTTPS endpoint (or [ngrok](/development/development-tools/ngrok-setup) for local development) and your [public key](https://portal.telnyx.com/#/app/api-keys) for signature verification
