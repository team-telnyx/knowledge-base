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

*Part 2 of 5 — see also: [Part 1](ai-insights--part-1.md), [Part 3](ai-insights--part-3.md), [Part 4](ai-insights--part-4.md), [Part 5](ai-insights--part-5.md)*

AI Insights let you analyze Telnyx AI Assistant conversations to extract summaries, scores, classifications, and structured data. You can build custom free-form or schema-based insights, organize them into reusable Insight Groups with webhook delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.

## Structured insights

Structured insights extract data in a predefined JSON schema, producing consistent, machine-readable results ideal for analytics, dashboards, and downstream processing.

### When to use structured insights

| Use case | Unstructured | Structured |
| --- | --- | --- |
| Open-ended summaries | ✅ | ❌ |
| Sentiment scoring (1-5) | ❌ | ✅ |
| Issue categorization | ❌ | ✅ |
| Descriptive analysis | ✅ | ❌ |
| Compliance flags | ❌ | ✅ |
| Dashboard metrics | ❌ | ✅ |

### Creating a structured insight

1. Navigate to [AI Insights](https://portal.telnyx.com/#/ai/insights) and click **Create Insight**.
2. Enter a name and basic instructions.
3. Click **Collect as structured data** to reveal the schema configuration interface.
4. For each field you want to extract, add a parameter with:
   - **Name** — the field name in the JSON output (e.g., `sentiment_score`, `issue_type`).
   - **Type** — the data type.
   - **Required** — whether the field must always be present.
   - **Description** — instructions for extracting this specific field.
5. Click **Add parameter** to add additional fields.

### Parameter types

- **string** — text values for categories, descriptions, identifiers.
- **enum** — predefined categories; the AI selects one value from your list. Provides better accuracy and strict validation than listing options in a string description.
- **number** — numeric values for scores, ratings, counts, percentages.
- **integer** — whole numbers without decimals (counts, quantities, IDs).
- **boolean** — true/false flags for presence checks or yes/no decisions.
- **array** — generic lists of values.
- **array (string / number / boolean)** — typed lists with enforced element types for better type safety.
- **object** — nested structures for complex related data.

### Example: sentiment analysis

```
Name: Customer Sentiment Analysis
Instructions: Analyze the customer's emotional state throughout the conversation.

Parameters:
1. positivity_score — number, required. Rate positive sentiment from 1-5 (1=very negative, 5=very positive).
2. frustration_level — number, required. Rate customer frustration from 1-5 (1=not frustrated, 5=very frustrated).
3. overall_sentiment — string, required. Overall sentiment classification: "positive", "neutral", or "negative".
4. key_emotions — array, optional. List of specific emotions detected (e.g., "happy", "confused", "angry", "satisfied").
```

Sample output:

```json
{
  "positivity_score": 4,
  "frustration_level": 2,
  "overall_sentiment": "positive",
  "key_emotions": ["satisfied", "relieved", "appreciative"]
}
```

### Example: sales qualification

```
Name: Lead Qualification
Instructions: Assess the sales opportunity from this conversation.

Parameters:
1. budget_mentioned — boolean, required. Did the prospect mention or discuss budget?
2. budget_range — string, optional. If mentioned, what budget range? (e.g., "under $1000", "$1000-$5000", "over $5000").
3. decision_timeframe — string, required. When do they need to make a decision? ("immediate", "this_month", "this_quarter", "exploring", "unknown").
4. pain_points — array, required. List of specific problems or needs mentioned.
5. competitor_mentions — array, optional. Names of competing solutions mentioned.
6. lead_score — number, required. Qualification score from 1-10 based on buying signals.
```

### Example: support ticket categorization

```
Name: Support Ticket Classification
Instructions: Categorize and triage the support request.

Parameters:
1. issue_type — string, required. Primary issue type: "technical", "billing", "account", "feature_request", "bug_report".
2. priority — string, required. Urgency level: "critical", "high", "medium", "low".
3. affected_service — string, optional. Which product/service is affected?
4. resolved — boolean, required. Was the issue resolved during this conversation?
5. resolution_time_minutes — number, optional. If resolved, how many minutes did it take?
6. follow_up_needed — boolean, required. Does this require follow-up action?
7. tags — array, optional. Relevant tags for categorization (e.g., "password_reset", "billing_dispute", "api_error").
```

### Advanced mode

Enable **Advanced mode** at the top of the structured data section to access additional schema configuration options:

- Custom validation rules.
- Enum constraints for string values.
- Min/max constraints for numbers.
- Pattern matching for strings.
- Nested object definitions.
