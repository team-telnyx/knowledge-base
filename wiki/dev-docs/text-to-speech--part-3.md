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

*Part 3 of 5 — see also: [Part 1](text-to-speech--part-1.md), [Part 2](text-to-speech--part-2.md), [Part 4](text-to-speech--part-4.md), [Part 5](text-to-speech--part-5.md)*

Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces (WebSocket streaming, REST API, and in-call playback) and a broad set of providers, including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra, Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider catalogue, voice formats, configuration parameters, pronunciation dictionaries, SSML support, and integration patterns for each surface.

## Third-Party Providers

### AWS Polly

**Voice format:** `aws.Polly.<Engine>.<VoiceId>`

Example: `aws.Polly.Generative.Lucia`. The engine can also be parsed from a hyphenated suffix on the voice ID — e.g., `Lucia-longform` resolves to engine `long-form`.

| Voice | Language | Gender |
| --- | --- | --- |
| `aws.Polly.Danielle-Neural` | en-US | Female |
| `aws.Polly.Gregory-Neural` | en-US | Male |
| `aws.Polly.Lucia-Generative` | es-ES | Female |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`, `ogg_vorbis`. |
| `sample_rate` | integer | — | 8000, 16000, 22050, 24000. |
| `language` | string | — | BCP-47 language code. Passed as `language_code` to Polly. |
| `text_type` | string | `text` | `text` or `ssml`. Polly supports SSML for fine-grained prosody control. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `engine` | string | `standard` | `standard`, `neural`, `generative`, `long-form`. |
| `output_format` | string | — | Any [Polly output format](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-OutputFormat). |
| `sample_rate` | string | — | e.g. `"8000"`, `"16000"`, `"22050"`, `"24000"`. Valid values depend on engine and format. |
| `lexicon_names` | array | — | Pronunciation lexicon names to apply. |
| `language_code` | string | — | BCP-47. Overrides `language` query param. |
| `text_type` | string | `text` | `text` or `ssml`. Overrides query param. |

```
{
  "text": " ",
  "voice_settings": {
    "engine": "generative",
    "output_format": "mp3",
    "sample_rate": "24000"
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `engine` | string | `standard` | `standard`, `neural`, `generative`, `long-form`. |
| `output_format` | string | — | Polly output format. |
| `sample_rate` | string | — | Sample rate in Hz. |
| `lexicon_names` | array | — | Pronunciation lexicon names. |
| `language_code` | string | — | BCP-47 language code. |
| `text_type` | string | `text` | `text` or `ssml`. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Azure Speech

**Voice format:** `azure.<VoiceId>`

Example: `azure.en-US-AvaMultilingualNeural`. No model ID segment — Azure voices are flat identifiers. Default voice: `en-US-AvaMultilingualNeural`.

| Voice | Language | Gender |
| --- | --- | --- |
| `azure.en-US-AvaMultilingualNeural` | en-US | Female |
| `azure.en-US-AndrewMultilingualNeural` | en-US | Male |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `wav`, `linear16`, `mulaw`, `alaw`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 24000, 48000. |
| `language` | string | `en-US` | BCP-47 language code. |
| `text_type` | string | `text` | `text` or `ssml`. Azure supports SSML for pronunciation and prosody control. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `output_format` | string | `audio-24khz-160kbitrate-mono-mp3` | See [Azure audio formats](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs). |
| `language_code` | string | `en-US` | BCP-47. Overrides `language` query param. |
| `text_type` | string | `text` | `text` or `ssml`. Overrides query param. |
| `effect` | string | — | `eq_car`, `eq_telecomhp8k`. Audio equalization. |
| `gender` | string | — | `Male`, `Female`. Voice gender filter. |

```
{
  "text": " ",
  "voice_settings": {
    "output_format": "audio-48khz-192kbitrate-mono-mp3",
    "effect": "eq_car"
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `output_format` | string | `audio-24khz-160kbitrate-mono-mp3` | Azure audio format string. |
| `language_code` | string | `en-US` | BCP-47 language code. |
| `text_type` | string | `text` | `text` or `ssml`. |
| `effect` | string | — | `eq_car`, `eq_telecomhp8k`. |
| `gender` | string | — | `Male`, `Female`. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### ElevenLabs

ElevenLabs requires your own API key configured in your Telnyx account. Telnyx relays requests to the ElevenLabs API — voice settings are passed through directly.

**Voice format:** `elevenlabs.<Model>.<VoiceId>`

Example: `elevenlabs.v3.Adam`. `voice_id` is a voice from **your own ElevenLabs account** — pre-built, cloned, or designed. Preview voices at [elevenlabs.io/voice-library](https://elevenlabs.io/voice-library).

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`, `mulaw`. |
| `sample_rate` | integer | — | 8000, 16000, 22050, 24000, 44100. |
| `language` | string | — | BCP-47 language code. |

**WebSocket voice settings** — relayed directly to the [ElevenLabs API](https://elevenlabs.io/docs/api-reference/text-to-speech). Any field ElevenLabs accepts can be passed here.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `model_id` | string | — | ElevenLabs model override (e.g. `eleven_multilingual_v2`). |
| `language_code` | string | — | BCP-47. Overrides `language` query param. |
| `stability` | float | — | 0.0–1.0. Voice consistency. |
| `similarity_boost` | float | — | 0.0–1.0. Clarity and similarity to original voice. |
| `style` | float | — | 0.0–1.0. Style exaggeration. |
| `use_speaker_boost` | boolean | — | Speaker boost toggle for clarity. |

```
{
  "text": " ",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0.3
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `model_id` | string | — | ElevenLabs model override. |
| `stability` | float | — | 0.0–1.0. Voice consistency. |
| `similarity_boost` | float | — | 0.0–1.0. Clarity and similarity. |
| `style` | float | — | 0.0–1.0. Style exaggeration. |
| `use_speaker_boost` | boolean | — | Speaker boost toggle. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Fish Audio

**Voice format:** `FishAudio.<Model>.<VoiceId>`

Fish Audio is a Telnyx-hosted external TTS provider. Telnyx exposes a **hand-vetted shortlist** of Fish Audio voices from their public Voice Library. Fish Audio is **cross-lingual** — any voice can speak any language from the input text. The `language` field in the voice listing is the voice's native accent only, not a synthesis constraint.

**Models:**

| Model | Description |
| --- | --- |
| `s2.1-pro` | Latest generation. Improved quality, latency, and throughput. **Default.** |
| `s2-pro` | Previous generation. Multi-speaker, expression control. |
| `s1` | Oldest generation. |

All curated voices are available under all three models.

**Curated voices:**

| Voice | Gender | Native Language | Voice ID |
| --- | --- | --- | --- |
| Aria | Female | English | `933563129e564b19a115bedd57b7406a` |
| Nova | Female | English | `b545c585f631496c914815291da4e893` |
| Paula | Female | English | `c2623f0c075b4492ac367989aee1576f` |
| Claire | Female | French | `5567200c7d8341738f0892bbacd3be3c` |
| Yuki | Female | Japanese | `5161d41404314212af1254556477c17d` |
| Ethan | Male | English | `536d3a5e000945adb7038665781a4aca` |
| Atlas | Male | English | `c5f56a6cc2ec4fa8920cb4c5889a3fb7` |
| Max | Male | English | `802e3bc2b27e49c2995d23ef70e6ac89` |
| Adrian | Male | English | `bf322df2096a46f18c579d0baa36f41d` |
| Mateo | Male | Spanish | `35199d5438854f5d9157c500479ab684` |

Only curated catalog voices are accepted for synthesis. Arbitrary Fish Voice-Library `reference_id`s cannot be used under the Telnyx API key.

**Emotion tags:** Fish Audio S2 models (`s2.1-pro`, `s2-pro`) support inline emotion, tone, and audio-effect markers placed directly in the input text. S1 uses parentheses — `(happy)` — instead of brackets. The markers are processed by the upstream Fish Audio API and do not add latency or count toward token limits.

```
[happy] What a beautiful day!
[sad] I'm sorry to hear that.
[excited] This is amazing news!
[whispering] I have a secret to share.
[laughing] That was hilarious! Ha, ha!
```

The same syntax works on both the REST endpoint and the WebSocket `text` field. Markers can be combined for layered effects — `[excited][laughing] We won! Ha ha!` — and accept intensity modifiers like `[slightly sad]`, `[very excited]`, `[extremely angry]`. For the full list of supported emotions, tone markers, audio effects, and S1 syntax, see Fish Audio's [Emotion Control guide](https://docs.fish.audio/developer-guide/core-features/emotions).

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `linear16` | `mp3`, `wav`, `linear16` (maps to PCM). |
| `sample_rate` | integer | `24000` | Depends on format (see table below). |

**WebSocket voice settings:** Fish Audio does not expose speed or pitch controls. `voice_settings` are limited to format and sample rate overrides. Emotion and tone are controlled inline in the text via bracket markers.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `format` | string | `pcm` | `mp3`, `wav`, `pcm`, `opus`. |
| `sample_rate` | integer | `24000` | Sample rate in Hz (valid values depend on format). |

```
{
  "text": " ",
  "voice_settings": {
    "format": "mp3",
    "sample_rate": 44100
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `format` | string | `pcm` | `mp3`, `wav`, `pcm`, `opus`. |
| `sample_rate` | integer | `24000` | Sample rate in Hz (valid values depend on format). |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

**Audio formats and sample rates:**

| Format | Accepted Sample Rates (Hz) |
| --- | --- |
| `pcm` | 8000, 16000, 24000, 32000, 44100 |
| `wav` | 8000, 16000, 24000, 32000, 44100 |
| `mp3` | 32000, 44100 |
| `opus` | 48000 |

On WebSocket, the `audio_format` query parameter and `voice_settings.format` are independent parameters with different vocabularies. The `audio_format` query param accepts `mp3`, `wav`, and `linear16` (which maps to `pcm`). The `voice_settings.format` field accepts `mp3`, `wav`, `pcm`, and `opus` directly. If both are set, `voice_settings.format` takes precedence.

Fish Audio is available for in-call TTS via Call Control `speak` and TeXML `<Say>`. For telephony playback, the gateway automatically delivers MP3 at 44.1 kHz to ensure correct resampling by the call-control audio pipeline.

See also: [Fish Audio API Reference](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech), [Fish Audio Voice Library](https://fish.audio/).

### Inworld

**Voice format:** `inworld.<Model>.<VoiceId>`

**Models:**

- `inworld-tts-1.5-mini` (alias `Mini`) — faster, lower latency.
- `inworld-tts-1.5-max` (alias `Max`) — higher quality.
- `inworld-tts-2` (alias `TTS2`) — latest generation; supports the `delivery_mode` parameter.

Defaults to `inworld-tts-1.5-mini` if model omitted.

| Voice | Model | Gender |
| --- | --- | --- |
| `Inworld.Max.Hank` | Max | Male |
| `Inworld.Mini.Loretta` | Mini | Female |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000. |
| `language` | string | — | BCP-47 language code. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `encoding` | string | `MP3` | `MP3` or `LINEAR16`. |
| `sample_rate` | integer | `24000` | Output sample rate in Hz. |
| `language_code` | string | — | BCP-47. Overrides `language` query param. |
| `delivery_mode` | string | — | `STABLE`, `BALANCED`, or `CREATIVE`. Only supported by `inworld-tts-2`. |

```
{
  "text": " ",
  "voice_settings": {
    "encoding": "LINEAR16",
    "sample_rate": 16000
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `encoding` | string | `MP3` | `MP3` or `LINEAR16`. |
| `sample_rate` | integer | `24000` | Output sample rate in Hz. |
| `language_code` | string | — | BCP-47 language code. |
| `delivery_mode` | string | — | `STABLE`, `BALANCED`, or `CREATIVE`. Only supported by `inworld-tts-2`. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Minimax

**Voice format:** `minimax.<Model>.<VoiceId>`

`voice_id` can be a **system voice** (pre-built) or a **cloned voice** from the [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab) (organization-scoped).

| Voice | Gender |
| --- | --- |
| `Minimax.speech-2.8-turbo.English_expressive_narrator` | Male |
| `Minimax.speech-2.8-turbo.English_radiant_girl` | Female |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 32000, 44100. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `speed` | float | — | Playback speed multiplier. |
| `vol` | float | — | Volume level. |
| `pitch` | integer | — | Pitch adjustment. |
| `language_boost` | string | — | Language emphasis for multilingual synthesis. |

```
{
  "text": " ",
  "voice_settings": {
    "speed": 1.1,
    "vol": 1.0,
    "pitch": 0
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `speed` | float | — | Playback speed multiplier. |
| `vol` | float | — | Volume level. |
| `pitch` | integer | — | Pitch adjustment. |
| `language_boost` | string | — | Language emphasis. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Resemble

**Voice format:** `resemble.Turbo.<VoiceId>`

Default model: `Turbo`. `voice_id` is a voice from **your own Resemble account**.

| Voice | Language | Gender |
| --- | --- | --- |
| `Resemble.Turbo.Aaron_en-US` | en-US | Male |
| `Resemble.Turbo.Amelia_en-US` | en-US | Female |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `wav`. |
| `sample_rate` | integer | `48000` | 8000, 16000, 22050, 32000, 44100, 48000. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `format` | string | `mp3` | `mp3` or `wav`. |
| `precision` | string | `PCM_32` | `PCM_16`, `PCM_24`, `PCM_32`, `MULAW`. |
| `sample_rate` | string | `48000` (mp3) / `16000` (wav) | `8000`, `16000`, `22050`, `32000`, `44100`, `48000`. Default depends on format. |

```
{
  "text": " ",
  "voice_settings": {
    "format": "wav",
    "precision": "PCM_16",
    "sample_rate": "22050"
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `format` | string | `mp3` | `mp3` or `wav`. |
| `precision` | string | `PCM_32` | `PCM_16`, `PCM_24`, `PCM_32`, `MULAW`. |
| `sample_rate` | string | `48000` / `16000` | Sample rate. Default depends on format. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Rime

**Models:**

| Model | Description | Languages |
| --- | --- | --- |
| Coda | Rime's flagship model (May 2026). LLM backbone + speech engine, sub-100ms latency, 184 voices, top-rated quality. | en, es, fr, pt, de, ja |
| ArcanaV3 | Previous flagship. Expressive, multilingual codeswitching. | ar, en, fr, de, he, hi, ja, pt, es, ta |

**Voice format:**

```
Rime.Coda.<VoiceId>
Rime.ArcanaV3.<VoiceId>
```

Coda is Rime's recommended model for new integrations. It surpasses ArcanaV3 in naturalness, prosody, and artifact-free output.

| Voice | Language | Gender |
| --- | --- | --- |
| `Rime.Coda.albion` | en-US | Male |
| `Rime.Coda.luna` | en-US | Female |
| `Rime.ArcanaV3.albion` | en-US | Male |
| `Rime.ArcanaV3.arcade` | en-US | Male |

**WebSocket query parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000, 96000. |

**WebSocket voice settings:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |

```
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 0.9
  }
}
```

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default response (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
