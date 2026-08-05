---
title: Telnyx Programmable Voice
summary: A consolidated reference for Telnyx Programmable Voice covering the Voice
  API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression,
  Transcription), Text-to-Speech providers, and the European regional endpoint.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
updated_at: 2026-08-05T14:05:29Z
---

# Telnyx Programmable Voice

*Part 1 of 5 — see also: [Part 2](telnyx-programmable-voice--part-2.md), [Part 3](telnyx-programmable-voice--part-3.md), [Part 4](telnyx-programmable-voice--part-4.md), [Part 5](telnyx-programmable-voice--part-5.md)*

A consolidated reference for Telnyx Programmable Voice covering the Voice API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression, Transcription), Text-to-Speech providers, and the European regional endpoint.

## Overview

Telnyx Programmable Voice provides a REST-based Voice API and a TeXML scripting layer for building inbound and outbound voice applications. Developers can initiate calls, control them in real time through webhooks, stream media, transcribe speech, suppress noise, and synthesize speech using a variety of TTS providers. A dedicated European endpoint at `https://api.telnyx.eu` is available to reduce latency for calls held in Europe.

## Getting Started

To build a Voice API application you need a Telnyx account, an API key, a webhook URL, a phone number, and a configured Voice API Application. The application defines how Telnyx handles calls to and from your numbers and exposes settings for webhooks, anchor site, codecs, DTMF handling, and inbound/outbound channel limits.

When a call is placed, Telnyx sends a sequence of webhooks (`call.initiated`, `call.answered`, `call.hangup`, etc.) to the configured URL. Your webhook handler can respond with Voice API commands to control the call (for example, `speak`, `transcription`, `recording`).

### Making an Outbound Call

Replace the placeholders with your actual values: `your_api_key`, `your_phone_number`, `destination_number`, and `connection_id` (the Application ID).

```bash
curl --location 'https://api.telnyx.com/v2/calls' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_api_key' \
--data '{
   "to": "+1234567890",
   "from": "your_phone_number",
   "connection_id": "your_connection_id",
   "command_id": "unique-command-id-123"
}'
```

### Common Issues

| Issue | Solution |
| --- | --- |
| Webhook not received | Verify URL is publicly accessible, check firewall rules. |
| Call immediately ends | Verify the destination number is valid and your Voice API application is properly configured. |
| Authentication error | Verify API key is correct and has proper permissions. |
| Number not working | Ensure your Telnyx phone number (from) is assigned to your Voice API Application. |
