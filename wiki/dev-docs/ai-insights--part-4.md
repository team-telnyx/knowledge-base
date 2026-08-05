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

*Part 4 of 5 — see also: [Part 1](ai-insights--part-1.md), [Part 2](ai-insights--part-2.md), [Part 3](ai-insights--part-3.md), [Part 5](ai-insights--part-5.md)*

AI Insights let you analyze Telnyx AI Assistant conversations to extract summaries, scores, classifications, and structured data. You can build custom free-form or schema-based insights, organize them into reusable Insight Groups with webhook delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.

## Telnyx-managed insights

Telnyx-managed insights are built-in quality metrics maintained by Telnyx. They use consistent scoring rubrics, are available to every account, and require no prompt engineering or schema design — just add them to an Insight Group and assign the group to an assistant.

### Available insights

**Agent Instruction Following** — measures how well the assistant followed its system prompt and tool-use instructions.

| Score | Meaning |
| --- | --- |
| Excellent | Followed all instructions precisely |
| Good | Followed instructions with minor deviations |
| Fair | Missed one or more instructions but stayed on task |
| Poor | Significantly deviated from instructions |
| N/A | Could not be evaluated for this conversation |

Use this when prompt adherence matters — complex assistants with many tool instructions, compliance-sensitive flows, or when debugging unexpected behavior.

**User Satisfaction** — estimates how satisfied the caller was based on their responses, tone, and engagement signals.

| Score | Meaning |
| --- | --- |
| Excellent | User was clearly satisfied and engaged |
| Good | User was generally satisfied |
| Fair | User was neutral or mixed |
| Poor | User was frustrated or dissatisfied |
| N/A | Could not be evaluated for this conversation |

Use this for customer support, sales calls, and any voice flow where caller experience directly impacts business outcomes.

The set of Telnyx-managed insights may grow over time. Check the Insight Group configuration in the Portal for the current list.

### Enabling Telnyx-managed insights

1. Navigate to [AI Insights](https://portal.telnyx.com/#/ai/insights) and open the **AI Insight Groups** tab.
2. Create a new group or edit an existing one.
3. In the insights dropdown, search for **Agent Instruction Following** and **User Satisfaction** and add whichever you need.
4. Save the group.
5. Open your assistant in the [Portal](https://portal.telnyx.com/#/ai/assistants), go to **Analysis** → **Insights**, select the group, and save.
6. Insights run automatically after each conversation completes.

### Viewing results

**Per conversation:**

1. Open your assistant → **Analysis** → **Conversation History**.
2. Click any conversation and scroll to the **Insights** section to see the scores for each insight in the group.

**Over time (7-day trend):**

The **Insights Over Time** sub-tab shows a stacked-bar chart of daily score counts for the last 7 days, scoped to the current assistant.

- One bar per day (UTC) for the last 7 days.
- Each bar is segmented by score value, color-coded: **Poor** (red), **Fair** (amber), **Good** (green), **Excellent** (blue), **N/A** (gray).
- Bars are stacked bottom-to-top with N/A pinned to the bottom and Poor through Excellent ascending, so the best results sit on top.
- Use the **Insight** dropdown to select which Telnyx-managed insight to view (only Telnyx-managed insights appear here).

**Comparing assistant versions:**

Toggle **Compare by assistant version** above the chart to split the data into separate charts — one per assistant version. Version comparison uses `metadata.assistant_version_id` to attribute conversations to versions; conversations without a version ID are grouped as "Unknown version".

### Tips for getting value from Telnyx-managed insights

- **Spot regressions after a change** — after updating your assistant's prompt, tools, or voice settings, watch the over-time chart for the next few days. If "Poor" or "Fair" segments grow while "Good" or "Excellent" shrink, the change may have hurt quality.
- **Correlate with volume** — taller bars mean more conversations. A spike in volume can amplify small score shifts; check raw counts in the chart tooltip before drawing conclusions.
- **Understand N/A rates** — a large gray segment means the insight frequently couldn't be evaluated. For Agent Instruction Following, this may indicate conversations that were too short or didn't trigger tool use. For User Satisfaction, it may mean the conversation lacked enough user signal (e.g., one-sided calls).
- **Use scores alongside conversation history** — the over-time chart tells you *when* quality shifted; the conversation history tells you *why*. When you see a dip, switch to Conversation History, filter to that day, and review individual conversations.

## Managing individual insights

- **Editing** — click the edit icon (pencil) on an insight row to modify its name or instructions, then click **Save**.
- **Copying the insight ID** — click the copy icon next to the insight ID. Example ID format: `cfcc865c-d3d4-4823-8a4b-f0df57d9f56f`. Use this ID with the Memory API or for programmatic access.

## Configuring webhook delivery

### Via Insight Groups

Set a webhook URL when creating or editing an Insight Group:

1. Navigate to [AI Insight Groups](https://portal.telnyx.com/#/ai/insights-groups).
2. Click **Create Insight Group** or edit an existing group.
3. Enter your webhook URL in the **Webhook URL** field (e.g., `https://api.mycompany.com/webhooks/ai-insights`).
4. Save the group.

All assistants using this group will send insights to this URL unless overridden.

### Per-assistant override

Override the group's webhook URL for a specific assistant:

1. Navigate to your AI Assistant configuration.
2. Go to the **Analysis** tab → **Insights** sub-tab.
3. Select an Insight Group.
4. Click **Edit selected** to modify the group settings.
5. Enter a different webhook URL for this assistant.
6. Save the assistant configuration.

This is useful when different assistants need insights delivered to different systems or for testing with staging webhooks.

## Best practices

### Writing clear instructions

1. **Be specific** — clearly state what to extract.
   - ❌ "Analyze the call".
   - ✅ "Identify the customer's main complaint and rate the urgency from 1-5".
2. **Define output format** — specify how the response should be structured.
   - ❌ "Tell me about sentiment".
   - ✅ "Rate sentiment from 1-10 and provide a one-sentence explanation".
3. **Provide context** — explain why the information matters.
   - ❌ "List products mentioned".
   - ✅ "List products the customer showed interest in purchasing, noting their budget concerns".
4. **Use examples** — show the format you expect.

### Testing your insights

1. Start with test conversations.
2. Review results and check if the extracted information matches your expectations.
3. Refine instructions based on the results.
4. Validate accuracy across different conversation types.

### Naming conventions

Use clear, descriptive names that indicate:

- **What** is being analyzed: "Customer Sentiment", "Product Interest", "Issue Type".
- **Why** it matters: "Escalation Needed", "Follow-up Required", "Compliance Check".
- **Scope**: "Healthcare Compliance", "Sales Qualification", "Support Quality".

### Structured insight best practices

1. **Keep schemas focused** — don't try to extract everything in one insight; create multiple focused insights instead.
2. **Make instructions clear** — each parameter's description should be unambiguous, including any value ranges.
3. **Use enums for categories** — when you have a fixed set of categories, use the **enum** type instead of listing values in a string description for better accuracy and strict validation.
4. **Mark optional appropriately** — only mark fields as required if they should always be extractable.
5. **Provide value ranges** — for numeric fields, specify the range (e.g., "Urgency score from 1-5, where 1 is low priority and 5 is critical/urgent").
6. **Test with edge cases** — very short conversations, missing information, ambiguous discussions, and multiple topics in one conversation.
