---
title: SIP Trunking
summary: Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections
  for inbound traffic and Outbound Voice Profiles for outbound routing, with features
  including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external
  transfers, and configurable routing with automatic failover.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
  content_hash: 9eb2fe48821c830f63dc0734e6dbff398b9e3b2c6731b4be16518a995f4f2c86
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
  content_hash: 0df4ac40477704bce1951ffc0f6e9d0c0d66aeb9c171cd84ac57c46bb135884a
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
  content_hash: 6257d47fdb7d705d255a04e111bf905548a6267d09c97ee632e2e6935214d3b6
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
  content_hash: a68ac69255fe564f1859d60c1b1faae826cddd7258272e05dee44613e4f20211
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
  content_hash: 4b45b1fc043fd33dfdf03cce835b7baacf03eacde4773fb2911b200cf83dc279
- url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started/index
  content_hash: 4088d75674f02be51edf153962b16262017f2e333cb110181e0ff86c3fa64857
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
  content_hash: af1ad38a4f37fe678151703eed982474b72377cb42bc0851d12e13a28fec9808
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
  content_hash: 437b009489004c4a93669078625c47e7d7bcff98de193c17eade613518f39a2b
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records
  content_hash: fa13c88b62b3e2e2e4ea41e0ae9b87c7d1ef053f68c8969198d5158899f9c719
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
  content_hash: fb027e19c90bf1c08f40c7a9bf90edadf6b38a675bcc62fd545d1681f5a2ff4f
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration
  content_hash: 56311f97b6b250e4af9cb9c61d0c4cad3664d4d2536eb8d4773e7d5acae7af0a
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/failover-and-retries/index
  content_hash: 798b0177d01a4da0305500160f2b542ced47f42330fdecd80713841c935929f2
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
  content_hash: 7ee446688bf3dabf8fd77e17a3e53e01add3339fc55500dfcd4566daa0b57451
- url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
  content_hash: 7ae6b902ba3f38003afa9e50e689249f0393051475ceb27265b0099ef39da6b3
updated_at: 2026-06-11T10:45:55Z
---

# SIP Trunking

*Part 2 of 3 — see also: [Part 1](sip-trunking--part-1.md), [Part 3](sip-trunking--part-3.md)*

Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections for inbound traffic and Outbound Voice Profiles for outbound routing, with features including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external transfers, and configurable routing with automatic failover.

## Features

### Jitter Buffer

Jitter buffering smooths out packet arrival variation on SIP connections to reduce audio artifacts such as choppy or distorted speech. An adaptive jitter buffer temporarily holds incoming voice packets and dynamically adjusts its size between configurable minimum and maximum values based on observed network conditions.

| Setting | Purpose | Default | Range |
| --- | --- | --- | --- |
| `enable_jitter_buffer` | Toggle on/off | `false` | — |
| `jitterbuffer_msec_min` | Minimum buffer size (ms) | `60` | 40–400 |
| `jitterbuffer_msec_max` | Maximum buffer size (ms) | `200` | 40–400 |

`jitterbuffer_msec_min` cannot exceed `jitterbuffer_msec_max`. Configure via `PATCH` on credential, FQDN, or IP connections:

```json
{
  "jitter_buffer": {
    "enable_jitter_buffer": true,
    "jitterbuffer_msec_min": 60,
    "jitterbuffer_msec_max": 200
  }
}
```

**Tuning guidance:** Higher values increase latency tolerance (better for high-jitter networks like international routes); lower values reduce latency (better for stable networks). Increase the maximum for routes with known high jitter rather than raising the minimum, which adds baseline latency to all calls. Start with defaults (60–200 ms) before tuning.

### Noise Suppression

Noise suppression removes background noise from audio streams. It can be configured at the **connection level** (applied to all phone numbers on the connection; overrides number-level settings) or the **number level** (applied to specific numbers for granular control). Connection-level settings take precedence.

**Supported engines:**

| Engine | Value | Best for |
| --- | --- | --- |
| Denoiser | `Denoiser` | Default option for most calls |
| DeepFilterNet | `DeepFilterNet` | Telephony and WebRTC (full-band 48 kHz) |
| Krisp Viva Tel Lite | `Krisp Viva Tel Lite` | Telephony up to 16 kHz; isolates primary speaker |
| Krisp Viva Pro | `Krisp Viva Pro` | Close-microphone WebRTC calls |
| Krisp Viva SS | `Krisp Viva SS` | Smart speakers and far-field microphones |
| AI-coustics Quail | `AI-coustics Quail` | STT-optimized; up to 43% WER reduction |

For SIP trunking, **Denoiser** and **Krisp Viva Tel Lite** are the most common choices.

**Direction options:**

| Value | Description |
| --- | --- |
| `inbound` | Processes audio from PSTN to your system |
| `outbound` | Processes audio from your system to PSTN |
| `both` | Processes audio in both directions |
| `disabled` | Turns off noise suppression |

Each direction is processed and billed independently. Processing adds minimal latency (typically < 20 ms). Noise suppression works with G.711, G.722, and Opus codecs.

Configure at connection level via `PATCH /v2/ip_connections/` or at number level via `PATCH /v2/phone_numbers/<id>/voice`:

```json
{
  "noise_suppression": {
    "direction": "both",
    "noise_suppression_engine": "Denoiser"
  }
}
```

### External Call Transfers

External transfers move an inbound PSTN call to an external destination while preserving the original caller's identity. Telnyx validates transfers to prevent unauthorized call spoofing:

- An active inbound call must exist from the original caller to the Telnyx number
- The outbound call leg must include a SIP `Diversion` header containing the Telnyx number: `Diversion: <sip:+12125551234@sip.telnyx.com>`

Transfers are rejected when no active call can be matched, the Diversion header is missing, or the header contains an unauthorized number.

**Blind transfer** (immediate, no announcement):

```
REFER sip:+13035559876@sip.telnyx.com SIP/2.0
Refer-To: <sip:+13035559876@sip.telnyx.com>
```

**Attended transfer:** Place original call on hold, dial the transfer destination, announce, then complete with SIP REFER.

**Programmable Voice implementations:**

- Transfer command: `POST /v2/calls/<id>/actions/transfer` with `to` and `from` fields
- Dial with bridge: `POST /v2/calls` with `link_to` and `bridge_intent`
- TeXML: Use the `<Dial>` verb with `callerId`

### SIP URI Calling

SIP URI calling enables inbound calls to a SIP username (e.g., `support@sip.telnyx.com`), eliminating the need for a traditional phone number. This feature is disabled by default and must be explicitly enabled.

**Username requirements:** Must begin with a non-numeric character (prevents number spoofing). Valid: `support@`, `pbx-main@`, `alice123@`. Invalid: `123456@`.

**Access control modes:**

| Mode | Value | Description |
| --- | --- | --- |
| Disabled | `disabled` | Blocks all SIP URI calls (default) |
| Unrestricted | `unrestricted` | Allows calls from anyone on the internet |
| Internal | `internal` | Allows calls only from SIP connections within the same Telnyx account |

Configure via `PATCH /v2/ip_connections/` with `sip_uri_calling_preference`.

**Billing:** Calls from Telnyx SIP connections use standard rate deck pricing. Calls from external or unidentifiable sources (when set to `unrestricted`) are billed at **$0.002/minute** to the connection owner.
