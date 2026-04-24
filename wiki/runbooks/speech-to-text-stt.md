---
title: Speech-to-Text (STT)
summary: STT models available through Telnyx for LiveKit voice agents.
sources:
  - url: https://developers.telnyx.com/docs/livekit/models/stt
    content_hash: dec24a88638bcaf2db27cbd75248de4236ee9f0846d173978a59abfb9108e080
updated_at: 2026-04-10T00:00:00Z
---

# Speech-to-Text (STT)

STT models available through Telnyx for LiveKit voice agents.

Telnyx hosts Deepgram models on dedicated GPUs. Access them through the Telnyx plugin:

```python theme={null}
from livekit.plugins import telnyx

stt = telnyx.deepgram.STT(model="nova-3", language="en")
```

> **Note:** The plugin provides two STT classes:
> 
>   * **`telnyx.deepgram.STT`** — Recommended. Connects to Deepgram models hosted on Telnyx GPUs. Takes a `model` parameter (`nova-3`, `nova-2`, `flux`).
>   * **`telnyx.STT`** — Connects to Telnyx's own transcription engine (default) or Deepgram via `transcription_engine="Deepgram"`. Takes a `transcription_engine` parameter instead of `model`.
> 
>   For most use cases, `telnyx.deepgram.STT` is the simpler interface.

*[Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin)*

## Available models

### Nova-3 (recommended)

Latest generation, best accuracy.

```python theme={null}
stt = telnyx.deepgram.STT(
    model="nova-3",
    language="en",
    interim_results=True,
    keyterm=["YourBrand", "custom-term"],  # keyword boosting
)
```

### Nova-2

Previous generation, stable and reliable. Uses weighted keyword boosting.

```python theme={null}
stt = telnyx.deepgram.STT(
    model="nova-2",
    language="en",
    interim_results=True,
    keywords=["YourBrand:2.0", "custom-term:1.5"],
)
```

### Flux

Experimental, with built-in end-of-turn detection. Designed for real-time voice agents.

```python theme={null}
stt = telnyx.deepgram.STT(
    model="flux",
    language="en",
    interim_results=True,
    keyterm=["YourBrand", "custom-term"],
    eot_threshold=0.5,
    eot_timeout_ms=3000,
    eager_eot_threshold=0.3,
)
```

## Parameters

| Parameter             | Default  | Description                                  |
| --------------------- | -------- | -------------------------------------------- |
| `model`               | `nova-3` | Model to use (`nova-3`, `nova-2`, `flux`)    |
| `language`            | `en`     | Language code                                |
| `interim_results`     | `True`   | Stream partial transcriptions                |
| `keyterm`             | —        | Keyword boosting (Nova-3, Flux)              |
| `keywords`            | —        | Weighted keyword boosting (Nova-2)           |
| `eot_threshold`       | —        | End-of-turn confidence threshold (Flux only) |
| `eot_timeout_ms`      | —        | End-of-turn timeout in ms (Flux only)        |
| `eager_eot_threshold` | —        | Eager end-of-turn threshold (Flux only)      |


## Related Pages

- [Speech-to-Text](../concepts/speech-to-text.md)
