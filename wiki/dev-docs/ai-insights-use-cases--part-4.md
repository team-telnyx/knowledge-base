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

*Part 4 of 5 — see also: [Part 1](ai-insights-use-cases--part-1.md), [Part 2](ai-insights-use-cases--part-2.md), [Part 3](ai-insights-use-cases--part-3.md), [Part 5](ai-insights-use-cases--part-5.md)*

Industry-specific examples of Telnyx AI Insights implementations, covering healthcare, customer support, sales, e-commerce, and financial services. Each use case includes insight configurations, group organization, webhook integration patterns, and best practices for production deployments.

## E-commerce

### Use case: Customer service & order management

**Business Need:** Handle order inquiries, identify dissatisfaction early, and capture product feedback.

#### Insight configurations

**1. Order inquiry classification** (structured)

```
Name: Order Support Classifier

Instructions: Classify the type of order-related inquiry or issue.

Parameters:
1. inquiry_type
   - Type: string
   - Required: Yes
   - Description: Type of inquiry: "order_status", "return_request", "product_question", "shipping_issue", "payment_problem", "cancel_order", "modify_order"

2. order_number
   - Type: string
   - Required: No
   - Description: Order number if mentioned

3. urgency
   - Type: string
   - Required: Yes
   - Description: Urgency level: "urgent", "moderate", "low"

4. resolution_provided
   - Type: boolean
   - Required: Yes
   - Description: Was a resolution or answer provided?

5. compensation_offered
   - Type: boolean
   - Required: No
   - Description: Was any compensation (refund, discount, credit) offered?

6. next_action
   - Type: string
   - Required: Yes
   - Description: Required next step: "none", "process_return", "issue_refund", "escalate", "ship_replacement", "cancel_order"
```

**2. Customer sentiment** (structured)

```
Name: E-commerce Customer Sentiment

Instructions: Gauge customer satisfaction with their shopping experience.

Parameters:
1. satisfaction_level
   - Type: string
   - Required: Yes
   - Description: Overall satisfaction: "very_satisfied", "satisfied", "neutral", "dissatisfied", "very_dissatisfied"

2. likely_to_repurchase
   - Type: boolean
   - Required: Yes
   - Description: Based on the conversation, is customer likely to purchase again?

3. likely_to_recommend
   - Type: number
   - Required: Yes
   - Description: NPS score from 0-10: How likely to recommend to a friend?

4. complaint_severity
   - Type: string
   - Required: No
   - Description: If complaining, severity: "minor", "moderate", "major"

5. praise_areas
   - Type: array
   - Required: No
   - Description: What aspects did they appreciate or praise?
```

**3. Product feedback** (unstructured)

```
Name: Product Feedback Collection

Instructions: Capture any product feedback, suggestions, or quality issues mentioned. Include:
- Specific products mentioned.
- Positive feedback or features they loved.
- Negative feedback or problems encountered.
- Feature requests or suggestions.
- Quality concerns.

Focus on actionable insights for product and marketing teams.
```

#### Insight group configuration

```
Name: E-commerce Customer Insights
Webhook URL: https://api.shop.com/webhooks/customer-insights

Insights:
  - Order Support Classifier
  - E-commerce Customer Sentiment
  - Product Feedback Collection
```

#### Webhook integration example

```javascript
app.post('/webhooks/customer-insights', async (req, res) => {
  res.status(200).send('OK');

  const { conversation_id, insights } = req.body;
  const insightMap = Object.fromEntries(
    insights.map(i => [i.insight_name, i.result])
  );

  const orderClassification = insightMap['Order Support Classifier'];
  const sentiment = insightMap['E-commerce Customer Sentiment'];
  const feedback = insightMap['Product Feedback Collection'];

  // Process order actions
  switch (orderClassification.next_action) {
    case 'process_return':
      await orders.initiateReturn(orderClassification.order_number);
      break;
    case 'issue_refund':
      await orders.processRefund(orderClassification.order_number);
      break;
    case 'cancel_order':
      await orders.cancel(orderClassification.order_number);
      break;
    case 'ship_replacement':
      await orders.shipReplacement(orderClassification.order_number);
      break;
  }

  // Alert on poor experiences
  if (sentiment.satisfaction_level === 'very_dissatisfied') {
    await alerts.send({
      type: 'customer_dissatisfaction',
      conversation_id,
      order_number: orderClassification.order_number,
      severity: orderClassification.complaint_severity,
      nps_score: sentiment.likely_to_recommend
    });
  }

  // Collect product feedback
  if (feedback) {
    await productFeedback.create({
      conversation_id,
      feedback: feedback,
      source: 'ai_assistant',
      sentiment: sentiment.satisfaction_level
    });
  }

  // Segment for marketing
  if (!sentiment.likely_to_repurchase) {
    await marketing.addToWinBackCampaign({
      conversation_id,
      reason: orderClassification.inquiry_type
    });
  }
});
```
