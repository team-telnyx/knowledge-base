---
title: AI insights use cases
summary: Industry-specific examples and implementation patterns for AI Insights across healthcare, customer support, sales, e-commerce, and financial services.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases/index
    content_hash: fb6a9998d1a01fe6076bb70cfe8fe1fa8351b8aff835c38ba2e5099397e0576a
updated_at: 2026-04-10T00:00:00Z
---

# AI insights use cases

Industry-specific examples and implementation patterns for AI Insights across healthcare, customer support, sales, e-commerce, and financial services.

This guide provides complete, industry-specific examples of AI Insights implementations. Each use case includes insight configurations, group organization, webhook integration, and best practices.

## Healthcare

### Use case: Patient call quality & compliance

**Business Need:** Ensure regulatory compliance (HIPAA) while monitoring patient interaction quality and identifying follow-up needs.

### Insight configurations

**1. HIPAA compliance check** (structured)

```
Name: HIPAA Compliance Verification

Instructions: Verify HIPAA compliance requirements were met during this call.

Parameters:
1. disclosures_made
   - Type: boolean
   - Required: Yes
   - Description: Were required privacy disclosures made at the start of the call?

2. consent_obtained
   - Type: boolean
   - Required: Yes
   - Description: Was patient consent obtained before discussing PHI?

3. phi_handled_properly
   - Type: boolean
   - Required: Yes
   - Description: Was Protected Health Information handled according to HIPAA guidelines?

4. violations
   - Type: array
   - Required: No
   - Description: List any potential HIPAA violations or concerns

5. compliant
   - Type: boolean
   - Required: Yes
   - Description: Overall assessment: was this call HIPAA compliant?
```

**2. Patient care quality** (structured)

```
Name: Patient Care Assessment

Instructions: Evaluate the quality of patient care and interaction.

Parameters:
1. empathy_score
   - Type: number
   - Required: Yes
   - Description: Rate the assistant's empathy from 1-5 (1=robotic, 5=highly empathetic)

2. clarity_score
   - Type: number
   - Required: Yes
   - Description: Rate explanation clarity from 1-5 (1=confusing, 5=very clear)

3. questions_answered
   - Type: boolean
   - Required: Yes
   - Description: Were all patient questions adequately answered?

4. follow_up_needed
   - Type: boolean
   - Required: Yes
   - Description: Does this patient require follow-up contact?

5. urgency_level
   - Type: string
   - Required: Yes
   - Description: Urgency classification: "routine", "moderate", "urgent", "emergency"
```

**3. Appointment summary** (unstructured)

```
Name: Call Summary for Patient Record

Instructions: Create a concise summary for the patient's medical record. Include:
- Reason for call.
- Symptoms or concerns discussed.
- Instructions provided.
- Any appointments scheduled.
- Follow-up requirements.

Keep summary professional and factual for medical record inclusion.
```

### Insight group configuration

```
Name: Healthcare Patient Calls
Webhook URL: https://ehr.healthcorp.com/api/webhooks/ai-insights

Insights:
  - HIPAA Compliance Verification
  - Patient Care Assessment
  - Call Summary for Patient Record
```

### Webhook integration example

```python theme={null}
@app.route('/api/webhooks/ai-insights', methods=['POST'])
def handle_patient_call_insights():
    data = request.json

    conversation_id = data['conversation_id']
    insights = {i['insight_name']: i['result'] for i in data['insights']}

    # Check compliance
    compliance = insights.get('HIPAA Compliance Verification', {})
    if not compliance.get('compliant'):
        # Alert compliance team
        alert_compliance_team(
            conversation_id=conversation_id,
            violations=compliance.get('violations', [])
        )

    # Check if urgent follow-up needed
    care = insights.get('Patient Care Assessment', {})
    if care.get('urgency_level') in ['urgent', 'emergency']:
        # Create urgent task
        create_urgent_followup(
            conversation_id=conversation_id,
            urgency=care['urgency_level']
        )

    # Store summary in EHR
    summary = insights.get('Call Summary for Patient Record')
    if summary:
        ehr.add_patient_note(
            conversation_id=conversation_id,
            note=summary,
            note_type='ai_assistant_call'
        )

    return jsonify({'status': 'processed'}), 200
```

### Expected results

