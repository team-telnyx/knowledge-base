---
title: Programmable Voice
summary: A comprehensive guide to Telnyx Programmable Voice features including AI
  assistants, conversational AI, answering machine detection, deepfake detection,
  conferencing, call center and call tracking applications, and command reliability
  patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
updated_at: 2026-06-11T10:41:58Z
---

# Programmable Voice

*Part 3 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 2](programmable-voice--part-2.md), [Part 4](programmable-voice--part-4.md)*

A comprehensive guide to Telnyx Programmable Voice features including AI assistants, conversational AI, answering machine detection, deepfake detection, conferencing, call center and call tracking applications, and command reliability patterns.

## Answering Machine Detection

Outbound calls placed with the Voice API can be enabled with Answering Machine Detection (AMD). When a call is answered, Telnyx runs real-time detection to determine if it was picked up by a human or a machine and sends webhooks with the result.

### AMD Settings

Set the `answering_machine_detection` value when creating an outbound call or transferring an inbound call:

| Setting | Description | Webhooks Sent |
| --- | --- | --- |
| `detect` | Only detect if answering machine or human. | `call.machine.detection.ended` |
| `detect_beep` | Listens for a final "beep" after detecting a `machine`. | `call.machine.detection.ended` and `call.machine.greeting.ended` (only if beep detected) |
| `detect_words` | After a `machine` is detected, a 30-second beep detection begins. | `call.machine.detection.ended` and `call.machine.greeting.ended` |
| `greeting_end` | Listens for extended silence or a beep to determine if the greeting has ended. | `call.machine.detection.ended` and `call.machine.greeting.ended` |
| `premium` | **Recommended.** Uses advanced speech recognition and machine learning for exceptional accuracy. | `call.machine.premium.detection.ended` and optionally `call.machine.premium.greeting.ended` |
| `premium_ios_call_screening_detection` | Premium AMD with Apple Call Screening support. | `call.machine.premium.detection.ended`, `call.machine.premium.greeting.ended`, and `call.machine.premium.call_screening.detected` |

### Standard AMD Webhooks

**`call.machine.detection.ended`** — Sent when Telnyx can determine human or machine. Results: `human`, `machine`, or `not_sure` (recommended to treat as human).

**`call.machine.greeting.ended`** — Sent when the prompt or beep detection finishes. Results: `ended` (greeting over, `greeting_end` only), `beep_detected` (`detect_beep`/`detect_words`), or `not_sure` (30-second timeout).

### Premium AMD Webhooks

**`call.machine.premium.detection.ended`** — Results include: `human_residence`, `human_business`, `machine`, `silence`, `fax_detected`, or `not_sure`. The `total_analysis_time_millis` setting (default 30 seconds) controls the detection timeout; if reached, the result is `not_sure`.

**`call.machine.premium.greeting.ended`** — Sent only if a machine answered. Results: `beep_detected` (beep heard), `no_beep_detected` (timeout reached without beep), or `prompt_ended` (iOS call-screening prompt ended without beep, `premium_ios_call_screening_detection` only).

**`call.machine.premium.call_screening.detected`** — Sent when an Apple Call Screening tone is detected (result: `screening`). Telnyx then restarts Premium AMD; expect another `call.machine.premium.detection.ended` webhook.

### iOS Call Screening Detection

When `premium_ios_call_screening_detection` is set, Telnyx first runs Premium AMD. If the initial result is `machine`, Telnyx listens for the iOS call-screening prompt. Use `answering_machine_detection_config.prompt_end_timeout_millis` to control the maximum wait time (default 30000 ms; range 1000–120000 ms). When the screening prompt ends without a beep, the `prompt_ended` result signals your application to respond to the iOS screening prompt.

### General Order of Operations

1. Create outbound call.
2. Receive `call.initiated` webhook.
3. Receive `call.answered` webhook.
4. Receive detection webhook with human/machine status.
5. Receive greeting-ended webhook (when applicable).

At any point the callee could hang up, generating a `call.hangup` webhook.

## Deepfake Detection

Deepfake Detection analyzes live call audio to determine whether the remote party's voice is human or AI-generated. It runs in the background with no impact on call audio or latency. Available on both outbound calls (Dial) and inbound calls (Answer).

### How It Works

1. You enable `deepfake_detection` when dialing or answering a call.
2. Telnyx streams the remote party's audio to the detection service.
3. The service returns a result within the configured timeout.
4. You receive a `call.deepfake_detection.result` or `call.deepfake_detection.error` webhook.

### Configuration Parameters

| Parameter | Type | Default | Range | Description |
| --- | --- | --- | --- | --- |
| `enabled` | boolean | `false` | — | Whether deepfake detection is enabled. |
| `timeout` | integer | `15` | 5–60 | Maximum seconds to wait for a detection result. |
| `rtp_timeout` | integer | `30` | 5–120 | Maximum seconds to wait for RTP audio. |

### Enabling on an Outbound Call

```
curl -X POST https://api.telnyx.com/v2/calls \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_id": "7267xxxxxxxxxxxxxx",
    "from": "+18005550101",
    "to": "+18005550100",
    "deepfake_detection": {"enabled": true}
  }'
```

### Enabling on an Inbound Call

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"deepfake_detection": {"enabled": true}}'
```

### Result Webhook

The `call.deepfake_detection.result` webhook contains:

| Field | Description |
| --- | --- |
| `result` | `real` (human voice), `fake` (AI-generated), or `silence_timeout` (no analyzable speech). |
| `score` | Probability the audio is AI-generated, 0.0–1.0. Null for `silence_timeout`. |
| `consistency` | Percentage (0–100) of consistent classification across frames. Above 90% indicates high confidence. Null for `silence_timeout`. |

### Error Webhook

The `call.deepfake_detection.error` webhook includes an `error_message`:

| Error | Description |
| --- | --- |
| `detection_timeout` | No result within the configured `timeout`. |
| `rtp_timeout` | No RTP audio within the configured `rtp_timeout`. |
| `dfd_connection_error` | Could not connect to the detection service. |
| `dfd_stream_error` | Audio stream to the detection service failed. |

### Best Practices

- Set appropriate timeouts. Increase if callers may take longer to start speaking.
- Use `score` and `consistency` together. A high score with high consistency is a strong signal; high score with low consistency may warrant additional verification.
- Handle errors gracefully — detection errors should not block the call.

## Dialogflow ES Integration

Telnyx integrates with Google Dialogflow ES to create sophisticated voice interactions. Audio from the call is sent to Dialogflow and the bot's response is played on the call.

### Configuration

Assign Dialogflow configuration to your Voice API application:

```
curl -X POST https://api.telnyx.com/v2/dialogflow_connections/{connection_id} \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{ "service_account": "GOOGLE_APPLICATION_CREDENTIALS" }'
```

The `GOOGLE_APPLICATION_CREDENTIALS` must be provided as encoded JSON. See [Google Dialogflow Setup](https://cloud.google.com/dialogflow/es/docs/quick/setup#sa-create).

### Enabling for Outbound Calls

Include `"enable_dialogflow": true` in the Dial request.

### Enabling for Inbound Calls

Include `"enable_dialogflow": true` in the Answer command.

### Webhooks

When enabled, Dialogflow response webhooks (`dialogflow.detectintent.response`) are delivered to your webhook URL, containing `fulfillment_messages`, `transcript`, `confidence`, and `is_final` fields.
