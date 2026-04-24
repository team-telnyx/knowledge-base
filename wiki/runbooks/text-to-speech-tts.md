---
title: Text-to-Speech (TTS)
summary: TTS models and voices available through Telnyx for LiveKit voice agents.
sources:
  - url: https://developers.telnyx.com/docs/livekit/models/tts
    content_hash: 26afdd0265b404df189b46f8a4698e5d185a345162926aa827e34cba7609d66a
updated_at: 2026-04-10T00:00:00Z
---

# Text-to-Speech (TTS)

TTS models and voices available through Telnyx for LiveKit voice agents.

Telnyx offers an extensive library of voices across multiple providers and models, with broad language and accent support. Access them through the Telnyx plugin:

```python theme={null}
from livekit.plugins import telnyx

tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

## Voice ID format

Voice IDs follow the pattern `Provider.Model.voice_name`. To find a voice:

1. Browse the [voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index)
2. Copy the voice ID (e.g. `Telnyx.NaturalHD.astra`)
3. Pass it to `telnyx.TTS(voice="...")`

## Examples

```python theme={null}


## Related Pages

- [Text-to-Speech](../runbooks/text-to-speech.md)
- [Text-to-Speech Overview](../concepts/text-to-speech-overview.md)
