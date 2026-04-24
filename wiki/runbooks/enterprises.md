---
title: Enterprises
summary: Register your business as an enterprise to use Branded Calling and Number Reputation services.
sources:
  - url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
    content_hash: 3b77c9da4d7692c278f9d951e1b0fd7db938cf59f97b97b5b313b7bf3bed8a73
updated_at: 2026-04-10T00:00:00Z
---

# Enterprises

Register your business as an enterprise to use Branded Calling and Number Reputation services.

## Overview

An **Enterprise** represents your business entity on the Telnyx platform. It's the top-level resource required before you can use Number Reputation or Branded Calling features.

Register your organization once, then opt into either or both products:

* **Number Reputation** — monitor and manage spam reputation of your outbound calling numbers
* **Branded Calling** — display your business name, logo, and call reason on recipients' screens *(coming soon)*

## What you need

To create an enterprise, you'll need:

| Field                           | Description                                  |
| :------------------------------ | :------------------------------------------- |
| `legal_name`                    | Registered legal name (3–64 characters)      |
| `doing_business_as`             | DBA name                                     |
| `organization_type`             | `commercial`, `government`, or `non_profit`  |
| `country_code`                  | ISO 3166-1 alpha-2 (e.g. `US`)               |
| `website`                       | Your business website                        |
| `fein`                          | Federal Employer Identification Number (EIN) |
| `industry`                      | Industry classification                      |
| `organization_physical_address` | Physical business address                    |
| `billing_contact`               | Billing contact information                  |
| `billing_address`               | Billing address                              |

## Quick start

### 1. Accept Terms of Service

Before creating an enterprise, accept the Number Reputation Terms of Service:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### 2. Create an enterprise

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "legal_name": "Acme Corp",
    "doing_business_as": "Acme",
    "organization_type": "commercial",
    "country_code": "US",
    "website": "https://acme.com",
    "fein": "12-3456789",
    "industry": "technology",
    "number_of_employees": "51-200",
    "organization_legal_type": "corporation",
    "organization_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "jane@acme.com",
      "job_title": "CTO",
      "phone": "+12025551234"
    },
    "billing_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "billing@acme.com",
      "phone_number": "+12025551234"
    },
    "organization_physical_address": {
      "country": "US",
      "administrative_area": "CA",
      "city": "San Francisco",
      "postal_code": "94105",
      "street_address": "123 Main St"
    },
    "billing_address": {
      "country": "US",
      "administrative_area": "CA",
      "city": "San Francisco",
      "postal_code": "94105",
      "street_address": "123 Main St"
    }
  }'
```

The response includes an `id` — use this enterprise ID for all subsequent API calls.

### 3. Next steps

* [Enable Number Reputation](https://developers.telnyx.com/docs/branded-calling/number-reputation/overview) for your enterprise to start monitoring phone number spam scores.

## Enterprise and product relationship

The enterprise is a **shared resource** — register once and use it across both Number Reputation and Branded Calling. Fields like `doing_business_as` and `industry` are specifically required by the Number Reputation provider, while fields like `billing_address` are needed for Branded Calling. The API collects everything upfront so you don't need to update later.

## Access requirements

All Branded Calling and Number Reputation endpoints require a **verified** or **enterprise-level** Telnyx account. Trial and standard paid accounts cannot access these features. See [Account Levels and Capabilities](account-levels-and-capabilities.md) for details on upgrading.
