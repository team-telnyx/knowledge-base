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

*Part 2 of 6 — see also: [Part 1](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-1.md), [Part 3](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-3.md), [Part 4](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-4.md), [Part 5](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-5.md), [Part 6](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-6.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## Storing Call Recordings

Call recordings are automatically stored in S3 buckets owned by Telnyx, but you can opt to store recordings in your own S3, GCS, or Azure Blob Storage bucket instead.

### Telnyx S3 storage

Recordings are stored in Telnyx-owned S3 buckets. The link is shared in the `call.recording.saved` webhook when the recording is ready to download. The link is active for 10 minutes.

### Custom GCS storage

Store recordings in a customer-owned GCS bucket by sending the following request with user credentials for the application:

```
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "gcs",
	"configuration": {
		"credentials": "JSON_WITH_CREDENTIALS",
		"bucket": "BUCKET_NAME"
	}
}'
```

The provided user must have permission to store files in the bucket. See the [GCS credentials documentation](https://cloud.google.com/iam/docs/keys-create-delete#creating) for how to generate credentials. The `call.recording.saved` webhook then reports the GCS path (for example, `gs://tacrde12904/...`).

### Custom S3 storage

Store recordings in a customer-owned AWS S3 bucket:

```
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "s3",
	"configuration": {
		"bucket": "BUCKET_NAME",
    "region" : "REGION_NAME",
    "aws_access_key_id" :  "AWS_ACCESS_KEY_ID",
    "aws_secret_access_key" : "AWS_SECRET_ACCESS_KEY"
	}
}'
```

The `call.recording.saved` webhook then reports an `s3://...` URL.

### Custom Microsoft Azure Blob Storage

Store recordings in a customer-owned Azure Blob Storage container:

```
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "azure",
	"configuration": {
		"bucket": "BUCKET_NAME",
    "account_name" :  "AZURE_ACCOUNT_NAME",
    "account_key" : "AZURE_ACCOUNT_KEY"
	}
}'
```

The `call.recording.saved` webhook then reports an `https://<account>.blob.core.windows.net/<bucket>/...` URL.

See the [call recording API reference](/api-reference/call-recordings/retrieve-a-call-recording) for more details.

## Speech-to-Text

Telnyx supports real-time speech-to-text transcription of calls using either the Voice API or TeXML. Before starting, ensure your [Voice API](voice-api.md) or [TeXML Setup](texml-setup.md) application is correctly configured.

### Supported engines

- **Google** (default) — Google speech-to-text engine with features like interim results.
- **Telnyx** — In-house engine with significantly better transcription accuracy and lower latency.
- **Deepgram** — Supports three models (`nova-2`, `nova-3`, `flux`) set via the `transcription_model` setting.
- **Azure** — Strong support for multiple languages and accents.
- **xAI** — xAI Grok STT engine with the `xai/grok-stt` model.
- **AssemblyAI** — Universal-Streaming engine (backed by Universal-3.5 Pro Realtime) with the `assemblyai/universal-streaming` model.
- **Speechmatics** — Real-time engine with the `speechmatics/standard` model; high accuracy with multilingual and bilingual language packs.
- **Soniox** — Real-time engine with the `soniox/stt-rt-v4` model; automatic language detection with interim results and endpointing support.
- **Parakeet** — Self-hosted NVIDIA Parakeet engine with the `nvidia/parakeet-v3` model; automatic multilingual language detection with final transcripts only.
- **Reson8** — Turn-based engine with the `reson8/turns` model; automatic language detection across 10 European languages; transcripts delivered per turn of speech.

### Voice API

Enable transcription on a Voice API call using the [transcription_start endpoint](/api-reference/call-commands/transcription-start):

```
curl -i -X POST \
'https://api.telnyx.com/v2/calls/{call_control_id}/actions/transcription_start' \
-H 'Authorization: Bearer YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
    "language": "en",
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
    "transcription_engine": "Google/Telnyx/Deepgram/Azure/xAI/AssemblyAI/Speechmatics/Soniox/Parakeet/Reson8"
}'
```

Results are delivered as a `call.transcription` webhook to the URL defined for the Voice API application, with `transcription_data` containing `confidence`, `is_final`, and `transcript` fields.

### TeXML

Enable transcription on TeXML calls by including a `<Transcription>` verb inside a `<Start>` block:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription language="en" transcriptionCallback="/transcription" transcriptionEngine=”Telnyx” />
  </Start>
</Response>
```

The transcription results are sent to the callback in a form-encoded payload containing `AccountSid`, `CallSid`, `CallSidLegacy`, `Confidence`, `ConnectionId`, `From`, `IsFinal`, `To`, and `Transcript`.

## TeXML Fundamentals

TeXML is an XML-based markup language used to define call control and processing instructions. When properly configured, Telnyx fetches TeXML instructions from your application and processes calls accordingly. See [TeXML TwiML Compatibility](texml-twiml-compatibility.md) for the full list of verbs and nouns.

### TeXML Application

A TeXML Application is a collection of configuration parameters that defines the interaction between Telnyx and your application:

| Field | Description |
| --- | --- |
| **Application Name** | A descriptive name to identify your TeXML application. |
| **AnchorSite** | Defines the preferable data center for handling traffic. With `latency`, ICMP ping to the webhook URL is used to calculate the closest data center. |
| **Voice method** | HTTP method used to interact with your webhooks. |
| **Webhook URL** | The URL where Telnyx fetches TeXML instructions when a call is initiated. Can be served by Telnyx via `TeXML bin URL` (see [TeXML Bin Quickstart](texml-bin-quickstart.md)). |
| **Webhook Failover URL** | A backup URL used if the primary webhook URL fails to respond. |
| **Call progress events URL** | URL where Telnyx sends event callbacks related to your calls. |
| **Status Callback Method** | HTTP method (GET or POST) used for status callbacks. |
| **Hang-up on timeout** | Number of seconds Telnyx waits for the initial application response before hanging up. |
| **DTMF Type** | Configuration for how DTMF (touch-tone) inputs are handled. |
| **Enable Call Cost** | Specifies whether the call cost webhook should be sent. |

A TeXML Application can be created through the [Telnyx Mission Control Portal](https://portal.telnyx.com/#/call-control/texml/new) or via the [Telnyx API](https://developers.telnyx.com/api-reference/texml-applications/creates-a-texml-application#creates-a-texml-application).
