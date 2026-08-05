---
title: Telnyx Verify
summary: The Telnyx Verify API delivers carrier-grade two-factor authentication over
  SMS, voice, flash call, and DTMF confirmation. This page covers the verification
  methods, how to create verify profiles, send and verify codes, build branded custom
  templates, and handle results via webhooks.
sources:
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
updated_at: 2026-08-05T13:43:44Z
---

# Telnyx Verify

*Part 2 of 4 — see also: [Part 1](telnyx-verify--part-1.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md)*

The Telnyx Verify API delivers carrier-grade two-factor authentication over SMS, voice, flash call, and DTMF confirmation. This page covers the verification methods, how to create verify profiles, send and verify codes, build branded custom templates, and handle results via webhooks.

## Trigger a verification request

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

Profile configuration for call — include the `call` configuration when creating your verify profile:

```
curl --location --request POST 'https://api.telnyx.com/v2/verify_profiles' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data-raw '{
    "name": "my-app-call-verify",
    "language": "en-US",
    "call": {
        "default_timeout_secs": 600
    }
}'
```

Initiate a call verification:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"phone_number":"+13035551234","verify_profile_id":"4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
  https://api.telnyx.com/v2/verifications/call
```

**User experience:** The user receives a phone call. An automated voice reads the verification code aloud (e.g., "Your verification code is 1-7-6-8-6"). The code is repeated twice. The user then enters the code in your application.

**DTMF confirmation:** You can optionally enable DTMF confirmation, where the user enters the code on their phone keypad during the call instead of typing it in your app. See the [DTMF Confirmation guide](dtmf-confirmation-verification.md) for details.

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

Telnyx Verify supports webhooks to receive instant notifications when users complete verification, eliminating the need for polling. See [Receiving Webhooks](receiving-webhooks.md) for details.
