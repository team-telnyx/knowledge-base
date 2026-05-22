---
title: SMS 2FA and Messaging Workflows with Telnyx
summary: A concise, practical guide to build secure SMS-based 2FA and common messaging
  workflows on Telnyx—covering OTP design, compliance, scheduling, sender selection,
  spend controls, and helpful features like group MMS, alphanumeric sender IDs, URL
  shortening, and Zapier automation.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration
updated_at: 2026-05-20T08:59:56Z
---

# SMS 2FA and Messaging Workflows with Telnyx

*Part 1 of 2 — see also: [Part 2](sms-2fa-and-messaging-workflows-with-telnyx--part-2.md)*

A concise, practical guide to build secure SMS-based 2FA and common messaging workflows on Telnyx—covering OTP design, compliance, scheduling, sender selection, spend controls, and helpful features like group MMS, alphanumeric sender IDs, URL shortening, and Zapier automation.

## Prerequisites and setup

- Telnyx account and v2 API key
- A messaging-enabled phone number assigned to a messaging profile
- Webhook URL configured for inbound and status events (as needed)
- For US long codes and toll-free, complete applicable registrations/verification
- See [Phone Number Messaging Configuration](phone-number-messaging-configuration.md) and [Messaging Profiles](messaging-profiles.md)

## Choose a verification approach (DIY vs Verify API)

- DIY with Messaging API: full control over OTP generation, storage, templates, and verification logic
- [Verify API](verify-api.md): managed OTP lifecycle with built-in generation, delivery, retry logic, rate limiting, multi-channel (SMS, voice, WhatsApp), status tracking, and audit logging
- Use DIY only when you need custom flows or tight integration with existing auth systems

## Designing an SMS 2FA flow

Typical steps:
1) Generate a cryptographically secure 6‑digit numeric code
2) Persist it with expiry (e.g., 3–5 minutes) and attempt counter (max ~3)
3) Send via Messaging API (consider local presence using sender selection features below)
4) Verify using constant‑time comparison; invalidate on success or after max attempts/expiry
5) Rate‑limit OTP requests and return the same generic response (“OTP sent”) to avoid enumeration
6) Support device autofill: keep the OTP on its own line; append Android app hash when applicable

## OTP security best practices

- Use crypto‑secure RNG (e.g., Python secrets, Node crypto.randomBytes, Java SecureRandom)
- Short expiry (3–5 minutes); delete expired codes proactively
- Limit verification attempts (e.g., 3) per code/phone
- Constant‑time comparison (e.g., compare_digest/timingSafeEqual)
- Rate‑limit requests (example guardrails):
  - Per phone: ≤1 request per 60s
  - Per IP: ≤10 per hour
  - Per account: ≤5 per hour
- Prefer numeric‑only codes for usability and platform autofill

If you don’t want to build this yourself, use [Verify API](verify-api.md).

## Opt‑in/out compliance and customization

- Default STOP keywords (STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT) create a block rule; START/UNSTOP remove it
- Block rules apply at the messaging profile level; attempting to message a blocked recipient returns 40300 “Blocked due to STOP message”
- Customize auto‑responses and keywords (start/stop/help) per country; reserve keywords START/STOP/HELP cannot be reassigned; up to 20 trigger keywords per config; default ops require ≥20 characters in response text
- Toll‑free numbers also trigger carrier “NETWORK MSG” opt‑out replies you cannot suppress; design your responses to complement them
- Inbound webhooks include autoresponse_type (e.g., STOP/START/HELP) to keep your database in sync
- Learn more in [Advanced Opt-In/Out Management](advanced-opt-in-out-management.md)

## Scheduling and reminders

- Use scheduled sending for precise delivery (e.g., reminders, time‑zone windows)
- Constraints: send_at 5 minutes to 5 days in the future; minute‑level accuracy; up to 1M scheduled messages
- Retrieve/cancel by message ID; cancellation allowed until 1 minute before send time
- Standard messaging webhooks fire at send/finalization time
- For recurring or multi‑window reminders, consider cron or a job queue; see also [Schedule SMS and MMS Messages](schedule-sms-and-mms-messages.md)

