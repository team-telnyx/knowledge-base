---
title: Voice AI Assistants
summary: Telnyx Voice AI Assistants let you build, configure, and operate conversational
  voice agents entirely from the Mission Control Portal or via API. This page covers
  the no-code quickstart, supported language and transcription models, voice and noise-suppression
  settings, built-in and library tools, integrations, scheduled outbound events with
  retries, and programmatic voice control.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
updated_at: 2026-08-05T13:45:11Z
---

# Voice AI Assistants

*Part 2 of 6 — see also: [Part 1](voice-ai-assistants--part-1.md), [Part 3](voice-ai-assistants--part-3.md), [Part 4](voice-ai-assistants--part-4.md), [Part 5](voice-ai-assistants--part-5.md), [Part 6](voice-ai-assistants--part-6.md)*

Telnyx Voice AI Assistants let you build, configure, and operate conversational voice agents entirely from the Mission Control Portal or via API. This page covers the no-code quickstart, supported language and transcription models, voice and noise-suppression settings, built-in and library tools, integrations, scheduled outbound events with retries, and programmatic voice control.

## Transcription Settings

Telnyx AI Assistants support multiple speech-to-text (STT) models. The model you choose affects transcription accuracy, supported languages, and response latency. You can also tune provider-specific behavior such as end-of-turn detection, formatting, keyterm boosting, and Azure region selection.

### Available models

| Model | Engine | Best for |
| --- | --- | --- |
| `deepgram/flux` | Deepgram | Conversational AI, optimized for turn-taking with multilingual support |
| `deepgram/nova-3` | Deepgram | Fast multilingual transcription, recommended for multilingual assistants |
| `deepgram/nova-2` | Deepgram | Fast multilingual transcription on Deepgram's previous-generation model |
| `azure/fast` | Azure | Fast multilingual transcription with optional Azure region and API key configuration |
| `assemblyai/universal-streaming` | AssemblyAI | Conversational, multilingual streaming transcription with configurable turn detection, backed by Universal-3.5 Pro Realtime |
| `xai/grok-stt` | xAI | Multilingual transcription using Grok STT |
| `nvidia/parakeet-v3` | Parakeet | Multilingual transcription with automatic language detection |
| `reson8/turns` | Reson8 | Turn-based transcription of 10 European languages with automatic language detection |

`deepgram/flux` supports English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch. For broader language coverage, use `deepgram/nova-3`, `deepgram/nova-2`, `azure/fast`, `assemblyai/universal-streaming`, `xai/grok-stt`, `nvidia/parakeet-v3`, or `reson8/turns`.

### Selecting a model

