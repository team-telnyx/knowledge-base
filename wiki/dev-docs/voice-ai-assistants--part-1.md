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

*Part 1 of 6 — see also: [Part 2](voice-ai-assistants--part-2.md), [Part 3](voice-ai-assistants--part-3.md), [Part 4](voice-ai-assistants--part-4.md), [Part 5](voice-ai-assistants--part-5.md), [Part 6](voice-ai-assistants--part-6.md)*

Telnyx Voice AI Assistants let you build, configure, and operate conversational voice agents entirely from the Mission Control Portal or via API. This page covers the no-code quickstart, supported language and transcription models, voice and noise-suppression settings, built-in and library tools, integrations, scheduled outbound events with retries, and programmatic voice control.

## Overview

Telnyx Voice AI Assistants are configurable conversational agents that can answer phone calls, place outbound calls, send SMS, and integrate with enterprise systems. You can build them entirely in the [Mission Control Portal](https://portal.telnyx.com/#/ai/assistants) without writing code, or drive them programmatically through the Telnyx API. The platform supports multiple language models, transcription engines, and text-to-speech providers, and exposes a shared Tools Library so the same tool can be reused across many assistants.

## Quickstart: Build a No-Code Voice Assistant

The fastest path to a working voice assistant is the no-code flow in the portal. You will configure an AI Assistant, attach voice settings, optionally assign a phone number, and then test the call.

### Configure the AI Assistant

Navigate to the [AI Assistants tab](https://portal.telnyx.com/#/ai/assistants) and create a new assistant from a blank template. A minimal instruction set and greeting can be:

```
You are an intelligent and concise voice assistant. This is a {{telnyx_conversation_channel}} happening on {{telnyx_current_time}}. The agent is at {{telnyx_agent_target}} and the user is at {{telnyx_end_user_target}}.
```

```
Hi {{first_name}}, this is Nyx, your friendly Telnyx Assistant! How can I help you today?
```

Telnyx injects system variables into the prompt at call time:

| Variable | Description | Example |
| --- | --- | --- |
| `{{telnyx_current_time}}` | Current date and time in UTC | `Monday, February 24 2025 04:04:15 PM UTC` |
| `{{telnyx_conversation_channel}}` | `phone_call`, `web_call`, or `sms_chat` | `phone_call` |
| `{{telnyx_agent_target}}` | Phone number, SIP URI, or other identifier for the agent | `+13128675309` |
| `{{telnyx_end_user_target}}` | Phone number, SIP URI, or other identifier for the end user | `+13128675309` |
| `{{telnyx_sip_header_user_to_user}}` | User-to-User SIP header for the call, if applicable | `cmlkPTM0Nzg1O3A9dQ==;encoding=base64;purpose=call` |
| `{{telnyx_sip_header_diversion}}` | Diversion SIP header for the call, if applicable | `<sip:bob@example.com>;reason=user-busy` |
| `{{call_control_id}}` | Call control ID for the call, if applicable | `v3:u5OAKGEPT3Dx8SZSSDRWEMdNH2OripQhO` |

Timezone-aware variants (e.g. `{{telnyx_current_time_America/New_York}}`), shorthands (`{{telnyx_current_date}}`, `{{telnyx_current_weekday}}`), and a custom `date` format filter are also supported. See [Dynamic Variables](dynamic-variables.md) for the full list. You can also define your own custom dynamic variables and supply them via webhook, custom SIP headers, or an outbound API call.

By default the Hangup tool is enabled so the assistant can end the call at an appropriate time.

### Configure the voice settings

In the voice step you can accept the defaults and click **Create**, or explore the available providers:

- **TTS (Text-to-Speech):** Telnyx, AWS, Azure, ElevenLabs, Inworld. See [Text-to-Speech Available Voices](text-to-speech-available-voices.md) for the full list.
- **STT (Speech-to-Text):** Telnyx (Whisper), Deepgram, Azure, and others — see [Transcription Settings](transcription-settings.md) for model details.

[Ultra](/docs/voice/tts/providers/telnyx/ultra) and [xAI Grok](/docs/voice/tts/providers/telnyx/grok) voices support Expressive Mode with inline SSML emotion tags and nonverbal cues like `[laughter]`.

**Background audio** can be enabled to play during the call, making longer pauses from tool calls feel more natural. Choose from predefined options or supply a custom public URL.

**Speaking plan** controls when the agent starts talking. Four pause types are available:

1. **Wait seconds** — baseline delay before the agent speaks (e.g. `0.3s` for snappy customer service, `1.5s` for IVR systems).
2. **On punctuation seconds** — delay when the transcription ends with `.` or `?` (e.g. `0.1s` for minimal delay).
3. **On no punctuation seconds** — delay when the user trails off without punctuation (e.g. `1.5s` so the agent does not interrupt while the user reads digits).
4. **On number seconds** — delay tuned for digit sequences (e.g. `1.0s` to avoid cutting the user off mid-number).

**Noise suppression** reduces background noise and improves STT accuracy. Two engines are available through the assistant's `telephony_settings`:

| Engine | Description |
| --- | --- |
| **Krisp** | Industry-leading noise suppression effective across home offices, contact centers, and outdoor environments |
| **DeepFilterNet** | Configurable attenuation for fine-grained control |

For STT-optimized suppression, Telnyx also offers **AiCoustics**, which is applied per-call via the [Call Control API `suppression_start` action](/docs/voice/programmable-voice/noise-suppression) with `noise_suppression_engine: "AiCoustics"`. See the [Noise Suppression guide](/docs/voice/programmable-voice/noise-suppression) for the full engine list and configuration.

Enable noise suppression in the portal under voice settings, or via API:

```
curl -X POST https://api.telnyx.com/v2/ai/assistants/{assistant_id} \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "telephony_settings": {
      "noise_suppression": "krisp"
    }
  }'
```

Set to `"disabled"` to turn off noise suppression.

### Assign a phone number and test

If you already own a Telnyx number with voice features, you can assign it to the assistant immediately. Otherwise you can skip this step and still test the assistant in the portal.

Once the assistant is created, you can talk to it directly in the portal. If a number is assigned, you can also have the assistant call you from the portal, via API/CLI, or through an automated workflow such as Zapier using the TeXML Outbound Call action.

### Outbound calls via API

To initiate an outbound call with your AI assistant, use the `/v2/texml/ai_calls/` endpoint:

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

If the assistant has voicemail detection configured, include the AMD parameters:

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-6207ab25-b185-478f-b2ef-85159e226727",
      "MachineDetection": "Enable",
      "AsyncAmd": true,
      "DetectionMode": "Premium"
  }'
```

### Review the conversation

All historical conversations are available in the **Conversation History** tab.

## Supported Language Models

Telnyx AI Assistants support multiple language models. Select a model in the **Agent** tab when creating or editing an assistant.

| Model | Provider | Description |
| --- | --- | --- |
| `anthropic/claude-haiku-4-5` | Anthropic (native) | Fast, lightweight model — no API key required |
| `openai/gpt-5.4-mini` | OpenAI | Compact high-efficiency model for production voice workflows — requires OpenAI API key |
| `openai/gpt-4o` | OpenAI | Requires OpenAI API key |
| `moonshotai/Kimi-K2.5` | Telnyx (native) | Recommended balance of intelligence and cost |

Native models run on Telnyx infrastructure with no external API key required. For models from external providers, see the third-party integrations section below or [Custom LLMs for Assistants](custom-llms-for-assistants.md). For the complete list, see [Available Models](/docs/inference/models).
