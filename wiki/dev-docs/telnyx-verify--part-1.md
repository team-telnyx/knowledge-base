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

*Part 1 of 6 — see also: [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md), [Part 5](telnyx-verify--part-5.md), [Part 6](telnyx-verify--part-6.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Overview

The Telnyx Verify API enables you to implement robust two-factor authentication (2FA) and phone-number verification using carrier-grade voice and messaging. The service supports multiple verification channels — SMS, voice call, flashcall, and DTMF confirmation — and is backed by a profile-based configuration model, customizable message templates, real-time webhooks, and a set of security and fraud-prevention primitives.

This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference.

## Verification methods

Telnyx Verify supports four verification methods. Each can be configured on a [Verify Profile](verify-profile.md) and combined for fallback strategies.

- **`sms`** — The verification code is sent in a custom or default templated message. Widest global coverage, 1–5 second delivery.
- **`call`** — The code is spoken aloud in a custom or default templated message when the user answers. Useful for landlines, VoIP, and regions with unreliable SMS. 10–20 second delivery.
- **`flashcall`** — The verification code is embedded in the caller ID of a brief "flash" call (the call rings once and hangs up). The user's app extracts the code automatically. 2–5 second delivery, mobile-only.
- **`dtmf_confirm`** — Telnyx calls the number, plays a TTS prompt, and collects a single keypress (`1`) to confirm ownership. No verification code is generated — the keypress is the confirmation. Works on landlines and is unique to Telnyx (Twilio and Vonage Verify APIs only support code-based voice verification).

### Choosing the right method

| Feature | SMS | Call | Flashcall | DTMF Confirm |
| --- | --- | --- | --- | --- |
| User action | Type code | Listen + type code | None | Press 1 |
| Code generated | Yes | Yes | Yes (caller ID) | No |
| Verify endpoint | Required | Required | Required | Not needed |
| Landline support | No | Yes | No | Yes |
| Fraud risk | SIM swap, interception | Low | Low | Low |
| Competitor support | Twilio, Vonage | Twilio, Vonage | Twilio | Telnyx only |

**Fallback strategy:** Configure multiple methods on the same profile. Start with SMS (fastest and widest coverage), fall back to call if SMS fails. For mobile apps, consider flashcall as a zero-friction primary method with SMS as fallback.

## Prerequisites

1. **Create a Telnyx account** at [telnyx.com](https://telnyx.com/sign-up).
2. **Get your API key** following the [API Keys guide](https://developers.telnyx.com/development/api-fundamentals/create-api-keys). Set it as an environment variable:
   - macOS/Linux: `export TELNYX_API_KEY="YOUR_API_KEY"`
   - Windows: `$env:TELNYX_API_KEY = "YOUR_API_KEY"`
3. **Install an SDK** (optional):
   - Node.js: `npm install telnyx`
   - Python: `pip install telnyx`
   - Ruby: `gem install telnyx`
   - Go: `go get github.com/team-telnyx/telnyx-go`
   - PHP: `composer require telnyx/telnyx-php`

## Verify profiles

A Verify Profile contains the configurations used when sending 2FA messages and receiving responses. Each profile can have one of each verification method configured. It is recommended that you use a different profile for each application.

### Select a message template

List available templates:

```
curl --location --request GET 'https://api.telnyx.com/v2/verify_profiles/templates' \
--header 'Authorization: Bearer YOUR_API_KEY'
```

Example response:

```
{
    "data": [
        {
            "id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            "text": "Your {{app_name}} verification code is: {{code}}."
        },
        {
            "id": "2ca3f1da-5621-4aa6-ae56-df21caff79e0",
            "text": "{{code}} is your verification code for {{app_name}}."
        },
        {
            "id": "33dfb056-6c1b-40bd-920e-4243e01248a5",
            "text": "Your {{app_name}} verification code is: {{code}}. Do not share this code with anyone; our employees will never ask for the code."
        },
        {
            "id": "46acd63c-be57-4993-ae8d-0e4067ad1d57",
            "text": "Your {{app_name}} verification code is: {{code}}. This code will expire in {{default_verification_timeout_secs}} minutes."
        },
        {
            "id": "723ead5e-ada6-4c29-a962-349170866187",
            "text": "{{code}} is your verification code for {{app_name}}. This code will expire in {{default_verification_timeout_secs}} minutes."
        },
        {
            "id": "88d0781f-f4c7-4b78-8d0a-1f3e4de78b5e",
            "text": "Your {{app_name}} verification code is: {{code}}. This code will expire in {{default_verification_timeout_secs}} minutes. Do not share this code with anyone; our employees will never ask for the code."
        }
    ]
}
```

If no template is selected, the default is "Your verification code is `{code}`." You can also [create custom templates](custom-templates-for-telnyx-verify.md) that match your brand voice and compliance requirements.

### Create a verify profile

```
curl --location --request POST 'https://api.telnyx.com/v2/verify_profiles' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data-raw '{
    "name": "foobar-en-v1",
    "language": "en-US",
    "sms": {
        "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
        "whitelisted_destinations": ["US", "CA"],
        "default_timeout_secs": 300,
        "code_length": 5
    },
    "call": {
        "default_timeout_secs": 600
    }
}'
```

Example response:

```
{
    "data": {
        "id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
        "name": "foobar-en-v1",
        "created_at": "2024-03-27T11:45:41.292913",
        "updated_at": "2024-03-27T11:45:41.292913",
        "record_type": "verify_profile",
        "sms": {
            "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            "whitelisted_destinations": ["US", "CA"],
            "default_timeout_secs": 300,
            "code_length": 5
        },
        "call": {
            "default_timeout_secs": 600
        },
        "language": "en-US"
    }
}
```

Take note of the profile's `id` — you will need it to send 2FA verifications. You can list all of your Verify Profiles via the [List Verify Profiles API](https://developers.telnyx.com/api-reference/verify/list-all-verify-profiles).

### Create a DTMF confirm profile

For DTMF confirmation, create a profile with `dtmf_confirm` settings. This can be combined with other verification types (SMS, call) on the same profile.

```
curl -X POST https://api.telnyx.com/v2/verify_profiles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "name": "caller-id-verification",
    "language": "en-US",
    "dtmf_confirm": {
      "default_timeout_secs": 300
    }
  }'
```

The returned `id` is required for verification requests.
