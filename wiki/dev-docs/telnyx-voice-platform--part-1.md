---
title: Telnyx Voice Platform
summary: 'Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication
  (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text
  transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine
  model selection, and provider migration).'
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
  content_hash: e71721006805ece97317b6a2ce287bded0ee694d74cd96070f8efb6ec4546534
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
  content_hash: 8a1cedc407a7eeed8a1f689a60c15c545dc6394a4ce0d4d664a31846b54b856b
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
  content_hash: ddcbe69b5d283081160304794571d8ad56e52cca94e1f55ac224d31fe3f9ac5f
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
  content_hash: a17bf544d2f5411cb7a1e10bd8204fae4fb499a8debccef66cb9d596da2c280c
- url: https://developers.telnyx.com/docs/voice/stt/migration
  content_hash: 8273de02389d2c31f810a359f89523eeb2a64aa43286be196c610a805e479cdc
- url: https://developers.telnyx.com/docs/voice/stt/models
  content_hash: 637078dde1176884102bdc0e61dcc482b32bdee3552c24cbf5158b865a6a1426
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
  content_hash: 3cd2887c1a24d01ca417a1e3a2f2e7e7db6cd92449fb5a77027b8cadb348015f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
  content_hash: 277f6f5e42acfabb557c1b22f1293ce8235db0e343e8af493560f9071b12fa36
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
  content_hash: c75d57b2ceae2c7f6f780f4385e6a545f6dcc11d41a7cca25441d1add888572f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
  content_hash: 3856e7e0bf451af19678e8ba5f19deb2fffe5ebab69aa15c93f0ee331521f964
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
  content_hash: afd719ffe51051e3855f74439d0eba8bde4e617f527163f25e99321d501562d6
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
  content_hash: 262aa6764992fbe5d612843b7bfe1044f0ddfb4a118cb7cb7038d64fb2ae28aa
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
  content_hash: 56bd4f643fc6734d46569c545513342da1a4a2e611b863a525edb13ea879d8dc
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
  content_hash: d6959b095ff36f9266a76bb3ba3f39c0cd75fd2f49e2b4bb7e1d3a7b480f23d6
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
