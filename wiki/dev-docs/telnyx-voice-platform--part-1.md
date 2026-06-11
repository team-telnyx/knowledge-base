---
title: Telnyx Voice Platform
summary: 'Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication
  (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text
  transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine
  model selection, and provider migration).'
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
updated_at: 2026-06-11T10:47:02Z
---

# Telnyx Voice Platform

*Part 1 of 4 — see also: [Part 2](telnyx-voice-platform--part-2.md), [Part 3](telnyx-voice-platform--part-3.md), [Part 4](telnyx-voice-platform--part-4.md)*

Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine model selection, and provider migration).

## STIR/SHAKEN Attestation Behavior

Telnyx assigns STIR/SHAKEN attestation levels on outbound calls based on phone number ownership:

- **Attestation A** — call originates from a phone number owned by the account
- **Attestation B** — call originates from a non-owned or verified number

### Certificate Selection

The signing certificate is chosen by origin and destination:

| Origin | Destination | Certificate |
|---|---|---|
| US number | Any | US |
| Canadian number | Canadian number | Canadian |
| Canadian number | US number | US |

### Call Forwarding

When call forwarding is enabled on a Telnyx number, the original STIR/SHAKEN passport is preserved or passed through. A DIV (diversion) passport is added for the forwarded leg with **Attestation A**.

| Route | Certificate |
|---|---|
| US → US | US |
| Canada → Canada | Canadian |
| US ↔ Canada (cross-border) | US |

### Call Transfers

| Method | Origination Number | Attestation | Original Passport |
|---|---|---|---|
| SIP REFER | Original caller | B | Not preserved |
| Call Control API (transfer) | Specified in request | A or B* | Not preserved |
| Call Control API (dial/bridge) | Specified in request | A or B* | Not preserved |
| TeXML `<Dial>` | Specified in request | A or B* | Not preserved |

\*A if the "from" number is owned, B otherwise.

## Hosted STIR/SHAKEN Certificate

Use a self-hosted STIR/SHAKEN certificate to sign outbound calls.

### Requirements

- STIR/SHAKEN certificate from an authorized STI-CA
- Certificate hosted at a public HTTPS URL (`x5u`)
- Unencrypted PEM-format private key (EC-P256 or RSA-2048)
- Outbound voice profile
- US phone number (for validation)

### Upload Certificate

`POST /v2/stir_shaken_certs`

```json
{
  "x5u_url": "https://certificates.transnexus.com/xxx/xxxx.pem",
  "private_key": "-----BEGIN EC PRIVATE KEY-----[KEY]-----END EC PRIVATE KEY-----"
}
```

| Parameter | Description |
|---|---|
| `x5u_url` | Public URL to X.509 certificate (hosted by STI-CA or self-hosted) |
| `private_key` | PEM-formatted EC-P256 or RSA-2048 private key (no `\n` characters) |

### Associate with Outbound Voice Profile

`PATCH /v2/outbound_voice_profiles/{id}`

```json
{
  "stir_shaken_cert_id": "e25c6e2e-4f77-42fb-b8d3-e5d8d0c7d019"
}
```

### Verify Signing

1. Create an IP connection with "Receive SHAKEN/STIR Identity SIP header" enabled
2. Assign a US phone number to this connection
3. Place a call from a connection using the configured outbound voice profile
4. Check the inbound INVITE for the `Identity` header:

```
Identity:[JWT];info=<https://[CERT_URL]>;alg=ES256;ppt="shaken"
```

### Cost

$100 per certificate per month. Billing is per unique `x5u_url`, not per account. A 7-day grace period applies from upload before billing begins. Deleting the certificate cancels recurring charges.

## STIR/SHAKEN SIP Header Parameters

Telnyx provides call attestation information through the `verstat` parameter in the `P-Asserted-Identity` SIP header:

```
P-Asserted-Identity: "John Doe" <sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

| Value | Description |
|---|---|
| `TN-Validation-Passed` | Verification succeeded, A-level attestation |
| `TN-Validation-Passed-B` | Verification succeeded, B-level attestation |
| `TN-Validation-Passed-C` | Verification succeeded, C-level attestation |
| `TN-Validation-Failed` | Verification failed (invalid certificate) |
| `No-TN-Validation` | No Identity header provided |

The `verstat` parameter is included for inbound calls from the PSTN and on-net calls between Telnyx customers.

## Speech-to-Text Overview

Telnyx STT transcribes audio to text in three ways:

- **WebSocket Streaming** — stream audio over a persistent WebSocket connection with real-time partial and final transcripts
- **File-Based Transcription (REST API)** — upload audio files via a synchronous REST endpoint that is OpenAI SDK compatible
- **In-Call Transcription** — enable transcription during live voice calls via Call Control (`transcription_start`/`transcription_stop`) or TeXML

The audio codec for in-call transcription is managed by the Telnyx platform — no format configuration needed. Engine selection (Telnyx, Google, Deepgram, Azure, xAI, AssemblyAI, Speechmatics, Soniox) is specified as a parameter on the transcription command.
