---
title: "Short Code Best Practices"
summary: "In the United States, the CTIA serves as the governing body for text messaging programs, ensuring consumer protection against unwanted messages."
sources:
- url: "https://support.telnyx.com/en/articles/8173789-short-code-best-practices"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/8173789-short-code-best-practices.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/8173789-short-code-best-practices.md -->

# Short Code Best Practices

## CTIA - US SMS Messaging Programs

In the United States, the CTIA serves as the governing body for text messaging programs, ensuring consumer protection against unwanted messages. All message senders must adhere to the CTIA regulations, along with Wireless Providers' code of conduct and best practices.

To ensure compliance with CTIA requirements, it is essential for your program to incorporate the following Guiding Principles and Short Code Program Components:

## **Call-to-Action (CTA)**

The Call-to-Action (CTA) serves the purpose of obtaining consumer consent to receive text messages and understanding the program's nature. The CTA language should encourage consumers to opt into the messaging program and be clearly displayed with the following information:

- Program (Brand) Name/Product Description
- Message Frequency Disclosure
- Notification of potential Message and Data Rates (if non-FTEU)
- Opt-out information with the STOP keyword (Opt-out details may also appear in the terms and conditions.)
- Complete terms and conditions or a link to access them (Popups are not suitable for displaying terms and conditions.)
- Privacy policy or a link to the privacy policy

## User Consent

Messaging programs must be transparent, ensuring that consumers are aware and receive messages only from programs they have opted into.

### Opt-in

Consumers should opt-in to receive messages related to a specific program. Enrolling a consumer in multiple programs based on a single opt-in is not allowed, even if all programs operate on the same Short Code.

### Opt-out

Message senders must acknowledge and act upon all opt-out requests. Monitoring procedures should confirm successful opt-outs.

## Privacy Policy

Message senders are responsible for safeguarding consumers' information and complying with relevant privacy laws. Message senders should have a privacy policy for all programs, accessible from the initial CTA. Any mention of 3rd Party Data Sharing, Renting, or Selling is disallowed unless the below disclosure is included. When displaying a privacy policy link, it should be labeled clearly. In all cases, terms and conditions, as well as privacy policy disclosures, must provide up-to-date, accurate information about program details and functionality.

## Terms and Conditions

Comprehensive terms and conditions can be presented in full beneath the CTA or made accessible through a link close to the CTA. The terms and conditions must disclose the following:

- Program (Brand) Name

- Product Description

- Message Frequency Disclosure

- Notification of potential Message and Data Rates (if non-FTEU)

- Customer Care Contact Information (email or toll-free phone number)

- Opt-Out Instructions (reply STOP to opt-out)

For more information about CTIA messaging requirements, refer to:

- [CTIA Messaging Monitoring Handbook](https://www.wmcglobal.com/hubfs/CTIA%20Short%20Code%20Monitoring%20Handbook%20-%20v1.8.pdf)
- [CTIA Messaging Principles and Best Practices.](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)

## US - Program Message Flow Key Elements

A messaging program's message flow consists of the following:

## Opt-In Confirmation

Messaging programs should send a single opt-in confirmation message with details to verify the consumer's enrollment, program identification, and opt-out instructions.

Additionally, opt-in messages must contain the program (brand) name or product description, customer care contact information, message frequency disclosure, "message and data rates may apply" disclosure (for non-FTEU programs), and opt-out instructions (reply STOP to opt-out).

## HELP

Message senders must respond with a HELP message when consumers text the HELP keyword. Short Codes should provide the program's name and additional contact information for consumer assistance.

## Opt-Out

Message senders must send an opt-out message when consumers text a keyword indicating their desire to opt out (e.g., STOP, END, CANCEL, QUIT, UNSUBSCRIBE). The opt-out message must include the program's name and confirmation of the consumer's opt-out status.

## Robust Age Gates

Messaging content related to controlled substances or adult content distribution (SHAFT) may undergo additional carrier review. Such messaging should include robust age verification methods (e.g., electronic age and identity confirmation).

Examples of robust age gates include:

- Requesting the user's birthdate (e.g., "Reply with your birthdate xx/xx/xxxx")

- Utilizing a web opt-in form that requires the user to input their birthday

*"Reply YES/AGREE" does not qualify as a robust age verification method*

For additional question email: [shortcode@telnyx.com](mailto:shortcode@telnyx.com)

---

Related Articles

- [10DLC Campaign Approval Best Practices](https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices)
- [Regulatory Guidelines for US Short Code Marketing and Opt-in Procedures](https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures)
- [10DLC Campaign Compliance Requirements](https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements)
- [10DLC Carrier Error Codes Explanations](https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations)
- [Short Code Compliance Quick Reference Guide](https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide)
