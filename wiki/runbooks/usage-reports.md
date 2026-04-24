---
title: Usage Reports
summary: The (v2) Usage Reports API is a single endpoint that enables viewing aggregated usage data across all of a customer's Telnyx products.
sources:
  - url: https://developers.telnyx.com/docs/reporting/usage-reports/index
    content_hash: 6d72abc0d2103dbe55232a08beb2a6e04b56c2b9ef7d79c7bc49d4a5876f83b7
updated_at: 2026-04-10T00:00:00Z
---

# Usage Reports

## Overview

The (v2) Usage Reports API is a single endpoint that enables viewing aggregated usage data across all of a customer's Telnyx products. It is built to be flexible and customizable, so that you have programmatic access to view data in a way that makes sense to your business and use cases. It can be used to efficiently monitor usage trends and costs, as well as to directly integrate with your internal systems.

### Query Requirements

#### Products

A product from the Options response (see next section) must be included. At this time, there is not a way to view usage for all or multiple products at once.

Products Supported:

* Sip-Trunking (sip-trunking)
* Messaging (messaging)
* Voice API (call-control)
* Wireless (wireless)
* Cloud Storage (cloud-storage)
* Inference (inference)
* Verify 2fa (verify-2fa)
* Fax API (fax-api)
* WebRTC (webrtc)
* Calls per Second (cps)
* Conference (conference)
* Video API (programmable-video)
* Call Control Features (call-control-features)
* Customer Service Record (customer-service-record)
* Media Streaming (media-streaming)
* Noise Suppression (noise-suppression)
* Text to Speech (text-to-speech)
* Speech to Text (speech-to-text)
* Recording (recording)
* Forking (forking)
* Media Storage (media-storage)
* Answering Machine Detection (amd)

#### Dates

The start and end date parameters should be in the format `YYYY-MM-DDThh:mm:ssTZD` (eg `2022-12-24T19:20:30-05:00`). This allows you to specify the timespan in your local time by including the timezone offset. The `start_date` parameter is inclusive, while the `end_date` parameter is exclusive - e.g. if you wanted data for all of February, the `start_date` would be `2023-02-01T00:00:00-00:00` and the `end_date` would be `2023-03-01T00:00:00-00:00`. Billing usage is calculated using UTC. The maximum range supported is 31 days.

