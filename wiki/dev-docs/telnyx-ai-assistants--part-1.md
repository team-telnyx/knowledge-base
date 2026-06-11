---
title: Telnyx AI Assistants
summary: Telnyx AI Assistants are configurable voice and chat agents that combine
  large language models, text-to-speech, speech-to-text, and real-time tools into
  a single no-code or API-driven platform. Assistants can handle inbound and outbound
  calls, multi-participant conversations, scheduled outreach, structured conversation
  workflows, and integrations with enterprise systems — all managed from the Mission
  Control Portal or the Assistants API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
  content_hash: 1ae007d98f0a079c6d9fa1acec7fd9203c2af7ca66d212171ca711e3da94d0c7
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
  content_hash: d07570a4fd30575a9f261a3f4988a2208d3115a79d4b0278f337f6a791606a6b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
  content_hash: dc746a7ef6ef062d69a462a97a0c854a29da9576afc690ef62164b2ffecfcaf8
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
  content_hash: 97d3c9a314e001171d8cdac0f6a5707f088237e0e32561470fc8a92acbfdf55c
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
  content_hash: 155c354770eb16a9fe21e6eb194f7391f2ece82729736cef4540e5a28ee21ca4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
  content_hash: 1ea79c8dd0f948970ff36ae3e9de9dd2efaf764f85c57429bb3366a97a0eb55b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
  content_hash: 1a351e40f03eb9e9387cc17956573eb2a3423d73dde019f2ec3879f1bcc72dd1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
  content_hash: 69f833223aa236218e653b4f8fd0f4a0cd8aa0aecf5872dfe647ef741dca081f
updated_at: 2026-06-11T10:30:28Z
---

# Telnyx AI Assistants

