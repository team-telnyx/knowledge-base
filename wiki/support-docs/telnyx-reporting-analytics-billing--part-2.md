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

*Part 2 of 5 — see also: [Part 1](telnyx-reporting-analytics-billing--part-1.md), [Part 3](telnyx-reporting-analytics-billing--part-3.md), [Part 4](telnyx-reporting-analytics-billing--part-4.md), [Part 5](telnyx-reporting-analytics-billing--part-5.md)*

This page consolidates Telnyx's reporting, analytics, and billing-related documentation, covering the Mission Control Portal Reporting section (Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless), real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status Page.

## Message Deliverability Dashboard

The Message Deliverability Dashboard provides real-time monitoring and analysis of messaging usage, including visibility into "In-Flight" messages. It is accessible from the Reports drop-down under Reporting, or directly at the messaging-deliverability page.

### Summary Headers

At the top of the screen, summary headers display total messages, average deliverability percentage, and total In-Flight messages.

### Filters

The time-span can range from the current day to a specific calendar month or a custom time-frame. Additional filters include:

- Direction: Outbound (Inbound functionality planned for a future release)
- Type: All, SMS, MMS
- Product: All, Toll Free, Short Code, Long Code, Alphanumeric

### Per-Profile Statistics

Once generated, the report displays the following stats per active messaging profile for the selected period:

- Deliverability — ratio of delivered vs undelivered/failed SMS
- Total — total SMS for the period
- Delivered — total SMS that received a delivery receipt from downstream carriers
- Not Delivered — total SMS that failed or did not receive a delivery receipt
- Parts — total number of parts sent
- In-Flight — messages sent but not yet acknowledged by downstream carriers

Clicking "View Profile" navigates to that messaging profile's configuration page. Note: this dashboard operates in UTC 00:00, while usage reports and other reporting use local browser time.

## Telnyx Dashboards

The Telnyx Dashboard provides real-time voice and SMS analytics, accessible from the Dashboard icon in the top-right corner of the portal. Calling information represents conversational calls only — high-volume short-duration calling is not captured.

### Available Charts

The dashboard provides an overview of:

- Voice: Number of Calls
- SMS: Number of Messages
- Voice: Connection Rate
- Voice: Max Concurrent Calls
- Voice: Outbound Peak Calls Per Second (CPS)
- Voice: Peak Inbound Concurrent Channel
- Abandoned Calls Percentage
- Messaging: Usage and Spend per Country

Live data is also captured for Active Calls (Inbound & Outbound) and Numbers Ported (In Queue & Ported Successfully).

Charts can be dynamically adjusted based on a selected time frame, with options for 24 hours, 7 days, or 30 days.

### Voice: Number of Calls

Shows the number of inbound and outbound calls over the selected time frame.

### Voice: Connection Rate

Shows the percentage of inbound and outbound calls that were connected out of all attempted calls.

### Voice: Max Concurrent Calls

Shows the total number and individual inbound and outbound concurrent calls made from the account.

### SMS: Number of Messages

Shows the total number of inbound and outbound SMS received or sent from the account, with filtering by SMS type (All, Long-Code, Short-Code, Toll-Free).

### Active Calls: Inbound & Outbound

Shows the active number of inbound and outbound calls in real time, updated every few seconds.

### Numbers Ported: In Queue & Ported Successfully

- In Queue — numbers that entered the porting queue in the selected period and are currently in the queue
- Ported Successfully — numbers that entered the porting queue in the selected period and were ported in successfully

### Outbound Peak Calls Per Second (CPS)

Displays the peak number of outbound calls per second over the last 30 days. Applies to SIP Trunking services only.

### Peak Inbound Concurrent Channels

Illustrates the peak number of concurrent inbound channels for different zones (Zone A, Zone B, Zone C, Zone US) over the last 30 days.

### Abandoned Calls Percentage

Provides an at-a-glance view of abandoned traffic percentages to help pinpoint problematic trends.

### Messaging: Usage and Spend per Country

The Messaging Dashboard displays usage and spend by country, with countries toggleable via the chart legend.

## Outbound Declined Calls

The Outbound Declined Calls section lists telephone numbers with declined or rejected calls (603/608 responses) for reputation management.
