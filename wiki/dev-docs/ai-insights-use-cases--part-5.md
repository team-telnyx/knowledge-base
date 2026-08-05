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

*Part 5 of 5 — see also: [Part 1](ai-insights-use-cases--part-1.md), [Part 2](ai-insights-use-cases--part-2.md), [Part 3](ai-insights-use-cases--part-3.md), [Part 4](ai-insights-use-cases--part-4.md)*

Industry-specific examples of Telnyx AI Insights implementations, covering healthcare, customer support, sales, e-commerce, and financial services. Each use case includes insight configurations, group organization, webhook integration patterns, and best practices for production deployments.

## Financial services

### Use case: Fraud detection & compliance

**Business Need:** Identify potential fraud, ensure regulatory compliance, and categorize financial inquiries.

#### Insight configurations

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

#### Insight group configuration

```
Name: Financial Services Security & Compliance
Webhook URL: https://api.bank.com/webhooks/insights

Insights:
  - Fraud Risk Detector
  - Financial Compliance Verification
  - Financial Inquiry Classifier
```

#### Webhook integration example

```python
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

## Best practices across use cases

### 1. Start with core insights

Begin with 2-3 essential insights:

- Sentiment/satisfaction.
- Primary classification.
- Action required.

Add more specialized insights once core metrics are validated.

### 2. Balance structured and unstructured

Use structured insights for:

- Metrics and scores.
- Categories and classifications.
- Boolean flags.

Use unstructured insights for:

- Summaries and context.
- Open-ended feedback.
- Nuanced analysis.

### 3. Configure appropriate webhooks

- **Real-time action required** → Webhook to operational system.
- **Analytics only** → Webhook to analytics platform.
- **Manual review** → No webhook, use Portal.

### 4. Test with real conversations

Before production:

1. Test insights on 10-20 real conversations.
2. Review accuracy of classifications.
3. Validate webhook integration.
4. Adjust instructions based on results.

### 5. Monitor and iterate

Track these metrics:

- Insight accuracy.
- Webhook delivery success rate.
- False positive/negative rates for classifications.
- Time to process insights.

Refine instructions monthly based on performance.

### 6. Secure sensitive data

For regulated industries:

- Use HTTPS for all webhooks.
- Implement proper authentication.
- Encrypt data at rest.
- Maintain audit logs.
- Follow industry-specific compliance requirements.

## Related resources

- [Voice Assistant Quickstart](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant) - Set up your AI assistant.
- [Memory API](https://developers.telnyx.com/docs/inference/ai-assistants/memory) - Use insights in conversation memory.
- [API Reference](/api-reference/assistants/list-assistants) - Programmatic insights access.
