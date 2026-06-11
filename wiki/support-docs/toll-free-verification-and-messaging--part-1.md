---
title: Toll-Free Verification and Messaging
summary: Toll-Free numbers on Telnyx require verification before sending outbound
  messages. This page covers the full verification process, form requirements, use
  case selection, opt-in workflows, prohibited content, carrier rejections, and related
  topics such as opt-out handling, webhook notifications, and number porting.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
updated_at: 2026-06-11T11:12:33Z
---

# Toll-Free Verification and Messaging

*Part 1 of 4 — see also: [Part 2](toll-free-verification-and-messaging--part-2.md), [Part 3](toll-free-verification-and-messaging--part-3.md), [Part 4](toll-free-verification-and-messaging--part-4.md)*

Toll-Free numbers on Telnyx require verification before sending outbound messages. This page covers the full verification process, form requirements, use case selection, opt-in workflows, prohibited content, carrier rejections, and related topics such as opt-out handling, webhook notifications, and number porting.

## Overview

Telnyx supports SMS and MMS (US and Canada only) on toll-free numbers. Before sending your first outbound message from a toll-free number, you must submit a verification request. Unverified toll-free numbers are blocked from sending messages — this is an industry-wide requirement enforced since late 2023.

Verification ensures compliance with carrier standards and helps identify the end business, confirming they have proper measures in place to send compliant traffic. Verified traffic benefits from higher throughput and fewer false-positive spam blocks.

## Verification Process and Statuses

Submit a verification request via:

- **Telnyx Portal:** portal.telnyx.com > Real Time Communications > Messaging > Compliance > [Toll Free Verification](https://portal.telnyx.com/#/programmable-messaging/toll-free-messaging) > Submit Verification Request
- **Telnyx API:** [Submit Verification Request](https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request)

Approval timelines are normally **5 business days or less**, though this can vary based on request volume. After submission, the request moves through the following statuses:

| Status | Description |
|---|---|
| **Waiting for Telnyx** | Telnyx reviews the submission for compliance and platform suitability. |
| **Waiting for Customer** | Telnyx has requested changes; the decline reason explains what to fix. |
| **Waiting for Vendor** | Telnyx approved the request; it is now with carriers for final approval. |
| **Rejected** | Either Telnyx or the carriers rejected the request. The decline reason explains why. |
| **Verified** | Both Telnyx and carriers approved the request. You can now send outbound messages. |

**Important:** Submitting a new verification request for an already-verified toll-free number will overwrite the existing verification and leave the number unverified until the new request is approved.

## Verification Form Requirements

### Business Identification

- **Business Name:** Must match the website domain and email domain, or any differences must be explained in the additional information field. The exact legal name must match your EIN/IRS records.
- **DBA:** This is the brand name; it can differ from the legal business name.
- **Corporate Website:** Must include business name, contact information, products/services, about page, contact us page, and privacy/terms page. No "under construction" pages. The website must be publicly accessible (not password-protected or behind a login wall). Social media pages are acceptable but must include business contact details and be established/active.
- **Email Address:** The domain must match the business website. Freemail addresses (e.g., Gmail) can be cause for decline.
- **Business Address:** A valid physical business address.
- **Contact Number:** A contact number for the business — not the toll-free number being verified.
- **Business Contact:** Must be a person's first and last name, not a business name or department.

### Messaging Details

- **Expected Message Volume:** Selected from available dropdown options.
- **Use Case:** The specific purpose for toll-free messaging (e.g., 2FA, marketing, transactional). See the Use Case Selection section below for all options.
- **Description of Use Case / Summary:** Detailed explanation of message types, intended audience, and compliance measures. Must match the opt-in disclosure language.
- **Message Content:** Sample messages for each selected use case. Samples must include your brand name and opt-out language (e.g., "Hi from Acme Corp! Your order is ready. Reply STOP to opt out.").

### Opt-In Workflow and Image

See the Opt-In Workflow and Consent section below for detailed requirements.

### ISV/Reseller Information

If the Telnyx account username domain does not match the business website and email domain, the submission will be placed in "Waiting for Customer" status until the Reseller field is filled out accurately. If the account domain matches the business being registered, leave the Reseller field blank.

### Additional Supporting Details

If submitting more than 5 toll-free numbers in a single request, include a detailed, valid explanation for why multiple numbers are needed. Be specific — for example, list each number with its associated location and purpose. If you run out of characters, host the explanation in a publicly accessible Google Doc, paste the link in the request, and describe the document's contents.

### Privacy Policy and Terms Links

- **Privacy Policy Link:** Must include language stating that SMS opt-in data will not be shared with third parties for marketing purposes.
- **Terms and Conditions Link:** Must contain the services agreement between the customer and the business.

### Opt-In Keyword

This field must be START, YES, BEGIN, or a custom keyword the business uses to restart SMS after a recipient replies STOP.

## Business Registration Number Requirements

As of **February 17, 2026**, the Business Registration Number (BRN) is mandatory for all new toll-free verification submissions. Carriers require a government-issued identifier to align toll-free verification with 10DLC standards.

**Required BRN fields:**

- **Business Registration Number:** U.S. businesses must provide their 9-digit EIN. Canadian businesses must provide their Business Number (BN).
- **Business Registration Type:** EIN, CBN, CRN, NEQ, PROVINCIAL_NUMBER, VAT, ACN, ABN, BRN, SIREN, SIRET, NZBN, UST-IDNR, CIF, NIF, CNPJ, or UID.
- **Legal Entity or Organization Type:** Private Company, Publicly Traded Company, Charity / Non-Profit Organization, Government, or Sole Proprietor.
- **Issuing Country:** The country where the business is legally registered.

If a submission is rejected because the business registration number is missing or invalid, you must attach a screenshot of the official Business Registration form before resubmitting. Do not resubmit without this documentation — email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) instead.

## Use Case Selection

Most verification requests fall into one or more of the primary use cases. If you have more than one use case, or any combination of non-marketing and marketing content, select **Mixed**.

**Primary use cases:**

- **2FA:** One-time codes at login
- **App Notifications:** E.g., "Your password has been reset"
- **Booking Confirmations:** E.g., "Your stay has been booked at the Telnyx Hotel in Denver, CO for Jan 1st, 2028"
- **Conversational / Alerts:** Catch-all for 1-on-1 texting such as customer service
- **Courier Services & Deliveries:** E.g., "Your order has been delivered by FedEx at 12:00pm"
- **Fundraising:** Charity messaging that will solicit donations
- **General Marketing:** Promotions, quotes, or offers to customers
- **Mixed:** Two or more of the other use cases
- **Order Notifications:** E.g., "Your order number is 123456, please pick up at counter 3 in 15 minutes"
- **Political:** Content promoting a political candidate or soliciting political donations
- **System Alerts:** E.g., "Fridge 3 is over the temperature threshold"

**Additional use case options:** Appointments, Auctions, Auto Repair Services, Bank Transfers, Billing, Business Updates, COVID-19 Alerts, Career Training, Chatbot, Emergency Alerts, Events & Planning, Financial Services, Fraud Alerts, General School Updates, HR / Staffing, Healthcare Alerts, Housing Community Updates, Insurance Services, Job Dispatch, Legal Services, Motivational Reminders, Notary Notifications, Public Works, Real Estate Services, Religious Services, Repair and Diagnostics Alerts, Rewards Program, Surveys, Voting Reminders, Waitlist Alerts, Webinar Reminders, Workshop Alerts.

All SMS use cases mentioned on the opt-in form must be reflected in the use case selection and description. Consistency across the entire verification request is required.
