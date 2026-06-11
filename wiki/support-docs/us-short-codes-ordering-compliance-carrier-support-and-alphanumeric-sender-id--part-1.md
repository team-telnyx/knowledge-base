---
title: 'US Short Codes: Ordering, Compliance, Carrier Support, and Alphanumeric Sender
  ID'
summary: End-to-end guide to ordering and migrating US short codes with Telnyx, mandatory
  Short Code Registry (SCR) brand/content‑provider registration, key compliance requirements
  (CTA, HELP/STOP, terms and privacy), carrier notes, supported-carrier scope, and
  how Alphanumeric Sender ID works outside the US/Canada.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
updated_at: 2026-05-20T14:19:13Z
---

# US Short Codes: Ordering, Compliance, Carrier Support, and Alphanumeric Sender ID

*Part 1 of 2 — see also: [Part 2](us-short-codes-ordering-compliance-carrier-support-and-alphanumeric-sender-id--part-2.md)*

End-to-end guide to ordering and migrating US short codes with Telnyx, mandatory Short Code Registry (SCR) brand/content‑provider registration, key compliance requirements (CTA, HELP/STOP, terms and privacy), carrier notes, supported-carrier scope, and how Alphanumeric Sender ID works outside the US/Canada.

## What short codes are and where they work
Short codes are short numerical sender IDs used for high-throughput SMS/MMS like alerts, authentication, and marketing. They are country-specific: a short code registered in the United States can only deliver to US recipients. 

## Order types and timelines
Telnyx supports two order types:
- New short code (random or vanity)
- Migration of an existing short code from another provider

Typical timeline: after your brief is approved and the brand/content provider are registered, allow about 6 weeks for final carrier approvals, provisioning, and testing (subject to volume and seasonality).

## Requirements to order a new US short code
For new random or vanity codes, complete the following in parallel (forms have overlapping information):
- Short Code Order Brief (for carriers)
- Brand Registration Form (for the Short Code Registry)
- Content Provider Registration Form (for the Short Code Registry)

Notes
- “Brand” is the perceived sender (e.g., Nike). “Content provider” is the entity creating/sending content (e.g., marketing agency). They may be the same entity.
- To request current forms, email shortcode@telnyx.com.
- As part of SCR brand registration, both the brand and content provider contacts must verify via an email sent by certify@aegismobile.com or a noreply@usshortcodes.com address. Third‑party vetting applies.
- Telnyx can procure a “parked” short code during registration, but it cannot send traffic until brand and content provider registration is complete and the program is fully approved.

## Migrating an existing US short code
Provide the following:
- Short Code Order Brief
- Brand and Content Provider Registration Forms
- Migration Letter
- Letter of Authorization (LOA)
- Have your current provider transfer the code to the Short Code Registry Telnyx account (request account ID via shortcode@telnyx.com)

After documentation is approved and accepted, expect ~6 weeks for final carrier approval, testing, and provisioning.

## Mandatory SCR brand and content provider registration (new and renewals)
The Short Code Registry (SCR) requires registration for both new orders and renewals.
- New orders: SCR brand and content provider registration must be completed before a code can become active.
- Existing leases: For renewals on/after January 15, 2025, brands must be registered. Brands that do not complete by March 31, 2025 receive a 60‑day grace period after the first auto‑renewal date on or after March 31, 2025. Non‑compliant codes may face enforcement (suspension/termination).
- Registration details should match the entity’s IRS CP‑575 (EIN Confirmation) letter.
- Brand vetting and 2FA are repeated annually; update contacts as needed.
- For forms or questions: shortcode@telnyx.com.

## Compliance essentials for US short codes
Carriers and industry bodies (e.g., CTIA) require specific disclosures in your Calls to Action (CTAs), opt‑in flows, and messaging. Expect audits; carriers may suspend service at their discretion. Ensure your program also complies with laws like the TCPA. Telnyx customers must follow the Telnyx Acceptable Use Policy: https://telnyx.com/acceptable-use-policy.

