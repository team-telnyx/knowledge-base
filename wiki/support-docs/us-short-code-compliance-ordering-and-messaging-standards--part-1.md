---
title: US Short Code Compliance, Ordering, and Messaging Standards
summary: This page consolidates Telnyx guidance on ordering US short codes, registering
  brands and content providers, complying with carrier and CTIA standards for HELP/STOP
  keywords and opt-in CTAs, and meeting short-code messaging requirements across subscription
  and one-off programs.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
updated_at: 2026-08-05T13:24:16Z
---

# US Short Code Compliance, Ordering, and Messaging Standards

*Part 1 of 2 — see also: [Part 2](us-short-code-compliance-ordering-and-messaging-standards--part-2.md)*

This page consolidates Telnyx guidance on ordering US short codes, registering brands and content providers, complying with carrier and CTIA standards for HELP/STOP keywords and opt-in CTAs, and meeting short-code messaging requirements across subscription and one-off programs.

## Overview of US Short Codes

Short codes are short numerical codes used to send and receive SMS and MMS messages. They are especially useful for businesses and organizations to conduct marketing campaigns, alerts, and two-factor authentication because they are memorable and capable of handling high message volumes. Short codes are country-specific — a short code registered in the United States, for example, can only deliver in-country traffic to other United States numbers.

Telnyx maintains a global list of carriers that can support short code messages, including major US carriers (AT&T, T-Mobile, Verizon Wireless, U.S. Cellular, Sprint Nextel, Google Voice, and others) and Canadian carriers (Bell Mobility, Rogers Wireless, Telus Mobility, Videotron, and others). The list is subject to change and may be updated occasionally.

## Ordering a New Random or Vanity Short Code

To order a new Random or Vanity Short Code through Telnyx, three forms must be completed:

1. **Short Code Order Brief** — for the carriers.
2. **Brand Registration Form** — for the Short Code Registry. This is revetted every 12 months by the Short Code Registry.
3. **Content Provider Registration Form** — for the Short Code Registry. The content provider can be the same entity as the brand.

A brand is the perceived sender of the messages (for example, Nike sending text messages about shoes), while the content provider is the entity that develops and types the content into the application to send (for example, a marketing agency hired by Nike). They can be the same entity.

There is significant overlap between the forms, so filling them out at the same time is beneficial. As part of the brand registration process, the brand and content provider contacts must complete a verification email sent by the Short Code Registry, and a third-party vetting will be completed. Once the brief is approved and the brand is registered, it takes about 6 weeks to get final approval from the carriers, do provisioning, and testing. This can vary based on volume and season.

To request a current Short Code Order Brief, Brand, or Content Provider Registration Form, contact [Shortcode@telnyx.com](mailto:Shortcode@telnyx.com).

## Migrating an Existing Short Code

To migrate an existing Random or Vanity Short Code to Telnyx, the following are required:

1. Short Code Order Brief
2. Brand and Content Provider Registration Form
3. Migration Letter
4. Letter of Authorization (LOA)
5. The current provider must transfer the short code to the Short Code Registry Telnyx account. Email [shortcode@telnyx.com](mailto:shortcode@telnyx.com) for the account ID.

Once the documents are approved and accepted, it takes about 6 weeks to get final carrier approval, do testing, and provisioning.

## Brand and Content Provider Registration Process

The Short Code Registry has introduced a new mandatory process for both ordering and renewing existing leases on short codes. For new short code orders, and starting January 15, 2025 for all existing short code renewals, brands and their content providers must be registered with the Short Code Registry. For Telnyx customers going through brand registration, the following are required:

1. Brand Registration Form
2. Content Provider Form
3. Email verification by the Brand contact and Content Provider contact. The verification email is sent by [certify@aegismobile.com](mailto:certify@aegismobile.com) or an address like [noreply@usshortcodes.com](mailto:noreply@usshortcodes.com).

For new short code orders, the short code itself cannot be procured until brand registration and content provider registration are complete. The one caveat is that a "parked" short code can be procured, which cannot be used for messaging during the process, but the short code will not achieve an "active" status where messages can be sent until registration is complete.

For existing short code renewals, brands that do not complete this process by March 31, 2025 will have a sixty (60) calendar day grace period after the first auto-renewal date on or after March 31, 2025 to get a brand and content provider registered. Short codes that are not updated with the requisite information within this timeframe will be subject to compliance enforcement and may be suspended or terminated.

The information filled out on the form should match the entity's IRS Form CP-575 (also known as the EIN Confirmation letter) to be successful in registration. Brand vetting and 2FA are redone every year, so Telnyx should be notified if the point of contact changes.

For up-to-date forms or any other questions, contact [Shortcode@telnyx.com](mailto:Shortcode@telnyx.com).

## Compliance Quick Reference Guide

The following carrier requirements apply when ordering a short code. The information is current as of November 2024.

### Subscription Programs

**Call to Action (CTA):**

The user must consent to opt-in. Language needs to:

- Be clear
- Include product description
- State that message and data rates may apply
- State message frequency
- Include opt-out instructions
- Include a privacy policy or link to a privacy policy
- Link to complete terms and conditions (T&Cs)
- Include customer care instructions: *Reply HELP to [10DLC or toll-free #, website, or support email address]*. If displaying the HELP keyword, include 10DLC with it.

**Opt-in Confirmation Prompt (Optional):**

- Program brand name and/or product description
- Response command (for example, Reply Y or PIN)

**Welcome Message:**

- Program brand name and/or product description
- Message frequency
- Message and data rates may apply
- Customer care contact info (Reply HELP for help, toll-free #, website, or support email address)

**Ongoing Broadcast Copy:**

- Program brand name and/or product description
- Opt-out information

### One-Off Programs

**Call to Action (CTA):**

- Product description
- Message and data rates may apply
- Privacy policy or link to a privacy policy
- Link to complete terms and conditions (T&Cs) OR customer care instructions: *Reply HELP to [10DLC, toll-free #, website, or support email address]*. If displaying the HELP keyword, include 10DLC with it.

**One-Off Reply:**

- Program brand name and/or product description

### Terms and Conditions

Terms may be **full** on the CTA if the **HELP disclosure includes the 10DLC or a form of customer care** (toll-free #, website, or support email address).

If terms are **not** in full on the CTA, the following are required:

- Program brand name and/or product description
- Message frequency (only for subscription)
- Message and data rates may apply
- Customer care contact info (Reply HELP for help, toll-free #, website, or support email address)

### Privacy Policy

- Any language that hints or states personal info is shared or sold to third parties for marketing purposes is **not allowed**. No share, no disclose, no transfer.
- "We respect your privacy" or "we do not share data" is **not sufficient**.
- The policy **must state that messaging application data will not be shared with third parties for marketing purposes**.

### T-Mobile Notes

The following use cases require additional complexity and review:

- Political campaigns
- Shopping cart reminders
- Donations

Consistency throughout the brief is required. The following must match in the messaging, the CTA, and the terms page:

- Program description
- Message frequency

Gray marketing for financial institutions is **not allowed** (even at a direct lender).

### Verizon Notes

- For OTP/2FA, there **must** be an alternative way to receive the passcode (for example, email).
- Content that must be avoided:
  - Abandoned cart
  - Financial incentives
  - Financial aid (remove industry speak, loan type, link to secure instrument)
- **Collections are not allowed**.
