---
title: Telnyx Number Reputation and Enterprises
summary: 'Learn how Enterprises power Telnyx Number Reputation and Branded Calling,
  and how to enable reputation monitoring: accept terms, create an enterprise, upload
  an LOA, configure auto-refresh, register phone numbers, and query spam risk and
  scores.'
sources:
- url: https://developers.telnyx.com/docs/branded-calling/enterprises
  content_hash: 4e88a7b67e15f6425c5a871cdc04906f07d700de64ca0c5eef7bf5cd6c017ea5
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation
  content_hash: 2051de8ada3fe3cd597727f749bcf4e09e7032ca8653967a459ddf62e27399f3
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
  content_hash: 0241db45de4306f7dbad659086b695c089a8b050fa1ddb4e42419d4bc01b8131
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
  content_hash: 619f11e059d1c3daa88e5007b4e305a0b44444c239308b1b6cf3c97fb40ee897
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
  content_hash: f0313a49ba0f7b9138ad6b01e695086ccd836853ad8e0583692656cc7b0b9a37
updated_at: 2026-05-08T13:04:24Z
---

# Telnyx Number Reputation and Enterprises

Learn how Enterprises power Telnyx Number Reputation and Branded Calling, and how to enable reputation monitoring: accept terms, create an enterprise, upload an LOA, configure auto-refresh, register phone numbers, and query spam risk and scores.

## Overview
An Enterprise is your business entity on Telnyx and the shared prerequisite for Number Reputation and Branded Calling. Number Reputation provides real-time spam risk and granular scores for your outbound numbers, powered by Hiya and registered across major analytics engines (Hiya, First Orion, TNS). Branded Calling uses the same Enterprise and will display brand details on recipients’ screens when available.

## Access and prerequisites
- Account level: Verified or enterprise-level accounts only (trial/standard paid are not supported). See [Account Levels and Capabilities](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index).
- API key: Create/manage in the Telnyx Portal.
- At least one US local phone number on your account.
- A signed Letter of Authorization (LOA) for your business.

## Accept Terms of Service
Agree to the Number Reputation terms before any other step: `POST /v2/terms_of_service/number_reputation/agree`.

## Create an enterprise
Create your Enterprise once and reuse it across products. Key fields include:
- legal_name (3–64 chars), doing_business_as, organization_type (`commercial`, `government`, `non_profit`), country_code (ISO 3166-1 alpha-2), website, fein (EIN), industry
- organization_contact (name, email, title, phone)
- organization_physical_address
- billing_contact and billing_address
The response returns an `id` (`enterprise_id`) used in subsequent calls. See [Enterprises](https://developers.telnyx.com/docs/branded-calling/enterprises).

## Upload a Letter of Authorization (LOA)
Upload a signed LOA via the Telnyx Documents API (save the returned `document_id`). The LOA authorizes Telnyx to register your numbers with third-party analytics providers.

## Enable Number Reputation and vetting
Enable monitoring by submitting your LOA: `POST /v2/enterprises/{enterprise_id}/reputation` with `loa_document_id`.
- Vetting typically completes in minutes.
- Check status: `GET /v2/enterprises/{enterprise_id}/reputation`.
- Status lifecycle: `pending → approved` (register/query numbers), `pending → rejected` (inspect `rejection_reasons`), `approved → deleted` (after disabling).
See [Reputation Settings](https://developers.telnyx.com/docs/branded-calling/number-reputation/settings).

## Configure auto-refresh schedules
Telnyx runs fresh queries on your registered numbers per `check_frequency` (billed per number per run):
- business_daily (Mon–Fri, default), daily, weekly, biweekly, monthly, never
Change schedule: `PATCH /v2/enterprises/{enterprise_id}/reputation/frequency` with `check_frequency`.

## Associate phone numbers for monitoring
Register numbers: `POST /v2/enterprises/{enterprise_id}/reputation/numbers` with `phone_numbers`.
- Up to 100 numbers per request; the operation is atomic (all succeed or all fail).
- Numbers must be US local, E.164 format, in service, and belong to your account.
See [Phone Number Reputation](https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers).

## Query reputation data (cached vs fresh)
- Cached (free): `GET /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}` returns the most recent stored data.
- Fresh (billed): add `?fresh=true` to fetch live data from Hiya. If no cached data exists, a fresh query runs automatically.
- List all monitored numbers: `GET /v2/enterprises/{enterprise_id}/reputation/numbers` (supports `page[number]`, `page[size]`).

## Reputation data model and meanings
Each number returns `reputation_data` with:
- spam_risk: `low` (clean), `medium` (some risk), `high` (likely flagged)
- spam_category: label when flagged (e.g., Telemarketer, Survey, Debt Collector, Nonprofit, Political)
- Scores (0–100; `null` means insufficient data):
  - maturity_score (calling history over time)
  - connection_score (answer rates)
  - engagement_score (post-answer retention)
  - sentiment_score (block/report behavior)
- last_refreshed_at: timestamp of the latest fresh result

## Manage numbers and disable monitoring
- Remove a number: `DELETE /v2/enterprises/{enterprise_id}/reputation/numbers/{phone_number}`.
- Disable Number Reputation for the enterprise: `DELETE /v2/enterprises/{enterprise_id}/reputation` (status becomes `deleted` and numbers are de-registered).

## Constraints and limits
- Number format: US local, E.164 only
- Batch size: up to 100 numbers per request (atomic)
- Score range: 0–100; `null` when insufficient data
- Account access: verified or enterprise-level required

## Simplified endpoints for single-enterprise accounts
If your account has only one enterprise, you can omit `enterprise_id`:
- List: `GET /v2/reputation/numbers`
- Get one: `GET /v2/reputation/numbers/{phone_number}`
- Remove: `DELETE /v2/reputation/numbers/{phone_number}`

## Next steps and related docs
- Overview: [Number Reputation](https://developers.telnyx.com/docs/branded-calling/number-reputation)
- Guided setup: [Quickstart](https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart)
- Settings: [Reputation Settings](https://developers.telnyx.com/docs/branded-calling/number-reputation/settings)
- Numbers in depth: [Phone Number Reputation](https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers)
- Enterprise fundamentals: [Enterprises](https://developers.telnyx.com/docs/branded-calling/enterprises)
