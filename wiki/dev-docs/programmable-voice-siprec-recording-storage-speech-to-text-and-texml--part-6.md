---
title: 'Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML'
summary: A consolidated reference for Telnyx Programmable Voice features covering
  SIPREC client and server configuration, call recording storage backends, real-time
  speech-to-text transcription, and the TeXML markup language including applications,
  instruction fetching, dynamic templating, HTTP requests, and answering machine detection.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
updated_at: 2026-08-05T14:04:31Z
---

# Programmable Voice: SIPREC, Recording Storage, Speech-to-Text, and TeXML

*Part 6 of 6 — see also: [Part 1](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-1.md), [Part 2](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-2.md), [Part 3](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-3.md), [Part 4](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-4.md), [Part 5](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-5.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## TeXML Answering Machine Detection

TeXML supports Answering Machine Detection (AMD) for outbound calls in two modes: synchronous and asynchronous.

### Synchronous mode

In synchronous mode, TeXML instructions are not executed until the AMD results are provided in the status callback. New instructions can be sent back as a response to be processed by the TeXML engine:

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
  "From": "+13127367421",
  "To": "your-sip-user@sip.telnyx.com",
  "Url": "https://your-server.example.com/texml/instructions",
  "FallbackUrl": "https://your-server.example.com/texml/fallback",
  "StatusCallback": "https://your-server.example.com/callback/status",
  "StatusCallbackMethod": "POST",
  "Method": "POST",
  "MachineDetection": "Enable",
  "DetectionMode": "Premium",
  "AsyncAmd": false
}'
```

The results of the analysis are sent as the `AnsweredBy` parameter of the `StatusCallback` request.

#### `AnsweredBy` parameter values

When `MachineDetection` is `Enable` (detects as soon as the answering machine is identified):

| Value | Description |
| --- | --- |
| `human` | A human answered the call |
| `machine_start` | An answering machine was detected (detection completes immediately) |
| `fax` | A fax machine was detected |
| `unknown` | Detection was inconclusive |

When `MachineDetection` is `DetectMessageEnd` (waits for the answering machine greeting to finish):

| Value | Description |
| --- | --- |
| `human` | A human answered the call |
| `machine_end_beep` | Answering machine greeting ended with a beep detected |
| `machine_end_silence` | Answering machine greeting ended with silence |
| `machine_end_other` | Answering machine greeting ended (other detection) |
| `fax` | A fax machine was detected |
| `unknown` | Detection was inconclusive |

The `MachineDetection` parameter accepts `Enable`, `Disable` (default), and `DetectMessageEnd`. The `DetectionMode` parameter accepts `Regular` (default) or `Premium`.

### Asynchronous mode

In asynchronous mode, TeXML instructions are processed in parallel with the AMD process. The results are provided in the `AsyncAmdStatusCallback` callback:

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/Accounts/{account_sid}/Calls \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
  "From": "+13127367421",
  "To": "your-sip-user@sip.telnyx.com",
  "Url": "https://your-server.example.com/texml/instructions",
  "FallbackUrl": "https://your-server.example.com/texml/fallback",
  "Method": "POST",
  "StatusCallback": "https://your-server.example.com/callback/status",
  "StatusCallbackMethod": "POST",
  "MachineDetection": "Enable",
  "DetectionMode": "Premium",
  "AsyncAmd": true,
  "AsyncAmdStatusCallback": "https://your-server.example.com/callback/amd-status",
  "AsyncAmdStatusCallbackMethod": "POST"
}'
```

The results of the AMD analysis are sent as callback requests to the address provided as `AsyncAmdStatusCallback`. This can be used for both basic and premium AMD.

#### `AsyncAmdStatusCallback` parameters

| Parameter | Description |
| --- | --- |
| `AnsweredBy` | The result of AMD analysis. See the `AnsweredBy` parameter values table above for the full list of mode-dependent values (`human`, `machine_start`, `machine_end_beep`, `machine_end_silence`, `machine_end_other`, `fax`, `unknown`) |
| `CallSid` | The unique identifier for the call |
| `CallSidLegacy` | Legacy call identifier (same as `CallSid`) |
| `AccountSid` | Your Telnyx account SID |
| `ConnectionId` | The unique identifier of the connection used for the call |
| `MachineDetectionDuration` | The duration of the machine detection in milliseconds |
