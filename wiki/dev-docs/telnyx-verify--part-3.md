---
title: Telnyx Verify
summary: The Telnyx Verify API enables robust two-factor authentication and phone-number
  verification using carrier-grade voice and messaging. This page consolidates the
  Verify quickstart, custom templates, DTMF confirmation, webhooks, security best
  practices, and rate-limiting/fraud-prevention guidance into a single reference covering
  SMS, call, flashcall, and DTMF confirm verification methods, profile configuration,
  code verification, and production hardening.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-07-17T09:13:37Z
---

# Telnyx Verify

*Part 3 of 6 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 4](telnyx-verify--part-4.md), [Part 5](telnyx-verify--part-5.md), [Part 6](telnyx-verify--part-6.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Trigger a verification

To send a verification attempt, you need the Verify Profile ID, the phone number that will receive the message, and the verification type.

### SMS

SMS verification sends a code via text message. This is the most common method with the widest global coverage.

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"phone_number":"+13035551234","verify_profile_id":"4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
  https://api.telnyx.com/v2/verifications/sms
```

**User experience:** The user receives a text message with a numeric code (e.g., "Your verification code is: 17686"). They enter this code in your application.

### Call

Call verification speaks the code aloud when the user answers. Useful when the user cannot receive SMS (landlines, VoIP) or in regions with unreliable SMS delivery.

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"phone_number":"+13035551234","verify_profile_id":"4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
  https://api.telnyx.com/v2/verifications/call
```

**User experience:** The user receives a phone call. An automated voice reads the verification code aloud (e.g., "Your verification code is 1-7-6-8-6"). The code is repeated twice. The user then enters the code in your application.

**DTMF confirmation:** You can optionally enable DTMF confirmation, where the user enters the code on their phone keypad during the call instead of typing it in your app. See the [DTMF Confirmation Verification](dtmf-confirmation-verification.md) guide for details.

### DTMF confirm

DTMF confirmation calls a phone number, plays a TTS prompt, and collects a single keypress (`1`) to confirm ownership. No verification code is generated — the keypress is the confirmation. The `POST /verifications/{id}/actions/verify` endpoint is **not used**; verification completes on the call itself.

```
curl -X POST https://api.telnyx.com/v2/verifications/dtmf_confirm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "phone_number": "+13035551234",
    "verify_profile_id": "YOUR_PROFILE_ID"
  }'
```

Example response:

```
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "phone_number": "+13035551234",
    "record_type": "verification",
    "status": "pending",
    "type": "dtmf_confirm",
    "timeout_secs": 300,
    "verify_profile_id": "YOUR_PROFILE_ID",
    "created_at": "2026-02-20T15:30:00.000000",
    "updated_at": "2026-02-20T15:30:00.000000"
  }
}
```

Default TTS prompt:

> *"This is a verification call to confirm that this phone number is going to be used as a Caller ID for outbound calls. If you did not request this verification, or if someone is asking you to accept this call, please ignore this message. If you did request this verification, please press 1."*

The TTS language is determined by the `language` field on the Verify Profile (default: `en-US`). The prompt is fixed to the standard verification message — custom prompt text is not yet supported.

#### DTMF flow outcomes

| Outcome | Trigger | Status |
| --- | --- | --- |
| Confirmed | Digit `1` pressed | `accepted` |
| Rejected | Wrong digit | `invalid` |
| Timed out | No keypress (10s) | `expired` |
| Failed | Call not answered | `error` |

Up to 3 attempts per call. After 3 wrong digits, the call ends with status `invalid`.

### Example response (all methods)

```
{
  "data": {
    "created_at": "2020-09-14T17:03:32.965812",
    "id": "12ade33a-21c0-473b-b055-b3c836e1c292",
    "phone_number": "+13035551234",
    "record_type": "verification",
    "status": "pending",
    "timeout_secs": 300,
    "verify_profile_id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
    "type": "sms",
    "updated_at": "2020-09-14T17:03:32.965812"
  }
}
```

## Verify a 2FA code

The user provides the code they received (via SMS or call). Submit it to Telnyx to verify it matches:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"code":"17686", "verify_profile_id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
  https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify
```

Example response:

```
{
  "data": {
    "phone_number": "+13035551234",
    "response_code": "accepted"
  }
}
```

A `response_code` of `"accepted"` confirms the code matches. Other possible values:

| Response Code | Meaning |
| --- | --- |
| `accepted` | Code is correct — verification successful |
| `rejected` | Code is incorrect |
| `expired` | Verification timed out (exceeded `timeout_secs`) |
| `max_attempts_exceeded` | Too many incorrect attempts |
