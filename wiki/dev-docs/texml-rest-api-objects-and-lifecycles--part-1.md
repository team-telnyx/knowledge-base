---
title: 'TeXML REST API: Objects and Lifecycles'
summary: Overview of TeXML REST API resources—what each object represents, how it’s
  created during call flows or via API, and where to manage or retrieve them (calls,
  conferences, participants, queues, recordings, transcripts, SIPREC sessions, streams,
  application configs, and secrets).
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
updated_at: 2026-05-20T09:42:18Z
---

# TeXML REST API: Objects and Lifecycles

*Part 1 of 2 — see also: [Part 2](texml-rest-api-objects-and-lifecycles--part-2.md)*

Overview of TeXML REST API resources—what each object represents, how it’s created during call flows or via API, and where to manage or retrieve them (calls, conferences, participants, queues, recordings, transcripts, SIPREC sessions, streams, application configs, and secrets).

## What the TeXML REST API models
The TeXML REST API exposes resources that reflect real-time voice operations and media workflows:
- TeXML applications (configuration driving instruction fetching and webhooks)
- Calls (individual call legs)
- Conferences (multi-party sessions) and conference participants (each joined leg)
- Queues (FIFO holding areas for calls)
- Recordings and transcripts
- SIPREC sessions (SIP-based compliance/monitoring capture)
- Streams (WebSocket audio streaming)
- Secrets (secure values for TeXML apps)

## TeXML applications
A TeXML application defines how inbound and outbound calls are handled using TeXML instructions, including where TeXML is fetched, which webhooks fire, and call behavior defaults. More background: TeXML fundamentals and interpreter behavior [TeXML Fundamentals](https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals).

## Calls
- Definition: A call object represents a single call leg, including state, metadata, and lifecycle.
- Creation:
  - Outbound via REST: Telnyx creates the call immediately when you initiate an outbound call [Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call).
  - Inbound: When a number assigned to a TeXML application is called, a call object is created, the call is answered, and Telnyx fetches TeXML instructions.
  - From TeXML <Dial>: Each execution of `<Dial>` creates a new call resource linked to its parent leg [<Dial>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial).
- Retrieval: Fetch details for up to 30 days after the call ends [Fetch a call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-call).

## Conferences
- Definition: A conference object represents a multi-participant audio session.
- Creation:
  - When TeXML executes `<Dial>` with a `<Conference>` noun; if the named conference does not exist, it’s created [<Conference>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference), [<Dial>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial).
- Management:
  - Fetch a conference [Fetch](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-conference-resource)
  - List conferences [List](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-resources)
  - Update a conference [Update](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-resource)
  - List associated recordings [Recordings](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-recordings)

## Conference participants
- Definition: A conference participant object represents an individual call leg added to a conference.
- Creation:
  - Dial a new participant into a conference via REST [Dial participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant).
  - Join via TeXML when a `<Dial>` contains `<Conference>` [<Conference>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference).
- When participant APIs return no records:
  - The conference has completed (ended).
  - The participant’s call leg is no longer active (hung up).
  - The participant was explicitly removed via REST [Delete participant](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-conference-participant).
  - The participant’s call leg received new TeXML via REST and effectively left the conference context [Update call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-call).

## Queues
- Definition: A queue is a FIFO holding area for calls.
- Creation:
  - Explicitly via REST [Create queue](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-new-queue).
  - Implicitly via TeXML `<Enqueue>`; if the named queue doesn’t exist, it’s created and the call is added [<Enqueue>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue).
- Management:
  - Fetch queue (by SID or name) [Fetch](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-queue-resource)
  - Update queue (e.g., max size) [Update](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-queue-resource)
  - Delete queue [Delete](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-queue-resource)

## Recordings
- Definition: A recording object represents audio captured during a call or conference, with metadata (format, duration, times, storage location).
- Creation scenarios:
  - Outbound call with recording enabled via REST [Initiate call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call).
  - TeXML `<Record>` verb execution [<Record>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record).
  - TeXML `<Dial>` executed with recording attributes [<Dial>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial).
  - TeXML `<Dial>` to `<Conference>` with recording attributes [<Conference>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference).
  - Manually start via REST on an existing call [Start recording](https://developers.telnyx.com/api-reference/texml-rest-commands/request-recording-for-a-call).
  - Dialing a new conference participant via REST with recording enabled [Dial participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant).
- Retrieval:
  - By recording ID [Fetch recording](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recording-resource)
  - By conference ID [For conference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-conference)
  - By call ID [For call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-call)
- Control ongoing recordings:
  - Update or stop recording on a call [Update/stop](https://developers.telnyx.com/api-reference/texml-rest-commands/update-recording-on-a-call)

## Transcripts
- Creation:
  - TeXML `<Transcription>` verb starts capture per verb parameters; transcripts are provided in real time via status callbacks [<Transcription>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription).
  - TeXML `<Record>` with transcription attributes triggers transcription after the recording completes [<Record>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record).
- Retrieval:
  - Fetch the transcription object for a recording segment [Fetch transcription](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-recording-transcription-resource)

## SIPREC sessions
- Definition: A SIPREC session represents SIP Client Recording media delivery to an external SIP recording server (for compliance/monitoring). Requires configured SIPREC client connectors [Tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client).
- Creation:
  - Start via REST for an active call [Start SIPREC](https://developers.telnyx.com/api-reference/texml-rest-commands/request-siprec-session-for-a-call).
  - Start via TeXML `<Siprec>`; typically invoked synchronously (commonly nested within `<Start>`) and subsequent TeXML proceeds after SIPREC is stopped [<Siprec>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec).
- Management:
  - Update or stop an active SIPREC session via REST [Update/stop](https://developers.telnyx.com/api-reference/texml-rest-commands/updates-siprec-session-for-a-call)
