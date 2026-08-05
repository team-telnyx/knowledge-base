---
title: Branded Calling
summary: 'Branded Calling is a Telnyx product (currently in beta, US-only) that displays
  a verified business identity — display name, logo, and call reason — on outbound
  calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed
  industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported
  carriers and devices. This page covers the full lifecycle: registering an Enterprise,
  accepting the Branded Calling Terms of Service, activating the product, creating
  and vetting a Display Identity Record (DIR), attaching phone numbers in batches,
  configuring call reasons, handling infringement claims, and pricing.'
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
updated_at: 2026-08-05T13:39:22Z
---

# Branded Calling

*Part 2 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx product (currently in beta, US-only) that displays a verified business identity — display name, logo, and call reason — on outbound calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported carriers and devices. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, handling infringement claims, and pricing.

## Enterprises

An **Enterprise** represents your business entity on the Telnyx platform. It's the top-level resource you must register before you can use Branded Calling to display your verified business identity (display name, logo, call reason) on outbound calls.

### Required fields

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

### Create an enterprise

```
curl -X POST https://api.telnyx.com/v2/enterprises \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "legal_name": "Acme Plumbing LLC",
    "doing_business_as": "Acme Plumbing",
    "organization_type": "commercial",
    "organization_legal_type": "llc",
    "country_code": "US",
    "role_type": "enterprise",
    "jurisdiction_of_incorporation": "Delaware",
    "website": "https://acmeplumbing.example.com",
    "fein": "12-3456789",
    "industry": "technology",
    "number_of_employees": "51-200",
    "organization_contact": {
      "first_name": "Sam",
      "last_name": "Owner",
      "email": "sam@acmeplumbing.example.com",
      "job_title": "Compliance Lead",
      "phone_number": "+13125550000"
    },
    "billing_contact": {
      "first_name": "Alex",
      "last_name": "Bill",
      "email": "billing@acmeplumbing.example.com",
      "phone_number": "+13125550001"
    },
    "organization_physical_address": {
      "country": "US",
      "administrative_area": "IL",
      "city": "Chicago",
      "postal_code": "60601",
      "street_address": "100 Main St"
    },
    "billing_address": {
      "country": "US",
      "administrative_area": "IL",
      "city": "Chicago",
      "postal_code": "60601",
      "street_address": "100 Main St"
    }
  }'
```

The response includes an `id`; use this enterprise ID for all subsequent API calls.

### Activate Branded Calling on the enterprise

Branded Calling is a paid product that must be explicitly activated per enterprise. Without this step, DIR creation returns `400` with `code=10015` and a `detail` pointing back to this endpoint.

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/branded_calling \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The HTTP response returns with the enterprise body. Activation completes asynchronously; if DIR creation returns `400` right after activation, wait a moment and retry. Both endpoints are idempotent. A `403` here means the Branded Calling Terms of Service hasn't been accepted yet.

Activating Branded Calling is **billable**. See [Branded Calling pricing](https://telnyx.com/pricing/branded-calling).

### Reusing the enterprise

Register the enterprise once and reuse it for all of your Branded Calling work. The API collects all required fields up front so you don't need to update them later.
