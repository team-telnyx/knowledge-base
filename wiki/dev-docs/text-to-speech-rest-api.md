---
title: Text-to-Speech REST API
summary: Convert text to audio with a single POST request that streams synthesized
  audio back over the same HTTP connection. Choose from streaming, base64, or async
  retrieval; customize voices and pronunciation; and use OpenAI SDK-compatible clients
  with Telnyx’s endpoint.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
  content_hash: 0dffbb7f5a3c9b2b9e4251dd3cc0b645720108a435078b652a1404beefef00c8
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
  content_hash: ecf72e0af62f083cffb9c30648c84eaa1b0e7e6ed516a8804485ef4f3892d61e
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
  content_hash: 17f13471d7b7cea2acf9e43010a94c3d987ebacd62c04f583573ae6dbe43ed13
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
  content_hash: 61090dd1ae926bbdfc576d1480437a4ce5fb5731905ff297c9899dc2c52b3cde
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
  content_hash: c49b70c0f53c4d4cc689931efd6e0431a43c94d59f74ccee90870a46f7805eb5
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
  content_hash: d1ab64615afbe40ba60c5393e931d1332b37852072dc8294dcdbfd7afbfc2caa
updated_at: 2026-05-20T10:19:11Z
---

# Text-to-Speech REST API

Convert text to audio with a single POST request that streams synthesized audio back over the same HTTP connection. Choose from streaming, base64, or async retrieval; customize voices and pronunciation; and use OpenAI SDK-compatible clients with Telnyx’s endpoint.

## How streaming over REST works
You send text in, and audio streams back on the same HTTP response using HTTP chunked transfer encoding. Clients can begin playback as soon as the first chunks arrive—no polling or callbacks. The connection stays open until synthesis completes or 30 seconds pass with no new chunks. This makes the REST API suitable for real-time playback of single turns; for multi‑turn conversational use where you continuously feed text, use [Text-to-Speech WebSocket Streaming](text-to-speech-websocket-streaming.md).

## Endpoint and authentication
POST https://api.telnyx.com/v2/text-to-speech

Example (cURL):

```
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "text": "Hello from Telnyx text-to-speech.",
  "voice": "Telnyx.NaturalHD.astra"
}'
```

## Request parameters
- text (string, required): Text to synthesize. Markdown is automatically stripped.
- voice (string, required): Dot-separated voice identifier. Format: Provider.Model.VoiceId (e.g., Telnyx.NaturalHD.astra), or Provider.VoiceId when the provider has a single model.
- output_type (string, optional, default: binary_output): One of binary_output, base64_output, or audio_id.
- language (string, optional): BCP‑47 language code (e.g., en-US). Supported by AWS Polly, Azure, ElevenLabs, and Inworld; ignored by other providers.
- text_type (string, optional, default: text): text or ssml. SSML is supported by AWS Polly and Azure. Some Telnyx models (e.g., Ultra) may have their own SSML emotion syntax.
- voice_settings (object, optional): Provider‑specific tuning (e.g., speed, pitch, format, emotion). Fields vary by provider; see individual provider docs.
- pronunciation_dict_id (string, optional): UUID of a custom pronunciation dictionary. Applied before synthesis; see [Pronunciation Dictionaries](pronunciation-dictionaries.md).
- disable_cache (boolean, optional, default: false): Bypass the audio cache to always synthesize fresh output.

## Response formats and retrieval
The output_type you request controls the response:

- Streaming audio (default: binary_output): The response body is raw audio streamed with chunked transfer encoding, for example:

  ```
  HTTP/1.1 200 OK
  Content-Type: audio/mpeg
  Transfer-Encoding: chunked

  <audio chunk 1>
  <audio chunk 2>
  ...
  ```
  Start reading the body immediately; do not buffer the full response.

- Base64 (base64_output): A JSON payload returned after synthesis completes: {"base64_audio": "<base64-encoded-audio>"}. No streaming.

- Async handle (audio_id): Immediate JSON handle: {"audio_url": "https://api.telnyx.com/v2/text-to-speech/speech/<id>"}. Retrieve the audio later with GET /v2/text-to-speech/speech/:audio_id. If synthesis is still in progress, that GET response will itself stream chunks as they become available.

## Text preprocessing pipeline
Before synthesis, input text passes through:
1) Markdown stripping (headers, bold/italics, code blocks, links, lists, emoji converted to plain text), then
2) Optional pronunciation dictionary replacements when pronunciation_dict_id is provided.

## OpenAI SDK compatibility example
You can use OpenAI’s Audio SDK style as a drop‑in replacement by pointing the client at Telnyx and using your Telnyx API key:

```
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_TELNYX_API_KEY",
    base_url="https://api.telnyx.com/v2"
)

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="astra",
    input="Hello from Telnyx."
)

response.stream_to_file("output.mp3")
```

## Pricing and plans
Pricing varies by engine and model. See the public pricing page at https://telnyx.com/pricing/text-to-speech or contact sales at https://telnyx.com/contact-us for current rates.

## API reference and provider notes
- Full reference: Generate Speech from Text at https://developers.telnyx.com/api-reference/text-to-speech-commands/generate-speech-from-text.
- The OpenAPI spec is being cleaned up; some fields and provider‑specific schemas may be incomplete.
- For continuous, multi‑turn interactions, prefer [Text-to-Speech WebSocket Streaming](text-to-speech-websocket-streaming.md).
