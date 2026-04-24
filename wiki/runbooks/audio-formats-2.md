---
title: Audio Formats
summary: Supported audio input formats, sample rates, and engine compatibility.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
    content_hash: 2aee37f1d72c49183e1d659787c6ebc01f65c9f8e0a8725d059314d95ead55ca
updated_at: 2026-04-10T00:00:00Z
---

# Audio Formats

Supported audio input formats, sample rates, and engine compatibility.

Set via the `input_format` query parameter. Audio is sent as binary WebSocket frames -- chunked bytes, no base64, no JSON wrapping.

Container formats (mp3, webm, etc.) are self-describing: the server demuxes the byte stream and extracts encoding/sample rate from headers. Raw formats have no metadata, so you must set `sample_rate` explicitly.

Works for both real-time capture (microphone, MediaRecorder, telephony bridge) and file streaming (read a file in chunks, push through the socket).

## Browser Capture

Output from `MediaRecorder` or similar browser APIs. Container headers carry sample rate.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=webm_opus
```

| Format      | Sample rate | Notes                                              |
| ----------- | ----------- | -------------------------------------------------- |
| `webm`      | from header | WebM container                                     |
| `webm_opus` | from header | WebM + Opus. Valid: 8000–48000. Alias: `webm-opus` |
| `ogg_opus`  | from header | Ogg + Opus. Valid: 8000–48000. Alias: `ogg-opus`   |
| `ogg`       | from header | Ogg container (Vorbis or other)                    |

## Telephony

Codecs from voice networks. Raw frames, `sample_rate` required.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=mulaw&sample_rate=8000
```

| Format   | Sample rate        | Notes                                            |
| -------- | ------------------ | ------------------------------------------------ |
| `mulaw`  | any                | G.711 µ-law. North America. Default: 8000 Hz.    |
| `alaw`   | any                | G.711 A-law. EU/international. Default: 8000 Hz. |
| `g729`   | 8000               | G.729. Fixed.                                    |
| `amr_nb` | 8000               | AMR narrowband. Fixed. Alias: `amr-nb`           |
| `amr_wb` | 16000              | AMR wideband. Fixed. Alias: `amr-wb`             |
| `speex`  | 8000, 16000, 32000 | Google: 16000 only.                              |

Invalid sample rate returns [error 40005](errors.md).

## Raw PCM

Uncompressed audio from microphones, processing pipelines, or SDKs. `sample_rate` required.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=linear16&sample_rate=16000
```

| Format     | Sample rate                      | Notes                                                        |
| ---------- | -------------------------------- | ------------------------------------------------------------ |
| `linear16` | any                              | 16-bit signed PCM, little-endian (s16le). Default: 16000 Hz. |
| `linear32` | any                              | 32-bit float PCM, little-endian (f32le). Default: 16000 Hz.  |
| `opus`     | 8000, 12000, 16000, 24000, 48000 | Raw Opus frames, no container. Deepgram also: 44100.         |

Invalid sample rate returns [error 40005](errors.md).

## Recorded File

Pre-recorded files read in chunks and streamed through the socket. Container headers carry sample rate.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=mp3
```

| Format | Sample rate | Notes                                 |
| ------ | ----------- | ------------------------------------- |
| `mp3`  | from header | Default for most engines              |
| `wav`  | from header | Uncompressed. Default for Flux model. |
| `flac` | from header | Lossless compression                  |

## Engine Compatibility

Unsupported format/engine combination returns [error 40002](errors.md). Unsupported Flux format returns [error 40006](errors.md).

Deepgram has three model generations with different format support. Flux is the most restrictive — it drops `mp3`, `flac`, `webm_opus`, `amr_nb`, `amr_wb`, `g729`, and `speex` compared to Nova.

| Format     | Deepgram Nova | Deepgram Flux | Telnyx | Google | Azure |
| ---------- | :-----------: | :-----------: | :----: | :----: | :---: |
| mp3        |       ✓       |               |    ✓   |    ✓   |   ✓   |
| wav        |       ✓       |       ✓       |    ✓   |    ✓   |   ✓   |
| webm       |       ✓       |       ✓       |        |        |       |
| ogg        |       ✓       |       ✓       |        |        |       |
| flac       |       ✓       |               |        |    ✓   |       |
| ogg\_opus  |       ✓       |       ✓       |        |    ✓   |       |
| webm\_opus |       ✓       |               |        |    ✓   |       |
| linear16   |       ✓       |       ✓       |    ✓   |    ✓   |   ✓   |
| linear32   |       ✓       |       ✓       |    ✓   |        |       |
| mulaw      |       ✓       |       ✓       |        |    ✓   |       |
| alaw       |       ✓       |       ✓       |        |        |       |
| opus       |       ✓       |       ✓       |        |        |       |
| amr\_nb    |       ✓       |               |        |    ✓   |       |
| amr\_wb    |       ✓       |               |        |    ✓   |       |
| g729       |       ✓       |               |        |        |       |
| speex      |       ✓       |               |        |    ✓   |       |

Universal formats (all engines and models): `wav`, `linear16`.


## Related Pages

- [Audio Formats](../runbooks/audio-formats.md)
