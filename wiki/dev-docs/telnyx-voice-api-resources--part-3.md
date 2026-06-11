---
title: Telnyx Voice API Resources
summary: Covers the TeXML REST API resource types—applications, calls, conferences,
  queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along
  with the Text-to-Speech system including in-call playback and pronunciation dictionaries.
sources:
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/applications/index
  content_hash: f2dc8ac0555aca4b1bc5cd8f6f0026e03d4f9302d0673a200734b2d78307ae27
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
  content_hash: c4a93404708f0041869ea616e4776fee88b838677ab29bb77da46c5c37443fb1
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
  content_hash: 3dface952c3f9b06f20ab0ecca13b7b27503ed79861f155f05e97188a61dd5d2
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
  content_hash: dd9e4f35eadb36349dbcb062174031b45f97dbc4d52ca9ad93e1c9430a28d5f9
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
  content_hash: 0b2aa6aa69905f12a4ea2a55bae0611bdedb35eadd23bff1b524e92e38693f6a
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
  content_hash: 562e866ba4e13aa4db303517917af30a402332f8c15aeb07d5ee0c8102522a21
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/secrets/index
  content_hash: 337a951a0d85b95e330c046de3232278072c410693f92ee6657c029a50fff146
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
  content_hash: 725be89e6deaff2d5e5a1a563d27ed8bc11e925d73b65a7a1e24d65434bb5bf9
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
  content_hash: 56e64cf84743db7b33171b5fe084e558dcac20f2ec451806613bf05171639417
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
  content_hash: b323b65fe70abd1d1e4219d06bf9bd1882014e5d2fc5e4fd7fce97ca71dc24cb
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
  content_hash: de08a5759d5522f0e6336ebfdcbffa6cf8b693a345982cb4c53cd65d42f8b6b3
- url: https://developers.telnyx.com/docs/voice/tts/overview/index
  content_hash: 0e4dafb6ba3146321a9be9ed2b4904eacdc54b2f5f88d57eb662abe749ab6054
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
  content_hash: d8aa81fc59d3ddfffb8692e4e6e6f0671d67f8be426d479a7953913d5b6803fd
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
