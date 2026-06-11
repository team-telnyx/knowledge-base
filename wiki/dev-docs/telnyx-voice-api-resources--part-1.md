---
title: Telnyx Voice API Resources
summary: Covers the TeXML REST API resource types—applications, calls, conferences,
  queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along
  with the Text-to-Speech system including in-call playback and pronunciation dictionaries.
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
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
- url: https://developers.telnyx.com/docs/voice/tts/overview/index
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
updated_at: 2026-06-11T10:46:12Z
---

# Telnyx Voice API Resources

*Part 1 of 3 — see also: [Part 2](telnyx-voice-api-resources--part-2.md), [Part 3](telnyx-voice-api-resources--part-3.md)*

Covers the TeXML REST API resource types—applications, calls, conferences, queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along with the Text-to-Speech system including in-call playback and pronunciation dictionaries.

## TeXML Applications

A TeXML application defines how inbound and outbound calls are handled using TeXML instructions. Each application instance encapsulates configuration parameters that control call behavior, instruction retrieval, and webhook interactions. These parameters determine where Telnyx fetches TeXML from, how call events are handled, and how call flows are executed. See the [Applications documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index#texml-application) for more details.

## Calls

A call object represents a single call leg, containing all state, metadata, and lifecycle information for that leg.

### Creating calls

A call object is created in three situations:

1. **Outbound call via REST API** — Telnyx immediately creates a call resource when an outbound call is initiated through the [Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call) endpoint.
2. **Inbound call to a TeXML application** — When an inbound call reaches a phone number assigned to a TeXML application, a call resource is created, the call is answered, and the instruction fetch request is sent. The lifecycle is driven by the TeXML response.
3. **`<Dial>` verb execution** — Each execution of [`<Dial>`](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial) creates a new call resource, logically associated with the parent call. Telnyx manages both as part of a multi-leg call flow.

### Fetching call details

Call details can be retrieved using the [Fetch a call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-call) endpoint up to 30 days after the call has ended.

## Conferences and Participants

A conference object represents a multi-participant audio session. A conference participant object represents an individual call leg that has been added to a conference.

### Creating conferences

A conference is instantiated when a `<Dial>` to a non-existent `<Conference>` is executed. When Telnyx processes a TeXML response containing a `<Dial>` verb with a [`<Conference>`](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference) noun, it attempts to place the current call into the named conference, creating it if necessary.

### Managing conferences

Once instantiated, conferences can be managed via REST API:

- [Fetch a conference resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-conference-resource)
- [List all conferences](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-resources)
- [Update a conference](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-resource)
- [List associated recordings](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-recordings)

### Creating conference participants

A conference participant is instantiated when:

1. A new participant is dialed into an existing conference via the [Dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant) REST API endpoint.
2. A call leg joins a conference via `<Dial>` with `<Conference>` in TeXML.

### When participant API responses return no results

The participant API returns no records under these conditions:

1. The conference has completed (all participants disconnected or session terminated).
2. A participant's call leg is no longer active (hung up).
3. The participant was explicitly removed via the [Delete a conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-conference-participant) endpoint.
4. The participant's call leg was given new TeXML instructions via the [Update call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-call) endpoint, causing it to leave the conference context.

## Queues

A queue object represents a holding area for calls, ordered by enqueue time (First-In-First-Out).

### Creating queues

Queues can be instantiated in two ways:

1. **REST API** — Explicitly created via the [Create New Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-new-queue) endpoint.
2. **`<Enqueue>` verb** — Created dynamically during call flow execution. When an [`<Enqueue>`](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue) verb references a queue name that doesn't exist, Telnyx automatically creates a new queue with default settings and adds the call to it.

### Managing queues

- [Fetch a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-queue-resource) — Returns current state including current size, average wait time, and maximum size.
- [Update a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-queue-resource) — Modify properties such as maximum allowed calls.
- [Delete a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-queue-resource) — Remove a queue from your account.
