---
title: Build a Call Center with TeXML and the Telnyx Voice API
summary: 'Learn how to stand up a simple yet extensible call center using TeXML and
  the Telnyx Voice API: route inbound calls to multiple agents, add queueing, voicemail
  and recording, detect answering machines on outbound legs, integrate Dialogflow
  ES, and optionally enable SIPREC for compliance recording.'
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
  content_hash: 0bf458fbc809c2b7a36e7a6d5372c778f686c193f37d80ece921378409ca1051
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
  content_hash: fcdfe6a4af680bf3cafd547884b274231be25a03c8ae875ecbfe4b815b3255ba
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
  content_hash: bfae202034bacfe313c356c98c338a6bb32a8f8295e1df3f037bb0be3368a472
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
  content_hash: 337f0ca2af78bd549d75b2fcaf8b2c682a725992eff0bcf44b45b7ed32b44bcb
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
  content_hash: c86d85d99b148a6fa6bd5058414352fece7f68a44b7358f4392f8b7d63bbf008
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
  content_hash: 56ab3dd523c210a790aa9895a6a3726a1a2a66d035ba39579b51cf050df9ebb6
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
  content_hash: 8e6469160e60781d5a7734d99169040762f635ef0fc99ff097cbefbf3c1370e8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
  content_hash: 2e0b6e278dd3a8bf90febe2abee150c72c034a62aaff8f78ed3c06a4cc9e0512
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
  content_hash: f87b022b285ccb562258a1f2e65487db2acd65d18a70d2f9076c39a2a38047d1
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
  content_hash: ba81bcb1b369f61f4cb77064548a6f7ea827d8a5be2ff283c05a9e1ce48742ac
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
  content_hash: 906d83ba4b672f2646f30e3311d3727b9e3c12e59d7e8f7d3d95fcdddbf00e56
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
  content_hash: f06cb0df36c49852ff58e838af48e8ff0f25794c94b7674643f0b1392271d258
updated_at: 2026-05-20T09:32:42Z
---

# Build a Call Center with TeXML and the Telnyx Voice API

*Part 1 of 2 — see also: [Part 2](build-a-call-center-with-texml-and-the-telnyx-voice-api--part-2.md)*

Learn how to stand up a simple yet extensible call center using TeXML and the Telnyx Voice API: route inbound calls to multiple agents, add queueing, voicemail and recording, detect answering machines on outbound legs, integrate Dialogflow ES, and optionally enable SIPREC for compliance recording.

## Overview
This guide combines Telnyx call-center best practices and sample code into one flow you can run locally in minutes, then extend with advanced Voice API features. You’ll:
- Receive inbound calls to a Telnyx number and fan them out to multiple SIP agents (softphones, desk phones, WebRTC).
- Control the flow with TeXML templates you can edit without server code changes.
- Add queueing, voicemail and storage, AMD on outbound, Dialogflow ES, and SIPREC.
- Run everything locally behind ngrok while you iterate.

Useful background: [Voice API Fundamentals](voice-api-fundamentals.md), [Sending Commands](sending-commands.md), [Receiving Webhooks](receiving-webhooks.md), [TeXML TwiML Compatibility](texml-twiml-compatibility.md).

## Call flow and architecture
Baseline flow from the sample app:
1. Caller dials your Telnyx number; TeXML plays a TTS greeting.
2. The app simultaneously dials multiple SIP Connections (agents) via SIP URI; call recording can be enabled.
3. First agent to answer is bridged; other rings stop.
4. If no answer, the app retries once; if still no answer, it offers voicemail and stores the recording.
5. On hangup, the caller hears a final message.
All steps are defined by TeXML files you can customize (greeting, retry logic, voicemail prompts, post-call behavior).

## Prerequisites and portal setup
- Create a Telnyx account and API key in Mission Control Portal.
- Expose your local app with ngrok and note the HTTPS forwarding URL.
- Create a TeXML Application and set:
  - Voice Method: GET, Voice URL: https://<your-ngrok>/TeXML/inbound
  - Status Callback Method: POST, URL: https://<your-ngrok>/TeXML/events
- Buy a voice-enabled number and assign it to the TeXML Application at checkout.

Resources: sample app (Python, AIOHTTP + TeXML) and a video walkthrough are in the Telnyx repos and site:
- GitHub: demo-python-telnyx/call-center-texml (call-center)
- Video: “Call Center Demo (Python)” on telnyx.com

## Create agents’ SIP Connections
Create one Credentials-based SIP Connection per agent:
- Inbound options: enable “Receive SIP URI calls” (From anyone) so agents can receive SIP-URI dials.
- Events (webhooks) for agent call status: set Webhook URL to https://<your-ngrok>/outbound/event so the app knows when to stop ringing others after one answers.
- Optional per-agent caller ID override for outbound.
Agents can register with softphones or WebRTC; see Telnyx configuration guides and the free WebRTC demo tool.

## Outbound Voice Profile for agent forwarding
Create an Outbound Voice Profile and add all agent SIP Connections (and/or the TeXML App) to permit forwarding dials. Enable international destinations if needed.

