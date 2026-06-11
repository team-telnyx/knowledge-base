---
title: TeXML Verbs Reference
summary: A comprehensive reference for all TeXML verbs supported by Telnyx, including
  attributes, child elements, examples, and expected callbacks for building programmable
  voice applications.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
updated_at: 2026-06-11T10:44:08Z
---

# TeXML Verbs Reference

*Part 2 of 5 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md)*

A comprehensive reference for all TeXML verbs supported by Telnyx, including attributes, child elements, examples, and expected callbacks for building programmable voice applications.

## Conference

The `<Conference>` noun (nested within `<Dial>`) connects a call to a named conference room. If the conference name does not exist, a new one is created. It is commonly used as a container for hold, transfer, and barge scenarios.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `muted` | Whether the participant is muted. | — | `false` |
| `startConferenceOnEnter` | Start the conference when a participant joins. If `false`, the participant is muted and hears hold music until a participant with `true` joins. | — | `true` |
| `endConferenceOnExit` | End the conference and drop all participants when this participant leaves. | — | `false` |
| `maxParticipants` | Maximum number of participants. | `2`–`250` | `250` |
| `beep` | Play a notification beep on join/leave. The joining participant never hears the beep. Does not affect the recording start beep. | `true`, `false`, `onEnter`, `onExit` | `true` |
| `participantLabel` | Unique label for the participant, usable with the TeXML REST API. | — | — |
| `record` | Record the conference. `record-from-start` begins recording immediately after the conference starts. | `do-not-record`, `record-from-start` | `do-not-record` |
| `recordBeep` | Play a beep at the start of recording. Independent of the `beep` attribute. | — | `true` |
| `recordingStatusCallback` | URL for recording availability webhooks. | — | — |
| `recordingStatusCallbackEvent` | Recording events for webhooks, space-separated. | `in-progress`, `completed`, `absent` | `completed` |
| `recordingStatusCallbackMethod` | HTTP method for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `recordingTimeout` | Seconds to wait for recording to stop on silence (0 = no timeout). Uses transcription for silence detection. | `0`–`14400` | `0` |
| `trim` | Trim leading/trailing silence from recording. | `trim-silence`, `do-not-trim` | `do-not-trim` |
| `sendRecordingUrl` | Whether the recording URL is sent in callbacks. | — | `true` |
| `statusCallback` | URL for conference event webhooks. | — | — |
| `statusCallbackMethod` | HTTP method for `statusCallback`. | `GET`, `POST` | `POST` |
| `statusCallbackEvent` | Conference events for webhooks, space-separated. | `start`, `end`, `join`, `leave`, `speaker` | — |
| `waitUrl` | URL for hold music (MP3/WAV) or TeXML instructions executed while waiting for the conference to start. | — | — |
| `waitMethod` | HTTP method for `waitUrl`. | `GET`, `POST` | `POST` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial action="/nextinstructions.php">
        <Conference>conference_name</Conference>
    </Dial>
</Response>
```

### Expected Callbacks

When `statusCallbackEvent` is configured, webhooks are sent for the following events:

| Event | Callback Reference |
|---|---|
| `start` | [Conference Start](https://developers.telnyx.com/api-reference/callbacks/texml-conference-start) |
| `end` | [Conference End](https://developers.telnyx.com/api-reference/callbacks/texml-conference-end) |
| `join` | [Participant Join](https://developers.telnyx.com/api-reference/callbacks/texml-conference-join) |
| `leave` | [Participant Leave](https://developers.telnyx.com/api-reference/callbacks/texml-conference-leave) |
| `speaker` | [Participant Speaker](https://developers.telnyx.com/api-reference/callbacks/texml-conference-speaker) |

## Connect

The `<Connect>` verb starts the service defined in the nested noun in synchronous mode. Subsequent instructions execute when the service stops.

### Child Verbs/Nouns

| Noun/Verb | Description |
|---|---|
| `Stream` | Start a media stream over WebSocket. See [Stream documentation](texml-verbs-reference-stream.md). |
| `ConversationRelay` | Route a call to a ConversationRelay service for voice interactions over WebSocket. |

## ConversationRelay

The `<ConversationRelay>` verb routes a call to a ConversationRelay service providing speech-to-text transcription and text-to-speech synthesis over a WebSocket connection. Must be nested within `<Connect>`.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `url` | WebSocket URL of the conversation relay server. | — | — |
| `welcomeGreeting` | Greeting message spoken when the session starts. | — | — |
| `voice` | TTS voice (e.g., `Telnyx.Natural.abbie`, `Telnyx.NaturalHD.astra`). | — | — |
| `language` | Language for TTS and transcription (e.g., `en`, `fr`, `es`). | — | — |
| `transcriptionProvider` | Speech-to-text provider (e.g., `deepgram`). | — | — |
| `interruptible` | Whether TTS playback can be interrupted. `true` is an alias for `any`; `false` is an alias for `none`. | `none`, `any`, `speech`, `dtmf`, `true`, `false` | `any` |
| `welcomeGreetingInterruptible` | Whether the welcome greeting can be interrupted. | `none`, `any`, `speech`, `dtmf`, `true`, `false` | `any` |
| `dtmfDetection` | Enable DTMF detection during the session. | — | `false` |

### Child Verbs/Nouns

| Noun/Verb | Description |
|---|---|
| `Language` | Configures a supported language with optional per-language voice and provider settings. Multiple elements enable multilingual conversations. |
| `Parameter` | Custom key-value parameter passed to the WebSocket server as assistant dynamic variables. |

### Language Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `code` | Language code (e.g., `en`, `fr`, `es`). | — | — |
| `ttsProvider` | TTS provider for this language (e.g., `telnyx`, `google`). | — | — |
| `voice` | Voice to use for this language. | — | — |
| `transcriptionProvider` | STT provider for this language (e.g., `google`, `telnyx`, `deepgram`). | — | — |
| `speechModel` | Speech recognition model (e.g., `nova-2`). | — | — |

### Parameter Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `name` | Name of the custom parameter. | — | — |
| `value` | Value of the custom parameter. | — | — |

### Examples

Basic usage:

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

Multilingual with DTMF language selection:

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

Custom parameters:

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

Non-interruptible greeting:

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
