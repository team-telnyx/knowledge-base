---
title: Model Config
summary: Pass-through to [Deepgram's pre-recorded API](https://developers.deepgram.com/docs/pre-recorded-audio) query parameters.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
    content_hash: b87435413715fea155b2396648b67e7abbe48ce65cb8ae814c40a3674aad863e
updated_at: 2026-04-10T00:00:00Z
---

# Model Config

Deepgram only. Returns 400 if used with other models.

Pass-through to [Deepgram's pre-recorded API](https://developers.deepgram.com/docs/pre-recorded-audio) query parameters. Every key-value pair in `model_config` is forwarded directly — Telnyx does not validate individual options.

## Commonly Used Options

| Option         | Type    | Description                                                               |
| -------------- | ------- | ------------------------------------------------------------------------- |
| `smart_format` | boolean | Capitalization, punctuation, dates, numbers, currency                     |
| `punctuate`    | boolean | Add punctuation                                                           |
| `diarize`      | boolean | Speaker identification. Adds `speakers` array to `verbose_json` segments. |
| `utterance`    | boolean | Segment transcript into utterances                                        |
| `numerals`     | boolean | Convert spoken numbers to digits                                          |
| `language`     | string  | Override language. Top-level `language` param takes precedence.           |

## Example

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "file=@call-recording.mp3" \
  -F "model=deepgram/nova-3" \
  -F "response_format=verbose_json" \
  -F 'model_config={"smart_format": true, "diarize": true, "punctuate": true}'
```

`model_config` can be sent as a JSON string in the multipart form field. The server parses it before forwarding.

## Unvalidated Pass-Through

Any Deepgram query parameter can be passed. If Deepgram adds new options, they work immediately without a Telnyx API update. Conversely, invalid keys are forwarded and may cause Deepgram to return an error.

Refer to [Deepgram's API reference](https://developers.deepgram.com/reference/listen-file) for the full list of supported parameters.
