---
title: Speech-to-Text
summary: 'Telnyx Speech-to-Text (STT) transcribes audio to text via three integration
  paths: WebSocket streaming for real-time partial and final transcripts, a REST API
  for synchronous file-based transcription, and in-call transcription for live voice
  calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper,
  Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable
  per request, with a single global endpoint and Bearer-token authentication.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
updated_at: 2026-08-05T14:06:51Z
---

# Speech-to-Text

*Part 6 of 7 — see also: [Part 1](speech-to-text--part-1.md), [Part 2](speech-to-text--part-2.md), [Part 3](speech-to-text--part-3.md), [Part 4](speech-to-text--part-4.md), [Part 5](speech-to-text--part-5.md), [Part 7](speech-to-text--part-7.md)*

Telnyx Speech-to-Text (STT) transcribes audio to text via three integration paths: WebSocket streaming for real-time partial and final transcripts, a REST API for synchronous file-based transcription, and in-call transcription for live voice calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable per request, with a single global endpoint and Bearer-token authentication.

## Migrating from Other Providers

Most migrations require changing 2–3 lines of code.

### Deepgram

**WebSocket**

```
- wss://api.deepgram.com/v1/listen?model=nova-2&language=en
- Authorization: Token DEEPGRAM_KEY
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-2&language=en
+ Authorization: Bearer TELNYX_KEY
```

The wire protocol is the same — send binary audio frames, receive JSON transcripts.

|  | Deepgram | Telnyx |
| --- | --- | --- |
| Auth scheme | `Token` | `Bearer` |
| Engine | implicit | `transcription_engine=Deepgram` |
| Model name | `nova-2`, `nova-3`, `flux` | `nova-2`, `nova-3`, `flux`, `flux-multi` |

Response field mapping:

| Deepgram | → Telnyx |
| --- | --- |
| `results.channels[0].alternatives[0].transcript` | `transcript` |
| `is_final` | `is_final` |
| `speech_final` | `is_final` |

**REST**

```
# Before (Deepgram)
curl -X POST https://api.deepgram.com/v1/listen?model=nova-2 \
  -H "Authorization: Token DEEPGRAM_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav

# After (Telnyx)
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer TELNYX_KEY" \
  -F model="deepgram/nova-3" \
  -F file=@audio.wav
```

|  | Deepgram | Telnyx |
| --- | --- | --- |
| Auth scheme | `Token` | `Bearer` |
| Body | raw binary | `multipart/form-data` |
| Model name | `nova-2` | `deepgram/nova-3` |

Response field mapping:

| Deepgram | → Telnyx |
| --- | --- |
| `results.channels[0].alternatives[0].transcript` | `text` |
| `results.channels[0].alternatives[0].words` | available via `model_config.diarize` / `model_config.smart_format` |

### ElevenLabs

**WebSocket**

```
- wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v1&language_code=en
- xi-api-key: ELEVENLABS_KEY
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&language=en
+ Authorization: Bearer TELNYX_KEY
```

The wire protocol is the same — send binary audio frames, receive JSON transcripts.

Config mapping:

| ElevenLabs | Telnyx query parameter |
| --- | --- |
| `model_id` | `transcription_engine` + `model` |
| `language_code` | `language` |
| `keywords` | `keyterm` (Nova-3/Flux) |

Response field mapping:

| ElevenLabs | → Telnyx |
| --- | --- |
| `text` | `transcript` |
| `is_final` | `is_final` |

**REST**

```
# Before (ElevenLabs)
curl -X POST https://api.elevenlabs.io/v1/speech-to-text \
  -H "xi-api-key: ELEVENLABS_KEY" \
  -F "audio=@audio.mp3" \
  -F "model_id=scribe_v1"

# After (Telnyx)
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer TELNYX_KEY" \
  -F model="openai/whisper-large-v3-turbo" \
  -F file=@audio.mp3
```

|  | ElevenLabs | Telnyx |
| --- | --- | --- |
| Auth header | `xi-api-key` | `Authorization: Bearer` |
| File field | `audio` | `file` |
| Model field | `model_id` | `model` |

Response shape: identical. Telnyx returns the same `{"text": "..."}` shape — no parsing changes needed.

### OpenAI

**REST** — The easiest migration. Telnyx REST is OpenAI SDK compatible. Change the API key and base URL, everything else stays the same.

Python:

```python
from openai import OpenAI

client = OpenAI(
-    api_key="sk-OPENAI_KEY",
+    api_key="YOUR_TELNYX_API_KEY",
+    base_url="https://api.telnyx.com/v2",
)

result = client.audio.transcriptions.create(
    model="openai/whisper-large-v3-turbo",
    file=open("audio.mp3", "rb"),
)
```

JavaScript:

```javascript
import OpenAI from "openai";
import fs from "fs";

const client = new OpenAI({
-  apiKey: "sk-OPENAI_KEY",
+  apiKey: "YOUR_TELNYX_API_KEY",
+  baseURL: "https://api.telnyx.com/v2",
});

const result = await client.audio.transcriptions.create({
  model: "openai/whisper-large-v3-turbo",
  file: fs.createReadStream("audio.mp3"),
});
```

|  | OpenAI | Telnyx |
| --- | --- | --- |
| `api_key` | `sk-...` | Telnyx API key |
| `base_url` | (default) | `https://api.telnyx.com/v2` |
| Method | `client.audio.transcriptions.create(...)` | unchanged |
| Response | `result.text` | unchanged |

