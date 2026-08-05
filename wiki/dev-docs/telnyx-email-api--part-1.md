---
title: Telnyx Email API
summary: The Telnyx Email API is a full email platform combining transactional sending,
  bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure
  that powers Telnyx's global messaging network. This page covers the API's capabilities,
  architecture, getting-started paths, inboxes, migration from other ESPs, and rate
  limits and quotas.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/inboxes/index
- url: https://developers.telnyx.com/docs/messaging/email/migrate-to-telnyx
- url: https://developers.telnyx.com/docs/messaging/email/overview
- url: https://developers.telnyx.com/docs/messaging/email/quickstart
- url: https://developers.telnyx.com/docs/messaging/email/rate-limits
updated_at: 2026-08-05T13:51:25Z
---

# Telnyx Email API

*Part 1 of 5 — see also: [Part 2](telnyx-email-api--part-2.md), [Part 3](telnyx-email-api--part-3.md), [Part 4](telnyx-email-api--part-4.md), [Part 5](telnyx-email-api--part-5.md)*

The Telnyx Email API is a full email platform combining transactional sending, bi-directional inboxes, deliverability tooling, and event tracking on the same infrastructure that powers Telnyx's global messaging network. This page covers the API's capabilities, architecture, getting-started paths, inboxes, migration from other ESPs, and rate limits and quotas.

## Overview

The Telnyx Email API is a full email platform — not just a send endpoint. It combines transactional sending, bi-directional inboxes, deliverability tooling, and event tracking into a single API built on the same infrastructure that powers Telnyx's global messaging network.

| Capability | What it does |
| --- | --- |
| **Send email** | Transactional and marketing email with HTML, attachments, scheduling, idempotency, and batch sending |
| **Receive email** | Full inboxes with threads, labels, drafts, replies, forwarding, and sender filters |
| **Track everything** | Open tracking, click tracking, unsubscribe tracking, and a complete event lifecycle from queued to delivered |
| **Manage reputation** | Automatic suppressions, unsubscribe groups, deliverability monitoring, and domain reputation scoring |
| **Use templates** | Liquid-templated email templates with variable auto-extraction |
| **Validate addresses** | Single and batch email validation to reduce bounces before you send |
| **Own your domain** | Full DKIM/SPF/DMARC support with automated DNS record generation and verification |
| **Instant onboarding** | Shared domain for two-minute sends with zero DNS setup |

Telnyx Email runs on the same global infrastructure that powers Telnyx's messaging network:

- **REST API** for all operations — sending, inbox management, domain configuration, suppressions, and events
- **Webhooks** for real-time delivery and engagement events (queued, sent, delivered, bounced, opened, clicked, unsubscribed)
- **Polling** for on-demand event retrieval via `GET /email_events`
- **Fully managed** — no mail server setup, no IP warmup, no MTA configuration

**Email API is in invite-only beta.** Access is limited to accounts with the `email.beta_access` capability enabled. Contact support to request access.

## API surfaces

| Surface | Endpoint prefix | Guide |
| --- | --- | --- |
| Messages | `/email_messages` | [Sending Email](sending-email.md) |
| Inboxes | `/email_inboxes` | [Manage Inboxes](manage-inboxes.md) |
| Threads | `/email_threads` | [Manage Inboxes](manage-inboxes.md) |
| Domains | `/email_domains` | [Email Domains & DKIM](email-domains-dkim.md) |
| Validation | `/email_validations` | [Email Validation](email-validation.md) |
| Templates | `/email_templates` | [Email Templates](email-templates.md) |
| Suppressions | `/email_blocks` | [Suppressions & Unsubscribes](suppressions-unsubscribes.md) |
| Unsubscribe Groups | `/email_unsubscribe_groups` | [Unsubscribe Groups](unsubscribe-groups.md) |
| Events | `/email_events` | [Webhooks & Events](webhooks-events.md) |
