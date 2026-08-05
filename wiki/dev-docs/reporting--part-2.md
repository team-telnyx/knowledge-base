---
title: Reporting
summary: Telnyx provides several reporting tools for inspecting usage, costs, and
  session-level activity across its products. The Usage Reports API exposes aggregated,
  queryable usage data; Session Analysis reconstructs the full event and cost tree
  for individual sessions (especially AI-powered calls); and On-Demand Reports offers
  a natural-language interface on top of Usage Report data.
sources:
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis/index
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
updated_at: 2026-08-05T14:01:58Z
---

# Reporting

*Part 2 of 4 — see also: [Part 1](reporting--part-1.md), [Part 3](reporting--part-3.md), [Part 4](reporting--part-4.md)*

Telnyx provides several reporting tools for inspecting usage, costs, and session-level activity across its products. The Usage Reports API exposes aggregated, queryable usage data; Session Analysis reconstructs the full event and cost tree for individual sessions (especially AI-powered calls); and On-Demand Reports offers a natural-language interface on top of Usage Report data.

## Usage Reports API

The (v2) Usage Reports API is a single endpoint that returns aggregated usage data across all of a customer's Telnyx products. It is designed to be flexible and customizable so that you can programmatically view data in a way that fits your business and use cases, and integrate it directly with internal systems.

### Query Requirements

#### Products

A product from the Options response must be included. There is no way to view usage for all or multiple products at once. Supported products include:

- Sip-Trunking (`sip-trunking`)
- Messaging (`messaging`)
- Voice API (`call-control`)
- Wireless (`wireless`)
- Cloud Storage (`cloud-storage`)
- Inference (`inference`)
- Verify 2FA (`verify-2fa`)
- Fax API (`fax-api`)
- WebRTC (`webrtc`)
- Calls per Second (`cps`)
- Conference (`conference`)
- Video API (`programmable-video`)
- Call Control Features (`call-control-features`)
- Customer Service Record (`customer-service-record`)
- Media Streaming (`media-streaming`)
- Noise Suppression (`noise-suppression`)
- Text to Speech (`text-to-speech`)
- Speech to Text (`speech-to-text`)
- Recording (`recording`)
- Forking (`forking`)
- Media Storage (`media-storage`)
- Answering Machine Detection (`amd`)

#### Dates

`start_date` and `end_date` use the format `YYYY-MM-DDThh:mm:ssTZD` (for example, `2022-12-24T19:20:30-05:00`), allowing you to specify the timespan in your local time by including the timezone offset. `start_date` is inclusive and `end_date` is exclusive — to get all of February, use `start_date=2023-02-01T00:00:00-00:00` and `end_date=2023-03-01T00:00:00-00:00`. Billing usage is calculated using UTC. The maximum supported range is 31 days.

You can also use date literals (see the [API date literals reference](https://developers.telnyx.com/api#date-literals)) by replacing `start_date` and `end_date` with `date_range`, for example `date_range=last_1_weeks`.

To break out data by day, use the `date` dimension (available on all products). For hourly breakdowns, use the `date_time` dimension.

#### Format

Specifying a format is optional. The endpoint returns JSON by default, and also supports generating a CSV file by passing `format=csv`.

### Dimensions & Metrics Options Per Product

Metrics are the values you want to measure (for example, the number of calls attempted or the total cost of usage). Dimensions are how you want the data broken out (for example, by connection, messaging profile, or traffic direction).

To see the dimensions and metrics available for a product, call the Options endpoint. Pass the `product` parameter to scope the response to a single product, or omit it to see all products.

Request:

```
curl --location 'https://api.telnyx.com/v2/usage_reports/options?product=sip-trunking' \
--header 'Authorization: Bearer YOUR_API_KEY
```

Response (sample for SIP Trunking):

```
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

### Product Examples

#### SIP Trunking

##### Simple SIP Report

To view SIP trunking usage for the week of January 23rd, with totals for calls connected vs. attempted and total cost, broken out by direction and country:

| Requirement | Query parameter |
| --- | --- |
| Product: sip-trunking | `product=sip-trunking` |
| Date(s): January 23rd – 28th 2024 | `start_date=2024-01-23T00:00:00-00:00 end_date=2024-01-29T00:00:00-00:00` |
| Metrics: calls connected, calls attempted, total cost | `metrics=connected,attempted,cost` |
| Broken out by destination country (direction must be included when filtering on it) | `dimensions=country_code,direction` |
| Outbound only | `filter[direction]=outbound` |
| API response page size/number | `page[number]=1 page[size]=20` |

Request:

```
curl --location --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-23T00:00:00-00:00&end_date=2024-01-29T00:00:00-00:00&metrics=connected,attempted,cost&dimensions=direction,country_code&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

Response:

```
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

##### Short Duration Calls

Telnyx enforces automatic surcharges for accounts whose short duration calls (greater than 0 and less than or equal to 6 seconds) total 15% or more of their outbound traffic. A dedicated metric is exposed for this calculation.

| Requirement | Query parameter |
| --- | --- |
| Product: sip-trunking | `product=sip-trunking` |
| Date(s): January 2024 | `start_date=2024-01-01T00:00:00-00:00 end_date=2024-02-01T00:00:00-00:00` |
| Metrics: calls completed | `metrics=completed` |
| Broken out by SDC (direction must be included when filtering on it) | `dimensions=short_duration_call,direction` |
| Outbound only | `filter[direction]=outbound` |
| API response page size/number | `page[number]=1 page[size]=20` |

Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&metrics=completed&dimensions=direction,short_duration_call&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

Response:

```
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

From this response, the percentage of traffic considered short duration is `414515 / (414515 + 522094) = 44%`. Adding `connection_id` to the dimensions list would identify which connections are the biggest offenders.

#### Messaging

##### Simple Messaging Report

A simple request to view Messaging usage for a single day:

| Requirement | Query parameter |
| --- | --- |
| Product: messaging | `product=messaging` |
| Date(s): Today | `date_range=today` |
| Metrics: total cost, total messages sent, total message parts | `metrics=cost,count,parts` |
| Broken out by carrier (direction must be included when filtering on it) | `dimensions=short_duration_call,direction` |
| Outbound only | `filter[direction]=outbound` |
| API response page size/number | `page[number]=1 page[size]=20` |

Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=messaging&dimensions=direction,normalized_carrier&metrics=cost,parts,count&date_range=today&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

Response (abbreviated):

```
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

##### Alphanumeric by MNC/MCC

A monthly Messaging report of Alphanumeric traffic per country, broken out by MCC (Mobile Country Code) and MNC (Mobile Network Code):

| Requirement | Query parameter |
| --- | --- |
| Product: messaging | `product=messaging` |
| Date(s): January 2024 | `start_date=2024-01-01T00:00:00-00:00 end_date=2024-02-01T00:00:00-00:00` |
| Metrics: total cost, total message parts | `metrics=cost,parts` |
| Dimensions: mcc, mnc, destination country, status_v2 | `dimensions=direction,mcc,mnc,country_iso,product_name,status_v2` |
| Filters: alphanumeric, outbound, billable statuses only | `filter[product_name]=alphanumeric_id filter[direction]=outbound filter[status_v2]=delivered filter[status_v2]=delivery_failed filter[status_v2]=delivery_unconfirmed` |

Request:

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&product=messaging&metrics=parts,cost&dimensions=direction,mcc,mnc,country_iso,product_name,status_v2&filter[product_name]=alphanumeric_id&filter[direction]=outbound&filter[status_v2]=delivered&filter[status_v2]=delivery_failed&filter[status_v2]=delivery_unconfirmed' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

Response (abbreviated):

```
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
