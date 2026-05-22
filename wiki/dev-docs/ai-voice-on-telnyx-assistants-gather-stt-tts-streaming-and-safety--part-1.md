---
title: 'AI Voice on Telnyx: Assistants, Gather, STT/TTS, Streaming, and Safety'
summary: A practical guide to building AI-powered phone experiences on Telnyx. Learn
  when to use AI Assistants vs. Gather using AI, how to enable real-time media streaming,
  boost accuracy with noise suppression, add speech-to-text and text-to-speech (with
  SSML), and protect users with deepfake detection—plus key API calls and webhooks.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
  content_hash: 935729b032e38560301bf75fc52ae1799fd5184302fd224c88f05735a6e58e71
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
  content_hash: d17b526f566259e0e46f037b959216bbcf8a44e4a37521b5bd2b0efbeabf52f2
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
  content_hash: d6c3a73183ef7dc045d05c03ad29cf800a84e402c0b6c73d98e389b200a52b7d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
  content_hash: d0385b42b214b00cbda771a0671f724e760f90cbb2aa2f27e8e5d54bcd81e963
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
  content_hash: 6b108ff706319fa60a39497e105970f313d7b897740c0af34a21b6203265c1f8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
  content_hash: 56af332514e7916c8ab86d19963c873d2dae2ad760b2ea817357aa96108590e8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
  content_hash: 7c8e72fa751ece777e8f2ac7052003197d2a14b594125d5f0559e7b1273902a5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
  content_hash: cdee1b37fe2bfaf58920935e1538bcad65442f11294e8c586b9018478e948ed3
updated_at: 2026-05-20T09:33:28Z
---

# AI Voice on Telnyx: Assistants, Gather, STT/TTS, Streaming, and Safety

*Part 1 of 2 — see also: [Part 2](ai-voice-on-telnyx-assistants-gather-stt-tts-streaming-and-safety--part-2.md)*

A practical guide to building AI-powered phone experiences on Telnyx. Learn when to use AI Assistants vs. Gather using AI, how to enable real-time media streaming, boost accuracy with noise suppression, add speech-to-text and text-to-speech (with SSML), and protect users with deepfake detection—plus key API calls and webhooks.

## Choosing the right capability
- AI Assistant: Attach a pre-configured, conversational AI agent to an active call. Best for open-ended, back-and-forth dialog. See [Attach an AI Assistant to a Call](attach-an-ai-assistant-to-a-call.md).
- Gather using AI: Prompt the caller for specific fields (e.g., age, address) and receive a structured JSON payload that matches your JSON Schema. Best for quick, structured data capture. See [Gather using AI](gather-using-ai.md).
- Real-time media streaming: Fork call audio over WebSocket to your own AI engine for custom pipelines; optionally send audio back (bidirectional). See [Media Streaming over Websockets](media-streaming-over-websockets.md).
- Speech-to-Text (STT): Turn call audio into text using Telnyx or partner engines; events delivered via webhooks. See [Speech-to-Text with Voice API and TeXML](speech-to-text-with-voice-api-and-texml.md).
- Text-to-Speech (TTS): Play synthesized speech on calls using Telnyx voices or third-party providers (Polly, Azure, ElevenLabs, etc.). See [Text-to-Speech](text-to-speech.md) and customize pronunciation with [SSML Tags](ssml-tags.md).
- Noise suppression: Improve ASR and AI performance by removing background noise in one or both directions. See [Noise Suppression](noise-suppression.md).
- Deepfake detection: Classify whether the remote party’s voice is human or AI-generated—results via webhook. See [Deepfake Detection](deepfake-detection.md).

## One-time setup checklist for AI calls
- Telnyx account and a Voice API application able to place or receive calls.
- For AI Assistant: an assistant id (assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx) created in Portal or via API.
- Webhook endpoint(s) to receive events (e.g., transcription, streaming, assistant, deepfake results).

## Starting an AI Assistant on a live call
Attach an assistant to the active call; it will handle STT and speak with your chosen voice.

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_start \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistant": { "id": "assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" }
  }'
```
Webhooks emitted:
- call.conversation.ended — AI conversation finished
- call.conversation_insights.generated — Summary/insights available

Stop the assistant:
```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_stop \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" -d '{}'
```

## Adding participants to an ongoing AI conversation
You can dial a new participant, wait for call.answered, then join them to the existing conversation using ai_assistant_join.

Join example (id must be the participant’s call_control_id; supported role: "user"):
```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_join \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "participant": {
      "id": "{call_control_id}",
      "role": "user",
      "name": "Alex",
      "on_hangup": "continue_conversation" 
    }
  }'
