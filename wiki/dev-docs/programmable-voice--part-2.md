---
title: Programmable Voice
summary: The Telnyx Programmable Voice API enables you to integrate voice calling
  capabilities into your applications, providing flexible inbound and outbound call
  control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake
  Detection, Dialogflow ES integration, and AI-driven gather flows.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
updated_at: 2026-08-05T14:03:33Z
---

# Programmable Voice

*Part 2 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 3](programmable-voice--part-3.md), [Part 4](programmable-voice--part-4.md)*

The Telnyx Programmable Voice API enables you to integrate voice calling capabilities into your applications, providing flexible inbound and outbound call control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake Detection, Dialogflow ES integration, and AI-driven gather flows.

## Conversation Relay over WebSockets

Conversation Relay connects a live Telnyx call to your WebSocket application. Telnyx handles speech recognition and text-to-speech while your application receives caller input and sends commands back in real time. Use Conversation Relay when you want to build your own conversational voice application, connect calls to an LLM, react to DTMF input, play audio, change languages during a session, or end the relay session from your application.

### How Conversation Relay Works

Conversation Relay uses a single bidirectional WebSocket connection per session:

1. Your application provides a public `wss://` WebSocket URL.
2. Telnyx starts Conversation Relay on the call, either from TeXML or with a Programmable Voice command.
3. Telnyx opens a WebSocket connection to your application.
4. Telnyx sends a `setup` frame that identifies the session and call.
5. Telnyx sends `prompt`, `dtmf`, `interrupt`, and `error` frames as call events occur.
6. Your application sends `text`, `play`, `sendDigits`, `language`, or `end` frames back to Telnyx.

Telnyx does not reconnect automatically if the WebSocket closes. Closing the WebSocket terminates the Conversation Relay session.

### Starting Conversation Relay Using TeXML

Return a `<Connect>` verb with a nested `<ConversationRelay>` verb from your TeXML voice URL:

```
<?xml version="1.0" encoding="UTF-8"?>
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
      dtmfDetection="true"
    >
      <Language code="fr" voice="Telnyx.NaturalHD.astra" transcriptionProvider="google" />
      <Language code="es" voice="Telnyx.NaturalHD.albion" transcriptionProvider="telnyx" />
      <Parameter name="customer_id" value="customer_123" />
    </ConversationRelay>
  </Connect>
</Response>
```

The `action` attribute is configured on `<Connect>`, not on `<ConversationRelay>`. It controls where Telnyx sends the action callback after the connected service stops. Your application can use that callback request to return the next TeXML instructions for the call.

Key attributes:

- `url` — The WebSocket URL Telnyx connects to. Must start with `ws://` or `wss://`.
- `welcomeGreeting` — Text Telnyx speaks when the relay starts.
- `voice` — The TTS voice used for generated speech.
- `language` — The default language for TTS and transcription.
- `transcriptionProvider` — The speech recognition provider.
- `dtmfDetection` — Enables DTMF detection and `dtmf` WebSocket frames.
- `interruptible` and `welcomeGreetingInterruptible` — Control when caller input can interrupt speech.

Child nouns:

- `Language` — Adds a supported language with optional per-language `voice`, `ttsProvider`, `transcriptionProvider`, and `speechModel` settings.
- `Parameter` — Sends custom key-value data to your WebSocket server in the `setup` frame.

### Starting Conversation Relay Using Programmable Voice

