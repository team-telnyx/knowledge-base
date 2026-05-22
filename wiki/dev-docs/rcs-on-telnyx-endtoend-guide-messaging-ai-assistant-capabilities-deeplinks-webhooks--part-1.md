---
title: 'RCS on Telnyx: end‑to‑end guide (Messaging, AI Assistant, Capabilities, Deeplinks,
  Webhooks)'
summary: Build and launch Rich Communication Services (RCS) on Telnyx—from agent approval
  and sending rich messages to device capability checks, deeplinks, webhooks, and
  optional AI Assistant integration for no-code conversational replies.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
  content_hash: 5039b349d6faabf9972f41a04d1de56f3ee2f8a40332c5ce6f10e905693b229b
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
  content_hash: 6db6e84317092f1b6b9a9fc31f5976c50c89e93786dd2245c8dc16e2dc438218
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
  content_hash: c10492c441f3e12d56c2f06d828dcd65644d5dd6bfe1af1c1cc25341481a80f1
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
  content_hash: 62edd2dc217194d6d4e74b1ea186a18d434c093300e1ec69d326c545c35e68d7
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
  content_hash: 1fac49cc3430f838929b09ed83ca4b7955432331a077f61706adc02b6d7d7041
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
  content_hash: bd80adb102952b25eba6c10c6e870272a0a62299a078d46f675b543dc89f7fae
updated_at: 2026-05-20T09:08:21Z
---

# RCS on Telnyx: end‑to‑end guide (Messaging, AI Assistant, Capabilities, Deeplinks, Webhooks)

*Part 1 of 2 — see also: [Part 2](rcs-on-telnyx-endtoend-guide-messaging-ai-assistant-capabilities-deeplinks-webhooks--part-2.md)*

Build and launch Rich Communication Services (RCS) on Telnyx—from agent approval and sending rich messages to device capability checks, deeplinks, webhooks, and optional AI Assistant integration for no-code conversational replies.

## Why RCS + AI Assistant
RCS delivers app‑like messaging in the native inbox (rich cards, carousels, suggested actions, read receipts). Pairing it with Telnyx AI Assistant lets you:
- Launch a functional agent fast for carrier onboarding (no custom webhook or LLM code)
- Handle conversation state and knowledge retrieval automatically
- Configure in minutes (instructions + knowledge sources) instead of weeks of development

## Approval and testing timeline
RCS requires agent registration and carrier approval:
- Submit your RCS Agent (brand, use case, sample content)
- Testing stage: invite beta test numbers and send via API while approval is pending
- Carrier approval typically takes 4–6 weeks
- Go live after approval (send to any RCS‑capable device)

You can test as soon as your agent is in testing stage—no need to wait for full approval. See [RCS Getting Started](rcs-getting-started.md).

## Key building blocks and routing
- RCS Agent: the branded sender approved by carriers
- Messaging Profile: routes messages and webhooks; links to an AI Assistant via ai_assistant_id
- AI Assistant (optional): instructions + knowledge sources; responds to inbound messages automatically when linked
- Webhook routing differences:
  - Inbound RCS messages (message.received): webhook URL from the RCS Agent
  - Outbound status (message.sent, message.finalized, message.read): per‑request URL, else messaging profile URL

See details in [Receiving RCS Webhooks](receiving-rcs-webhooks.md).

## Configure an AI‑powered RCS agent (portal + API)
1) Create an AI Assistant (Portal → AI Assistants):
- Add a name and persona instructions (e.g., concise, friendly, escalate when unsure)
- Connect knowledge sources (uploaded docs, websites, or API)
- Save and note the Assistant ID

2) Create a Messaging Profile and link the Assistant (Portal → Messaging):
- Add new profile and select your AI Assistant (or paste Assistant ID)
- Save and note the Messaging Profile ID

3) Link your RCS Agent to the AI‑enabled profile (after or during approval):
```bash
curl -X PATCH https://api.telnyx.com/v2/rcs_agents/YOUR_RCS_AGENT_ID \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "profile_id": "your_ai_messaging_profile_id"
  }'
```
If you’re mid‑onboarding, ask Telnyx to provision your agent on your AI‑enabled profile (share Assistant ID, Messaging Profile ID, and agent details).

