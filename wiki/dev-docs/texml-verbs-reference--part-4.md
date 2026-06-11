---
title: TeXML Verbs Reference
summary: A comprehensive reference for all TeXML verbs supported by Telnyx, including
  attributes, child elements, examples, and expected callbacks for building programmable
  voice applications.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
  content_hash: af198eef7639e391f8c8f060405b7b04bad9b1c02f5eb3d0771068267a71caec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
  content_hash: afbc1d87d0606d433f6e5f456da75392521725ceebeec0a015e41479b6925ca6
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
  content_hash: f6246336ddcc26e377ef5a351ff895009cfab433929d181fa375ef09312ca49d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
  content_hash: dc8d6bbc5592d61ad053cc65f12f14d46cd45c42fce7c9c888e080bd775c0e37
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
  content_hash: d63d26ac52566cb49f4398eb06e0be92ce5093c2726eeec62887b4259770e650
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
  content_hash: 5fae52a988962b1da6c202ea94e3a1c3f03e5a91d33715480c226586ecd7f94a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
  content_hash: 802557ce95d90b7cad4499133baf861a0378c2c4d25f7948466065fd06917085
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
  content_hash: 598265ec490514334437faa8896ebb239db96bb5c07e2423a8e0b275874c33c0
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
  content_hash: 1a98d136a32499275e01c6a23d47697b2f6ed227eb045c7aff6e8e559cb92454
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
  content_hash: aff57efbd08370a28153150b16a57ae8a59fc7be4fdcd7c5eb9f5f1e00ebcc0d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
  content_hash: e2785d6fb22979fb9d219336aa2266f819a04d494710e3a5c063312a0202179e
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
  content_hash: 7d0c629edbe69236ddf3169e86442136d8063a9b534b148164cc3c4fa1e23e7c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
  content_hash: dfbb4e7ed40f0ebdbb5969ad0de1a97c96b87edbf0b3e886c3bd01d676b17130
updated_at: 2026-06-11T10:44:08Z
---

# TeXML Verbs Reference

*Part 4 of 5 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 5](texml-verbs-reference--part-5.md)*

A comprehensive reference for all TeXML verbs supported by Telnyx, including attributes, child elements, examples, and expected callbacks for building programmable voice applications.

## Enqueue