*Part 1 of 4 — see also: [Part 2](telnyx-ai-assistants--part-2.md), [Part 3](telnyx-ai-assistants--part-3.md), [Part 4](telnyx-ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and chat agents that combine large language models, text-to-speech, speech-to-text, and real-time tools into a single no-code or API-driven platform. Assistants can handle inbound and outbound calls, multi-participant conversations, scheduled outreach, structured conversation workflows, and integrations with enterprise systems — all managed from the Mission Control Portal or the Assistants API.

## Getting Started

Create a voice assistant in under five minutes from the [Mission Control Portal](https://portal.telnyx.com/#/ai/assistants) without writing code. Start by selecting a blank or prebuilt template, then configure the assistant's instructions and greeting. A default Hangup tool is included so the assistant can end calls at the right time.

Instructions and greetings support system dynamic variables such as `{{telnyx_current_time}}`, `{{telnyx_conversation_channel}}`, `{{telnyx_agent_target}}`, `{{telnyx_end_user_target}}`, and `{{call_control_id}}`, as well as timezone-aware variants (e.g. `{{telnyx_current_time_America/New_York}}`) and custom variables set via webhook, custom SIP headers, or an outbound API call. See [Dynamic Variables](dynamic-variables.md) for the full list.

After configuring the agent, set up voice settings (TTS and STT providers), optionally assign a phone number, enable messaging, and test the assistant by calling in or placing an outbound call.

### Outbound calls via API

Initiate an outbound call with the `/v2/texml/ai_calls/` endpoint:

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-6207ab25-b185-478f-b2ef-85159e226727"
  }'
```

If the assistant has voicemail detection configured, include `MachineDetection`, `AsyncAmd`, and `DetectionMode` parameters in the request.

### Supported language models

| Model | Provider | Notes |
|---|---|---|
| `anthropic/claude-haiku-4-5` | Anthropic (native) | No external API key required |
| `openai/gpt-4o` | OpenAI | Requires OpenAI API key |
| `moonshotai/Kimi-K2.5` | Telnyx (native) | Recommended balance of intelligence and cost |

For a complete list see the [Available Models](https://developers.telnyx.com/docs/inference/models) page. Native models run on Telnyx infrastructure with no external API key. Third-party LLM and TTS providers (OpenAI, ElevenLabs, Vapi) can also be integrated — see the relevant integration sections below.

## Voice and Transcription Settings

### Text-to-speech

TTS providers include Telnyx, AWS, Azure, ElevenLabs, and Inworld. Ultra and xAI Grok voices support Expressive Mode with inline SSML emotion tags and nonverbal cues like `[laughter]`. Browse available voices on the [Text-to-Speech Available Voices](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index) page.

### Speaking plan

Control when the agent starts talking with four pause types:

1. **Wait seconds** — baseline silence before responding (e.g. 0.3 s for snappy responses, 1.5 s for IVR navigation).
2. **On punctuation seconds** — delay after a confident endpoint (period, question mark).
3. **On no punctuation seconds** — delay after an uncertain endpoint (e.g. the user paused mid-sentence).
4. **On number seconds** — delay after a digit sequence to avoid cutting off slow number reading.

### Background audio

Configure background audio to play during calls for a more realistic noise environment. Select from predefined options or provide a custom public URL.

### Noise suppression

Enable noise suppression to improve STT accuracy. Two engines are available:

| Engine | Description |
|---|---|
| **Krisp** | Industry-leading noise suppression across diverse environments |
| **DeepFilterNet** | Configurable attenuation for fine-grained control |

Enable via the Portal under voice settings, or via the API by setting `noise_suppression` in `telephony_settings` (e.g. `"krisp"` or `"disabled"`).

### Transcription models

| Model | Engine | Best for |
|---|---|---|
| `deepgram/flux` | Deepgram | Conversational AI, optimized turn-taking, multilingual |
| `deepgram/nova-3` | Deepgram | Fast multilingual transcription |
| `deepgram/nova-2` | Deepgram | Previous-generation fast multilingual |
| `azure/fast` | Azure | Fast multilingual with optional region and API key |
| `assemblyai/universal-streaming` | AssemblyAI | Conversational streaming with configurable turn detection |
| `xai/grok-stt` | xAI | Multilingual transcription via Grok STT |

Select a model in the Portal under the **Voice** tab, or set `transcription.model` via the API.

#### Deepgram Flux end-of-turn detection

`deepgram/flux` provides end-of-turn detection and eager end-of-turn (speculative LLM processing before the caller fully stops speaking).

| Field | Range | Default | Description |
|---|---|---|---|
| `eot_threshold` | 0.5–0.9 | 0.8 | Confidence to trigger final end of turn |
| `eot_timeout_ms` | 500–10000 | 5000 | Max silence (ms) before forcing end of turn |
| `eager_eot_threshold` | 0.3–0.9 | 0.4 | Confidence to start speculative LLM processing |

`eager_eot_threshold` must be ≤ `eot_threshold`. Setting both to the same value effectively disables eager end-of-turn.

#### Keyterm boost

`deepgram/flux` and `deepgram/nova-3` support `keyterm` — a comma-separated list of terms to boost during recognition (product names, acronyms, participant names). Keyterm boost also supports dynamic variables:

```json
"transcription": {
  "model": "deepgram/nova-3",
  "settings": {
    "keyterm": "Telnyx,VoIP,SIP,{{customer_name}},{{product_name}}"
  }
}
```

#### AssemblyAI settings

`assemblyai/universal-streaming` supports configurable turn detection:

| Field | Range | Default |
|---|---|---|
| `end_of_turn_confidence_threshold` | 0–1 | 0.4 |
| `min_turn_silence` | 100–5000 | 400 |
| `max_turn_silence` | 100–5000 | 1280 |

#### Azure settings

`azure/fast` supports region selection (defaults to `latency` for auto-selection of the closest Telnyx-managed region) and an optional `api_key_ref` for your own Azure API key.

### MMS integration during voice calls

Assistants can receive and process MMS messages during live voice calls for visual context and real-time image analysis. Requirements:

- Messaging must be enabled on the assistant.
- A vision-capable model must be selected: `Groq/llama-4-maverick-17b-128e-instruct` or `OpenAI/gpt-4o`.
- Common image formats (JPEG, PNG, etc.) are supported.

Use cases include customer service (product photos), technical support (error screenshots), insurance claims, identity verification, quality control, and damage assessment.
