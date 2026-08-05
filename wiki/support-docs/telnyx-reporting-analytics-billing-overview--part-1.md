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

*Part 1 of 4 — see also: [Part 2](telnyx-reporting-analytics-billing-overview--part-2.md), [Part 3](telnyx-reporting-analytics-billing-overview--part-3.md), [Part 4](telnyx-reporting-analytics-billing-overview--part-4.md)*

This page consolidates Telnyx Mission Control Portal reporting, analytics, and billing resources, covering detail records (CDR/MDR/WDR), usage and monthly charge reports, real-time dashboards, message deliverability, invoices, configuration propagation, and related features such as real-time transcription and feature requests.

## Reporting Overview

The Telnyx Mission Control Portal exposes a unified Reporting section that gives customers visibility into calls, messaging, voice API, fax, wireless, WebRTC, and real-time transcription activity. To access it, log in to the [Telnyx portal](https://portal.telnyx.com/) and click **Reporting** in the left-hand navigation. The Reporting section contains six areas:

- **Detail Records** – Calls, Messaging, Voice API (Call Control), Fax API, Wireless, Real-Time Transcriptions, and WebRTC detail requests.
- **Usage Reports** – Detailed usage reports for Calls, Messaging, Telco Data, and Real-Time Transcription, with breakdowns by call direction, product, country, and connection.
- **Monthly Charges** – A monthly report of charges, optionally broken down by number.
- **Message Deliverability** – Messaging usage and overall health of messaging profiles.
- **Outbound Declined Calls** – Telephone numbers with declined/rejected calls (603/608 responses) for reputation management.
- **On-Demand Reports** – Natural-language querying for usage data, generating charts and breakdowns from v2 Usage Report data. Queries can be saved and re-run for a selected relative timespan. Example queries include "Daily wireless spend for the last 10 days", "Number of messages by direction as a pie chart", and "Weekly total calls in February".

## Detail Records

The Detail Records area is the primary place to generate per-event reports. Available report types are Calls, Messaging, Call Control, Fax API, Wireless, WebRTC, and Real-Time Transcriptions. The information returned and the available options differ by report type.

Filters and options include:

- **CLD** – filter by destination number.
- **CLI** – filter by calling number.
- **TAG** – filter by tags applied to DIDs or voice profiles.
- **Billing Groups** – filter by the billing group assigned to DIDs or voice profiles.
- **Start/End Time** – required start date/time; end date defaults to the current time but can be overridden.
- **Record Types** – Complete, Incomplete, Errors, or All.
- **Call/Message Type** – Outbound, Inbound, or Both.
- **Connections/Messaging Profiles** – restrict to specific connections or profiles, or include all.
- **Metadata** – choose from 35 different data headers (all included by default).

After configuring the report, click **Generate Detailed Report**. The status appears under **Download Report**; a download link means the report is ready, while "expired" means the link has lapsed and can be regenerated using the refresh icon. Each report row also shows the creation time, the time range covered, and any filters that were applied.

## Usage Reports

The Usage Reports section is available at the [Usage Reports page](https://portal.telnyx.com/#/app/reporting/usage-reports). It supports products ranging from AI Voice Assistant, Call Control, and Media Storage to SIP Trunking, with the available information and reporting options varying by product.

Key options include:

- **Product** – the Telnyx product the report covers.
- **Timespan** – Custom (specify start date and time) or Month (specify a month to generate the report for).
- **Advanced Filters** – aggregate the report by setting Dimensions, Metrics, and Filters.

Messaging usage is calculated **per message part**. In a detail request report, the CSV contains one row per message and a column indicating how many message parts were associated with that message.

## Monthly Charges

The Monthly Charges report is available at the [Monthly Charges page](https://portal.telnyx.com/#/app/reporting/monthly-charges). The billing cycle for monthly recurring charges (MRC) runs at the start of each new month, and the charges shown have already been deducted from the account balance.

Select a month and year to review, and choose either a **summary** of charges or an individual **breakdown by number**. The breakdown by number shows only charges and features that pertain to DIDs, such as the Monthly Recurring Charge (MRC) or the MRC charge for CNAM.

The generated table includes:

- **Numbers**
- **Features**
- **Additional Services**
- **Credit (Funds Added to Account Balance)**
- **Ledger Adjustments**
- **Ending Balance** (all totals combined)

### Number Types

- **Local DIDs** – Numbers identified by an area code in a specific region (city or state), enabling inbound calls without extensions or operators.
- **Vanity DIDs** – Memorable numbers, often used for marketing, that typically incur a higher MRC than a local DID.
- **Toll-Free DIDs** – Numbers dialable from anywhere (generally in-country) without long-distance charges to the caller. Telnyx is an independent RespOrg, maintaining toll-free registration in the SMS/800 registry and redundant connections with each toll-free carrier.

### Features

Features that may appear on a number include Bundle Pricing, Channels, CNAM, Emergency services, High Definition Voice, Inbound Call Screening, and SMS.

### Additional Services

Additional services that may be charged include Port-Outs, Vanity Port-Outs, and Unregistered E911 Calls.

### Credit (Funds Added to Account Balance)

- **Payments** – Count and total of payments made in the month.
- **Promo Code Redemptions** – Any promo codes redeemed during the period.
- **Referral Credit** – Any referral credit issued by Telnyx.
- **Ledger Adjustments** – Refunds issued to the account balance when Telnyx has overcharged.

The ending balance reflects all totals combined from each section.

## Message Deliverability Dashboard

The [Message Deliverability dashboard](https://portal.telnyx.com/#/app/reporting/messaging-deliverability) provides real-time monitoring and analysis of messaging usage, including visibility into "In-Flight" messages. It can be accessed from **Reports → Reporting → Message Deliverability** in the Mission Control Portal.

Summary headers at the top of the screen display total messages, the average deliverability percentage, and the total of "In-Flight" messages. The time-span selector supports the current day, a specific calendar month, or a custom time-frame.

Available filters:

- **Direction** – Outbound (Inbound functionality is planned for a future release).
- **Type** – All, SMS, MMS.
- **Product** – All, Toll Free, Short Code, Long Code, Alphanumeric.

Click **Apply Filters** to generate the report. The resulting table shows, for each active messaging profile in the selected time period:

- **Deliverability** – Ratio of delivered vs undelivered/failed SMS.
- **Total** – Total SMS for the period.
- **Delivered** – SMS that received a delivery receipt from downstream carriers.
- **Not Delivered** – SMS that failed or did not receive a delivery receipt.
- **Parts** – Total number of parts sent.
- **In-Flight** – Messages sent but not yet acknowledged by downstream carriers.

Click **View Profile** to navigate to a specific messaging profile's configuration page. Note that this dashboard operates in UTC 00:00, while usage reports and other reporting use the local browser time.
