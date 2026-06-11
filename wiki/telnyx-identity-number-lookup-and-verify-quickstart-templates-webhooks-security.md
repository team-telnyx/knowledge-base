---
title: 'Telnyx Identity: Number Lookup and Verify (Quickstart, Templates, Webhooks,
  Security)'
summary: 'End‑to‑end guide to Telnyx Identity: perform Number Lookup, set up and send
  verifications (SMS, Call, Flashcall, and Telnyx‑exclusive DTMF Confirm), use custom
  message templates, handle webhooks, and harden your integration against fraud.'
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
  content_hash: fa80def3c3596ad186e98c49e0778e9a6bce97ed4dcc64aaf5f168f9bcc34d88
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
  content_hash: 51000d23488b95ad9217efb823ab288f11b2c71fe6477fcce924de1e28a613b7
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
  content_hash: f4d003c0914ab3c0e385a6aa3a61eae3b51fd21299b8f7ec2386d11ea40f6a4c
- url: https://developers.telnyx.com/docs/identity/verify/quickstart
  content_hash: 267f4f83abfcf6f42b649167ede4e4606307980e6af4396026396a17e22e75a2
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
  content_hash: 878de37eced23fbc390cd86a24a3c4453e3469a30ffb678c2fbb8927181d8b33
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
  content_hash: a984167ebdc1587a5a56e3bc926c8b3e10018b2647310177f0d9dc0b6fce7087
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
  content_hash: 80b2801f7ba79ea32a3d65e2e570c513d49117f924b86b69968e63ffcc09bced
updated_at: 2026-05-08T13:10:58Z
---

# Telnyx Identity: Number Lookup and Verify (Quickstart, Templates, Webhooks, Security)

End‑to‑end guide to Telnyx Identity: perform Number Lookup, set up and send verifications (SMS, Call, Flashcall, and Telnyx‑exclusive DTMF Confirm), use custom message templates, handle webhooks, and harden your integration against fraud.

