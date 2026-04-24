---
title: In-Call Transcription
summary: Real-time speech-to-text during live Telnyx voice calls via Voice API or TeXML.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
    content_hash: 99dd59b63f0f21d9f5694770bbe86c5cb210ecbf1847d9d98ee36f09350067d6
updated_at: 2026-04-10T00:00:00Z
---

# In-Call Transcription

Real-time speech-to-text during live Telnyx voice calls via Voice API or TeXML.

In-call transcription enables real-time STT on live voice calls. The audio codec is managed by the Telnyx platform — no format configuration needed.

Two integration paths:

* **Voice API** — `transcription_start` / `transcription_stop` commands on active calls. See the [Voice API STT guide](speech-to-text-with-voice-api-and-texml.md#voice-api).
* **TeXML** — XML-based call flow with transcription directives. See the [TeXML transcription guide](speech-to-text-with-voice-api-and-texml.md#texml).

Engine selection (Telnyx, Google, Deepgram, Azure) is specified as a parameter on the transcription command. Same engines as [WebSocket streaming](engines-models.md).


## Related Pages

- [Transcription](../runbooks/transcription.md)
- [Transcription Settings](../runbooks/transcription-settings.md)
