---
title: Telnyx Programmable Voice
summary: 'Telnyx Programmable Voice provides multiple paradigms for building voice
  applications: the Voice API (Call Control) for programmatic call management, TeXML
  for XML-driven call flows, and AI Assistants for no-code conversational AI. This
  page covers configuration, compatibility, real-time transcription, third-party integrations,
  and migration guidance.'
sources:
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
  content_hash: 8ad66d6c9ea440951f259f45a6639b7abdbc3762c8808b57774d2fe4d60f2783
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
  content_hash: 79afc77e4a975867133c6229080f1870df4e29203581a2478b9a3fc0d2156692
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
  content_hash: 796dc56257808f5e02f4e076a2b65788bfa9d791ab06a565014e8c8345ef7344
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
  content_hash: d3098961d17ae5558a906b63a69ef91d005647ce75cf01b844d239258b3718c7
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
  content_hash: b446fc44af8df4f3f3b7050ef415b1fadccc6aa4e17e7af6463f1d2c863bfde2
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
  content_hash: 7f026b4e298be9c1cdbc1d17345b7f469b7d6c5245fb4dc81a485ebb089163d8
- url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
  content_hash: 76a7beabc40726462c19c585a7ec962f8b56840817ff7da0a189c6186943a562
- url: https://support.telnyx.com/en/articles/9413928-telnyx-flow
  content_hash: 61bba2d7c7e49fcb586998819a9bd3107405f5a685d462e3cc484f5efe30ad1f
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
  content_hash: b11a5bdfb665e039b8a9927cebf7acbfdb5f7c8a5f1fd43631989d2e8b27a947
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
  content_hash: 95152862fbcb84bca63783a9ab66c43f144b2976be4888290a32c7a9b312d6d9
- url: https://support.telnyx.com/en/collections/9526270-telnyx-flow
  content_hash: da5c6979781c13f828bafee007d84d826b44739ecd4cba8ef4c0f7f8c1efbc0b
updated_at: 2026-06-11T11:40:11Z
---

# Telnyx Programmable Voice

*Part 2 of 3 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 3](telnyx-programmable-voice--part-3.md)*

Telnyx Programmable Voice provides multiple paradigms for building voice applications: the Voice API (Call Control) for programmatic call management, TeXML for XML-driven call flows, and AI Assistants for no-code conversational AI. This page covers configuration, compatibility, real-time transcription, third-party integrations, and migration guidance.

## AI Assistants

AI Assistants provide a no-code way to manage inbound/outbound calling and messaging through the Telnyx Mission Control Portal, under the **AI, Storage and Compute** tab.

### Creating an assistant

Start from a blank canvas or use popular templates (Lead Qualification, Survey and Feedback Specialist, Customer Service Representative). Give the assistant an appropriate name.

### Model selection

Choose an open-source model (e.g., Qwen) or a provider model like OpenAI. For provider models, add the API key in the relevant field. API keys can be saved as **integration secrets**, hiding them from other org members and securing against bad actors.

### Fallback model

Configure a fallback model that steps in if the primary model experiences issues — even mid-call.

### Instructions and greeting

- **Instructions**: Specify instructions, greetings, and mannerisms the LLM should use. Dynamic variables can insert real-time call data ([dynamic variables docs](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)).
- **Greeting**: Specify the greeting the agent should follow. Dynamic variables are supported.
- **Dynamic variables Webhook URL**: If populated, dynamic variables are fetched from the specified webhook and provided to the assistant in real time.

### Tools

Every AI assistant can hang up calls by default. Additional tools can be added:

#### Webhook tool

Sends HTTP requests to external services. Configuration fields:

- **Name**: Descriptive name, no spaces (e.g., `call_status_webhook`).
- **Description**: Clear explanation of what the webhook does.
- **Timeout (ms)**: Maximum wait time. Recommended: 1000–5000 ms (1–5 seconds). Telnyx requires an HTTP 2xx response to confirm successful delivery.
- **Method**: HTTP method (e.g., `POST`).
- **URL**: Webhook endpoint URL.

Advanced settings:

- **Headers**: Custom headers for authentication or format specification (e.g., `Authorization: Bearer your_api_key_here`).
- **Path Parameters**: Dynamic values injected into the URL path (e.g., `{assistant_id}` → `12345`).
- **Query Parameters**: Key-value pairs appended to the URL for filtering, versioning, or security tokens.
- **Body Parameters**: Custom fields in the request body (usually JSON) for additional metadata.

#### Handoff tool

Add another AI assistant to help the current agent. For example, an accommodation booking agent can hand off to a travel arrangements agent. This enables specialization while agents work as a team.

- **Unified voice mode**: All agents share the same voice, making the handoff transparent.
- **Distinct voice mode**: Each assistant retains its own voice config, providing a conference-call-like experience.

Give the handoff agent a descriptive display name and select the target AI assistant from the dropdown.

#### Transfer tool

Moves the call from the AI assistant to a real person.

- **From number / SIP URI**: Must be owned by the user or organization and have a connection with an attached outbound voice profile.
- **Targets**: Name of the transfer target (e.g., "Live agent 1").
- **To number / SIP URI**: Destination number or SIP URI (e.g., `sip:user@domain`).
- **Custom headers**: Added to the SIP INVITE during transfer.

#### SIP Refer tool

Transfers a call to external SIP infrastructure during a TeXML call.

- **Targets**: Name of the refer target.
- **Name**: Descriptive name for the refer.
- **SIP Address**: SIP sub-domain to refer (e.g., `sip:+14085551234@sip.example.com`).
- **SIP Auth Username / Password**: Authentication credentials.
- **SIP Headers**: Optional headers (User-User or Diversion).
- **Custom headers**: Name-value pairs passed on SIP messages (e.g., `X-Campaign-ID: 12345`).

#### Transfer vs SIP Refer

- **Transfer**: Moves a call within the same system/application. Use when redirecting to another department within your organization.
- **SIP Refer**: Transfers a call to an external SIP system/provider. Use when the call needs to be handled by different SIP infrastructure.

#### Send DTMF

Pre-configured tool for sending DTMF tones during a call, useful for completing IVR options on outbound calls.

#### MCP server (Model Context Protocol)

MCP standardizes how AI models send requests and receive context/data from external tools, data sources, or services (e.g., Google Sheets, Calendar).

- **Name**: Descriptive and easy to remember.
- **Type**: `HTTP` or `SSE`.
- **URL**: The MCP server endpoint.

**SSE (Server-Sent Events)**: Provides real-time streaming connections where the server pushes updates to the client over a single, long-lived HTTP connection. It's lightweight, one-way (server → client), and uses plain HTTP.

**HTTP**: Uses standard HTTP methods for structured, stateless request-response communication. Each request is independent; the server doesn't remember past interactions.

## Real-Time Transcription

Real-time transcription converts spoken language into written text as the conversation happens. Available with both the Voice API and TeXML. SIP Trunking users must convert to a programmatic voice option to use speech-to-text.

### Transcription engines

- **Engine A (Google)**: Default engine. Supports `interim_results` for faster but less accurate results. Approximately $0.050/minute.
- **Engine B (Telnyx)**: More accurate and less costly. Approximately $0.025/minute. Does not support interim results.

Check current pricing at [portal.telnyx.com/#/pricing/voice](https://portal.telnyx.com/#/pricing/voice) under Voice > Speech to Text.

### Voice API parameters

- `call_control_id`, `client_state`, `command_id`, `interim_results` (Google only), `language`, `transcription_engine` (A or B), `transcription_tracks` (`inbound`, `outbound`, or `both`).

### TeXML attributes

TeXML provides corresponding attributes for transcription configuration via the `<Start Transcription>` and `<Stop>` verbs.

### Automatic transcription with recording timeout

If you set a timeout on call recording (recording stops after a period of silence), Telnyx uses transcription to detect that silence. This automatically triggers real-time transcription even if not explicitly enabled, and you will be billed for it.

### Use cases

- **AI integration**: Pass transcription to AI/LLM systems for evaluation, summarization, or participation.
- **Voicemail**: Read and share written transcripts of voicemails.
- **Business meetings**: Written records for later review.
- **Legal compliance**: Live transcripts of legal proceedings.
- **Accessibility**: Helps hearing-impaired participants.
- **Customer service**: Real-time analytics and quality control.
