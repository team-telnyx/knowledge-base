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

*Part 2 of 2 — see also: [Part 1](telnyx-ai-assistants-configuration-tools-and-integrations--part-1.md)*

End-to-end guide to configuring Telnyx AI Assistants in Mission Control, optimizing call quality with Noise Suppression, and integrating with third-party platforms like Vapi and ElevateAI. Includes tool setup (webhook, handoff, transfer, SIP Refer, DTMF, MCP), testing, troubleshooting, security tips, and Flow deprecation guidance.

## Vapi: connect a Telnyx number
- Two setup paths:
  - Import an existing Telnyx number into Vapi (recommended).
  - BYO Telnyx SIP trunk (only for advanced SIP routing needs).
- Prerequisites:
  - Active Telnyx and Vapi accounts, Telnyx voice-capable number, Vapi assistant/squad, Telnyx API v2 key for Vapi, and (for outbound) an Outbound Voice Profile with destinations enabled.
- Set up the assistant in Vapi: name, greeting, instructions, voice/model, tools/webhooks/transfer logic. Quickstart: https://docs.vapi.ai/quickstart/phone
- Purchase/choose a Telnyx number in Mission Control → Numbers; copy in E.164 (e.g., +15551234567).
- Create a dedicated Telnyx API key for Vapi and follow key hygiene (name clearly, store only in Vapi, rotate if exposed, delete if unused). API key guidance: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- Import the Telnyx number in Vapi: Phone Numbers → Create → Telnyx → enter number details → paste Telnyx API key → save → assign the assistant/squad. Guide: https://docs.vapi.ai/telnyx
- Enable outbound via Telnyx:
  - Mission Control → Voice → Outbound Voice Profiles: create/edit; enable destination countries; under Connections and Applications attach Vapi; save. Docs: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index
- Test:
  - Inbound: call the number; confirm Vapi answers and behaves as configured; check Vapi logs if not.
  - Outbound: place a call from Vapi using the imported Telnyx number to an enabled destination; confirm caller ID rules are met.
- Advanced: BYO Telnyx SIP trunk
  - Retrieve Vapi private key; create/select Telnyx SIP trunk.
  - Configure Telnyx inbound SIP routing to Vapi and assign the Telnyx number to the trunk.
  - Set the Telnyx number’s translated number to the Vapi SIP URI (e.g., sip:<unique-id>@sip.vapi.ai).
  - For inbound-enabled gateways, use IP addresses (do not use sip.telnyx.com as gateway value).
  - Create outbound SIP credentials in Telnyx if Vapi will originate calls.
  - Create/update an Outbound Voice Profile and attach the SIP trunk.
  - Create the SIP trunk credential in Vapi, add the number, and assign the assistant. Guides: https://docs.vapi.ai/advanced/sip/telnyx and https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors
- Troubleshooting highlights:
  - Import failures: verify number is active, voice-capable, in your Telnyx account, E.164 formatted, and API key is valid.
  - Inbound not reaching Vapi: confirm number appears in Vapi with correct assistant; for SIP, ensure number is assigned to the trunk and translated number matches Vapi SIP URI.
  - Outbound failures: verify destination is enabled, Level 2 verification completed if required, and Vapi/trunk is attached to the correct Outbound Voice Profile; check caller ID allowances.
  - SIP/gateway errors: use IPs for inbound-enabled Vapi gateways; validate SIP credentials and IP allowlists for Vapi signaling.

## ElevateAI: transcription and recording PoC
- Create a Call Control application in Mission Control → Voice → Programmable Voice → Add new App; set webhook URL and save.
- Purchase a Telnyx number (Numbers → Search & Buy); assign it to the Call Control app during checkout.
- Sign up for ElevateAI, then copy your API token (Account → Manage Keys). https://www.elevateai.com/
- Clone and run the sample PoC: https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control

## Telnyx Flow deprecation and migration
- Telnyx Flow sunsets on July 3, 2026; workflows stop and Flow webhooks cease delivery.
- Action required: before the sunset date, update any Voice or Messaging application webhooks that point to Flow to your own hosted service or an alternative orchestration platform.
- Options:
  - Build directly with Telnyx APIs (Voice, Messaging, Chat Completions) or use No-Code AI Assistant to accelerate deployment: https://developers.telnyx.com/api-reference/overview and https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant
  - Prefer visual tooling? Consider n8n with the Telnyx AI node.

## Testing and troubleshooting
- Validate end-to-end:
  - Calls connect, assistant answers promptly, greeting/instructions render correctly, tools (webhooks, transfer, DTMF) function.
  - If using Noise Suppression, verify audible clarity and STT accuracy improvements; adjust model and direction as needed.
  - For outbound, confirm destination permissions, verification status, valid caller ID, and correct Outbound Voice Profile attachment.
- Logs and diagnostics:
  - Use Telnyx CDRs/SIP Call-IDs and partner logs (e.g., Vapi) to trace failures.
  - Confirm webhook endpoints respond with 2xx within configured timeouts and implement authentication.

## Support and security best practices
- When contacting Telnyx Support (help@telnyx.com), include: Telnyx phone number(s), flow used (import vs BYO trunk), call direction, source/destination numbers, timestamp/timezone, partner call ID (e.g., Vapi), Telnyx CDR/SIP Call-ID, and non-sensitive screenshots.
- Do not share secrets: API keys, SIP passwords, private keys.
- Use Integration Secrets for third-party model keys; add auth headers to webhooks; rotate credentials if exposed; remove unused keys.

## References
- Dynamic variables: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- Noise Suppression (pricing): https://telnyx.com/pricing/voice-api
- Noise Suppression dev docs: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- Outbound Voice Profiles: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index
- Telnyx API keys guidance: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- Vapi phone quickstart: https://docs.vapi.ai/quickstart/phone
- Vapi Telnyx import: https://docs.vapi.ai/telnyx
- Vapi Telnyx SIP: https://docs.vapi.ai/advanced/sip/telnyx
- Vapi SIP troubleshooting: https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors
- ElevateAI PoC repo: https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control
- Low-latency AI assistant demo: https://telnyx.com/resources/build-low-latency-voice-assistant
