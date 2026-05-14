---
title: Number Reputation
summary: Telnyx Number Reputation monitors and improves the spam reputation of your
  outbound US local phone numbers. Powered by Hiya, it provides real-time risk levels,
  granular scores, and automated rechecks. You’ll first register an Enterprise, accept
  Terms of Service, upload a Letter of Authorization, then enable monitoring and query
  results via API.
sources:
- url: https://developers.telnyx.com/docs/branded-calling/enterprises
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
updated_at: 2026-05-14T09:44:00Z
---

# Number Reputation

Telnyx Number Reputation monitors and improves the spam reputation of your outbound US local phone numbers. Powered by Hiya, it provides real-time risk levels, granular scores, and automated rechecks. You’ll first register an Enterprise, accept Terms of Service, upload a Letter of Authorization, then enable monitoring and query results via API.

## What it is
Number Reputation gives programmatic visibility into how analytics engines perceive your outbound caller IDs, replacing “Spam Likely” guesswork with actionable data:
- Spam risk: low, medium, high
- Four granular 0–100 scores with timestamps
- Historical tracking and scheduled auto-refreshes
Powered by Hiya (AT&T’s primary spam analytics partner). When enabled, numbers are registered across Hiya, First Orion, and TNS.

## Relationship to Enterprises
An Enterprise represents your business entity on Telnyx and is required before using Number Reputation. It’s a shared resource you’ll also use for Branded Calling (name/logo/call reason — coming soon). The Enterprise collects all business and billing details up front so you don’t need to update later.

## Access and prerequisites
- Telnyx account level: verified or enterprise (trial/standard paid not supported)
- Telnyx API key
- At least one US local phone number on your account (E.164, in service, owned by you)
- Signed Letter of Authorization (LOA) from the business entity

## Accept Terms of Service
One-time per account, required before enabling monitoring:
```
POST /v2/terms_of_service/number_reputation/agree
Authorization: Bearer YOUR_API_KEY
```

## Create an Enterprise
Create once, then reuse across products:
```
POST /v2/enterprises
```
Provide required organization fields (examples):
- legal_name (3–64 chars), doing_business_as
- organization_type (commercial, government, non_profit)
- country_code (ISO 3166-1 alpha-2), website, fein, industry
- number_of_employees, organization_legal_type
- organization_contact (name, email, title, phone)
- billing_contact (name, email, phone_number)
- organization_physical_address and billing_address (country, state, city, postal_code, street)
Save the returned id as your enterprise_id.

## Enable Number Reputation
1) Upload your signed LOA via the Documents API and note the document_id.
2) Enable monitoring with your Enterprise and LOA:
```
POST /v2/enterprises/{enterprise_id}/reputation
{ "loa_document_id": "YOUR_DOCUMENT_ID" }
```
Check status anytime:
```
GET /v2/enterprises/{enterprise_id}/reputation
```

## Vetting lifecycle and status
- pending → approved: you can now register numbers and query reputation
- pending → rejected: review rejection_reasons in the response
- approved → deleted: reputation disabled via DELETE
Response fields include status (pending, approved, rejected, deleted), check_frequency, loa_document_id, rejection_reasons.

## Manage phone numbers (associate, list, remove)
Associate numbers for monitoring (all-or-nothing up to 100 per request):
```
POST /v2/enterprises/{enterprise_id}/reputation/numbers
{ "phone_numbers": ["+12025551234", "+12025555678"] }
```
Constraints:
- US local numbers only, E.164 format
- Must be in-service and belong to your account
- Up to 100 numbers per request; atomic operation
List all monitored numbers (supports pagination with page[number], page[size]):
```
GET /v2/enterprises/{enterprise_id}/reputation/numbers
```
Remove a number from monitoring:
```
DELETE /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}
```
Simplified endpoints (if your account has only one Enterprise):
- GET /v2/reputation/numbers
- GET /v2/reputation/numbers/{phone_number}
- DELETE /v2/reputation/numbers/{phone_number}

## Query reputation (cached vs fresh)
- Cached (free): returns most recently stored results
```
GET /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}
```
- Fresh (billed): fetches live data from Hiya
```
GET /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}?fresh=true
```
If no cached data exists, a fresh query is triggered automatically. No changes to your call control or voice setup are required; this is a standalone monitoring product.

## Reputation data model and meanings
Reputation response includes phone_number and reputation_data with:
- spam_risk: low | medium | high
- spam_category: label if flagged (e.g., Telemarketer, Survey, Debt Collector, Nonprofit, Political)
- maturity_score (0–100): calling history over time
- connection_score (0–100): how often recipients answer
- engagement_score (0–100): whether recipients stay on the call
- sentiment_score (0–100): recipient sentiment/opt-in behavior (e.g., blocks/reports)
- last_refreshed_at: ISO timestamp of the latest reputation refresh
A null score means insufficient data.

## Auto-refresh schedules and cost
Telnyx can automatically run fresh queries across all registered numbers based on check_frequency:
- business_daily (Mon–Fri, default)
- daily (every day)
- weekly
- biweekly
- monthly
- never (manual only; use ?fresh=true or bulk refresh)
Change the schedule:
```
PATCH /v2/enterprises/{enterprise_id}/reputation/frequency
{ "check_frequency": "daily" }
```
Billing notes: cached reads are free; each fresh query (including auto-refresh) is billed per number. Choose a frequency that balances freshness and cost.

## Disable Number Reputation
Stop monitoring and de-register numbers from analytics providers:
```
DELETE /v2/enterprises/{enterprise_id}/reputation
```
Status transitions to deleted.

## Limits and constraints
- Phone numbers: US local only, E.164 format
- Batch size: up to 100 numbers per request (atomic)
- Score range: 0–100 (null when insufficient data)
- Account access: verified or enterprise-level accounts only

## See also
- [Enterprises](enterprises.md) — Enterprise object, purpose, and required fields for setup
