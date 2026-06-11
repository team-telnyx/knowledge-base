---
title: Telnyx Voice API and SIP Trunking
summary: Telnyx provides a programmable Voice API for building voice applications
  with call control, conferencing, queuing, recording, and AI assistants, alongside
  an Elastic SIP Trunking platform with multiple authentication methods and granular
  routing, billing, and caller-ID configuration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
updated_at: 2026-06-11T10:44:15Z
---

# Telnyx Voice API and SIP Trunking

*Part 2 of 3 — see also: [Part 1](telnyx-voice-api-and-sip-trunking--part-1.md), [Part 3](telnyx-voice-api-and-sip-trunking--part-3.md)*

Telnyx provides a programmable Voice API for building voice applications with call control, conferencing, queuing, recording, and AI assistants, alongside an Elastic SIP Trunking platform with multiple authentication methods and granular routing, billing, and caller-ID configuration.

## Voice API Webhooks

Voice API webhooks are HTTP callbacks that notify your application in real time when events occur during a call. Your application receives a JSON payload and can respond with call control commands.

### Webhook Configuration

Webhooks can be configured at three levels:

1. **Connection webhook config** — default webhook URL tied to a Voice API connection.
2. **Custom webhook config** — per-command overrides via `webhook_url` and `webhook_url_method` parameters.
3. **Events webhook config** — routes specific event types to different URLs.

Key configuration parameters:

| Parameter | Description |
|---|---|
| `webhook_event_url` | Primary destination for webhook delivery |
| `webhook_event_failover_url` | Secondary URL when primary fails |
| `webhook_api_version` | Format version (`"1"` or `"2"`) |
| `webhook_timeout_secs` | Timeout in seconds (0–30) |

### HTTP Methods and Headers

Webhooks use `POST` by default. Set `webhook_url_method` to `GET` in a command to receive payloads as query parameters. Every request includes:

- `Content-Type: application/json`
- `User-Agent: telnyx-webhooks`
- `Telnyx-Signature-Ed25519` — ED25519 signature for verification
- `Telnyx-Timestamp` — Unix timestamp of generation

### Webhook Payload Structure

All webhooks share a common envelope with `data` (containing `record_type`, `event_type`, `id`, `occurred_at`, and `payload`) and `meta` (containing `attempt` and `delivered_to`). Key payload fields include `call_control_id` (used to issue commands), `call_leg_id` (unique per leg), `call_session_id` (shared across related legs), `connection_id`, and `client_state` (base64-encoded state from a previous command).

### Event Types

**Call state:** `call.initiated`, `call.answered`, `call.hold`, `call.unhold`, `call.hangup`, `call.bridged`

**Audio playback:** `call.playback.started`, `call.playback.ended`, `call.speak.started`, `call.speak.ended`

**DTMF and gather:** `call.dtmf.received`, `call.gather.ended`

**Recording:** `call.recording.saved`

**Answering machine detection:** `call.machine.detection.ended`, `call.machine.greeting.ended`, `call.machine.premium.detection.ended`, `call.machine.premium.greeting.ended`

**Media forking:** `call.fork.started`, `call.fork.stopped`

**Queue:** `call.enqueued`, `call.dequeued`

**Transcription:** `call.transcription`

**Streaming:** `streaming.started`, `streaming.stopped`

### Response Codes

| Code | Behavior |
|---|---|
| 2xx | Webhook acknowledged |
| 3xx | Followed (up to 3 redirects) |
| 408, 429 | Retried |
| Other 4xx | Not retried |
| 5xx | Retried |

### Webhook Best Practices

1. Return 2xx immediately, then process asynchronously.
2. Implement idempotency using the event `id` to deduplicate.
3. Verify the `Telnyx-Signature-Ed25519` header.
4. Use `command_id` in call control commands to prevent duplicate processing (duplicate IDs within 60 seconds are ignored).
5. Monitor failures and configure a failover URL.

Use the [Webhook Deliveries API](https://developers.telnyx.com/api-reference/webhooks/list-webhook-deliveries) to inspect delivery history and debug missed webhooks.

## Voice API Services in Europe

Telnyx provides a dedicated European endpoint at `https://api.telnyx.eu` to reduce latency for calls in Europe. To receive calls in Europe, set the Anchor Site for your application to a European site (Frankfurt, London, or Amsterdam) in the application settings. All conference participants and queued calls must be in the same region.

## SIP Trunk Authentication

Telnyx SIP connections support multiple authentication methods:

| Method | Inbound | Outbound | Dynamic IP | Static IP |
|---|---|---|---|---|
| Credentials | ✓ | ✓ | ✓ | ✓ |
| IP + Tech Prefix | ✓ | ✓ | — | ✓ |
| IP + Token | ✓ | ✓ | — | ✓ |
| IP + P-Charge-Info | ✓ | ✓ | — | ✓ |
| FQDN + Credentials | ✓ | ✓ | ✓ | ✓ |
| FQDN + IP | ✓ | ✓ | — | ✓ |

### Credential-Based Authentication

Use username and password for SIP registration. Create via `POST /v2/credential_connections`.

### IP Authentication Token

The `X-Telnyx-Token` header distinguishes multiple SIP connections sharing the same IP address. Requirements:

- 12–48 alphanumeric characters and hyphens
- Globally unique across all Telnyx connections

Both the source IP and token must match the connection configuration. Configure via `PATCH /v2/ip_connections/` with `outbound.ip_authentication_token`.

### Tech Prefix Authentication

A 4-digit identifier prepended to outbound dial strings to differentiate connections sharing the same IP. Format: `[tech_prefix][destination_number]` (e.g., prefix `1234` + destination `+18005678912` = `123418005678912`). Missing or incorrect prefix results in `407 Proxy Authentication Required`. Enable via `PATCH /v2/ip_connections/` with `outbound.tech_prefix_enabled: true`. The prefix value is assigned by Telnyx.

### P-Charge-Info Authentication

A SIP header containing a phone number in E.164 format associated with the connection:

```
P-Charge-Info: <sip:+12125551234@sip.telnyx.com>
```

The number must be assigned to the connection. This is useful for multiple DIDs on a single SIP connection, CDR attribution, and billing per number.

### FQDN Authentication

Hostname-based inbound routing combined with credentials or IP authentication for outbound.
