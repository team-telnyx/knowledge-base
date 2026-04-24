---
title: Response
summary: REST TTS response formats — streaming audio, base64, and async retrieval.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
    content_hash: 6db8a0d9bcb4d6d157a455943e507e7dec3c64765c5c852e50a9a6d099ae4179
updated_at: 2026-04-10T00:00:00Z
---

# Response

REST TTS response formats — streaming audio, base64, and async retrieval.

The `output_type` request field controls what comes back.

## Streaming Audio (default)

With `output_type: "binary_output"` (or omitted), the response is raw audio over HTTP chunked transfer encoding:

```
HTTP/1.1 200 OK
Content-Type: audio/mpeg
Transfer-Encoding: chunked

<audio chunk 1>
<audio chunk 2>
...
```

Start reading the body immediately — don't buffer the full response.

## Base64

With `output_type: "base64_output"`, the full audio is returned as a JSON payload after synthesis completes:

```json theme={null}
{"base64_audio": "<base64-encoded-audio>"}
```

No streaming — the entire file must synthesize before the response is sent.

## Async (audio\_id)

With `output_type: "audio_id"`, synthesis runs in the background. You get a URL back immediately:

```json theme={null}
{"audio_url": "https://api.telnyx.com/v2/text-to-speech/speech/<id>"}
```

Retrieve the audio later with `GET /v2/text-to-speech/speech/:audio_id`. If the audio is still synthesizing, the GET response itself streams chunks as they become available.


## Related Pages

- [Response Format](../runbooks/response-format.md)
- [SIP Response Codes](../runbooks/sip-response-codes.md)
