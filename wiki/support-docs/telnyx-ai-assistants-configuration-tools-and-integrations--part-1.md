---
title: 'Telnyx AI Assistants: Configuration, Tools, and Integrations'
summary: End-to-end guide to configuring Telnyx AI Assistants in Mission Control,
  optimizing call quality with Noise Suppression, and integrating with third-party
  platforms like Vapi and ElevateAI. Includes tool setup (webhook, handoff, transfer,
  SIP Refer, DTMF, MCP), testing, troubleshooting, security tips, and Flow deprecation
  guidance.
sources:
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
  content_hash: da295b7e591d46f557f38a89261715e9dc2918558022b967d9d70a298feaff28
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
  content_hash: f3f18221694b4adc3a303b47707bf341e91f450359b978632d0c670a318d269f
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
  content_hash: 0b38896d79229e16ace3215e19a9acce12177aec21274cc28e142eb6e4845350
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
  content_hash: 36092e79d5aec26ca42e3005364332db254183a47eb7617e15387d08b40c6c1e
- url: https://support.telnyx.com/en/articles/9413928-telnyx-flow
  content_hash: 93a8336c12ddb49e50315a93376191e9a40bcbefde1b2a126930a23fd05da7c3
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
  content_hash: cc2a5003580a55972312e66f093b91bcaee45eda919fc9208e24d6f7cb8c7c87
- url: https://support.telnyx.com/en/collections/9526270-telnyx-flow
  content_hash: 0eb5a9c8ea9582c54f99e57190c78c96a20b360ac6e04acfe401906039e5392e
updated_at: 2026-05-20T15:32:10Z
---

# Telnyx AI Assistants: Configuration, Tools, and Integrations

*Part 1 of 2 — see also: [Part 2](telnyx-ai-assistants-configuration-tools-and-integrations--part-2.md)*

End-to-end guide to configuring Telnyx AI Assistants in Mission Control, optimizing call quality with Noise Suppression, and integrating with third-party platforms like Vapi and ElevateAI. Includes tool setup (webhook, handoff, transfer, SIP Refer, DTMF, MCP), testing, troubleshooting, security tips, and Flow deprecation guidance.

## Where to configure AI Assistants in Mission Control
- In the Telnyx Mission Control Portal, go to AI, Storage & Compute → AI Assistants.
- Create from a blank canvas or start with templates (Lead Qualification, Survey & Feedback, Customer Service).

## Model selection and secrets management
- Choose an LLM model (e.g., open source models like Qwen or commercial providers). If using a third-party model (e.g., OpenAI), supply the API key.
- Store sensitive keys as Integration Secrets to hide them from org members and reduce exposure risk.
- Configure a fallback model to take over automatically if the primary model has issues—even mid-call.

## Prompts, greetings, and dynamic variables
- Instructions: define tone, behavior, and constraints; insert dynamic variables for real-time call context.
- Greeting: specify an opening line; dynamic variables are supported here too.
- Dynamic variables webhook URL: if set, the assistant fetches variables at runtime from your endpoint. See dynamic variables docs: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables

## Built-in and add-on tools
- Default capability: the assistant can hang up when appropriate.
- Add optional tools: Webhook Tool, Handoff Tool, Transfer Tool, SIP Refer Tool, Send DTMF, and MCP server.

## Webhook Tool configuration
- Name: descriptive, no spaces (e.g., call_status_webhook).
- Description: simple statement of purpose (e.g., callstatus_updates).
- Timeout (ms): 1,000–5,000 recommended. Requests failing to respond in time are treated as failed.
- Method: choose HTTP method (commonly POST). Telnyx expects an HTTP 2xx for success.
- URL: your webhook endpoint (e.g., https://example.com/webhooks/call-status).
- Advanced options:
  - Headers: add auth and content headers (e.g., Authorization: Bearer <token>, Content-Type: application/json).
  - Path parameters: template values into URL paths (e.g., /webhooks/{assistant_id}/status).
  - Query parameters: append key-value pairs (e.g., ?version=1.0&token=secureToken123).
  - Body parameters: include custom fields with event payloads (e.g., assistant_id, event_type, timestamp, custom metadata) to add app context.

## Handoff Tool for multi-agent experiences
- Purpose: add another AI assistant to assist or specialize mid-conversation (e.g., primary agent books lodging; handoff agent handles travel).
- Voice mode:
  - Unified: all agents share the same voice so handoffs are transparent.
  - Distinct: each agent keeps its own voice for a “conference” feel.
- Best practices: give the handoff agent a clear display name and select it from the dropdown when configuring.

## Transfer and SIP Refer tools
- Transfer Tool: move the live call from the AI assistant to a human or another endpoint within your system.
  - From number / SIP URI: source identity; numbers must be owned by the org and associated with a connection that has an outbound voice profile.
  - Targets: friendly name (e.g., Live Agent 1).
  - To number / SIP URI: destination E.164 number or SIP URI (e.g., sip:user@domain).
  - Custom headers: add SIP INVITE headers (e.g., Name: AI transfer, Value: Front Desk).
- SIP Refer Tool: refer a call to an external SIP infrastructure during a TeXML flow.
  - Configure Targets, a descriptive Name, SIP Address (e.g., sip:+14085551234@sip.example.com), SIP auth username/password as needed.
  - Optional SIP headers (User-User, Diversion) and custom headers (e.g., X-Campaign-ID: 12345).
- When to use which:
  - Transfer: keep routing within the same system/application.
  - SIP Refer: hand calls off to external SIP providers/infrastructure.

## Send DTMF tool
- Purpose: programmatically send DTMF tones to navigate IVRs during calls. Preconfigured and ready to use.

## MCP server integration
- MCP (Model Context Protocol) connects AI models to external tools/data.
- Add an MCP server so assistants can use org tools (e.g., Sheets, Calendar, Zapier).
- Types:
  - HTTP: stateless request–response (GET/POST, etc.).
  - SSE: server-sent events for one-way streaming from server to client.
- Fields: Name (descriptive), Type (HTTP/SSE), URL.
- Demo and low-latency overview: https://telnyx.com/resources/build-low-latency-voice-assistant

## Noise Suppression for Voice AI quality
- Benefit: cleaner audio improves human listening, STT accuracy, and Voice AI performance.
- Scope: set at connection level to affect all associated numbers and override number-level settings. Configure per direction (inbound, outbound, both). Billing applies per direction; see pricing: https://telnyx.com/pricing/voice-api
- Configure in Portal:
  - Mission Control → Voice → SIP Trunking → select connection → Configuration → Advanced → Noise Suppression → choose model + direction → Save.
- Configure via API:
  - Use noise_suppression in connection/number configs, or call suppression_start with noise_suppression_engine on active calls. Developer docs: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- Direction options:
  - Inbound only: cleans audio you receive from Telnyx.
  - Outbound only: cleans audio you send to Telnyx.
  - Both: maximum clarity; billed per direction.
  - Disabled: pass-through.
- Model guidance (pick what matches your pipeline):
  - Denoiser: lightweight general default.
  - Krisp Viva Tel Lite: standard SIP/telephony and contact centers.
  - Krisp Viva Pro: WebRTC/browser softphones and multi-talk/echo scenarios.
  - Krisp Viva SS: far-field mics, smart speakers, conference rooms.
  - AIcoustics Rook Small: excellent for AI assistant calls; also removes reverb.
  - AIcoustics Rook Large: same as Small, scaled for harsh acoustic environments.
  - AIcoustics Quail Voice Focus S: tuned for STT/Voice AI—preserves phonetics for machines; ideal for assistants and transcription pipelines.
