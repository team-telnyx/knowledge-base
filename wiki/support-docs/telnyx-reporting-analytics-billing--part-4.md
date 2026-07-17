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

*Part 4 of 5 — see also: [Part 1](telnyx-reporting-analytics-billing--part-1.md), [Part 2](telnyx-reporting-analytics-billing--part-2.md), [Part 3](telnyx-reporting-analytics-billing--part-3.md), [Part 5](telnyx-reporting-analytics-billing--part-5.md)*

This page consolidates Telnyx's reporting, analytics, and billing-related documentation, covering the Mission Control Portal Reporting section (Detail Records, Usage Reports, Monthly Charges, Message Deliverability, Outbound Declined Calls, and On-Demand Reports), per-product detail records (MDRs for SMS, WDRs for Wireless), real-time dashboards, Calls Per Second (CPS) limits and surcharges, short duration call penalties, abandoned call surcharges, post dial delay, and the Telnyx Status Page.

## Calls Per Second (CPS) Surcharge

Telnyx uses CPS in two related but separate ways: real-time Outbound CPS limits (which protect the network by limiting excessive outbound SIP call attempts in real time) and the monthly Outbound Peak CPS surcharge (which applies charges for sustained or recurring high outbound CPS usage based on the customer's monthly 95th percentile peak CPS value).

### Real-Time Outbound CPS Limits

Real-time Outbound CPS limits are applied by traffic source, not by account. Standard SIP Trunking traffic is limited to 20 CPS per source IP address or SIP username by default. Traffic exceeding the applicable limit is rejected with SIP response code 503 CPS Limit Reached (P05). Calls rejected because they exceed the real-time CPS limit are not included in the Monthly Outbound Peak CPS surcharge calculation.

### Monthly Outbound Peak CPS Surcharge

The Monthly Outbound Peak CPS surcharge is calculated independently of the real-time CPS limits. It is based only on outbound SIP Trunking call attempts that were accepted, and is measured at the account level, not by IP address or SIP username.

The Monthly Outbound Peak CPS represents the highest number of outbound SIP Trunking call attempts initiated during the same second throughout the month, as derived from SIP Trunking CDRs. The following traffic is excluded from the surcharge calculation:

- Programmable Voice / Call Control traffic
- Telnyx internal retry attempts
- SIP Trunking attempts blocked by CPS limits

### Monitoring Outbound CPS Usage

The Mission Control Portal includes an Outbound Peak Calls Per Second (CPS) dashboard to help monitor traffic patterns. The dashboard displays outbound peak call attempts over time, making it easier to identify high-CPS bursts and determine when they occur. Monitoring outbound CPS usage can help distribute traffic more evenly throughout the day, reducing the likelihood of real-time CPS rejections or a higher monthly CPS Peak surcharge.

### How Monthly CPS Peak Usage Is Measured

For each active hour during the billing month, Telnyx identifies the highest outbound SIP Trunking CPS value recorded within that hour. These hourly peak values form the dataset used to calculate the monthly CPS Peak. Hours with no outbound SIP Trunking call attempts are excluded from the calculation rather than being counted as 0 CPS.

The monthly CPS Peak surcharge is based on the 95th percentile of the active hourly peak CPS values. This approach reflects sustained or recurring periods of high outbound CPS usage, rather than a single exceptional burst or the customer's average CPS throughout the month.

### How Telnyx Calculates the CPS Peak Value

1. For each active hour, determine the highest outbound CPS value recorded during that hour.
2. Exclude hours with no outbound CPS activity.
3. Calculate the 95th percentile of the remaining hourly peak CPS values.
4. Use the resulting 95th percentile CPS value to calculate the monthly surcharge.

For example, if a customer has 100 active hours in a month and only 5 hours contain unusually high CPS peaks, those hours are treated as outliers and have little effect on the 95th percentile calculation. If elevated CPS levels occur across many more active hours, the monthly CPS Peak value increases because the pattern represents sustained usage rather than isolated events.

### CPS Peak Pricing Model

CPS Peak surcharges use a graduated pricing model:

- First 5 CPS = free
- Any additional CPS up to 25 = $12/CPS
- Any additional CPS up to 200 = $16/CPS
- Any additional CPS up to 250 = $24/CPS
- Any additional CPS 251+ = $30/CPS

For example, if the monthly 95th percentile peak CPS value is 163, the surcharge is calculated as:

(5 CPS × $0) + (20 CPS × $12) + (138 CPS × $16) = $2,448

### How CPS Surcharges Appear on Invoices

CPS surcharges appear on the monthly invoice as an Outbound Calls-Per-Second Peak Usage Surcharge. The invoice line item is based on the monthly 95th percentile outbound peak CPS value for SIP Trunking traffic.

## Short Duration Calls

Short Duration Calls (SDCs) are outbound calls that are 6 seconds or less in duration. Telnyx allows 15% of traffic to be SDCs on the platform. If SDC traffic exceeds 15% at any time in the month, an email alert is sent. If the SDC rate is still above 15% at month end, the traffic is penalized with additional charges.

If SDC traffic is above 15% for the calendar month, the penalty applies to all SDCs made that month, not only those above the 15% mark. SDCs are calculated as: count of short duration calls connected / total count of connected calls (which includes the short duration call count). The time-frame is always based in UTC from 00:00:00.

Example:

- Start Date = 23rd January 2023 00:00:00
- End Date = 30th January 2023 00:00:00
- Short Duration Call Count = 200
- Total Connected Call Count = 1000
- 200 / 1000 = 20% of calls considered short duration

As of 1 January 2024, short duration calls to international destinations are also subject to a fee of $0.01 per call where more than 15% of total traffic is short duration. Telnyx does not support use cases that require Short Duration calls through its network.

### Locating the Origin of Short Duration Calls

To locate the origin of SDCs within traffic:

1. Download a detail report for the desired time-frame from the detailed-records page, filtering outbound calls only.
2. Sort the generated CSV file based on the call duration column.
3. Remove any rows of calls with a duration of 0 seconds.
4. Calculate how many calls were less than or equal to 6 seconds in duration.
5. Check the column with the SIP connection name to see which one shows up often to determine the source of the short duration traffic.
