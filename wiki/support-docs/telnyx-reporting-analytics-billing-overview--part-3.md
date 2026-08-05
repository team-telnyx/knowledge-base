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

*Part 3 of 4 — see also: [Part 1](telnyx-reporting-analytics-billing-overview--part-1.md), [Part 2](telnyx-reporting-analytics-billing-overview--part-2.md), [Part 4](telnyx-reporting-analytics-billing-overview--part-4.md)*

This page consolidates Telnyx Mission Control Portal reporting, analytics, and billing resources, covering detail records (CDR/MDR/WDR), usage and monthly charge reports, real-time dashboards, message deliverability, invoices, configuration propagation, and related features such as real-time transcription and feature requests.

## Invoice Overview

Telnyx account invoices are available through the Billing section of the Mission Control Portal under the **Invoices** tab. Navigate via the profile icon in the upper-right corner, then **Manage Billing → Invoices**, or use the [Invoices page](https://portal.telnyx.com/#/app/billing/invoices).

Invoices for the previous month appear during the first few days of the new month and can be sorted by status (Paid, Unpaid). Email notifications for new invoices can be configured at the [Notifications page](https://portal.telnyx.com/#/app/advanced-features/notifications). All prices within the invoice are in USD.

The top of the invoice shows the company name, first and last name, address, the date of issuance, and the time-span it pertains to.

### Summary

The summary section provides a brief overview of the account balance, including total charges, total account top-ups, the balance due at the beginning and end of the month, and convenience fees related to the 3% charge for using credit card or PayPal.

### Numbers Summary

Lists charges pertaining to all owned numbers, including normal and pro-rated Monthly Recurring Charges, One-Time Costs from purchases, and fees for Port-Ins and Port-Outs.

### Existing Features

Lists recurring charges for features enabled before the month of the invoice, such as inbound channels, CNAM, emergency services, and VXCs.

### New Features

Covers the same items as Existing Features, but details any One-Time Charges received upon activation of the features.

### Usage Charges – Voice & Data

Details all incurred costs from voice and data traffic, broken down into quantity, average cost, and total amount charged.

### Usage Charges – Messaging

Details all incurred costs from messaging traffic for the month, broken down by associated countries, with any carrier fees listed.

### Wireless – SIM Cards Summary

Reviews the monthly recurring costs for SIM cards in the account, including the monthly cost for each SIM card and any linked features such as voice services.

### Ledger

Details all changes to the portal balance over the course of the month, with each charge assigned a service name, charge amount, units used, cost code, cost type, transaction type, and timestamp.

### Cost Codes

A CSV list of cost codes and their descriptions (for example, `GLOBAL-CONV-SDC-SURCHARGE`, `GLOBAL-CONV-RATE0-USAGE`, `US-EMERGENCY-UNREGISTERED-RATE0-USAGE`) is attached to the invoice article. For any queries or concerns about invoices or charges, contact [billing@telnyx.com](mailto:billing@telnyx.com).

## Configuration Propagation Delays

When changes are made in the Mission Control Portal or via the Telnyx API, updates must propagate across Telnyx's globally distributed infrastructure. Each change needs to reach all data center instances before becoming fully effective.

Propagation timing:

- **Minimum:** ~1 second
- **Average:** ~1.5 seconds
- **Maximum:** ~3 seconds

This window applies to all configuration updates, including creating or modifying On-Demand SIP Credentials, updating call control settings, modifying connection configurations, and editing messaging profiles or number settings.

Because of this short but unavoidable delay, customers should design workflows with propagation time in mind. For example, creating new SIP credentials and attempting to use them immediately may result in authentication failure until propagation completes. Adding a small delay before first use, or pre-creating credentials ahead of time, avoids potential issues.

## Real-Time Transcription

Real-time transcription converts spoken language into written text as a conversation happens, providing a live written version of the call. It is automated and instantaneous, unlike traditional post-call transcription.

### Key Features

- **Instantaneous** – Text appears nearly simultaneously with the spoken words.
- **Automated** – Powered by advanced speech-to-text algorithms without human intervention.
- **Multi-Functional** – Useful for accessibility, legal compliance, documentation, and data analysis.
- **Accuracy** – Quality varies based on speech clarity, background noise, and the sophistication of the technology.

### Voice API Parameters

- `call_control_id` – Unique ID for controlling the call.
- `client_state` – Adds state of call to webhook.
- `command_id` – Optional ID set arbitrarily.
- `interim_results` – Available only with Google Engine A; returns results more quickly but less accurately.
- `language` – Set language for transcription.
- `transcription_engine` – `A` (Google Transcription Engine, default; supports `interim_results`) or `B` (Telnyx Transcription Engine, more accurate and less costly).
- `transcription_tracks` – Which leg of the call to transcribe: `inbound`, `outbound`, or `both`.

### Product Options

STT is available with the Telnyx Voice API or TeXML. SIP Trunking users must convert to one of the two programmatic voice options to use Speech to Text capabilities.

### Applications

- **AI** – Pass calls to an AI or LLM system to evaluate, summarize, or participate in calls.
- **Voicemail** – Read and share written transcripts of voicemails.
- **Business Meetings** – Provides a written record for later review.
- **Legal Requirements** – Live transcript of important legal proceedings over the phone.
- **Accessibility** – Helps the hearing-impaired fully participate in conversations.
- **Customer Service** – Real-time analytics and quality control.

### Costs

- **Telnyx Engine (B):** $0.025 USD per minute.
- **Google Engine (A):** $0.050 USD per minute.

Up-to-date pricing is available at the [Voice pricing page](https://portal.telnyx.com/#/pricing/voice) under Voice > Speech to Text. The default engine is A (Google) because it supports interim results; engine B (Telnyx) offers significantly better transcription accuracy and lower latency. Select the engine using the `transcription_engine` parameter.

### Automatic Transcription with Call Recording Timeout

If a timeout is set for call recording (the recording stops after a period of silence), Telnyx uses transcription to detect that silence, which automatically triggers Real-Time Transcription even if it was not explicitly enabled. If transcription is triggered by the timeout setting, billing applies. This is useful for voicemail systems that need to track silence length to trigger the stop recording command.

## ElevateAI Proof-of-Concept Setup

This guide walks through integrating Telnyx with ElevateAI for transcription and recording, demonstrating a sample application using Telnyx-Python transcription and recording functionality.

### Step 1: Create a Call Control Application

In the Telnyx Portal, click **Voice → Programmable Voice**, then click **Add new App** in the top-right corner. Enter the application name and webhook URL, then click **Save**.

### Step 2: Purchase a Telnyx Phone Number

Click the **Numbers** tab in the left-side menu, then **Search & Buy Numbers**. Select the search type and region/area code, click **Search Numbers**, choose a number, click **Add to Cart**, then click **Cart** in the top-right corner. Under **Connections or Applications**, select the ElevateAI call control application created in Step 1, then click **Place Order**.

### Step 3: Sign Up for ElevateAI

Navigate to [ElevateAI's website](https://www.elevateai.com/) and click **Get Started**, then **Sign Up**. Fill out the registration form, verify the account, log in, and click **Manage Keys**. Copy the API token for later use.

### Step 4: Clone the PoC Project

Clone the project from the [Telnyx demo repository](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control) and follow the steps in the README.
