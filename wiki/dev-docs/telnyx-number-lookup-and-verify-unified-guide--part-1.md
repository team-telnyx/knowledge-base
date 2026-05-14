---
title: 'Telnyx Number Lookup and Verify: Unified Guide'
summary: Build phone intelligence and secure user verification flows with Telnyx.
  This guide combines Number Lookup fundamentals with a practical, security‑hardened
  Verify implementation, including SMS/Call/Flashcall, DTMF Confirm, custom templates,
  webhooks, and fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/quickstart
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-05-14T09:50:03Z
---

# Telnyx Number Lookup and Verify: Unified Guide

*Part 1 of 2 — see also: [Part 2](telnyx-number-lookup-and-verify-unified-guide--part-2.md)*

Build phone intelligence and secure user verification flows with Telnyx. This guide combines Number Lookup fundamentals with a practical, security‑hardened Verify implementation, including SMS/Call/Flashcall, DTMF Confirm, custom templates, webhooks, and fraud prevention.

## Key capabilities

- Number Lookup: retrieve carrier, line type, caller name, portability/LRN, national formatting, and country code for a phone number.
- Verify (OTP): send and verify one-time passwords via SMS, voice call, or flashcall; or confirm ownership with a single keypress via DTMF Confirm.
- Custom templates: brand your OTP messages with {{app_name}} and {{code}} variables.
- Webhooks: receive delivery and completion events in real time.
- Security: rate limiting, geo-fencing, anomaly detection, and webhook hardening.

## Number Lookup: carrier, caller name, and portability

Number Lookup returns rich metadata about a number, such as:
- carrier name and type (mobile, landline, VoIP)
- caller_name (CNAM)
- country_code and national_format
- portability details (line_type, LRN, city/state, ported status/date)

Basic request (REST):
```
curl -X GET \
  -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/number_lookup/+18665552368"
```

Requesting CNAM and carrier details explicitly:
```
# Query parameters style
curl -X GET \
  -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/number_lookup/+18665552368?carrier&caller-name"
```

Notes
- If caller-name/carrier are not requested, their fields may be null.
- SDKs (Node, Python, Ruby) provide helpers like NumberLookup.retrieve(+E.164) and optional type flags.

## Verify: methods and profiles

Verification methods
- sms: code sent via text message using a default or custom template.
- call: code spoken by TTS to the recipient.
- flashcall: code embedded in the caller ID of a brief call (app parses automatically).
- dtmf_confirm: Telnyx calls and collects a single keypress (1) to confirm ownership; no code generated.

Create a Verify Profile (choose channels, language, and defaults):
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-profile",
    "language": "en-US",
    "sms": {"default_timeout_secs": 300, "code_length": 6},
    "call": {"default_timeout_secs": 600}
  }'
```

Tip
- Use separate profiles per application or locale. Profiles can include multiple verification methods concurrently for fallbacks.

## Custom verification templates

Template variables
- {{app_name}} — your application name from the Verify Profile
- {{code}} — the generated verification code

Create a template:
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"text": "Your {{app_name}} verification code is {{code}}. Do not share this code."}'
```

Use the template on a profile (SMS example):
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-verification",
    "language": "en-US",
    "sms": {
      "messaging_template_id": "TEMPLATE_ID",
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 6
    }
  }'
```

Update a template (propagates to all referencing profiles):
```
curl -X PATCH 'https://api.telnyx.com/v2/verify_profiles/templates/TEMPLATE_ID' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."}'
```

Best practices for templates
- Keep under 160 characters to avoid multipart SMS.
- Include security warnings (e.g., “Never share this code with anyone.”).
- Localize per region; use the profile language field to align TTS and messaging.

## Sending verifications (SMS, Call, Flashcall)

Trigger SMS:
```
curl -X POST 'https://api.telnyx.com/v2/verifications/sms' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"phone_number":"+13035551234","verify_profile_id":"PROFILE_ID"}'
```

Trigger Call:
```
curl -X POST 'https://api.telnyx.com/v2/verifications/call' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"phone_number":"+13035551234","verify_profile_id":"PROFILE_ID"}'
```

General guidance
- SMS is fastest and broadest; fall back to call for landlines or delivery issues.
- Flashcall can be primary in supported mobile-app scenarios with SMS fallback.

## Verifying codes (SMS/Call) and outcomes

Submit the code your user enters:
```
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"code":"17686","verify_profile_id":"PROFILE_ID"}' \
  "https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify"
```

Response codes
- accepted — code is correct; verification successful
- rejected — code is incorrect
- expired — exceeded timeout_secs window
- max_attempts_exceeded — too many incorrect attempts

## DTMF Confirm: single-keypress verification

What it is
- Telnyx places a call, plays a TTS prompt, and collects a single keypress (1) to confirm ownership. No OTP is generated, and you do not call the verify action endpoint. The call itself completes verification.

Outcomes during the call
- accepted — recipient pressed 1
- invalid — wrong digit (up to 3 attempts)
- expired — no keypress within ~10 seconds
- error — call not answered or failed

Configure a profile and trigger:
```
# Profile
curl -X POST https://api.telnyx.com/v2/verify_profiles \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"name":"caller-id-verification","language":"en-US","dtmf_confirm":{"default_timeout_secs":300}}'

# Start verification
curl -X POST https://api.telnyx.com/v2/verifications/dtmf_confirm \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"phone_number":"+13035551234","verify_profile_id":"PROFILE_ID"}'
```

Notes
- Default TTS prompt explains the purpose and asks the user to press 1. The language follows the profile’s language (e.g., en-US).
- Ideal for landlines and low-friction caller ID ownership checks.

## Webhooks: delivery and completion

Delivery events (for send attempts)
- verify.sent — sent to upstream provider
- verify.delivered — delivery confirmed by provider
- verify.failed — sending failed

Completion events
- verification.complete — final status for a verification (e.g., accepted, invalid, expired). DTMF Confirm completes entirely on the call; for code-based methods, you can rely on webhooks instead of polling.

Operational notes
- Prefer event-driven workflows; avoid polling unless as a fallback.
- Allowlist Telnyx webhook subnet 192.76.120.192/27 and use HTTPS.
- Validate payload structure and never trust client-reported status.

## Security best practices (must‑dos)

Rate limiting (typical starting points)
- Per phone number: 3 attempts per 10 minutes; 5 per hour
- Per IP address: 10 attempts per hour
- Per account/session: 5 attempts per hour
- Monitor global volume for spikes

Code security
- Code length: 5–6 digits (configure on profile) for strong entropy vs. usability
- Timeouts: ~300s default; shorter windows increase security
- Max failed attempts lockout to deter brute force
- Prevent number enumeration: return the same generic response regardless of account existence

Channel strategy
- Primary SMS → fallback Call if not delivered in ~30s
- Consider Flashcall for supported mobile markets to minimize friction

Webhook security
- HTTPS only, IP allowlist, strict payload validation, server-side verification of outcomes
