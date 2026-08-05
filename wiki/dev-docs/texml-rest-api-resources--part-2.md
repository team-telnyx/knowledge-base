---
title: TeXML REST API Resources
summary: Overview of the core resource objects exposed by the Telnyx TeXML REST API,
  including applications, calls, conferences, queues, recordings, secrets, SIPREC
  sessions, streams, and transcripts, with details on how each resource is created,
  managed, and retrieved.
sources:
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/applications/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/secrets/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
updated_at: 2026-08-05T14:06:05Z
---

# TeXML REST API Resources

*Part 2 of 3 — see also: [Part 1](texml-rest-api-resources--part-1.md), [Part 3](texml-rest-api-resources--part-3.md)*

Overview of the core resource objects exposed by the Telnyx TeXML REST API, including applications, calls, conferences, queues, recordings, secrets, SIPREC sessions, streams, and transcripts, with details on how each resource is created, managed, and retrieved.

## Recordings

A recording object represents an audio recording generated during a call or conference using a TeXML application. Recording objects track metadata such as format, duration, start and end times, and storage locations.

A recording can be created in the following situations:

1. When an outbound call is initiated with record enabled via the REST API ([Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call)). If your application initiates an outbound call and specifies the record attribute, Telnyx automatically begins recording the call when it is answered.
2. When a [Record](record.md) verb is executed in a TeXML script. Whenever a `<Record>` verb is encountered in a TeXML response, Telnyx initiates audio capture for the call leg that executed the verb. Each execution produces a distinct recording object that captures the audio during the `<Record>` period.
3. When a [Dial](dial.md) verb is executed with record attributes enabled. If a `<Dial>` verb includes recording parameters (e.g., to record the outbound leg created by the dial), Telnyx begins recording as soon as that outbound call leg is created.
4. When a `<Dial>` to [Conference](conference.md) is executed with record attributes. When a `<Dial>` connects a call into a `<Conference>` and recording attributes are provided, Telnyx initiates conference recording.
5. When recording is started manually via the REST API ([Request recording for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-recording-for-a-call)). The recording may be triggered dynamically on any existing call by making a request to the start recording endpoint. When the request is executed, Telnyx creates a new recording object associated with that ongoing call.
6. When a conference participant is dialed and joined via the REST API with recording enabled ([Dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant)). If a new participant is added to a conference using the REST API and recording is enabled for that action, Telnyx begins capturing audio for the participant or the entire conference session.

Recording objects can be retrieved through several query paths depending on how the recording was initiated:

1. By Recording ID — [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recording-resource)
2. By Conference ID — [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-conference)
3. By Call ID — [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-call)

Once recording is active, your application can manage or modify the recording session using the REST API:

- Update or stop an ongoing recording on a call — [API reference](https://developers.telnyx.com/api-reference/texml-rest-commands/update-recording-on-a-call)

## TeXML Application Secrets

The TeXML Secrets API provides a secure mechanism for storing, managing, and retrieving sensitive information required by your TeXML applications. This includes credentials, API keys, tokens, and other confidential values that should not be hardcoded into TeXML documents or exposed in application source code. See the [sending HTTP requests tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests#using-secrets) for more information.

A secret can be created using the [Create a TeXML secret](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-texml-secret) endpoint.

## SIPREC Sessions

A SIPREC session represents an active SIP Client Recording (SIPREC) media session associated with a call. SIPREC sessions enable the delivery of call media to an external SIP recording server for compliance recording, monitoring, or archival purposes. Each SIPREC session object encapsulates the configuration, state, and lifecycle of a single recording session tied to a call. In order to use SIPREC, the SIPREC client connectors must be configured in your Telnyx account. See the [SIPREC client tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client) for more information.

A SIPREC session can be started in the following ways:

1. Starting a SIPREC session via the REST API ([Request a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-siprec-session-for-a-call)). Using the REST API, an application can explicitly request the initiation of a SIPREC session for an active call. When this endpoint is invoked, Telnyx creates a SIPREC session object and begins streaming the call media to the configured SIP recording endpoint according to the supplied parameters. This approach allows SIPREC to be started dynamically at any point during the call lifecycle.
2. Starting a SIPREC session via the TeXML [Siprec](siprec.md) verb. The SIPREC session is initiated synchronously (nested to `<Start>` verb) as part of the sequential TeXML execution flow. Subsequent TeXML instructions are processed only after the SIPREC session has been stopped.

Once a SIPREC session has been started — either via the REST API or via TeXML — it can be managed throughout its lifecycle using the REST API ([Update a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/updates-siprec-session-for-a-call)). This endpoint allows an application to update the state of an active SIPREC session or explicitly stop the recording.

## Streams

A stream object represents an active media streaming session originating from a call. Streams allow real-time audio from a call to be delivered to an external destination using WebSockets. Each stream object encapsulates the configuration, state, and lifecycle of a single streaming session associated with a call.

A stream object can be started in the following ways:

1. Starting a stream via the REST API ([Start streaming media from a call](https://developers.telnyx.com/api-reference/texml-rest-commands/start-streaming-media-from-a-call)). Using the REST API, an application can explicitly start streaming media from an active call. When this endpoint is invoked, a stream object is created and audio begins streaming from the specified call according to the provided configuration. This method allows streaming to be initiated dynamically at any point during the call lifecycle.
2. Starting a stream via the TeXML `<Stream>` verb. Streams can also be initiated as part of TeXML execution using the `<Stream>` verb, which supports two operational modes:
   - **Asynchronous streaming via `<Start>`** — When the `<Stream>` verb is nested inside a `<Start>` verb, the stream is started asynchronously. In this mode, streaming begins in parallel with the ongoing call flow, allowing audio to be streamed without interrupting or blocking other TeXML instructions.
   - **Synchronous streaming via `<Connect>`** — When the `<Stream>` verb is nested inside a `<Connect>` verb, streaming is initiated synchronously. In this mode, the call flow waits for the streaming operation to stop before proceeding to the next TeXML instruction.

In both cases, execution of the `<Stream>` verb results in the creation of a stream object associated with the active call.

Once a stream has been started — whether via the REST API or TeXML — it can be managed throughout its lifecycle using the REST API:

- Updating or stopping a stream via the REST API ([Update streaming on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-streaming-on-a-call)). When streaming is stopped, the associated stream object transitions to a completed state, and websockets are closed.
