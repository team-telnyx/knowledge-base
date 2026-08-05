---
title: Telnyx Programmable Voice
summary: A consolidated reference for Telnyx Programmable Voice covering the Voice
  API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression,
  Transcription), Text-to-Speech providers, and the European regional endpoint.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
updated_at: 2026-08-05T14:05:29Z
---

# Telnyx Programmable Voice

*Part 5 of 5 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 2](telnyx-programmable-voice--part-2.md), [Part 3](telnyx-programmable-voice--part-3.md), [Part 4](telnyx-programmable-voice--part-4.md)*

A consolidated reference for Telnyx Programmable Voice covering the Voice API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression, Transcription), Text-to-Speech providers, and the European regional endpoint.

## Voice API Services in Europe

Telnyx provides a dedicated European endpoint at `https://api.telnyx.eu` to reduce latency for calls held in Europe. To receive Voice API calls in Europe, set the AnchorSite® for the application to one of the European Anchorsites — Frankfurt, London, or Amsterdam. All participants of conferences and calls added to a queue must be in the same region.

```bash
curl --location --request POST 'https://api.telnyx.com/v2/calls' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data-raw '{
    "to":"+18727726004",
    "from":"+18022455739",
    "connection_id":"1684641123236054244"
    }'
```

## Next Steps

After the basics are in place, explore advanced features such as AI assistants, speech recognition, media streaming, TeXML scripting, answering machine detection, and IVR/call center/call tracking tutorials. Official SDKs are available for Node.js, Python, PHP, Ruby, and Java.
