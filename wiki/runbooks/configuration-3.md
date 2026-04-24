---
title: Configuration
summary: Query parameters and voice settings — two configuration surfaces for WebSocket TTS.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
    content_hash: a04c371874640cf8125d7478ab36485c77456486c430e812d12eecd1a3003165
updated_at: 2026-04-10T00:00:00Z
---

# Configuration

Query parameters and voice settings — two configuration surfaces for WebSocket TTS.

## Two Configuration Surfaces

| Surface          | When                         | What                                                           | Mutable?               |
| ---------------- | ---------------------------- | -------------------------------------------------------------- | ---------------------- |
| Query parameters | WebSocket URL                | Voice selection, audio format, sample rate, connection options | No — locked at connect |
| `voice_settings` | Init frame (`{"text": " "}`) | Provider-specific tuning (speed, pitch, format, etc.)          | No — locked at init    |

Both are one-shot. After the init frame, no configuration can change for the session. To change settings, open a new connection.

## Query Parameters

Set on the URL at connect time. Immutable for the session.

### Voice Selection

| Parameter | Type   | Default | Description                                          |
| --------- | ------ | ------- | ---------------------------------------------------- |
| `voice`   | string | —       | Voice identifier in `Provider.Model.VoiceId` format. |

The `voice_id` segment (third part of the `voice` string) refers to different things depending on the provider and model:

| Type                    | Example                        | How you get it                                                                                                                                                                                                                   |
| ----------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pre-built voice**     | `Telnyx.NaturalHD.astra`       | Browse via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech/list-voices) or [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab). Shipped by the provider — available to everyone. |
| **Your cloned voice**   | `Telnyx.Qwen3TTS.my-ceo-clone` | Create in the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab). Scoped to your organization — only your API key can use it. Available for Qwen3TTS and Minimax.                                           |
| **BYOK provider voice** | `elevenlabs.v3.Adam`           | A voice ID from your own ElevenLabs or Resemble account. You bring your own API key; Telnyx relays the request.                                                                                                                  |

The Voices API (`GET /v2/ai/tts/voices`) returns all voices available to your account — pre-built and cloned — with each voice's compound `id` ready to use as the `voice` parameter.

### Connection Options

| Parameter      | Type    | Default          | Description                                                                                                                                                    |
| -------------- | ------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `language`     | string  | —                | BCP-47 language code. Passed to the provider as `language_code`. Only used by providers that accept it (AWS Polly, Azure, ElevenLabs, Inworld).                |
| `text_type`    | string  | `text`           | Text type hint: `text` or `ssml`. Only AWS Polly and Azure use this.                                                                                           |
| `audio_format` | string  | `mp3`            | Output audio format: `mp3`, `linear16`, `wav`, `mulaw`, `alaw`, `ogg_vorbis`. Not all formats are supported by every provider — see providers dedicated pages. |
| `sample_rate`  | integer | provider default | Output sample rate in Hz. Accepted values vary by provider — see providers dedicated pages.                                                                    |

\| `disable_cache` | boolean | `false` | Bypass the audio cache and always synthesize fresh. |

### Example

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=linear16&disable_cache=true
```

## Voice Settings

Provider-specific tuning (speed, pitch, format, emotion, etc.) is not set via query parameters. It is passed once in the `voice_settings` object on the [initialization frame](lifecycle-2.md#2-streaming):

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2,
    "emotion": "happy"
  }
}
```

Voice settings are applied when the synthesis worker starts and cannot be changed mid-session.

**There are no common voice\_settings fields.** Every field is provider-specific — the available fields, defaults, and accepted values are completely different per provider. Unrecognized fields are silently ignored. See your selected provider's page under [Providers](telnyx.md) for the exact fields.


## Related Pages

- [Configuration](../runbooks/configuration.md)
- [Configuration](../runbooks/configuration-2.md)
- [AnchorSite Configuration](../runbooks/anchorsite-configuration.md)
