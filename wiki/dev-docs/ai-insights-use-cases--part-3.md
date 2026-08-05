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

*Part 3 of 5 — see also: [Part 1](ai-insights-use-cases--part-1.md), [Part 2](ai-insights-use-cases--part-2.md), [Part 4](ai-insights-use-cases--part-4.md), [Part 5](ai-insights-use-cases--part-5.md)*

Industry-specific examples of Telnyx AI Insights implementations, covering healthcare, customer support, sales, e-commerce, and financial services. Each use case includes insight configurations, group organization, webhook integration patterns, and best practices for production deployments.

## Sales

### Use case: Lead qualification & pipeline management

**Business Need:** Automatically qualify inbound leads, score opportunities, and route to appropriate sales representatives.

#### Insight configurations

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

#### Insight group configuration

```
Name: Sales Call Intelligence
Webhook URL: https://crm.salesteam.com/api/webhooks/leads

Insights:
  - Sales Lead Qualifier
  - Product Interest Tracking
  - Sales Objections Analysis
```

#### Webhook integration example

```javascript
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
