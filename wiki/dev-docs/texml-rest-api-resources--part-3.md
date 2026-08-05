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

*Part 3 of 3 — see also: [Part 1](texml-rest-api-resources--part-1.md), [Part 2](texml-rest-api-resources--part-2.md)*

Overview of the core resource objects exposed by the Telnyx TeXML REST API, including applications, calls, conferences, queues, recordings, secrets, SIPREC sessions, streams, and transcripts, with details on how each resource is created, managed, and retrieved.

## Transcripts

A transcription can be enabled from TeXML in two scenarios:

1. When a [Transcription](transcription.md) verb is executed in TeXML. When Telnyx processes a TeXML document containing the `<Transcription>` verb, it initiates an audio capture operation based on the parameters defined in that verb. Once the audio is captured and processed, a transcription is provided in status callbacks in real-time.
2. When a [Record](record.md) verb is executed with transcription attributes. If a TeXML `<Record>` verb includes transcription-related attributes, Telnyx performs transcription on the recorded audio once the recording is complete.

Upon completion of the transcription process, a transcription object representing the text output associated with that recording segment is created and can be retrieved using the [Fetch a recording transcription resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-recording-transcription-resource) endpoint.