The `<Enqueue>` verb enqueues the current call in a call queue.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | URL called when the call leaves the queue. Sent immediately on `<Leave>`; sent after bridged calls disconnect when dequeued via `<Dial>`. | — | — |
| `method` | HTTP request type for `action`. | `GET`, `POST` | `POST` |
| `waitUrl` | URL to a TeXML document executed while the call is waiting. Re-requested after all commands execute. Supported verbs: `<Play>`, `<Say>`, `<Gather>`, `<Pause>`, `<Hangup>`, `<Redirect>`, `<Leave>`. | — | — |
| `waitUrlMethod` | HTTP request type for `waitUrl`. | `GET`, `POST` | `POST` |
| `maxWaitTimeSecs` | Maximum time in seconds a call can stay in the queue. If not dequeued in time, the call is removed and the action URL is called. Must be at least 1. | — | `14400` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Enqueue/>
</Response>
```

### Expected Callbacks

If `waitUrl` is set, a callback is sent when the call enters the queue. See [Queue Callback](https://developers.telnyx.com/api-reference/callbacks/texml-queue) for the full payload.

## Gather

The `<Gather>` verb collects DTMF tones during a call. `<Say>` and `<Play>` can be nested within `<Gather>` to create an interactive IVR.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | URL where TeXML sends the gathered result and message history. Transfers control to the returned TeXML file. | — | — |
| `timeout` | Seconds between digits before sending results to the action URL. Timeout starts after all nested verbs execute. | `1`–`120` | `5` |
| `input` | Input type for the gather action. | `dtmf`, `speech`, `dtmf speech` | `dtmf` |
| `speechTimeout` | Seconds to wait after speech ends before timing out. | — | — |
| `partialResultCallback` | URL for partial gather results. | — | — |
| `partialResultCallbackMethod` | HTTP method for `partialResultCallback`. | `GET`, `POST` | `POST` |
| `profanityFilter` | Filter profanity from speech recognition results (camelCase). | — | — |
| `useEnhanced` | Enable enhanced transcription for `phone_call` and `video` models (camelCase). | — | — |
| `hints` | Comma-separated hints for transcription accuracy. On Deepgram, maps to Nova-2 keyword biasing; silently dropped on Nova-3 (use `keyterms` instead). | — | — |
| `keyterms` | Comma-separated keyterm prompting for Deepgram Nova-3. Silently dropped on Nova-2 (use `hints` instead). | — | — |
| `smartFormat` | Disable Deepgram smart formatting to keep transcript lowercase with no punctuation. Deepgram-only; silently dropped on other engines. | — | `true` |
| `transcriptionEngine` | Speech recognition engine. | `Google`, `Telnyx`, `Azure`, `Deepgram`, `xAI`, `AssemblyAI`, `Soniox`, `Speechmatics` | — |
| `model` | Speech recognition model in `vendor/model-name` format (e.g., `deepgram/nova-2`, `deepgram/nova-3`, `azure/fast`). Vendor must match `transcriptionEngine`. On Deepgram, defaults to `deepgram/nova-3` when unset. | — | — |
| `apiKeyRef` | Reference to the API key for authentication. Optional as defaults exist for some regions. Used with Azure. See [integration secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret). | — | — |
| `region` | Region for the transcription engine. Required for Azure. | — | — |
| `finishOnKey` | Digit(s) that indicate the end of the gather. | `0`–`9`, `*`, `#` | `#` |
| `numDigits` | Number of digits to gather. | — | — |
| `language` | Language used. See [RESTful API documentation](https://developers.telnyx.com/api-reference/call-commands/speak-text) for supported values. | — | `en-US` |
| `validDigits` | Set of valid digits for the gather action. | — | — |
| `invalidDigitsAction` | URL for invalid gathered digits. Transfers control to the returned TeXML file. | — | — |
| `minDigits` | Minimum number of digits to gather. | `1`–`128` | `1` |
| `maxDigits` | Maximum number of digits to gather. | `1`–`128` | `128` |

### Child Verbs/Nouns

| Noun/Verb | Description |
|---|---|
| `Say` | Text-to-speech while gathering. |
| `Play` | Audio playback while gathering. |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather timeout="5" numDigits="1" finishOnKey="#">
        <Say>Press 1 for sales, press 2 for support.</Say>
    </Gather>
</Response>
```

### Expected Callbacks

If `action` is set, a callback is sent when gather completes with the collected digits or speech. See [Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-gather) for the full payload.

## Hangup

The `<Hangup>` verb ends the call. It takes no attributes.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Hangup/>
</Response>
```

### Expected Callbacks

When the call ends, a callback is sent to the connection-level webhook URL with `CallStatus` set to `completed`. See [Call Completed Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) for the full payload.

## HttpRequest

The `<HttpRequest>` verb sends a request to an external server. It contains `<Request>` and `<Response>` child nodes.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `async` | Whether TeXML should wait for the request response. When `false`, a callback is sent to the `action` URL when the request is processed. | — | `false` |
| `action` | URL for the callback when the request is processed (only if `async` is `false`). | — | — |

### Child Verbs/Nouns

| Noun/Verb | Description |
|---|---|
| `Request` | Defines the request attributes. Child nodes: `<Headers>` and `<Body>`. |
| `Response` | Defines the expected response attributes. Child nodes: `<Headers>` and `<Body>`. |

### Examples

Asynchronous request:

```xml
<Response>
    <HttpRequest async="true">
        <Request url="https://example.com" method="POST">
        <Headers>
            <Header>
                <Key>Authorization</Key>
                <Value>Bearer API_key</Value>
            </Header>
            <Header>
                <Key>Content-Type</Key>
                <Value>application/json</Value>
            </Header>
        </Headers>
        <Body>
        <![CDATA[{ "from":{{From}} }]]>
        </Body>
        </Request>
    </HttpRequest>
</Response>
```

Synchronous request with response mapping:

```xml
<Response>
    <HttpRequest async="false" action="https://example.com">
        <Request url="https://example.com" method="POST">
        ...
        </Request>
        <Response>
            <Type>JSON</Type>
            <StatusCode>200</StatusCode>
            <Content>
                <Field>
                    <Name>contact.name.first</Name>
                    <Value>first_name</Value>
                </Field>
                <Field>
                    <Name>contact.name.last</Name>
                    <Value>last_name</Value>
                </Field>
            </Content>
        </Response>
    </HttpRequest>
</Response>
```

### Expected Callbacks

When the HTTP request completes, a callback is sent to the `action` URL. See [HTTP Request Callback](https://developers.telnyx.com/api-reference/callbacks/texml-http-request) for the full payload.

## Leave

The `<Leave>` verb removes a call from the queue and continues with the next verb after the original `<Enqueue>`. It does not support any attributes.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Leave/>
</Response>
```

## Pause

The `<Pause>` verb waits silently for a specified number of seconds. No nouns can be nested, and a self-closing tag must be used.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `length` | Seconds to pause. | `1`–`180` | `1` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pause length="5"/>
</Response>
```
