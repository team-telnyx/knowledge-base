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

*Part 1 of 5 — see also: [Part 2](ai-insights-use-cases--part-2.md), [Part 3](ai-insights-use-cases--part-3.md), [Part 4](ai-insights-use-cases--part-4.md), [Part 5](ai-insights-use-cases--part-5.md)*

Industry-specific examples of Telnyx AI Insights implementations, covering healthcare, customer support, sales, e-commerce, and financial services. Each use case includes insight configurations, group organization, webhook integration patterns, and best practices for production deployments.

## Overview

This guide provides complete, industry-specific examples of AI Insights implementations. Each use case includes insight configurations, group organization, webhook integration, and best practices for production deployments.

## Healthcare

### Use case: Patient call quality & compliance

**Business Need:** Ensure regulatory compliance (HIPAA) while monitoring patient interaction quality and identifying follow-up needs.

#### Insight configurations

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

#### Insight group configuration

```
Name: Healthcare Patient Calls
Webhook URL: https://ehr.healthcorp.com/api/webhooks/ai-insights

Insights:
  - HIPAA Compliance Verification
  - Patient Care Assessment
  - Call Summary for Patient Record
```

#### Webhook integration example

```python
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

#### Expected results

```json
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
