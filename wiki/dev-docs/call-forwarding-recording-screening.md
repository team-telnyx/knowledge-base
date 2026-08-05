---
title: Call Forwarding, Recording & Screening
summary: Configure call forwarding, recording, inbound call screening, and noise suppression
  on Telnyx mobile phone numbers via the `PATCH /mobile_phone_numbers/{id}` endpoint.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
updated_at: 2026-08-05T13:46:40Z
---

# Call Forwarding, Recording & Screening

Configure call forwarding, recording, inbound call screening, and noise suppression on Telnyx mobile phone numbers via the `PATCH /mobile_phone_numbers/{id}` endpoint.

All settings below are configured via `PATCH /mobile_phone_numbers/{id}`.

## Call Forwarding

Set the `call_forwarding` object to route calls when the device is unavailable.

| Type | Behavior |
| --- | --- |
| `unconditional` | All calls forward immediately — device never rings |
| `no_answer` | Forward after timeout (device rings first) |
| `busy` | Forward when line is in use |

Forward to any number — landline, mobile, SIP connection, or Call Control application.

## Call Recording

Set `call_recording` to record inbound, outbound, or both. Recordings are accessible through the standard Telnyx Recordings API — same storage, retrieval, and webhooks as Call Control recordings.

## Inbound Call Screening

Inbound Call Screening automatically blocks or flags inbound calls based on caller reputation and SHAKEN/STIR attestation. The feature is free on any number.

### How it works

Screening evaluates three factors:

| Factor | Description |
| --- | --- |
| **Number Reputation** | Cross-references caller identity against CallerAPI, Nomorobo, and YouMail databases |
| **Number Validation** | Checks whether the originating number is valid and exists |
| **SHAKEN/STIR Attestation** | Validates Caller ID authenticity — screens calls with Attestation C (unauthenticated) or Invalid (certificate error) |

### Handling modes

| Mode | Behavior |
| --- | --- |
| **Flag** | Call connects but displays “SPAM LIKELY” in the From and P-Asserted-ID headers. A custom SIP header carries the screening status for your routing logic. |
| **Reject** | Call is blocked at the network level and never reaches your infrastructure. |

### Enabling call screening

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Go to **My Numbers**, select a number, and click **Edit**.
3. Under the **Voice** tab, enable **Inbound Call Screening** and choose Flag or Reject.

You can also enable it via `PATCH /mobile_phone_numbers/{id}` by setting the `inbound_call_screening` field.

### Webhook integration

Enable webhooks to receive the `call_screening_result` field in the `call.initiated` webhook payload.

Number reputation screening applies to US and Canada calls. SHAKEN/STIR screening applies to North America.

## Other Settings

| Setting | Description |
| --- | --- |
| `noise_suppression` | AI noise reduction for loud environments |

## Example

```json
{
  "call_forwarding": {
    "forwarding_type": "no_answer",
    "forwarding_number": "+15551234567",
    "timeout_secs": 30
  },
  "call_recording": {
    "inbound": "enabled",
    "outbound": "disabled"
  },
  "noise_suppression": "enabled"
}
```
