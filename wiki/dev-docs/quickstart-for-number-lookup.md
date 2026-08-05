---
title: Quickstart for Number Lookup
summary: Number Lookup is a Telnyx API service that retrieves information about a
  phone number, including carrier name, line type (landline, mobile, VoIP), caller
  name, and portability details. This quickstart demonstrates how to perform a basic
  lookup and how to request optional carrier and caller-name data using cURL, Python,
  Node, and Ruby.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
updated_at: 2026-08-05T13:43:06Z
---

# Quickstart for Number Lookup

Number Lookup is a Telnyx API service that retrieves information about a phone number, including carrier name, line type (landline, mobile, VoIP), caller name, and portability details. This quickstart demonstrates how to perform a basic lookup and how to request optional carrier and caller-name data using cURL, Python, Node, and Ruby.

## Overview

Number Lookup is a service offered by the Telnyx SDK that allows you to [look up a phone number](https://telnyx.com/number-lookup) and retrieve information such as:

- Carrier name
- Type of phone (landline, mobile, VoIP, etc.)
- Name and business associated with the number

The API always returns the same response object, but if the `carrier` and `caller-name` options are not requested, those fields will be `null`.

## Response fields

A typical Number Lookup response looks like this:

```json
{
  "data": {
    "caller_name": {
      "caller_name": "TELNYX LLC",
      "error_code": "10001"
    },
    "carrier": {
      "error_code": null,
      "mobile_country_code": "US",
      "mobile_network_code": 866,
      "name": "Telnyx/4",
      "type": "voip"
    },
    "country_code": "US",
    "fraud": null,
    "national_format": "(0312) 945-7420",
    "phone_number": "+13129457420",
    "portability": {
      "altspid": "073H",
      "altspid_carrier_name": "Telnyx/4",
      "altspid_carrier_type": "3",
      "city": "WAUKEGAN",
      "line_type": "voip",
      "lrn": "2245701999",
      "ocn": "073H",
      "ported_date": "2017-10-20",
      "ported_status": "Y",
      "spid": "073H",
      "spid_carrier_name": "Telnyx/4",
      "spid_carrier_type": "3",
      "state": "Illinois"
    },
    "record_type": "number_lookup"
  }
}
```

Key fields include:

- `national_format` — the number formatted in national style.
- `portability.city` and `portability.state` — the geographic location associated with the number.
- `portability.ported_status` and `portability.ported_date` — whether and when the number was ported.
- `portability.lrn` — the Local Routing Number.
- `carrier.name` and `carrier.type` — the serving carrier and line type.
- `caller_name.caller_name` — the CNAM (caller name) record, when available.

## cURL

### Basic number lookup

Replace `YOUR_API_KEY` with your Telnyx API key.

```bash
curl -X GET \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --globoff "https://api.telnyx.com/v2/number_lookup/+18665552368"
```

### Retrieving caller name and carrier

Append the `carrier` and `caller-name` query parameters to populate those fields in the response:

```bash
curl -X GET \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --globoff "https://api.telnyx.com/v2/number_lookup/+18665552368?carrier&caller-name"
```

## Python

### Basic number lookup

```python
import telnyx
telnyx.api_key = "YOUR_API_KEY"
telnyx.NumberLookup.retrieve("+13129457420")
```

### Retrieving caller name and carrier

Pass the `type` option with both `caller-name` and `carrier` to populate those fields in the response.

## Node

### Basic number lookup

```javascript
import Telnyx from 'telnyx';

const telnyx = new Telnyx("YOUR_API_KEY");

// In Node 10
const { data: numberInfo } = await telnyx.numberLookup.retrieve(
  '+18665552368'
);

// In other environments
telnyx.numberLookup.retrieve(
  '+18665552368'
).then(function(response){
  const numberInfo = response.data; // asynchronously handled
});
```

### Retrieving caller name and carrier

```javascript
import Telnyx from 'telnyx';

const telnyx = new Telnyx("YOUR_API_KEY");

// In Node 10
const { data: numberInfo } = await telnyx.numberLookup.retrieve(
  '+18665552368',
  {
    type: ["caller-name", "carrier"]
  }
);

// In other environments
telnyx.numberLookup.retrieve(
  '+18665552368',
  {
    type: ["caller-name", "carrier"]
  }
).then(function(response){
  const numberInfo = response.data; // asynchronously handled
});
```

## Ruby

### Basic number lookup

```ruby
require "telnyx"
Telnyx.api_key = "YOUR_API_KEY"

Telnyx::NumberLookup.retrieve('+12624755500')
```

### Retrieving caller name and carrier

Pass the `type` option with both `caller-name` and `carrier` to populate those fields in the response.
