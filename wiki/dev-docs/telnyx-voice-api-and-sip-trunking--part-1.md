---
title: Telnyx Voice API and SIP Trunking
summary: Telnyx provides a programmable Voice API for building voice applications
  with call control, conferencing, queuing, recording, and AI assistants, alongside
  an Elastic SIP Trunking platform with multiple authentication methods and granular
  routing, billing, and caller-ID configuration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
updated_at: 2026-06-11T10:44:15Z
---

# Telnyx Voice API and SIP Trunking

*Part 1 of 3 — see also: [Part 2](telnyx-voice-api-and-sip-trunking--part-2.md), [Part 3](telnyx-voice-api-and-sip-trunking--part-3.md)*

Telnyx provides a programmable Voice API for building voice applications with call control, conferencing, queuing, recording, and AI assistants, alongside an Elastic SIP Trunking platform with multiple authentication methods and granular routing, billing, and caller-ID configuration.

## Voice API Fundamentals

The Telnyx Voice API lets you make and receive calls, control call flows in real time, and add features such as text-to-speech, transcription, media streaming, and AI assistants. To get started you need a Telnyx account, an API key, a publicly accessible webhook URL, a purchased phone number, and a Voice API Application.

### Creating a Voice API Application

A Voice API Application defines how Telnyx handles calls to and from your numbers. Create one in the Mission Control Portal under **Real-Time Communication > Voice > Programmable Voice** by clicking **Create Voice App**. Key configuration sections include:

- **Application settings** — name, webhook URL, webhook failover URL, webhook API version (v1 or v2; v2 recommended), anchor site (routes media through the site with the lowest round-trip time), tags, hang-up on timeout, custom webhook timeout, DTMF type (RFC 2833 recommended), and enable call cost.
- **Inbound** — SIP subdomain, SIP subdomain receive settings, inbound channel limit, SHAKEN/STIR headers, and codecs.
- **Outbound** — outbound voice profile and outbound channel limit.
- **Numbers** — assign purchased phone numbers to the application.

### Making Your First Outbound Call

Use `POST /v2/calls` with your API key, a `from` number, a `to` number, and the `connection_id` (the Application ID visible on your Voice API Application details page). Example with cURL:

```bash
curl --location 'https://api.telnyx.com/v2/calls' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "to": "+1234567890",
    "from": "+18005551234",
    "connection_id": "YOUR_CONNECTION_ID"
  }'
```

When a call is made, Telnyx sends `call.initiated`, `call.answered`, and `call.hangup` webhooks to your configured URL.

### Common Issues

| Issue | Solution |
|---|---|
| Webhook not received | Verify URL is publicly accessible; check firewall rules |
| Call immediately ends | Verify destination number and application configuration |
| Authentication error | Verify API key and permissions |
| Number not working | Ensure the `from` number is assigned to your Voice API Application |

### Call Recording

Enable recording via the Outbound Voice Profile settings in the Mission Control Portal or programmatically with the Start Recording API (`POST /v2/calls/:call_control_id/actions/record_start`). Retrieve recordings from the [Call Recordings page](https://portal.telnyx.com/#/voice/call-recordings) in the portal.

## Voice API Commands and Resources

### Call Commands

All call commands use the path prefix `/v2/calls/:call_control_id/actions/`.

| Action | Description |
|---|---|
| `answer` | Answer an incoming call |
| `bridge` | Bridge a call with another destination |
| `client_state_update` | Update client state for a call |
| `enqueue` | Add a call to a queue |
| `fork_start` / `fork_stop` | Start or stop media forking |
| `gather_using_audio` | Play audio until DTMF signals are gathered |
| `gather_using_speak` | Play speech until DTMF signals are gathered |
| `gather_using_ai` | Collect information using an AI agent |
| `gather_stop` | Stop an ongoing gather operation |
| `hangup` | Terminate a call |
| `leave_queue` | Remove a call from a queue |
| `playback_start` / `playback_stop` | Start or stop audio playback |
| `record_start` / `record_stop` / `record_pause` / `record_resume` | Control call recording |
| `reject` | Reject an incoming call |
| `send_dtmf` | Send DTMF tones |
| `send_sip_info` | Send a SIP INFO message |
| `speak` | Speak text to a call |
| `streaming_start` / `streaming_stop` | Start or stop media streaming |
| `suppression_start` / `suppression_stop` | Start or stop noise suppression (beta) |
| `transcription_start` / `transcription_stop` | Start or stop transcription |
| `transfer` | Transfer a call to another destination |
| `siprec_start` / `siprec_stop` | Start or stop SIPREC recording |
| `refer` | Send a SIP REFER request |
| `ai_assistant_start` / `ai_assistant_stop` | Start or stop an AI assistant |

Additional call-related endpoints:

- `POST /v2/calls` — Initiate a new call
- `GET /v2/connections/:connection_id/active_calls` — List active calls for a connection
- `GET /v2/calls/:call_control_id` — Retrieve call status
- `GET /v2/call_events` — List call events

### Conference Commands

Conferences use the path prefix `/v2/conferences/:id/`.

| Action | Description |
|---|---|
| `POST /v2/conferences` | Create a new conference |
| `GET /v2/conferences` | List all conferences |
| `GET /v2/conferences/:id` | Retrieve conference details |
| `GET /v2/conferences/:id/participants` | List participants |
| `PATCH /v2/conferences/:id/participants/:participant_id` | Update a participant |
| `actions/join` | Join a call to a conference |
| `actions/leave` | Remove a call from a conference |
| `actions/record_start` / `record_stop` / `record_pause` / `record_resume` | Control conference recording |
| `actions/mute` / `actions/unmute` | Mute or unmute all participants |
| `actions/hold` / `actions/unhold` | Hold or unhold all participants |
| `actions/play` | Play audio to a conference |
| `actions/speak` | Speak text to a conference |
| `actions/stop` | Stop all ongoing activities |

### Queue Endpoints

- `GET /v2/queues/:queue_name` — Get queue details
- `GET /v2/queues/:queue_name/calls` — List calls in a queue
- `GET /v2/queues/:queue_name/calls/:call_control_id` — Get details of a specific call in a queue

### Recording Endpoints

- `GET /v2/recordings` — List all recordings
- `GET /v2/recordings/:id` — Get recording details
- `DELETE /v2/recordings/:id` — Delete a recording

### Custom Storage Credentials

- `POST /v2/custom_storage_credentials` — Create custom storage credentials
- `GET /v2/custom_storage_credentials` — List all custom storage credentials
- `GET /v2/custom_storage_credentials/:id` — Get credential details
- `DELETE /v2/custom_storage_credentials/:id` — Delete a credential

### Recording Transcriptions

- `GET /v2/recordings/:recording_id/transcriptions` — List transcriptions for a recording
- `GET /v2/recordings/:recording_id/transcriptions/:id` — Get transcription details
- `DELETE /v2/recordings/:recording_id/transcriptions/:id` — Delete a transcription
