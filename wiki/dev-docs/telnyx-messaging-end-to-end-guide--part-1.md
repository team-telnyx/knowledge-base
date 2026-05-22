---
title: 'Telnyx Messaging: End-to-End Guide'
summary: A practical guide to choosing your sender type, configuring messaging profiles,
  sending and receiving messages, tracking delivery with webhooks, understanding rate
  limits and encoding, and troubleshooting errors across the Telnyx Messaging platform.
sources:
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
updated_at: 2026-05-20T08:58:54Z
---

# Telnyx Messaging: End-to-End Guide

*Part 1 of 2 — see also: [Part 2](telnyx-messaging-end-to-end-guide--part-2.md)*

A practical guide to choosing your sender type, configuring messaging profiles, sending and receiving messages, tracking delivery with webhooks, understanding rate limits and encoding, and troubleshooting errors across the Telnyx Messaging platform.

## Choose the right sender type

Pick a sender based on your use case, volume, and geography:

- Transactional alerts (OTPs, reminders, order updates)
  - Best: Toll-free (fast provisioning, high throughput, handset delivery receipts) or 10DLC long code (local presence; requires brand + campaign registration). Short code for very high volume.
- Marketing & promotions
  - Best: 10DLC (required for US A2P marketing), Toll-free (good for mixed traffic; verify), or Short code (premium throughput/brand). RCS for rich, interactive campaigns.
- Conversational/two-way
  - Best: 10DLC (local feel), Toll-free (when local presence isn’t required), RCS for rich interactions.
- International
  - Best: Alphanumeric sender ID (one-way only; widely supported; may require pre-registration in some countries) or local long codes where required.
- Rich media (images, buttons, carousels)
  - Best: RCS for full rich experiences; MMS on long code/toll-free/short code for US/CA.

Notes
- Alphanumeric sender IDs are one-way only and must be 1–11 characters, Latin letters/numbers/spaces, with at least one letter. Not supported in all destinations; may be substituted.
- US toll-free and short codes deliver to US/CA only. For international, use alphanumeric or local numbers.
- Provisioning/registration (typical timelines): 10DLC brand+campaign ~2–3 business days; Toll-free verification ~2–3 business days; Short code 2–6 weeks; RCS 6–10 weeks; Alphanumeric instant.

See [Choosing a Sender Type](choosing-a-sender-type.md) for deeper comparisons and coverage nuances.

## Messaging profiles and number assignment

A messaging profile is your central configuration:
- Assign numbers (required to enable messaging) and define webhook URLs.
- Enable features: Number Pool (geomatch, sticky sender, skip unhealthy), Smart Encoding, MMS transcoding, spend limits, URL shortening.
- Use profiles to separate use cases (e.g., transactional vs. marketing) and control routing/analytics.

Key actions
- Create a profile and set primary/failover webhook URLs.
- Assign one or more messaging-enabled numbers to the profile.
- Optionally enable Number Pool with sticky sender/geomatch for throughput and deliverability.

Learn more in [Messaging Profiles Overview](messaging-profiles-overview.md), [Number Pool](number-pool.md), [Sticky Sender](sticky-sender.md), and [Geomatch](geomatch.md).

## Quick start: sending and receiving

Sending
- Use the same API for all sender types; E.164 format is required (e.g., +15551234567).
- The from value determines sender type automatically: phone number → long code/toll-free, short code digits → short code, alphanumeric string → alpha sender ID.
- For MMS, include public HTTPS media URLs (US/CA only on SMS/MMS routes).

Receiving
- Configure a webhook URL on your messaging profile to receive inbound SMS/MMS events.
- Inbound MMS includes a media array; download within 30 days (authenticated with your API key).

Get step-by-step walkthroughs in [Send Your First Message](send-your-first-message.md) and [Receive Messages](receive-messages.md).

## Delivery tracking and webhooks

Events
- message.received: inbound message to your number.
- message.sent: outbound accepted and sent to carrier.
- message.finalized: terminal status (delivered, delivery_failed, delivery_unconfirmed, etc.).

