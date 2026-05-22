---
title: 'Telnyx Programmable Voice API: Outbound Voice Profiles, Commands, and Webhooks'
summary: A practical guide to building with the Telnyx Programmable Voice API—covering
  core concepts, outbound voice profiles, application setup, making calls, webhooks,
  commands, reliability practices, and recordings.
sources:
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/overview/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
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