In the [AI Assistants tab](https://portal.telnyx.com/#/ai/assistants), edit your assistant and open the **Voice** tab. Choose your STT model from the **Transcription Model** dropdown. When you change models in the Portal, related settings reset to the provider defaults:

- `deepgram/flux` supports explicit languages, `auto`, and `multi` for its supported languages, and applies Flux end-of-turn defaults.
- Other Deepgram models enable `smart_format` and `numerals` by default.
- `assemblyai/universal-streaming` applies AssemblyAI turn detection defaults.
- `azure/fast` defaults the Azure region to `latency`, which auto-selects the closest supported Telnyx-managed region.
- `nvidia/parakeet-v3` uses automatic multilingual transcription.
- `reson8/turns` defaults the language to `auto` for automatic detection.

Via API, set the `transcription.model` field when creating or updating an assistant:

```
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

You can also set the transcription language explicitly. If omitted or set to `auto`, supported models auto-detect the language:

```
"transcription": {
  "model": "deepgram/nova-3",
  "language": "es"
}
```

### Languages

| Model | Language behavior |
| --- | --- |
| `deepgram/flux` | English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, Dutch, plus `auto` and `multi` modes |
| `deepgram/nova-3` | Auto-detect plus supported Deepgram Nova 3 language codes |
| `deepgram/nova-2` | Auto-detect plus supported Deepgram Nova 2 language codes |
| `azure/fast` | Explicit Azure locale codes, such as `en-US`, `es-MX`, or `fr-FR` |
| `assemblyai/universal-streaming` | `auto` for multilingual detection, or one of 18 supported languages: `en`, `es`, `de`, `fr`, `pt`, `it`, `tr`, `nl`, `sv`, `no`, `da`, `fi`, `hi`, `vi`, `ar`, `he`, `ja`, `zh` |
| `xai/grok-stt` | `auto` plus supported Grok STT language codes |
| `nvidia/parakeet-v3` | Automatic multilingual detection |
| `reson8/turns` | `auto` (default) for automatic detection, or one of `nl`, `en`, `fr`, `fy`, `de`, `it`, `pl`, `pt`, `es`, `sv` |

If your assistant has a language filter set elsewhere in the Voice tab, the Portal only shows transcription models and language choices that are compatible with that language.

### Deepgram settings

**Flux end-of-turn detection.** `deepgram/flux` is optimized for live voice agents and provides end-of-turn detection so the assistant can start responding as soon as the caller finishes speaking. It also supports eager end-of-turn, which starts LLM processing before the caller fully stops speaking to reduce perceived latency. Portal defaults:

| Field | Type | Range | Portal default | Description |
| --- | --- | --- | --- | --- |
| `eot_threshold` | number | 0.5-0.9 | 0.8 | Confidence required to trigger a final end of turn. Higher values require more confidence and may add latency. |
| `eot_timeout_ms` | integer | 500-10000 | 5000 | Maximum silence duration, in milliseconds, before forcing an end of turn. |
| `eager_eot_threshold` | number | 0.3-0.9 | 0.4 | Confidence required to start speculative LLM processing before final end-of-turn confirmation. Lower values trigger earlier. |

`eager_eot_threshold` must be less than or equal to `eot_threshold`. Setting both to the same value effectively disables eager end-of-turn behavior. The `eager_eot_threshold` field is controlled by the `FE-eager-eot-threshold` Portal feature flag; when disabled, the Portal hides the field but API payloads can still include it if your account supports the setting.

When using Flux, the Portal may prompt you to lower the assistant's start speaking plan timings. Flux works best with low start speaking delays, such as `0.1` seconds for wait time and endpointing plan thresholds.

**Keyterm Boost.** `deepgram/flux` and `deepgram/nova-3` support `keyterm`, a comma-separated list of terms to boost during recognition. Use it for product names, customer names, acronyms, or domain-specific vocabulary. Keyterm Boost also supports [Dynamic Variables](dynamic-variables.md) for caller-specific terms:

```
"transcription": {
  "model": "deepgram/nova-3",
  "settings": {
    "keyterm": "Telnyx,VoIP,SIP,{{customer_name}},{{product_name}}"
  }
}
```

**Smart Format and Numerals.** For Deepgram models other than Flux, the Portal exposes these settings and enables both by default:

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `smart_format` | boolean | `true` | Automatically formats transcripts for readability, including punctuation and casing. |
| `numerals` | boolean | `true` | Converts spoken numbers to digits, for example "five hundred" to "500". |

### AssemblyAI settings

`assemblyai/universal-streaming` supports configurable turn detection. Portal defaults:

| Field | Type | Range | Portal default | Description |
| --- | --- | --- | --- | --- |
| `end_of_turn_confidence_threshold` | number | 0-1 | 0.4 | Confidence required to trigger an end of turn. Higher values require more certainty before ending a turn. |
| `min_turn_silence` | integer | 100-5000 | 400 | Minimum silence duration, in milliseconds, before a turn can end. |
| `max_turn_silence` | integer | 100-5000 | 1280 | Maximum silence duration, in milliseconds, before forcing an end of turn. |

`min_turn_silence` must be less than or equal to `max_turn_silence`.

```
"transcription": {
  "model": "assemblyai/universal-streaming",
  "language": "auto",
  "settings": {
    "end_of_turn_confidence_threshold": 0.4,
    "min_turn_silence": 400,
    "max_turn_silence": 1280
  }
}
```

### Parakeet settings

`nvidia/parakeet-v3` supports multilingual transcription with automatic language detection and does not require provider-specific settings:

```
"transcription": {
  "model": "nvidia/parakeet-v3",
  "language": "auto"
}
```

### Reson8 settings

`reson8/turns` delivers transcripts per turn of speech: the assistant receives the full transcript of a turn when the caller finishes speaking. Language defaults to `auto` for automatic detection and can be fixed to one of the 10 supported languages. It does not require provider-specific settings:

```
"transcription": {
  "model": "reson8/turns",
  "language": "auto"
}
```

### Azure settings

`azure/fast` supports region selection and an optional Azure API key reference.

| Field | Type | Description |
| --- | --- | --- |
| `region` | string | Azure transcription region. The Portal defaults to `latency`, which auto-selects the closest supported Telnyx-managed region. |
| `api_key_ref` | string | Optional integration secret reference for your Azure API key. When provided, the Portal only shows regions that support custom API keys. |

Common Telnyx-managed regions include `latency`, `australiaeast`, `centralindia`, `eastus`, `northcentralus`, `westeurope`, and `westus2`. Additional Azure regions are available when using your own Azure API key.

```
"transcription": {
  "model": "azure/fast",
  "language": "en-US",
  "region": "latency"
}
```

### Configure advanced settings via API

```
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
        "eot_threshold": 0.8,
        "eot_timeout_ms": 5000,
        "eager_eot_threshold": 0.4,
        "keyterm": "Telnyx,VoIP,SIP,{{customer_name}},{{product_name}}"
      }
    }
  }'
```
