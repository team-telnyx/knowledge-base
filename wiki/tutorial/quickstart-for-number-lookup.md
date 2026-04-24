---
title: Quickstart for Number Lookup
summary: Lookup a phone number and retrieve information.
sources:
  - url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
    content_hash: e0dc0457579ed52920f4d890b2431244c0b61d43f272effbcd1d79cbb31071b5
updated_at: 2026-04-10T00:00:00Z
---

# Quickstart for Number Lookup

Lookup a phone number and retrieve information. Start building on Telnyx today.

## Lookup: Carrier and caller name

\| [cURL](#curl) | [Python](#python) | [Node](#node) | [Ruby](#ruby) |

***

## cURL

Number Lookup is a service offered by the Telnyx SDK that allows the user to <a href="https://telnyx.com/number-lookup">look up a phone number</a> and retrieve information regarding that phone number such as:

* Carrier name
* Type of phone (landline, mobile, etc.)
* Name and business associated with the number

### Basic number lookup example

Running the following code will perform a number lookup on the given number parameter.

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
curl -X GET \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --globoff "https://api.telnyx.com/v2/number_lookup/+18665552368"
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The response will look something like this:

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This example shows results for a Telnyx user-owned number. It displays the formatted version of the number in the national-format value. The location of the number can be seen under portability -> city and state. Other useful information such as carrier and caller\_name can be retrieved if available.

### Retrieving caller name and carrier

Users may also specify the type of the request in order to receive information about the carrier and caller-name. Note that the request will always return the same object, however if the caller-name and carrier options are not sent, the return values will be null. An example of adding both these parameters to the request is shown below:

```bash theme={null}
curl -X GET \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --globoff "https://api.telnyx.com/v2/number_lookup/+18665552368?carrier&caller-name"
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Python

Number Lookup is a serviceis a service offered by the Telnyx SDK that allows the user to look up a phone number and retrieve information regarding that phone number such as:

* Carrier name
* Type of phone (landline, mobile, etc.)
* Name and business associated with the number

### Basic number lookup example

Running the following code will perform a number lookup on the given number parameter using Python.

```python theme={null}
import telnyx
telnyx.api_key = "YOUR_API_KEY"
telnyx.NumberLookup.retrieve(“+13129457420”)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The response will look something like this:

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This example shows results for a Telnyx user-owned number. It displays the formatted version of the number in the national-format value. The location of the number can be seen under portability -> city and state.

### Retrieving caller name and carrier

Users may also specify the type of the request in order to receive information about the carrier and caller-name. Note that the request will always return the same object, however if the caller-name and carrier options are not sent, the return values will be null.

## Node

Number Lookup is a serviceoffered by the Telnyx SDK that allows the user to look up a phone number and retrieve information regarding that phone number such as:

* Carrier name
* Type of phone (landline, mobile, etc.)
* Name and business associated with the number

### Basic number lookup example

Running the following code will perform a number lookup on the given number parameter.

```javascript theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The response will look something like this:

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This example shows results for a Telnyx user-owned number. It displays the formatted version of the number in the national-format value. The location of the number can be seen under portability -> city and state. Other useful information such as carrier and caller\_name can be retrieved if available.

### Retrieving caller name and carrier

Users may also specify the type of the request in order to receive information about the carrier and caller-name. Note that the request will always return the same object, however if the caller-name and carrier options are not sent, the return values will be null. An example request for these options is shown below:

```javascript theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Ruby

Number Lookup is a service is a service offered by the Telnyx SDK that allows the user to look up a phone number and retrieve information regarding that phone number such as:

* Carrier name
* Type of phone (landline, mobile, etc.)
* Name and business associated with the number

### Basic number lookup example

Running the following code will perform a number lookup on the given number parameter.

```ruby theme={null}
require "telnyx"
Telnyx.api_key = "YOUR_API_KEY"

Telnyx::NumberLookup.retrieve('+12624755500')
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

The response will look something like this:

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This example shows results for a Telnyx user-owned number. It displays the formatted version of the number in the national-format value. The location of the number can be seen under portability -> city and state. Other useful information such as carrier and caller\_name can be retrieved if available.

### Retrieving caller name and carrier

Users may also specify the type of the request in order to receive information about the carrier and caller-name. Note that the request will always return the same object, however if the caller-name and carrier options are not sent, the return values will be null.


## Related Pages

- [Quickstart for Telnyx Verify](../tutorial/quickstart-for-telnyx-verify.md)
