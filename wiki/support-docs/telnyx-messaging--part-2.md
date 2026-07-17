---
title: Telnyx Messaging
summary: A consolidated reference for Telnyx programmable messaging covering messaging
  profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification,
  hosted SMS, SMPP setup, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-07-17T09:00:31Z
---

# Telnyx Messaging

*Part 2 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md)*

A consolidated reference for Telnyx programmable messaging covering messaging profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification, hosted SMS, SMPP setup, and third-party integrations.

## Toll-Free Messaging

Telnyx supports SMS on toll-free numbers, and Toll-Free MMS in the US and Canada only. Toll-free messaging requires use case verification to ensure compliance with industry standards; unverified toll-free numbers may be spam blocked at any time, and unblocking requires use case verification.

### Registration

As of November 23, 2022, use case registration can be submitted from the [Mission Control portal](https://portal.telnyx.com/#/app/programmable-messaging/toll-free-messaging). Required information includes:

- Business details
- The toll-free number being used
- A summary of the use case
- Message content examples and expected monthly volume
- The opt-in process
- Additional use case details (Terms URL, Privacy Policy)
- Reseller/ISV field (if applicable)

Registration can also be done via API for bulk submissions and status tracking. After submission, status can be tracked from the Requests tab, and updates can be received via webhook. Current approval time is approximately 1–2 weeks.

From **November 8, 2023**, unverified toll-free numbers attempting to send messages are blocked industry-wide. From **January 31, 2024**, this blocking is automatic. Only one unique use case can be associated with one toll-free number; multiple toll-free numbers cannot send the same messaging content.

### Message content length

- **UCS-2 (16-bit):** 70 characters max; 67 characters per segment for multi-part.
- **Latin1 (8-bit):** 140 characters max; 134 characters per segment for multi-part.
- **GSM7 (7-bit):** 160 characters max; 153 characters per segment for multi-part.

### Valid use cases

Acceptable use cases include 2FA, Account Notification, Customer Care, Delivery Notification, Fraud Alert Messaging, Higher Education, Low Volume Mixed, Marketing, Mixed, Polling and Voting, and Public Service Announcements.

### Inappropriate use cases

Prohibited content (regardless of opt-in status) includes social marketing, collections, cryptocurrency, high-risk financial services (subprime lending, auto loans, mortgages, payday loans, short-term loans, student loans, debt consolidation), insurance (car, health), gambling/casino/bingo, gift cards, sweepstakes, free prizes, investment opportunities, lead generation, SEO services, recruiting, commission programs, credit repair, tax relief, illicit/illegal substances (including cannabis), work-from-home schemes, get-rich-quick schemes, UGGS and RayBan campaigns, phishing, fraud/scams, cannabis, deceptive marketing, and SHAFT (Sex, Hate, Alcohol, Firearms, Tobacco).

### Best practices

- Obtain clear consent with a call-to-action that discloses the program, originating numbers, organization identity, opt-in language and fees, opt-out instructions, customer care contact, and privacy policy.
- Do not send more than 10 messages to a recipient in any 24-hour period unless the recipient has engaged in two-way SMS communication or has explicitly opted in to frequent messages.
- Do not spoof another individual or business.
- Do not engage in fraud or phishing.
- Honor opt-out requests within 24 hours.

### Toll-free verification webhook notifications

Telnyx sends real-time webhook updates for verification status changes. The `verification_status` field can be:

- `Rejected`
- `Waiting For Vendor`
- `Waiting For Customer`
- `Verified`

Each event includes the affected phone number(s), business name, and reason for the current status when applicable.

## Picking a Toll-Free Use Case

When submitting a Toll-Free Verification Request, select the use case that best matches the messaging content. If more than one applies, select **Mixed**. If both marketing and non-marketing content are sent, select **Mixed**.

Common use cases include:

- **2FA:** One-time codes at login.
- **App Notifications:** Notifications such as password resets.
- **Booking Confirmations:** Reservation confirmations.
- **Conversational / Alerts:** One-on-one texting such as customer service.
- **Courier Services & Deliveries:** Delivery notifications.
- **Fundraising:** Charity solicitations for donations.
- **General Marketing:** Promotions, quotes, or offers.
- **Mixed:** Two or more of the other use cases.
- **Order Notifications:** Order status updates.
- **Political:** Political candidate promotion or fundraising.
- **System Alerts:** Operational alerts such as threshold breaches.

Additional use case options include Appointments, Auctions, Auto Repair Services, Bank Transfers, Billing, Business Updates, COVID-19 Alerts, Career Training, Chatbot, Emergency Alerts, Events & Planning, Financial Services, Fraud Alerts, General School Updates, HR / Staffing, Healthcare Alerts, Housing Community Updates, Insurance Services, Job Dispatch, Legal Services, Motivational Reminders, Notary Notifications, Public Works, Real Estate Services, Religious Services, Repair and Diagnostics Alerts, Rewards Program, Surveys, Voting Reminders, Waitlist Alerts, Webinar Reminders, and Workshop Alerts.
