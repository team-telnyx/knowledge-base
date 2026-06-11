---
title: Telnyx Voice API and SIP Trunking
summary: Telnyx provides a programmable Voice API for building voice applications
  with call control, conferencing, queuing, recording, and AI assistants, alongside
  an Elastic SIP Trunking platform with multiple authentication methods and granular
  routing, billing, and caller-ID configuration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
  content_hash: c617d44bc1fc0bc1be420034d4c1026e2c4f016923402abe89323e8f32bf91bd
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
  content_hash: ee417d1dfad37fcabbddef493e31af88542396ebe9bf5cfc92fea896734c1897
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
  content_hash: f280e1e698c8ad5e911371a3763705c24114677c2673ef677da1efea29aa9599
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
  content_hash: fae3dff7c2e998a65ad96f2be354bc26131290574c75dd9b8842b68a44841d82
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
  content_hash: a7aeea9b623ecf466cf005fc50a4b40a95b3e46d8b2ae7c500f7722e5a422133
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
  content_hash: 8ececeb032a8db111dc3b865467daf51793acecaba883c00559689942a405181
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
  content_hash: 05ff85b435e52e5651b44bb9be18489035064b4a685dacc630f9d2f0eeb8bd36
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
  content_hash: c9f2f43c2f6aad3649093a10343fccaa428a924ff3ec9871617898b52c921fd7
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
  content_hash: f61162327ee18005b2dae39ab0ad69d3388b01111ddb4ab366b79c7d4fde68df
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
  content_hash: 9d8ef6e984f6b49793df067dd4084a5bf057cbb75167dccb01199ca89c1b19db
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
  content_hash: 7a13bae241d106ef73ffbde5086251cc04f9dda596ce328b38c3050af8cf1495
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
  content_hash: 47531bc230c40949771adb48c4692d4b606e397844d76ac707463b6a4f91b886
updated_at: 2026-06-11T10:44:15Z
---

# Telnyx Voice API and SIP Trunking

*Part 3 of 3 — see also: [Part 1](telnyx-voice-api-and-sip-trunking--part-1.md), [Part 2](telnyx-voice-api-and-sip-trunking--part-2.md)*

Telnyx provides a programmable Voice API for building voice applications with call control, conferencing, queuing, recording, and AI assistants, alongside an Elastic SIP Trunking platform with multiple authentication methods and granular routing, billing, and caller-ID configuration.

## SIP Trunk Configuration

### Caller ID Policy

Telnyx enforces strict caller ID validation. Invalid numbers are rejected with `403 Caller Origination Number is Invalid D35`.

**Number formats by localization:**

- **USA** — National (`3129457420`), 11-digit (`13129457420`), or E.164 (`+13129457420`).
- **International** — National, country-specific, or E.164 formats.
- **Cross-border calls** — Only E.164 format is accepted.

**SIP header priority** (checked in order): `P-Preferred-Identity` > `P-Asserted-Identity` > `Remote-Party-Id` > `FROM`.

**Caller ID anonymization:** Include `Privacy: id` header. A valid origination number must still be provided. Toll-free and emergency calls cannot be anonymized; recipients always see the actual caller ID.

**International spoofing:** Outbound calls to international destinations with spoofed caller IDs are rejected with `503`.

Set connection localization via the API (`PATCH /v2/credential_connections/`, `PATCH /v2/fqdn_connections/`, or `PATCH /v2/ip_connections/`) with `outbound.localization`.

### P-Charge-Info Header

The `P-Charge-Info` SIP header identifies the billing number for outbound calls. Requirements: valid DID in E.164 format, wrapped in SIP URI format, and associated with the connection. Use for CDR attribution, per-number billing, and carrier-side routing.

### Concurrent Call Limits

Concurrent call limits control the maximum simultaneous outbound calls across all outbound voice profiles.

| Verification Level | Concurrent Calls |
|---|---|
| Initial setup | 2 |
| Level 2 verification | 10 |
| Custom (contact support) | 10+ |

Exceeding the limit returns `403 User channel limit exceeded D1`. Implement exponential backoff for retries. Monitor usage via `GET /v2/calls` filtered to active calls, or track `call.initiated` and `call.hangup` webhooks. For limits over 10, contact [support@telnyx.com](mailto:support@telnyx.com).

### Outbound Voice Profiles

Outbound voice profiles control routing, billing, and rate limits for outbound SIP calls. Components include:

- **Profile ID** — unique identifier for API calls and billing reports
- **Tags** — custom labels for cost allocation
- **SIP Connections** — authorized connections for outbound calls
- **Service Plan** — allowed destinations and rate deck
- **Channel Limit** — maximum concurrent outbound channels

Telnyx supports 255 destinations across 10 regions; many require Level 2 verification. Billing options include rate deck selection, max destination rate (rejects calls above threshold), and daily spend limit (resets at 00:00:00 UTC). Call recording can be enabled with WAV or MP3 format, mono or stereo channels, and scoped to all calls or specific ANI numbers.

## Third-Party Configuration Guides

Telnyx provides configuration guides for connecting a wide range of SIP infrastructure to Elastic SIP Trunks. These cover IP-PBX systems, SBCs, IP phones, softphones, ATAs, and cloud platforms. Qualified vendors include 3CX, Asterisk, Avaya, Cisco (CUBE/CUCM/CME), FreePBX, FreeSWITCH, Grandstream, Microsoft Teams, Yealink, Yeastar, Zoiper, and many more. Guides are available in the [Telnyx Support Center](https://support.telnyx.com) and are intended as general guidelines rather than configuration templates. Telnyx does not provide direct support for third-party products.
