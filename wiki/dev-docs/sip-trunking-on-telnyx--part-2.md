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

*Part 2 of 5 — see also: [Part 1](sip-trunking-on-telnyx--part-1.md), [Part 3](sip-trunking-on-telnyx--part-3.md), [Part 4](sip-trunking-on-telnyx--part-4.md), [Part 5](sip-trunking-on-telnyx--part-5.md)*

Telnyx Elastic SIP Trunking provides elastic, programmable telephony over IP with multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling support. This page consolidates the authentication options, configuration guides, caller ID and concurrency policies, advanced features, and emergency calling capabilities available on Telnyx SIP trunks.

## Caller ID Policy

Telnyx enforces strict caller ID validation to prevent spoofing and ensure compliance with telecommunications regulations. Invalid caller ID numbers are rejected with a `403 Caller Origination Number is Invalid D35` SIP response.

### Number format requirements

The accepted caller ID format depends on the connection's localization setting and call destination.

**USA localization** accepts national format (`3129457420`), 11-digit format (`13129457420`), or E.164 format (`+13129457420`).

**International localization** (e.g., Ireland) accepts national format (`840-1234`), country-specific format (`01-840-1234`), or E.164 format (`+353-1-840-1234`).

**Cross-border calls** require E.164 format only. For example, a connection with Ireland localization calling the USA must use `+13129457420`.

Connections with Caller ID Override enabled can send any format for outbound calls, bypassing standard validation rules.

### SIP header priority

Telnyx checks the following SIP headers in order to determine the caller ID:

1. `P-Preferred-Identity` (User part)
2. `P-Asserted-Identity` (User part)
3. `Remote-Party-Id` (User part)
4. `FROM` (User part)

When multiple headers are present, only the highest priority header is used.

### Caller ID anonymization

To anonymize the caller ID, include the `Privacy: id` header in the SIP request:

```
Privacy: id
```

A valid origination number must still be provided; invalid numbers with this header trigger the D35 error. Toll-free and emergency number calls cannot be anonymized. Recipients always see the actual caller ID for emergency services (911, etc.) and toll-free numbers.

### International spoofing restrictions

Outbound calls to international destinations with spoofed caller IDs are rejected with a `503` error response, allowing fallback routing logic on the client side.

### Validation behavior

If no localization is configured and a number appears invalid, Telnyx defaults to USA validation rules. Failed validation returns a `404 Invalid Destination` response.

### Configuration

Set the connection localization in the Mission Control Portal under Connection Outbound Settings, or via the API on credential, FQDN, or IP connections:

```
{
  "outbound": {
    "localization": "US"
  }
}
```

### Troubleshooting

| Error | Cause | Solution |
| --- | --- | --- |
| 403 D35 | Invalid caller ID format | Use E.164 format or match localization requirements |
| 404 | Invalid destination | Verify the called number is in E.164 format |
| 503 | International spoofing | Use a valid origination number for the destination country |

## Concurrent Call Limits

Concurrent call limits control the maximum number of simultaneous outbound calls allowed on an account. This limit applies globally across all outbound voice profiles.

### Default limits

| Verification level | Concurrent calls |
| --- | --- |
| Initial setup | 2 |
| Level 2 verification completed | 10 |
| Custom limit (contact support) | 10+ |

### Error handling

When the application attempts to establish a call that exceeds the configured limit, Telnyx returns a SIP 403 error:

```
403 User channel limit exceeded D1
```

Implement exponential backoff when handling limit errors:

```
on 403 "channel limit exceeded":
    wait 2^attempt seconds (1s, 2s, 4s, ...)
    retry up to max_retries
```

### Monitoring

Track concurrent call usage to prevent limit errors. Via the API, use `GET /v2/calls` and filter for `status: active` to get the current concurrent call count. Via webhooks, track call lifecycle events: increment on `call.initiated` and decrement on `call.hangup`. Maintain an in-memory or database counter to track real-time concurrent usage.

### Best practices

1. Set alerts when usage reaches 80% of the limit.
2. Queue calls when approaching limits rather than failing immediately.
3. Monitor peak usage patterns to anticipate when limit increases are needed.
4. Test error handling to verify the application handles 403 limit errors gracefully.

### Requesting limit increases

For concurrent call limits exceeding 10 channels, contact [support@telnyx.com](mailto:support@telnyx.com). Include the current concurrent call requirement, expected growth trajectory, and use case description (required for limits exceeding 100 channels).

## Outbound Voice Profiles

Outbound voice profiles control routing, billing, and rate limits for outbound SIP calls. Each profile generates a unique Profile ID used in API calls and CDR reports.

| Component | Description |
| --- | --- |
| Profile ID | Unique identifier for API calls and billing reports |
| Tags | Custom labels for tracking and cost allocation |
| SIP Connections | Associated connections authorized for outbound calls |
| Service Plan | Allowed destinations and rate deck configuration |
| Channel Limit | Maximum concurrent outbound channels per profile |

### Destinations

Telnyx supports 255 destinations across 10 regions. Enable destinations by region or individual country. Many destinations require Level 2 verification before activation.

### Channel limits

Channels represent concurrent call capacity. Each active call consumes one channel. Set channel limits per profile to control concurrency and prevent service degradation.

### Billing configuration

**Rate deck** — Calls are rated based on destination number prefix. Download current rate decks or request custom rates through an account representative.

**Max destination rate** — Set a maximum per-minute rate threshold. Calls to destinations exceeding this rate are rejected automatically. For example, a max rate of $0.10/min rejects calls to $0.15/min destinations.

**Daily spend limit** — Define maximum spend per day per connection. Limits reset at 00:00:00 UTC. This prevents unexpected overages from misconfigured systems or traffic anomalies.

### Call recording

Enable recording for all outbound calls or specific ANI numbers.

| Setting | Options |
| --- | --- |
| Format | WAV, MP3 |
| Channels | Mono (single-channel), Stereo (dual-channel) |
| Scope | All calls or specific ANI list |
