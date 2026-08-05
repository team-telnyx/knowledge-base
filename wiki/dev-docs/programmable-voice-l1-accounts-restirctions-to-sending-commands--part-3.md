---
title: Programmable Voice - L1 Accounts Restirctions to Sending Commands
summary: A consolidated reference for Telnyx Programmable Voice covering account restrictions
  for L1 verified accounts, sending commands and receiving webhooks, media streaming
  over WebSockets, noise suppression, call queueing, and Pay over Voice.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
updated_at: 2026-08-05T14:04:29Z
---

# Programmable Voice - L1 Accounts Restirctions to Sending Commands

*Part 3 of 4 — see also: [Part 1](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-1.md), [Part 2](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-2.md), [Part 4](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-4.md)*

A consolidated reference for Telnyx Programmable Voice covering account restrictions for L1 verified accounts, sending commands and receiving webhooks, media streaming over WebSockets, noise suppression, call queueing, and Pay over Voice.

## Noise Suppression

Noise suppression works for both AI-powered calls (such as AI Assistants and Gather Using AI) and regular voice calls. While it improves audio quality across all call types by reducing background noise, the biggest value comes from enhanced AI performance — cleaner audio leads to more accurate speech recognition and better AI responses. This makes noise suppression especially valuable for AI use cases where audio quality directly impacts user experience.

### Voice API

Noise suppression can be enabled for Voice API calls. The only required parameter is `direction`, which can be `inbound`, `outbound`, or `both`. A charge is applied for each direction separately.

```
curl --request POST \
  --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "direction": "inbound"
  }'
```

Noise suppression can be stopped at any time:

```
curl --request POST \
  --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_stop \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{}'
```

### Supported Engines

Telnyx offers four noise suppression engines, each optimized for different use cases:

| Engine | Value | Description | Best for |
| --- | --- | --- | --- |
| Denoiser | `Denoiser` | Built-in, general-purpose noise reduction | Default option for most calls |
| DeepFilterNet | `DeepFilterNet` | Open-source, full-band 48 kHz processing | Telephony and WebRTC |
| Krisp | `Krisp` | Telephony noise suppression with speaker isolation; supports multiple sub-models via `noise_suppression_engine_config.model` | Telephony with speaker isolation |
| AiCoustics | `AiCoustics` | STT-optimized noise suppression | AI and speech recognition workloads |

#### Choosing an Engine

- For standard telephony, use `Denoiser` (default) or `Krisp` for speaker isolation.
- For WebRTC calls, use `DeepFilterNet` for full-band processing.
- For AI-powered calls (AI Assistants, Gather Using AI), consider `AiCoustics` for the best speech recognition accuracy.

Set the engine using the `noise_suppression_engine` parameter:

```
curl --request POST \
  --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "direction": "inbound",
    "noise_suppression_engine": "AiCoustics"
  }'
```

### Engine Configuration

Some engines support additional tuning via `noise_suppression_engine_config`. Parameters are engine-specific and ignored by other engines.

#### Krisp Models

The `Krisp` engine supports three sub-models optimized for different telephony scenarios. Select a model using `noise_suppression_engine_config.model`:

| Model value | Best for |
| --- | --- |
| `krisp-nlsv-f4t-v2.4ef` | General telephony (default-quality model) |
| `krisp-nlsv-f4t-12k-v1.ef` | Narrowband telephony (12 kHz) |
| `krisp-nlsv-b1-v1.4ef` | Lightweight model for constrained environments |

Suppression intensity can also be set with `suppression_lev` (0–100):

```
curl --request POST \
  --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "direction": "inbound",
    "noise_suppression_engine": "Krisp",
    "noise_suppression_engine_config": {
      "model": "krisp-nlsv-f4t-12k-v1.ef",
      "suppression_lev": 80
    }
  }'
```

#### DeepFilterNet Configuration

The `DeepFilterNet` engine supports two tuning parameters:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `attenuation_lim` | integer (0–100) | `100` | Maximum attenuation applied to noise |
| `mode` | `standard` \| `advanced` | — | Processing mode |

#### AiCoustics Configuration

The `AiCoustics` engine exposes enhancement and gain controls:

| Parameter | Type | Range | Description |
| --- | --- | --- | --- |
| `enhancement_lev` | number | 0–1 | Enhancement intensity |
| `voice_gain` | number | 0.1–4 | Voice gain multiplier |

### TeXML

In TeXML there is a dedicated verb for enabling noise suppression on the call:

```xml
<Response>
    <Start>
        <Suppression direction="inbound" noise_suppression_engine="Krisp"/>
    </Start>
...
    <Stop>
        <Suppression/>
    </Stop>
</Response>
```

## Queueing Calls

Call Queueing is fully integrated with the Telnyx Voice API. The Call Queue API allows creating and managing call queues with a few API requests.

### Adding a Call to a New or Existing Queue

A call can be placed into a queue using the `enqueue` command. Use the `queue_name` parameter to specify a queue into which the call should be placed.

- If the `queue_name` refers to a queue that already exists, the call will be placed at the end of the queue.
- If the `queue_name` hasn't been used before, a new queue with this name will be created and the call will be placed into it.

```
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer YOUR_API_KEY"
  --data '{"queue_name": "support"}'
  https://api.telnyx.com/v2/calls/<CALL_CONTROL_ID>/actions/enqueue
```

If the call for which the `enqueue` command was issued is bridged to another call leg (i.e. it is in an active conversation with someone), the call will be unbridged.

### Bridging an Existing Call to a Queue

The `bridge` command can be used to bridge a call to another call waiting in a queue. The queue's `queue_name` should be used as the bridge command's `queue` parameter. For example, a customer support agent can be bridged to the first call from a queue of waiting customer calls:

```
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer YOUR_API_KEY"
  --data '{"queue": "support"}'
  https://api.telnyx.com/v2/calls/8899ad4a-de6f-11eb-a54c-02420a0d4168/actions/bridge
```

When a `bridge` command is issued, the call at the top of the specified queue will be dequeued and a bridge will be attempted.

### Dequeuing Calls

Calls can be removed from queues in four ways:

1. Ending the call by any means (e.g. a `hangup` command, or the call being disconnected by calling parties).
2. Issuing any command that results in the call being bridged elsewhere (e.g. `bridge`, `transfer`, conference `join`, `refer`).
3. A call is automatically removed from queues if the `max_wait_time_secs` parameter was used when adding the call to a queue and the specified maximum waiting time has elapsed. The automatically dequeued call will remain in a parked state and await further call commands.
4. Sending the `leave_queue` command with a call's `call_control_id` will remove that call from any queue it is in, leaving it parked awaiting further call commands.

```
curl -X POST
  --header "Content-Type: application/json"
  --header "Accept: application/json"
  --header "Authorization: Bearer YOUR_API_KEY"
  https://api.telnyx.com/v2/calls/<CALL_CONTROL_ID>/actions/leave_queue
```

### Inspecting Queue State

A number of endpoints let you inspect queues and enqueued calls:

- Retrieve a queue
- Retrieve a call from a queue
- List calls in a queue

Empty queues will automatically be garbage collected after a period of inactivity.

### Receiving Webhooks for Call Queueing Events

The Telnyx API sends a webhook for every major queue event — when a call is put in a queue, and when a call leaves the queue for some reason. Webhooks contain information about the call and the queue with which it is associated.
