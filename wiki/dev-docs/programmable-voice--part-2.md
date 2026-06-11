---
title: Programmable Voice
summary: A comprehensive guide to Telnyx Programmable Voice features including AI
  assistants, conversational AI, answering machine detection, deepfake detection,
  conferencing, call center and call tracking applications, and command reliability
  patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
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
