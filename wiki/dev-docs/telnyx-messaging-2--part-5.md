---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
  content_hash: d98fde358c8bb0a6117412a2971da4898405065ec7c3650984ae9a6494d9dcd3
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
  content_hash: 192a65ec89e4ea6a7be165a7b17a5e44f6ecd3121b756cc292aebd63a50fee49
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
  content_hash: e691bcb40f682bbc7d1087d2755ac4c3680e9cf93520f97c0d86645ab7657ad4
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
  content_hash: 458a86b8e1297624173a766ba456ed0768c0cb62eb8d60575ce3367c8625c318
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
  content_hash: 362df72c3dbe5bdfb19da2c433895133466aa88bd4ab4737f7754ecf0892fa18
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
  content_hash: f170f09f5d980d0e492e300a0e07ce6b1591881c60d71f8f506f2a02ad2cc34b
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
  content_hash: 62bd8025784ec0901f20d6bc1597886e9df41722271dcc11c7b8d8a86d2c94a1
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
  content_hash: c088661a2d1c9ce8faaf92b86e072d0951aa7bf6301ed3bc75f1825e75c5b505
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
  content_hash: 33d60e88cce1298b6009415cd6dc5afb26a05430927e0b5e286cd9ec8770efaa
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
  content_hash: 6adf9a29c630ce93d9fd16b676d2d2df67db1a1772c5e97c9e33646f6597ec0f
updated_at: 2026-06-11T10:38:14Z
---

# Telnyx Messaging

*Part 5 of 5 — see also: [Part 1](telnyx-messaging-2--part-1.md), [Part 2](telnyx-messaging-2--part-2.md), [Part 3](telnyx-messaging-2--part-3.md), [Part 4](telnyx-messaging-2--part-4.md)*

Telnyx Messaging provides APIs and infrastructure for sending and receiving SMS, MMS, and RCS messages globally. This page covers phone number configuration, messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international compliance, and RCS with AI integration.

## RCS with AI Assistant

Build an AI-powered RCS agent that answers customer questions automatically by connecting your RCS agent to Telnyx AI Assistant. No custom backend code is required.

### How it works

The messaging profile links your RCS Agent to an AI Assistant via the `ai_assistant_id` field. When a customer replies, the AI Assistant automatically receives the inbound message, processes it with the configured LLM and knowledge base, and sends an intelligent response back via RCS.

### Setup steps

1. **Create an AI Assistant** in the portal (AI Assistants section). Configure the persona with instructions, add knowledge sources (documents, website crawls, or API connections), and save the Assistant ID.
2. **Create a messaging profile** with AI enabled. In profile settings, select your AI Assistant from the dropdown or enter the Assistant ID.
3. **Link your RCS Agent** to the AI-enabled messaging profile. Update the agent's `profile_id` via API, or request provisioning on the AI profile during carrier approval.
4. **Test** by sending an RCS message to your agent. Customer replies are automatically handled by the AI.

### AI Assistant best practices

- Keep responses mobile-friendly (under 160 characters when possible, use bullet points).
- Set a greeting message to welcome new customers.
- Include escalation instructions for when the AI should hand off to a human (e.g., billing disputes, frustrated customers).
- Test with real questions from your support ticket history and FAQ analytics before going live.

### Monitoring and pricing

Track AI Assistant performance in the portal: conversation logs, knowledge gaps, and response times. RCS messages and AI Assistant are priced separately; AI charges are based on tokens processed (typically fractions of a cent per exchange for simple Q&A).
