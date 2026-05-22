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

*Part 2 of 2 — see also: [Part 1](texml-rest-api-objects-and-lifecycles--part-1.md)*

Overview of TeXML REST API resources—what each object represents, how it’s created during call flows or via API, and where to manage or retrieve them (calls, conferences, participants, queues, recordings, transcripts, SIPREC sessions, streams, application configs, and secrets).

## Streams
- Definition: A stream object represents an active WebSocket audio streaming session from a call.
- Creation:
  - Start via REST at any time during a call [Start streaming](https://developers.telnyx.com/api-reference/texml-rest-commands/start-streaming-media-from-a-call).
  - Start via TeXML `<Stream>`:
    - Asynchronous when nested in `<Start>` (streaming proceeds in parallel) [<Stream>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream), [<Start>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start)
    - Synchronous when nested in `<Connect>` (call flow waits until streaming stops) [<Connect>](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect)
- Management:
  - Update or stop streaming via REST; when stopped, the stream completes and WebSockets close [Update/stop](https://developers.telnyx.com/api-reference/texml-rest-commands/update-streaming-on-a-call)

## TeXML application secrets
- Definition: Secure storage and retrieval for sensitive values (credentials, API keys, tokens) that should not be embedded in TeXML or source code. Tutorial on using secrets in HTTP requests: [Guide](https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests#using-secrets).
- Creation:
  - Create a TeXML secret via REST [Create secret](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-texml-secret)

## See also
- Complete TeXML documentation index: https://developers.telnyx.com/llms.txt