```json theme={null}
{
  "insights": [
    {
      "insight_name": "HIPAA Compliance Verification",
      "result": {
        "disclosures_made": true,
        "consent_obtained": true,
        "phi_handled_properly": true,
        "violations": [],
        "compliant": true
      }
    },
    {
      "insight_name": "Patient Care Assessment",
      "result": {
        "empathy_score": 5,
        "clarity_score": 4,
        "questions_answered": true,
        "follow_up_needed": true,
        "urgency_level": "routine"
      }
    },
    {
      "insight_name": "Call Summary for Patient Record",
      "result": "Patient called regarding follow-up on recent lab results. Explained test findings indicating normal thyroid function. Patient had questions about medication dosing which were addressed. Scheduled 6-month follow-up appointment. No immediate concerns noted."
    }
  ]
}
```

***

## Customer support

### Use case: Support ticket automation & quality monitoring

**Business Need:** Automatically categorize and route support calls, monitor agent performance, and ensure customer satisfaction.

### Insight configurations

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

### Insight group configuration

```
Name: Support Call Analytics
Webhook URL: https://support.mycompany.com/api/webhooks/ai-insights

Insights:
  - Support Ticket Classifier
  - Customer Satisfaction Score
  - Agent Quality Assessment
```

### Webhook integration example

```javascript theme={null}
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

***

## Sales

### Use case: Lead qualification & pipeline management

**Business Need:** Automatically qualify inbound leads, score opportunities, and route to appropriate sales representatives.

### Insight configurations

**1. Lead qualification** (structured)

```
Name: Sales Lead Qualifier

Instructions: Assess the quality and readiness of this sales lead.

Parameters:
1. budget_discussed
   - Type: boolean
   - Required: Yes
   - Description: Did the prospect discuss budget or pricing?

2. budget_range
   - Type: string
   - Required: No
   - Description: Budget range if mentioned: "under_10k", "10k_50k", "50k_100k", "over_100k", "not_disclosed"

3. decision_timeframe
   - Type: string
   - Required: Yes
   - Description: When will they decide: "immediate", "this_month", "this_quarter", "next_quarter", "exploring", "unknown"

4. authority_level
   - Type: string
   - Required: Yes
   - Description: Decision-making authority: "decision_maker", "influencer", "end_user", "researcher", "unknown"

5. pain_points
   - Type: array
   - Required: Yes
   - Description: Specific problems or needs mentioned by the prospect

6. competitor_mentions
   - Type: array
   - Required: No
   - Description: Names of competing solutions mentioned

7. lead_score
   - Type: number
   - Required: Yes
   - Description: Overall qualification score from 1-10 based on BANT criteria

8. recommended_action
   - Type: string
   - Required: Yes
   - Description: Next step: "immediate_followup", "schedule_demo", "send_proposal", "nurture", "disqualify"
```

**2. Product interest** (structured)

```
Name: Product Interest Tracking

Instructions: Identify which products or features the prospect showed interest in.

Parameters:
1. products_mentioned
   - Type: array
   - Required: Yes
   - Description: List of products discussed during the call

2. primary_interest
   - Type: string
   - Required: Yes
   - Description: The product they seemed most interested in

3. feature_priorities
   - Type: array
   - Required: No
   - Description: Specific features they asked about or emphasized

4. use_case
   - Type: string
   - Required: Yes
   - Description: Brief description of their intended use case

5. integration_requirements
   - Type: array
   - Required: No
   - Description: Systems they need to integrate with
```

**3. Objections & concerns** (unstructured)

```
Name: Sales Objections Analysis

Instructions: Identify any objections, concerns, or hesitations the prospect expressed. Include:
- Price/budget concerns.
- Feature gaps or limitations.
- Competitive comparisons.
- Implementation concerns.
- Trust or credibility questions.

Provide actionable insights for sales team to address these objections.
```

### Insight group configuration

```
Name: Sales Call Intelligence
Webhook URL: https://crm.salesteam.com/api/webhooks/leads

Insights:
  - Sales Lead Qualifier
  - Product Interest Tracking
  - Sales Objections Analysis
