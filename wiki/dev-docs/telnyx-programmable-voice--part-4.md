---
title: Telnyx Programmable Voice
summary: A consolidated reference for Telnyx Programmable Voice covering the Voice
  API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression,
  Transcription), Text-to-Speech providers, and the European regional endpoint.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
updated_at: 2026-08-05T14:05:29Z
---

# Telnyx Programmable Voice

*Part 4 of 5 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 2](telnyx-programmable-voice--part-2.md), [Part 3](telnyx-programmable-voice--part-3.md), [Part 5](telnyx-programmable-voice--part-5.md)*

A consolidated reference for Telnyx Programmable Voice covering the Voice API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression, Transcription), Text-to-Speech providers, and the European regional endpoint.

## Text-to-Speech

Telnyx supports multiple Text-to-Speech providers that can be invoked through the Voice API `speak` action or the TeXML `<Say>` verb.

### Telnyx Ultra

Telnyx Ultra is a next-generation text-to-speech engine delivering ultra-quality voice synthesis with low latency and support for 44 languages.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "voice": "Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41"
}'
```

```xml
<Response>
    <Say voice="Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41">The text that should be said on the call!</Say>
</Response>
```

### Telnyx Internal TTS (KokoroTTS)

Telnyx provides a high-quality, low-latency Text-to-Speech engine for real-time voice applications.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.KokoroTTS.af"
}'
```

```xml
<Response>
    <Say voice="Telnyx.KokoroTTS.af">The text that should be said on the call!</Say>
</Response>
```

### Telnyx Natural

Telnyx Natural voices provide enhanced speech quality with improved naturalness and clarity.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.Natural.abbie"
}'
```

```xml
<Response>
    <Say voice="Telnyx.Natural.abbie">The text that should be said on the call!</Say>
</Response>
```

### Telnyx NaturalHD

Telnyx NaturalHD voices deliver premium-quality speech synthesis with exceptional clarity and richness.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Telnyx.NaturalHD.andersen_johan"
}'
```

```xml
<Response>
    <Say voice="Telnyx.NaturalHD.andersen_johan">The text that should be said on the call!</Say>
</Response>
```

### AWS Polly

Telnyx offers both neural and standard quality levels for AWS Polly. The neural voice can be used by adding the `-Neural` suffix to the voice name (for example, `Polly.Amy-Neural`).

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Polly.Brian"
}'
```

```xml
<Response>
    <Say voice="Polly.Amy-Neural">The text that should be said on the call!</Say>
</Response>
```

### Azure AI Speech

Azure AI Speech supports two service levels via Telnyx:

- **Neural** — Deep neural network voices with high-quality output and SSML support. Example: `Azure.en-CA-ClaraNeural`.
- **Neural HD (High Definition)** — Enhanced clarity and richness with finer prosody control. Example: `en-US-Emma:DragonHDLatestNeural`.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Azure.en-CA-ClaraNeural"
}'
```

```xml
<Response>
    <Say voice="Azure.en-CA-ClaraNeural">The text that should be said on the call!</Say>
</Response>
```

### ElevenLabs

ElevenLabs offers many voice options but response latency may exceed AWS Polly or Azure AI Speech. An ElevenLabs API key must be stored as a Telnyx integration secret. Only premium ElevenLabs accounts are supported.

```bash
curl --location 'https://api.telnyx.com/v2/integration_secrets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "identifier":"your_api_key_ref",
    "value":"api_key"
}'
```

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should said on the call",
    "voice": "ElevenLabs.Default.cgSgspJ2msm6clMCkdW9",
    "voice_settings": {"api_key_ref": "your_api_key_ref"}
}'
```

```xml
<Response>
    <Say voice="ElevenLabs.Default.cgSgspJ2msm6clMCkdW9" api_key_ref="your_api_key_ref">The text that should said on the call!</Say>
</Response>
```

### MiniMax

MiniMax offers high-quality text-to-speech with expressive voices across multiple languages and accents.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Minimax.speech-2.6-turbo.English_expressive_narrator"
}'
```

```xml
<Response>
    <Say voice="Minimax.speech-2.6-turbo.English_expressive_narrator">The text that should be said on the call!</Say>
</Response>
```

### ResembleAI

ResembleAI voices are built on the Chatterbox model and preserve emotion, style, and accent.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Resemble.Pro.Aaron_en-US"
}'
```

```xml
<Response>
    <Say voice="Resemble.Pro.Aaron_en-US">The text that should be said on the call!</Say>
</Response>
```

### Inworld

Inworld offers expressive multilingual AI voices across three models: Mini, Max, and TTS2.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Inworld.Mini.Loretta"
}'
```

```xml
<Response>
    <Say voice="Inworld.Mini.Loretta">The text that should be said on the call!</Say>
</Response>
```

### Rime

Rime offers two TTS models through Telnyx:

- **Coda** (recommended) — Rime's flagship model with sub-100ms latency, 184 voices, and support for English, Spanish, French, Portuguese, German, and Japanese. Voices use the `Rime.Coda.<VoiceId>` format.
- **ArcanaV3** — Previous flagship with multilingual codeswitching across 10 languages: Arabic, English, French, German, Hebrew, Hindi, Japanese, Portuguese, Spanish, and Tamil. Voices use the `Rime.ArcanaV3.<VoiceId>` format.

```bash
curl --location 'https://api.telnyx.com/v2/calls/v3:6MytEd1c56mFmXlAziof4tQd-eqOgwQqpFAvECu1gBRrvD5rmsclfg/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
    "payload": "The text that should be said on the call",
    "voice": "Rime.Coda.cove"
}'
```

```xml
<Response>
    <Say voice="Rime.Coda.cove">The text that should be said on the call!</Say>
</Response>
```
