---
title: 'AI Voice on Telnyx: Assistants, Gather, STT/TTS, Streaming, and Safety'
summary: A practical guide to building AI-powered phone experiences on Telnyx. Learn
  when to use AI Assistants vs. Gather using AI, how to enable real-time media streaming,
  boost accuracy with noise suppression, add speech-to-text and text-to-speech (with
  SSML), and protect users with deepfake detection—plus key API calls and webhooks.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
  content_hash: 935729b032e38560301bf75fc52ae1799fd5184302fd224c88f05735a6e58e71
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
  content_hash: d17b526f566259e0e46f037b959216bbcf8a44e4a37521b5bd2b0efbeabf52f2
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
  content_hash: d6c3a73183ef7dc045d05c03ad29cf800a84e402c0b6c73d98e389b200a52b7d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
  content_hash: d0385b42b214b00cbda771a0671f724e760f90cbb2aa2f27e8e5d54bcd81e963
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
  content_hash: 6b108ff706319fa60a39497e105970f313d7b897740c0af34a21b6203265c1f8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
  content_hash: 56af332514e7916c8ab86d19963c873d2dae2ad760b2ea817357aa96108590e8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
  content_hash: 7c8e72fa751ece777e8f2ac7052003197d2a14b594125d5f0559e7b1273902a5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
  content_hash: cdee1b37fe2bfaf58920935e1538bcad65442f11294e8c586b9018478e948ed3
updated_at: 2026-05-20T09:33:28Z
---

# AI Voice on Telnyx: Assistants, Gather, STT/TTS, Streaming, and Safety

*Part 2 of 2 — see also: [Part 1](ai-voice-on-telnyx-assistants-gather-stt-tts-streaming-and-safety--part-1.md)*

A practical guide to building AI-powered phone experiences on Telnyx. Learn when to use AI Assistants vs. Gather using AI, how to enable real-time media streaming, boost accuracy with noise suppression, add speech-to-text and text-to-speech (with SSML), and protect users with deepfake detection—plus key API calls and webhooks.

## Speaking on calls with Text-to-Speech
Use Telnyx voices or third-party providers. Invoke speak on an active call:
```
curl -X POST 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/speak' \
  -H 'Authorization: Bearer YOUR_API_KEY' -H 'Content-Type: application/json' \
  -d '{
    "payload": "Thanks for calling—let’s get started.",
    "voice": "Telnyx.Natural.abbie"
  }'
```
Examples:
- Telnyx Ultra: "voice": "Telnyx.Ultra.<voice_id>"
- Telnyx internal TTS: "voice": "Telnyx.KokoroTTS.af"
- AWS Polly: "voice": "Polly.Brian" or "Polly.Amy-Neural"
- Azure AI Speech: "voice": "Azure.en-CA-ClaraNeural" (HD variants available)
- ElevenLabs: supply api_key via Integration Secrets, then pass voice_settings: {"api_key_ref": "your_api_key_ref"}
- MiniMax, ResembleAI, Inworld, Rime: set the appropriate voice name (see provider docs/voice catalogs)
Enhance pronunciation, pacing, and emphasis with [SSML Tags](ssml-tags.md). TeXML: <Say voice="...">Your text</Say>.

## Detecting AI-generated voices (Deepfake Detection)
Screen inbound or outbound calls in the background without affecting media quality.

Enable on Dial:
```
curl -X POST https://api.telnyx.com/v2/calls \
  -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "connection_id": "7267xxxxxxxxxxxxxx",
    "from": "+18005550101",
    "to": "+18005550100",
    "deepfake_detection": {"enabled": true, "timeout": 15, "rtp_timeout": 30}
  }'
```
Enable on Answer:
```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer \
  -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"deepfake_detection": {"enabled": true}}'
```
Result webhook: call.deepfake_detection.result with fields result (real | fake | silence_timeout), score (0–1), consistency (0–100). Errors: call.deepfake_detection.error (e.g., detection_timeout, rtp_timeout).
Best practices: set reasonable timeouts, use score+consistency together, and fail open (do not block calls on detection errors).

## Practical tips
- Prefer [Gather using AI](gather-using-ai.md) to quickly capture and validate structured inputs; use [SSML Tags](ssml-tags.md) to make prompts clearer.
- Use [Noise Suppression](noise-suppression.md)—especially on inbound audio—to boost STT accuracy for assistants and gather flows.
- For custom AI stacks or advanced latency control, route audio with [Media Streaming over Websockets](media-streaming-over-websockets.md) and use L16 codec where possible to minimize transcoding.
- Combine [Speech-to-Text with Voice API and TeXML](speech-to-text-with-voice-api-and-texml.md) for transcripts and analytics with [Text-to-Speech](text-to-speech.md) for dynamic prompts and persona voices.

## Related pages
- [Attach an AI Assistant to a Call](attach-an-ai-assistant-to-a-call.md)
- [Gather using AI](gather-using-ai.md)
- [Media Streaming over Websockets](media-streaming-over-websockets.md)
- [Noise Suppression](noise-suppression.md)
- [Deepfake Detection](deepfake-detection.md)
- [Speech-to-Text with Voice API and TeXML](speech-to-text-with-voice-api-and-texml.md)
- [Text-to-Speech](text-to-speech.md)
- [SSML Tags](ssml-tags.md)
