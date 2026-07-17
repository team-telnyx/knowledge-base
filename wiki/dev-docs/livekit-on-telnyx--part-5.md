---
title: LiveKit on Telnyx
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale,
  combining LiveKit's agent framework with built-in telephony, colocated AI inference
  on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers
  architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM),
  telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
- url: https://developers.telnyx.com/docs/livekit/build/index
- url: https://developers.telnyx.com/docs/livekit/compatibility
- url: https://developers.telnyx.com/docs/livekit/connect
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
- url: https://developers.telnyx.com/docs/livekit/deploy/index
- url: https://developers.telnyx.com/docs/livekit/deploy/management
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
- url: https://developers.telnyx.com/docs/livekit/index
- url: https://developers.telnyx.com/docs/livekit/limits
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-07-17T09:14:35Z
---

# LiveKit on Telnyx

*Part 5 of 6 — see also: [Part 1](livekit-on-telnyx--part-1.md), [Part 2](livekit-on-telnyx--part-2.md), [Part 3](livekit-on-telnyx--part-3.md), [Part 4](livekit-on-telnyx--part-4.md), [Part 6](livekit-on-telnyx--part-6.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Secrets

### Setting secrets on deploy

Pass secrets when you deploy:

```
lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
```

To set additional secrets after deploy:

```
lk agent update-secrets <agent-id> --secrets "OPENAI_API_KEY=<your-key>"
```

### Updating secrets

Update secrets on a running agent:

```
lk agent update-secrets <agent-id> --secrets "KEY=value"
```

### Auto-injected variables

The platform automatically injects these into your agent's environment at runtime:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY` (your Telnyx API key — used for both platform auth and model access)
- `LIVEKIT_API_SECRET`

You don't need to set these manually. Note: `LIVEKIT_API_KEY` is your Telnyx API key. Telnyx can revoke it if needed, giving you a single credential to manage.

### Local development

For local development, use a `.env.local` file:

```
TELNYX_API_KEY=your-key-here
LIVEKIT_URL=https://nyc1.livekit-telnyx.com
LIVEKIT_API_KEY=your-key
LIVEKIT_API_SECRET=your-secret
```

Secrets set via the CLI are encrypted at rest and injected at runtime. They cannot be retrieved after being set.

## Management and access

### Access model

All platform interaction is through the `lk` CLI and the [Telnyx Portal](https://portal.telnyx.com). There is no direct access to underlying infrastructure (no kubectl, no SSH).

### What Telnyx manages

- LiveKit SFU (media server)
- SIP service (built-in telephony)
- Agent container runtime and orchestration
- Autoscaling
- TLS/SSL termination and load balancing
- Health checks and rolling deploys

### What you control

| Capability | How |
| --- | --- |
| Agent code and Dockerfile | `lk agent deploy .` |
| Secrets | `lk agent deploy --secrets` / `lk agent update-secrets` |
| Rollback | `lk agent rollback` |
| Logs | `lk agent logs` |
| Phone numbers | Telnyx Portal |
| SIP connections | Telnyx Portal |
| Model selection | Telnyx plugin or BYOK |

### Current limitations

- No volume mounts or persistent storage
- No custom networking or network policies
- No privileged containers
- No custom domains
- No direct database access — use external services with secrets

See [Compatibility](compatibility.md) for the full list of supported and unsupported features.

## Telephony

Telnyx is the carrier. Buy a number, connect it to your agent — no third-party SIP trunk setup, no FQDN auth dance. Calls route on-net from Telnyx SIP directly to your agent. For setup steps, see [Quickstart](quickstart.md).

### Supported

**Inbound calls.** Inbound calls are routed to your agent via SIP dispatch rules. When someone calls your DID, Telnyx forwards it to the LiveKit SIP service, which dispatches it to your agent based on the rules you configure.

**Outbound calls.** Use the `lk` CLI to place an outbound call into a room:

```
lk sip participant create \
  --room "my-room" \
  --trunk "<SIP_TRUNK_ID>" \
  --call "+15551234567" \
  --identity "outbound-caller"
```

**DTMF.** DTMF tones are supported via RFC 2833/4733. Tones are forwarded to your agent as events and can be handled in code.

**SIP headers.** Pass call metadata through to your agent using `headers_to_attributes`. Header values are mapped to LiveKit participant attributes, available in your agent at runtime.

**HD voice.** Telnyx supports two HD voice codecs for higher-quality audio on SIP calls:

- **G.722** — Wideband audio at 16 kHz sample rate. Enabled by default on all Telnyx SIP connections. No additional configuration needed.
- **Opus** — Wideband audio at 48 kHz sample rate. Requires SRTP encryption on both sides — enable OPUS in your Telnyx SIP connection's inbound codec list and set `media_encryption: ALLOW` on your LiveKit inbound trunk. Delivers the highest audio quality for voice AI agents.

Both codecs are negotiated automatically during SIP call setup. If the remote side supports Opus, it will be preferred over G.722.

### Not yet supported

These features require Enterprise SIP, which is on the roadmap:

- **Call transfers (REFER / warm transfer)**

## Observability

### What's available today

**Agent logs.** Stream logs from your running agent via the CLI:

```
lk agent logs <agent-id>
```

This gives you stdout/stderr from your agent in real time — same as LiveKit Cloud's log access.

### Coming very soon

Traces, metrics, and session debugging are on the [Compatibility](compatibility.md) roadmap.

## Limits and quotas

### Build limits

| Limit | Value |
| --- | --- |
| Build timeout | 10 minutes |
| Build context size | 1 GB |

### Agent limits

| Limit | Value |
| --- | --- |
| Max concurrent agents | Contact us |
| Max concurrent sessions per agent | Contact us |

### Telephony limits

| Limit | Value |
| --- | --- |
| Max concurrent calls | Contact us |

For specific limit increases, contact your Telnyx account team.

## Pricing

All services — compute, models, and telephony — are billed on a single Telnyx invoice. On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.

### Telnyx Ultra — Platform Exclusive

Our highest-fidelity voice. Available exclusively for agents deployed on LiveKit on Telnyx, not through the plugin alone. See the [TTS voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index) for the variety of voices, languages, and accents offered.

### STT

See [telnyx.com/pricing/speech-to-text](https://telnyx.com/pricing/speech-to-text) for current rates.

### TTS

See [telnyx.com/pricing/text-to-speech](https://telnyx.com/pricing/text-to-speech) for current rates.

### LLM

See [telnyx.com/pricing/conversational-ai](https://telnyx.com/pricing/conversational-ai) for current rates.
