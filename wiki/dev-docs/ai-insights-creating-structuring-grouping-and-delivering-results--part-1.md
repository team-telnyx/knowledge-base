---
title: 'AI Insights: Creating, Structuring, Grouping, and Delivering Results'
summary: A consolidated guide to building AI Insights in the Telnyx Mission Control
  Portal—from writing effective instructions and using variables, to collecting structured
  JSON, organizing with Insight Groups, configuring webhooks, consuming results, and
  applying best practices and industry patterns.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
  content_hash: 3b1c5ceaaae31f556a10080f4a8011bef1f28a56e14773207da81a2c36c7e535
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: faf7aa81b48b0b3f75d083453eab8fc8436d97733f61a4eeda2a35d8740d12c6
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 9535f3261b50eba991879efe40251ef848b5813f54534f7a4e706f0ce0a5a256
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 871874b88b14fe31dd5288d8d9619d2375add7c402b89982a308b5884ae14093
updated_at: 2026-05-20T08:32:23Z
---

# AI Insights: Creating, Structuring, Grouping, and Delivering Results

*Part 1 of 2 — see also: [Part 2](ai-insights-creating-structuring-grouping-and-delivering-results--part-2.md)*

A consolidated guide to building AI Insights in the Telnyx Mission Control Portal—from writing effective instructions and using variables, to collecting structured JSON, organizing with Insight Groups, configuring webhooks, consuming results, and applying best practices and industry patterns.

## What are AI Insights?
AI Insights analyze assistant conversations (voice calls, web calls, SMS chats) and return either free-form text or structured JSON you define. They help summarize, score, classify, and extract information for downstream systems. Insights can be reused across assistants, grouped for organization, and delivered automatically via webhooks.

## Prerequisites and access
- Mission Control Portal access.
- At least one AI Assistant configured (recommended for testing).
- Portal path: AI, Storage and Compute → AI Insights (or open directly via the Portal).

## Create an insight
1. In the Portal, go to AI Insights and click Create Insight.
2. Configure:
   - Name (required): e.g., “Conversation Summary”, “Customer Sentiment”, “Issue Classification”.
   - Instructions: what to analyze, how to extract it, and the desired output format.
3. Save the insight; it will appear in the list with its ID, name, and creation date.

## Write effective instructions
Be specific, define an output format, and provide context. Examples:

Conversation summary
```
Summarize the conversation for use as future context. Include:
- Key facts mentioned.
- Decisions made.
- User preferences expressed.
- Action items or follow-ups needed.

Keep the summary concise (2-3 sentences) and focus on information that would be useful in future conversations with this user.
```

Sentiment analysis
```
Measure the positivity & negativity of the call and rate it from 1-5 in ascending order.

Positivity: How positive, satisfied, or happy was the customer? (1=very negative, 5=very positive)
Negativity: How frustrated, angry, or dissatisfied was the customer? (1=no negativity, 5=very negative)

Provide your ratings and a brief explanation of why you assigned those scores.
```

Issue categorization
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

## Use variables in instructions
Add dynamic context with variables in your instructions.
- System variables:
  - {{telnyx_current_time}} – Date/time of the conversation.
  - {{telnyx_conversation_channel}} – Channel (phone_call, web_call, sms_chat).
  - {{telnyx_agent_target}} – Assistant’s phone/identifier.
  - {{telnyx_end_user_target}} – User’s phone/identifier.
- You can also reference custom variables configured for your assistant. See [Dynamic Variables](dynamic-variables.md).

Example
```
Analyze this {{telnyx_conversation_channel}} conversation from {{telnyx_current_time}}.

Identify if the user at {{telnyx_end_user_target}} expressed interest in any of our products or services.
If so, list the products mentioned and their level of interest (high/medium/low).
```

## Save and manage insights
- Edit: Click the pencil icon on an insight row to update name/instructions, then Save.
- Copy ID: Use the copy icon next to the insight ID (e.g., cfcc865c-d3d4-4823-8a4b-f0df57d9f56f) for APIs and memory queries.

## Structured insights (JSON schemas)
Use structured insights when you need consistent, machine-readable results (metrics, categories, booleans, dashboards). To enable:
1. Create an insight and enter basic instructions.
2. Click Collect as structured data to open schema configuration.
3. Add parameters with Name, Type, Required, and Description. Add as many fields as needed.