Behavior and reliability
- Respond to webhook POSTs within 2 seconds (API v2). Telnyx retries with exponential backoff and uses your failover URL if configured.
- Webhook URL priority: per-message webhook_url in the send request, then messaging profile URLs; if none, no webhook is delivered.
- Delivery receipts may vary by carrier; some destinations don’t confirm handset delivery.

Security
- Verify signatures (Ed25519) using telnyx-signature-ed25519 and telnyx-timestamp headers.
- Allowlist 192.76.120.192/27 if you firewall inbound traffic.

See [Receiving Webhooks for Messaging](receiving-webhooks-for-messaging.md) for payloads, verification, and retry policy.

## Throughput, rate limits, and queuing

Defaults (platform-level)
- Account-level defaults (typical): SMS ~50 MPS; MMS ~15 MPS; RCS ~1 MPS.
- Sender-level defaults: Long code ~0.1 MPS per number; Toll-free ~20 MPS per number; Short code ~1000 MPS per code; Alphanumeric ~0.1 MPS per sender ID.

10DLC specifics (US A2P long code)
- AT&T sets throughput per campaign (TPM) based on use case and brand vetting score.
- T-Mobile sets daily brand-level caps based on vetting tier (e.g., 10k–200k/day typical ranges; sole proprietor much lower).
- Verizon relies on content filtering; published limits vary.

Queuing
- Excess messages queue for up to 4 hours (FIFO). When full, API returns 40318 (queue full).
- Queue depth ≈ rate limit (MPS) × 14,400 seconds.

Best practices
- Implement client-side rate limiting; scale throughput with Number Pool (more numbers → higher effective MPS).
- Monitor queue depth and handle 429/40318 with backoff.
- Request higher limits through Telnyx if needed.

Details and carrier tables in [SMS messaging rate limits](sms-messaging-rate-limits.md).

## Message encoding and segmentation

- GSM-7: up to 160 chars in a single segment; 153 per segment when concatenated.
- UTF-16 (triggered by any non‑GSM‑7 character such as emojis/curly quotes): up to 70 chars single; 67 per concatenated segment.
- Extended GSM-7 characters like [, ], {, }, |, \\, ^, ~, and € count as 2 characters each.
- Max 10 segments per message; cost scales with segments.
- Use Smart Encoding to replace common Unicode with GSM‑7 equivalents and reduce cost; consider MMS/RCS for rich content and emojis.

See [Message Encoding](message-encoding.md) for calculators, character sets, and best practices.

## Opt-outs and keyword handling

- If a recipient sends STOP keywords (e.g., STOP, STOP ALL, END, QUIT, UNSUBSCRIBE), Telnyx blocks further messages to that number at the account/number level; API attempts return a 409/blocked error. To unblock, the user must send START/UNSTOP.
- Build explicit opt-in and help flows; see [Opt-In/Out Management](opt-in-out-management.md).
- When building auto-replies, guard against reply loops (especially between automated systems).

## Errors and troubleshooting

Common API responses
- 400 Bad Request: malformed JSON/missing fields.
- 401 Unauthorized: check API key.
- 402 Payment Required: top up account balance.
- 403 Forbidden: number not assigned to a profile, sender registration missing, profile disabled, or recipient opted out.
- 422 Unprocessable: E.164 formatting errors, invalid media URL/size, text too long.
- 429 Too Many Requests: slow down; use retry-after and backoff.
- 5xx: transient; retry with exponential backoff.

Delivery failures (asynchronous)
- Reported via message.finalized webhooks with error codes (e.g., carrier spam filtering, not routable/landline, invalid destination, 10DLC required, toll-free not verified).

Troubleshooting checklist
- Verify API key status; ensure from number is assigned to an enabled messaging profile.
- Confirm E.164 formatting for from/to.
- Complete required registration: 10DLC, toll-free verification, or short code provisioning.
- Check account balance and profile spend limits.
- Review content (length, encoding, URLs/media) and carrier compliance.
- Inspect webhook events and Message Detail Records for final status and error codes.

See [Messaging Error Code Reference](messaging-error-code-reference.md) for complete code lists and guidance.
