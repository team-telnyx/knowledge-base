---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
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
