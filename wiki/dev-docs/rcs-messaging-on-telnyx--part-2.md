---
title: RCS Messaging on Telnyx
summary: RCS (Rich Communication Services) on Telnyx enables rich, interactive messaging
  beyond SMS, with support for rich cards, carousels, suggested actions, AI-powered
  assistants, capability lookups, deeplinks, and carrier-specific throughput considerations.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
updated_at: 2026-08-05T13:55:58Z
---

# RCS Messaging on Telnyx

*Part 2 of 3 — see also: [Part 1](rcs-messaging-on-telnyx--part-1.md), [Part 3](rcs-messaging-on-telnyx--part-3.md)*

RCS (Rich Communication Services) on Telnyx enables rich, interactive messaging beyond SMS, with support for rich cards, carousels, suggested actions, AI-powered assistants, capability lookups, deeplinks, and carrier-specific throughput considerations.

## RCS with AI Assistant

Combining RCS with Telnyx AI Assistant solves two problems: RCS carrier onboarding requires functional agents before approval, and building conversational AI is hard. AI Assistant gives your agent real functionality instantly and handles NLP/LLM integration with your knowledge sources.

| Traditional approach | With Telnyx AI Assistant |
| --- | --- |
| Build custom webhook handler | Configure in portal |
| Integrate LLM (OpenAI, etc.) | Built-in LLM |
| Manage conversation state | Handled automatically |
| Build knowledge retrieval | Upload docs or connect sources |
| Weeks of development | Minutes to configure |

### Prerequisites

- A Telnyx account
- An approved RCS Agent (or one in the approval process)
- Content for your AI Assistant (FAQs, docs, or knowledge base)

### Step 1: Create an AI Assistant

1. Navigate to [AI Assistants](https://portal.telnyx.com/#/app/ai/assistants) in the portal.
2. Click **Create Assistant** and give it a name (e.g., "Support Bot").
3. Configure the persona with instructions that define your assistant's behavior, for example:

```
You are a helpful customer support agent for [Your Company].

Guidelines:
- Be friendly and professional
- Keep responses concise (under 160 characters when possible)
- If you don't know something, offer to connect them with a human
- Always greet new customers warmly
```

4. Add knowledge sources: upload PDFs/text/markdown documents, crawl websites, or connect via API for dynamic content.
5. Save and copy the Assistant ID (e.g., `assistant-11deda65-f3f0-457a-9946-ec021622b061`).

### Step 2: Create a Messaging Profile with AI

1. Navigate to [Messaging](https://portal.telnyx.com/#/app/messaging) in the portal.
2. Click **Add new profile** and name it (e.g., "RCS AI Profile").
3. In profile settings, find **AI Assistant** and select your assistant from the dropdown (or enter the Assistant ID).
4. Save and copy the Messaging Profile ID.

The Messaging Profile links your RCS Agent to an AI Assistant via the `ai_assistant_id` field.

### Step 3: Link your RCS Agent to the AI-enabled profile

If you already have an approved RCS Agent, update it to use your AI-enabled messaging profile:

```
curl -X PATCH https://api.telnyx.com/v2/rcs_agents/YOUR_RCS_AGENT_ID \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "profile_id": "your_ai_messaging_profile_id"
  }'
```

Alternatively, when submitting your RCS Agent for carrier approval, request that Telnyx provisions it on your existing AI Assistant messaging profile by contacting sales with your AI Assistant ID, Messaging Profile ID, and RCS Agent details. With a functional AI Assistant attached, your agent has real capabilities to demonstrate during carrier review, making approval easier.

### Step 4: Test your AI-powered RCS agent

Once your RCS Agent is approved (or using test numbers), send a message to trigger the AI:

```
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_rcs_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_ai_messaging_profile_id",
    "agent_message": {
      "content_message": {
        "text": "Hello! How can I help you today?"
      }
    }
  }'
```

When the customer replies, the AI Assistant automatically receives the inbound message via the messaging profile, processes it with your configured LLM and knowledge base, and sends an intelligent response back via RCS. No webhook code is required — the AI handles the conversation.

### Best practices

- **Keep responses mobile-friendly**: RCS messages display on mobile devices. Configure your AI to keep responses concise (under 160 characters when possible), use bullet points for lists, and avoid long paragraphs.
- **Set a greeting message**: Configure a greeting in your AI Assistant to welcome new customers, for example:

```
Welcome to [Company] Support! I'm here to help with questions about 
our products and services. What can I assist you with today?
```

- **Handle escalation gracefully**: Include instructions for when the AI should hand off to a human, for example when the customer asks to speak to a human, has a billing dispute, or is frustrated after 3 exchanges.
- **Test with real questions**: Before going live, test with questions your customers actually ask by checking support ticket history, reviewing FAQ page analytics, and testing edge cases.

### Monitoring and analytics

Track your AI Assistant's performance in the portal under **AI Assistants > Insights**:

- **Conversation logs**: Review AI responses and customer satisfaction
- **Knowledge gaps**: Identify questions the AI couldn't answer
- **Response times**: Monitor latency and throughput

### Pricing

| Component | Pricing |
| --- | --- |
| RCS messages | [See RCS pricing](https://telnyx.com/pricing/messaging) |
| AI Assistant | [See AI pricing](https://telnyx.com/pricing/conversational-ai) |

AI Assistant charges are based on tokens processed. Simple Q&A conversations typically cost fractions of a cent per exchange.
