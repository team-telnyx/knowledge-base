---
title: Telnyx Text-to-Speech WebSocket Streaming
summary: 'Real-time text-to-speech over a persistent WebSocket: open a connection,
  send text frames, and receive base64-encoded audio chunks as they’re synthesized.
  Configure voices and output via URL query parameters and provider-specific voice_settings
  in the init frame, then stream text with optional flushing and barge-in controls.
  Includes message schema, examples, errors, and provider notes.'
sources:
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
updated_at: 2026-05-20T10:22:43Z
---

# Telnyx Text-to-Speech WebSocket Streaming

*Part 1 of 2 — see also: [Part 2](telnyx-text-to-speech-websocket-streaming--part-2.md)*

Real-time text-to-speech over a persistent WebSocket: open a connection, send text frames, and receive base64-encoded audio chunks as they’re synthesized. Configure voices and output via URL query parameters and provider-specific voice_settings in the init frame, then stream text with optional flushing and barge-in controls. Includes message schema, examples, errors, and provider notes.

## Endpoint and authentication
- WebSocket URL: wss://api.telnyx.com/v2/text-to-speech/speech
- Authenticate by sending Authorization: Bearer <YOUR_API_KEY> in the HTTP upgrade headers.
- Connect either directly with a wss:// URL (including query parameters) or via an HTTP GET that upgrades with 101 Switching Protocols if you need fine-grained header control.

## Connection lifecycle and flow
- Handshake (required): first client message must be a text frame with a single space: "text": " ". You may include voice_settings here.
- Streaming: after init, send one or more text frames; the server buffers until sentence boundaries and streams corresponding audio.
- Teardown: send an empty string frame ("text": "") to flush any remaining buffered text. The server sends remaining audio, a final frame, then closes. The connection may also close on error or inactivity timeout.
- Configuration lock: URL query parameters are fixed at connect; voice_settings are fixed at init.

## Configuration surfaces and query parameters
Two one-shot configuration surfaces:
- URL query parameters (immutable after connect):
  - voice: Provider.Model.VoiceId (e.g., Telnyx.NaturalHD.astra)
  - language: BCP‑47 language code (used by providers that accept it: AWS Polly, Azure, ElevenLabs, Inworld)
  - text_type: text or ssml (AWS Polly, Azure)
  - audio_format: mp3 (default), linear16, wav, mulaw, alaw, ogg_vorbis (availability varies by provider)
  - sample_rate: output Hz (accepted values vary by provider)
  - disable_cache: boolean (default false) to bypass audio cache
  - Example: wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=linear16&disable_cache=true
- voice_settings in the init frame (immutable after init): provider-specific tuning (speed, pitch, emotion, etc.). Unrecognized fields are ignored.

## Voice selection and scopes
- voice uses the compound format Provider.Model.VoiceId.
  - Pre-built voice (e.g., Telnyx.NaturalHD.astra): available to everyone.
  - Your cloned voice (e.g., Telnyx.Qwen3TTS.my-ceo-clone): created in Voice Design Lab; scoped to your organization.
  - BYOK provider voice (e.g., elevenlabs.v3.Adam): a voice from your own provider account; Telnyx relays using your provider key.
- Discover voices with the Voices API (GET /v2/ai/tts/voices) — see List available voices in the Telnyx API Reference.

## Client message schema and sequence
Client messages are JSON text frames with these fields:
- text (string, required): content to synthesize. Use a single space " " for handshake; use an empty string "" to end and flush.
- voice_settings (object): provider-specific parameters; only honored in the handshake frame.
- flush (boolean): when true, immediately synthesize buffered text without waiting for punctuation.
- force (boolean): when true, stop the current synthesis worker and start a new one (barge-in). The original handshake is replayed automatically.

Typical sequence:
- Handshake: {"text":" ", "voice_settings":{...optional...}}
- Text frames: {"text":"Hello..."} (repeat as needed)
- Optional flush: {"text":"partial", "flush":true}
- Optional barge-in: {"force":true}
- End/flush/close: {"text":""}

## Server message schema and delivery modes
Server messages are JSON text frames:
- Audio chunk (concatenated): contains audio for a complete text segment
  - audio: base64 audio (string) or null
  - text: original text segment (string) or null
  - isFinal: false
  - cached: boolean indicating cache hit
  - timeToFirstAudioFrameMs: present on the first chunk of a synthesis
- Streamed audio chunk (incremental): for providers that stream incrementally, audio arrives in separate frames with text always null
  - audio: base64 audio (string)
  - text: null
  - isFinal: false
  - cached: boolean
- Final frame: signals synthesis completion for the current input
  - audio: null
  - text: ""
  - isFinal: true
- Error frame: {"error":"..."}; the server closes shortly after sending an error.

Delivery mode notes:
- Streamed providers (Telnyx Natural/NaturalHD/Qwen3TTS, Rime, Minimax, Resemble, Inworld): collect audio from streamed audio chunk frames (text=null). The text-bearing chunk’s audio may be null.
- AWS Polly and Azure: audio is returned in the text-bearing chunk’s audio field.
- After a final frame, the connection remains open; you can send more text. Send an empty text frame when you are finished to close gracefully.

## Barge-in and interruption behavior
- To interrupt mid-synthesis, send {"force":true}. This stops the current worker and starts a new one; the original handshake (including voice_settings) is replayed automatically.
- Immediately follow with a new text frame to steer the conversation.

## Text preprocessing and buffering rules
- Sentence buffering: text accumulates until a boundary (period, question mark, exclamation). Short fragments wait for more input; use flush:true to force early synthesis.
- Markdown stripping: headings, bold/italics, code blocks, links, lists, and emoji are removed automatically prior to synthesis — useful with LLM output.
- Pronunciation dictionaries: if you pass a pronunciation_dict_id, replacements are applied before synthesis. See [Pronunciation Dictionaries](pronunciation-dictionaries.md).

## Examples: basic, conversational, LLM token streaming
Basic streaming (Python):
```
import asyncio
import json
import base64
import websockets

async def tts_stream():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        # 1) Handshake
        await ws.send(json.dumps({"text": " "}))

        # 2) Send text
        await ws.send(json.dumps({"text": "Hello from Telnyx text-to-speech."}))

        # 3) End/flush
        await ws.send(json.dumps({"text": ""}))

        # 4) Receive audio
        audio_chunks = []
        async for message in ws:
            data = json.loads(message)
            if data.get("error"):
                raise RuntimeError(data["error"])
            if data.get("audio"):
                audio_chunks.append(base64.b64decode(data["audio"]))
            if data.get("isFinal"):
                break

    with open("output.mp3", "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

asyncio.run(tts_stream())
```

Conversational barge-in (Python):
```
import asyncio
import json
import websockets

async def conversational_tts():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        await ws.send(json.dumps({
            "text": " ",
            "voice_settings": {"voice_speed": 1.1}
        }))

        await ws.send(json.dumps({"text": "Welcome to the demo."}))

        # Interrupt quickly (barge-in)
        await ws.send(json.dumps({"force": True}))
        await ws.send(json.dumps({"text": "Actually, let me start over."}))

        await ws.send(json.dumps({"text": ""}))

asyncio.run(conversational_tts())
```

LLM token streaming (Python):
```
import asyncio
import json
import websockets

async def llm_to_tts(llm_token_stream):
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        await ws.send(json.dumps({"text": " "}))
        for token in llm_token_stream:
            await ws.send(json.dumps({"text": token}))
        await ws.send(json.dumps({"text": ""}))
```
