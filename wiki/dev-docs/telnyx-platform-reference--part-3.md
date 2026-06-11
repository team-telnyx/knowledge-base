---
title: Telnyx Platform Reference
summary: A comprehensive reference for the Telnyx platform, covering AI, API, and
  telecom glossaries, the Number Lookup service, and the Telnyx Verify API including
  its quickstart, verification methods, custom templates, DTMF confirmation, webhooks,
  security best practices, and rate limiting for fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/glossary/ai-glossary/index
- url: https://developers.telnyx.com/docs/glossary/api-glossary
- url: https://developers.telnyx.com/docs/glossary/telecom-glossary
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-06-11T10:29:44Z
---

# Telnyx Platform Reference

*Part 3 of 4 — see also: [Part 1](telnyx-platform-reference--part-1.md), [Part 2](telnyx-platform-reference--part-2.md), [Part 4](telnyx-platform-reference--part-4.md)*

A comprehensive reference for the Telnyx platform, covering AI, API, and telecom glossaries, the Number Lookup service, and the Telnyx Verify API including its quickstart, verification methods, custom templates, DTMF confirmation, webhooks, security best practices, and rate limiting for fraud prevention.

## Number Lookup

The Telnyx Number Lookup service lets you query a phone number and retrieve information such as the carrier name, phone type (landline, mobile, VoIP), caller name, and portability details (including city, state, OCN, ported status, and date).

### Basic lookup

A `GET` request to `/v2/number_lookup/{phone_number}` returns the lookup data. You must include a Bearer token in the `Authorization` header.

```bash
curl -X GET \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/number_lookup/+18665552368"
```

The response includes `caller_name`, `carrier` (with `name`, `type`, `mobile_country_code`, `mobile_network_code`), `country_code`, `national_format`, `phone_number`, and a `portability` object with geographic and carrier-switching details.

### Retrieving caller name and carrier

By default, `caller_name` and `carrier` values may be `null`. Append `?carrier&caller-name` query parameters to populate them:

```bash
curl -X GET \
  --header "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/number_lookup/+18665552368?carrier&caller-name"
```

### SDK examples

**Python:**

```python
import telnyx
telnyx.api_key = "YOUR_API_KEY"
telnyx.NumberLookup.retrieve("+13129457420")
```

**Node:**

```javascript
import Telnyx from 'telnyx';
const telnyx = new Telnyx("YOUR_API_KEY");
const { data: numberInfo } = await telnyx.numberLookup.retrieve('+18665552368');
```

**Ruby:**

```ruby
require "telnyx"
Telnyx.api_key = "YOUR_API_KEY"
Telnyx::NumberLookup.retrieve('+12624755500')
```
