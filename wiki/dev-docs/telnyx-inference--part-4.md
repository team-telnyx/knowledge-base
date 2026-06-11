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

*Part 4 of 6 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 5](telnyx-inference--part-5.md), [Part 6](telnyx-inference--part-6.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## Insight Use Cases

### Healthcare: Patient Call Quality & Compliance

**Insight configurations:**

| Insight | Type | Purpose |
|---|---|---|
| HIPAA Compliance Verification | Structured | Check disclosures, consent, PHI handling, violations, overall compliance |
| Patient Care Assessment | Structured | Rate empathy and clarity (1-5), check questions answered, follow-up needed, urgency level |
| Call Summary for Patient Record | Unstructured | Concise summary for the patient's medical record |

**Group**: `Healthcare Patient Calls` → Webhook to EHR system. On receipt: check compliance (alert team on violations), route urgent follow-ups, store summary in EHR.

### Customer Support: Ticket Automation & Quality Monitoring

| Insight | Type | Purpose |
|---|---|---|
| Support Ticket Classifier | Structured | Issue type, product area, priority, resolution status, tags |
| Customer Satisfaction Score | Structured | CSAT (1-5), sentiment, frustration level, churn risk, positive feedback |
| Agent Quality Assessment | Structured | Professionalism, problem-solving, efficiency scores, escalation needed, improvement areas |

**Group**: `Support Call Analytics` → Webhook to ticketing system. Create tickets for unresolved issues, alert on churn risk, log agent performance.

### Sales: Lead Qualification & Pipeline Management

| Insight | Type | Purpose |
|---|---|---|
| Sales Lead Qualifier | Structured | Budget discussed, budget range, decision timeframe, authority level, pain points, competitor mentions, lead score (1-10), recommended action |
| Product Interest Tracking | Structured | Products mentioned, primary interest, feature priorities, use case, integration requirements |
| Sales Objections Analysis | Unstructured | Identify objections, concerns, hesitations with actionable insights for the sales team |

**Group**: `Sales Call Intelligence` → Webhook to CRM. Create/update leads, route high-quality leads immediately, add to nurture campaigns.

### E-commerce: Customer Service & Order Management

| Insight | Type | Purpose |
|---|---|---|
| Order Support Classifier | Structured | Inquiry type, order number, urgency, resolution provided, compensation offered, next action |
| E-commerce Customer Sentiment | Structured | Satisfaction level, likely to repurchase, NPS score (0-10), complaint severity, praise areas |
| Product Feedback Collection | Unstructured | Product feedback, suggestions, quality issues |

**Group**: `E-commerce Customer Insights` → Webhook to shop system. Process order actions (returns, refunds, cancellations, replacements), alert on poor experiences, collect product feedback, segment for win-back campaigns.

### Financial Services: Fraud Detection & Compliance

| Insight | Type | Purpose |
|---|---|---|
| Fraud Risk Detector | Structured | Risk level, risk indicators, verification requested, authentication status, recommended action, confidence score |
| Financial Compliance Verification | Structured | Disclosures made, consent obtained, PII handled properly, recording disclosure, violations, overall compliance |
| Financial Inquiry Classifier | Structured | Inquiry category, account type, transaction amount, resolution status, callback required |

**Group**: `Financial Services Security & Compliance` → Webhook to bank system. Handle high/critical fraud risk (alert team, block accounts for critical), handle compliance violations (alert, audit log), route callbacks.

### Cross-Use-Case Best Practices

1. **Start with core insights** — begin with 2-3 essential insights (sentiment, classification, action required), then add more specialized ones.
2. **Balance structured and unstructured** — use structured for metrics, categories, and boolean flags; unstructured for summaries, open-ended feedback, and nuanced analysis.
3. **Configure appropriate webhooks** — real-time action → webhook to operational system; analytics only → webhook to analytics platform; manual review → no webhook, use portal.
4. **Test with real conversations** — test on 10-20 real conversations before production, review accuracy, validate webhooks, adjust instructions.
5. **Monitor and iterate** — track accuracy, delivery success rate, false positive/negative rates, and processing time; refine instructions monthly.
6. **Secure sensitive data** — use HTTPS for all webhooks, implement authentication, encrypt data at rest, maintain audit logs, follow industry-specific compliance.
