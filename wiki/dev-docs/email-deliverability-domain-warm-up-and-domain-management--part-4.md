---
title: Email Deliverability, Domain Warm-up, and Domain Management
summary: How mailbox providers evaluate mail, how to authenticate and warm up a sending
  domain with Telnyx, how to read delivery events and error codes, and how to register,
  verify, and manage email domains.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/deliverability-best-practices
- url: https://developers.telnyx.com/docs/messaging/email/deliverability/index
- url: https://developers.telnyx.com/docs/messaging/email/domains/index
updated_at: 2026-08-05T13:54:17Z
---

# Email Deliverability, Domain Warm-up, and Domain Management

*Part 4 of 7 — see also: [Part 1](email-deliverability-domain-warm-up-and-domain-management--part-1.md), [Part 2](email-deliverability-domain-warm-up-and-domain-management--part-2.md), [Part 3](email-deliverability-domain-warm-up-and-domain-management--part-3.md), [Part 5](email-deliverability-domain-warm-up-and-domain-management--part-5.md), [Part 6](email-deliverability-domain-warm-up-and-domain-management--part-6.md), [Part 7](email-deliverability-domain-warm-up-and-domain-management--part-7.md)*

How mailbox providers evaluate mail, how to authenticate and warm up a sending domain with Telnyx, how to read delivery events and error codes, and how to register, verify, and manage email domains.

## Warm up your sending domain

Inbox providers build reputation for both the sending IP and the authenticated domain. Telnyx manages the shared sending infrastructure; you build your domain reputation through recipient quality, consistent volume, and wanted email.

Warm up when you:

- Send from a new domain or subdomain.
- Move an established domain to Telnyx or change sending providers.
- Resume sending after a long inactive period.
- Increase your normal volume substantially.

Low-volume transactional senders may warm naturally as real usage grows. Do not generate artificial traffic just to follow a schedule.

### Before you increase volume

- Send from a dedicated subdomain, such as `mail.example.com`, that you do not use for employee email.
- Keep transactional and marketing traffic on separate subdomains when possible.
- Verify the domain and publish the SPF, DKIM, and DMARC records returned by Telnyx.
- Start with recipients who explicitly opted in and recently engaged with your product.
- Remove invalid addresses and honor all bounces, complaints, and unsubscribes.
- Configure [Webhooks & Events](webhooks-events.md) before the first production send.
- Register your authenticated domain with [Google Postmaster Tools](https://postmaster.google.com/) and use any other mailbox-provider reporting available to you. Provider-reported spam rates are not the same as Telnyx complaint events.

### Conservative starting schedule

There is no universal warm-up schedule. Mailbox providers evaluate Gmail, Microsoft, Yahoo, and other traffic independently, so review each provider before advancing. Use this as a starting point for a new domain with a clean, opted-in audience. These are reputation-based ceilings, not Telnyx account quotas. If your account's sending quota is lower, the lower limit applies. See [Rate Limits & Quotas](rate-limits-quotas.md).

In this schedule, one message means one recipient delivery. Every address in `to`, `cc`, and `bcc` counts toward the daily ceiling for that recipient's mailbox provider. It does not mean one API request. The Email API rejects the same normalized recipient address appearing more than once across those fields.

| Stage | Suggested maximum | What to do |
| --- | --- | --- |
| Days 1–2 | 100–500 messages per major mailbox provider per day | Send only to your most recently engaged recipients. Spread sends throughout the day. |
| Days 3–4 | Up to 2× the previous successful daily volume | Increase only where delivery signals remain healthy. |
| Days 5–7 | Increase by 50–100% per day | Hold volume for providers showing increased deferrals or filtering. |
| Week 2 onward | Increase by 20–50% per day | Continue toward normal volume. A high-volume domain may take 3–6 weeks to establish reputation. |

A schedule is a ceiling, not a promise. Do not increase volume simply because another day passed. Hold or reduce it when delivery signals worsen.

If your normal traffic is below these amounts, send only real, wanted traffic appropriate to that sending stream. Never purchase recipients, send to fake addresses, or create synthetic engagement to warm a domain.

### Migrating an established domain

An established domain may retain some reputation history, but a new sending provider introduces new infrastructure and a changed sending pattern. Keep the previous provider available during the transition, then move a small portion of wanted traffic to Telnyx and increase it gradually. Preserve your recognizable From address and authentication alignment throughout the migration.

### Decide whether to increase, hold, or pause

Review delivery events by mailbox provider at least daily during warm-up. `GET /v2/email_events` does not provide a mailbox-provider filter. Group events using the domain in `payload.recipient` and, when present, `payload.mx_hostname`. Multiple recipient domains can belong to the same provider — for example, Outlook, Hotmail, and Live are all Microsoft traffic.

| Signal | Action |
| --- | --- |
| Delivery is stable; complaints and hard bounces remain low | Continue the planned increase. |
| `email.deferred` events or provider throttling increase | Hold at the current volume or reduce it until performance normalizes. |
| Hard bounces rise | Pause new volume, validate the source of your addresses, and remove invalid recipients. |
| Provider-reported spam rate approaches 0.1%, or `email.complained` events increase | Pause the ramp and investigate consent, targeting, content, and frequency. Gmail and Yahoo require senders to remain below 0.3%, but you should operate well below that limit. |

A receiving server accepting a message means it was delivered to that server, not necessarily placed in the inbox. Provider reputation tools and controlled inbox-placement tests can supply additional visibility.

Use provider-reported spam rates and Telnyx complaint events together. Google's thresholds refer to the spam rate reported in Google Postmaster Tools, while Yahoo calculates its spam rate from mail delivered to the inbox. Telnyx's `complaint_rate` is the percentage of delivered recipients for whom Telnyx received an individual feedback report. Reporting coverage still differs by provider, so the metrics are not directly comparable.

### Avoid these warm-up mistakes

- Sending your full audience on the first day.
- Warming with purchased, scraped, old, or unengaged lists.
- Sending only to Gmail while assuming other mailbox providers are warming too.
- Retrying permanent failures or suppressed recipients.
- Mixing risky marketing campaigns with password resets, receipts, or other transactional mail.
- Increasing volume while deferrals, bounces, or complaints are getting worse.
