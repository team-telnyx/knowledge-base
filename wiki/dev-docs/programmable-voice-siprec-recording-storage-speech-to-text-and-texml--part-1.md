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

*Part 1 of 6 — see also: [Part 2](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-2.md), [Part 3](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-3.md), [Part 4](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-4.md), [Part 5](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-5.md), [Part 6](programmable-voice-siprec-recording-storage-speech-to-text-and-texml--part-6.md)*

A consolidated reference for Telnyx Programmable Voice features covering SIPREC client and server configuration, call recording storage backends, real-time speech-to-text transcription, and the TeXML markup language including applications, instruction fetching, dynamic templating, HTTP requests, and answering machine detection.

## SIPREC Client

A SIPREC client (SRC) is the component within the SIPREC framework responsible for initiating and managing the recording session. It communicates with a Session Recording Server (SRS) to send media streams and metadata for recording.

### Creating a SIPREC server connector

Before starting a recording session, define a SIPREC server connector that establishes the connection to the SRS:

```
curl --request POST \
  --url https://api.telnyx.com/v2/siprec_connectors \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "siprec-server-connector",
	"host": "siprec.telnyx.com",
	"port": 5060
}'
```

### Starting and stopping a SIPREC session for Voice API calls

Start a SIPREC recording session against an active Voice API call:

```
curl --request POST \
  --url https://api.telnyx.com/v2/{call_control_id}/actions/siprec_start \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json' \
  --data '{
        "connector_name": "siprec-server-connector",
        "direction": "both_tracks"
   }'
```

Stop the session at any point:

```
curl --request POST \
  --url https://api.telnyx.com/v2/{call_control_id}/actions/siprec_stop \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json'
```

### Starting and stopping a SIPREC session for TeXML calls

For TeXML calls, embed the `<Siprec>` verb inside a `<Start>` block to begin recording, and a `<Stop>` block to end it:

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Siprec track="both_tracks" connectorName="siprec-server-connector" statusCallback="https://example.com/siprec_callback" />
  </Start>
</Response>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Siprec/>
  </Stop>
</Response>
```

## SIPREC Server (SRS) Configuration

SIPREC (Session Initiation Protocol Recording) is a standardized mechanism for recording VoIP calls. A SIPREC server, also known as a Session Recording Server (SRS), captures and stores these communications for compliance, quality assurance, and other purposes.

### Step 1: Create a Voice API Application

1. Log in to the [Telnyx portal](https://portal.telnyx.com).
2. Navigate to **Voice → Programmable Voice → Voice API**.
3. Click **Add New Application** and configure the application settings, providing a meaningful name and description.

### Step 2: Assign an Inbound SIP Subdomain

Within the new Voice API Application, locate the **Inbound Settings** section and assign an inbound SIP subdomain. This subdomain routes incoming SIP traffic to your SIPREC server (for example, `yourcompany.sip.telnyx.com`). Save the changes.

![Configure siprec server connection](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/siprec_server_portal.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=a986c466f98811433aa2e50f77cf2da7)

### Step 3: Configure the SIPREC Client (SRC)

Configure your SIPREC Client to use the following Session Recording Server URI:

```
sip:username@siprec.telnyx.com;secure=true
```

- **username** — any SIP username; the value is dropped by the SRS.
- **siprec.telnyx.com** — the Telnyx SIPREC server (SRS) domain.

The destination host header must be sent in the INVITE message as a custom header: `X-DestHost`.

### Step 4: Configure SIPREC Token Authentication

SIPREC authentication tokens add an extra layer of security for SIPREC calls directed to your subdomain application. Configure up to two tokens per connection by updating the connection settings:

```
curl -X PATCH 'https://api.telnyx.com/v2/call_control_applications/:connection_id' \
-H 'content-type: application/json' -H 'authorization: Bearer <api-key>' \
--data-raw '{"siprec_tokens": ["test-token1", "test-token2"] }'
```

To enable authentication:

1. Add the token to the SIPREC INVITE request using the `X-Auth-Token` SIP header.
2. During SIPREC call setup, the token in the `X-Auth-Token` header is verified against either of the two configured tokens. Only verified tokens allow the SIPREC call to proceed.

### Step 5: Initiate and record the SIPREC call

When the SIPREC session starts, Telnyx sends two `call.initiated` webhooks — one for each SIP call of the media stream. Each webhook includes the `call_control_id` and the metadata from the original SIPREC call as custom headers such as `X-DestHost`, `X-Label`, `X-ParticipantID`, `X-SIPREC-SessionID`, `X-StreamID`, and `X-metadata-xml`.

Use the `call_control_id` to issue Voice API commands to answer and record both calls:

```
curl -L 'https://api.telnyx.com/v2/calls/v3:ehsopsWMfki2clglbX0x4zeJoD1lV52zwLnw7rDJq_-kJoSnZcr0LQ/actions/answer' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
```

```
curl -L 'https://api.telnyx.com/v2/calls/v3:ehsopsWMfki2clglbX0x4zeJoD1lV52zwLnw7rDJq_-kJoSnZcr0LQ/actions/record_start' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{}'
```

### SIPREC call flow

![SIPREC call flow](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/siprec_call_flow.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=5ecfa38288c9af3d0da2a28655137156)

1. A call is established on the user's SBC (which has SIPREC SRC capabilities) with RTP streams A and B.
2. The SIPREC SRC initiates a SIPREC call towards the Telnyx SIPREC SRS (`siprec.telnyx.com`) with two RTP streams (A and B).
3. The Telnyx SRS initiates two SIP calls towards `sip.telnyx.com`, one for each RTP stream, each with `a:sendonly` indicating that RTP is only sent and not received.
4. Telnyx sends two `call.initiated` webhooks to the Voice API application URL, one for each SIP call, including the `call_control_id` and the metadata from the original SIPREC call.
5. The `call_control_id` is used to issue Voice API commands to answer and record both calls.

### SIPREC metadata

Telnyx passes the metadata included by the SIPREC client on the original SIPREC INVITE message as custom SIP headers on the SIP calls, and each of these triggers a webhook containing all of the SIP custom headers.

Webhook variables with SIPREC metadata from the INVITE message received by the SIPREC SRS:

- **to** — the content of the SIP URI
- **SIP custom headers** — any SIP custom headers are included in the webhook
- **SIPREC XML default metadata** — extracted from the XML metadata and included in the webhook:
  - DataMode
  - ParticipantID
  - NameID-AOR
  - Associate-Time
  - StreamID
  - Label
- **SIPREC XML custom metadata** — any custom variables are also extracted from the XML metadata and included in the webhook
