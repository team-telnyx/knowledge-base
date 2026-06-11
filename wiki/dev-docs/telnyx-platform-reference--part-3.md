---
title: Telnyx Platform Reference
summary: A comprehensive reference for the Telnyx platform, covering AI, API, and
  telecom glossaries, the Number Lookup service, and the Telnyx Verify API including
  its quickstart, verification methods, custom templates, DTMF confirmation, webhooks,
  security best practices, and rate limiting for fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/glossary/ai-glossary/index
  content_hash: 7a88323f4a713c8e58298daafce9b14d653a74f185c4f7c58f7a2ee1f492be15
- url: https://developers.telnyx.com/docs/glossary/api-glossary
  content_hash: 95e55f121677445e076d3a94687445e427c1f325cee3191c13b1efc56b75310a
- url: https://developers.telnyx.com/docs/glossary/telecom-glossary
  content_hash: 2498ce6f1a3191b62ab4864d776679f05fc5ea49118135f1308f40be2520c82f
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
  content_hash: 87802d596c8ff6ec0fe7dad04a81717723f8bd71b802c6559f2ba5dae36b9c2d
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
  content_hash: 0e2f873503bba841a7e3e977a333e1f6428095c64ccf6ad6bf3ccb2facbdab03
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
  content_hash: 012f00382a6f536741620745424a8626b375dec75a63b293d507ad49507bfbaa
- url: https://developers.telnyx.com/docs/identity/verify/index
  content_hash: 442d1361293b33b1a7246693f7192ebade7d8b0d41449245e64728db7339b55e
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
  content_hash: d9b13cef30b58ef5d5c90894f58c87c2a73c0d19eeb3c5a4f03ba3eb541494d4
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
  content_hash: 43412196dd8c24c7d7d865b29128485094e1f33bb3e1fb34e0a2c0b596f16763
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
  content_hash: e27e6bdcd02aca7679e72ca7370c9e0134a17c5657fd817af2d88e4f032173bb
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
  content_hash: 2566c9d73b33320007839c8312ecff04b03098e738ff18694901b63e39233692
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
