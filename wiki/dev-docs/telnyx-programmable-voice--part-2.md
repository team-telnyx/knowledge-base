---
title: Telnyx Programmable Voice
summary: Telnyx Programmable Voice provides tools for building voice applications
  including SIPREC recording, speech-to-text transcription, call recording storage,
  SSML-based text-to-speech, and the TeXML markup language for declarative call control
  with TwiML compatibility.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/speech-to-text/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ssml-tags/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
updated_at: 2026-06-11T10:43:02Z
---

# Telnyx Programmable Voice

*Part 2 of 3 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 3](telnyx-programmable-voice--part-3.md)*

Telnyx Programmable Voice provides tools for building voice applications including SIPREC recording, speech-to-text transcription, call recording storage, SSML-based text-to-speech, and the TeXML markup language for declarative call control with TwiML compatibility.

## Storing Call Recordings

By default, recordings are stored in Telnyx-owned S3 buckets and a download link is provided in the `call.recording.saved` webhook (active for 10 minutes). Customers can instead store recordings in their own cloud storage.

### Custom Google Cloud Storage

```curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
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

The recording URL in the webhook will use the `gs://` scheme. See [GCS credential generation](https://cloud.google.com/iam/docs/keys-create-delete#creating) for details.

### Custom AWS S3 Storage

```curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
  --header 'Authorization: Bearer xxxx' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "backend": "s3",
    "configuration": {
      "bucket": "BUCKET_NAME",
      "region": "REGION_NAME",
      "aws_access_key_id": "AWS_ACCESS_KEY_ID",
      "aws_secret_access_key": "AWS_SECRET_ACCESS_KEY"
    }
  }'
```

The recording URL in the webhook will use the `s3://` scheme.

### Custom Microsoft Azure Blob Storage

```curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
  --header 'Authorization: Bearer xxxx' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "backend": "azure",
    "configuration": {
      "bucket": "BUCKET_NAME",
      "account_name": "AZURE_ACCOUNT_NAME",
      "account_key": "AZURE_ACCOUNT_KEY"
    }
  }'
```

The recording URL in the webhook will use the `https://` Azure blob URL scheme.

## TeXML Overview

TeXML is an XML-based markup language for defining call control instructions. It is the quickest way to get started with Programmable Voice using a simple `.xml` file containing commands called **verbs** and **nouns**. The TeXML interpreter executes commands sequentially from top to bottom.

A proper TeXML response comprises:

- A **`<Response>`** root element wrapping the document body
- **Verbs** — XML tags denoting the desired action (e.g. `<Say>`, `<Dial>`, `<Hangup>`)
- **Nouns** — XML tags denoting the object of the action (e.g. `<Number>`, `<Sip>`, `<Conference>`)

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling Telnyx. Please hold.</Say>
  <Dial>
    <Number>+13129457420</Number>
  </Dial>
</Response>
```

## TeXML Application Configuration

A TeXML Application is a collection of configuration parameters defining the interaction between Telnyx and your application:

| Field | Description |
|-------|-------------|
| Application Name | Descriptive name for the application |
| AnchorSite | Preferred data center; use `latency` to auto-select via ICMP ping |
| Voice Method | HTTP method for webhook interaction (GET or POST) |
| Webhook URL | URL where Telnyx fetches TeXML instructions; can be a TeXML Bin URL |
| Webhook Failover URL | Backup URL if the primary fails |
| Call Progress Events URL | URL for event callbacks |
| Status Callback Method | HTTP method (GET or POST) for status callbacks |
| Hang-up on Timeout | Seconds to wait for initial response before hanging up |
| DTMF Type | Configuration for touch-tone input handling |
| Enable Call Cost | Whether to send call cost webhooks |

Applications can be created through the [Mission Control Portal](https://portal.telnyx.com/#/call-control/texml/new) or via the [Telnyx API](https://developers.telnyx.com/api-reference/texml-applications/creates-a-texml-application).

## TeXML Instruction Fetching

### Inbound Calls

When Telnyx receives a call to a SIP subdomain or phone number assigned to a TeXML Application, it fetches instructions from the application's webhook URL.

### Outbound Calls

There are two ways to trigger instruction fetching on outbound calls:

1. **Using TeXML Calls API** — A TeXML application is required. Initiate via the REST endpoint:
   ```
   curl -L 'https://api.telnyx.com/v2/texml/Accounts/:account_sid/Calls' \
     -H 'Authorization: Bearer YOUR_API_KEY' \
     -d '{
       "ApplicationSid": "xxxxxxxx",
       "To": "+13121230000",
       "From": "+13120001234",
       "Url": "https://www.example.com/texml.xml",
       "StatusCallback": "https://www.example.com/statuscallback-listener"
     }'
   ```
2. **Using SIP Trunking Connections** — Configure a SIP trunking connection to "Park Outbound Calls". When an outbound call is initiated, Telnyx parks the leg, fetches instructions from the connection's URL, and processes the call. No TeXML application is required.

### HTTP Request Parameters

When fetching instructions, Telnyx always includes these parameters:

| Parameter | Description | Example |
|-----------|-------------|--------|
| AccountSid | User's Telnyx account ID | `6a9a7976-012e-45d2-9258-6f5dc68d861e` |
| CallSid | Unique call identifier | `fcc47bc6-e428-11ed-ad79-02420aef00b4` |
| CallSidLegacy | Legacy call ID for backward compatibility | same as CallSid |
| CallerId | Caller identifier | `+13122010091` |
| CallingPartyType | `sip` or `pstn` | `sip` |
| From | Initiating phone number | `+13122010091` |
| FromSipUri | Caller SIP URI | `+13122010091@10.239.182.10` |
| To | Receiving phone number | `+13122010090` |
| ToSipUri | Receiver SIP URI | `+13122010090@sip.telnyx.com` |
| ConnectionId | Telnyx connection ID | `1568109700606592442` |

Parameters are sent as URL query parameters (GET) or form-encoded body data (POST). The application should respond with valid TeXML (a `<Response>` root element, HTTP 200) without exceeding size limits.

## TeXML Bin

TeXML Bin allows uploading TeXML files to Telnyx storage for use in call flows without needing an application server. Create and manage TeXML Bin files from the Mission Control Portal under Voice → Settings → TeXML Bin.

### Quickstart Workflow

1. **Create your XML** — Use the TeXML editor in the portal to write instructions, for example a simple voicemail:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <Response>
     <Say>Thank you for calling YYZ co. Please leave a message.</Say>
     <Record playBeep="true" finishOnKey="*9" />
   </Response>
   ```
   Or a simple call forward:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <Response>
     <Dial>
       <Sip>ext1@sip.xyzco.com</Sip>
       <Sip>ext3@sip.xyzco.com</Sip>
       <Sip>ext4@sip.xyzco.com</Sip>
     </Dial>
   </Response>
   ```
2. **Set up the application** — In Mission Control, select the TeXML Bin script from the drop-down in your TeXML Application.
3. **Test** — Assign a phone number to the application, dial it, and verify the behavior.
