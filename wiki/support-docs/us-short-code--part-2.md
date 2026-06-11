---
title: US Short Code
summary: A comprehensive guide to ordering, registering, and maintaining compliance
  for US Short Codes on the Telnyx platform, covering the ordering process, brand
  and content provider registration, supported carriers, keyword standards, and regulatory
  marketing and opt-in requirements.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
  content_hash: 9d57003059a9460ba3ad630ef4e0cda754216dfce3f6c755d1e1628125862564
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
  content_hash: 18cb804b0fc52e6e871630daa35d6bbd8a8a7ebe1637d96a817c20058c94ce82
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
  content_hash: ff40150b81fc5b308b3ffbaa9121f5c2515b5342592c413d828e48585074f1ec
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
  content_hash: e6d5f36b6c5bbc94e8cf8597ec9c8a0cdc7e0ba565fa935dc0de72c2c652b0f4
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
  content_hash: 489d2501cf9bb0fd262d8c86074600bc5ad0da6e389742c399d7e817089208b9
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
  content_hash: 717a6def14840de67c8aaaa73fc21594877a5146d73db694ef71bce70e05542a
updated_at: 2026-06-11T11:10:14Z
---

# US Short Code

*Part 2 of 2 — see also: [Part 1](us-short-code--part-1.md)*

A comprehensive guide to ordering, registering, and maintaining compliance for US Short Codes on the Telnyx platform, covering the ordering process, brand and content provider registration, supported carriers, keyword standards, and regulatory marketing and opt-in requirements.

## Compliance Quick Reference

The following carrier requirements apply when ordering and operating a short code.

### Subscription Programs

**Call to Action (CTA) must include:**

- Clear opt-in consent language
- Product description
- "Message & data rates may apply"
- Message frequency
- Opt-out instructions
- Privacy policy or link to privacy policy
- Link to complete terms & conditions (T&Cs)
- Customer care instructions (e.g., "Reply HELP to [10DLC or toll-free #, website, or support email address]"). If displaying the HELP keyword, include a 10DLC number with it.

**Opt-in Confirmation Prompt (optional):**

- Program brand name and/or product description
- Response command (e.g., "Reply Y" or "Reply PIN")

**Welcome Message must include:**

- Program brand name and/or product description
- Message frequency
- "Message & data rates may apply"
- Customer care contact info (e.g., "Reply HELP for help, toll-free #, website, or support email address")

**Ongoing Broadcast Copy must include:**

- Program brand name and/or product description
- Opt-out information

### One-Off Programs

**Call to Action (CTA) must include:**

- Product description
- "Msg & data rates may apply"
- Privacy policy or link to privacy policy
- Link to complete T&Cs **or** customer care instructions (e.g., "Reply HELP to [10DLC, toll-free #, website, or support email address]"). If displaying the HELP keyword, include a 10DLC number with it.

**One-Off Reply must include:**

- Program brand name and/or product description

### Terms and Conditions

If terms are displayed **in full** on the CTA, the HELP disclosure must include a 10DLC or another form of customer care (toll-free #, website, or support email address).

If terms are **not** in full on the CTA, the following is required:

- Program brand name and/or product description
- Message frequency (only required for subscription programs)
- "Msg & data rates may apply"
- Customer care contact info

### Privacy Policy Requirements

- Any language stating or implying personal info is shared or sold to third parties for marketing purposes is **not allowed**. No share, no disclose, no transfer.
- "We respect your privacy" or "we do not share data" is **not sufficient**.
- The policy **must state** that messaging application data will not be shared with third parties for marketing purposes.

### T-Mobile Specific Notes

The following use cases require **additional complexity and review**:

- Political campaigns
- Shopping cart reminders
- Donations

Consistency is required throughout the brief — the program description and message frequency must match in the messaging, the CTA, and the terms page.

Gray marketing for financial institutions is **not allowed**, even at a direct lender.

### Verizon Specific Notes

- For OTP/2FA use cases, there **must** be an alternative way to receive the passcode (e.g., email).
- Content that must be avoided: abandoned cart, financial incentives, financial aid (remove industry speak, loan type, links to secure instruments).
- **Collections are not allowed.**

## Keyword Standards (HELP, STOP, and Opt-In)

All US-based Telnyx short codes are required to respond appropriately to the HELP and STOP keywords, regardless of the sender's subscription status. These standards follow the [CTIA Short Code Monitoring Handbook](https://www.wmcglobal.com/us-resources).

### STOP Keyword

Users must be able to opt out by texting STOP or equivalent keywords: **END, CANCEL, UNSUBSCRIBE, QUIT**. When a user sends one of these keywords, your application must:

- Process the request and maintain the opt-out list.
- Place the user on a block list, prohibiting further messages unless they choose to opt back in.
- Send a compliant response.

**Example STOP response:**

> You are unsubscribed from {Campaign Name} {Description} Alerts. No more messages will be sent. Reply HELP for help or {toll-free number}.

### HELP Keyword

A compliant response is required whenever a recipient texts HELP to your short code, regardless of subscription status.

**Example HELP response:**

> {Campaign Name} {Description} Alerts: Help available at {source of help #1} or {toll-free number}. Msg&data rates may apply. {Message frequency}. Text STOP to cancel.

**Important notes:**

- The "description" should succinctly define the alert type (e.g., "Account Alerts," "News Alerts," "Promo Alerts").
- The help source **must** include either a toll-free phone number or a support email address at minimum. Other help forms are permissible but one of these is required.
- Message frequency must be specific (e.g., "1 message per day," "4 messages per month," "2 messages per transaction"). "Message frequency varies" is also acceptable.

## Marketing and Opt-In Procedures

Industry norms require specific details wherever your short code is promoted or wherever individuals opt in to receive messages. This includes any medium through which a person provides their phone number — online platforms, paper forms, etc. These promotions and opt-in forms are commonly called **Calls to Action (CTAs)**.

### CTA Requirements

Wherever the short code is advertised, the following mandatory information must be included:

> Message and data rates may use. {Message frequency}. Text HELP to ##### for assistance. Text STOP to ##### to unsubscribe. For terms: {URL to SMS terms of service}. For privacy: {URL to privacy policy}

### Key Considerations

- **Message frequency** must be precise (e.g., "1 message/day," "4 messages/month"). If frequency depends on user interaction, use "1 message/user request." For variable frequencies, "Message frequency varies" is permissible but may require justification.
- **Privacy policy** must be tailored to your text messaging campaign and detail how data is managed. It must be accessible via the CTA and clearly marked.
- **Terms and conditions** must be linked within the CTA and clearly explain campaign operation. Consult legal counsel to ensure all necessary legal notices are included.
- The word **STOP** should be emphasized in **bold** wherever it appears.
- Additional language may be needed to comply with specific legal requirements depending on the nature of your campaign.

### Regulatory Audits and Enforcement

U.S. short code campaigns are routinely reviewed for compliance per the CTIA Short Code Monitoring Handbook. Carriers have the discretion to **terminate short code services without notice**, so compliance with these guidelines does not guarantee uninterrupted service. Campaigns may also be subject to additional regulatory obligations under U.S. legislation such as the Telephone Consumers Protection Act of 1991 (TCPA). Consult legal counsel to ensure procedures conform to all applicable laws and industry practices.

For questions about any of the above, contact [Shortcode@telnyx.com](mailto:Shortcode@telnyx.com).

For related compliance topics, see [Short Code Compliance Quick Reference Guide](short-code-compliance-quick-reference-guide.md) and [Standards for US Short Code Keywords: HELP, STOP, and Opt-In Confirmation](standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation.md).
