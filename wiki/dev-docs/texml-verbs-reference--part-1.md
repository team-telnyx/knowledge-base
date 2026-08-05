---
title: TeXML Verbs Reference
summary: A consolidated reference for the TeXML verbs available in Telnyx Programmable
  Voice, covering call control, media playback, recording, transcription, conferencing,
  payments, and SIPREC. Each verb section lists attributes, child nouns, examples,
  and the callbacks that the platform emits.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/recording
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
updated_at: 2026-08-05T14:05:15Z
---

# TeXML Verbs Reference

*Part 1 of 7 — see also: [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md), [Part 6](texml-verbs-reference--part-6.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Overview

TeXML is Telnyx's XML-based markup language for controlling programmable voice calls. A TeXML document is a `<Response>` element containing one or more verbs that execute sequentially. Some verbs (such as [Gather](gather.md), [Play](play.md), and [Say](say.md)) can also be nested inside other verbs to compose richer call flows. A small set of verbs (`<Start>`, `<Stop>`) act as containers that begin or end a long-running service in parallel with the rest of the script.

The verbs documented on this page are:

- [Gather](gather.md) — collect DTMF or speech input
- [Hangup](hangup.md) — end the call
- [HttpRequest](httprequest.md) — call an external HTTP service
- [Leave](leave.md) — exit a queue
- [Pause](pause.md) — wait silently
- [Pay](pay.md) — collect and process payments
- [Play](play.md) — play audio, DTMF, or ringback tones
- [Record](record.md) — record the call (blocking)
- [Recording](recording.md) — start a non-blocking recording (nested in `<Start>`)
- [Redirect](redirect.md) — hand control to another TeXML document
- [Refer](refer.md) — transfer the call to an external SIP endpoint
- [Reject](reject.md) — reject the call
- [Say](say.md) — speak text using text-to-speech
- [Siprec](siprec.md) — start a SIPREC session (nested in `<Start>`/`<Stop>`)
- [Start](start.md) — start a nested service

## Gather

The `<Gather>` verb collects DTMF tones during a call. `<Say>` can be nested within `<Gather>` to create an interactive IVR with text-to-speech.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | URL where TeXML will send the gathered result and message history. Same method (`GET`/`POST`) as set for the TeXML application is used. Transfers control of the current call to the TeXML file returned. | — | — |
| `timeout` | Time in seconds between digits before the `<Gather>` digits are sent to your action URL. Telnyx will wait until all nested verbs have been executed before beginning the timeout period. | `1`–`120` | `5` |
| `input` | The input type for the gather action. | `dtmf`, `speech`, `dtmf speech` | `dtmf` |
| `speechTimeout` | Time in seconds to wait after speech ends before timing out. | — | — |
| `partialResultCallback` | URL for sending partial gather results. | — | — |
| `partialResultCallbackMethod` | HTTP request type used for `partialResultCallback`. | `GET`, `POST` | `POST` |
| `profanityFilter` | Whether to filter profanity from speech recognition results (camelCase format). | — | — |
| `useEnhanced` | Enables enhanced transcription; works for models `phone_call` and `video` (camelCase format). | — | — |
| `hints` | Hints to improve transcription accuracy. On Deepgram, this maps to the Nova-2 keyword biasing feature and is supported only on `model="deepgram/nova-2"`; it is silently dropped on Nova-3 (use `keyterms` instead). Accepts a comma-separated string. | — | — |
| `keyterms` | Deepgram Nova-3 keyterm prompting. Biases recognition toward domain-specific terms or brand names. Supported only on `model="deepgram/nova-3"`; silently dropped on Nova-2 (use `hints` instead). Accepts a comma-separated string. | — | — |
| `smartFormat` | Disable Deepgram's smart formatting so the transcript stays lowercase with no punctuation. Deepgram-only; silently dropped on other engines. | — | `true` |
| `transcriptionEngine` | Engine to use for speech recognition. | `Google`, `Telnyx`, `Azure`, `Deepgram`, `xAI`, `AssemblyAI`, `Soniox`, `Speechmatics`, `Parakeet`, `Humain`, `Reson8`, `Cohere` | — |
| `model` | Speech recognition model. Format is `vendor/model-name` — e.g. `deepgram/nova-2`, `deepgram/nova-3`, `azure/fast`, `assemblyai/universal-streaming`, `soniox/stt-rt-v4`, `speechmatics/standard`, `nvidia/parakeet-v3`, `xai/grok-stt`, `humain/realtime`, `reson8/turns`, `cohere/ar-stt`. The vendor must match `transcriptionEngine`. On Deepgram, defaults to `deepgram/nova-3` when unset. | — | — |
| `apiKeyRef` | Reference to the API key for authentication. See the [integration secrets documentation](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret) for details. The parameter is optional as defaults are available for some regions. Used with Azure `transcriptionEngine`. | — | — |
| `region` | Region to use with the specified transcription engine. Required for Azure. See regions in [transcription_engine_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). | — | — |
| `finishOnKey` | The set of digits (`0`–`9`, `*`, `#`) that indicates the end of the gather. | — | `#` |
| `numDigits` | The number of digits to be gathered. | — | — |
| `language` | The language used. See the [RESTful API documentation](https://developers.telnyx.com/api-reference/call-commands/speak-text) for supported values. | — | `en-US` |
| `validDigits` | The set of valid digits for the gather action. | — | — |
| `invalidDigitsAction` | URL where TeXML will send the invalid gathered digits. The same method (`GET`/`POST`) as set for the TeXML application is used. Transfers control of the current call to the TeXML file returned. | — | — |
| `minDigits` | Minimum number of digits to be gathered. | `1`–`128` | `1` |
| `maxDigits` | Maximum number of digits to be gathered. | `1`–`128` | `128` |

### Child verbs/nouns

- `Say`
- `Play`

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather timeout="5" numDigits="1" finishOnKey="#">
        <Say>Press 1 for sales, press 2 for support.</Say>
    </Gather>
</Response>
```

### Expected callbacks

If `action` is set, a callback is sent when gather completes with the collected digits or speech. See the [Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-gather) for the full payload reference.

## Hangup

The `<Hangup>` verb ends the call.

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Hangup/>
</Response>
```

### Expected callbacks

When the call ends, a callback is sent to the webhook URL defined on the connection level with `CallStatus` set to `completed`. See the [Call Completed Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) for the full payload reference.