Another way to specify the timespan you want is to utilize the date literals spelled out in our developer docs - [https://developers.telnyx.com/api#date-literals](https://developers.telnyx.com/api#date-literals). This can be achieved by replacing `start_date` & `end_date` with `date_range` like this: `date_range=last_1_weeks`.

To see the requested data broken out by day for the timespan selected, there is a `date` dimension available on all products. Additionally, there’s a breakout by hour available using the `date_time` dimension.

#### Format

Specifying a format is optional. The endpoint returns JSON by default. At this time, the API also supports generating a CSV file from the response by specifying `format=csv` in your query.

## Dimensions & Metrics Options Per Product

To view the products with their dimensions and metrics available for reporting, you can make a request to the endpoint below.

Metrics are the values you’re interested in, for example, the number of calls attempted or the total cost of your usage. Dimensions are how you want your data broken out, for example, by connection, messaging profile, or the traffic’s direction.

Below, you’ll see a sample of the “Options” response for Sip-Trunking. If you already know the product you want and are looking for only its supported dimensions/metrics, you can pass the product parameter as shown in the example. If you want to see all products, simply leave off the product parameter.

##### Request:

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```
curl --location 'https://api.telnyx.com/v2/usage_reports/options?product=sip-trunking' \
--header 'Authorization: Bearer YOUR_API_KEY
```

##### Response:

```json theme={null}
{
    "data": [
        {
            "product": "sip-trunking",
            "product_dimensions": [
                "date",
                "tn_type",
                "tags",
                "billing_group_id",
                "country_code",
                "outbound_profile_id",
                "source_tn_type",
                "date_time",
                "connection_id",
                "bundle_id",
                "short_duration_call",
                "source_country_code",
                "currency",
                "is_local_calling",
                "call_type",
                "direction"
            ],
            "product_metrics": [
                "connected",
                "cost",
                "attempted",
                "call_sec",
                "completed",
                "billed_sec"
            ],
            "record_types": null
        }
    ]
}
```

## Product Examples

### SIP Trunking

#### Example 1: Simple SIP Report

Let’s say we’re interested in our sip-trunking usage for the week of January 23rd. And let’s say we want to see the total calls connected versus calls attempted and the total cost. And we need these numbers broken out by direction and country. We first make a query to the Options endpoint listed above to make sure those requirements are all supported and to see how to query for them.

These are our requirements shown next to how we’d construct our query for them:

<table>
  <tbody>
    <tr>
      <td>Product: sip-trunking</td>
      <td><code>product=sip-trunking</code></td>
    </tr>

    <tr>
      <td>Date(s): January 23rd - 28th 2024</td>
      <td><code>start\_date=2024-01-23T00:00:00-00:00<br />end\_date=2024-01-29T00:00:00-00:00</code></td>
    </tr>

    <tr>
      <td>Metrics: calls connected, calls attempted, cotal cost</td>
      <td><code>metrics=connected,attempted,cost</code></td>
    </tr>

    <tr>
      <td>Broken out by destination country<br />*Note: Since we’re filtering on the direction, we must include it.*</td>
      <td><code>dimensions=country\_code,direction</code></td>
    </tr>

    <tr>
      <td>Outbound only</td>
      <td><code>filter\[direction]=outbound</code></td>
    </tr>

    <tr>
      <td>API Response’s Page Size/Number</td>
      <td><code>page\[number]=1<br />page\[size]=20</code></td>
    </tr>
  </tbody>
</table>

##### Request:

```
curl --location --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-23T00:00:00-00:00&end_date=2024-01-29T00:00:00-00:00&metrics=connected,attempted,cost&dimensions=direction,country_code&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

##### Response:

From the response below, we can see that during the week in question, our account only had traffic to the US (country code = 1). Our connected versus attempted is 883,930 vs 1,245,811 calls respectively. And the total cost for those outbound calls was 1911.624 (*Note: If you had wanted the currency, that is another dimension that can be added in the query with* `dimensions=currency`).

```json theme={null}
{
  "data": [
    {
       "country_code": "1",
       "direction": "outbound",
       "product": "sip-trunking",
       "connected": 883930.0,
       "cost": 1911.6248,
       "attempted": 1245811.0
    }
  ],
  "meta": {
    "page_size": 20,
    "page_number": 1,
    "total_results": 1,
    "total_pages": 1
  }
}
```

#### Example 2: Short Duration Calls

Telnyx enforces automatic surcharges for customer accounts whose short duration calls (greater than 0 and less than or equal to 6 seconds) total 15% or more of their outbound traffic. As someone running SIP traffic, I may want to know if I’m in danger of receiving the surcharge at the end of the month. We have exposed a metric solely for the purpose of this calculation.

<table>
  <tbody>
    <tr>
      <td>Product: sip-trunking</td>
      <td><code>product=sip-trunking</code></td>
    </tr>

    <tr>
      <td>Date(s): January 2024</td>
      <td><code>start\_date=2024-01-01T00:00:00-00:00<br />end\_date=2024-02-01T00:00:00-00:00</code></td>
    </tr>

    <tr>
      <td>Metrics: calls completed</td>
      <td><code>metrics=completed</code></td>
    </tr>

    <tr>
      <td>Broken out by SDC (short duration call: true or false)<br />*Note: Since we’re filtering on the direction, we must include it.*</td>
      <td><code>dimensions=short\_duration\_call,direction</code></td>
    </tr>

    <tr>
      <td>Outbound only</td>
      <td><code>filter\[direction]=outbound</code></td>
    </tr>

    <tr>
      <td>API Response’s Page Size/Number</td>
      <td><code>page\[number]=1<br />page\[size]=20</code></td>
    </tr>
  </tbody>
</table>

##### Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&metrics=completed&dimensions=direction,short_duration_call&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

##### Response:

From the response below, we can determine the percentage of our traffic that is currently considered short duration: `414515 / (414515 + 522094) = 44%`. If we wanted to take this a step further, we could see which connections are the biggest offenders by adding “connection\_id” to the dimensions list.

```json theme={null}
{
  "data": [
    {
       "short_duration_call": "false",
       "direction": "outbound",
       "product": "sip-trunking",
       "completed": 522094.0
    },
    {
       "short_duration_call": "true",
       "direction": "outbound",
       "product": "sip-trunking",
       "completed": 414515.0
    }
  ]
  ,
  "meta": {
    "page_size": 20,
    "page_number": 1,
    "total_results": 2,
    "total_pages": 1
  }
}
```

### Messaging

#### Example 1: Simple Messaging Report

In this example, we’ll put together a simple request to view our Messaging usage for a single day.

<table>
  <tbody>
    <tr>
      <td>Product: messaging</td>
      <td><code>product=messaging</code></td>
    </tr>

    <tr>
      <td>Date(s): Today</td>
      <td><code>date\_range=today</code></td>
    </tr>

    <tr>
      <td>Metrics: total cost, total messages sent, total message parts</td>
      <td><code>metrics=cost,count,parts</code></td>
    </tr>

    <tr>
      <td>Broken out by Carrier<br />*Note: Since we’re filtering on the direction, we must include it.*</td>
      <td><code>dimensions=short\_duration\_call,direction</code></td>
    </tr>

    <tr>
      <td>Outbound only</td>
      <td><code>filter\[direction]=outbound</code></td>
    </tr>

    <tr>
      <td>API Response’s Page Size/Number</td>
      <td><code>page\[number]=1<br />page\[size]=20</code></td>
    </tr>
  </tbody>
</table>

##### Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=messaging&dimensions=direction,normalized_carrier&metrics=cost,parts,count&date_range=today&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

##### Response (abbreviated):

```json theme={null}
{
  "data": [
    ...
    {
      "normalized_carrier": "AT&T",
      "direction": "outbound",
      "product": "messaging",
      "cost": 132.4653,
      "parts": 33952.0,
      "count": 18088
    },
    {
      "normalized_carrier": "Verizon Wireless",
      "direction": "outbound",
      "product": "messaging",
      "cost": 205.2036,
      "parts": 48924.0,
      "count": 25171
    }
    ...
  ],
  "meta": {
    "page_size": 20,
    "page_number": 1,
    "total_results": 27,
    "total_pages": 2
  }
}
```

#### Example 2: Alphanumeric by MNC/MCC

This example is a little more complex, and lays out a monthly Messaging report of our Alphanumeric traffic per country, broken out by MCC (Mobile Country Code) and MNC (Mobile Network Code).

<table>
  <tbody>
    <tr>
      <td>Product: messaging</td>
      <td><code>product=messaging</code></td>
    </tr>

    <tr>
      <td>Date(s): January 2024</td>
      <td><code>start\_date=2024-01-01T00:00:00-00:00<br />end\_date=2024-02-01T00:00:00-00:00</code></td>
    </tr>

    <tr>
      <td>Metrics: total cost, total message parts</td>
      <td><code>metrics=cost,parts</code></td>
    </tr>

    <tr>
      <td>Dimensions: mcc, mnc, destination country, status\_v2</td>
      <td><code>dimensions=direction,mcc,mnc,country\_iso,product\_name,status\_v2</code></td>
    </tr>

    <tr>
      <td>Filters: alphanumeric, outbound, billable statuses only</td>
      <td><code>filter\[product\_name]=alphanumeric\_id<br />filter\[direction]=outbound<br />filter\[status\_v2]=delivered<br />filter\[status\_v2]=delivery\_failed<br />filter\[status\_v2]=delivery\_unconfirmed</code></td>
    </tr>
  </tbody>
</table>

##### Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&product=messaging&metrics=parts,cost&dimensions=direction,mcc,mnc,country_iso,product_name,status_v2&filter[product_name]=alphanumeric_id&filter[direction]=outbound&filter[status_v2]=delivered&filter[status_v2]=delivery_failed&filter[status_v2]=delivery_unconfirmed' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

##### Response (abbreviated):

```json theme={null}
{
  "data": [
    ...
    {
      "status_v2": "delivered",
      "mnc": "01",
      "mcc": "270",
      "product_name": "alphanumeric_id",
      "country_iso": "LU",
      "direction": "outbound",
      "product": "messaging",
      "cost": 9.519,
      "parts": 167.0
    },
    {
      "status_v2": "delivered",
      "mnc": "01",
      "mcc": "272",
      "product_name": "alphanumeric_id",
      "country_iso": "IE",
      "direction": "outbound",
      "product": "messaging",
      "cost": 659.2542,
      "parts": 18623.0
    },
    ...
  ],
  "meta": {
    "page_size": 20,
    "page_number": 1,
    "total_results": 100,
    "total_pages": 5
  }
}
```
