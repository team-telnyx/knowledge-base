---
title: Telnyx Programmable Voice API
summary: The Telnyx Programmable Voice API enables integration of voice calling capabilities
  into applications, providing granular control over inbound and outbound calls through
  commands, webhooks, media streaming, IVR, call queueing, noise suppression, and
  SIPREC recording.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
updated_at: 2026-06-11T10:42:33Z
---

# Telnyx Programmable Voice API

*Part 3 of 3 — see also: [Part 1](telnyx-programmable-voice-api--part-1.md), [Part 2](telnyx-programmable-voice-api--part-2.md)*

The Telnyx Programmable Voice API enables integration of voice calling capabilities into applications, providing granular control over inbound and outbound calls through commands, webhooks, media streaming, IVR, call queueing, noise suppression, and SIPREC recording.

## Call Queueing

Call Queueing is integrated with the Voice API and lets you create and manage queues with a few commands.

### Adding a Call to a Queue

Use the `enqueue` command with a `queue_name`. If the queue exists, the call is placed at the end; if not, a new queue is created. If the call is currently bridged, it will be unbridged first.

```bash
curl -X POST --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"queue_name": "support"}' \
  https://api.telnyx.com/v2/calls/<CALL_CONTROL_ID>/actions/enqueue
```

### Bridging to a Queue

Use the `bridge` command with a `queue` parameter to connect a call to the first call waiting in the named queue. The dequeued call is removed from the queue.

```bash
curl -X POST --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"queue": "support"}' \
  https://api.telnyx.com/v2/calls/<CALL_CONTROL_ID>/actions/bridge
```

### Dequeuing Calls

Calls leave queues in four ways:

1. The call ends (hangup or disconnect).
2. A command bridges the call elsewhere (`bridge`, `transfer`, conference `join`, `refer`).
3. The `max_wait_time_secs` expires — the call is automatically removed and remains parked.
4. The `leave_queue` command is issued — the call is removed and left parked.

### Inspecting Queues

API endpoints are available to retrieve a queue, retrieve a specific call from a queue, and list all calls in a queue. Empty queues are automatically garbage collected after a period of inactivity.

Webhooks are sent when a call is enqueued or leaves a queue. See the [enqueue command](telnyx-programmable-voice-api-sending-commands.md) API reference for example payloads.

## Noise Suppression

Noise suppression works for both AI-powered calls (AI Assistants, Gather Using AI) and regular voice calls. It improves audio quality across all call types but provides the biggest value for AI performance — cleaner audio leads to more accurate speech recognition.

### Voice API

Start suppression with `suppression_start` and stop with `suppression_stop`. The `direction` parameter is required: `inbound`, `outbound`, or `both`. Charges apply per direction.

```bash
curl --request POST \
  --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"direction": "inbound"}'
```

### Supported Engines

| Engine | Value | Best For |
|---|---|---|
| Denoiser | `Denoiser` | Default for most calls |
| DeepFilterNet | `DeepFilterNet` | WebRTC, full-band 48 kHz processing |
| Krisp | `Krisp` | Telephony with speaker isolation; supports sub-models |
| AiCoustics | `AiCoustics` | AI and speech recognition workloads |

Set the engine with the `noise_suppression_engine` parameter.

### Engine Configuration

- **Krisp** — supports sub-models via `noise_suppression_engine_config.model`: `krisp-nlsv-f4t-v2.4ef` (general), `krisp-nlsv-f4t-12k-v1.ef` (narrowband), `krisp-nlsv-b1-v1.4ef` (lightweight). Also supports `suppression_lev` (0–100).
- **DeepFilterNet** — `attenuation_lim` (0–100, default 100) and `mode` (`standard` or `advanced`).
- **AiCoustics** — `enhancement_lev` (0–1) and `voice_gain` (0.1–4).

### TeXML

Use the `<Suppression>` nested verb inside `<Start>` or `<Stop>`:

```xml
<Response>
  <Start>
    <Suppression direction="inbound" noise_suppression_engine="Krisp"/>
  </Start>
  <Stop>
    <Suppression/>
  </Stop>
</Response>
```

## SIPREC Recording

A SIPREC client (SRC) initiates and manages recording sessions by communicating with a Session Recording Server (SRS).

### Creating a SIPREC Server Connector

```bash
curl --request POST \
  --url https://api.telnyx.com/v2/siprec_connectors \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"name": "siprec-server-connector", "host": "siprec.telnyx.com", "port": 5060}'
```

### Voice API SIPREC Session

Start with `siprec_start` and stop with `siprec_stop`:

```bash
curl --request POST \
  --url https://api.telnyx.com/v2/{call_control_id}/actions/siprec_start \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"connector_name": "siprec-server-connector", "direction": "both_tracks"}'
```

### TeXML SIPREC Session

```xml
<Response>
  <Start>
    <Siprec track="both_tracks" connectorName="siprec-server-connector" statusCallback="https://example.com/siprec_callback" />
  </Start>
</Response>
```

Stop with:

```xml
<Response>
  <Stop>
    <Siprec/>
  </Stop>
</Response>
```

## L1 Account Restrictions

Accounts with L1 verification are subject to the following restrictions:

- All machine-generated speak commands are prepended with: *"This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com"*. This applies to:
  - `/v2/calls` (Dial)
  - `/v2/calls/:call_control_id/actions/transfer`
  - `/v2/calls/:call_control_id/actions/gather_using_audio`
  - `/v2/calls/:call_control_id/actions/gather_using_speak`
  - `/v2/calls/:call_control_id/actions/playback_start`
  - `/v2/calls/:call_control_id/actions/speak`
  - `/v2/calls/:call_control_id/actions/gather_using_ai`
  - `/v2/calls/:call_control_id/actions/ai_assistant_start`
  - TeXML verbs: `Play`, `Say`, `AIGather`
- Maximum of 100 outbound calls per day
- Maximum of 10 outbound calls per hour