```
Optional participant fields: name (display), on_hangup (continue_conversation | end_conversation).

## Collecting structured data with Gather using AI
Prompt the caller, define required fields with JSON Schema, and receive results in a structured format.

```
curl -X POST 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_using_ai' \
  -H 'Accept: application/json' -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "greeting": "Can you tell me your age and where you live?",
    "parameters": {
      "type": "object",
      "properties": {
        "age": {"description": "The age of the customer.", "type": "integer"},
        "location": {"description": "The location of the customer.", "type": "string"}
      },
      "required": ["age", "location"]
    },
    "voice": "Polly.Brian",
    "message_history": [
      {"role": "assistant", "content": "Hello what’s your name?"},
      {"role": "user", "content": "My name is Enzo."}
    ]
  }'
```
- parameters: JSON Schema for fields to capture.
- required: when all listed fields are gathered, Telnyx sends the webhook and gathering ends. If omitted, ends after first captured value.
- message_history: optional context to continue the dialog seamlessly.
- TeXML alternative: use the <AIGather> verb with Greeting, Voice, Parameters (JSON Schema), and MessageHistory.

Tip: Enable [Noise Suppression](noise-suppression.md) to improve transcription accuracy during gathering.

## Boosting accuracy with Noise Suppression
Enable on inbound, outbound, or both directions; billed per direction. Especially valuable for AI calls (ASR and agent response quality).

Start noise suppression:
```
curl -X POST https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
  -H 'Accept: application/json' -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"direction": "inbound", "noise_suppression_engine": "Krisp Viva Pro"}'
```
Stop:
```
curl -X POST https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_stop \
  -H 'Accept: application/json' -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' -d '{}'
```
Engines (choose based on use case): Denoiser (default), DeepFilterNet, Krisp Viva Tel Lite, Krisp Viva Pro, Krisp Viva SS, AI-coustics Quail.

## Real-time media streaming to your AI engine
Fork call audio over WebSocket to process in real time; the fork does not occupy the call stream. One streaming/fork operation per call. Request at dial or answer time.

Dial with streaming:
```
curl -X POST https://api.telnyx.com/v2/calls \
  -H 'Authorization: Bearer YOUR_API_KEY' -H 'Content-Type: application/json' \
  -d '{
    "connection_id": "uuid",
    "to": "+18005550199",
    "from": "+18005550100",
    "stream_url": "wss://yourdomain.com",
    "stream_track": "inbound_track" 
  }'
```
Answer with streaming:
```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer \
  -H 'Authorization: Bearer YOUR_API_KEY' -H 'Content-Type: application/json' \
  -d '{
    "stream_url": "wss://yourdomain.com",
    "stream_track": "both_tracks"
  }'
```
Lifecycle highlights:
- WebSocket sends: {"event":"connected"}.
- Webhook: streaming.started (with call_control_id, stream_url).
- WS start frame: includes media_format (encoding, sample_rate, channels) and stream_id.
- WS media frames: base64-encoded RTP payloads; order not guaranteed—use chunk/timestamp to reorder.
- Webhook: streaming.stopped; WS stop frame follows.
- If RTP forking is requested later, the WS stream is stopped and replaced.

Bidirectional (send audio back): set stream_bidirectional_mode to rtp; choose stream_bidirectional_codec (PCMU, PCMA, G722, OPUS, AMR-WB, L16). Send audio via WS media events; chunks 20 ms–30 s. You can also send base64 MP3 for playback (1 message/sec limit), clear the queue with {"event":"clear"}, and track completion with mark messages. DTMF events and structured error frames are delivered over the WS.

## Adding Speech-to-Text (transcription)
Start transcription on an active call and receive results via webhook call.transcription. Supported engines include Google (default), Telnyx (low-latency, high accuracy), Deepgram (nova-2/3, flux via transcription_model), Azure, xAI Grok STT, AssemblyAI, and Speechmatics.

```
curl -X POST 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/transcription_start' \
  -H 'Authorization: Bearer YOUR_API_KEY' -H 'Content-Type: application/json' \
  -d '{
    "language": "en",
    "transcription_engine": "Telnyx"
  }'
```
Webhook example payload includes transcript, confidence, and is_final flags. TeXML: use <Start><Transcription .../></Start>.