## Prerequisites and setup
- Create a Telnyx account and generate an API key: [Sign up](https://telnyx.com/sign-up) and see [API keys](https://developers.telnyx.com/development/api-fundamentals/create-api-keys).
- Optional SDKs: `npm install telnyx` (Node). Official clients also exist for Python, Ruby, Go, Java, .NET, and PHP.
- Keep your API key in an environment variable and use HTTPS for all requests.

## Number Lookup essentials
Number Lookup returns carrier, line type, national formatting, country, and optional caller name/portability data for a phone number.
- Basic request (cURL):
  - GET https://api.telnyx.com/v2/number_lookup/{E164_NUMBER}
  - Add Bearer authorization header.
- Include optional types to enrich data:
  - Query flags: `?carrier&caller-name`
  - If omitted, those sections may be null in the response.
- Typical fields you’ll use:
  - `carrier.name`, `carrier.type` (mobile/landline/voip), `country_code`, `national_format`, `caller_name.caller_name`, and `portability.*` (e.g., LRN, city/state, ported status/date).

## Verify methods at a glance
Choose one or multiple verification methods per Verify Profile:
- sms: code in an SMS using a default or custom template.
- call: code spoken by TTS in a voice call.
- flashcall: code embedded in the caller ID of a brief call (app extracts it).
- dtmf_confirm: Telnyx‑only, no code; user simply presses 1 during a call to confirm ownership (great for landlines and low‑friction flows).

## Create a Verify Profile
A Verify Profile centralizes language, timeouts, code length, destination allowlists, and channel settings. You’ll reference its `id` in all verification requests.
- List available message templates to pick one:
  - GET https://api.telnyx.com/v2/verify_profiles/templates
- Create a profile (example fields):
  - POST https://api.telnyx.com/v2/verify_profiles
  - Body highlights:
    - `language`: e.g., `en-US` (also sets TTS language for calls/DTMF Confirm)
    - `sms`: `{ messaging_template_id, whitelisted_destinations, default_timeout_secs, code_length }`
    - `call`: `{ default_timeout_secs }`
    - `dtmf_confirm`: `{ default_timeout_secs }` (optional, for single‑keypress verification)

## Custom message templates (SMS/Call)
Craft branded, compliant OTP content and reference it from profiles.
- Variables supported: `{{app_name}}`, `{{code}}`
- Create template:
  - POST https://api.telnyx.com/v2/verify_profiles/templates
  - Body: `{ "text": "Your {{app_name}} verification code is {{code}}. Do not share this code." }`
- Use it in a profile:
  - `sms.messaging_template_id: <template_id>` when creating/updating a Verify Profile
- Update template text:
  - PATCH https://api.telnyx.com/v2/verify_profiles/templates/{template_id}
- Tips:
  - Keep messages concise (aim <160 chars).
  - Include security warnings for sensitive use cases.
  - Localize via profile `language` and per‑locale templates.

## Send a verification (SMS/Call/Flashcall)
Trigger a verification by method, providing the destination number and your Verify Profile ID.
- SMS: POST https://api.telnyx.com/v2/verifications/sms
- Call: POST https://api.telnyx.com/v2/verifications/call
- Flashcall: POST the corresponding flashcall endpoint (configure `flashcall` on the profile first)
- Common response fields: `id`, `type`, `status` (initially `pending`), `timeout_secs`, `phone_number`, `verify_profile_id`.

## DTMF Confirm (press 1 to verify)
A Telnyx‑unique, code‑less flow that calls the number, plays a standard TTS prompt, and accepts a single keypress:
- Configure on the profile: include `dtmf_confirm.default_timeout_secs`.
- Trigger: POST https://api.telnyx.com/v2/verifications/dtmf_confirm with `phone_number` and `verify_profile_id`.
- Outcomes on the call:
  - `accepted` (digit 1 pressed), `invalid` (wrong digit, 3 attempts max), `expired` (no keypress within ~10s), `error` (call not answered).
- No follow‑up verify API call is needed; completion is driven by the call result and delivered by webhooks (see below).

## Confirm a code (SMS/Call/Flashcall)
For code‑based methods, collect the code from the user and verify:
- POST https://api.telnyx.com/v2/verifications/by_phone_number/{E164_NUMBER}/actions/verify
  - Body: `{ code, verify_profile_id }`
- Response codes:
  - `accepted` (match), `rejected` (wrong code), `expired` (timed out), `max_attempts_exceeded` (too many failures).

## Webhooks and delivery events
Use webhooks for delivery receipts and real‑time completion to avoid polling.
- Configure webhooks on your Verify Profile.
- Delivery lifecycle events (SMS/Call send flow): `verify.sent`, `verify.failed`, `verify.delivered` with `payload.delivery_status` such as `sent`, `delivered`, `sending_failed`, `delivery_failed`, `delivery_unconfirmed`.
- Completion events:
  - DTMF Confirm emits `verification.complete` with `status` like `accepted` or `invalid`.
  - For code‑based flows, you can rely on your own verify response or add webhooks for state changes.
- Network allowlisting for inbound webhooks: accept only from 192.76.120.192/27, require HTTPS, validate payload shape, and never trust client‑side status.

## Security and fraud‑prevention checklist
Layer defenses to stop SMS pumping, toll fraud, and brute force:
- Rate limiting (multi‑layer):
  - Per phone number: 3/10min, 5/hour
  - Per IP: 10/hour
  - Per account/session: 5/hour
  - Global spike monitoring with alerts
- Geo‑fencing: allow only countries you serve via `sms.whitelisted_destinations` on the profile; also validate server‑side. Treat certain country codes as higher‑risk with extra scrutiny.
- Code and timeout hygiene:
  - `code_length`: 5–6 digits recommended (balance UX vs. brute‑force resistance)
  - `default_timeout_secs`: ~300s typical; shorter windows increase security
  - Lockout after too many failed verifications
- Abuse detection and cost controls:
  - Monitor conversion rate (codes sent vs. verified); investigate if <20%
  - Detect sequential or near‑sequential destination numbers
  - Spend alerts and circuit breakers to auto‑pause during anomalies
- Operational response: if under attack, enable circuit breaker, reduce allowlist/rates, investigate patterns, and contact [Telnyx Support](https://support.telnyx.com).

## Troubleshooting DTMF Confirm
- Voicemail answers: result times out as `expired`; retry later or fall back to SMS.
- Wrong digit: up to 3 attempts within the call; after that, status `invalid`.
- Pending without webhook: ensure your webhook URL is reachable and configured; you can poll GET https://api.telnyx.com/v2/verifications/{verification_id} as a fallback.
- Prompt text: currently fixed; voice/language come from the profile’s `language`.

## Helpful references
- Number Lookup overview: [Number Lookup](https://telnyx.com/number-lookup)
- Number Lookup API: [Lookup phone number data](https://developers.telnyx.com/api-reference/number-lookup/lookup-phone-number-data)
- Verify quickstart: [Telnyx Verify quickstart](https://developers.telnyx.com/docs/identity/verify/quickstart)
- DTMF Confirm guide: [DTMF confirmation](https://developers.telnyx.com/docs/identity/verify/dtmf-confirm)
- Custom templates: [Custom templates](https://developers.telnyx.com/docs/identity/verify/custom-templates)
- Webhooks: [Receiving webhooks](https://developers.telnyx.com/docs/identity/verify/receiving-webhooks)
- Hardening guides: [Security Best Practices](https://developers.telnyx.com/docs/identity/verify/security-best-practices), [Rate Limiting & Fraud Prevention](https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention)
