---
title: 10DLC Compliance on Telnyx
summary: 10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person
  (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates
  Telnyx's guidance on registration deadlines, brand and campaign setup, use cases,
  throughput, prohibited content, carrier error codes, and related compliance obligations.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-08-05T13:24:50Z
---

# 10DLC Compliance on Telnyx

*Part 3 of 3 — see also: [Part 1](10dlc-compliance-on-telnyx--part-1.md), [Part 2](10dlc-compliance-on-telnyx--part-2.md)*

10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates Telnyx's guidance on registration deadlines, brand and campaign setup, use cases, throughput, prohibited content, carrier error codes, and related compliance obligations.

## Carrier Error Codes

When a 10DLC campaign is rejected or flagged, carriers return specific error codes. The most common are:

- **701** — Prohibited Content; Cannabis (including CBD, hemp, teas, beauty products, derivatives, and shipping services).
- **702** — Prohibited Content; Guns/Ammo (sales require age verification; educational content is acceptable if it does not engage in sales).
- **703** — Prohibited Content; Explicit Sexual (illegal sexual themes, non-consensual acts, underage exploitation, or family-friendly-looking content with adult themes).
- **704** — Prohibited Content; Gambling (casino games, sports betting, lottery, online gambling; bingo may be allowed with age gating).
- **705** — Prohibited Content; Hate (hate speech, inappropriate content, profanity).
- **706** — Prohibited Content; Alcohol (Age-Gated) — requires a functioning DD/MM/YYYY age gate at opt-in.
- **707** — Prohibited Content; Tobacco/Vape (Age-Gated) — requires age gate and legal compliance.
- **708** — Lead Gen/Affiliate Marketing Prohibited (any mention of lead generation or SEO on the website can trigger this).
- **709** — Lead Gen/Affiliate Marketing Prohibited (High-Risk Financial Services) — payday loans, non-direct lenders, debt collection, credit repair, debt forgiveness, crypto, and stock trading traffic.
- **601** — Campaign Attributes Do Not Match Website and/or Sample Message Content (e.g., embedded link/phone marked YES but missing from samples).
- **602** — Inaccurate Registration; Inconsistent Sample Message and Use-Case (e.g., marketing use case not reflected in the CTA or message flow).
- **603** — Inaccurate Registration; Inconsistent Website and Sample Messages.
- **611** — Opt-in Message Requirements Not Met (must include program name, message frequency, HELP, opt-out, and data rate disclosures; opt-in must meet express consent standard, e.g., a checkbox next to the CTA).
- **710** — Reseller / Non-compliant KYC (the brand sending messages must be the one registered, not the agency).
- **711** — Repeated Use of Same EIN for Multiple Brands (requires a valid explanation).
- **712** — Misleading Registration (direct lenders and regulated entities must mark themselves as such).
- **713** — Large Companies Using Non-Official Email Domains.
- **801** — Not Sole Proprietor (does not meet TCR/carrier Sole Proprietor criteria).
- **802** — Sole Proprietor Not Yet Authorized (requires Syniverse authorization).
- **803** — Opt-in Language Required on Website (if a phone number is required for contact, opt-in language must be present).
- **804** — Unable to Verify Website/CTA Information (incomplete or inaccessible CTA, broken links).
- **805** — Non-Compliant Privacy Policy (must state that SMS opt-in data will not be shared with third parties).
- **806** — Unable to Verify, Needs Compliant and Accurate CTA Information (missing HELP, STOP, message frequency, data rates, or privacy policy link/language). For verbal opt-in, the message flow must contain all required language; for online opt-in, the CTA must include program/brand name, message frequency disclosure, "Standard Message and Data Rates may apply" (if non-FTEU), "Reply STOP to opt out," "Reply Help for help," and links to Terms & Conditions and Privacy Policy (not pop-ups).
- **851** — Privacy Policy and Opt-in Confirmation Requirements Not Met.
- **852** — Privacy Policy Compliance Missing (must clearly state mobile opt-in data is not shared with third parties).
- **861** — CTA Information Incomplete (must contain program name, message frequency, opt-in disclosures, and links to terms & conditions).
- **807** — Unable to Verify, Inauthentic Website (common for real estate and insurance companies with incomplete websites).

## Sample Registration: Chiropractors

A chiropractor registering a 10DLC campaign should:

- Select the **Healthcare** vertical.
- Use the **Low Volume Mixed** use case with a **Customer Care** sub-use case.
- Provide a campaign description such as: "Campaign to send SMS customer care messages to [Practice Name] patients."
- Document a verbal opt-in flow at the front desk, including all required disclosures (program name, message frequency, data rates, STOP, HELP, no third-party sharing).
- Send a confirmation SMS after verbal agreement.
- Configure START, STOP, and HELP auto-responses with compliant language.
- Provide a sample appointment reminder message.
- Set campaign attributes: Subscriber opt-in Yes, Subscriber help Yes, Direct lending No, Embedded phone No, Age-gated No, Subscriber opt-out Yes, Number pooling No, Embedded link No, Affiliate marketing No.
- Leave compliance links and webhooks blank unless needed.

## Additional Regulatory Frameworks

In addition to 10DLC and Telnyx's Acceptable Use Policy, customers must comply with applicable laws and industry standards, including:

- **CAN-SPAM (US)** — Federal law regulating commercial email and Internet-to-phone SMS commercial messages referencing Internet domains. Full text: [PLAW-108publ187](http://www.gpo.gov/fdsys/pkg/PLAW-108publ187/pdf/PLAW-108publ187.pdf).
- **CASL (Canada)** — Canada's anti-spam law regulating commercial electronic messages (CEMs) sent to or from computer systems in Canada. Requires prior consent and prescribed form/content. Full text: [Justice Laws — CASL](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/index.html).
- **CTIA Messaging Principles** — Industry best practices for the wireless messaging ecosystem. See [CTIA Messaging Principles and Best Practices](https://api.ctia.org/docs/default-source/default-document-library/170119-ctia-messaging-principles-and-best-practices.pdf).
- **Accessible Canada Act (ACA)** — Canadian accessibility requirements for telecom providers. Customers can submit ACA feedback to [acafeedback@telnyx.com](mailto:acafeedback@telnyx.com) with the subject line "ACA: Feedback," including name, phone number, email, relation to Telnyx, and a description of the feedback.

## Definitions and Acronyms

- **10DLC** — 10 Digit Long Code. The protocol under which local long code A2P messages are regulated in the US.
- **A2P** — Application To Person Messaging. Covers virtually all messages sent by or on behalf of a business.
- **Brand** — The trading name of the company sending messages, tied to an EIN.
- **Campaign** — A way to organize 10DLC-registered numbers and their use cases, governed by TCR.
- **MO** — Messaging Origination. A message sent to an A2P number; subject to MO fees.
- **MT** — Messaging Termination. A message sent from an A2P number to an end user; subject to MT fees.
- **P2P** — Person-to-person messaging not on behalf of a business; subject to limited exemptions.
- **TCR** — The Campaign Registry, the entity appointed by carriers to manage 10DLC registration records.

## Telnyx's Role and Customer Responsibility

Telnyx provides APIs, portal tools, and direct integration with The Campaign Registry so businesses can create Brands and Campaigns, assign numbers, and send 10DLC-compliant traffic. However, it is the customer's responsibility — including ISVs on behalf of their customers — to ensure that all A2P traffic sent over 10DLC numbers is compliant. Any fees or fines imposed by MNOs for non-compliance are the customer's responsibility.

For the latest 10DLC functionality, see the [Telnyx 10DLC Release Notes](https://telnyx.com/release-notes?tag=10dlc). For fees, see [10DLC Fees and Charges](10dlc-fees-and-charges.md). For additional questions, contact Telnyx support 24/7 via the [Mission Control Portal](mission-control-portal.md) or email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).
