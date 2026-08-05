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

*Part 2 of 5 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 3](telnyx-programmable-voice--part-3.md), [Part 4](telnyx-programmable-voice--part-4.md), [Part 5](telnyx-programmable-voice--part-5.md)*

A consolidated reference for Telnyx Programmable Voice covering the Voice API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression, Transcription), Text-to-Speech providers, and the European regional endpoint.

## Voice API Commands and Resources

The Voice API exposes endpoints for call control, conferences, queues, recordings, custom storage, and recording transcriptions.

### Call

- `POST /v2/calls` — Initiate a new call
- `POST /v2/calls/:call_control_id/actions/answer` — Answer an incoming call
- `POST /v2/calls/:call_control_id/actions/fork_start` — Start a media fork for a call
- `POST /v2/calls/:call_control_id/actions/fork_stop` — Stop a media fork for a call
- `POST /v2/calls/:call_control_id/actions/hangup` — Terminate a call
- `POST /v2/calls/:call_control_id/actions/reject` — Reject an incoming call
- `POST /v2/calls/:call_control_id/actions/transfer` — Transfer a call to another destination
- `POST /v2/calls/:call_control_id/actions/suppression_start` — Start noise suppression for a call
- `POST /v2/calls/:call_control_id/actions/suppression_stop` — Stop noise suppression for a call
- `POST /v2/calls/:call_control_id/actions/client_state_update` — Update client state information for a call
- `POST /v2/calls/:call_control_id/actions/bridge` — Bridge a call with another destination
- `POST /v2/calls/:call_control_id/actions/ai_assistant_start` — Start an AI assistant on the call
- `POST /v2/calls/:call_control_id/actions/ai_assistant_stop` — Stop an AI assistant on the call
- `POST /v2/calls/:call_control_id/actions/enqueue` — Add a call to a queue
- `POST /v2/calls/:call_control_id/actions/leave_queue` — Remove a call from a queue
- `POST /v2/calls/:call_control_id/actions/gather_using_audio` — Play an audio file on the call until the required DTMF signals are gathered
- `POST /v2/calls/:call_control_id/actions/gather_using_speak` — Play a speech on the call until the required DTMF signals are gathered
- `POST /v2/calls/:call_control_id/actions/gather_using_ai` — Collect request information using an AI agent
- `POST /v2/calls/:call_control_id/actions/gather_stop` — Stop an ongoing gather operation
- `POST /v2/calls/:call_control_id/actions/playback_start` — Start playing audio to a call
- `POST /v2/calls/:call_control_id/actions/playback_stop` — Stop playing audio to a call
- `POST /v2/calls/:call_control_id/actions/record_start` — Start recording a call
- `POST /v2/calls/:call_control_id/actions/record_stop` — Stop recording a call
- `POST /v2/calls/:call_control_id/actions/record_pause` — Pause recording a call
- `POST /v2/calls/:call_control_id/actions/record_resume` — Resume recording a call
- `POST /v2/calls/:call_control_id/actions/refer` — Send a SIP REFER request for a call
- `POST /v2/calls/:call_control_id/actions/send_dtmf` — Send DTMF tones to a call
- `POST /v2/calls/:call_control_id/actions/send_sip_info` — Send a SIP INFO message for a call
- `POST /v2/calls/:call_control_id/actions/speak` — Speak text to a call
- `POST /v2/calls/:call_control_id/actions/streaming_start` — Start media streaming for a call
- `POST /v2/calls/:call_control_id/actions/streaming_stop` — Stop media streaming for a call
- `POST /v2/calls/:call_control_id/actions/transcription_start` — Start transcription for a call
- `POST /v2/calls/:call_control_id/actions/transcription_stop` — Stop transcription for a call
- `POST /v2/calls/:call_control_id/actions/siprec_start` — Start SIPREC recording for a call
- `POST /v2/calls/:call_control_id/actions/siprec_stop` — Stop SIPREC recording for a call
- `GET /v2/connections/:connection_id/active_calls` — List all active calls for a connection
- `GET /v2/calls/:call_control_id` — Retrieve a call status

### Call Events

- `GET /v2/call_events` — Provide a list of call events based on a filter

### Conference

- `GET /v2/conferences` — List all conferences
- `GET /v2/conferences/:id` — Get details of a specific conference
- `GET /v2/conferences/:id/participants` — List participants in a conference
- `PATCH /v2/conferences/:id/participants/:participant_id` — Update a participant in a conference
- `POST /v2/conferences` — Create a new conference
- `POST /v2/conferences/:id/actions/join` — Join a call to a conference
- `POST /v2/conferences/:id/actions/leave` — Remove a call from a conference
- `POST /v2/conferences/:id/actions/record_start` — Start recording a conference
- `POST /v2/conferences/:id/actions/record_stop` — Stop recording a conference
- `POST /v2/conferences/:id/actions/record_pause` — Pause recording a conference
- `POST /v2/conferences/:id/actions/record_resume` — Resume recording a conference
- `POST /v2/conferences/:id/actions/mute` — Mute all participants in a conference
- `POST /v2/conferences/:id/actions/unmute` — Unmute all participants in a conference
- `POST /v2/conferences/:id/actions/hold` — Put all participants on hold in a conference
- `POST /v2/conferences/:id/actions/unhold` — Remove hold for all participants in a conference
- `POST /v2/conferences/:id/actions/play` — Play audio to a conference
- `POST /v2/conferences/:id/actions/speak` — Speak text to a conference
- `POST /v2/conferences/:id/actions/stop` — Stop all ongoing activities in a conference
- `POST /v2/conferences/:id/actions/update` — Update conference participant

### Queue

- `GET /v2/queues/:queue_name` — Get details of a specific queue
- `GET /v2/queues/:queue_name/calls` — List calls in a queue
- `GET /v2/queues/:queue_name/calls/:call_control_id` — Get details of a call in a queue

### Recording

- `GET /v2/recordings` — List all recordings
- `GET /v2/recordings/:id` — Get details of a specific recording
- `DELETE /v2/recordings/:id` — Delete a recording

### Custom Storage

- `POST /v2/custom_storage_credentials` — Create custom storage credentials
- `GET /v2/custom_storage_credentials` — List all custom storage credentials
- `GET /v2/custom_storage_credentials/:id` — Get details of a specific custom storage credential
- `DELETE /v2/custom_storage_credentials/:id` — Delete a custom storage credential

### Recording Transcription

- `GET /v2/recordings/:recording_id/transcriptions` — List all transcriptions for a recording
- `GET /v2/recordings/:recording_id/transcriptions/:id` — Get details of a specific recording transcription
- `DELETE /v2/recordings/:recording_id/transcriptions/:id` — Delete a recording transcription
