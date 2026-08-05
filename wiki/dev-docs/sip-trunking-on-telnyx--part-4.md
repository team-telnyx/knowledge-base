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

*Part 4 of 5 — see also: [Part 1](sip-trunking-on-telnyx--part-1.md), [Part 2](sip-trunking-on-telnyx--part-2.md), [Part 3](sip-trunking-on-telnyx--part-3.md), [Part 5](sip-trunking-on-telnyx--part-5.md)*

Telnyx Elastic SIP Trunking provides elastic, programmable telephony over IP with multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling support. This page consolidates the authentication options, configuration guides, caller ID and concurrency policies, advanced features, and emergency calling capabilities available on Telnyx SIP trunks.

## Noise Suppression

Noise suppression enhances call quality by removing background noise from audio streams. Configure this feature at the connection level or individual phone number level to reduce unwanted ambient sounds during calls.

### Configuration scope

Noise suppression can be configured at two levels:

- **Connection level**: Applied to all phone numbers associated with the SIP connection. This setting overrides individual number configurations.
- **Number level**: Applied to specific phone numbers for granular control.

Connection-level settings take precedence over number-level configurations, simplifying management and ensuring consistent audio quality across all calls.

### Configuration via API

**Configure at connection level** via `PATCH /v2/ip_connections/` with the `noise_suppression` object:

```
{
  "noise_suppression": {
    "direction": "both",
    "noise_suppression_engine": "Denoiser"
  }
}
```

**Configure at number level** via `PATCH /v2/phone_numbers/{id}/voice` with the `noise_suppression` object:

```
{
  "noise_suppression": {
    "direction": "inbound",
    "noise_suppression_engine": "Krisp Viva Tel Lite"
  }
}
```

### Supported engines

Use the `noise_suppression_engine` parameter to select an engine. If omitted, `Denoiser` is used.

| Engine | Value | Description | Best for |
| --- | --- | --- | --- |
| **Denoiser** | `Denoiser` | Built-in, general-purpose noise reduction | Default option for most calls |
| **DeepFilterNet** | `DeepFilterNet` | Open-source, full-band 48 kHz processing | Telephony and WebRTC |
| **Krisp Viva Tel Lite** | `Krisp Viva Tel Lite` | Telephony up to 16 kHz, isolates primary speaker | Telephony with speaker isolation |
| **Krisp Viva Pro** | `Krisp Viva Pro` | WebRTC 16–32 kHz, full voice isolation | Close-microphone WebRTC calls |
| **Krisp Viva SS** | `Krisp Viva SS` | WebRTC 16–32 kHz, far-field optimized | Smart speakers and far-field microphones |
| **AI-coustics Quail** | `AI-coustics Quail` | STT-optimized, up to 43% WER reduction | AI and speech recognition workloads |

For SIP trunking, **Denoiser** and **Krisp Viva Tel Lite** are the most common choices. Use `Krisp Viva Tel Lite` when you need to isolate the primary speaker from background voices.

### Direction options

The `direction` parameter controls which audio streams are processed:

| Value | Description | Use case |
| --- | --- | --- |
| `inbound` | Processes audio from the PSTN to your system | Clean up audio received by your users or applications |
| `outbound` | Processes audio from your system to the PSTN | Reduce background noise from your users or applications |
| `both` | Processes audio in both directions | Maximum call clarity when both sides may have background noise |
| `disabled` | Turns off noise suppression | Preserve natural ambient sounds when needed |

### Codec compatibility

Noise suppression works with standard SIP trunking codecs including G.711 (μ-law and A-law), G.722, and Opus.

### Performance considerations

- Each direction (inbound/outbound) is processed and billed independently.
- Processing adds minimal latency (typically < 20ms).
- Noise suppression is applied in real-time during the call.
- Connection-level configuration provides consistent behavior across all numbers.

### Best practices

1. Use connection-level configuration for consistent audio quality across all phone numbers.
2. Enable bidirectional suppression (`both`) for optimal results in noisy environments.
3. Test with your specific use case to balance noise reduction with audio naturalness.
4. Monitor call quality metrics to validate the impact on your application.

## SIP URI Calling

SIP URI calling enables inbound calls to a SIP username, eliminating the need for a traditional phone number. This feature allows direct communication using SIP addresses in the format `username@sip.telnyx.com`.

### Prerequisites

- Active SIP connection with credential authentication.
- SIP device or softphone registered with connection credentials.
- Feature enabled on the connection's inbound settings.

SIP URI calling is disabled by default and must be explicitly enabled for each connection.

### SIP URI format

Calls are placed to the SIP username using the standard SIP URI format:

```
username@sip.telnyx.com
```

Username requirements:

- Must begin with a non-numeric character.
- This restriction prevents number spoofing and unauthorized dialing.

Example valid usernames: `support@sip.telnyx.com`, `pbx-main@sip.telnyx.com`, `alice123@sip.telnyx.com`. Example invalid username: `123456@sip.telnyx.com` (starts with numeric character).

### Configuration

**Access control options** — Configure SIP URI calling access using one of three modes:

| Mode | Value | Description | Use case |
| --- | --- | --- | --- |
| Disabled | `disabled` | Blocks all SIP URI calls | Default security posture |
| Unrestricted | `unrestricted` | Allows calls from anyone on the internet | Public-facing services, customer support lines |
| Internal | `internal` | Allows calls only from SIP connections within the same Telnyx account | Private inter-office communication, internal extensions |

**Configure via API** — `PATCH /v2/ip_connections/` with the `sip_uri_calling_preference` parameter:

```
{
  "sip_uri_calling_preference": "unrestricted"
}
```

Set to `disabled`, `unrestricted`, or `internal` based on security requirements.

### Making SIP URI calls

**From Telnyx SIP connections** — Dial directly to the SIP URI from any registered SIP endpoint:

```
INVITE sip:username@sip.telnyx.com SIP/2.0
```

**From external systems** — When configured as `unrestricted`, external SIP systems can place calls:

```
INVITE sip:username@sip.telnyx.com SIP/2.0
From: <sip:caller@external-domain.com>
```

### Receiving SIP URI calls

Configure the SIP endpoint to accept incoming calls:

1. Register the SIP device using the connection credentials.
2. Enable SIP URI calling with the appropriate access control.
3. Configure the dial plan or routing rules to handle incoming calls.

The call will arrive with the From header containing the caller's SIP URI or phone number.

### Billing

**Identifiable sources** — Calls from Telnyx SIP connections use standard rate deck pricing based on the originating connection's pricing plan.

**Unidentifiable sources** — When SIP URI calling is set to `unrestricted`, calls from external or unidentifiable sources are billed at **$0.002/minute** to the connection owner. Monitor usage when enabling unrestricted access to prevent unexpected charges from public internet traffic.

### Security considerations

1. **Username validation**: Non-numeric username requirements prevent unauthorized number spoofing.
2. **Access control**: Use `internal` mode for private communications within the organization.
3. **Rate monitoring**: Track call volumes and sources when using `unrestricted` mode.
4. **Authentication**: Credential-based connections provide secure endpoint registration.

### Troubleshooting

If SIP URI calls fail, verify:

1. SIP URI calling is enabled on the connection.
2. Username begins with a non-numeric character.
3. Access control mode permits the calling source.
4. SIP endpoint is properly registered with valid credentials.
5. Firewall rules allow SIP traffic to/from Telnyx infrastructure.