```

### Webhook integration example

```javascript theme={null}
app.post('/api/webhooks/leads', async (req, res) => {
  res.status(200).send('OK');

  const { conversation_id, insights } = req.body;
  const insightMap = Object.fromEntries(
    insights.map(i => [i.insight_name, i.result])
  );

  const qualification = insightMap['Sales Lead Qualifier'];
  const interest = insightMap['Product Interest Tracking'];
  const objections = insightMap['Sales Objections Analysis'];

  // Create or update lead in CRM
  const lead = await crm.leads.upsert({
    source: 'ai_assistant',
    conversation_id,
    score: qualification.lead_score,
    budget_range: qualification.budget_range,
    timeframe: qualification.decision_timeframe,
    authority: qualification.authority_level,
    pain_points: qualification.pain_points,
    primary_interest: interest.primary_interest,
    products: interest.products_mentioned,
    use_case: interest.use_case,
    objections: objections
  });

  // Route high-quality leads immediately
  if (qualification.lead_score >= 8) {
    const rep = await assignSalesRep(interest.primary_interest);
    await crm.tasks.create({
      assigned_to: rep,
      lead_id: lead.id,
      type: 'immediate_followup',
      priority: 'high',
      notes: `High-quality lead (score: ${qualification.lead_score}). ${qualification.recommended_action}`
    });

    // Send Slack notification
    await slack.notify({
      channel: '#sales',
      message: `🔥 Hot lead! Score: ${qualification.lead_score}/10. Assigned to ${rep.name}.`
    });
  }

  // Add to appropriate nurture campaign
  if (qualification.recommended_action === 'nurture') {
    await marketing.addToCampaign(lead.email, {
      campaign: `nurture_${qualification.decision_timeframe}`,
      interests: interest.products_mentioned
    });
  }
});
```

***

## E-commerce

### Use case: Customer service & order management

**Business Need:** Handle order inquiries, identify dissatisfaction early, and capture product feedback.

### Insight configurations

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

### Insight group configuration

```
Name: E-commerce Customer Insights
Webhook URL: https://api.shop.com/webhooks/customer-insights

Insights:
  - Order Support Classifier
  - E-commerce Customer Sentiment
  - Product Feedback Collection
```

### Webhook integration example

```javascript theme={null}
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

***

## Financial services

### Use case: Fraud detection & compliance

**Business Need:** Identify potential fraud, ensure regulatory compliance, and categorize financial inquiries.

### Insight configurations

**1. Fraud risk assessment** (structured)

```
Name: Fraud Risk Detector

Instructions: Assess potential fraud risk indicators in this conversation.

Parameters:
1. risk_level
   - Type: string
   - Required: Yes
   - Description: Overall risk: "no_risk", "low", "medium", "high", "critical"

2. risk_indicators
   - Type: array
   - Required: No
   - Description: Specific fraud indicators detected (e.g., "urgency_pressure", "unusual_request", "inconsistent_info", "social_engineering_attempt")

3. verification_requested
   - Type: boolean
   - Required: Yes
   - Description: Did the caller request account changes or sensitive actions?

4. authentication_status
   - Type: string
   - Required: Yes
   - Description: Authentication status: "verified", "partially_verified", "not_verified", "failed_verification"

5. recommended_action
   - Type: string
   - Required: Yes
   - Description: Recommended action: "approve", "additional_verification", "escalate_to_fraud_team", "block_immediately"

6. confidence_score
   - Type: number
   - Required: Yes
   - Description: Confidence in risk assessment from 0-100%
```

**2. Compliance check** (structured)

```
Name: Financial Compliance Verification

Instructions: Verify regulatory compliance requirements for financial services.

Parameters:
1. required_disclosures_made
   - Type: boolean
   - Required: Yes
   - Description: Were all required financial disclosures made?

2. customer_consent_obtained
   - Type: boolean
   - Required: No
   - Description: Was consent obtained for account changes or data sharing?

3. pii_handled_properly
   - Type: boolean
   - Required: Yes
   - Description: Was Personally Identifiable Information handled securely?

4. recording_disclosure
   - Type: boolean
   - Required: Yes
   - Description: Was call recording disclosure made?

5. compliance_violations
   - Type: array
   - Required: No
   - Description: Any potential compliance violations or concerns

6. compliant
   - Type: boolean
   - Required: Yes
   - Description: Overall compliance status
```

**3. Inquiry categorization** (structured)

