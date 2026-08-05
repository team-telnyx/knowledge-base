---
title: TeXML Programmable Voice
summary: TeXML is Telnyx's XML-based markup language for controlling Programmable
  Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers
  the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint
  parity, and detailed reference for the core verbs including Dial, Conference, Enqueue,
  Connect, AIAssistant, AIGather, and ConversationRelay.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
updated_at: 2026-08-05T14:04:49Z
---

# TeXML Programmable Voice

*Part 6 of 6 — see also: [Part 1](texml-programmable-voice--part-1.md), [Part 2](texml-programmable-voice--part-2.md), [Part 3](texml-programmable-voice--part-3.md), [Part 4](texml-programmable-voice--part-4.md), [Part 5](texml-programmable-voice--part-5.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## ConversationRelay

The `<ConversationRelay>` verb routes a call to a ConversationRelay service that provides voice interactions over a WebSocket connection. It provides speech-to-text transcription and allows requesting text-to-speech synthesis for the call over WebSocket.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `url` | The WebSocket URL of the conversation relay server. | — | — |
| `welcomeGreeting` | A greeting message spoken when the conversation relay session starts. | — | — |
| `voice` | The TTS voice to use (e.g., `Telnyx.Natural.abbie`, `Telnyx.NaturalHD.astra`). | — | — |
| `language` | The language for TTS and transcription (e.g., `en`, `fr`, `es`). | — | — |
| `transcriptionProvider` | The speech-to-text provider (e.g., `deepgram`). | — | — |
| `interruptible` | Whether TTS playback can be interrupted by the caller. `true` is an alias for `any`, `false` is an alias for `none`. | `none`, `any`, `speech`, `dtmf`, `true`, `false` | `any` |
| `welcomeGreetingInterruptible` | Whether the welcome greeting can be interrupted by the caller. `true` is an alias for `any`, `false` is an alias for `none`. | `none`, `any`, `speech`, `dtmf`, `true`, `false` | `any` |
| `dtmfDetection` | Whether to enable DTMF detection during the conversation relay session. | — | `false` |
| `backgroundAudioType` | The type of background audio to mix into the call. Must be set together with `backgroundAudioValue`. | `media_url` | — |
| `backgroundAudioValue` | The background audio source. For `media_url`, a URL pointing to an audio file. Must be set together with `backgroundAudioType`. | — | — |

### Child verbs/nouns

- **`<Language>`** — Configures a supported language with optional per-language voice and provider settings. Multiple `<Language>` elements can be specified to enable multilingual conversations.
- **`<Parameter>`** — Custom key-value parameter passed to the WebSocket server as assistant dynamic variables.

### Language attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `code` | The language code (e.g., `en`, `fr`, `es`). | — | — |
| `ttsProvider` | The text-to-speech provider for this language (e.g., `telnyx`, `google`). | — | — |
| `voice` | The voice to use for this language. | — | — |
| `transcriptionProvider` | The speech-to-text provider for this language (e.g., `google`, `telnyx`, `deepgram`). | — | — |
| `speechModel` | The speech recognition model for this language (e.g., `nova-2`). | — | — |
| `backgroundAudioType` | The type of background audio to mix into the call for this language. Must be set together with `backgroundAudioValue`. | `media_url` | — |
| `backgroundAudioValue` | The background audio source for this language. Must be set together with `backgroundAudioType`. | — | — |

### Parameter attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `name` | The name of the custom parameter. | — | — |
| `value` | The value of the custom parameter. | — | — |

### Examples

**Basic usage with greeting and voice:**

```xml
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

**Multilingual with DTMF language selection:**

```xml
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Hello! I am your multilingual assistant. Press 1 for English, 2 for French, 3 for Spanish."
      welcomeGreetingInterruptible="any"
      interruptible="any"
      dtmfDetection="true"
    >
      <Language code="fr" voice="Telnyx.NaturalHD.astra" transcriptionProvider="google" />
      <Language code="es" voice="Telnyx.NaturalHD.albion" transcriptionProvider="telnyx" />
    </ConversationRelay>
  </Connect>
</Response>
```

**Custom parameters:**

```xml
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Hi there!"
    >
      <Parameter name="customer_id" value="12345" />
      <Parameter name="agent_mode" value="support" />
    </ConversationRelay>
  </Connect>
</Response>
```

**Non-interruptible greeting:**

```xml
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Please listen to this important message."
      welcomeGreetingInterruptible="none"
      interruptible="speech"
    />
  </Connect>
</Response>
```

**Background audio:**

```xml
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Hello! How can I help you today?"
      backgroundAudioType="media_url"
      backgroundAudioValue="https://example.com/hold-music.mp3"
    />
  </Connect>
</Response>
```

Per-language background audio is also supported on `<Language>` elements:

```xml
<Response>
  <Connect>
    <ConversationRelay
      url="wss://myapp.example.com/ws"
      voice="Telnyx.Natural.abbie"
      language="en"
      transcriptionProvider="deepgram"
      welcomeGreeting="Hello! I am your multilingual assistant."
    >
      <Language
        code="fr"
        voice="Telnyx.NaturalHD.astra"
        transcriptionProvider="google"
        backgroundAudioType="media_url"
        backgroundAudioValue="https://example.com/hold-music-fr.mp3"
      />
      <Language
        code="es"
        voice="Telnyx.NaturalHD.albion"
        transcriptionProvider="telnyx"
        backgroundAudioType="media_url"
        backgroundAudioValue="https://example.com/hold-music-es.mp3"
      />
    </ConversationRelay>
  </Connect>
</Response>
```

## Where to next

- Watch the [video walkthrough](https://telnyx.com/resources/texml-setup-tutorial) of this tutorial.
- Watch the [video guide](https://telnyx.com/resources/demo-how-to-make-a-texml-call-using-the-telnyx-api) showing how to make an outbound call from your Telnyx number using the Telnyx API and play text-to-speech when the call is answered using the same TeXML file. Be sure to set up an Outbound Voice Profile first.
- To start building with the RESTful API, see the guide to [setting up your development environment](https://developers.telnyx.com/docs/development). After setup, learn how to [send commands](https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands) and [receive webhooks](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks).
