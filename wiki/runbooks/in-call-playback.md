---
title: In-Call Playback
summary: TTS during live voice calls via Voice API or TeXML.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/in-call-playback/index
    content_hash: 20fc0c4a75e121d93e32cab6d8398c6dee61321bcdc9f34bc7ced02e976020c6
updated_at: 2026-04-10T00:00:00Z
---

# In-Call Playback

TTS during live voice calls via Voice API or TeXML.

In-call TTS plays synthesized speech during live voice calls. Two integration paths:

## Voice API

Use the [`speak`](https://developers.telnyx.com/api-reference/call-commands/speak-text) command to play TTS on an active call:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/{call_control_id}/actions/speak' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
  "voice": "Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41"
}'
```

See [Voice API docs](https://developers.telnyx.com/docs/voice/programmable-voice) for the full command reference.

## TeXML

Use the `` element:

```xml theme={null}

  <Say voice="Telnyx.NaturalHD.astra">Your appointment is confirmed for tomorrow at 3 PM.

```

See [TeXML docs](https://developers.telnyx.com/docs/voice/texml) for the full `` reference.

## AI Assistants

AI Assistants use TTS for voice output. Configure the voice model in assistant settings.

See [AI Assistants](https://developers.telnyx.com/docs/inference/ai-assistants) for voice configuration.

## Voice Selection

In-call TTS uses the same voice format as WebSocket and REST:

```
Provider.Model.VoiceId
```

All models (including Ultra) are available for in-call playback.