```
Name: Financial Inquiry Classifier

Instructions: Categorize the type of financial inquiry or request.

Parameters:
1. inquiry_category
   - Type: string
   - Required: Yes
   - Description: Primary category: "account_balance", "transaction_dispute", "card_activation", "fraud_report", "account_opening", "loan_inquiry", "investment_advice", "general_question"

2. account_type
   - Type: string
   - Required: No
   - Description: Account type involved: "checking", "savings", "credit_card", "loan", "investment", "multiple"

3. transaction_amount
   - Type: number
   - Required: No
   - Description: Dollar amount if transaction-related inquiry

4. resolution_status
   - Type: string
   - Required: Yes
   - Description: Resolution status: "resolved", "pending", "escalated", "requires_callback"

5. callback_required
   - Type: boolean
   - Required: Yes
   - Description: Does customer need a callback from specialist?
```

### Insight group configuration

```
Name: Financial Services Security & Compliance
Webhook URL: https://api.bank.com/webhooks/insights

Insights:
  - Fraud Risk Detector
  - Financial Compliance Verification
  - Financial Inquiry Classifier
```

### Webhook integration example

```python theme={null}
@app.route('/webhooks/insights', methods=['POST'])
def handle_financial_insights():
    data = request.json

    conversation_id = data['conversation_id']
    insights = {i['insight_name']: i['result'] for i in data['insights']}

    fraud_risk = insights.get('Fraud Risk Detector', {})
    compliance = insights.get('Financial Compliance Verification', {})
    inquiry = insights.get('Financial Inquiry Classifier', {})

    # Handle high fraud risk immediately
    if fraud_risk.get('risk_level') in ['high', 'critical']:
        fraud_team.alert({
            'conversation_id': conversation_id,
            'risk_level': fraud_risk['risk_level'],
            'indicators': fraud_risk['risk_indicators'],
            'recommended_action': fraud_risk['recommended_action'],
            'confidence': fraud_risk['confidence_score']
        })

        # Block if critical
        if fraud_risk['risk_level'] == 'critical':
            security.block_account_temporarily(conversation_id)

    # Handle compliance violations
    if not compliance.get('compliant'):
        compliance_team.alert({
            'conversation_id': conversation_id,
            'violations': compliance['compliance_violations'],
            'severity': 'high'
        })

        # Log for audit
        audit_log.create({
            'event': 'compliance_violation',
            'conversation_id': conversation_id,
            'details': compliance
        })

    # Route inquiry to appropriate team
    if inquiry.get('callback_required'):
        routing.create_callback({
            'conversation_id': conversation_id,
            'category': inquiry['inquiry_category'],
            'account_type': inquiry.get('account_type'),
            'priority': 'high' if fraud_risk['risk_level'] != 'no_risk' else 'normal'
        })

    return jsonify({'status': 'processed'}), 200
```

***

## Best practices across use cases

### 1. Start with core insights

Begin with 2-3 essential insights:

* ✅ Sentiment/satisfaction.
* ✅ Primary classification.
* ✅ Action required.

Add more specialized insights once core metrics are validated.

### 2. Balance structured and unstructured

Use structured insights for:

* Metrics and scores.
* Categories and classifications.
* Boolean flags.

Use unstructured insights for:

* Summaries and context.
* Open-ended feedback.
* Nuanced analysis.

### 3. Configure appropriate webhooks

* **Real-time action required** → Webhook to operational system.
* **Analytics only** → Webhook to analytics platform.
* **Manual review** → No webhook, use Portal.

### 4. Test with real conversations

Before production:

1. Test insights on 10-20 real conversations.
2. Review accuracy of classifications.
3. Validate webhook integration.
4. Adjust instructions based on results.

### 5. Monitor and iterate

Track these metrics:

* Insight accuracy.
* Webhook delivery success rate.
* False positive/negative rates for classifications.
* Time to process insights.

Refine instructions monthly based on performance.

### 6. Secure sensitive data

For regulated industries:

* Use HTTPS for all webhooks.
* Implement proper authentication.
* Encrypt data at rest.
* Maintain audit logs.
* Follow industry-specific compliance requirements.

## Related resources

* [Voice Assistant Quickstart](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant) - Set up your AI assistant.
* [Memory API](https://developers.telnyx.com/docs/inference/ai-assistants/memory) - Use insights in conversation memory.
* [API Reference](https://developers.telnyx.com/api-reference/assistants/list-assistants) - Programmatic insights access.
