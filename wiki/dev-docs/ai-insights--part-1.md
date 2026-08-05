---
title: AI Insights
summary: AI Insights let you analyze Telnyx AI Assistant conversations to extract
  summaries, scores, classifications, and structured data. You can build custom free-form
  or schema-based insights, organize them into reusable Insight Groups with webhook
  delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/telnyx-managed-insights
updated_at: 2026-08-05T13:45:36Z
---

# AI Insights

*Part 1 of 5 — see also: [Part 2](ai-insights--part-2.md), [Part 3](ai-insights--part-3.md), [Part 4](ai-insights--part-4.md), [Part 5](ai-insights--part-5.md)*

AI Insights let you analyze Telnyx AI Assistant conversations to extract summaries, scores, classifications, and structured data. You can build custom free-form or schema-based insights, organize them into reusable Insight Groups with webhook delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.

## Overview

AI Insights analyze conversations handled by Telnyx AI Assistants and return either free-form text or structured JSON based on instructions you define. Insights are created in the Mission Control Portal, organized into reusable [Insight Groups](insight-groups.md), and assigned to one or more assistants. Results can be viewed per conversation, queried via the Memory API, or delivered automatically to a webhook.

In addition to custom insights, Telnyx provides **Telnyx-managed insights** — built-in, AI-evaluated quality metrics such as *Agent Instruction Following* and *User Satisfaction* that require no prompt engineering or schema design.

## Prerequisites

- Access to the Telnyx Mission Control Portal.
- At least one AI Assistant configured (recommended for testing).

## Accessing AI Insights

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **AI, Storage and Compute** > **AI Insights**.
3. You'll see a list of existing insights with their IDs, names, instructions, and creation dates.

## Creating a custom insight

Free-form insights return natural-language responses based on your instructions. To create one:

1. Click **Create Insight** in the top-right corner of the AI Insights page.
2. Configure the basic settings:
   - **Name** (required) — a descriptive identifier such as "Conversation Summary", "Customer Sentiment", or "Issue Classification".
   - **Instructions** — a detailed prompt describing what to analyze and extract. Be specific about the information you want, include output format expectations, and reference conversation elements (transcript, metadata, etc.).
3. (Optional) Add dynamic variables to inject context about the specific conversation. Click **Add a variable** to choose from:
   - `{{telnyx_current_time}}` — date and time of the conversation.
   - `{{telnyx_conversation_channel}}` — channel type (`phone_call`, `web_call`, `sms_chat`).
   - `{{telnyx_agent_target}}` — assistant's phone number or identifier.
   - `{{telnyx_end_user_target}}` — user's phone number or identifier.
   - Any [custom dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables) configured for your assistant.
4. Click **Save**. The insight appears in your insights list.

### Example instructions

**Conversation summary**

```
Summarize the conversation for use as future context. Include:
- Key facts mentioned.
- Decisions made.
- User preferences expressed.
- Action items or follow-ups needed.

Keep the summary concise (2-3 sentences) and focus on information that would be useful in future conversations with this user.
```

**Sentiment analysis**

```
Measure the positivity & negativity of the call and rate it from 1-5 in ascending order.

Positivity: How positive, satisfied, or happy was the customer? (1=very negative, 5=very positive)
Negativity: How frustrated, angry, or dissatisfied was the customer? (1=no negativity, 5=very negative)

Provide your ratings and a brief explanation of why you assigned those scores.
```

**Issue categorization**

```
Analyze the conversation and identify the primary issue or request. Categorize it into one of the following:
- Technical Support.
- Billing Question.
- Feature Request.
- General Inquiry.
- Complaint.
- Other.

Also provide a brief description of the specific issue within that category.
```

**Using variables**

```
Analyze this {{telnyx_conversation_channel}} conversation from {{telnyx_current_time}}.

Identify if the user at {{telnyx_end_user_target}} expressed interest in any of our products or services.
If so, list the products mentioned and their level of interest (high/medium/low).
```
