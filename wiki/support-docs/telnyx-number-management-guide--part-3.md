---
title: Telnyx Number Management Guide
summary: A consolidated reference for managing phone numbers on Telnyx, covering ordering
  restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF
  verification flows, use-case selection, and the sunset Google Verified Calls product.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Number Management Guide

*Part 3 of 5 — see also: [Part 1](telnyx-number-management-guide--part-1.md), [Part 2](telnyx-number-management-guide--part-2.md), [Part 4](telnyx-number-management-guide--part-4.md), [Part 5](telnyx-number-management-guide--part-5.md)*

A consolidated reference for managing phone numbers on Telnyx, covering ordering restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF verification flows, use-case selection, and the sunset Google Verified Calls product.

## Picking a Toll-Free Use Case

Most Verification Requests fall into one or more of these primary use cases. If you have more than one, select "Mixed". If you have any non-marketing content alongside marketing content, select "Mixed".

- **2FA** — One-time codes such as at login.
- **App Notifications** — Notifications such as "Your password has been reset".
- **Booking Confirmations** — Confirmations such as "Your stay has now been booked at the Telnyx Hotel in Denver, CO for Jan 1st, 2028."
- **Conversational / Alerts** — A large catch-all for any 1-on-1 texting such as customer service.
- **Courier Services & Deliveries** — "Your order has been delivered by FedEx at 12:00pm."
- **Fundraising** — Any charity messaging that will solicit donations.
- **General Marketing** — Any promotions, quotes, or offers made to customers.
- **Mixed** — Two or more of the other use cases.
- **Order Notifications** — "Your order number is 123456, please pick up at counter 3 in 15 minutes."
- **Political** — Any content promoting a political candidate or soliciting donations for political candidates.
- **System Alerts** — "Fridge 3 is over the temperature threshold."

Additional use case options include: Appointments, Auctions, Auto Repair Services, Bank Transfers, Billing, Business Updates, COVID-19 Alerts, Career Training, Chatbot, Emergency Alerts, Events & Planning, Financial Services, Fraud Alerts, General School Updates, HR / Staffing, Healthcare Alerts, Housing Community Updates, Insurance Services, Job Dispatch, Legal Services, Motivational Reminders, Notary Notifications, Public Works, Real Estate Services, Religious Services, Repair and Diagnostics Alerts, Rewards Program, Surveys, Voting Reminders, Waitlist Alerts, Webinar Reminders, Workshop Alerts.

## Verified Numbers (Non-Telnyx Numbers as CLI)

Verified Numbers are phone numbers confirmed to belong to the user and authorized to display as the CLI on calls made through the Telnyx platform. They are numbers obtained from a different provider that the customer wants to use as a CLI for outbound calls through Telnyx.

After February 15, 2023, Telnyx users cannot make calls from unverified numbers that have not been ported to Telnyx.

### Why Verify?

Ensuring customers use numbers they own for outbound calling reduces the risk of malicious use cases on the Telnyx network.

### How to Verify

Numbers can be verified through the Mission Control Portal. Users receive a verification code via Voice or SMS to each number they wish to verify. Once the code is verified in the portal, the number is marked as Verified in the Verified Numbers section.

### Pricing

There is a one-off charge of $0.03 per number verified, plus a separate charge based on the destination and channel used to send the verification request.

### Bulk Verification

If you have over 200 non-Telnyx numbers on calls through the Telnyx platform, Telnyx will assist you through a bulk verification process — a reinforced KYC process carried out with your account manager.

### Routing

Verified Numbers continue to receive incoming calls and messages through the original external provider.

### Voice and SMS

This feature applies to all voice services (SIP Trunking and Programmable Voice).

### Sharing Across the Organization

- If the account owner adds a verified number, it is available to all users.
- If a sub-user adds a verified number, it is available exclusively to that sub-user.
- To share verified numbers across the organization, ask the account admin to verify the number.

### Step-by-Step Verification via Mission Control Portal

1. Log into the Mission Control Portal and select "Phone Numbers" in the Voice Suite from the navigation menu.
2. Choose "My Numbers" to view all Telnyx numbers associated with your account.
3. Back to the navigation menu, select "Verified Numbers" to access the Verified Numbers section.
4. Choose either SMS or Call as the verification method.
   - **SMS** — A validation code is sent to your non-Telnyx number via SMS.
   - **Call** — A voice call is placed to your non-Telnyx number and an IVR plays the validation code twice.
5. Enter the verification code and press "Verify Number".
6. Your number appears on the list of Verified Numbers and is authorized to display as the CLI on calls made through the Telnyx platform.

### SIP Headers for Caller ID

Once numbers are verified and used for outbound calls, the Telnyx caller ID policy applies. The following SIP headers are accepted for Caller ID, ordered by priority (1 highest, 4 lowest):

1. P-Preferred-Identity User
2. P-Asserted-Identity User
3. Remote-Party-Id User
4. FROM User

Send the verified number in one of these headers, taking into account the order priority.

### Unverified Number Behavior

A call attempt using a non-Telnyx number that has not been verified will be rejected with a "403 Unverified Caller Origination Number D51" SIP error.

### Pay-as-You-Go Pricing

| Method | Cost |
| --- | --- |
| Verified Number via SMS | $0.03 per successful verification + [SMS API pricing](https://telnyx.com/pricing/messaging) |
| Verified Number via Voice call | $0.03 per successful verification + [Voice API pricing](https://telnyx.com/pricing/call-control) |
| Verified Number via Flash call | $0.03 per successful verification + [Flash pricing](https://telnyx.com/pricing/call-control) |
