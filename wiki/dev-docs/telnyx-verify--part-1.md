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

*Part 1 of 4 — see also: [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md)*

The Telnyx Verify API delivers carrier-grade two-factor authentication over SMS, voice, flash call, and DTMF confirmation. This page covers the verification methods, how to create verify profiles, send and verify codes, build branded custom templates, and handle results via webhooks.

## Overview

The Telnyx Verify API enables you to implement robust security features using carrier-grade voice and messaging to keep your customers safe. It supports multiple verification methods, configurable verify profiles, branded custom templates, and webhook-based result delivery.

## Verification methods

Telnyx Verify supports four verification methods. Each can be configured on a verify profile, and a single profile can combine multiple methods to enable fallback strategies.

- **`sms`** — The verification code is sent in a custom or default templated message.
- **`call`** — The code is spoken aloud in a custom or default templated message when the user answers the call.
- **`flashcall`** — The verification code is embedded in the caller ID of a brief "flash" call (the call rings once and hangs up). The user's app extracts the code automatically.
- **`dtmf_confirm`** — A phone call plays a TTS prompt and collects a single keypress (`1`) to confirm ownership. No verification code is generated — the keypress is the confirmation.

### Choosing the right method

| Feature | SMS | Call | Flashcall |
| --- | --- | --- | --- |
| **Delivery speed** | 1–5 seconds | 10–20 seconds (ring + answer) | 2–5 seconds |
| **User interaction** | Read code, type it in | Listen to code, type it in | Automatic (app reads caller ID) |
| **Works on web** | ✅ Yes | ✅ Yes | ❌ No (mobile only) |
| **Works on landlines** | ❌ No | ✅ Yes | ❌ No |
| **Cost** | Per-message rate | Per-minute rate | Per-call rate (very short) |
| **Global coverage** | Widest | Wide | Limited |
| **Accessibility** | Good | Best (audio) | App-dependent |
| **Best for** | General purpose | Landlines, accessibility | Mobile apps with auto-read |

**Fallback strategy:** Configure multiple methods in your verify profile. Start with SMS (fastest and widest coverage), fall back to call if SMS fails. For mobile apps, consider flashcall as a zero-friction primary method with SMS as fallback.

## Prerequisites

1. Create a Telnyx account at [telnyx.com](https://telnyx.com/sign-up).
2. Generate an API key and set it as an environment variable:

   macOS/Linux:
   ```
   export TELNYX_API_KEY="YOUR_API_KEY"
   ```

   Windows:
   ```
   $env:TELNYX_API_KEY = "YOUR_API_KEY"
   ```

3. Optionally install an SDK:

   - Node.js: `npm install telnyx`
   - Python: `pip install telnyx`
   - Ruby: `gem install telnyx`
   - Go: `go get github.com/team-telnyx/telnyx-go`
   - PHP: `composer require telnyx/telnyx-php`

   Java and .NET examples use the standard HTTP client libraries included with the platform.

## Create a verify profile

A Verify Profile contains the configurations used when sending 2FA messages and receiving responses. Each profile can have one of each verification method configured. It is recommended that you use a different profile for each application.

### Select a message template

List the available templates:

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

If no template is selected, the default is "Your verification code is `{code}`." You can also [create custom templates](custom-templates.md) that match your brand voice and compliance requirements.

### Create the profile

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

Take note of the profile's `id` — you will need it to send 2FA verifications. You can list all of your verify profiles at any time via the API.