4) Test the AI flow (no webhook code required for replies):
```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_rcs_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_ai_messaging_profile_id",
    "agent_message": {"content_message": {"text": "Hello! How can I help you today?"}}
  }'
```
When the customer replies, the AI Assistant receives the message via the messaging profile, consults your knowledge sources, and sends an intelligent response via RCS.

Best practices for AI on mobile: keep replies concise (~160 chars), use bullets over long paragraphs, greet first‑time users, and define clear human‑handoff rules.

## Send RCS messages (text, rich cards, carousels, suggestions)
- Text:
```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {"content_message": {"text": "Hi! How can we help you today?"}}
  }'
```
- Rich card (image + buttons). Media URLs must be public (e.g., JPEG/PNG/GIF):
```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {"content_message": {"rich_card": {"standalone_card": {
      "card_orientation": "VERTICAL",
      "thumbnail_image_alignment": "LEFT",
      "card_content": {
        "title": "Order Shipped! ",
        "description": "Your order #12345 is on its way.",
        "media": {"height": "MEDIUM", "content_info": {"file_url": "https://example.com/shipping.jpg", "content_type": "image/jpeg"}},
        "suggestions": [
          {"action": {"text": "Track Order", "open_url_action": {"url": "https://example.com/track/12345"}}},
          {"reply": {"text": "Contact Support", "postback_data": "support_request"}}
        ]
      }
    }}}}
  }'
```
- Carousel (2–10 cards, same width across cards): see [Send RCS Messages](send-rcs-messages.md) for a full example.
- Suggested actions supported: quick replies, open URL (browser or webview), dial, view/share location, create calendar event, compose message.

For more patterns and parameters, see [Send RCS Messages](send-rcs-messages.md).

## SMS fallback and adaptive delivery
Not all recipients support RCS. Include a fallback to SMS:
```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {"content_message": {"text": "Your order shipped! Track: https://example.com/track/12345"}},
    "fallback": {"from": "+15551234567", "text": "Your order shipped! Track: https://example.com/track/12345"}
  }'
```
Notes:
- fallback.from must be a Telnyx SMS‑capable number on your messaging profile
- Fallback is plain text only (rich card content isn’t included)
- You can also decide between rich cards vs. text vs. SMS using capability checks (next section)

## Device capability checks (single, bulk) and features
Query if a number supports RCS and which features are available:
- Single number:
```bash
curl -s https://api.telnyx.com/v2/messaging/rcs/capabilities/{agent_id}/{phone_number} \
  -H "Authorization: Bearer YOUR_API_KEY"
```
- Bulk (up to 100 numbers):
```bash
curl -X POST https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities \
  -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"agent_id": "your_agent_id", "phone_numbers": ["+15551234567", "+15559876543"]}'
```
Typical outcomes:
- Full RCS support: features include RICHCARD_STANDALONE, RICHCARD_CAROUSEL, ACTION_OPEN_URL, ACTION_DIAL, etc.
- Generic RCS only: device supports RCS but feature granularity unknown—send basic text RCS, avoid rich cards
- No RCS: status indicates disabled/not provisioned—send SMS/MMS

Feature reference (subset):
| Feature | Use for |
| --- | --- |
| RICHCARD_STANDALONE | Single product/notice cards |
| RICHCARD_CAROUSEL | Multi‑card carousels |
| ACTION_OPEN_URL / IN_WEBVIEW | Link out or in‑app browsing |
| ACTION_DIAL | Click‑to‑call |
| ACTION_VIEW_LOCATION / SHARE_LOCATION | Maps and delivery |
| ACTION_CREATE_CALENDAR_EVENT | Appointment booking |
| ACTION_COMPOSE | Prefill a message |
| GENERIC_RCS_FEATURE | Text‑only RCS when details unknown |

Performance: capability queries can take several seconds—cache results and refresh periodically rather than querying before each send.

Adaptive sending strategy:
- If supports rich cards and you have media → send rich card with SMS fallback
- If RCS enabled but no rich card support → send RCS text with SMS fallback
- If RCS not enabled → send SMS directly

See patterns in [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md).
