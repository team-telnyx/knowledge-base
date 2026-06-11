---
title: TeXML AI and Real‑Time Voice Capabilities
summary: Build natural, interactive voice experiences on Telnyx using TeXML verbs
  for AI assistants, structured data collection, WebSocket conversations, real‑time
  media streaming, transcription, SIPREC recording, noise suppression, HTTP integrations,
  and call transfers.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
updated_at: 2026-05-20T09:39:10Z
---

# TeXML AI and Real‑Time Voice Capabilities

*Part 1 of 2 — see also: [Part 2](texml-ai-and-realtime-voice-capabilities--part-2.md)*

Build natural, interactive voice experiences on Telnyx using TeXML verbs for AI assistants, structured data collection, WebSocket conversations, real‑time media streaming, transcription, SIPREC recording, noise suppression, HTTP integrations, and call transfers.

## Overview
Use these TeXML verbs to add AI and real‑time functionality to calls:
- <AIAssistant> to run a Telnyx AI Assistant on a call or join an existing AI conversation
- <AIGather> to extract structured parameters from speech using a JSON Schema
- <ConversationRelay> to drive a live, bidirectional voice UX over your own WebSocket
- <Stream> to send/receive near‑real‑time audio over WebSocket
- <Transcription> for real‑time STT across multiple engines
- <Siprec> to stream compliant call recording to your SRS
- <Suppression> to denoise call audio
- <HttpRequest> to call external HTTP services mid‑flow
- <Refer> to transfer a call to external SIP

Many features are toggled at runtime with [Start](start.md) and [Stop](stop.md), and interactive flows are typically enclosed in [Connect](connect.md).

## Choosing the right building block
- Use AIAssistant when you’ve provisioned an AI assistant in the API and want it to handle the call end‑to‑end, or when you need to join an existing AI conversation.
- Use AIGather when you need specific, validated fields (e.g., name, date, order number) returned to your app via a callback.
- Use ConversationRelay when you want full control via WebSocket (custom ASR/TTS routing, multilingual handling, tool calls server‑side).
- Use Stream for raw audio streaming to your infra (analytics, custom ML) and optional bidirectional audio injection.
- Add Transcription when you need STT events for analytics, compliance, or downstream automation.
- Add Siprec for standards‑based recording to a SIP Recording Server (SRS).
- Add Suppression to improve audio quality on one or both legs.
- Add HttpRequest to fetch data or push events to your backend during a call.
- Use Refer to transfer the call to a different SIP system mid‑flow.