You can also start Conversation Relay on an active Programmable Voice call with the [Start Conversation Relay command](/api-reference/call-commands/start-conversation-relay). Use this option when your application is already controlling the call through Call Control. After the call is active, send a `conversation_relay_start` command with the call's `call_control_id`:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/conversation_relay_start \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "url": "wss://yourdomain.com/conversation-relay",
    "voice": "Telnyx.Natural.abbie",
    "tts_provider": "telnyx",
    "voice_settings": {
      "type": "telnyx"
    },
    "greeting": "Welcome to the Conversation Relay demo.",
    "language": "en-US",
    "languages": [
      {
        "language": "en-US",
        "tts_provider": "telnyx",
        "voice": "Telnyx.Natural.abbie",
        "transcription_engine": "Deepgram",
        "transcription_engine_config": {
          "transcription_model": "deepgram/nova-3"
        }
      },
      {
        "language": "es",
        "tts_provider": "telnyx",
        "voice": "Telnyx.NaturalHD.albion",
        "transcription_engine": "Deepgram",
        "transcription_engine_config": {
          "transcription_model": "deepgram/nova-3"
        }
      }
    ],
    "dtmf_detection": true,
    "interruptible": "none",
    "interruptible_greeting": "none",
    "transcription_engine": "Deepgram",
    "transcription_engine_config": {
      "transcription_model": "deepgram/nova-3"
    },
    "custom_parameters": {
      "customer_id": "customer_123"
    }
  }'
```

Common fields:

- `url` — The Conversation Relay WebSocket URL.
- `greeting` — Text Telnyx speaks when the relay starts.
- `voice` — The TTS voice used for generated speech.
- `tts_provider` — The text-to-speech provider. If omitted, Telnyx derives it from `voice` or `provider`.
- `voice_settings` — Provider-specific voice settings.
- `language` — The default language for TTS and transcription.
- `languages` — Per-language TTS and transcription settings.
- `dtmf_detection` — Enables DTMF detection.
- `interruptible` and `interruptible_greeting` — Control when caller input can interrupt speech.
- `transcription_engine` and `transcription_engine_config` — Configure the speech recognition provider.
- `custom_parameters` — Key-value data forwarded to the relay session.

The response includes a regular command confirmation with the Conversation Relay session ID:

```
{
  "data": {
    "result": "ok",
    "conversation_relay_id": "d7e9c1d4-8b2a-4b8f-b3a7-9a671c9e9b0a"
  }
}
```

### WebSocket Process Flow

When Conversation Relay starts, Telnyx opens a WebSocket connection to the configured `url` and sends a `setup` frame:

```
{
  "type": "setup",
  "sessionId": "7a7e6a4f-1d44-4f0c-b5d4-9f9bf3a5c1f2",
  "accountSid": "1f1a8b6f-1234-4abc-9def-1234567890ab",
  "callSid": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
  "callControlId": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
  "callSessionId": "ff55a038-6f5d-11ef-9692-02420aeffb1f",
  "callLegId": "428c31b6-7af4-4b6f-92e7-7a7e6a4f1d44",
  "from": "+13122010094",
  "to": "+13122123456",
  "direction": "inbound",
  "callerName": "",
  "callStatus": "active",
  "customParameters": {
    "customer_id": "customer_123"
  }
}
```

Use the `setup` frame to initialize call-specific state in your application. After setup, your application can send `text`, `play`, `sendDigits`, `language`, or `end` frames back to Telnyx.

### Frames Sent by Telnyx

| Type | Description |
| --- | --- |
| `setup` | First frame sent after the WebSocket connects. Identifies the relay session and call. |
| `prompt` | Caller speech transcribed to text. Partial transcripts use `last: false`; final transcripts use `last: true`. |
| `dtmf` | DTMF digit pressed by the caller. |
| `interrupt` | Sent when the caller interrupts ongoing TTS playback. |
| `error` | Sent when your application sends an invalid frame or another relay error occurs. |

**Prompt frame** — Telnyx sends `prompt` frames as the caller speaks:

```
{
  "type": "prompt",
  "voicePrompt": "hello there how are you",
  "lang": "en",
  "last": true
}
```

Use `last: false` prompts as interim transcription updates. Use `last: true` prompts as the final transcript for the caller's utterance.

**DTMF frame** — When DTMF detection is enabled, keypad input is sent as `dtmf` frames:

```
{
  "type": "dtmf",
  "digit": "1"
}
```

**Interrupt frame** — When the caller barges in over TTS playback, Telnyx sends an `interrupt` frame:

```
{
  "type": "interrupt",
  "utteranceUntilInterrupt": "Welcome to Telnyx, how can I help",
  "durationUntilInterruptMs": 1820
}
```

### Frames Sent by Your Application

| Type | Description |
| --- | --- |
| `text` | Text fragment to speak back to the caller using TTS. |
| `play` | Audio URL to play into the call. |
| `sendDigits` | DTMF digits to send on the call. |
| `language` | Change TTS and/or transcription language during the session. |
| `end` | Gracefully end the Conversation Relay session. |

**Sending text** — Send a `text` frame to speak text to the caller. The text content is sent in the `token` field:

```
{
  "type": "text",
  "token": "Hello, how can I help you today?",
  "last": true
}
```

For streaming LLM output, send each token or chunk with `last: false`, then send the final chunk with `last: true`:

```
{ "type": "text", "token": "Hello", "last": false }
{ "type": "text", "token": ", how can I help?", "last": true }
```

If you omit `last`, Telnyx treats it as `false`. Send `last: true` when the turn is complete.

**Playing audio** — Send a `play` frame to play an audio file by URL:

```
{
  "type": "play",
  "source": "https://example.com/audio/welcome.mp3",
  "loop": 1,
  "interruptible": true,
  "preemptible": false
}
```

**Sending DTMF digits** — Send a `sendDigits` frame to send DTMF digits on the call:

```
{
  "type": "sendDigits",
  "digits": "1234#"
}
```

Valid characters are `0`-`9`, `A`-`D`, `w` or `W` for a pause, `#`, and `*`.

