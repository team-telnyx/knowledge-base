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

*Part 3 of 3 — see also: [Part 1](telnyx-voice-api-resources--part-1.md), [Part 2](telnyx-voice-api-resources--part-2.md)*

Covers the TeXML REST API resource types—applications, calls, conferences, queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along with the Text-to-Speech system including in-call playback and pronunciation dictionaries.

## Pronunciation Dictionaries

Pronunciation dictionaries control how specific words and phrases are spoken during TTS synthesis. They are applied automatically before speech generation—no changes to input text are required.

### Item types

Each dictionary contains up to 100 items of two types:

- **Alias (text replacement)** — Replaces matched text with alternative text before synthesis. Example: `"ASAP"` → `"as soon as possible"`.
- **Phoneme (IPA notation)** — Specifies exact pronunciation using the International Phonetic Alphabet. Example: `"GIF"` with phoneme `ɡɪf`.

### Using a dictionary

Pass the `pronunciation_dict_id` when synthesizing speech:

- **REST API** — Include `pronunciation_dict_id` in the POST body.
- **WebSocket** — Pass `pronunciation_dict_id` as a query parameter on the connection URL.

### Managing dictionaries

Dictionaries are managed via the `/v2/pronunciation_dicts` API:

- **Create** — POST with JSON items, or upload a PLS/XML or plain text file via `multipart/form-data`. Updates use optimistic locking; concurrent modifications return `409 Conflict`.
- **List** — GET with pagination (`page[number]` and `page[size]`).
- **Get** — GET by dictionary ID.
- **Update** — PATCH by dictionary ID.
- **Delete** — DELETE by dictionary ID.

### File upload formats

Two formats are supported for file uploads:

- **PLS/XML** — Standard [W3C Pronunciation Lexicon Specification](https://www.w3.org/TR/pronunciation-lexicon/) format.
- **Plain text** — Line-based format using `word=alias` for alias items and `word:/phoneme/` for IPA phonemes.

### Limits

| Limit | Value |
|---|---|
| Dictionaries per organization | 50 |
| Items per dictionary | 100 |
| Text field (match) | 200 characters |
| Alias / phoneme value | 500 characters |
| File upload | 1 MB |
