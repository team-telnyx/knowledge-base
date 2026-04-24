---
title: Transcripts
summary: Access and manage TeXML call transcriptions.
sources:
  - url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
    content_hash: 5556ceba9d7c35067bd50877cb9c0b3ba9ebce1d2868fef57f3e94397f2ee1fe
updated_at: 2026-04-10T00:00:00Z
---

# Transcripts

Access and manage TeXML call transcriptions.

## Transcription Creation

A transcription can be enabled from TeXML in 2 scenarios:

1\. When a `` verb is executed in TeXML
Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription)

When Telnyx processes a TeXML document containing the `` verb, it initiates an audio capture operation based on the parameters defined in that verb. Once the audio is captured and processed, a transcription is provided in statuscallbacks in real-time.

2\. When a `` verb is executed with transcription attributes
Documentation: [``](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record)

If a TeXML `` verb includes transcription-related attributes, Telnyx performs transcription on the recorded audio once the recording is complete.

## Retrieving recording transcription

Upon completion of the transcription process, a transcription object representing the text output associated with that recording segment is created and can be retrieved using the following endpoint: [Fetch a recording transcription resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-recording-transcription-resource)