## Appointment reminders pattern

- Timing: 24 hours before (primary) and 2–3 hours before (final); avoid overnight; respect recipient time zone
- Content: concise (ideally 1 SMS segment)—name, date/time, short location, reply instructions
- Handle replies: accept CONFIRM/CANCEL (or variants) via inbound webhooks and acknowledge
- Always honor opt‑outs (STOP) and stop scheduling for opted‑out numbers
- See templates and flows in [Appointment Reminders via SMS](appointment-reminders-via-sms.md)

## Sender selection: Number Pool, Sticky Sender, Geomatch

- [Number Pool](number-pool.md): distribute messages across multiple numbers; control long code vs toll‑free with weights; optionally skip unhealthy numbers
- [Sticky Sender](sticky-sender.md): reuse the same number per recipient; mapping persists for 8 days of inactivity (then reselected); takes priority over other selection methods
- [Geomatch](geomatch.md): match recipient’s area code (NANP only) to boost trust; requires Number Pool; priority after Sticky Sender
- Priority order when combined: 1) Sticky mapping exists → use it; 2) else Geomatch if available; 3) else pool weights/availability
- To use the pool, omit from and send with messaging_profile_id; Telnyx will return the selected from in the response

## Spend control and throughput

- [Configurable Spend Limits](configurable-spend-limits.md): per‑profile daily spend cap (USD); on exceed, Telnyx rejects new messages with HTTP 429 and code 40333, sends a webhook and email; auto‑resets at midnight UTC
- Consider separate profiles (and limits) for transactional (e.g., OTP) vs marketing traffic
- Handle 40333 gracefully: alert team, queue for retry after reset, or switch to a backup profile
- Standard throughput/rate limits still apply to immediate and scheduled sends, and to Zapier‑originated traffic

## Alphanumeric sender IDs

- [Alphanumeric Sender ID](alphanumeric-sender-id.md): brand text in the from field; one‑way SMS only (no replies), no MMS
- Format: 1–11 chars; letters/numbers/spaces; must include at least one letter
- Not allowed for US/CA/PR; configure a fallback long code on your profile for those destinations
- Some countries require pre‑registration; check availability; common errors include InvalidFromAddress, AlphaSenderNotConfigured, and UnsupportedDestination

## Group MMS conversations

- [Group Messaging](group-messaging.md): send group MMS to multiple recipients in one call; all participants see each other’s replies (MMS protocol)
- Constraints: MMS only, US/CA only, max 8 recipients (+ sender), billed per recipient, v2 webhooks required
- Inbound group messages include a cc array with other participants; per‑recipient delivery webhooks are emitted

## URL shortening and engagement

- [Custom URL Shortening with Telnyx Messaging](custom-url-shortening-with-telnyx-messaging.md): replace common shortener domains (e.g., bit.ly, t.co) with your branded domain; optional expansion to all domains
- Configure per messaging profile: domain, prefix, replace_blacklist_only toggle, and link‑click webhooks
- View clicks in Message Engagement Reports; feature requires activation by Telnyx/Sales; ensure your custom domain’s DNS is properly configured

## No‑code automations with Zapier

- [Zapier Integration](zapier-integration.md) connects Telnyx to 7,000+ apps
- Triggers: Receive a Message; Actions: Send SMS
- Good for simple workflows (alerts, forwards, auto‑replies); use the API for high‑volume/low‑latency or complex logic
- Limitations: polling delay by plan, SMS‑only (no MMS media), one sender per action step, no delivery status tracking; standard Telnyx rate limits apply

## Phone number configuration and common issues

- Assign each number to a messaging profile before sending/receiving
- US long codes require 10DLC registration; toll‑free requires verification; unregistered traffic may be filtered
- Inbound webhooks require a profile with a valid webhook URL
- Typical send failures: number not on a messaging profile, blocked by STOP (40300), spend limit reached (40333), queue/throughput issues
