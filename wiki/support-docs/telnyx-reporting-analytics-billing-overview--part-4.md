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

*Part 4 of 4 — see also: [Part 1](telnyx-reporting-analytics-billing-overview--part-1.md), [Part 2](telnyx-reporting-analytics-billing-overview--part-2.md), [Part 3](telnyx-reporting-analytics-billing-overview--part-3.md)*

This page consolidates Telnyx Mission Control Portal reporting, analytics, and billing resources, covering detail records (CDR/MDR/WDR), usage and monthly charge reports, real-time dashboards, message deliverability, invoices, configuration propagation, and related features such as real-time transcription and feature requests.

## Obtaining a CSR From Your Carrier

A CSR (Customer Service Record) is a copy of how telephone records appear in the telephone company's database. It contains information about each separate line charge (type of service, federal access charge, number portability charge, calling blocks, 911 charge, etc.) that makes up the monthly service charge.

A CSR also reveals the service location, billing address, additional directory listings, PIC designations, hunting order, charged features and the lines they appear on, calling plans with monthly charges, and taxes applied to each item.

### CSR and Porting

The CSR is important for the porting process. When a port-out request is initiated, the current carrier matches some of the information in the request against the CSR. If enough data matches, the numbers are allowed to port away. Carriers generally match on:

- The name of the business on the account.
- The zip or postal code of the service address (often different from the billing address).
- The account number or BTN/ATN of the account.

Having the CSR handy before starting the porting process is the #1 way to speed up porting. Most delays are caused by submitting incorrect data to Telnyx when initiating the porting process. In some cases Telnyx can obtain a CSR, but carriers are not obligated to release them to other carriers, so it is best to obtain one directly from the current carrier.

### How to Request and Obtain a CSR

Call the customer service or support number for the carrier and clearly state that a copy of the CSR is needed. Most carriers should provide a CSR upon request. Have the CSR sent via email to capture the full details rather than only part of the information over the phone. Once obtained, upload it to the Telnyx Mission Control portal.

### Special Note for Canadian Customers

Canadian telecom carriers are generally not willing to provide CSRs to other carriers.

## Feature Requests

A feature request allows users to request features that are not currently supported in the Mission Control Portal.

### How to Submit a Feature Request

1. Log in to the Telnyx Portal at [portal.telnyx.com](https://portal.telnyx.com/).
2. Click the question mark (?) icon in the far-right corner of the top navigation bar.
3. Select **Feature Request** from the drop-down menu.
4. Click **Submit Idea** in the top-right corner of the page.

The product portal also displays **planned** features, features **being implemented**, and features **under consideration**. Clicking into these features allows selecting one of three options: **Nice-to-have**, **Important**, or **Critical**.

5. Enter the following details and click **Submit** to create the feature request:
   - Feature Request
   - Importance of Feature
   - Email Address

Notification of any further developments is sent via the email entered. Telnyx also has a feedback loop where the support team can tag a case as a feature request, allowing product managers to be notified internally and potentially include the improvement on the public product board.
