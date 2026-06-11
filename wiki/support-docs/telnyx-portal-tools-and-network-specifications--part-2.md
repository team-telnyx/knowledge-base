---
title: Telnyx Portal Tools and Network Specifications
summary: A comprehensive guide to Telnyx's Mission Control Portal features including
  debugging tools, reporting, dashboards, and network specifications, as well as the
  status page for incident monitoring.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
  content_hash: a7909fd9da64db0f973d0c0fd07d8a5b5b2365631813eccf5fbd43753fbcbc9f
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
  content_hash: 0b3728a9ae0a1f2caf3012c645fb1d9843c2a91f96d795fca3483e82421b7fb8
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
  content_hash: 341002e45148401d2a67a440822b905946718a96fcdce6e8cbce5d54f0914fa3
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
  content_hash: 9fc160f8e420916d6634d100ddbeb777bdee708fb9bacaad7fb44b384e131be1
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
  content_hash: e32513a252b1b8f3385424a74a449d2f6b1ee2a33766af144f26a19aac41c05c
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
  content_hash: 3cdc92b1d0fcaf6c64cb28d6fbdab55332e1e61d8dcd9c50a4a046663a2dc441
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
  content_hash: aa982f42ee65f0f2bed27901d3c4bc26ad9dbe60c3cfa15a10e32de89b87cc48
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
  content_hash: dc72e18b229c4623f5f799236dcd09b145ca7b931283b80cefabda858af78ec0
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
  content_hash: 29d42e44a7140e0a0b1bb3bdabee96aecb26165edf4dcc6ee5d783d62385fa0b
updated_at: 2026-06-11T11:42:46Z
---

# Telnyx Portal Tools and Network Specifications

*Part 2 of 2 — see also: [Part 1](telnyx-portal-tools-and-network-specifications--part-1.md)*

A comprehensive guide to Telnyx's Mission Control Portal features including debugging tools, reporting, dashboards, and network specifications, as well as the status page for incident monitoring.

## Reporting

The Reporting section is accessible from the left-hand navigation in the portal. It contains six sub-sections: Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports.

### Detail Records

The [Detail Records](https://portal.telnyx.com/#/reporting/detailed-records) page lets you generate detailed report logs for the following products:

- Calls
- Messaging
- Voice API (Call Control)
- Fax API
- Wireless
- WebRTC
- Real-Time Transcriptions

**Available filters:**

- **CLI** — originating number
- **CLD** — destination number
- **Tags** — defined at the number (inbound) or outbound voice profile (outbound)
- **Billing Groups** — filter by billing group assigned to DIDs/voice profiles
- **Managed accounts** — select a managed account to report on (if applicable)

**Record types:** Completed, Incomplete, Errors, or All.

**Call/Message type:** Inbound, Outbound, or Both.

**Connections/Messaging Profiles:** Restrict results to specific connections/profiles.

**Metadata:** Customize the data headers returned in the report (35 headers available; all included by default).

After configuring filters and selecting a start/end time, click **Generate Detailed Report**. Reports appear under the Download section; expired downloads can be regenerated via the refresh icon.

### Usage Reports

The [Usage Reports](https://portal.telnyx.com/#/app/reporting/usage-reports) section generates detailed usage reports on Calls, Messaging, Telco Data, and Real-Time Transcription.

- **Product** — Select the Telnyx product (e.g., AI Voice Assistant, Call Control, Media Storage, SIP Trunking, etc.). Information returned varies by product.
- **Timespan** — Choose Custom (specify start/end date) or Month (select a specific month).
- **Advanced Filters** — Aggregate your report with Dimensions, Metrics, and Filters. Call usage reports can be broken down by call direction, product, country, and/or connection.

> **Note:** Messaging usage is calculated **per message part**. In detail request CSV reports, one row represents the message with a column indicating the number of associated message parts.

### Monthly Charges

The [Monthly Charges](https://portal.telnyx.com/#/app/reporting/monthly-charges) report shows your monthly recurring charges (MRC), which are deducted from your account balance at the start of each month.

You can specify the month/year and choose between a **summary** or a **breakdown by number**. The breakdown by number shows charges for DIDs such as MRC and CNAM MRC. The generated report includes:

- **Numbers** — Charges for Local DIDs, Vanity DIDs, and Toll-Free DIDs
- **Features** — Bundle Pricing, Channels, CNAM, Emergency Services, High Definition Voice, Inbound Call Screening, SMS
- **Additional Services** — Port-Outs, Vanity Port-Outs, Unregistered E911 Calls
- **Credit** — Payments, Promo Code Redemptions, Referral Credit
- **Ledger Adjustments** — Refunds issued for overcharges
- **Ending Balance** — Combined total of all sections

### Message Deliverability

The Message Deliverability section shows messaging usage and the overall health of your Messaging Profiles. Traffic can be filtered by:

- **Direction** — Inbound, Outbound
- **Type** — SMS, MMS
- **Product** — Toll Free, Short Code, Long Code, Alphanumeric

### Outbound Declined Calls

View telephone numbers with declined or rejected calls (603/608 SIP responses) for reputation management.

### On-Demand Reports

On-Demand Reports support natural-language querying for usage data. Describe the chart or breakdown you need in plain English and the system generates it from your v2 Usage Report data. You can save queries/visualizations and re-run them for a selected relative timespan.

Example queries:

- "Daily wireless spend for the last 10 days"
- "Number of messages by direction as a pie chart"
- "Weekly total calls in February"

## Dashboards

The [Telnyx Dashboard](https://portal.telnyx.com/#/reports/dashboard) provides real-time and historical analytics for Voice and SMS. Access it via the Dashboard icon in the top-right corner of the portal.

> **Note:** Calling information only represents **conversational** calls. High-volume short-duration calling is not captured.

Charts can be dynamically adjusted for **24 hours, 7 days, or 30 days** time frames.

### Voice Metrics

- **Number of Calls** — Inbound and outbound call counts over the selected time frame
- **Connection Rate** — Percentage of inbound and outbound calls connected out of all attempted
- **Max Concurrent Calls** — Total, inbound, and outbound concurrent calls
- **Outbound Peak CPS** — Peak outbound calls per second (SIP Trunking only) over the last 30 days
- **Peak Inbound Concurrent Channels** — Peak concurrent inbound channels by zone (A, B, C, US) over the last 30 days
- **Abandoned Calls Percentage** — At-a-glance view of abandoned traffic percentages to pinpoint problematic trends

### SMS Metrics

- **Number of Messages** — Total inbound and outbound SMS, filterable by type (All, Long-Code, Short-Code, Toll-Free)
- **Usage and Spend per Country** — Messaging usage and spend broken down by country (countries can be toggled via the chart legend)

### Live Data

- **Active Calls** — Real-time count of inbound and outbound active calls (updated every few seconds)
- **Numbers Ported** — In Queue (numbers currently in the porting queue) and Ported Successfully (numbers that completed porting)

## Status Page

The [Telnyx Status Page](https://status.telnyx.com/) provides real-time updates on incidents and maintenance schedules. You can subscribe to receive updates through multiple channels.

For assistance, refer to Telnyx best practices for contacting the different customer-facing teams.
