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

*Part 3 of 4 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 4](telnyx-verify--part-4.md)*

The Telnyx Verify API delivers carrier-grade two-factor authentication over SMS, voice, flash call, and DTMF confirmation. This page covers the verification methods, how to create verify profiles, send and verify codes, build branded custom templates, and handle results via webhooks.

## DTMF confirmation

DTMF confirmation calls a phone number, plays a TTS prompt, and collects a single keypress (`1`) to confirm ownership. No verification code is generated — the keypress is the confirmation. The `POST /verifications/{id}/actions/verify` endpoint is **not used**. Verification completes on the call itself.

DTMF confirmation is unique to Telnyx — Twilio and Vonage Verify APIs only support code-based voice verification (read a code, then type it). Single-keypress confirmation reduces user friction and works on landlines.

### Flow

| Outcome | Trigger | Status |
| --- | --- | --- |
| Confirmed | Digit `1` pressed | `accepted` |
| Rejected | Wrong digit | `invalid` |
| Timed out | No keypress (10s) | `expired` |
| Failed | Call not answered | `error` |

Up to 3 attempts per call. After 3 wrong digits, the call ends with status `invalid`.

### Use cases

- **Caller ID verification** — Confirm ownership before allowing a number as outbound Caller ID.
- **Landline verification** — Verify numbers that cannot receive SMS.
- **Accessibility** — Single keypress instead of reading and typing a code.
- **Account recovery** — Confirm phone ownership without code entry.

### Create a verify profile with DTMF

Create a profile with `dtmf_confirm` settings. This can be combined with other verification types (SMS, call) on the same profile.

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

### Trigger DTMF verification

```
curl -X POST https://api.telnyx.com/v2/verifications/dtmf_confirm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "phone_number": "+13035551234",
    "verify_profile_id": "YOUR_PROFILE_ID"
  }'
```

Response:

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

The TTS language is determined by the `language` field on the Verify Profile (default: `en-US`).

### Handle the DTMF result

Verification completes on the call — no verify endpoint call needed. Receive the outcome via webhooks.

Accepted (digit `1` pressed):

```
{
  "data": {
    "event_type": "verification.complete",
    "payload": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "phone_number": "+13035551234",
      "status": "accepted",
      "type": "dtmf_confirm",
      "verify_profile_id": "YOUR_PROFILE_ID"
    }
  }
}
```

Failed (wrong digit, timeout, or call failure):

```
{
  "data": {
    "event_type": "verification.complete",
    "payload": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "phone_number": "+13035551234",
      "status": "invalid",
      "type": "dtmf_confirm",
      "verify_profile_id": "YOUR_PROFILE_ID"
    }
  }
}
```

Polling alternative:

```
curl https://api.telnyx.com/v2/verifications/{verification_id} \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

### Verification type comparison

| Feature | SMS | Call | Flash Call | DTMF Confirm |
| --- | --- | --- | --- | --- |
| **User action** | Type code | Listen + type code | None | Press 1 |
| **Code generated** | Yes | Yes | Yes (caller ID) | No |
| **Verify endpoint** | Required | Required | Required | Not needed |
| **Landline support** | No | Yes | No | Yes |
| **Fraud risk** | SIM swap, interception | Low | Low | Low |
| **Competitor support** | Twilio, Vonage | Twilio, Vonage | Twilio | Telnyx only |

### DTMF troubleshooting

- **Call reaches voicemail** — Verification times out with status `expired`. Implement a retry with delay, or fall back to SMS.
- **Wrong digit pressed** — Up to 3 attempts per call. After 3 failures, status is `invalid`. Trigger a new verification to retry.
- **Stuck in pending** — Call was not answered and no webhook received. Verify the webhook URL is configured and reachable. Poll the status endpoint as fallback.
- **Custom TTS prompt** — The prompt is fixed to the standard verification message. Voice and language are determined by the Verify Profile's `language` setting. Custom prompt text is not yet supported.
- **Rate limits** — Standard Verify API rate limits apply. Avoid triggering multiple concurrent verifications for the same phone number — the previous call must complete or time out first.
