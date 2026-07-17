---
title: Telnyx Messaging Compliance and Number Types
summary: Comprehensive guide to Telnyx messaging compliance, covering US short code
  ordering and registration, 10DLC use cases and trust scores, ISV requirements, long
  code deliverability, short code keyword and CTA standards, acceptable use policies,
  forbidden messaging categories, supported carriers, and country-specific SMS guidelines
  for Norway, Belize, and the Palestinian Territory.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574037-belize-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679259-palestinian-territory-sms-guidelines
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
updated_at: 2026-07-17T09:00:02Z
---

# Telnyx Messaging Compliance and Number Types

*Part 1 of 4 — see also: [Part 2](telnyx-messaging-compliance-and-number-types--part-2.md), [Part 3](telnyx-messaging-compliance-and-number-types--part-3.md), [Part 4](telnyx-messaging-compliance-and-number-types--part-4.md)*

Comprehensive guide to Telnyx messaging compliance, covering US short code ordering and registration, 10DLC use cases and trust scores, ISV requirements, long code deliverability, short code keyword and CTA standards, acceptable use policies, forbidden messaging categories, supported carriers, and country-specific SMS guidelines for Norway, Belize, and the Palestinian Territory.

## Overview

Telnyx messaging services in the US and Canada operate across three primary number types — 10DLC (long code), toll-free, and short code — each with its own registration, compliance, and throughput framework. This page consolidates the ordering, registration, compliance, and deliverability requirements for these channels, along with country-specific SMS guidelines and prohibited content categories.

## US Short Code Ordering Process

There are two order types for US short codes: ordering a new random or vanity short code, and migrating an existing short code from another provider.

### Ordering a New Random or Vanity Short Code

Three forms must be completed:

1. **Short Code Order Brief** — submitted to the carriers.
2. **Brand Registration Form** — submitted to the Short Code Registry; revetted every 12 months.
3. **Content Provider Registration Form** — submitted to the Short Code Registry (can be the same entity as the brand).

The brand is the perceived sender of messages (e.g., Nike sending texts about shoes), while the content provider is the entity that develops and types the content (e.g., a marketing agency hired by Nike). They can be the same entity.

As part of brand registration, the brand and content provider contacts must complete a verification email from the Short Code Registry, and a third-party vetting is performed. Once the brief is approved and the brand is registered, it takes approximately 6 weeks to obtain final carrier approval, provisioning, and testing. Timelines can vary based on volume and season.

### Migrating an Existing Short Code

To migrate an existing short code:

1. Fill out the Short Code Order Brief.
2. Fill out the Brand and Content Provider Registration Form.
3. Provide a Migration Letter.
4. Provide an LOA (Letter of Authorization).
5. Have the current provider transfer the short code to the Short Code Registry Telnyx account (email shortcode@telnyx.com for the account ID).

After documents are approved, it takes approximately 6 weeks for final carrier approval, testing, and provisioning.

For current forms, contact shortcode@telnyx.com.

## Short Code Brand and Content Provider Registration

The Short Code Registry introduced a mandatory registration process for both new orders and renewals. For new short code orders, the short code cannot be procured until brand and content provider registration is complete. A "parked" short code can be obtained during the process, but it cannot achieve "active" status for messaging until registration is complete.

For Telnyx customers, the following are required:

1. Brand Registration Form
2. Content Provider Form
3. Email verification by the brand contact and content provider contact (verification emails come from certify@aegismobile.com or noreply@usshortcodes.com)

For existing short code renewals, brands that did not complete this process by March 31, 2025 have a 60 calendar day grace period after the first auto-renewal date on or after March 31, 2025 to register. Short codes not updated within this timeframe may be suspended or terminated.

Information on the registration form must match the entity's IRS Form CP-575 (EIN Confirmation letter). Brand vetting and 2FA are redone annually; contact information should be kept current.

## 10DLC Use Cases

Standard 10DLC use cases include:

- **2FA**: Authentication, verification, or one-time passcode messages.
- **Account Notification**: Account-related notifications (password reset, low-balance alerts, suspicious login attempts, transaction alerts).
- **Customer Care**: Account management and customer support interactions.
- **Delivery Notifications**: Status updates on product or service delivery.
- **Fraud Alert Messaging**: Notifications about potential fraudulent account activity.
- **Higher Education**: Messaging on behalf of colleges, universities, school districts, and educational institutions (not for "free to the consumer" messaging).
- **Low Volume Mixed**: For brands with multiple use cases and very low throughput (test/demo accounts, small businesses). Maximum of 5 sub-standard use cases.
- **Machine-to-Machine (M2M)**: Wireless communication between physical assets with no human interaction. Subscriber-facing campaigns prohibited. Dedicated use case.
- **Marketing**: Communications containing marketing or promotional content.
- **Mixed**: For brands with multiple use cases on the same campaign. Minimum 2, maximum 5 sub-use cases.
- **Polling and Voting**: Surveys and polling/voting campaigns.
- **Public Service Announcement**: Informational messaging to raise awareness of important issues.
- **Security Alert**: Notifications that system security has been compromised.

## 10DLC Trust Scores and Throughput

US A2P 10DLC message throughput is determined by Trust Score and Campaign Use Case. Throughput is measured in message segments per second (MPS), with each segment consisting of up to 160 GSM-7 encoded characters. T-Mobile also imposes separate daily message limits toward their subscribers that cannot be exceeded without a special business review.

Trust Scores are assigned when a brand is registered via a reputation algorithm and do not change over time. The algorithm is believed to be primarily determined by brand footprint (larger brands score higher) and the quality/consistency of the brand registration request (fewer discrepancies yield better scores).

Specific campaign use cases also determine MPS. Mixed use campaigns allow reuse of the same phone number but typically incur higher fees than campaigns with specific use cases. Political campaigns must be verified at campaignverify.com, which supplies a token upon successful verification.

Brand registration requests are sent to The Campaign Registry (TCR), the third-party administrator of the carriers' registration system, which assigns the Trust Score.
