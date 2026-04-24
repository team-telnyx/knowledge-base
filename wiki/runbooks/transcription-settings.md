---
title: Transcription Settings
summary: Choose and configure speech-to-text (STT) models for AI Assistants, including Deepgram Flux eager end-of-turn for reduced response latency.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings/index
    content_hash: bb1b011162b23b5b2d121e8f44e934bcb2c1f8a2f0b5dd6ceb5c83289b71a40e
updated_at: 2026-04-10T00:00:00Z
---

# Transcription Settings

Choose and configure speech-to-text (STT) models for AI Assistants, including Deepgram Flux eager end-of-turn for reduced response latency.

Telnyx AI Assistants support multiple speech-to-text (STT) models for transcribing caller audio. The model you choose affects transcription accuracy, supported languages, and response latency. You can also fine-tune transcription behavior through settings like eager end-of-turn detection.

***

## Available models

| Model                            | Engine   | Best for                                                                |
| -------------------------------- | -------- | ----------------------------------------------------------------------- |
| `distil-whisper/distil-large-v2` | Telnyx   | Default — good accuracy, runs on Telnyx infrastructure                  |
| `openai/whisper-large-v3-turbo`  | Telnyx   | High accuracy, larger model, multilingual support                       |
| `deepgram/flux`                  | Deepgram | Conversational AI — optimized for turn-taking, English only             |
| `deepgram/nova-3`                | Deepgram | Multilingual with automatic language detection, slightly higher latency |
| `deepgram/nova-2`                | Deepgram | Legacy — stable, cost-effective                                         |
| `azure/fast`                     | Azure    | Fast transcription with multilingual support                            |

> **Note:** `deepgram/flux` is English-only. For multilingual use cases, use `deepgram/nova-3`, `openai/whisper-large-v3-turbo`, or `azure/fast`.

***

## Selecting a model

### Portal

In the [AI Assistants tab](https://portal.telnyx.com/#/ai/assistants), edit your assistant and navigate to the **Voice** tab. Select your preferred STT model from the **Transcription Model** dropdown.

<img alt="AI Assistant Transcription Model Selection" />

### API

Set the `transcription.model` field when creating or updating an assistant:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/ai/assistants \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Assistant",
    "model": "anthropic/claude-haiku-4-5",
    "instructions": "You are a helpful voice assistant.",
    "transcription": {
      "model": "deepgram/flux"
    }
  }'
```

You can also set the transcription language explicitly. If omitted or set to `auto`, the model auto-detects the language:

```json theme={null}
"transcription": {
  "model": "deepgram/nova-3",
  "language": "es"
}
```

***

## Eager end-of-turn (Deepgram Flux)

Eager end-of-turn detection is a latency optimization available exclusively with `deepgram/flux`. It starts large language model (LLM) processing *before* the caller fully stops speaking, reducing perceived response time by \~150 ms on average.

**Eager end-of-turn is enabled by default** when using `deepgram/flux`. The `eager_eot_threshold` defaults to `0.3`, meaning the system aggressively begins speculative processing at the earliest sign of a turn ending.

### How it works

1. **EagerEndOfTurn** — The transcription model detects a likely pause. The system begins generating an LLM response speculatively.
2. **TurnResumed** — If the caller continues speaking, the speculative response is discarded and transcription continues.
3. **EndOfTurn** — When the caller definitively finishes, the final (or already-prepared) response plays back.

Because the LLM starts processing early, the response is often ready the moment the caller stops — eliminating the wait that normally occurs between end-of-speech and response playback.

### Parameters

These settings are available under `transcription.settings` and apply only to `deepgram/flux`:

| Field                 | Type    | Range   | Default | Description                                                                                                  |
| --------------------- | ------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------ |
| `eager_eot_threshold` | number  | 0.3–0.9 | 0.3     | Confidence level to start speculative LLM processing. Lower values trigger earlier.                          |
| `eot_threshold`       | number  | —       | —       | Confidence level for final end-of-turn confirmation. Must be greater than or equal to `eager_eot_threshold`. |
| `eot_timeout_ms`      | integer | —       | —       | Maximum silence duration (ms) before forcing an end-of-turn.                                                 |

The following settings apply to all Deepgram models:

| Field          | Type    | Default | Description                                                       |
| -------------- | ------- | ------- | ----------------------------------------------------------------- |
| `smart_format` | boolean | —       | Enables automatic punctuation, casing, and formatting.            |
| `numerals`     | boolean | —       | Converts spoken numbers to digits (e.g., "five hundred" → "500"). |

### Trade-offs

**Lower `eager_eot_threshold` (e.g., 0.3)**

* Faster perceived responses — the LLM starts earlier
* More speculative LLM calls (50–70% increase) — some will be discarded when the caller continues speaking
* Best for: latency-sensitive applications like customer service bots

**Higher `eager_eot_threshold` (e.g., 0.7)**

* Fewer wasted LLM calls — triggers only on high-confidence pauses
* Slightly higher response latency
* Best for: cost-sensitive applications or conversations with frequent mid-sentence pauses

**Disabling eager end-of-turn:** Set `eager_eot_threshold` equal to `eot_threshold`. When both thresholds match, the system waits for full end-of-turn confirmation before starting LLM processing.

### Tuning recommendations

**Latency-sensitive (customer service, IVR)**

    Use the defaults — `eager_eot_threshold: 0.3` provides the fastest response times. Accept the higher LLM call volume as a trade-off for responsiveness.

    ```json theme={null}
    "transcription": {
      "model": "deepgram/flux",
      "settings": {
        "eager_eot_threshold": 0.3
      }
    }
    ```

---

**Balanced (general-purpose assistants)**

    Raise the eager threshold slightly to reduce speculative calls while still getting a latency benefit.

    ```json theme={null}
    "transcription": {
      "model": "deepgram/flux",
      "settings": {
        "eager_eot_threshold": 0.5
      }
    }
    ```

---

**Accuracy-sensitive (dictation, long-form input)**

    Disable eager end-of-turn by matching both thresholds. This avoids any speculative processing.

    ```json theme={null}
    "transcription": {
      "model": "deepgram/flux",
      "settings": {
        "eager_eot_threshold": 0.7,
        "eot_threshold": 0.7
      }
    }
    ```

---

### Configure via API

Create an assistant with tuned transcription settings:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/ai/assistants \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Low Latency Assistant",
    "model": "anthropic/claude-haiku-4-5",
    "instructions": "You are a helpful voice assistant.",
    "transcription": {
      "model": "deepgram/flux",
      "language": "en",
      "settings": {
        "eager_eot_threshold": 0.3,
        "eot_threshold": 0.7,
        "eot_timeout_ms": 5000,
        "smart_format": true,
        "numerals": true
      }
    }
  }'
```

***

## Related resources

* [Create an Assistant — API Reference](https://developers.telnyx.com/api-reference/assistants/create-an-assistant)
* [Voice Assistant quickstart](voice-assistant-quickstart.md)
* [STT WebSocket Streaming](https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming)


## Related Pages

- [Transcription](../runbooks/transcription.md)
- [Number Reputation Settings](../runbooks/number-reputation-settings.md)
- [In-Call Transcription](../runbooks/in-call-transcription.md)
