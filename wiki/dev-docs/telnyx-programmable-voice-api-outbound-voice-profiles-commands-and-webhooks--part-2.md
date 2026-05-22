---
title: 'Telnyx Programmable Voice API: Outbound Voice Profiles, Commands, and Webhooks'
summary: A practical guide to building with the Telnyx Programmable Voice API—covering
  core concepts, outbound voice profiles, application setup, making calls, webhooks,
  commands, reliability practices, and recordings.
sources:
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
  content_hash: 9200682c71900c49ca3d028566603fa820c615ede88bf30fc37990c6e5ecfb64
- url: https://developers.telnyx.com/docs/voice/overview/index
  content_hash: c0c2bf7cc837b2a299497b7209c0260abc40f1c4d6be277283f7c1b23b75a558
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
  content_hash: e178189da0a77c1d8fbe72503ed302ed00161df1200001fcd11aaba2451ff76f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
  content_hash: 69f8eea2a52deb0119ca863d55eec0046fc2441a23b5cea4e18756b9b340da59
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
  content_hash: 66a97c3563c6c8197a9cbe9895bb3b5b4d0889b9426deaa6a9938de24814b580
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
  content_hash: ead579cbba8f3675c4e3c39b7edcf549aca3519674ffae7cdfc4d1fd5ce62aeb
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
  content_hash: b020d1fff66371ca25e5bc86dc862a0284685c20b26e0eb61d7087c41c726571
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
  content_hash: 508fdee61dc660e01401d5f0a8c4a71888f646d5323549df829493ecd7f98d22
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
  content_hash: d8e5c33bc7836a4f1ebeede50bdc200f02f7aa12f00497335bebb95916967095
updated_at: 2026-05-20T09:31:54Z
---

# Telnyx Programmable Voice API: Outbound Voice Profiles, Commands, and Webhooks

*Part 2 of 2 — see also: [Part 1](telnyx-programmable-voice-api-outbound-voice-profiles-commands-and-webhooks--part-1.md)*

A practical guide to building with the Telnyx Programmable Voice API—covering core concepts, outbound voice profiles, application setup, making calls, webhooks, commands, reliability practices, and recordings.

## Reliability: Retries, Idempotency, and Failover
- Use command_id on every command (unique per command, e.g., UUIDv4). Duplicate command_ids received within ~60 seconds are ignored—this prevents double actions if you retry.
- Retry strategy
  - On HTTP 5xx from Telnyx: immediately retry the command.
  - On high latency (>500 ms without a response): send an identical command.
- Webhook resilience
  - Expect duplicates and out-of-order delivery; deduplicate using data.id and design idempotent handlers.
  - Set a failover webhook URL for critical apps.
  - Return 2xx quickly; process heavy work asynchronously.
  - Verify signatures to trust the source.

## Recording and Retrieving Calls
- Configure default recording at the Outbound Voice Profile level (e.g., record outbound calls by default) in Mission Control.
- Start/stop/pause/resume recordings programmatically with recording commands.
- Retrieve and manage recordings via the Mission Control Call Recordings page or the Recordings API (list, retrieve, delete). Transcriptions for recordings can also be queried and managed.

## Troubleshooting and Debugging
- Not receiving webhooks: ensure your URL is publicly reachable, SSL is valid, and firewalls allow Telnyx.
- Calls end immediately: confirm the destination is valid and your Voice API Application is correctly configured (numbers assigned, outbound profile set, limits sufficient).
- Authentication errors: confirm the API key and Authorization header.
- From number not working: assign your purchased number to the application and use E.164 format.
- Inspect webhook delivery history with the Webhook Deliveries API (filter by status/event/time) to diagnose failures.

## Next Steps and SDKs
- Build richer call flows: playback, TTS/SSML, gather, transfer/bridge, queues, conferences, transcription, and media streaming.
- Add AI features: noise suppression, deepfake detection, Dialogflow, attach AI assistants, gather using AI.
- Use official SDKs to speed integration: Node.js, Python, PHP, Ruby, Java.