Response shape: Telnyx returns the same `{"text": "..."}` shape — no parsing changes needed for the default `json` response format.

**Note on `verbose_json`:** OpenAI's Whisper API returns segments with timestamps when you set `response_format=verbose_json`. Telnyx's Whisper models (`openai/whisper-large-v3-turbo`, `openai/whisper-tiny`) return text only — no segments. If you need timestamps, switch to `model="deepgram/nova-3"` which supports segment- and word-level timestamps via `model_config`.

### Google Cloud

**WebSocket** — Google uses gRPC with protobuf. Telnyx uses WebSocket with JSON — no protobuf compilation, no service account credentials.

```python
# Before (Google Cloud)
from google.cloud import speech

client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
    enable_automatic_punctuation=True,
)
streaming_config = speech.StreamingRecognitionConfig(
    config=config,
    interim_results=True,
)
# ... gRPC streaming setup
```

```
# After (Telnyx)
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Google&language=en-US&interim_results=true&input_format=linear16&sample_rate=16000
Authorization: Bearer TELNYX_KEY
```

Config mapping:

| Google gRPC | Telnyx query parameter |
| --- | --- |
| `language_code` | `language` |
| `encoding` | `input_format` |
| `sample_rate_hertz` | `sample_rate` |
| `interim_results` | `interim_results` |
| `enable_automatic_punctuation` | enabled by default |

What you drop: protobuf definitions, gRPC client setup, service account credentials.

Response field mapping:

| Google Cloud | → Telnyx |
| --- | --- |
| `results[0].alternatives[0].transcript` | `transcript` |
| `results[0].is_final` | `is_final` |

### AWS Transcribe

**WebSocket** — AWS Transcribe Streaming uses HTTP/2 with event streams via the [`amazon-transcribe-streaming-sdk`](https://github.com/awslabs/amazon-transcribe-streaming-sdk). Telnyx uses a plain WebSocket — no AWS SDK, no SigV4 signing, no IAM credentials.

```python
# Before (AWS) — amazon-transcribe-streaming-sdk
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler

class Handler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, event):
        for result in event.transcript.results:
            for alt in result.alternatives:
                print(alt.transcript)

client = TranscribeStreamingClient(region="us-east-1")
stream = await client.start_stream_transcription(
    language_code="en-US",
    media_sample_rate_hz=16000,
    media_encoding="pcm",
)

# Send audio chunks via stream.input_stream.send_audio_event(...)
# Receive results via Handler
```

```
# After (Telnyx) — plain WebSocket
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&language=en-US&input_format=linear16&sample_rate=16000
Authorization: Bearer TELNYX_KEY
```

Send binary audio frames, receive JSON transcripts. No AWS SDK, no SigV4 signing, no IAM.

Config mapping:

| AWS Transcribe Streaming | Telnyx query parameter |
| --- | --- |
| `language_code` | `language` |
| `media_encoding` | `input_format` |
| `media_sample_rate_hz` | `sample_rate` |
| `enable_partial_results_stabilization` | `interim_results` |
| `vocabulary_name` | `keyterm` (Nova-3/Flux) |

Response field mapping:

| AWS Transcribe Streaming | → Telnyx |
| --- | --- |
| `transcript.results[].alternatives[].transcript` | `transcript` |
| `transcript.results[].is_partial` | `is_final` (inverted) |

### Azure

**WebSocket** — The [Azure Speech SDK](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-sdk) wraps a region-specific WebSocket with SDK abstractions and event handlers. Telnyx uses a plain WebSocket — no SDK install, no region routing.

```python
# Before (Azure Speech SDK)
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription="AZURE_KEY",
    region="eastus",
)
speech_config.speech_recognition_language = "en-US"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config,
)

recognizer.recognizing.connect(lambda evt: print(f"partial: {evt.result.text}"))
recognizer.recognized.connect(lambda evt: print(f"FINAL: {evt.result.text}"))
recognizer.start_continuous_recognition()
```

```
# After (Telnyx) — plain WebSocket
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Azure&language=en-US&interim_results=true
Authorization: Bearer TELNYX_KEY
```

Send binary audio frames, receive JSON transcripts. No SDK install, no region routing.

Config mapping:

| Azure Speech SDK | Telnyx query parameter |
| --- | --- |
| `speech_recognition_language` | `language` |
| `recognizing` event | partial result (`is_final: false`) |
| `recognized` event | final result (`is_final: true`) |
| `region` | not needed — single global endpoint |

Response field mapping:

| Azure Speech SDK | → Telnyx |
| --- | --- |
| `evt.result.text` (recognizing/recognized) | `transcript` |
| `recognizing` event | `is_final: false` |
| `recognized` event | `is_final: true` |

What you drop: Azure Speech SDK install, region routing, event-handler boilerplate, subscription key management.

**REST**

```
# Before (Azure)
curl -X POST \
  "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US" \
  -H "Ocp-Apim-Subscription-Key: AZURE_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav

# After (Telnyx)
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer TELNYX_KEY" \
  -F model="openai/whisper-large-v3-turbo" \
  -F file=@audio.wav
```

|  | Azure | Telnyx |
| --- | --- | --- |
| Auth | `Ocp-Apim-Subscription-Key` header | `Authorization: Bearer` |
| URL | region-specific | single global endpoint |
| Body | raw binary | `multipart/form-data` |
| Language | required query param | auto-detected or optional |

Response field mapping:

| Azure | → Telnyx |
| --- | --- |
| `DisplayText` | `text` |
| `NBest[0].Lexical` | `text` |
