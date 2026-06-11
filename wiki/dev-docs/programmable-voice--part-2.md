---
title: Programmable Voice
summary: A comprehensive guide to Telnyx Programmable Voice features including AI
  assistants, conversational AI, answering machine detection, deepfake detection,
  conferencing, call center and call tracking applications, and command reliability
  patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
  content_hash: 98741f32636161f55901706f46f8e1a44a9f23beb18370224ae446aa9a5bfd6f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
  content_hash: d7a369042ca143eb9760583149e142a1545bfb5d5630b46841e04080ab398b40
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
  content_hash: 6743698486c30f4d9b6e0f9371ad72d04ae17b4c418bbcf4f1a1a72199ebcf9f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
  content_hash: 8762f879ea7719ba40f6a5fa4721b21367249a69fc022fc96c8486d34a5727f8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
  content_hash: b6066b6a288f076617936c05582dd192c18263aa82d134eb52d14ab3a28b0518
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
  content_hash: 3de81d6148a7dd75fa2e2a36839abfc788546f0cfc98d4d7fbe35bc199cafbd7
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
  content_hash: 4b83741b3c773a4d36e4e5341557ead15eccf01625794e18a563f358764f1ecd
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
  content_hash: 25876583acfa3c5273554542ce524d05df1e663e9dd47fbd5d433dbd4ae70aaf
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
  content_hash: 0eccef25db89c30146704f1f025caac64b7b6a7fa062c496cf916f0ab68ba133
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
  content_hash: d2375c9c573083bca6581989d01b376e1cd7c24b5ae1c9a835ca334a49ec6df3
updated_at: 2026-06-11T10:41:58Z
---

# Programmable Voice

*Part 2 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 3](programmable-voice--part-3.md), [Part 4](programmable-voice--part-4.md)*

A comprehensive guide to Telnyx Programmable Voice features including AI assistants, conversational AI, answering machine detection, deepfake detection, conferencing, call center and call tracking applications, and command reliability patterns.

## Conversation Relay

Conversation Relay connects a live Telnyx call to your WebSocket application. Telnyx handles speech recognition and text-to-speech while your application receives caller input and sends commands in real time. Use it to build conversational voice applications, connect calls to an LLM, react to DTMF input, play audio, change languages, or end the session from your application.

### How It Works

1. Your application provides a public `wss://` WebSocket URL.
2. Telnyx starts Conversation Relay on the call (via TeXML or Programmable Voice).
3. Telnyx opens a WebSocket connection to your application.
4. Telnyx sends a `setup` frame identifying the session and call.
5. Telnyx sends `prompt`, `dtmf`, `interrupt`, and `error` frames as call events occur.
6. Your application sends `text`, `play`, `sendDigits`, `language`, or `end` frames back.

Telnyx does not reconnect automatically if the WebSocket closes. Closing the WebSocket terminates the session.

### Starting via TeXML

Use a `<Connect>` verb with a nested `<ConversationRelay>` verb:

```xml
<Response>
  <Connect action="https://yourdomain.com/conversation-relay/action">
    <ConversationRelay
      url="wss://yourdomain.com/conversation-relay"
      interruptible="none"
      welcomeGreeting="Welcome to the Conversation Relay demo."
      welcomeGreetingInterruptible="none"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      dtmfDetection="true">
      <Language code="fr" voice="Telnyx.NaturalHD.astra" transcriptionProvider="google" />
      <Language code="es" voice="Telnyx.NaturalHD.albion" transcriptionProvider="telnyx" />
      <Parameter name="customer_id" value="customer_123" />
    </ConversationRelay>
  </Connect>
</Response>
```

The `action` attribute is on `<Connect>`, not `<ConversationRelay>`. It controls where Telnyx sends the action callback after the connected service stops.

Key attributes: `url` (WebSocket URL), `welcomeGreeting` (spoken greeting), `voice`, `language`, `transcriptionProvider`, `dtmfDetection`, `interruptible`, and `welcomeGreetingInterruptible`. Child nouns: `Language` (per-language settings) and `Parameter` (custom key-value data sent in the `setup` frame).

### Starting via Programmable Voice

Use the `conversation_relay_start` command on an active call:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/conversation_relay_start \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "url": "wss://yourdomain.com/conversation-relay",
    "voice": "Telnyx.Natural.abbie",
    "tts_provider": "telnyx",
    "greeting": "Welcome to the Conversation Relay demo.",
    "language": "en-US",
    "languages": [
      { "language": "en-US", "tts_provider": "telnyx", "voice": "Telnyx.Natural.abbie", "transcription_engine": "Deepgram" },
      { "language": "es", "tts_provider": "telnyx", "voice": "Telnyx.NaturalHD.albion", "transcription_engine": "Deepgram" }
    ],
    "dtmf_detection": true,
    "interruptible": "none",
    "interruptible_greeting": "none",
    "transcription_engine": "Deepgram",
    "custom_parameters": { "customer_id": "customer_123" }
  }'
```

The response returns a `conversation_relay_id` in the result.

### Frames Sent by Telnyx

| Type | Description |
| --- | --- |
| `setup` | First frame after WebSocket connects. Identifies session and call (includes `sessionId`, `callControlId`, `from`, `to`, `customParameters`). |
| `prompt` | Caller speech transcribed to text. Partial transcripts use `last: false`; final transcripts use `last: true`. |
| `dtmf` | DTMF digit pressed by the caller. |
| `interrupt` | Caller interrupted ongoing TTS playback. Includes `utteranceUntilInterrupt` and `durationUntilInterruptMs`. |
| `error` | Invalid frame sent by your application or another relay error. |

### Frames Sent by Your Application

| Type | Description |
| --- | --- |
| `text` | Text fragment to speak via TTS. Use `token` for the text content and `last: true` when the turn is complete. For streaming LLM output, send chunks with `last: false` then a final chunk with `last: true`. |
| `play` | Audio URL to play. Supports `source`, `loop`, `interruptible`, and `preemptible` fields. |
| `sendDigits` | DTMF digits to send. Valid characters: `0`–`9`, `A`–`D`, `w`/`W` for pause, `#`, `*`. |
| `language` | Change TTS and/or transcription language during the session. At least one of `ttsLanguage` or `transcriptionLanguage` must be provided. |
| `end` | Gracefully end the Conversation Relay session. Supports optional `handoffData`. |

### Continuing After Conversation Relay

In TeXML, the `<Connect>` verb runs synchronously. When `<ConversationRelay>` stops, Telnyx continues with the next TeXML instructions. If `action` is set on `<Connect>`, Telnyx requests the next TeXML from that callback URL:

```xml
<Response>
  <Connect action="https://yourdomain.com/conversation-relay/action">
    <ConversationRelay url="wss://yourdomain.com/conversation-relay" />
  </Connect>
</Response>
```

### Conversation Relay Webhooks

When using Programmable Voice, lifecycle events are delivered to the Call Control webhook URL. When the session ends, Telnyx sends a `call.conversation.ended` webhook with a `reason` (e.g., `customer_disconnect` if the WebSocket disconnects).
