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

*Part 2 of 6 — see also: [Part 1](telnyx-inference--part-1.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md), [Part 6](telnyx-inference--part-6.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## Clusters & Theme Identification

Clustering analyzes how your embedded data groups together, revealing common themes and niche subtopics. For example, clustering the novel *The Great Gatsby* reveals broad themes (e.g., "Daisy's Past") with more specific subtopics within each.

### Compute Clusters

Once your documents are embedded in a storage bucket, compute clusters via API:

```bash
curl --request POST \
  --url https://api.telnyx.com/v2/ai/clusters \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "bucket": "cluster-gatsby",
    "min_cluster_size": 50,
    "min_subcluster_size": 10
  }'
```

The response returns a `task_id`. The `min_cluster_size` and `min_subcluster_size` parameters control granularity:

- **Top-level clusters** identify broad themes. Choose `min_cluster_size` based on the minimum data points for a broad theme.
- **Sub-clusters** identify specific topics within a theme. Choose `min_subcluster_size` for minimum data points for a niche subtopic.

Raising `min_cluster_size` results in broader, more generic clusters. You can compute multiple clusterings on the same data with different parameters.

### Inspect Clusters

View cluster structure as JSON:

```bash
curl --request GET \
  --url "https://api.telnyx.com/v2/ai/clusters/{task_id}?show_subclusters=true" \
  --header "Authorization: Bearer $TELNYX_API_KEY"
```

Include `top_n_nodes` to see the most central data points per cluster. Download a graph image:

```bash
curl --request GET \
  --url "https://api.telnyx.com/v2/ai/clusters/{task_id}/graph" \
  --header "Authorization: Bearer $TELNYX_API_KEY" --output clusters.png
```

Pass `cluster_id` to drill into a specific cluster's subclusters.

## AI Insights

AI Insights analyze conversations (transcripts, metadata) and extract information based on instructions you define. You create individual insights, then organize them into groups assigned to AI Assistants.

### Prerequisites

- Access to the [Mission Control Portal](https://portal.telnyx.com)
- At least one AI Assistant configured (recommended for testing)

### Creating an Insight

1. Navigate to **AI, Storage and Compute** > **AI Insights** in the portal.
2. Click **Create Insight**.
3. Fill in a **Name** (required) and **Instructions** (the prompt describing what to analyze and extract).
4. Optionally add variables (see below).
5. Click **Save**.

#### Writing Effective Instructions

Good instructions are clear, specific, and actionable:

- ❌ "Analyze the call" → ✅ "Identify the customer's main complaint and rate the urgency from 1-5"
- ❌ "Tell me about sentiment" → ✅ "Rate sentiment from 1-10 and provide a one-sentence explanation"
- ❌ "List products mentioned" → ✅ "List products the customer showed interest in purchasing, noting their budget concerns"

Use naming conventions that indicate **what** is being analyzed ("Customer Sentiment"), **why** it matters ("Escalation Needed"), and **scope** ("Healthcare Compliance").

#### System Variables

Include dynamic variables in instructions to provide conversation context:

| Variable | Description |
|---|---|
| `{{telnyx_current_time}}` | Date and time of the conversation |
| `{{telnyx_conversation_channel}}` | Channel type (`phone_call`, `web_call`, `sms_chat`) |
| `{{telnyx_agent_target}}` | Assistant's phone number or identifier |
| `{{telnyx_end_user_target}}` | User's phone number or identifier |

You can also reference [custom dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables) configured for your assistant.

Example with variables:

```
Analyze this {{telnyx_conversation_channel}} conversation from {{telnyx_current_time}}.
Identify if the user at {{telnyx_end_user_target}} expressed interest in any of our products or services.
```

#### Managing Insights

- **Edit**: Click the pencil icon on the insight row.
- **Copy ID**: Click the copy icon next to the insight ID (format: `cfcc865c-d3d4-4823-8a4b-f0df57d9f56f`). Use this ID with the Memory API or for programmatic access.

## Structured Insights

Structured insights extract data in a predefined JSON schema format, providing consistent, machine-readable results. Use structured insights when you need quantitative metrics, categorical data, boolean flags, consistent format for dashboards/databases, or multiple related fields.

| Use Case | Unstructured | Structured |
|---|---|---|
| Open-ended summaries | ✅ | ❌ |
| Sentiment scoring (1-5) | ❌ | ✅ |
| Issue categorization | ❌ | ✅ |
| Descriptive analysis | ✅ | ❌ |
| Compliance flags | ❌ | ✅ |
| Dashboard metrics | ❌ | ✅ |

### Creating a Structured Insight

1. Navigate to **AI Insights** and click **Create Insight**.
2. Enter a name and basic instructions.
3. Click **Collect as structured data** to reveal the schema configuration.
4. For each data field, click **Add parameter** and define:
   - **Name** — the field name in the JSON output
   - **Type** — the data type
   - **Required** — whether the field must always be present
   - **Description** — instructions for extracting this field
5. Click **Save**.

### Parameter Types

| Type | Use For | Example Output |
|---|---|---|
| `string` | Categories, descriptions, identifiers | `{"issue_category": "technical"}` |
| `enum` | Predefined categories (strict value validation) | `{"sentiment": "positive"}` |
| `number` | Scores, ratings, counts, percentages | `{"satisfaction_score": 8}` |
| `integer` | Whole numbers (counts, quantities, IDs) | `{"message_count": 5}` |
| `boolean` | True/false flags, presence checks | `{"escalation_needed": false}` |
| `array` | Lists of values | `{"products_mentioned": ["Widget Pro"]}` |
| `array (string)` | Typed list of text values | `{"issue_keywords": ["billing", "refund"]}` |
| `array (number)` | Typed list of numeric values | `{"mentioned_prices": [29.99, 49.99]}` |
| `array (boolean)` | Typed list of true/false flags | `{"feature_preferences": [true, false, true]}` |
| `object` | Nested structures | `{"customer_info": {"name": "Jane Smith"}}` |

Use `enum` instead of listing valid values in a string description — it provides better accuracy and enforces strict value validation. Use `integer` instead of `number` when you specifically need whole numbers. Typed arrays (`array (string)`, `array (number)`, `array (boolean)`) provide better type safety than the generic `array` type.

### Advanced Mode

Enable **Advanced mode** (checkbox at the top of the structured data section) for additional schema options: custom validation rules, enum constraints for string values, min/max constraints for numbers, pattern matching for strings, and nested object definitions.

### Structured Insight Best Practices

1. **Keep schemas focused** — create multiple focused insights rather than one massive insight capturing everything.
2. **Make instructions clear** — each parameter description should specify the exact range and meaning (e.g., "Rate from 1-10, where 1 is very negative, 5 is neutral, and 10 is very positive").
3. **Use enums for categories** — prefer the `enum` type over listing values in a string description.
4. **Mark optional appropriately** — only mark fields as required if they should always be extractable.
5. **Provide value ranges** — for numeric fields, specify the range in the description.
6. **Test with edge cases** — very short conversations, missing information, ambiguous discussions, multiple topics.
