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
