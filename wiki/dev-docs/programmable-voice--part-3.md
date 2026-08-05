---
title: Programmable Voice
summary: The Telnyx Programmable Voice API enables you to integrate voice calling
  capabilities into your applications, providing flexible inbound and outbound call
  control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake
  Detection, Dialogflow ES integration, and AI-driven gather flows.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
updated_at: 2026-08-05T14:03:33Z
---

# Programmable Voice

*Part 3 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 2](programmable-voice--part-2.md), [Part 4](programmable-voice--part-4.md)*

The Telnyx Programmable Voice API enables you to integrate voice calling capabilities into your applications, providing flexible inbound and outbound call control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake Detection, Dialogflow ES integration, and AI-driven gather flows.

## Deepfake Detection

Telnyx Deepfake Detection analyzes live call audio to determine whether the remote party's voice is human or AI-generated. When enabled, audio is streamed in real time to a detection model that returns a classification result via webhook. Deepfake detection is available on both outbound calls (Dial) and inbound calls (Answer).

### How Deepfake Detection Works

1. You enable `deepfake_detection` when dialing or answering a call.
2. Telnyx streams the remote party's audio to the detection service.
3. The service analyzes audio frames and returns a result within the configured timeout.
4. You receive a `call.deepfake_detection.result` webhook with the classification, or a `call.deepfake_detection.error` webhook if something went wrong.

The call proceeds normally while detection runs in the background — there is no impact on call audio or latency.

### Configuration Parameters

| Parameter | Type | Default | Range | Description |
| --- | --- | --- | --- | --- |
| `enabled` | boolean | `false` | — | Whether deepfake detection is enabled. |
| `timeout` | integer | `15` | 5–60 | Maximum seconds to wait for a detection result before timing out. |
| `rtp_timeout` | integer | `30` | 5–120 | Maximum seconds to wait for RTP audio. If no audio arrives within this window, detection stops with an error. |

### Enabling on an Outbound Call

Include the `deepfake_detection` object when creating an outbound call via the Dial command:

```
curl -X POST https://api.telnyx.com/v2/calls \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_id": "7267xxxxxxxxxxxxxx",
    "from": "+18005550101",
    "to": "+18005550100",
    "deepfake_detection": {"enabled": true}
  }'
```

### Enabling on an Inbound Call

Add `deepfake_detection` to the Answer command when picking up an incoming call:

```
curl -X POST https://api.telnyx.com/v2/calls/$CALL_CONTROL_ID/actions/answer \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"deepfake_detection": {"enabled": true}}'
```

### Handling the Result Webhook

When detection completes, you receive a `call.deepfake_detection.result` webhook:

```
{
  "record_type": "event",
  "event_type": "call.deepfake_detection.result",
  "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  "occurred_at": "2025-06-15T14:30:27.521992Z",
  "payload": {
    "call_control_id": "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
    "connection_id": "7267xxxxxxxxxxxxxx",
    "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
    "call_session_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "result": "fake",
    "score": 0.87,
    "consistency": 94.5
  }
}
```

Result fields:

| Field | Type | Description |
| --- | --- | --- |
| `result` | string | `real` — human voice detected. `fake` — AI-generated voice detected. `silence_timeout` — no analyzable speech before timeout. |
| `score` | float \| null | Probability the audio is AI-generated, from `0.0` (likely real) to `1.0` (likely deepfake). Null for `silence_timeout`. |
| `consistency` | float \| null | Percentage (0–100) indicating how consistently the model classified the audio across frames. Values above 90% indicate high confidence. Null for `silence_timeout`. |

### Handling Errors

If detection fails, you receive a `call.deepfake_detection.error` webhook:

```
{
  "record_type": "event",
  "event_type": "call.deepfake_detection.error",
  "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
  "occurred_at": "2025-06-15T14:30:27.521992Z",
  "payload": {
    "call_control_id": "v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
    "connection_id": "7267xxxxxxxxxxxxxx",
    "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
    "call_session_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "error_message": "detection_timeout"
  }
}
```

Error types:

| Error | Description |
| --- | --- |
| `detection_timeout` | No detection result received within the configured `timeout`. |
| `rtp_timeout` | No RTP audio received within the configured `rtp_timeout`. |
| `dfd_connection_error` | Could not connect to the detection service. |
| `dfd_stream_error` | Audio stream to the detection service failed. |

### Best Practices for Deepfake Detection

- **Set appropriate timeouts.** The default 15-second detection timeout works well for most calls. Increase it if callers may take longer to start speaking (for example, IVR prompts on the remote end).
- **Use `score` and `consistency` together.** A high score with high consistency is a strong signal. A high score with low consistency may warrant additional verification rather than an immediate hangup.
- **Handle errors gracefully.** Detection errors should not block the call. Design your application to fall through to normal call handling when detection is unavailable.

## Dialogflow ES Integration

Telnyx's Dialogflow integration lets you create and manage sophisticated voice interactions with your customers. You can integrate your Dialogflow ES instance so that audio from the call is sent to it and the bot's response is played on the call.

### Getting Started

Assign the Dialogflow configuration to your Voice API application using the following update request:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{ \
    service_account: “GOOGLE_APPLICATION_CREDENTIALS” \
  }' \
  https://api.telnyx.com/v2/dialogflow_connections/{connection_id}
```

`GOOGLE_APPLICATION_CREDENTIALS` must be provided in the form of an encoded JSON. See the [Google Dialogflow Setup guide](https://cloud.google.com/dialogflow/es/docs/quick/setup#sa-create).

### Enabling Dialogflow for Outbound Calls

```
curl --location --request POST 'https://api.telnyx.com/v2/calls' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "to":"+48662211095",
  "from":"+13127367481",
  "connection_id":"1714376719458109299",
  "enable_dialogflow": true
}'
```

### Enabling Dialogflow for Inbound Calls

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"enable_dialogflow": true}' \
  https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer
```

When the integration is enabled, the audio provided by Dialogflow is played on the call, and the following webhook is delivered to the webhook URL:

```
{
  "data": {
      "event_type": "dialogflow.detectintent.response",
      "id": "22cbf929-9a87-43ab-873b-b832ccf05a05",
      "occurred_at": "2022-05-23T16:01:53.301413Z",
      "payload": {
        "call_control_id": "v2:WE_lbN28P-h81n4xeceODATcx9J-FYci6WO4hP3Gp9Sb789WivnkMw",
        "call_leg_id": "a3dc0316-dab1-11ec-aaff-02420a0d6669",
        "call_session_id": "a3cf4428-dab1-11ec-84a9-02420a0d6669",
        "client_state": null,
        "confidence": 1,
        "connection_id": "1669581837548127492",
        "fulfillment_messages": [{
            "text": [
              "Hi! I'm the virtual car rental agent. I can help you start a new car rental reservation. How can I assist you today?"
            ]
          }
        ],
        "is_final": true,
        "stream_id": "eb724ae3-4f93-49d0-9ab5-c821b47c4fc5",
        "transcript": "hello"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/e437011a-bb4a-4f34-8060-30e6604c2cf6"
  }
}
```
