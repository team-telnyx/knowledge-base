---
title: AI Assistant Configuration
summary: Telnyx AI assistants can be extended with enterprise integrations, tuned
  interruption behavior, persistent memory across conversations, and multi-participant
  call capabilities. This page covers the available integration catalog and connection
  workflow, interruption settings for turn-taking and non turn-taking transcription
  models, memory configuration via the dynamic variables webhook, and the Invite and
  Skip Turn tools used to coordinate multi-participant voice calls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/interruption-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
updated_at: 2026-08-05T13:44:48Z
---

# AI Assistant Configuration

*Part 3 of 6 — see also: [Part 1](ai-assistant-configuration--part-1.md), [Part 2](ai-assistant-configuration--part-2.md), [Part 4](ai-assistant-configuration--part-4.md), [Part 5](ai-assistant-configuration--part-5.md), [Part 6](ai-assistant-configuration--part-6.md)*

Telnyx AI assistants can be extended with enterprise integrations, tuned interruption behavior, persistent memory across conversations, and multi-participant call capabilities. This page covers the available integration catalog and connection workflow, interruption settings for turn-taking and non turn-taking transcription models, memory configuration via the dynamic variables webhook, and the Invite and Skip Turn tools used to coordinate multi-participant voice calls.

## Interruption settings

Interruption settings control whether and how callers can interrupt your AI assistant while it is speaking. By default, interruptions are enabled — callers can barge in at any point. You can disable interruptions entirely, protect only the greeting from being cut off, or tune the endpointing thresholds that determine when the assistant treats caller speech as a complete turn.

### How it works

Interruption behavior depends on which transcription model your assistant uses.

**Turn-taking models** like `deepgram/flux` have built-in end-of-turn detection. When you use one of these models, the assistant determines when the caller has finished speaking using the transcription-level settings `eot_threshold`, `eot_timeout_ms`, and `eager_eot_threshold` — configured under `transcription.settings`. See the [Transcription Settings](transcription-settings.md) guide for details. You can still use `interruption_settings.enable` and `interruption_settings.disable_greeting_interruption` with turn-taking models, but the `start_speaking_plan` and `transcription_endpointing_plan` thresholds are not relevant because the model handles turn detection natively.

**Non turn-taking models** (such as `deepgram/nova-3`, `deepgram/nova-2`, `azure/fast`, or `nvidia/parakeet-v3`) do not have built-in turn detection. The assistant relies on the `interruption_settings.start_speaking_plan` to decide when to start speaking after the caller stops. This plan uses silence-based endpointing thresholds to detect end of turn.

### Configuration

Set the `interruption_settings` object when creating or updating an assistant:

```
curl -X POST https://api.telnyx.com/v2/ai/assistants \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Assistant",
    "model": "anthropic/claude-haiku-4-5",
    "instructions": "You are a helpful voice assistant.",
    "transcription": {
      "model": "deepgram/nova-3"
    },
    "interruption_settings": {
      "enable": true,
      "disable_greeting_interruption": true,
      "start_speaking_plan": {
        "wait_seconds": 0.4,
        "transcription_endpointing_plan": {
          "on_punctuation_seconds": 0.1,
          "on_no_punctuation_seconds": 1.5,
          "on_number_seconds": 0.5
        }
      }
    }
  }'
```

**Key fields**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `enable` | boolean | `true` | Whether callers can interrupt the assistant while it is speaking. |
| `disable_greeting_interruption` | boolean | — | When `true`, prevents callers from interrupting the assistant's greeting. |
| `start_speaking_plan.wait_seconds` | float | `0.4` | Minimum seconds to wait after the caller stops speaking before the assistant responds. |
| `start_speaking_plan.transcription_endpointing_plan.on_punctuation_seconds` | float | `0.1` | Seconds to wait after the transcript ends with punctuation before treating the turn as complete. |
| `start_speaking_plan.transcription_endpointing_plan.on_no_punctuation_seconds` | float | `1.5` | Seconds to wait after the transcript ends without punctuation before treating the turn as complete. |
| `start_speaking_plan.transcription_endpointing_plan.on_number_seconds` | float | `0.5` | Seconds to wait after the transcript ends with a number before treating the turn as complete. |

You can also configure interruption settings through the Mission Control Portal: navigate to **AI > Assistants**, select your assistant and click **Edit**, open the **Voice** tab, scroll to the **Interruption Settings** section, and toggle interruptions on or off, enable greeting protection, and adjust the start speaking plan thresholds.

### Example configurations

**Default — allow interruptions**

```
{
  "interruption_settings": {
    "enable": true
  }
}
```

**Protected greeting** — Allow interruptions during normal conversation but prevent callers from cutting off the assistant's initial greeting. Useful for flows where the greeting contains required disclosures or context.

```
{
  "interruption_settings": {
    "enable": true,
    "disable_greeting_interruption": true
  }
}
```

**Conservative endpointing for non turn-taking models** — Use longer silence thresholds to reduce false interruptions in noisy environments or when callers tend to pause mid-sentence.

```
{
  "interruption_settings": {
    "enable": true,
    "start_speaking_plan": {
      "wait_seconds": 0.8,
      "transcription_endpointing_plan": {
        "on_punctuation_seconds": 0.3,
        "on_no_punctuation_seconds": 2.0,
        "on_number_seconds": 1.0
      }
    }
  }
}
```

### Use cases

- **Call centers with background noise** — Increase `wait_seconds` and endpointing thresholds to prevent ambient noise from triggering false interruptions.
- **IVR-style interactions** — Keep interruptions enabled so callers can barge in to skip prompts they have already heard.
- **Greeting-heavy flows** — Enable `disable_greeting_interruption` to ensure callers hear required disclosures, legal notices, or welcome messages before interacting.
- **Dictation or number entry** — Increase `on_number_seconds` to give callers time to finish reading out long numbers like account IDs or phone numbers without the assistant cutting in.
