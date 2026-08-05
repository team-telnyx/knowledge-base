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

*Part 3 of 5 — see also: [Part 1](ai-insights--part-1.md), [Part 2](ai-insights--part-2.md), [Part 4](ai-insights--part-4.md), [Part 5](ai-insights--part-5.md)*

AI Insights let you analyze Telnyx AI Assistant conversations to extract summaries, scores, classifications, and structured data. You can build custom free-form or schema-based insights, organize them into reusable Insight Groups with webhook delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.

## Insight Groups

An **Insight Group** is a named collection of insights with optional webhook configuration. Groups are reusable across assistants, modular (insights can be mixed and matched), and flexible (each group can have its own webhook URL).

### Accessing Insight Groups

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **AI, Storage and Compute** > **AI Insights**.
3. Click the **AI Insight Groups** tab.

The page displays each group's ID, name, webhook URL, insights count, and creation date.

### Creating an Insight Group

1. Click **Create Insight Group**.
2. Configure the group:
   - **Name** (required) — a descriptive, business-oriented name such as "Customer Service Analytics", "Sales Qualification Metrics", or "Healthcare Compliance Checks".
   - **Webhook URL** (optional) — the HTTPS endpoint where insight results will be sent after each conversation (e.g., `https://your-domain.com/webhooks/insights`). Skip this if you only need to view insights in the Portal or fetch them via the API.
   - **Insights** (multi-select) — choose which insights to include. The same insight can belong to multiple groups.
3. Click **Save**.

### Example configurations

**Customer support group**

```
Name: Customer Support Analytics
Webhook URL: https://api.mycompany.com/webhooks/support-insights
Insights:
  - Customer Sentiment Analysis
  - Issue Classification
  - Resolution Status
  - Follow-up Required
```

**Sales qualification group**

```
Name: Sales Lead Qualification
Webhook URL: https://crm.mycompany.com/webhooks/lead-insights
Insights:
  - Budget Discussion
  - Decision Timeframe
  - Pain Points Identified
  - Competitor Mentions
  - Lead Score
```

**Compliance monitoring group**

```
Name: Healthcare Compliance
Webhook URL: https://compliance.healthcorp.com/insights
Insights:
  - HIPAA Compliance Check
  - Required Disclosures Made
  - Consent Verification
  - Patient Information Handled
```

**Quality assurance group**

```
Name: Call Quality Metrics
Webhook URL: -
Insights:
  - Agent Performance
  - Script Adherence
  - Professional Tone
  - Issue Resolution Quality
```

### Managing Insight Groups

- **Editing** — click the edit icon (pencil) on a group row to modify its name, webhook URL, or insights. Changes apply to all assistants using the group.
- **Copying the group ID** — click the copy icon next to the group ID. Example ID format: `a2708926-c060-480a-8631-041cb7304117`.

### Assigning groups to assistants

**Via the Portal:**

1. Open or create an AI Assistant.
2. Go to the **Analysis** tab → **Insights** sub-tab.
3. Select an Insight Group from the dropdown.
4. Save the assistant configuration.

**Via the API:**

```
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

### Using insights from groups

**In conversation history:**

1. Navigate to **AI Assistants** and select an assistant.
2. Go to **Analysis** → **Conversation History**.
3. Click a conversation and scroll to the **Insights** section.

**With the Memory API:**

```json
{
  "memory": {
    "conversation_query": "metadata->user_id=eq.123&limit=5",
    "insight_query": "insight_ids=insight_abc,insight_def,insight_xyz"
  }
}
```

Get insight IDs from your group by viewing the group details in the Portal and copying each insight's ID.

**Via webhooks:**

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

### Organization strategies

- **By use case** — "Sales Qualification", "Customer Support", "Compliance Monitoring", "Quality Assurance". Provides clear ownership and focused analytics.
- **By delivery destination** — group insights by webhook endpoint (e.g., "CRM Integration Group" → `https://crm.company.com/insights`). Simplifies webhook management.
- **By analysis type** — "Quantitative Metrics", "Categorical Classification", "Qualitative Analysis". Yields consistent data structures for downstream processing.
- **Hybrid approach** — combine strategies for complex scenarios (e.g., "Sales - Quantitative", "Support - Urgent").

### Best practices for groups

1. **Start small** — begin with 2-4 related insights; you can add more later.
2. **Test without webhooks first** — leave the webhook URL empty initially, assign to a test assistant, review results in the Portal, then add a webhook once validated.
3. **Use descriptive names** — make the group's purpose immediately clear.
4. **Document webhook endpoints** — record what each URL expects, who owns it, and how to troubleshoot delivery.
5. **Version your groups** — create a new group (e.g., "Support Analytics v2"), test with a subset of assistants, migrate fully, then retire the old group.
6. **Monitor insights count** — 1-5 insights is focused and fast; 5-10 is comprehensive; 10+ may be slower and should be split.
