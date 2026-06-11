---
title: Telnyx Messaging
summary: Telnyx Messaging provides a comprehensive API for sending and receiving SMS
  and MMS messages, with features including messaging profiles, alphanumeric sender
  IDs, geomatching, group messaging, two-factor authentication, appointment reminders,
  advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed
  error handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
  content_hash: e660dfc64ea2a2d6911f7d1a970f5a932c04da65aae78776e3c1ca3b18448b6d
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
  content_hash: 5fd82d8d9312b6ac6e28c0c73d0a00bf774769a0dd423127c48f73f591d7b3b9
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
  content_hash: abbae58584ee6800d04c5231b8e3b77d97f8af428a35e1c1433eb2378e318112
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
  content_hash: 6985fd062cf97e7e1fbaad7066a3bf2314c4f3753dd0115043ce47f104d1701e
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
  content_hash: 3debaf7e27ff822d9bbebe435006ae4d2d6d8b93ce63335ec32a07d69af3b79f
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
  content_hash: 1689fb1fb284ac9037440148c10c18cf7db9961ed4a23dc6b836eadbc54eb215
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
  content_hash: e1967e40b4a047d11b5125f1a52bc6d4e705bb3c9091fea33b0be3327dce7b6e
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
  content_hash: 482afc03676e3bc869ddc8ddcdc2e664b63ccf582eee0d99dc25181db71831b7
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
  content_hash: 39a6ee872f771c4a346c0ea1af391c578a9a69489623cf565ace914e877ab528
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
  content_hash: 183a7b2c87a6b2c0609b46d90d10746ff0ec211ef8ba7a7b4d481130f51b73ba
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
  content_hash: 178148332abbc910363f6baca179c2f8701f9fae87ddda430a5727b8c5bddc83
updated_at: 2026-06-11T10:36:31Z
---

# Telnyx Messaging

*Part 2 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md)*

Telnyx Messaging provides a comprehensive API for sending and receiving SMS and MMS messages, with features including messaging profiles, alphanumeric sender IDs, geomatching, group messaging, two-factor authentication, appointment reminders, advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed error handling.

## SMS Two-Factor Authentication

Implement SMS-based 2FA using the Telnyx Messaging API. This involves generating a cryptographically secure OTP, sending it via SMS, and verifying it with security best practices.

Consider the [Telnyx Verify API](telnyx-verify-api.md) first — it handles OTP generation, delivery, and verification for you, including retry logic, rate limiting, and multi-channel support (SMS, voice, WhatsApp). Use the DIY approach only if you need full control over the 2FA flow.

### Security Best Practices

- **Use cryptographically secure random generation** — never use `Math.random()`, `rand()`, or similar. Use `secrets.choice()` (Python), `crypto.randomBytes()` (Node), `SecureRandom.random_number()` (Ruby), `crypto/rand.Int()` (Go), `SecureRandom.nextInt()` (Java), `RandomNumberGenerator.GetBytes()` (.NET), or `random_int()` (PHP).
- **Set expiry times** — OTPs should expire after 3–5 minutes. Never allow OTPs to be valid indefinitely.
- **Limit verification attempts** — allow a maximum of 3 attempts per OTP. After exceeding the limit, invalidate the OTP and require a new one.
- **Use constant-time comparison** — use `secrets.compare_digest()` (Python), `crypto.timingSafeEqual()` (Node), `subtle.ConstantTimeCompare()` (Go), `MessageDigest.isEqual()` (Java), `CryptographicOperations.FixedTimeEquals()` (.NET), or `hash_equals()` (PHP) to prevent timing attacks.
- **Rate limit OTP requests** — per phone number: 1 request per 60 seconds; per IP address: 10 per hour; per account: 5 per hour. Return the same response regardless of whether the number exists to prevent enumeration attacks.
- **Use numeric-only codes** — they are easier to type on mobile, compatible with SMS autofill, and sufficient with attempt limits and expiry (a 6-digit code has 1,000,000 possible values; with a 3-attempt limit, guessing probability is 0.0003%).
- **Support SMS autofill** — Android (SMS Retriever API): include your app's hash at the end of the message. iOS: automatically detects codes from messages containing "code" or "passcode"; keeping the OTP on its own line helps.

## Appointment Reminders

Reduce no-shows by sending automated SMS appointment reminders. This covers scheduling strategies, message templates, opt-out handling, and timing best practices.

