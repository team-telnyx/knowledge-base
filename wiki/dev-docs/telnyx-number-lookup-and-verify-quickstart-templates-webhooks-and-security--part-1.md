---
title: 'Telnyx Number Lookup and Verify: Quickstart, Templates, Webhooks, and Security'
summary: Learn how to look up phone number intelligence and implement multi-channel
  verification (SMS, call, flashcall, and Telnyx-only DTMF confirmation). This guide
  covers quickstarts, custom OTP templates, webhook handling, and production-grade
  security and fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-05-20T08:27:44Z
---

# Telnyx Number Lookup and Verify: Quickstart, Templates, Webhooks, and Security

*Part 1 of 2 — see also: [Part 2](telnyx-number-lookup-and-verify-quickstart-templates-webhooks-and-security--part-2.md)*

Learn how to look up phone number intelligence and implement multi-channel verification (SMS, call, flashcall, and Telnyx-only DTMF confirmation). This guide covers quickstarts, custom OTP templates, webhook handling, and production-grade security and fraud prevention.

## Overview
Telnyx provides two complementary identity services:

- Number Lookup: Query carrier, line type, caller name, portability, and national formatting for any E.164 number.
- Verify: Deliver and validate one-time passwords (OTPs) via SMS, phone call, or flashcall, plus a Telnyx-only DTMF confirmation flow that verifies ownership with a single keypress (no code).

## Prerequisites
- Telnyx account and API key.
- Optional SDKs (Node, Python, Ruby, Go, Java, .NET, PHP). Set TELNYX_API_KEY in your environment or pass Bearer YOUR_API_KEY in requests.

## Number Lookup quickstart
Number Lookup returns phone intelligence including carrier, type (mobile/landline/voip), caller name, country code, national format, portability (LRN, ported status, city/state), and more.

- Basic request (add query params to compute extra data):
```
curl -X GET \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --globoff "https://api.telnyx.com/v2/number_lookup/+18665552368?carrier&caller-name"
```
- SDK examples:
  - Python:
    ```
    import telnyx
    telnyx.api_key = "YOUR_API_KEY"
    telnyx.NumberLookup.retrieve("+13129457420")
    ```
  - Node:
    ```
    import Telnyx from 'telnyx'
    const telnyx = new Telnyx("YOUR_API_KEY")
    const { data } = await telnyx.numberLookup.retrieve('+18665552368')
    ```
Notes:
- The response always has the same shape; if you omit types (e.g., carrier, caller-name), those sub-objects may be null.

## Verify methods and profiles
Verify supports multiple methods per profile:
- sms: Sends an OTP via text.
- call: Speaks the OTP over a phone call.
- flashcall: Encodes the OTP in the caller ID of a short call (mobile-app assisted).
- dtmf_confirm: Calls and verifies with a single keypress (press 1). No code, no verify endpoint call; completion happens on the call.

You configure methods on a Verify Profile and reuse the profile when sending or validating codes.

Select a message template (optional, for SMS/call):
```
curl -X GET 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```
Create a profile (example with SMS + call):
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-en",
    "language": "en-US",
    "sms": {
      "messaging_template_id": "TEMPLATE_ID",
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 6
    },
    "call": {
      "default_timeout_secs": 600
    }
  }'
```
Save the returned profile id for use in all verification requests.

## Custom verification message templates
Create branded, compliant OTP messages that interpolate variables:
- {{app_name}} — Application name from the verify profile.
- {{code}} — The generated verification code.

Create a template:
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }'
```
Use it in a profile (sms.messaging_template_id):
```
curl -X POST 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-verification",
    "language": "en-US",
    "sms": {
      "messaging_template_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 6
    }
  }'
```
Update a template:
```
curl -X PATCH 'https://api.telnyx.com/v2/verify_profiles/templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} code is {{code}}. Contact support if you did not request this."
  }'
```
Best practices:
- Keep under ~160 chars to avoid splitting.
- Include security warnings (e.g., never share codes).
- Test formatting, variable substitution, and character counts.
- Localize per region; set profile language accordingly.

## Send and verify codes (SMS and call)
Send an SMS verification:
```
curl -X POST https://api.telnyx.com/v2/verifications/sms \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number":"+13035551234","verify_profile_id":"YOUR_PROFILE_ID"}'
```
Send a call verification (reads the code aloud):
```
curl -X POST https://api.telnyx.com/v2/verifications/call \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number":"+13035551234","verify_profile_id":"YOUR_PROFILE_ID"}'
```
Verify a received code (for SMS/call):
```
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"code":"17686", "verify_profile_id": "YOUR_PROFILE_ID"}' \
  https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify
```
Result codes: accepted, rejected, expired, max_attempts_exceeded.

## DTMF confirmation (press 1 to verify)
DTMF confirmation is unique to Telnyx. It calls the number, plays a standard TTS prompt, and collects a single keypress (1) to confirm ownership. No code is generated and no verify action call is required.

Create a profile with DTMF confirm:
```
curl -X POST https://api.telnyx.com/v2/verify_profiles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "name": "caller-id-verification",
    "language": "en-US",
    "dtmf_confirm": { "default_timeout_secs": 300 }
  }'
```
Trigger a DTMF confirm verification:
```
curl -X POST https://api.telnyx.com/v2/verifications/dtmf_confirm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number": "+13035551234", "verify_profile_id": "YOUR_PROFILE_ID"}'
```
Outcomes per call attempt (up to 3 tries):
- Pressed 1 → accepted
- Wrong digit → invalid
- No keypress (10s) → expired
- Not answered → error

The TTS language follows the profile language. The prompt text is fixed (no custom TTS text yet).

## Webhooks and delivery/status events
Configure your Verify profile to receive events:
- Delivery lifecycle: verify.sent, verify.failed, verify.delivered
- Real-time completion: verification.complete (e.g., DTMF accepted/invalid)

Example completion event payload (shape):
```
{
  "data": {
    "event_type": "verification.complete",
    "payload": {
      "id": "...",
      "phone_number": "+13035551234",
      "status": "accepted|invalid|expired|error",
      "type": "sms|call|flashcall|dtmf_confirm",
      "verify_profile_id": "..."
    }
  }
}
```
Webhook security:
- Allowlist Telnyx IPs: 192.76.120.192/27
- Use HTTPS; validate payload structure; don’t trust client-reported status.

Polling fallback (if needed):
```
curl https://api.telnyx.com/v2/verifications/{verification_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```
