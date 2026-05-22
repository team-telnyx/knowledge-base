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

*Part 2 of 2 — see also: [Part 1](ai-insights-creating-structuring-grouping-and-delivering-results--part-1.md)*

A consolidated guide to building AI Insights in the Telnyx Mission Control Portal—from writing effective instructions and using variables, to collecting structured JSON, organizing with Insight Groups, configuring webhooks, consuming results, and applying best practices and industry patterns.

## Consume insight results
- Conversation history: Open AI Assistants → Conversation History → Insights to view results.
- Memory API: Filter by conversations and insight IDs.
```
{
  "memory": {
    "conversation_query": "metadata->user_id=eq.123&limit=5",
    "insight_query": "insight_ids=insight_abc,insight_def,insight_xyz"
  }
}
```
Get insight IDs from your group details. Learn more in [Memory](memory.md).

## Organization strategies
- By use case: Sales Qualification, Customer Support, Compliance Monitoring, Quality Assurance.
- By delivery destination: CRM Integration, Analytics Dashboard, Ticket System endpoints.
- By analysis type: Quantitative Metrics, Categorical Classification, Qualitative Analysis.
- Hybrid: e.g., Sales - Quantitative vs. Sales - Qualitative; Support - Urgent vs. Support - Complete.

## Best practices
Writing and testing
- Be specific: “Identify the main complaint and rate urgency 1-5.”
- Define formats: “Return sentiment 1-10 plus one-sentence rationale.”
- Provide context and examples.
- Start with test conversations; review and refine until consistent.
- Use clear, descriptive names indicating what/why/scope.

Groups and delivery
- Start small: 2–4 related insights per group; expand as validated.
- Test without webhooks first; add webhooks after reviewing Portal results.
- Document webhook endpoints (owners, expectations, troubleshooting).
- Version groups for major changes (e.g., “Support Analytics v2”).
- Monitor insights count: 1–5 focused; 5–10 comprehensive; 10+ consider splitting.

Structured schemas
- Keep schemas focused; split complex needs across multiple insights.
- Prefer enum for fixed categories; mark fields required only when always present.
- Provide numeric ranges and test edge cases (short, ambiguous, multi-topic chats).

Security
- Use HTTPS, authentication, encryption-at-rest, and audit logs for regulated data.

## Troubleshooting
- Insights not appearing: Confirm the group is assigned, a conversation completed after assignment, and individual insights are configured correctly.
- Webhook not receiving data: Verify URL correctness/accessibility, 200 OK responses, and check your endpoint logs.
- Wrong insights in group: Edit the group, adjust membership, and Save; changes apply to future conversations immediately.

## Industry use case patterns
Healthcare
- Insights: HIPAA Compliance Verification (structured), Patient Care Assessment (structured), Call Summary for Patient Record (unstructured).
- Group: “Healthcare Patient Calls” with webhook to your EHR; trigger compliance alerts, urgent follow-ups, and store summaries.

Customer support
- Insights: Support Ticket Classifier, Customer Satisfaction Score, Agent Quality Assessment (all structured).
- Group: “Support Call Analytics” with webhook to your ticketing/analytics systems; auto-create tickets, flag churn risk, and log performance.

Sales
- Insights: Sales Lead Qualifier, Product Interest Tracking (structured), Sales Objections Analysis (unstructured).
- Group: “Sales Call Intelligence” with webhook to your CRM; upsert leads, route hot leads, and kick off nurture campaigns.

E-commerce
- Insights: Order Support Classifier, E-commerce Customer Sentiment (structured), Product Feedback Collection (unstructured).
- Group: “E-commerce Customer Insights” with webhook to commerce backend; automate returns/refunds and capture product feedback.

Financial services
- Insights: Fraud Risk Detector, Financial Compliance Verification, Financial Inquiry Classifier (structured).
- Group: “Financial Services Security & Compliance” with webhook to fraud/compliance queues; alert on risk, log violations, and route callbacks.

See more patterns and examples in [AI Insights Use Cases](ai-insights-use-cases.md).

## Next steps and related resources
- Deep dives: [Creating Insights](creating-insights.md), [Structured insights](structured-insights.md), [Insight Groups](insight-groups.md), [AI Insights Use Cases](ai-insights-use-cases.md).
- Assistant setup and assignment: [Voice Assistant Quickstart](voice-assistant-quickstart.md).
- Data access and filtering: [Memory](memory.md).
- Context enrichment: [Dynamic Variables](dynamic-variables.md).
