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

*Part 1 of 3 — see also: [Part 2](texml-rest-api-resources--part-2.md), [Part 3](texml-rest-api-resources--part-3.md)*

Overview of the core resource objects exposed by the Telnyx TeXML REST API, including applications, calls, conferences, queues, recordings, secrets, SIPREC sessions, streams, and transcripts, with details on how each resource is created, managed, and retrieved.

## Applications

A TeXML application defines how inbound and outbound calls are handled using TeXML instructions. Each TeXML application instance encapsulates a set of configuration parameters that control call behavior, instruction retrieval, and webhook interactions. These parameters determine where Telnyx fetches TeXML from, how call events are handled, and how call flows are executed. See [TeXML Application](texml-application.md) for more details.

## Calls

A call object represents a single call leg. It contains all state, metadata, and lifecycle information of that call leg.

A call object is instantiated in the following situations:

1. When an outbound call is initiated through the [REST API](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call). Telnyx immediately creates a call resource to represent this outbound call.
2. When an inbound call reaches a phone number assigned to a TeXML application. Before processing any TeXML, a call resource is created to represent the inbound call itself. At that point, the call is answered and the instruction fetch request is sent. The lifecycle of this inbound call is driven by the instructions defined in the TeXML response.
3. When a [Dial](dial.md) verb is executed inside a TeXML script. Each execution of `<Dial>` creates a new call resource. This call is logically associated with the parent call that initiated the TeXML request, and Telnyx manages both calls as part of a multi-leg call flow if needed.

The details of a call can be retrieved using the [calls endpoint](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-call) up to 30 days after the call has ended.

## Conferences

A conference object represents a multi-participant audio session.

A conference is instantiated when a `<Dial>` to a non-existent [Conference](conference.md) is executed. When Telnyx processes a TeXML response that includes a [Dial](dial.md) verb with a `<Conference>` noun, it attempts to place the current call into a named conference.

Once instantiated, conferences can be managed via REST API endpoints, including:

- [Fetch a conference resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-conference-resource)
- [List all conferences](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-resources)
- [Update a conference](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-conference-resource)
- [List associated recordings](https://developers.telnyx.com/api-reference/texml-rest-commands/list-conference-recordings)

## Conference Participants

A conference participant object represents an individual call leg that has been added to a conference.

A conference participant is instantiated in the following situations:

1. When a new participant is dialed and added to a conference via the REST API ([dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant)). When your application requests to dial a new party into an existing conference using the REST API, a conference participant resource for the new call leg is created.
2. When a call leg is added to a conference via `<Dial>` with `<Conference>` in TeXML ([Conference](conference.md)). When a TeXML `<Dial>` verb that contains a `<Conference>` element is executed, the call leg joins the specified conference. At that point, Telnyx creates a conference participant object associated with that call leg.

Certain situations cause the participant API to return no participant records, even if the call or conference previously existed. Telnyx will return no participant objects under the following conditions:

1. The conference has been completed. Once a conference ends (e.g., all participants disconnect or the session is terminated), Telnyx no longer returns participant objects associated with that completed conference.
2. A participant's call leg is no longer active (i.e., has been hung up). If a participant disconnects — whether intentionally, due to call failure, or because of application logic — their call leg is considered complete, and the participant object is no longer returned by the API.
3. The participant has been explicitly removed via the REST API ([delete a conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-conference-participant)).
4. The participant's call leg has been given new TeXML instructions via the REST API ([update call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-call)). If a call leg that was previously in a conference is updated with new TeXML instructions via the REST API, it effectively leaves the conference context. As a result, it is no longer included in participant API responses.

## Queues

A queue object represents a holding area for calls. Calls in a queue are ordered by the time they were enqueued (First-In-First-Out).

There are two ways to instantiate a new queue:

1. Using the REST API. A queue can be explicitly created by sending a request to the [Create New Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-new-queue) endpoint.
2. Using the [Enqueue](enqueue.md) verb. A queue can also be created dynamically during call flow execution. When an `<Enqueue>` verb is executed inside a TeXML script with a specific queue name, Telnyx checks if a queue with that name already exists. If the queue exists, the call is added to it. If it does not exist, a new queue is automatically created with default settings, and the call is then added.

Once a queue is instantiated, it can be managed using the TeXML REST API:

- **[Fetch a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-queue-resource)** — Get detailed information about a specific queue by its Queue SID or name. This returns the current state, including the number of calls currently waiting (current size), the average wait time, and the maximum size configuration.
- **[Update a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/update-a-queue-resource)** — Modify the properties of an existing queue. For example, you can change the maximum number of allowed calls (max size) to prevent overloading the system.
- **[Delete a Queue](https://developers.telnyx.com/api-reference/texml-rest-commands/delete-a-queue-resource)** — Remove a queue from your account.
