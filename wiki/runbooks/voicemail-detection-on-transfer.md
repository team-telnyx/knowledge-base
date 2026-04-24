---
title: Voicemail Detection on Transfer
summary: Configure Voice AI Assistants to detect voicemail on transferred calls and respond automatically.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer/index
    content_hash: 85e6e4899a8d0895b6e212b06c3797a96a2eab1cbacb7ac1280c053912316ea9
updated_at: 2026-04-10T00:00:00Z
---

# Voicemail Detection on Transfer

Configure Voice AI Assistants to detect voicemail on transferred calls and respond automatically.

When a Voice AI Assistant transfers a call, the destination may go to voicemail. Without detection, the caller experiences dead air while the voicemail greeting plays. Voicemail detection on transfer solves this by identifying when a transferred call reaches voicemail and triggering a configured action automatically. The assistant stays on the line with the caller throughout, so there is never a gap in the conversation.

***

## How it works

1. The AI Assistant initiates a transfer using the transfer tool.
2. AMD (Answering Machine Detection) monitors the transfer destination.
3. If voicemail is detected, the configured action triggers immediately.
4. The assistant returns to the caller and continues the conversation.

The caller remains connected to the assistant during the entire process. If a human answers the transfer destination, the call proceeds as a normal transfer.

***

## Configuration options

### Detection mode

The `detection_mode` field controls whether voicemail detection is active on the transfer:

| Value      | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| `disabled` | No voicemail detection (default).                                      |
| `premium`  | ML-based detection with high accuracy. Recommended for production use. |

### Actions when voicemail is detected

The `on_voicemail_detected.action` field determines what happens when voicemail is detected:

| Action                            | Behavior                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------------- |
| `stop_transfer`                   | Cancels the transfer immediately and returns the assistant to the caller.                     |
| `leave_message_and_stop_transfer` | Delivers a TTS message to the voicemail, then cancels the transfer and returns to the caller. |

### Voicemail message options

When using `leave_message_and_stop_transfer`, the `on_voicemail_detected.voicemail_message` object configures what message is left:

| Field     | Value                        | Description                                                         |
| --------- | ---------------------------- | ------------------------------------------------------------------- |
| `type`    | `message`                    | Plays a custom TTS text as the voicemail message.                   |
| `type`    | `warm_transfer_instructions` | Uses the warm transfer audio instructions as the voicemail message. |
| `message` | string                       | The TTS text to deliver when `type` is `message`.                   |

***

## Setting up via the Portal

1. Navigate to **AI, Storage and Compute** in the [Telnyx Portal](https://portal.telnyx.com).
2. Select an existing AI Assistant or create a new one.
3. In the **Tools** section, open the transfer tool configuration.
4. Under **Voicemail Detection**, set the detection mode to **Premium**.
5. Choose your preferred action: **Stop the transfer** or **Leave a message and stop transfer**.
6. If leaving a message, enter the TTS text you want delivered to voicemail.
7. Save and test with a call to a number that goes to voicemail.

***

## Setting up via API

Configure voicemail detection within the transfer tool when creating or updating an assistant.

### Stop the transfer on voicemail

This configuration cancels the transfer and returns the assistant to the caller when voicemail is detected:

```bash theme={null}
curl -L 'https://api.telnyx.com/v2/ai/assistants' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ' \
  --data-raw '{
    "name": "Support Agent",
    "instructions": "You are a support agent. Transfer calls to the support team when needed.",
    "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
    "tools": [
      {
        "type": "transfer",
        "transfer": {
          "targets": [
            {
              "name": "Support Team",
              "to": "+15551234567"
            }
          ],
          "from": "+15553456789",
          "voicemail_detection": {
            "detection_mode": "premium",
            "on_voicemail_detected": {
              "action": "stop_transfer"
            }
          }
        }
      }
    ]
  }'
```

### Leave a message on voicemail

This configuration delivers a TTS message to voicemail before returning to the caller:

```bash theme={null}
curl -L 'https://api.telnyx.com/v2/ai/assistants' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ' \
  --data-raw '{
    "name": "Support Agent",
    "instructions": "You are a support agent. Transfer calls to the support team when needed.",
    "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
    "tools": [
      {
        "type": "transfer",
        "transfer": {
          "targets": [
            {
              "name": "Support Team",
              "to": "+15551234567"
            }
          ],
          "from": "+15553456789",
          "voicemail_detection": {
            "detection_mode": "premium",
            "on_voicemail_detected": {
              "action": "leave_message_and_stop_transfer",
              "voicemail_message": {
                "type": "message",
                "message": "Hello, this is a message from Telnyx support. We attempted to reach you regarding your open ticket. We will try again shortly. Thank you."
              }
            }
          }
        }
      }
    ]
  }'
```

### Leave warm transfer instructions on voicemail

This configuration uses the warm transfer audio instructions as the voicemail message instead of custom TTS text:

```bash theme={null}
curl -L 'https://api.telnyx.com/v2/ai/assistants' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer ' \
  --data-raw '{
    "name": "Support Agent",
    "instructions": "You are a support agent. Transfer calls to the support team when needed.",
    "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
    "tools": [
      {
        "type": "transfer",
        "transfer": {
          "targets": [
            {
              "name": "Support Team",
              "to": "+15551234567"
            }
          ],
          "from": "+15553456789",
          "voicemail_detection": {
            "detection_mode": "premium",
            "on_voicemail_detected": {
              "action": "leave_message_and_stop_transfer",
              "voicemail_message": {
                "type": "warm_transfer_instructions"
              }
            }
          }
        }
      }
    ]
  }'
```

***

## Related resources

* [Voice AI Assistant API Reference](https://developers.telnyx.com/api-reference/assistants/create-an-assistant#transfertool) - Complete transfer tool API documentation including voicemail detection parameters.
* [Agent Handoff](agent-handoff.md) - Configure AI-to-AI handoffs between specialized assistants.
* [Answering Machine Detection](answering-machine-detection.md) - AMD for outbound calls using programmable voice.
* [No-Code Voice Assistant](voice-assistant-quickstart.md) - Get started with Voice AI Assistants in the Portal.
