---
title: Telnyx Reporting
summary: Telnyx reporting combines the v2 Usage Reports API for aggregated usage data,
  the Session Analysis API for tree-based per-session cost and event inspection, and
  On-Demand Reports for natural-language queries against the same usage data.
sources:
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis/index
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
updated_at: 2026-07-17T09:16:44Z
---

# Telnyx Reporting

*Part 2 of 4 — see also: [Part 1](telnyx-reporting--part-1.md), [Part 3](telnyx-reporting--part-3.md), [Part 4](telnyx-reporting--part-4.md)*

Telnyx reporting combines the v2 Usage Reports API for aggregated usage data, the Session Analysis API for tree-based per-session cost and event inspection, and On-Demand Reports for natural-language queries against the same usage data.

## Usage Reports API

The v2 Usage Reports API exposes aggregated usage data through a single endpoint. It is designed to be flexible and customizable so that you can view data in a way that fits your business and use cases.

### Query Requirements

#### Products

A product must be included in every query. There is no way to view usage for all or multiple products in a single request. Supported products include:

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

The `start_date` and `end_date` parameters use the format `YYYY-MM-DDThh:mm:ssTZD` (for example, `2022-12-24T19:20:30-05:00`). Including the timezone offset lets you specify the timespan in your local time. `start_date` is inclusive and `end_date` is exclusive — to get all of February, use `start_date=2023-02-01T00:00:00-00:00` and `end_date=2023-03-01T00:00:00-00:00`. Billing usage is calculated in UTC. The maximum supported range is 31 days.

You can also use date literals (see the [date literals reference](https://developers.telnyx.com/api#date-literals)) by replacing `start_date` and `end_date` with `date_range`, for example `date_range=last_1_weeks`.

To break data out by day, use the `date` dimension (available on all products). For hourly breakdowns, use the `date_time` dimension.

#### Format

The endpoint returns JSON by default. You can request a CSV file by adding `format=csv` to the query.

### Dimensions and Metrics Options

Metrics are the values you want to measure (for example, number of calls attempted or total cost). Dimensions are how you want the data broken out (for example, by connection, messaging profile, or direction).

To see the dimensions and metrics available for a product, call the options endpoint. Pass the `product` parameter to scope the response to a single product, or omit it to see all products.

```
curl --location 'https://api.telnyx.com/v2/usage_reports/options?product=sip-trunking' \
--header 'Authorization: Bearer YOUR_API_KEY
```

Sample response for SIP Trunking:

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

**Example 1: Simple SIP report.** Get total calls connected vs. attempted and total cost for the week of January 23rd, broken out by direction and destination country, outbound only.

| Requirement | Query parameter |
| --- | --- |
| Product: sip-trunking | `product=sip-trunking` |
| Dates: January 23–28, 2024 | `start_date=2024-01-23T00:00:00-00:00 end_date=2024-01-29T00:00:00-00:00` |
| Metrics: connected, attempted, cost | `metrics=connected,attempted,cost` |
| Break out by destination country (must include direction when filtering on it) | `dimensions=country_code,direction` |
| Outbound only | `filter[direction]=outbound` |
| Pagination | `page[number]=1 page[size]=20` |

```
curl --location --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-23T00:00:00-00:00&end_date=2024-01-29T00:00:00-00:00&metrics=connected,attempted,cost&dimensions=direction,country_code&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

The response shows that during the week in question, the account only had traffic to the US (country code `1`), with 883,930 connected vs. 1,245,811 attempted calls and a total cost of 1911.624. Add `dimensions=currency` to also receive the currency.

**Example 2: Short duration calls.** Telnyx applies automatic surcharges when short duration calls (greater than 0 and at most 6 seconds) make up 15% or more of outbound traffic. A dedicated metric is exposed for this calculation.

| Requirement | Query parameter |
| --- | --- |
| Product: sip-trunking | `product=sip-trunking` |
| Dates: January 2024 | `start_date=2024-01-01T00:00:00-00:00 end_date=2024-02-01T00:00:00-00:00` |
| Metrics: completed | `metrics=completed` |
| Break out by SDC (must include direction when filtering on it) | `dimensions=short_duration_call,direction` |
| Outbound only | `filter[direction]=outbound` |
| Pagination | `page[number]=1 page[size]=20` |

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&metrics=completed&dimensions=direction,short_duration_call&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

From the response, the percentage of traffic that is short duration is `414515 / (414515 + 522094) = 44%`. Add `connection_id` to the dimensions list to see which connections are the biggest offenders.

#### Messaging

**Example 1: Simple messaging report.** View messaging usage for a single day, broken out by carrier.

| Requirement | Query parameter |
| --- | --- |
| Product: messaging | `product=messaging` |
| Dates: today | `date_range=today` |
| Metrics: cost, count, parts | `metrics=cost,count,parts` |
| Break out by carrier (must include direction when filtering on it) | `dimensions=short_duration_call,direction` |
| Outbound only | `filter[direction]=outbound` |
| Pagination | `page[number]=1 page[size]=20` |

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?product=messaging&dimensions=direction,normalized_carrier&metrics=cost,parts,count&date_range=today&filter[direction]=outbound&page[number]=1&page[size]=20' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```

**Example 2: Alphanumeric by MNC/MCC.** A monthly messaging report of alphanumeric traffic per country, broken out by MCC (Mobile Country Code) and MNC (Mobile Network Code).

| Requirement | Query parameter |
| --- | --- |
| Product: messaging | `product=messaging` |
| Dates: January 2024 | `start_date=2024-01-01T00:00:00-00:00 end_date=2024-02-01T00:00:00-00:00` |
| Metrics: cost, parts | `metrics=cost,parts` |
| Dimensions: mcc, mnc, country, status_v2 | `dimensions=direction,mcc,mnc,country_iso,product_name,status_v2` |
| Filters: alphanumeric, outbound, billable statuses only | `filter[product_name]=alphanumeric_id filter[direction]=outbound filter[status_v2]=delivered filter[status_v2]=delivery_failed filter[status_v2]=delivery_unconfirmed` |

```
curl --location -g --request GET 'https://api.telnyx.com/v2/usage_reports?start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&product=messaging&metrics=parts,cost&dimensions=direction,mcc,mnc,country_iso,product_name,status_v2&filter[product_name]=alphanumeric_id&filter[direction]=outbound&filter[status_v2]=delivered&filter[status_v2]=delivery_failed&filter[status_v2]=delivery_unconfirmed' \
--header 'Authorization: Bearer YOUR_TELNYX_KEY'
```
