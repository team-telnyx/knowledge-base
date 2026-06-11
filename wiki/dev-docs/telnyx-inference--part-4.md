---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
  content_hash: ff522f2e6bd1723aaae77aa0136c8445286d925413287656782da4be07d09f11
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: 7b522bb1ea6820875819e42eeb02ef42c22beea5981ac6d32e5415b96292655b
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 50e16a3392164849e8db62587e0a7d5fdc2f38c5f7bf22efbf8816070480878f
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 0bf1cdff1a2e68b76975f93b097d45c41337877c1dbbba2397ea493699f9fd35
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 35e09b760fc2688800b0cbec4812a2b908b2893f4c2b014c4c85e4b020cfe572
- url: https://developers.telnyx.com/docs/inference/clusters
  content_hash: 2168a5dbf3b8c93576ac5ca7eb6daef42850a48d2787e29743f161a668bc6b0d
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: bb1baccf1e6687a03af6f732aaceb0e310beb83d0b6ce6aa7f9cb934418a351b
- url: https://developers.telnyx.com/docs/inference/data-residency
  content_hash: 5ec98630f8132d215237b19167267f10bf0a0afc3879a204570c1e18258b6c5b
- url: https://developers.telnyx.com/docs/inference/embeddings
  content_hash: da55ec529bd85eaa5fbcc3baac0d1b3d0c01b0d70cc62a03854a507fe8accdf0
- url: https://developers.telnyx.com/docs/inference/functions
  content_hash: d8787dd1d761b9535b4b844287b039a25c7cc0a895592a3309b5da4b3f1ceb15
- url: https://developers.telnyx.com/docs/inference/getting-started/index
  content_hash: 91d21b775b382bcbd90ae079c0b93ca3854a5cfea589b985c25e9a151ea79b45
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
