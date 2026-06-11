---
title: Real-time STT and TTS WebSockets with Telnyx (plus Ultra Voices)
summary: Build low‑latency, real-time voice apps on Telnyx using WebSocket streaming
  for Speech‑to‑Text and Text‑to‑Speech, and level up naturalness with Telnyx Ultra
  voices, expressive SSML emotions, and a broad voices catalog.
sources:
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
updated_at: 2026-05-20T09:30:18Z
---

# Real-time STT and TTS WebSockets with Telnyx (plus Ultra Voices)

Build low‑latency, real-time voice apps on Telnyx using WebSocket streaming for Speech‑to‑Text and Text‑to‑Speech, and level up naturalness with Telnyx Ultra voices, expressive SSML emotions, and a broad voices catalog.

## Capabilities at a glance
- Speech-to-Text (STT) WebSocket streaming: send audio frames, receive incremental transcripts for live experiences.
- Text-to-Speech (TTS) WebSocket streaming: send text frames, receive incremental MP3 audio for real-time playback.
- Telnyx Ultra voices: sub‑100ms time to first byte, expressive delivery with SSML emotion tags, nonverbal cues like [laughter], and 36-language support.
- Broad voices catalog: Telnyx Natural, NaturalHD, Ultra, plus third‑party providers; choose per interaction to balance quality and cost.

## Authentication and endpoints
- Use a Telnyx API key in the Authorization header: `Authorization: Bearer YOUR_API_KEY`.
- STT endpoint: `wss://api.telnyx.com/v2/speech-to-text/transcription`
  - Query params:
    - `transcription_engine` (optional): e.g., Telnyx, Google, Deepgram, Azure.
    - `input_format` (optional): e.g., mp3, wav.
- TTS endpoint: `wss://api.telnyx.com/v2/text-to-speech/speech?voice={voice_id}`
  - Query params:
    - `voice` (required): voice identifier, e.g., `Telnyx.NaturalHD.astra` or `Telnyx.Ultra.<voice_id>`.
    - `inactivity_timeout` (optional): seconds to keep the socket open without messages (default 20).

## STT streaming flow
- Open a secure WebSocket with Authorization header.
- Send binary audio frames (e.g., 2KB chunks) as you capture or read audio.
- Receive JSON messages with transcription results as you stream.
- After sending all audio, wait briefly to collect final results before closing (e.g., ~20s grace period).

Flow (conceptual):
```
Client                                   Server
  |------- Connect ---------------------->|
  |<------ Connected ---------------------|
  |------- Audio Frame (Binary) --------->|
  |<------ Transcript (JSON) -------------|  {"transcript": "Hello", ...}
  |------- Disconnect ------------------->|
  |<------ Close -------------------------|
```

Typical transcript fields:
- `transcript`: text content
- `is_final`: boolean signaling end of an utterance
- `confidence`: numeric confidence score
- `error`: present on failures

Client prerequisites (example):
- Python 3.8+ and `websockets` (`pip install websockets`).

## Supported STT engines and input formats
- Engines: Telnyx (low latency, high accuracy), Google (interim results support), Deepgram (models like `nova-2`, `nova-3`, `flux` via `transcription_model` setting), Azure (broad language/accents).
- Input formats: set `input_format` (e.g., `mp3`, `wav`) to match your stream.

## TTS streaming flow
Lifecycle:
1) Connect with Authorization
2) Initialize: send a frame containing a single space in `text` (e.g., `{ "text": " " }`)
3) Send one or more text frames (e.g., `{ "text": "Hello" }`)
4) Receive audio frames incrementally (base64-encoded MP3)
5) Stop: send an empty text frame to finish (e.g., `{ "text": "" }`)
6) Close after processing completes

Flow (conceptual):
```
Client                          Server
  |------- Connect ------------>|
  |<------ Connected -----------|
  |------- Init  (" ") -------->|
  |------- Text ("Hello") ----->|
  |<------ Audio (base64 mp3) ---  ×N
  |------- Stop ("") ---------->|
  |<------ Close  --------------|
```

