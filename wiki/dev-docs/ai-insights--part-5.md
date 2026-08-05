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

*Part 5 of 5 — see also: [Part 1](ai-insights--part-1.md), [Part 2](ai-insights--part-2.md), [Part 3](ai-insights--part-3.md), [Part 4](ai-insights--part-4.md)*

AI Insights let you analyze Telnyx AI Assistant conversations to extract summaries, scores, classifications, and structured data. You can build custom free-form or schema-based insights, organize them into reusable Insight Groups with webhook delivery, and use Telnyx-managed insights for out-of-the-box quality measurement.

## Troubleshooting

### Insights not appearing

- Is the group assigned to the assistant?
- Did a conversation complete after assignment?
- Are the individual insights configured correctly?

### Webhook not receiving data

- Is the webhook URL correct and accessible?
- Is the endpoint returning 200 OK status?
- Check webhook logs in your application.

### Wrong insights in group

1. Edit the group.
2. Remove incorrect insights.
3. Add correct insights.
4. Save changes. Changes apply to future conversations immediately.

### Telnyx-managed chart shows "No insight data recorded"

- Confirm the Insight Group includes Agent Instruction Following or User Satisfaction.
- Confirm the group is assigned to the assistant in the Analysis tab.
- Confirm the assistant has had conversations in the last 7 days.
- Confirm conversations completed successfully — insights run after the conversation ends.

### Telnyx-managed scores seem inconsistent

Telnyx-managed insights use AI evaluation, which considers the full conversation context. Scores can vary based on conversation length, topic complexity, and user behavior. Look at trends over multiple days rather than individual conversations.

### Version comparison shows "Unknown version"

Conversations that occurred before version tracking was enabled (or that lack version metadata) are grouped as "Unknown version." Ensure your assistant has published versions and that conversations are attributed correctly.

## Related resources

- [Insight Groups](insight-groups.md) — organize insights and configure webhooks.
- [Structured Insights](structured-insights.md) — define JSON schemas for consistent data extraction.
- [Telnyx-Managed Insights](telnyx-managed-insights.md) — built-in quality metrics.
- [Dynamic Variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables) — custom variables for your insights.
- [Memory](https://developers.telnyx.com/docs/inference/ai-assistants/memory) — using insight IDs in memory queries.
- [Voice Assistant Configuration](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant#insights) — assigning insights to assistants.
- [Use Cases](https://developers.telnyx.com/docs/inference/ai-insights/use-cases) — industry-specific insight examples.
- [API Reference](/api-reference/assistants/list-assistants) — programmatic group management.
