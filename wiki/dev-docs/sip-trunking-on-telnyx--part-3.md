---
title: SIP Trunking on Telnyx
summary: Telnyx Elastic SIP Trunking provides elastic, programmable telephony over
  IP with multiple authentication methods, configurable outbound policies, call-quality
  features, and emergency calling support. This page consolidates the authentication
  options, configuration guides, caller ID and concurrency policies, advanced features,
  and emergency calling capabilities available on Telnyx SIP trunks.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
updated_at: 2026-08-05T14:05:52Z
---

# SIP Trunking on Telnyx

*Part 3 of 5 — see also: [Part 1](sip-trunking-on-telnyx--part-1.md), [Part 2](sip-trunking-on-telnyx--part-2.md), [Part 4](sip-trunking-on-telnyx--part-4.md), [Part 5](sip-trunking-on-telnyx--part-5.md)*

Telnyx Elastic SIP Trunking provides elastic, programmable telephony over IP with multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling support. This page consolidates the authentication options, configuration guides, caller ID and concurrency policies, advanced features, and emergency calling capabilities available on Telnyx SIP trunks.

## External Call Transfers

External transfers move an inbound PSTN call to an external destination while preserving the original caller's identity.

### Call flow

1. Caller A dials Telnyx number B.
2. Telnyx routes the call to the SIP endpoint (A → B).
3. The endpoint initiates a transfer to external number C.
4. Telnyx places a new outbound call (A → C).

### Validation requirements

Telnyx validates external transfers to prevent unauthorized call spoofing:

- **Active call verification**: An active inbound call must exist from the original caller to the Telnyx number.
- **Diversion header**: The outbound call leg must include a SIP `Diversion` header containing the Telnyx number.

Required Diversion header format:

```
Diversion: <sip:+12125551234@sip.telnyx.com>
```

Transfers are rejected when no active call can be matched, the Diversion header is missing, or the header contains an unauthorized number.

### Transfer types

**Blind transfer** — Immediate transfer without announcement:

```
REFER sip:+13035559876@sip.telnyx.com SIP/2.0
Refer-To: <sip:+13035559876@sip.telnyx.com>
```

**Attended transfer** — Place the original call on hold, dial the transfer destination, announce the transfer, and complete with SIP REFER.

### Programmable Voice implementation

**Transfer command** — `POST /v2/calls/{id}/actions/transfer`:

```
{
  "to": "+13035559876",
  "from": "+12125551234"
}
```

**Dial with bridge** — `POST /v2/calls` with `link_to` and `bridge_intent`:

```
{
  "connection_id": "1234567890",
  "to": "+13035559876",
  "from": "+12125551234",
  "link_to": "v3:abc123def456",
  "bridge_intent": true
}
```

**TeXML Dial** — `<Dial>` verb:

```
<Response>
  <Dial callerId="+12125551234">
    <Number>+13035559876</Number>
  </Dial>
</Response>
```

### Troubleshooting

If transfers fail, verify:

1. An active inbound call exists on the Telnyx number.
2. The Diversion header includes the correct Telnyx number.
3. The outbound voice profile allows calls to the destination.
4. The destination number is in E.164 format.

## Adaptive Jitter Buffer

Jitter buffering smooths out packet arrival variation on SIP connections to reduce audio artifacts such as choppy or distorted speech. Enable this feature at the connection level to improve call quality on networks with inconsistent latency.

### How it works

An adaptive jitter buffer temporarily holds incoming voice packets before playing them out, compensating for uneven packet arrival times (jitter). The buffer dynamically adjusts its size between configurable minimum and maximum values based on observed network conditions — expanding when jitter increases and shrinking when the network stabilizes.

### Configuration settings

| Setting | Purpose | Default | Range |
| --- | --- | --- | --- |
| `enable_jitter_buffer` | Toggle jitter buffering on/off | `false` | — |
| `jitterbuffer_msec_min` | Minimum buffer size (ms) | `60` | 40–400 |
| `jitterbuffer_msec_max` | Maximum buffer size (ms) | `200` | 40–400 |

`jitterbuffer_msec_min` cannot exceed `jitterbuffer_msec_max`. The API will reject requests where the minimum is greater than the maximum.

### Configuration via API

Jitter buffer can be configured on credential, FQDN, and IP connections via the corresponding `PATCH` endpoints:

```
{
  "jitter_buffer": {
    "enable_jitter_buffer": true,
    "jitterbuffer_msec_min": 60,
    "jitterbuffer_msec_max": 200
  }
}
```

### Tuning guidance

- **Higher values** increase latency tolerance and work better for high-jitter networks (e.g., international routes or mobile carriers).
- **Lower values** reduce latency and are suited for stable, low-jitter networks (e.g., dedicated fiber or local connections).
- **Default values** (`60`–`200` ms) work well for most deployments and are a good starting point.

Jitter buffer configuration is currently available via API only. Portal UI support is coming soon.

### Best practices

1. Start with defaults before tuning — the default range of 60–200 ms handles most network conditions.
2. Monitor call quality metrics after enabling to validate the impact on your specific traffic.
3. Increase the maximum for routes with known high jitter rather than raising the minimum, which adds baseline latency to all calls.
4. Enable on specific connections rather than globally if only certain routes experience jitter issues.
5. Test during peak hours when network congestion and jitter are most likely to occur.
