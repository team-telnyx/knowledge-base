---
title: Number Reputation
summary: Telnyx Number Reputation lets you monitor and improve the spam reputation
  of your outbound US local phone numbers. After registering your business as an Enterprise,
  accepting terms, and uploading a Letter of Authorization, you can enable monitoring
  powered by Hiya, view risk levels and granular scores, schedule automatic refreshes,
  and manage numbers via simple APIs.
sources:
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
updated_at: 2026-05-19T15:54:45Z
---

# Number Reputation

Telnyx Number Reputation lets you monitor and improve the spam reputation of your outbound US local phone numbers. After registering your business as an Enterprise, accepting terms, and uploading a Letter of Authorization, you can enable monitoring powered by Hiya, view risk levels and granular scores, schedule automatic refreshes, and manage numbers via simple APIs.

## What Number Reputation provides
- Real-time visibility into spam risk for your outbound numbers
- Spam risk level: low, medium, high
- Four granular scores (0–100): maturity, connection, engagement, sentiment
- Timestamps for when data was last refreshed
- Powered by Hiya (with registration across Hiya, First Orion, and TNS)
- No changes required to call control — this is a standalone monitoring product

## Access and prerequisites
- Telnyx account level: verified or enterprise (trial/standard paid are not eligible)
- API key
- At least one US local phone number on your account
- A signed Letter of Authorization (LOA) authorizing Telnyx to register your numbers with analytics providers

## Enterprises and product relationship
- An Enterprise represents your business on Telnyx and is required for Number Reputation (and Branded Calling).
- Register once, then enable Number Reputation and, optionally, Branded Calling.
- The API collects all enterprise details up front so you don’t need to update later.
- Key enterprise fields include: `legal_name`, `doing_business_as`, `organization_type` (`commercial`, `government`, `non_profit`), `country_code` (ISO 3166-1 alpha-2), `website`, `fein` (EIN), `industry`, `number_of_employees`, `organization_legal_type`, `organization_contact`, `billing_contact`, `organization_physical_address`, `billing_address`.
- Some fields are required specifically for Number Reputation providers (e.g., `doing_business_as`, `industry`) and others for Branded Calling (e.g., `billing_address`).

See [Enterprises](enterprises.md) for the full field reference and account requirements.

## Enablement steps (end-to-end)
1) Accept Terms of Service
- Endpoint: POST /v2/terms_of_service/number_reputation/agree

2) Create an Enterprise (if you don’t already have one)
- Endpoint: POST /v2/enterprises
- Save the `id` from the response as your `enterprise_id`.

3) Upload a Letter of Authorization (LOA)
- Use the Telnyx Documents API to upload your signed LOA and save the returned `document_id`.

4) Enable Number Reputation for the enterprise
- Endpoint: POST /v2/enterprises/{enterprise_id}/reputation
- Body includes: `loa_document_id`
- Your details are sent to Hiya for automated vetting (typically minutes).

5) Associate phone numbers for monitoring
- Endpoint: POST /v2/enterprises/{enterprise_id}/reputation/numbers
- Body includes: `phone_numbers` (up to 100 per request)

6) Query reputation
- Cached (free): GET /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}
- Fresh (billed): GET /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}?fresh=true
- If no cached data exists, a fresh query runs automatically (billed) regardless of the `fresh` parameter.

## Vetting lifecycle and status
- Status transitions:
  - pending → approved (you can now register numbers and query reputation)
  - pending → rejected (see `rejection_reasons` in the response)
  - approved → deleted (when you disable Number Reputation)
- Check status: GET /v2/enterprises/{enterprise_id}/reputation
- Response fields include: `status`, `check_frequency`, `loa_document_id`, `rejection_reasons`.

## Associating phone numbers
- Endpoint: POST /v2/enterprises/{enterprise_id}/reputation/numbers
- Limits and rules:
  - Up to 100 numbers per request
  - Atomic operation: all succeed or all fail
  - Numbers must be US local, in E.164 format
  - Numbers must be in service and belong to your account

## Querying reputation (cached vs fresh)
- Cached query (free): returns the most recent stored reputation data for the number.
- Fresh query (billed): fetches live data from Hiya; use `?fresh=true`.
- If no cached data exists, the first query will be fresh and billed.
- List all monitored numbers: GET /v2/enterprises/{enterprise_id}/reputation/numbers (supports `page[number]` and `page[size]`).

## Reputation data model and scores
Each number returns a `reputation_data` object composed of:
- `spam_risk`: low | medium | high
  - low: clean reputation
  - medium: some risk indicators present
  - high: likely flagged as spam by carriers
- `spam_category`: if flagged, category label such as Telemarketer, Survey, Debt Collector, Nonprofit, Political, etc.
- `maturity_score` (0–100): how established the number is over time
- `connection_score` (0–100): how often recipients answer
- `engagement_score` (0–100): whether recipients stay on the call
- `sentiment_score` (0–100): whether recipients want ongoing contact (blocking/reporting behavior)
- `last_refreshed_at`: timestamp of the latest refresh
- Note: a `null` score means insufficient data.

See [Phone Number Reputation](phone-number-reputation.md) for deeper API usage and examples.

## Auto-refresh schedules and cost
- Telnyx can automatically run fresh reputation checks over all registered numbers on a schedule configured by `check_frequency`.
- Available values:
  - `business_daily` (Mon–Fri, default)
  - `daily` (every day)
  - `weekly`
  - `biweekly`
  - `monthly`
  - `never` (manual only — use `?fresh=true` or bulk refresh)
- Change schedule: PATCH /v2/enterprises/{enterprise_id}/reputation/frequency with `check_frequency`.
- Billing: each auto-refresh counts as a billed fresh query per number. Choose a frequency that balances freshness and cost.

Learn more in [Number Reputation Settings](number-reputation-settings.md).

## Managing monitoring
- Remove a number: DELETE /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}
- Disable Number Reputation entirely: DELETE /v2/enterprises/{enterprise_id}/reputation
  - De-registers your numbers from analytics providers and sets status to `deleted`.

## Constraints and limits
- Phone number format: E.164
- Geography: US local numbers only
- Numbers per request: 100 (atomic)
- Score range: 0–100 (`null` means insufficient data)
- Account access: verified or enterprise-level accounts only

## Simplified endpoints (single-enterprise accounts)
If your account has only one enterprise, you can omit `enterprise_id`:
- List numbers: GET /v2/reputation/numbers
- Get number reputation: GET /v2/reputation/numbers/{phone_number}
- Remove a number: DELETE /v2/reputation/numbers/{phone_number}

## Provider and coverage
- Reputation data is powered by Hiya, AT&T’s primary spam analytics partner (ActiveArmor engine).
- When enabled, registration propagates across major analytics engines: Hiya, First Orion, and TNS.

## Related pages
- [Number Reputation Quickstart](number-reputation-quickstart.md) — a guided, step-by-step setup
- [Number Reputation Settings](number-reputation-settings.md) — vetting lifecycle, schedules, and configuration
- [Phone Number Reputation](phone-number-reputation.md) — associating numbers and querying reputation in depth
- [Enterprises](enterprises.md) — enterprise resource overview and requirements