## TTS frame semantics and audio handling
Outbound (client → server):
- Initialization frame: `{ "text": " " }` (must be first)
- Text frame(s): `{ "text": "Your text here" }` (send multiple as needed)
- Stop frame: `{ "text": "" }` (signals completion)

Inbound (server → client):
- Audio frames: `{ "audio": "<base64>" }`
  - Decode base64 and append bytes to an MP3 file in order received.
  - Each chunk is a complete MP3 segment with headers; simple concatenation via append is expected.
  - Audio specs: MP3, 16 kHz, 16-bit, mono.

## Choosing and configuring voices
- Provide `voice` in the TTS URL, e.g., `Telnyx.NaturalHD.astra` or `Telnyx.Ultra.<voice_id>`.
- Explore options and providers in [Text-to-Speech voices catalog](text-to-speech-voices-catalog.md) (Telnyx Natural/NaturalHD/Ultra + xAI Grok, AWS Polly, Azure, ElevenLabs, Inworld, MiniMax, ResembleAI, Rime). Mix providers/models per use case.
- For advanced TTS configuration with telephony (speak commands), see the Telnyx Voice API Text‑to‑Speech guide.

## Telnyx Ultra Voices features
- Sub‑100ms time to first byte for highly responsive experiences (vs. ~200–300ms typical for Natural/NaturalHD).
- Expressive delivery with SSML emotion tags; automatic emotional interpretation in live AI assistant scenarios.
- Natural nonverbal cues like `[laughter]`.
- 36 languages supported.
- Voice ID format: `Telnyx.Ultra.<voice_id>` (browse in [Text-to-Speech voices catalog](text-to-speech-voices-catalog.md)).

Enable expressive mode with AI Assistants:
- In Portal: Assistant → Voice Settings → choose a Telnyx Ultra voice → toggle Expressive Mode → Save.
- Via API (example):
```bash
curl -X PATCH "https://api.telnyx.com/v2/ai/assistants/YOUR_ASSISTANT_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "voice_settings": {
      "voice": "Telnyx.Ultra.YOUR_VOICE_ID",
      "expressive_mode": true
    }
  }'
```
Notes:
- `expressive_mode` is only valid for voices starting with `Telnyx.Ultra.`; using it with non‑Ultra voices returns a validation error.

## SSML emotions, nonverbals, and pauses
- Emotions format: `<emotion value="EMOTION" />Your text here.`
- Primary emotions (best quality): `angry`, `excited`, `content`, `sad`, `scared`.
- Additional options include: `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`, and more.
- Nonverbalisms: insert `[laughter]` inline for natural laughing.
- Pauses: use `<break time="0.2s"/>` (start with ~0.2–0.3s and tune by ear).
- Omit tags for neutral delivery; use explicit tags sparingly for emphasis or clarity.

## Language support for Ultra
- 36 languages supported via `language_boost` in assistant voice settings: Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Vietnamese.

## Troubleshooting and tips
STT
- Ensure `Authorization: Bearer <API_KEY>` is sent on connect.
- Stream audio as binary frames; match `input_format` to your source.
- After sending all audio, wait several seconds for final transcripts before closing.
- Listen for `error` fields in server messages.

TTS
- No audio? Verify you sent the initialization frame first.
- Garbled/empty audio? Check base64 decoding and ensure you append bytes to file; confirm text frames contain content.
- Connection issues? Re‑check token format and consider `inactivity_timeout` for longer sessions.

## References and demos
- STT quickstart and concepts: [Speech-to-Text WebSocket streaming API](speech-to-text-websocket-streaming-api.md)
- TTS streaming details: [Text-to-Speech WebSocket streaming API](text-to-speech-websocket-streaming-api.md)
- Ultra model capabilities and SSML: [Telnyx Ultra Voices](telnyx-ultra-voices.md)
- Browse available voices: [Text-to-Speech voices catalog](text-to-speech-voices-catalog.md)
- Demo projects on GitHub:
  - STT and general examples: https://github.com/team-telnyx/demo-python-telnyx
  - TTS asyncio streaming: https://github.com/team-telnyx/demo-python-telnyx/tree/master/asyncio-tts-standalone
