---
title: Telnyx Reporting, Analytics & Billing
summary: This page consolidates Telnyx's reporting, analytics, and billing-related
  documentation, covering the Mission Control Portal Reporting section (Detail Records,
  Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls,
  and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless),
  real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration
  call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status
  Page.
sources:
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
updated_at: 2026-07-17T09:02:33Z
---

# Telnyx Reporting, Analytics & Billing

*Part 1 of 5 — see also: [Part 2](telnyx-reporting-analytics-billing--part-2.md), [Part 3](telnyx-reporting-analytics-billing--part-3.md), [Part 4](telnyx-reporting-analytics-billing--part-4.md), [Part 5](telnyx-reporting-analytics-billing--part-5.md)*

This page consolidates Telnyx's reporting, analytics, and billing-related documentation, covering the Mission Control Portal Reporting section (Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless), real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status Page.

## Reporting Overview

The Telnyx Mission Control Portal provides a comprehensive Reporting section accessible from the left-hand navigation. It contains six primary areas: Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports. The On-Demand Reports feature allows natural-language querying of v2 Usage Report data — for example, "Daily wireless spend for the last 10 days" or "Number of messages by direction as a pie chart" — with the ability to save and re-run queries for a selected relative timespan.

## Detail Records

The Detail Records section is the entry point for generating per-event report logs across Telnyx products. Available report types include Calls, Messaging, Voice API (Call Control), Fax API, Wireless, WebRTC, and Real-Time Transcriptions. Each report type returns different fields and supports different filtering options.

### Available Filters

Beyond specifying a time-frame, the following filters are available to narrow down reports:

- CLI (originating number)
- CLD (destination number)
- Tags (defined at the number for inbound calls or at the outbound voice profile for outbound calls)
- Billing Groups

For managed accounts, the report can be scoped to a specific managed account. Record types include Completed, Incomplete, Errors, or All. Call/message type can be set to Inbound, Outbound, or Both. Reports can also be filtered by a specific connection, application, or messaging profile. The Metadata option exposes 35 different data headers that can be included in the output; all are included by default.

Once options are configured, click **Generate Detailed Report**. The status appears under **Download Report** — a download link indicates the report is ready, while "expired" means the link has lapsed and can be regenerated using the refresh icon. The report row also shows the creation time, the time range covered, and any filters that were applied.

## SMS Message Detail Records (MDRs)

For every sent or received SMS, an MDR (message detail record) is written. MDRs are stored as JSON objects. For privacy reasons, a message's body text is only stored for up to 10 days before it is wiped from the system; after that point, hash fields can be used to identify messages.

### Status Values

For sent messages, the MDR carries a status that reflects the delivery state. For received messages, a separate set of status values applies. The `delivery_status` field provides further detail about the delivery confirmation (outbound) or delivery attempt (inbound).

### Message Coding

The `coding` field is an integer representing the message's encoding. When sending, the encoding is determined by the characters in the message body — GSM 7-bit is used when possible, otherwise UTF-16 is used.

### Message Parts and Billing

Long messages are divided into parts for transmission, and the size of each part depends on the encoding. For outbound messages, the maximum message size is 10 parts. Billing and rate limiting are applied based on the number of parts per message:

- `rate` = price per message + carrier fee for one part
- `cost` = rate × message parts

## Wireless Detail Records (WDRs)

WDRs (wireless detail records) represent a single data session from a SIM card and can be pulled from the same Reporting section used for MDRs and CDRs.

### CSV Report Fields

A WDR CSV report includes the following columns:

- Record Opening Time (UTC) — time the related session was opened
- Telephone Number — number tied to the Telnyx SIM card
- Downlink Data (MB) — amount of data downloaded in the session
- Uplink Data (MB) — amount of data uploaded in the session
- SIM Card ID — UUID for the SIM card resource
- SIM Group ID — UUID for the SIM group resource
- Data Plan ID — UUID for the related data plan resource (used only for specific customer use cases)
- Mobile Country Code (MCC) — unique code identifying the country where the SIM was used
- Mobile Network Code (MNC) — unique code identifying the carrier the SIM was connected to
- International Mobile Subscriber Identity (IMSI) — used to identify the user on the network, similar to a MAC address
- Sim Card Tags — comma-separated list of associated tags

### JSON API

WDR analytics can also be retrieved via the JSON API. The endpoint returns a paginated response with one record per WDR:

```
curl --request GET \
  --url https://api.telnyx.com/v2/wireless/detail/records/reports/{id} \
  --header 'Authorization: Bearer <token>'
```

The response includes `closed_at`, `created_at`, `currency`, `data_cost`, `data_rate`, `data_unit` (nearly always MB), `downlink_data`, `id`, `imsi`, `ip_address`, `is_telnyx_billable` (always true), `mcc`, `mnc`, `phone_number`, `record_type` (always `wireless_detail_record`), `sim_card_id`, `sim_card_tags`, `sim_group_id`, `sim_group_name`, and `uplink_data`.

## Usage Reports

The Usage Reports section allows generation of detailed usage reports across Calls, Messaging, Telco Data, and Real-Time Transcription. Call usage can be broken down by call direction, product, country, and/or connection.

### Product Selection

The Product option defines the Telnyx product being reported on, spanning AI Voice Assistant, Call Control, Media Storage, SIP Trunking, and other available products. The information returned and reporting options differ by product.

Note: Messaging usage is calculated per message part. In a detail request report, the CSV contains one row per message with a column indicating how many parts were associated with that message.

### Timespan

The Timespan options define the report's time range. The Custom option requires a start date and time. The Month option allows specifying a particular month.

### Advanced Filters

Advanced Filters allow aggregation by setting Dimensions, Metrics, and Filters.

## Monthly Charges

The Monthly Charges section generates a report of charges for a selected month and year, available as either a summary or a breakdown by number. Breakdown by number shows only charges and features that pertain to DIDs, such as the Monthly Recurring Charge (MRC) or the MRC charge for CNAM.

The generated table includes Numbers, Features, Additional Services, Credit (Funds Added to Account Balance), Ledger Adjustments, and Ending Balance (all totals combined).

### Number Types

- **Local DIDs** — Numbers identified by an area code in a specific region, used to receive inbound calls without extensions or operators.
- **Vanity DIDs** — Memorable numbers (often spelling a business name or keyword), typically incurring a higher MRC than a local DID.
- **Toll-Free DIDs** — Numbers dialable from anywhere (generally in-country) without long-distance charges to the caller. Telnyx is an independent RespOrg, maintaining toll-free registration in the SMS/800 registry and redundant connections with each toll-free carrier.

### Number Features

Features that may appear on a number include Bundle Pricing, Channels, CNAM, Emergency services, High Definition Voice, Inbound Call Screening, and SMS.

### Additional Services

Additional services that may be charged include Port-Outs, Vanity Port-Outs, and Unregistered E911 Calls.

### Credit

The Credit section reflects funds added to the account balance, including Payments, Promo Code Redemptions, Referral Credit, and Ledger Adjustments (refunds issued when Telnyx has overcharged).