Key elements for subscription programs
- CTA must clearly state: product/program description; “Message & data rates may apply”; specific message frequency; opt‑out instructions; link to privacy policy; link to full terms & conditions; and customer care instructions (e.g., “Reply HELP for help” with a toll‑free number, website, or support email; if showing the HELP keyword, include a telephone contact such as 10DLC where applicable).
- Optional opt‑in confirmation prompt may include brand name/product description and a response command (e.g., “Reply Y”).
- Welcome message should reiterate brand/program description, message frequency, M&D rates may apply, and customer care contact (e.g., “Reply HELP for help” plus toll‑free, website, or support email).
- Ongoing broadcast messages should include the brand/program description and clear opt‑out info.

Key elements for one‑off programs
- CTA should include: product description, M&D rates may apply, privacy policy (link or clear access), and either a link to full T&Cs or explicit customer care instructions (e.g., “Reply HELP for help” with a toll‑free number, website, or support email; if showing HELP keyword, include a telephone contact such as 10DLC where applicable).
- The one‑off reply should include the brand/program name or description.

Terms & Conditions placement
- You may place full terms on the CTA if your HELP disclosure includes a phone‑based or equivalent customer care method (toll‑free, website, or support email). If not full, ensure at minimum: brand/program description; message frequency (for subscriptions); M&D rates may apply; and customer care contact info (e.g., “Reply HELP for help” plus toll‑free, website, or support email).

Privacy policy requirements
- Must explicitly state that messaging application data will not be shared with third parties for marketing purposes. “We respect your privacy” alone is insufficient. Avoid any language implying sale or disclosure for marketing.

HELP and STOP keyword standards (US)
- Your short code must respond compliantly to HELP and STOP (and STOP synonyms END, CANCEL, UNSUBSCRIBE, QUIT) regardless of subscription status.
- You must honor opt‑out requests sent by any legitimate means and maintain an opt‑out/block list. Do not message opted‑out users unless they independently opt back in.
- Example STOP response: “You are unsubscribed from {Campaign Name} {Description} Alerts. No more messages will be sent. Reply HELP for help or {toll‑free number}.”
- Example HELP response: “{Campaign Name} {Description} Alerts: Help at {support email or toll‑free}. Msg&data rates may apply. {Message frequency}. Text STOP to cancel.”
- Message frequency must be specific (e.g., “1 message/day,” “4 messages/month,” “2 messages per transaction”), or “Message frequency varies” if applicable.

Drafting CTAs and disclosures
- Include: “Message and data rates may apply. {Message frequency}. Text HELP to ##### for assistance. Text STOP to ##### to unsubscribe. Terms: {TOS URL}. Privacy: {Privacy URL}.”
- Emphasize the word STOP wherever it appears.
- Ensure privacy policy and terms are tailored to the SMS program and easily accessible from the CTA.
- Consult legal counsel for campaign‑specific requirements.

Currency of guidance
- The quick‑reference content above reflects carrier expectations current as of November 2024; carriers and requirements may change.

## Carrier‑specific notes
T‑Mobile
- Additional scrutiny applies to political campaigns, shopping cart reminders, and donations.
- Program description and message frequency must be consistent across the brief, CTA, and terms.
- “Gray” marketing for financial institutions is not permitted (even for direct lenders).

Verizon
- For OTP/2FA programs, provide an alternative passcode delivery method (e.g., email).
- Avoid content such as abandoned cart, financial incentives, or financial aid (remove industry jargon and sensitive instrument links). Collections content is not allowed.

## Supported carriers and coverage scope
- Short code delivery is supported across major US operators (AT&T, Verizon Wireless, T‑Mobile, U.S. Cellular) and many regional carriers, with additional coverage in Canada and select territories through participating carriers. The supported‑carrier list is maintained by Telnyx and may change.
- Short codes are country‑specific; US short codes only reach US numbers.
- To explore availability or submit a request: https://portal.telnyx.com/#/messaging-short-code
- For the latest supported‑carrier list, see: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
