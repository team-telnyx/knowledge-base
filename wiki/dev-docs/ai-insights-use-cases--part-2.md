---
title: AI Insights Use Cases
summary: Industry-specific examples of Telnyx AI Insights implementations, covering
  healthcare, customer support, sales, e-commerce, and financial services. Each use
  case includes insight configurations, group organization, webhook integration patterns,
  and best practices for production deployments.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
updated_at: 2026-08-05T13:45:59Z
---

# AI Insights Use Cases

*Part 2 of 5 — see also: [Part 1](ai-insights-use-cases--part-1.md), [Part 3](ai-insights-use-cases--part-3.md), [Part 4](ai-insights-use-cases--part-4.md), [Part 5](ai-insights-use-cases--part-5.md)*

Industry-specific examples of Telnyx AI Insights implementations, covering healthcare, customer support, sales, e-commerce, and financial services. Each use case includes insight configurations, group organization, webhook integration patterns, and best practices for production deployments.

## Customer support

### Use case: Support ticket automation & quality monitoring

**Business Need:** Automatically categorize and route support calls, monitor agent performance, and ensure customer satisfaction.

#### Insight configurations

**1. Ticket classification** (structured)

```
Name: Support Ticket Classifier

Instructions: Classify and triage the support request for ticket creation.

Parameters:
1. issue_type
   - Type: string
   - Required: Yes
   - Description: Primary issue category: "technical", "billing", "account", "feature_request", "bug_report", "general"

2. product_area
   - Type: string
   - Required: No
   - Description: Which product or service is affected?

3. priority
   - Type: string
   - Required: Yes
   - Description: Priority level: "critical", "high", "medium", "low"

4. resolved
   - Type: boolean
   - Required: Yes
   - Description: Was the issue completely resolved during this call?

5. resolution_time_minutes
   - Type: number
   - Required: No
   - Description: If resolved, approximately how many minutes did resolution take?

6. tags
   - Type: array
   - Required: No
   - Description: Relevant tags (e.g., "password_reset", "refund_request", "api_error")
```

**2. Customer satisfaction** (structured)

```
Name: Customer Satisfaction Score

Instructions: Assess customer satisfaction from the conversation.

Parameters:
1. csat_score
   - Type: number
   - Required: Yes
   - Description: Customer satisfaction from 1-5 (1=very dissatisfied, 5=very satisfied)

2. sentiment
   - Type: string
   - Required: Yes
   - Description: Overall sentiment: "positive", "neutral", "negative"

3. frustration_level
   - Type: number
   - Required: Yes
   - Description: Customer frustration from 1-5 (1=not frustrated, 5=extremely frustrated)

4. likely_to_churn
   - Type: boolean
   - Required: Yes
   - Description: Based on the conversation, is the customer likely to cancel service?

5. positive_feedback
   - Type: array
   - Required: No
   - Description: Specific things the customer praised or appreciated
```

**3. Agent performance** (structured)

```
Name: Agent Quality Assessment

Instructions: Evaluate the AI assistant's performance in handling this support request.

Parameters:
1. professionalism_score
   - Type: number
   - Required: Yes
   - Description: Professional tone and communication from 1-5

2. problem_solving_score
   - Type: number
   - Required: Yes
   - Description: Effectiveness in solving the issue from 1-5

3. efficiency_score
   - Type: number
   - Required: Yes
   - Description: How efficiently was the issue handled from 1-5

4. escalation_needed
   - Type: boolean
   - Required: Yes
   - Description: Should this have been escalated to human agent?

5. improvement_areas
   - Type: array
   - Required: No
   - Description: Areas where the assistant could improve
```

#### Insight group configuration

```
Name: Support Call Analytics
Webhook URL: https://support.mycompany.com/api/webhooks/ai-insights

Insights:
  - Support Ticket Classifier
  - Customer Satisfaction Score
  - Agent Quality Assessment
```

#### Webhook integration example

```javascript
app.post('/api/webhooks/ai-insights', async (req, res) => {
  res.status(200).send('OK');

  const { conversation_id, insights } = req.body;
  const insightMap = Object.fromEntries(
    insights.map(i => [i.insight_name, i.result])
  );

  const classification = insightMap['Support Ticket Classifier'];
  const satisfaction = insightMap['Customer Satisfaction Score'];
  const performance = insightMap['Agent Quality Assessment'];

  // Create ticket if unresolved
  if (!classification.resolved) {
    await ticketing.create({
      conversation_id,
      type: classification.issue_type,
      priority: classification.priority,
      product: classification.product_area,
      tags: classification.tags,
      customer_sentiment: satisfaction.sentiment
    });
  }

  // Alert on potential churn
  if (satisfaction.likely_to_churn) {
    await alerts.send({
      type: 'churn_risk',
      conversation_id,
      csat_score: satisfaction.csat_score,
      frustration: satisfaction.frustration_level
    });
  }

  // Log agent performance metrics
  await analytics.track('agent_performance', {
    conversation_id,
    professionalism: performance.professionalism_score,
    problem_solving: performance.problem_solving_score,
    efficiency: performance.efficiency_score,
    escalation_needed: performance.escalation_needed
  });
});
```
