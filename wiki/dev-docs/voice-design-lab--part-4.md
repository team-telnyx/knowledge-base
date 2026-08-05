---
title: Voice Design Lab
summary: 'The Voice Design Lab lets you create custom voices for text-to-speech in
  two ways: by describing a voice in natural language (Design a Voice) or by cloning
  from an audio sample (Clone from Audio). Both flows produce a production-ready voice
  clone that can be used across AI Assistants, Call Control, and the TTS API.'
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
updated_at: 2026-08-05T14:07:47Z
---

# Voice Design Lab

*Part 4 of 4 — see also: [Part 1](voice-design-lab--part-1.md), [Part 2](voice-design-lab--part-2.md), [Part 3](voice-design-lab--part-3.md)*

The Voice Design Lab lets you create custom voices for text-to-speech in two ways: by describing a voice in natural language (Design a Voice) or by cloning from an audio sample (Clone from Audio). Both flows produce a production-ready voice clone that can be used across AI Assistants, Call Control, and the TTS API.

## Using Custom Voices

Every voice clone gets a unique voice ID: `{Provider}.{Model}.{voice_id}`

- **Telnyx:** `Telnyx.Qwen3TTS.33226e69-3abd-429b-b64a-86775c9b5850`
- **Minimax:** `Minimax.speech-2.8-turbo.TB4ZMVKanThGeldiw8rLBEg21v4ifjUTRgLpkodJxpMYV`

Find it in the Voice Design by clicking on any saved voice, or build it from the clone response's `provider`, `provider_supported_models`, and `provider_voice_id` fields.

### AI Assistants

Select your custom voice in the assistant's voice settings. Telnyx clones appear under **Telnyx / Qwen3TTS**, Minimax clones under **Minimax**.

### Call Control

Pass the voice ID in the `voice` field of the `speak` command.

### TTS WebSocket

Pass the voice ID as the `voice` query parameter on the WebSocket URL. See the [TTS streaming guide](https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming) for the full connection flow.
