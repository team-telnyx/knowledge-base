---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/data-residency
- url: https://developers.telnyx.com/docs/inference/embeddings
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started/index
updated_at: 2026-06-11T10:33:19Z
---

# Telnyx Inference

*Part 3 of 6 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md), [Part 6](telnyx-inference--part-6.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## Insight Groups

An Insight Group is a named collection of insights with optional webhook configuration. Groups provide a modular, reusable approach to conversation analysis.

### Key Features

- **Reusable** — assign the same group to multiple assistants.
- **Modular** — mix and match insights across different groups.
- **Flexible Delivery** — configure unique webhook URLs per group.
- **Organized** — group insights by use case, department, or business function.

### Creating an Insight Group

1. Navigate to **AI Insights** and click the **AI Insight Groups** tab.
2. Click **Create Insight Group**.
3. Fill in:
   - **Name** (required) — a descriptive name indicating the group's purpose (e.g., "Customer Service Analytics").
   - **Webhook URL** (optional) — the HTTPS endpoint where insight results will be sent after each conversation (e.g., `https://api.mycompany.com/webhooks/insights`).
   - **Insights** (multi-select) — choose which insights to include. You can add multiple insights, use the same insight in multiple groups, and modify membership after creation.
4. Click **Save**.

### Assigning Groups to Assistants

**Via the Portal:** When creating or editing an AI Assistant, go to the **Analysis** tab, select **Insights**, choose an Insight Group, and save.

**Via the API:** Use the `insight_settings` field:

```bash
curl -X POST https://api.telnyx.com/v2/ai/assistants \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer Support Assistant",
    "model": "moonshotai/Kimi-K2.5",
    "instructions": "You are a helpful support assistant...",
    "insight_settings": {
      "insight_group_id": "a2708926-c060-480a-8631-041cb7304117"
    }
  }'
```

### Webhook Delivery

Set a webhook URL at the group level when creating or editing the group. Override it per assistant: navigate to the assistant's **Analysis** > **Insights** tab, select the group, click **Edit selected**, and enter a different webhook URL.

When a conversation completes, a webhook is sent:

```json
{
  "event_type": "conversation.insights.completed",
  "conversation_id": "conv_abc123",
  "insight_group_id": "a2708926-c060-480a-8631-041cb7304117",
  "insight_group_name": "Customer Support Analytics",
  "insights": [
    {
      "insight_id": "insight_xyz789",
      "insight_name": "Customer Sentiment",
      "result": { "score": 8, "sentiment": "positive" }
    },
    {
      "insight_id": "insight_abc456",
      "insight_name": "Issue Type",
      "result": { "category": "technical", "priority": "high" }
    }
  ]
}
```

### Using Insights from Groups

- **Conversation History**: Navigate to an assistant's **Conversation History** under the **Analysis** tab, click a conversation, and scroll to the **Insights** section.
- **Memory API**: Filter insights using the `insight_query` parameter (e.g., `insight_ids=insight_abc,insight_def,insight_xyz`).

### Organization Strategies

- **By use case** — group by business function (Sales Qualification, Customer Support, Compliance Monitoring, Quality Assurance).
- **By delivery destination** — group by webhook endpoint (CRM Integration, Analytics Dashboard, Ticket System).
- **By analysis type** — group by the kind of analysis (Quantitative Metrics, Categorical Classification, Qualitative Analysis).
- **Hybrid approach** — combine strategies (e.g., "Sales - Quantitative", "Support - Urgent").

### Insight Group Best Practices

1. **Start small** — begin with 2-4 related insights; avoid 15+.
2. **Test without webhooks first** — leave webhook URL empty, review results in the portal, then add webhook once validated.
3. **Use descriptive names** — make the group's purpose immediately clear.
4. **Document webhook endpoints** — maintain documentation of what each webhook expects, who owns it, and how to troubleshoot.
5. **Version your groups** — create a new group for significant changes, test with a subset of assistants, migrate fully, then retire the old group.
6. **Monitor insights count** — 1-5 insights: focused and fast; 5-10: comprehensive and efficient; 10+: consider splitting.