When to use structured insights
- Quantitative metrics (scores, counts, percentages).
- Categorical data (types, priorities, statuses).
- Boolean flags (yes/no decisions).
- Consistent format for databases/analytics.
- Multiple related fields in one result.

See also [Structured insights](structured-insights.md).

## Parameter types at a glance
- String: text values (e.g., issue_category).
- Enum: predefined categories; AI selects one from your list (better accuracy than free text for categories).
- Number: numeric values (scores, percentages).
- Integer: whole numbers (counts, IDs).
- Boolean: true/false flags.
- Array: list of values; prefer typed arrays below when possible.
- Array (string|number|boolean): lists with enforced element types.
- Object: nested structures for related fields.

Examples
```
# String
Name: issue_category
Type: string
Description: One of: "billing", "technical", "account", "general"

# Enum
Name: sentiment
Type: enum
Enum Values: positive, negative, neutral, mixed
Description: Overall sentiment

# Number
Name: satisfaction_score
Type: number
Description: Customer satisfaction 1-10

# Integer
Name: message_count
Type: integer
Description: Total customer messages

# Boolean
Name: escalation_needed
Type: boolean
Description: Requires supervisor escalation

# Array (string)
Name: issue_keywords
Type: array (string)
Description: Key terms describing the issue

# Object
Name: customer_info
Type: object
Description: Name, account number, preferred contact
```

## Advanced schema options
Enable Advanced mode to add:
- Enum constraints for strings.
- Min/max for numbers.
- Pattern matching for strings.
- Nested object definitions.
- Custom validation rules.

## Organize insights with Insight Groups
Insight Groups are named collections of insights with optional webhook delivery. They’re reusable across assistants and modular by use case.

Create a group
1. In AI Insights, open the AI Insight Groups tab and click Create Insight Group.
2. Configure:
   - Name (required): use clear, business-oriented names.
   - Webhook URL (optional): https endpoint to receive results.
   - Insights: multi-select the insights to include (you can reuse insights across groups).
3. Save; the group appears with ID, name, webhook URL, insights count, and created date.

Examples
```
Customer Support Analytics → Sentiment, Issue Classification, Resolution Status, Follow-up Required
Sales Lead Qualification → Budget Discussion, Decision Timeframe, Pain Points, Competitor Mentions, Lead Score
Healthcare Compliance → HIPAA Compliance Check, Required Disclosures, Consent Verification, Patient Information Handled
Call Quality Metrics (no webhook) → Agent Performance, Script Adherence, Professional Tone, Resolution Quality
```

Manage groups
- Edit name/webhook/insights; changes affect all assigned assistants.
- Copy group ID (e.g., a2708926-c060-480a-8631-041cb7304117) for APIs.

See [Insight Groups](insight-groups.md).

## Configure webhook delivery
- Via groups: Set a Webhook URL on the group; all assistants using the group will deliver to this endpoint unless overridden.
- Per-assistant override: In an assistant’s Analysis → Insights, select the group, click Edit selected, and set a different Webhook URL for that assistant.

Example event payload
```
{
  "event_type": "conversation.insights.completed",
  "conversation_id": "conv_abc123",
  "insight_group_id": "a2708926-c060-480a-8631-041cb7304117",
  "insight_group_name": "Customer Support Analytics",
  "insights": [
    { "insight_id": "insight_xyz789", "insight_name": "Customer Sentiment", "result": { "score": 8, "sentiment": "positive" } },
    { "insight_id": "insight_abc456", "insight_name": "Issue Type", "result": { "category": "technical", "priority": "high" } }
  ]
}
```

## Assign groups to assistants
- Portal: In the assistant editor, go to Analysis → Insights and select an Insight Group.
- API: Use insight_settings when creating/updating an assistant.
```
curl -X POST https://api.telnyx.com/v2/ai/assistants \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer Support Assistant",
    "model": "moonshotai/Kimi-K2.5",
    "instructions": "You are a helpful support assistant...",
    "insight_settings": { "insight_group_id": "a2708926-c060-480a-8631-041cb7304117" }
  }'
```
