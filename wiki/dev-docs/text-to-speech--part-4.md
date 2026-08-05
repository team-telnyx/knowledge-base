---
title: Text-to-Speech
summary: Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces
  (WebSocket streaming, REST API, and in-call playback) and a broad set of providers,
  including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra,
  Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax,
  MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider
  catalogue, voice formats, configuration parameters, pronunciation dictionaries,
  SSML support, and integration patterns for each surface.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
- url: https://developers.telnyx.com/docs/voice/tts/overview
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/ssml-tags
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
- url: https://developers.telnyx.com/docs/voice/tts/providers/fishaudio
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/bayan
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
updated_at: 2026-08-05T14:07:22Z
---

# Text-to-Speech

*Part 4 of 5 — see also: [Part 1](text-to-speech--part-1.md), [Part 2](text-to-speech--part-2.md), [Part 3](text-to-speech--part-3.md), [Part 5](text-to-speech--part-5.md)*

Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces (WebSocket streaming, REST API, and in-call playback) and a broad set of providers, including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra, Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider catalogue, voice formats, configuration parameters, pronunciation dictionaries, SSML support, and integration patterns for each surface.

## In-Call Playback

In-call TTS plays synthesized speech during live voice calls. Two integration paths:

### Voice API

Use the [`speak`](/api-reference/call-commands/speak-text) command to play TTS on an active call:

```
curl --location 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
  "voice": "Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41"
}'
```

See [Voice API](voice-api.md) docs for the full command reference.

### TeXML

Use the `<Say>` element:

```
<Response>
  <Say voice="Telnyx.NaturalHD.astra">Your appointment is confirmed for tomorrow at 3 PM.</Say>
</Response>
```

See [TeXML](texml.md) docs for the full `<Say>` reference.

### AI Assistants

[AI Assistants](ai-assistants.md) use TTS for voice output. Configure the voice model in assistant settings.

### Voice Selection

In-call TTS uses the same voice format as WebSocket and REST:

```
Provider.Model.VoiceId
```

All models (including Ultra) are available for in-call playback.

## Pronunciation Dictionaries

Pronunciation dictionaries let you control how specific words and phrases are spoken during text-to-speech synthesis. Dictionaries are applied automatically before speech generation — no changes to your text input required.

### Item Types

Each dictionary contains up to 100 items. Two types are supported:

**Alias (text replacement)** — replaces matched text with alternative text before synthesis:

```
{
  "text": "ASAP",
  "type": "alias",
  "alias": "as soon as possible"
}
```

**Phoneme (IPA notation)** — specifies exact pronunciation using the International Phonetic Alphabet:

```
{
  "text": "GIF",
  "type": "phoneme",
  "phoneme": "ɡɪf",
  "alphabet": "ipa"
}
```

### Using a Dictionary

Pass the dictionary ID when synthesizing speech.

**REST API:**

```
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech/speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "text": "Welcome to Telnyx.",
  "voice": "Telnyx.Ultra.002622d8-19d0-4567-a16a-f99c7397c062",
  "pronunciation_dict_id": "c215a3e1-be41-4701-97e8-1d3c22f9a5b7"
}'
```

**WebSocket:** pass `pronunciation_dict_id` as a query parameter on the connection URL:

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Ultra.002622d8-19d0-4567-a16a-f99c7397c062&pronunciation_dict_id=c215a3e1-be41-4701-97e8-1d3c22f9a5b7
```

### Managing Dictionaries

**Create a dictionary:**

```
curl --request POST \
  --url https://api.telnyx.com/v2/pronunciation_dicts \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "My Dictionary",
  "items": [
    {
      "text": "Telnyx",
      "type": "phoneme",
      "phoneme": "ˈtɛl.nɪks",
      "alphabet": "ipa"
    },
    {
      "text": "GIF",
      "type": "phoneme",
      "phoneme": "ɡɪf",
      "alphabet": "ipa"
    },
    {
      "text": "ASAP",
      "type": "alias",
      "alias": "as soon as possible"
    },
    {
      "text": "BTW",
      "type": "alias",
      "alias": "by the way"
    },
    {
      "text": "SQL",
      "type": "alias",
      "alias": "sequel"
    },
    {
      "text": "meeting",
      "type": "alias",
      "alias": "3:00 PM"
    }
  ]
}'
```

You can also upload a PLS/XML or plain text file via `multipart/form-data` instead of providing items as JSON. Plain text format:

```
Telnyx:/ˈtɛl.nɪks/
GIF:/ɡɪf/
ASAP=as soon as possible
BTW=by the way
SQL=sequel
meeting=3:00 PM
```

**List dictionaries:**

```
curl --url 'https://api.telnyx.com/v2/pronunciation_dicts?page[number]=1&page[size]=20' \
  --header 'Authorization: Bearer <token>'
```

**Get a dictionary:**

```
curl --url https://api.telnyx.com/v2/pronunciation_dicts/{id} \
  --header 'Authorization: Bearer <token>'
```

**Update a dictionary:**

```
curl --request PATCH \
  --url https://api.telnyx.com/v2/pronunciation_dicts/{id} \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "Brand Names v2",
  "items": [
    {
      "text": "Telnyx",
      "type": "alias",
      "alias": "tel-nicks"
    }
  ]
}'
```

Updates use optimistic locking — if the dictionary was modified concurrently, the request returns `409 Conflict`. Re-fetch and retry.

**Delete a dictionary:**

```
curl --request DELETE \
  --url https://api.telnyx.com/v2/pronunciation_dicts/{id} \
  --header 'Authorization: Bearer <token>'
```

### Limits

| Limit | Value |
| --- | --- |
| Dictionaries per organization | 50 |
| Items per dictionary | 100 |
| Text field (match) | 200 characters |
| Alias / phoneme value | 500 characters |
| File upload | 1 MB |

### File Upload Formats

When creating a dictionary via file upload, two formats are supported.

**PLS/XML** — standard [W3C Pronunciation Lexicon Specification](https://www.w3.org/TR/pronunciation-lexicon/) format:

```
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
  xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
  alphabet="ipa"
  xml:lang="en-US">
  <!-- Alias examples (text replacement) -->
  <lexeme>
    <grapheme>Telnyx</grapheme>
    <alias>tel-nicks</alias>
  </lexeme>
  <lexeme>
    <grapheme>SQL</grapheme>
    <alias>sequel</alias>
  </lexeme>
  <lexeme>
    <grapheme>IEEE</grapheme>
    <alias>I triple E</alias>
  </lexeme>
  <!-- IPA phoneme examples -->
  <lexeme>
    <grapheme>nginx</grapheme>
    <phoneme>ɛndʒɪnɛks</phoneme>
  </lexeme>
  <lexeme>
    <grapheme>kubectl</grapheme>
    <phoneme>kuːbkʌtəl</phoneme>
  </lexeme>
  <lexeme>
    <grapheme>Kubernetes</grapheme>
    <phoneme>kuːbɚnɛtɪz</phoneme>
  </lexeme>
</lexicon>
```

**Plain text** — line-based format:

- `word=alias` for alias items
- `word:/phoneme/` for IPA phonemes
