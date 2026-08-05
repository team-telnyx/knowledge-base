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

*Part 5 of 5 — see also: [Part 1](text-to-speech--part-1.md), [Part 2](text-to-speech--part-2.md), [Part 3](text-to-speech--part-3.md), [Part 4](text-to-speech--part-4.md)*

Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces (WebSocket streaming, REST API, and in-call playback) and a broad set of providers, including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra, Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider catalogue, voice formats, configuration parameters, pronunciation dictionaries, SSML support, and integration patterns for each surface.

## SSML Tags

Speech Synthesis Markup Language (SSML) is an XML-based markup language used to generate synthetic speech for applications. SSML tags change the tone of speech by adjusting pitch, volume, duration, and more. SSML is supported by AWS Polly and Azure (set `text_type: "ssml"`).

### Adding a Pause

**SSML Tag:** `<break> </break>`

There are two ways to define the length of the pause:

1. **Time** — defines the number of seconds or milliseconds.
2. **Strength** — chooses the strength using the following values:
   - `none` — no pause
   - `pause` — the same duration as after a period
   - `x-weak` — the same as none
   - `weak` — sets a pause of the same duration as the pause after a comma
   - `medium` — has the same strength as weak
   - `strong` — sets a pause of the same duration as the pause after a sentence
   - `x-strong` — sets a pause of the same duration as the pause after a paragraph

Example:

```
<speak> Mary had a little lamb <break time="3s"/>Whose fleece was white as snow. </speak>
```

### Emphasizing Words

**SSML Tag:** `<emphasis> </emphasis>`

The emphasis affects the speed and loudness of reading words and can be defined by using a `level` attribute with one of the following values:

1. `strong` — increases the volume and slows the speaking rate
2. `moderate` — increases the volume and slows the speaking rate, but less than Strong
3. `reduced` — decreases the volume and speeds up the speaking rate

Example:

```
<speak> I already told you we're <emphasis level="strong">nearly</emphasis> there </speak>
```

### Set a Different Language

**SSML Tag:** `<lang> </lang>`

The `xml:lang` tag defines the language for a specific word or sentence.

Example:

```
<speak> <xml:lang="es">Puedo hablar español</xml:lang="es"> </speak>
```

### Adding a Pause Between Paragraphs

**SSML Tag:** `<p> </p>`

This tag adds a pause between paragraphs that is longer than a regular pause at a comma or at the end of the sentence.

Example:

```
<speak>
<p>This is the first paragraph.</p> <p>This is the second paragraph.</p>
</speak>
```

### Using Phonetic Pronunciation

**SSML Tag:** `<phoneme> </phoneme>`

The phonetic pronunciation requires two attributes:

1. **Alphabet** — `ipa` (International Phonetic Alphabet) or `x-sampa` (Extended Speech Assessment Methods Phonetic Alphabet).
2. **ph** — specifies how the text should be pronounced.

Example:

```
<speak>Say <phoneme alphabet="ipa" ph="prəˌnʌnsɪˈeɪʃ(ə)n">pronunciation</phoneme>. </speak>
```

### Controlling Volume, Speaking Rate, and Pitch

**SSML Tag:** `<prosody> </prosody>`

The following attributes can be used with the Prosody tag:

1. **Volume** — `default`, `silent`, `x-soft`, `soft`, `medium`, `loud`, `x-loud`, or `+ndB` / `-ndB` for relative changes.
2. **Rate** — `x-slow`, `slow`, `medium`, `fast`, `x-fast`, or `n%` for a percentage change in speaking pace.

Example:

```
<speak>
Sometimes some words need to be said <prosody volume="loud">louder</prosody> and sometimes a lower volume <prosody volume="-6dB">is a more effective way of interacting with your audience. </prosody> 
</speak>
```

### Adding a Pause Between Sentences

**SSML Tag:** `<s> </s>`

This tag adds a pause between lines with the same effect as a period.

Example:

```
<speak>
<s>Here we go round the mulberry bush</s>
<s>On a cold and frosty morning</s>
</speak>
```

### Controlling How Special Words Are Spoken

**SSML Tag:** `<say-as> </say-as>`

The `say-as` tag uses one attribute, `interpret-as`, which uses a number of possible available values:

- `characters` or `spell-out`
- `cardinal` or `number`
- `digits`
- `fraction`
- `unit`
- `date`
- `time`
- `address`
- `telephone`

Example:

```
<speak><say-as interpret-as="telephone">+19999999</say-as></speak>
```

### Pronouncing Acronyms and Abbreviations

**SSML Tag:** `<sub> </sub>`

This tag should be used with the `alias` attribute to substitute a different word for selected text such as an acronym or abbreviation.

Example:

```
<speak> My favorite chemical element is <sub alias="Mercury">Hg</sub>, because it looks so shiny. </speak>
```

## Voice Design

Clone and design custom voices. Available on select providers: Qwen3TTS, Minimax, ElevenLabs, Resemble. Manage custom voices via the [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab) portal.