### Scheduling Strategies

- **Telnyx Scheduled Messages** — use the built-in `send_at` parameter. No infrastructure needed. Limited to single scheduled time per API call, max 7 days in advance.
- **Cron / Job Scheduler** — run a periodic job that queries your database for upcoming appointments. Full control, supports multiple reminder windows, but requires scheduler infrastructure.
- **Event-Driven Queue** — schedule individual reminder jobs when appointments are created using a task queue (Celery, Bull, Sidekiq). Precise timing and scalable, but requires message queue infrastructure.

### Handling Replies

Set up a webhook to receive replies (e.g., CONFIRM / CANCEL) and update appointment status. Respond with confirmation or cancellation messages accordingly.

### Opt-Out Handling

Telnyx automatically handles standard opt-out keywords for US long codes and toll-free numbers. Additionally, track opt-outs in your application database to prevent scheduling reminders for opted-out users.

### Timing Best Practices

- **24 hours before** — primary reminder with enough time to cancel/reschedule
- **2–3 hours before** — final reminder for same-day appointments
- **Avoid late night/early morning** — only send between 9 AM and 8 PM in the recipient's local time zone
- For high-value appointments, send two reminders (48/24 hours + 2–3 hours before)
- Always calculate reminder times in the recipient's local time zone
- Keep messages under 160 characters when possible to minimize costs

## Advanced Opt-In/Out

Customize keyword triggers and auto-responses on your messaging profile. Configure country-specific responses, custom keywords, and track opt-out behavior via webhooks — all while maintaining CTIA & TCPA compliance.

### Operation Types

| Operation (`op`) | Purpose | Default Keywords |
|---|---|---|
| `start` | Opt-in — removes block rule | START, UNSTOP |
| `stop` | Opt-out — creates block rule | STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT |
| `help` | Help — sends info response | HELP |
| Custom | Any custom keyword response | (none) |

Create custom auto-responses via `POST /v2/messaging_profiles/{profile_id}/autoresp_configs`.

### Country-Specific Auto-Responses

Configure different responses per country using ISO 3166-1 alpha-2 codes. The feature is language agnostic — you can use keywords and responses in any language. The `country_code` field determines which auto-response applies based on the sender's number origin.

### Tracking Opt-Out Webhooks

Inbound message webhooks include an `autoresponse_type` field (e.g., `STOP`, `START`, `HELP`) when a user sends an opt-in, opt-out, or help keyword. This field is also available in SMS Logs via Detail Record Search.

### Limitations

- **Reserved keywords** — START, STOP, and HELP cannot be reassigned to different operations. You can add additional keywords, but defaults always remain active.
- **Minimum 20 characters** for auto-response messages on default operations (carrier compliance).
- **Maximum 20 trigger keywords** per configuration.
- **Toll-free limitations** — toll-free numbers have a separate carrier-level opt-out system. Both the carrier's NETWORK MSG and your custom response are sent. You cannot prevent the carrier's messages.
- **Block rule scope** — block rules apply at the messaging profile level, not the individual number level. To manage separate opt-out lists for different programs, use separate messaging profiles.

## Configurable Spend Limits

Messaging profiles can be configured with a daily spending limit to prevent unexpected costs. When the limit is reached, outbound messages are rejected until the limit resets at midnight UTC.

### Setup

Enable `daily_spend_limit_enabled` and set a `daily_spend_limit` value (in USD, as a string) on your messaging profile via PATCH request. The limit applies per messaging profile — use separate profiles for different budgets.

### When the Limit Is Reached

1. New messages are rejected with HTTP `429` and error code `40333`
2. A `messaging-profile.spend-limit-reached` webhook is sent
3. An email notification is sent to your account

There may be a short delay between reaching the limit and enforcement. A small number of additional messages may be sent during this window, causing `current_cost` to slightly exceed `configured_limit`.

### Reset and Override

- **Automatic daily reset** — the running spend total resets at midnight UTC. Changing the limit values does not reset the running total.
- **Temporary override** — disable the limit, send urgent messages, then re-enable. Re-enabling does not reset the counter; if current spend exceeds the limit, messages will be blocked again immediately.
- **Increase the limit** — takes effect immediately.

### Best Practices

- Set limits on all production profiles
- Use separate profiles for different use cases (transactional vs. marketing)
- Set up webhook monitoring for spend limit events
- Build error handling for error code `40333`
- Review limits regularly as volume grows
