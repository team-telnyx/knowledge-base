---
title: Branded Calling
summary: 'Branded Calling is a Telnyx beta product (US-only) that displays a verified
  business identity (name, logo, call reason) on outbound calls. This page covers
  the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms
  of Service, activating the product, creating and vetting a Display Identity Record
  (DIR), attaching phone numbers in batches, configuring call reasons, and handling
  infringement claims.'
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
- url: https://developers.telnyx.com/docs/branded-calling/overview
- url: https://developers.telnyx.com/docs/branded-calling/pricing
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
updated_at: 2026-07-17T09:13:14Z
---

# Branded Calling

*Part 3 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx beta product (US-only) that displays a verified business identity (name, logo, call reason) on outbound calls. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, and handling infringement claims.

## Enterprises

An **Enterprise** represents your business entity on the Telnyx platform. It's the top-level resource you must register before you can use Branded Calling to display your verified business identity (display name, logo, call reason) on outbound calls.

### Enterprise fields

| Field | Required | Description |
| --- | --- | --- |
| `legal_name` | yes | Registered legal name (3-64 chars). |
| `doing_business_as` | yes | DBA name (max 255 chars). |
| `organization_type` | yes | One of `commercial`, `government`, `non_profit`. |
| `organization_legal_type` | yes | One of `corporation`, `llc`, `partnership`, `nonprofit`, `other`. |
| `country_code` | yes | ISO 3166-1 alpha-2 code. `US` and `CA` are accepted (`CA` applies to Number Reputation). Branded Calling itself is currently US-only. |
| `role_type` | no | One of `enterprise` (registers its own DIRs) or `bpo` (Business Process Outsourcer calling on behalf of others). Defaults to `enterprise`. |
| `jurisdiction_of_incorporation` | yes | State/province/country of registration (e.g. `Delaware`). |
| `website` | yes | Your business website. |
| `fein` | yes | Federal Employer Identification Number (`XX-XXXXXXX` or `XXXXXXXXX`). |
| `industry` | yes | Industry classification. Must be one of a fixed set of values (e.g. `technology`, `healthcare`, `retail`, `finance`, `legal`, `insurance`); an unrecognized value returns `400`. |
| `number_of_employees` | yes | One of `1-10`, `11-50`, `51-200`, `201-500`, `501-2000`, `2001-10000`, `10001+`. |
| `organization_contact` | yes | Object with `first_name`, `last_name`, `email`, `job_title`, `phone_number`. |
| `billing_contact` | yes | Object with `first_name`, `last_name`, `email`, `phone_number`. |
| `organization_physical_address` | yes | Physical business address. |
| `billing_address` | yes | Billing address. |
| `customer_reference` | no | Optional free-form identifier you can attach for your own bookkeeping (max 255 chars). |

Register the enterprise once and reuse it for all of your Branded Calling work. The API collects all required fields up front so you don't need to update them later.

## Terms of Service

You must accept the Branded Calling Terms of Service before activating Branded Calling on any enterprise (`POST /v2/enterprises/{enterprise_id}/branded_calling`); without it, activation returns `403`. Read the full terms at [telnyx.com/terms/branded-calling](https://telnyx.com/terms/branded-calling).

Acceptance is a one-time, idempotent action per user. If Telnyx publishes a new ToS version, you may need to re-accept.

### ToS API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v2/terms_of_service/status` | Check whether the current user has agreed to the current ToS for a product. |
| `POST` | `/v2/terms_of_service/branded_calling/agree` | Agree to the Branded Calling ToS. No body. |
| `GET` | `/v2/terms_of_service/agreements` | List your past agreements (paginated). |
| `GET` | `/v2/terms_of_service/agreements/{agreement_id}` | Get one specific agreement. |

The generic `GET /v2/terms_of_service/status`, `GET /v2/terms_of_service/agreements`, and `GET /v2/terms_of_service/info` endpoints accept a `product_type` query parameter that defaults to `branded_calling`.
