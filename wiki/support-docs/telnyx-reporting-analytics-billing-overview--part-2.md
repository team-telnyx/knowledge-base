---
title: Telnyx Reporting, Analytics & Billing Overview
summary: This page consolidates Telnyx Mission Control Portal reporting, analytics,
  and billing resources, covering detail records (CDR/MDR/WDR), usage and monthly
  charge reports, real-time dashboards, message deliverability, invoices, configuration
  propagation, and related features such as real-time transcription and feature requests.
sources:
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
updated_at: 2026-08-05T13:27:35Z
---

# Telnyx Reporting, Analytics & Billing Overview

*Part 2 of 4 — see also: [Part 1](telnyx-reporting-analytics-billing-overview--part-1.md), [Part 3](telnyx-reporting-analytics-billing-overview--part-3.md), [Part 4](telnyx-reporting-analytics-billing-overview--part-4.md)*

This page consolidates Telnyx Mission Control Portal reporting, analytics, and billing resources, covering detail records (CDR/MDR/WDR), usage and monthly charge reports, real-time dashboards, message deliverability, invoices, configuration propagation, and related features such as real-time transcription and feature requests.

## Telnyx Dashboards

The Telnyx Dashboard provides real-time voice and SMS analytics. Access it via the Dashboard icon in the top-right corner of the portal, or directly at the [Dashboard page](https://portal.telnyx.com/#/reports/dashboard). Calling information represents **conversational** calls only; high-volume short-duration calling is not captured.

The dashboard provides a comprehensive overview of:

- Voice: Number of Calls
- SMS: Number of Messages
- Voice: Connection Rate
- Voice: Max Concurrent Calls
- Voice: Outbound Peak Calls Per Second (CPS)
- Voice: Peak Inbound Concurrent Channel
- Abandoned Calls Percentage
- Messaging: Usage and Spend per Country

It also captures live data for Active Calls (Inbound & Outbound) and Numbers Ported (In Queue & Ported Successfully). Charts can be adjusted for 24-hour, 7-day, or 30-day projections via a drop-down on each chart.

### Voice: Number of Calls

Shows the number of inbound and outbound calls over the selected time frame.

### Voice: Connection Rate

Shows the percentage of inbound and outbound calls that were connected out of all attempted calls.

### Voice: Max Concurrent Calls

Shows the total number, as well as individual inbound and outbound concurrent calls, made from the account.

### SMS: Number of Messages

Shows the total number of inbound and outbound SMS received or sent from the account. The chart can be filtered by SMS type: All, Long-Code, Short-Code, or Toll-Free.

### Active Calls: Inbound & Outbound

Shows the active number of inbound and outbound calls in real time, updated every few seconds.

### Numbers Ported: In Queue & Ported Successfully

- **In Queue** – Numbers that entered the porting queue in the selected time period and are still in the queue.
- **Ported Successfully** – Numbers that entered the porting queue in the selected time period and were ported in successfully.

### Outbound Peak Calls Per Second (CPS)

Displays the peak number of outbound calls per second over the last 30 days. Applies to SIP Trunking services only.

### Peak Inbound Concurrent Channels

Illustrates the peak number of concurrent inbound channels for different zones (Zone A, Zone B, Zone C, Zone US) over the last 30 days.

### Abandoned Calls Percentage

Provides an at-a-glance view of abandoned traffic percentages, helping to pinpoint problematic trends and take corrective action.

### Messaging: Usage and Spend per Country

The [Messaging Dashboard](https://portal.telnyx.com/#/messaging/reports/dashboard) displays usage and spend by country. Countries can be toggled by clicking their respective key in the chart legend.

## SMS MDR (Message Detail Record) Report Log

For every sent or received SMS, an MDR (message detail record) is written. MDRs can be accessed and generated under **Reports → Reporting** in the Mission Control Portal.

MDRs are stored as JSON objects. The most important fields include the embedded **body** object, which contains additional fields. For privacy reasons, a message's body text is only stored for up to 10 days before being wiped from the system; after that, hash fields can be used to identify messages.

### Status

For **sent messages**, the MDR carries a status value indicating the delivery state. For received messages, a separate set of status values applies. The `delivery_status` field provides further details about the delivery confirmation (outbound) or delivery attempt (inbound).

### Message Coding

The `coding` field is an integer representing the message's encoding. When sending messages, the encoding is determined by the characters in the message body: GSM 7-bit is used when possible, otherwise UTF-16 is used.

### Message Parts

Long messages must be divided into parts for transmission. The size of each part depends on the encoding. For outbound messages, there is a maximum message size of 10 parts.

Billing is based on the number of message parts:

- `rate` = price per message + carrier fee for one part.
- `cost` = rate × message parts.

Billing and rate limiting are applied based on the number of parts per message.

## SIM Reporting & Analytics (WDRs)

WDR stands for wireless detail record and represents a single data session from a SIM card. WDR reports can be pulled from the Reporting section of the portal, similar to MDRs (messaging) or CDRs (voice).

### CSV Report

Reports can be downloaded as a CSV and include:

- **Record Opening Time (UTC)** – Time the related session was opened.
- **Telephone Number** – Telephone number tied to the Telnyx SIM card.
- **Downlink Data (MB)** – Amount of data downloaded in the session.
- **Uplink Data (MB)** – Amount of data uploaded in the session.
- **SIM Card ID** – UUID for the SIM card resource.
- **SIM Group ID** – UUID for the SIM group resource.
- **Data Plan ID** – UUID for the related data plan resource (used only for specific customer use cases).
- **Mobile Country Code (MCC)** – Unique code identifying the country where the SIM was used.
- **Mobile Network Code (MNC)** – Unique code identifying the carrier the SIM was connected to.
- **International Mobile Subscriber Identity (IMSI)** – Identifies the user on the network, similar to a MAC address.
- **SIM Card Tags** – Comma-separated list of associated tags.

### JSON Analytics

Data usage analytics can also be retrieved via the JSON API. The following cURL command returns a paginated response with a single record per WDR:

```
curl --request GET \
  --url https://api.telnyx.com/v2/wireless/detail/records/reports/{id} \
  --header 'Authorization: Bearer <token>'
```

This command returns all session information from yesterday for active SIM cards. The response includes:

- `closed_at` – Datetime the session was closed.
- `created_at` – Datetime the session was started.
- `currency` – Billing currency.
- `data_cost` – Total cost of the data in this session.
- `data_rate` – Unit price for each MB in this session.
- `data_unit` – Unit of measurement (nearly always MB).
- `downlink_data` – Amount of data downloaded.
- `id` – UUID for this specific session.
- `imsi` – User identifier on the network.
- `ip_address` – IP address the SIM card had during the session.
- `is_telnyx_billable` – Always true.
- `mcc` – Country code.
- `mnc` – Carrier code.
- `phone_number` – Telephone number tied to the SIM card.
- `record_type` – Always `wireless_detail_record`.
- `sim_card_id` – UUID for the SIM card resource.
- `sim_card_tags` – Comma-separated list of tags.
- `sim_group_id` – UUID for the SIM group resource.
- `sim_group_name` – Name of the related SIM group at the time of the session.
- `uplink_data` – Amount of data uploaded.
