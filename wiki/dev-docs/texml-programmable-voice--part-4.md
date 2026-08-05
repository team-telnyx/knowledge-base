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

*Part 4 of 6 — see also: [Part 1](texml-programmable-voice--part-1.md), [Part 2](texml-programmable-voice--part-2.md), [Part 3](texml-programmable-voice--part-3.md), [Part 5](texml-programmable-voice--part-5.md), [Part 6](texml-programmable-voice--part-6.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## Conference

The `<Dial>` verb's `<Conference>` noun connects a call to a conference room. Like `<Number>` connects to another phone number, `<Conference>` connects to a named conference room and allows talking with other callers connected to that room. Conference is commonly used as a container for calls when implementing hold, transfer, and barge. If the specified conference name does not exist, a new conference is created.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `muted` | Specify whether a participant is muted. | — | `false` |
| `startConferenceOnEnter` | Start the conference when a participant joins. If `false` and the participant joins a conference that has not started, they are muted and hear background music until a participant joins where `startConferenceOnEnter` is `true`. Useful for moderated conferences. | — | `true` |
| `endConferenceOnExit` | If `true`, when that participant leaves, the conference ends and all other participants drop out. Useful for moderated conferences that bridge two calls. | — | `false` |
| `maxParticipants` | Maximum number of participants allowed in the conference. | `2`–`250` | `250` |
| `beep` | Whether a notification beep is played when a participant joins or leaves. The joining participant never hears a beep. | `true`, `false`, `onEnter`, `onExit` | `true` |
| `participantLabel` | A unique label for the participant, used to read or update participant attributes via the TeXML REST API. | — | — |
| `record` | Records the entire conference. | `do-not-record`, `record-from-start` | `do-not-record` |
| `recordBeep` | If enabled, a beep sound is played at the start of a recording. Set to `false` to disable. | — | `true` |
| `recordingStatusCallback` | Optional URL where Telnyx makes a GET or POST request when the recording is available. | — | — |
| `recordingStatusCallbackEvent` | Recording events for which Telnyx sends a webhook. | `in-progress`, `completed`, `absent` | `completed` |
| `recordingStatusCallbackMethod` | HTTP request type for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `recordingTimeout` | Number of seconds Telnyx waits for the recording to be stopped if silence is detected. The timer only starts when speech is detected. 0 means no timeout. | `0`–`14400` | `0` |
| `trim` | Whether to trim leading and trailing silence from the recording. | `trim-silence`, `do-not-trim` | `do-not-trim` |
| `sendRecordingUrl` | Defines if the recording URL is sent in the callbacks. | — | `true` |
| `statusCallback` | URL for Telnyx to send webhook requests on each event in `statusCallbackEvent`. | — | — |
| `statusCallbackMethod` | HTTP method for the status callback URL. | `GET`, `POST` | `POST` |
| `statusCallbackEvent` | Conference events for which Telnyx sends a webhook. | `start`, `end`, `join`, `leave`, `speaker` | — |
| `waitUrl` | URL to an MP3 or WAV file used for the conference's hold music before the conference starts. Can also return an XML document with instructions executed while the call is waiting. | — | — |
| `waitMethod` | HTTP method for the wait URL. | `GET`, `POST` | `POST` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial action="/nextinstructions.php">
        <Conference>conference_name</Conference>
    </Dial>
</Response>
```

### Expected callbacks

If `statusCallbackEvent` is set, the following webhooks are sent:

| Event | Callback Reference |
| --- | --- |
| `start` | [Conference Start](https://developers.telnyx.com/api-reference/callbacks/texml-conference-start) |
| `end` | [Conference End](https://developers.telnyx.com/api-reference/callbacks/texml-conference-end) |
| `join` | [Participant Join](https://developers.telnyx.com/api-reference/callbacks/texml-conference-join) |
| `leave` | [Participant Leave](https://developers.telnyx.com/api-reference/callbacks/texml-conference-leave) |
| `speaker` | [Participant Speaker](https://developers.telnyx.com/api-reference/callbacks/texml-conference-speaker) |

## Enqueue

The `<Enqueue>` verb enqueues the current call in a call queue.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Absolute or relative URL used to send a request when the call leaves the queue. Sent right away when dequeued using `<Leave>`. When dequeued using `<Dial>`, sent once the bridged calls disconnect. | — | — |
| `method` | HTTP request type for `action`. | `GET`, `POST` | `POST` |
| `waitUrl` | URL to the TeXML document executed when the call is waiting in the queue. Once all commands are executed, the waitUrl is re-requested. Supported verbs: `<Play>`, `<Say>`, `<Gather>`, `<Pause>`, `<Hangup>`, `<Redirect>`, `<Leave>`. | — | — |
| `waitUrlMethod` | HTTP request type for `waitUrl`. | `GET`, `POST` | `POST` |
| `maxWaitTimeSecs` | Maximum time in seconds a call can stay in the queue. If not dequeued within this time, the call is removed and the action URL is called. Must be at least 1 second. | — | `14400` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Enqueue/>
</Response>
```

### Expected callbacks

If `waitUrl` is set, a callback is sent when the call enters the queue. See the [Queue Callback](https://developers.telnyx.com/api-reference/callbacks/texml-queue) reference.

## Connect

The `<Connect>` verb starts the service defined in the nested noun in synchronous mode. The following instructions are executed when the service is stopped.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Optional URL where TeXML makes a request when the `<Connect>` service ends to retrieve a new set of TeXML instructions. Supported for `<ConversationRelay>` and `<AIAssistant>` nouns. | — | — |
| `method` | HTTP method for the action URL. | `GET`, `POST` | `POST` |

### Child verbs/nouns

- **`<Stream>`** — Start media stream over websocket. See the [Stream](stream.md) documentation.
- **`<ConversationRelay>`** — Route a call to a ConversationRelay service that provides voice interactions over a WebSocket connection. See the [ConversationRelay](conversationrelay.md) documentation.
- **`<AIAssistant>`** — Start a voice assistant on the call. See the [AIAssistant](aiassistant.md) documentation.

### Expected callbacks

If `action` is set, TeXML makes a request to the action URL when the connected service ends and executes the TeXML instructions returned in the response, replacing the remaining call flow. This is supported for `<ConversationRelay>` and `<AIAssistant>` nouns.

The request payload includes a `Reason` field describing why the service ended. For `<AIAssistant>`, common reasons include `normal` (a transfer is in progress — the call flow continues and the action is not requested), `service_error`, `stt_error`, `handoff`, and `hangup`. The action endpoint can branch on `Reason` to decide how to continue the call — for example, returning a `<Dial>` to a human agent when the conversation ended with a server-error reason.
