---
title: 'TeXML REST API: Objects and Lifecycles'
summary: Overview of TeXML REST API resources—what each object represents, how it’s
  created during call flows or via API, and where to manage or retrieve them (calls,
  conferences, participants, queues, recordings, transcripts, SIPREC sessions, streams,
  application configs, and secrets).
sources:
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/applications/index
  content_hash: 82e50d11ac379406c79a06eeb1ff8d7055e2f1a0daa4fa5c1caba6261471b2a2
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
  content_hash: 9514c9e53e749ea8198f47936b07c16a1d29e154af9f127bdf27c504d1057197
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
  content_hash: 94f199669fdfd51db66224c9a030343b1844f989e4a3bfacd88f9834aecd4a34
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
  content_hash: a79c94ba8efd452866bfd7f156c81814f5398f51289135500e050a1dd48d65d6
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
  content_hash: 6d92463b4dae01353d953ed14ea1e150d4b6a318edd0e95d0c68d614d1236a45
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
  content_hash: c562fcd18fdce694f8e8f87f9cfdd0fb2fc1a5c1720a4fb14cd35283d757e6aa
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/secrets/index
  content_hash: 3c191ea3dae89e0fd013e8f3bdfb28e452f80dfef2bfb9cc8878c2186173adda
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
  content_hash: 24a0aa131be13db3b8c908d5ad86852898f39a58402702a04ab1045c6370150d
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
  content_hash: ec4da41250ed97cd22a51e232a217dc0cdcea4756d030298e6417a962ae45a51
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
  content_hash: 34bdc455abcdbbff2fd4267b03e8d6062e514b5fe12b3c49d40bfb9b79e36074
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