## <AIAssistant> — run an AI Assistant on the call
Starts an AI assistant or joins an existing assistant conversation.
- id: Assistant identifier created via the AI Assistant API (see Create Assistant: https://developers.telnyx.com/api-reference/assistants/create-an-assistant)
- join: An existing assistant conversation ID to join (adds this call leg as a participant)
- participantName: Display name when joining with join
- participantRole: Participant role when joining; user (default) or assistant

Example — start a new assistant
```
<Response>
  <Connect>
    <AIAssistant id="assistant-776d0d6f-716d-4d8f-b6da-b95181636838" />
  </Connect>
</Response>
```

Example — join an existing conversation
```
<Response>
  <Connect>
    <AIAssistant join="v3:abc123def456" participantName="John" participantRole="user" />
  </Connect>
</Response>
```

## <AIGather> — collect structured parameters with AI
Collects specific fields using AI guided by a JSON Schema provided in a child <Parameters> node.
- action: URL to receive the gathered result and message history; TeXML then follows the returned instructions
- method: HTTP method to fetch the next instructions (GET or POST; default POST)

Child nodes you can include:
- Greeting: Optional text played at the start of the gathering
- Voice: Configure the TTS voice used by the assistant
- Parameters: JSON Schema (inside CDATA) describing fields to collect and which are required
- MessageHistory: One or more <Message role="user|assistant"> elements to seed context
- Tools: One or more <Tool> elements, each containing a tool definition in JSON (tool types per Voice API “Gather using AI”: https://developers.telnyx.com/api-reference/call-commands/gather-using-ai)
- Assistant: Configure the model, api_key_ref, and instructions for the LLM, and optionally nest <Tools>

Voice attributes (on <Voice>):
- name: Voice selection. Supported providers and notation: 
  - ElevenLabs: ElevenLabs.model_id.voice_id
  - Telnyx: Telnyx.model_id.voice_id (default Telnyx.NaturalHD.Astra)
  - AWS Polly: AWS.Polly.voice_id or Polly.voice_id
- api_key_ref: Reference to your ElevenLabs API key (required only for ElevenLabs voices)
- voice_speed: 0.1–2.0 (Telnyx voices only; default 1.0)

Example — simple gather with two fields
```
<Response>
  <AIGather action="/after_ai_gather">
    <Greeting>Please tell me your age and city.</Greeting>
    <Parameters>
      <![CDATA[
      {
        "type": "object",
        "properties": {
          "age": {"type": "integer", "description": "Age of the customer"},
          "location": {"type": "string", "description": "City or town"}
        },
        "required": ["age", "location"]
      }
      ]]>
    </Parameters>
    <Voice name="Telnyx.NaturalHD.Astra" voice_speed="1.0" />
  </AIGather>
</Response>
```

Callback: If action is set, Telnyx posts the collected result and message history on completion (see AI Gather Callback: https://developers.telnyx.com/api-reference/callbacks/texml-ai-gather).

## <ConversationRelay> — WebSocket voice interactions you control
Routes the call to your ConversationRelay WebSocket, providing ASR and on‑demand TTS over the socket.
- url: Your ConversationRelay WebSocket URL
- welcomeGreeting: Optional greeting spoken at session start
- voice: TTS voice (e.g., Telnyx.Natural.abbie, Telnyx.NaturalHD.astra)
- language: Default language code (e.g., en, fr, es)
- transcriptionProvider: STT provider (e.g., deepgram)
- interruptible: Whether TTS can be interrupted by caller input; values any | none | speech | dtmf | true (alias any) | false (alias none); default any
- welcomeGreetingInterruptible: Same semantics for just the greeting; default any
- dtmfDetection: Enable DTMF detection (default false)

Child nodes:
- Language (multilingual): code, ttsProvider, voice, transcriptionProvider, speechModel
- Parameter: name, value — sent to your server as dynamic variables

Example — basic setup
```
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Hello! How can I help you today?"
    />
  </Connect>
</Response>
```

## <Stream> — near‑real‑time audio streaming over WebSocket
Starts streaming call audio to your WebSocket; audio arrives as base64‑encoded RTP payloads in JSON. Supports optional bidirectional audio.
- url: Destination WebSocket URL
- track: inbound_track | outbound_track | both_tracks (default inbound_track)
- name: Optional stream instance name
- codec: PCMU | PCMA | G722 | OPUS | AMR‑WB | default (transcoding supported only PCMU↔PCMA when possible)
- bidirectionalMode: mp3 | rtp (default mp3)
- bidirectionalCodec: PCMU | PCMA | G722 | OPUS | AMR‑WB (used only with bidirectionalMode=rtp; default PCMU)
- bidirectionalSamplingRate: 8000 | 16000 | 24000 (default 8000)
- statusCallback: URL for stream status webhooks
- statusCallbackMethod: GET | POST (default POST)
- enableReconnect: Whether to auto‑reconnect on socket drops (default true)

Child node:
- Parameter: name, value — included in the start message

Example — start streaming both legs
```
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" track="both_tracks" />
  </Start>
</Response>
```

Callbacks: If statusCallback is set, you’ll receive stream-started, stream-stopped, and stream-failed (Stream Callback: https://developers.telnyx.com/api-reference/callbacks/texml-stream).