## Run the sample app (Python)
- Requires Python 3.6+; create a virtualenv and install dependencies (e.g., pipenv, aiohttp, apscheduler, python-dotenv).
- From the repo root, run the setup script to scaffold a .env and then start the app on localhost:8080.
You’ll see TeXML instructions fetched by the app via your ngrok URL.

## Environment variables
Populate the app’s .env with at least:
- API_KEY: Telnyx API key.
- NGROK_URL: your HTTPS forwarding URL.
- OUTBOUND_PROFILE_ID: the Outbound Voice Profile ID used for forwarding.
- PROD: true/false (enables scheduled jobs in the sample).
- Optional SLACK_URL for basic notifications.

## Test the flow
- Call the number you purchased. The greeting plays, and registered agents begin ringing.
- Accept on one agent; the others stop. Hang up to hear the closing message.
- Decline to test the retry + voicemail path.

## Optional customizations with TeXML
Edit the TeXML files under the repo’s TeXML directory to change behavior:
- Hangup behavior: in answered.xml, the default uses <Say>. You can instead <Dial> to another target or <Redirect> to an IVR.
- Custom audio: place mp3 files (e.g., support_greeting.mp3, support_busy.mp3) in the app’s audio folder and switch templates from <Say> to <Play>.
- Voicemail: configure the Record verb and a recording status callback URL in voicemail.xml to receive the final recording link.
Reference: [TeXML Fundamentals](texml-fundamentals--part-1.md), [TeXML Verbs: Say](texml-verbs-say.md), [TeXML Verbs: Play](texml-verbs-play.md), [TeXML Verbs: Record](texml-verbs-record.md), [TeXML Verbs: Redirect](texml-verbs-redirect.md), [TeXML Verbs: Dial](texml-verbs-dial.md).

## Voicemail and recordings
When recording is enabled, Telnyx sends a call.recording.saved webhook containing time-bound download URLs by default. You can store recordings in your own cloud instead of Telnyx S3:
- Bring-your-own storage: AWS S3, Google Cloud Storage, or Azure Blob via the Custom Storage Credentials API bound to your Voice/TeXML application.
- Webhooks include cloud-native URIs (gs://, s3://, Azure https URL) once configured.
See [Storing call recordings](storing-call-recordings.md) for request formats and permission requirements.

## Queueing callers and dispatching agents
Add queueing to smooth spikes and route the next waiting caller to the next available agent:
- Put a call in a queue from your server code using the enqueue command with a queue_name (e.g., “support”). If bridged, it’ll be unbridged and parked first.
- Bridge an agent to the queue by issuing bridge with queue set to the same queue_name; the first call in that queue is dequeued and bridged.
- Remove a call with leave_queue or by hanging up/transferring/bridging elsewhere; optional max_wait_time can auto-dequeue.
Use the queue inspection endpoints to list queues and calls. Details: [Queueing Calls](queueing-calls.md).

## Detect voicemail on outbound legs (AMD)
If your center places outbound calls (or transfers inbound callers to PSTN), enable Answering Machine Detection to adapt flows:
- Standard AMD modes: detect, detect_beep, detect_words, greeting_end.
- Premium AMD (recommended): machine vs human_business/human_residence plus beep/no_beep; optional iOS Call Screening support.
- You’ll receive webhooks like call.machine.detection.ended or call.machine.premium.detection.ended and …greeting.ended to time your message or transfer.
For TeXML-originated outbound, you can enable AMD synchronously or asynchronously and receive AnsweredBy or async callbacks to branch instructions. See [Answering Machine Detection](answering-machine-detection.md) and [TeXML Answering Machine Detection Support](texml-answering-machine-detection-support.md).

## Add compliant recording with SIPREC
For regulated use cases, start a SIPREC session to stream call media and metadata to an SRS:
- Create a SIPREC connector (host, port), then start/stop SIPREC on a live Voice API call via siprec_start/siprec_stop.
- In TeXML, use <Start><Siprec …/> and <Stop><Siprec/>.
- Or bring your own SRS: assign an inbound SIP subdomain to your Voice API app, configure your SRC to target siprec.telnyx.com with optional token auth, and control the resulting calls via Voice API (two call legs, one per stream) to answer/record.
See [Using SIPREC client for Voice API and TeXML calls](using-siprec-client-for-voice-api-and-texml-calls.md) and [Telnyx SIPREC server (SRS) Configuration Guide](telnyx-siprec-server-srs-configuration-guide.md).

## Bring AI to your IVR with Dialogflow ES
Attach Dialogflow ES so caller audio streams to your agent and bot responses are played back:
- First, assign Dialogflow credentials to your Voice API application (service account JSON as an encoded blob).
- Enable per-call: set enable_dialogflow true when creating an outbound call or when answering an inbound call.
- Listen for dialogflow.detectintent.response webhooks carrying transcripts, fulfillment messages, and confidence to drive business logic.
Reference: [Dialogflow ES](dialogflow-es.md).