**Changing language** — Send a `language` frame to change TTS and/or transcription language:

```
{
  "type": "language",
  "ttsLanguage": "es-ES",
  "transcriptionLanguage": "es-ES"
}
```

At least one of `ttsLanguage` or `transcriptionLanguage` must be provided.

**Ending the session** — Send an `end` frame to end the Conversation Relay session gracefully:

```
{
  "type": "end",
  "handoffData": "{\"reason\":\"caller_done\"}"
}
```

### Continuing the Call After Conversation Relay

The `<Connect>` verb runs in synchronous mode. When the nested `<ConversationRelay>` service stops, Telnyx either continues with the next TeXML instructions in the same response or, when `action` is set on `<Connect>`, sends a request to that callback URL so your application can return the next TeXML document.

For example, you can provide a follow-up prompt after Conversation Relay ends:

```
<Response>
  <Connect>
    <ConversationRelay url="wss://yourdomain.com/conversation-relay" />
  </Connect>
  <Say voice="Telnyx.Natural.abbie">Conversation Relay has ended. Goodbye.</Say>
  <Hangup />
</Response>
```

If you set `action`, Telnyx requests the next instructions from your callback URL:

```
<Response>
  <Connect action="https://yourdomain.com/conversation-relay/action">
    <ConversationRelay url="wss://yourdomain.com/conversation-relay" />
  </Connect>
</Response>
```

The callback endpoint can then return the next TeXML document dynamically:

```
<Response>
  <Say voice="Telnyx.Natural.abbie">Conversation Relay has ended. Goodbye.</Say>
  <Hangup />
</Response>
```

### Conversation Relay Webhooks

When using Programmable Voice, Conversation Relay lifecycle events are delivered to your Call Control webhook URL. When the relay session ends, Telnyx sends:

```
{
  "data": {
    "event_type": "call.conversation.ended",
    "payload": {
      "reason": "customer_disconnect"
    },
    "record_type": "event"
  }
}
```

If your WebSocket disconnects, the webhook payload `reason` is `customer_disconnect`.

### Conversation Relay Error Handling

If your application sends malformed or invalid frames, Telnyx sends an `error` frame:

```
{
  "type": "error",
  "description": "Invalid message: missing required field: token"
}
```

After repeated invalid frames, Telnyx can close the WebSocket connection.
