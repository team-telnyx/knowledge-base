---
title: 10DLC Registration and Compliance
summary: A consolidated reference for registering and operating 10DLC messaging on
  Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and
  message flow requirements, opt-in form design, privacy policy language, sample messages,
  age gates, political campaigns, common errors, and associated fees.
sources:
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-07-17T09:00:56Z
---

# 10DLC Registration and Compliance

*Part 3 of 5 — see also: [Part 1](10dlc-registration-and-compliance--part-1.md), [Part 2](10dlc-registration-and-compliance--part-2.md), [Part 4](10dlc-registration-and-compliance--part-4.md), [Part 5](10dlc-registration-and-compliance--part-5.md)*

A consolidated reference for registering and operating 10DLC messaging on Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and message flow requirements, opt-in form design, privacy policy language, sample messages, age gates, political campaigns, common errors, and associated fees.

## Call-to-Action (CTA) Requirements

The CTA ensures the consumer consents to receive text messages and understands the program. It must clearly and unambiguously include:

- Program (Brand) Name / Product Description
- Message Frequency Disclosure (e.g., "Message frequency may vary.")
- "Standard Message and Data Rates may apply" (if non-FTEU)
- "Reply STOP to opt out" (opt-out information may appear in the terms and conditions)
- "Reply HELP for help"
- Terms and Conditions OR a link to them (not a pop-up)
- Privacy Policy OR a link to it
- Opt-in language specific to text messages only — it cannot bundle email or phone calls, which must be handled separately
- The phone number field on the website form should be optional, not mandatory, for opt-ins

For TCR compliance, every campaign must include the URL for the Terms and Conditions and Privacy Policy under the CTA. Even if the information is on the website, it must be displayed within TCR. TCR provides specific fields for Privacy Policy and Terms and Conditions links; these can be added in those fields or within the CTA section.

### Consent Models

**Implied Consent** — if the consumer initiates the text message exchange and the business only responds with relevant information, no verbal or written permission is expected. The first message is always sent by the customer, and the workflow must clearly and unmistakably explain how the customer is contacting the business to provide implied consent.

**Express Consent** — the consumer gives express permission before any text is sent, via text, form, website, or verbally.

- *Text:* the customer opts in by texting a specific keyword to a designated phone number. The workflow must include both the exact keyword and the designated phone number. Example: "Customer opt-in by sending 'WELCOME' to phone number 123456789".
- *Form:* the customer completes a form (electronic or paper) that includes opt-in language agreeing to receive text message communications. The form must be attached to TCR for verification.
- *Website:* the customer opts in through a webform. The phone number field should not be mandatory (forced opt-in is not allowed). Opt-in language should appear at the bottom of the form, clearly stating frequency, message and data rates, and that text messages will be sent. The opt-in must be exclusively for text messages; email and calls must be handled separately. If the opt-in is not on the main page, provide the specific URL where it occurs. Pop-up forms are allowed but must be specified as such in the CTA field of the registration.
- *Verbal:* the customer provides verbal consent during a phone call or in person. The process must clearly outline the scenarios in which consent is given. Example: "The customer will verbally opt-in during a phone conversation with one of our customer service representatives, who will ask if they would like to receive text messages from our company."

**Express Written Consent** — the consumer signs a form. When the use case is verbal or over email/written, provide the script or sample of the CTA to verify all aspects of the CTA are fulfilled. CTA requirements are based on T-Mobile Code of Conduct section 2.5 (Calls-to-Action) and CTIA Messaging Principles and Best Practices section 5.1.1 (Message Senders Should Provide Clear and Conspicuous Calls-to-Action).

### Marketing Use Case Example

> "By submitting this form and signing up for texts, you consent to receive marketing text messages (e.g. promos, cart reminders) from [company name] at the number provided, including messages sent by autodialer. Consent is not a condition of purchase. Msg & data rates may apply. Msg frequency varies. Carriers are not liable for delayed or undelivered messages. Unsubscribe at any time by replying STOP or clicking the unsubscribe link (where available). Text HELP for support. Privacy Policy [link] & Terms [link]."

## Opt-in Form Requirements

A digital opt-in form should look similar to the example below, although there are many valid variations:

![Example 10DLC opt-in form](_images/064b741afa8cc908.png)

Key requirements:

1. **Required disclaimers** — *By providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes.*
2. **SMS consent checkbox** — specific, explicit, and optional. Not buried in terms and conditions, not combined with other consents (such as "I agree to the terms and conditions"), and not a mandatory field.
3. **Subscriber knows what to expect** — the form clearly communicates the purpose, frequency, and terms of joining the campaign.
4. **Unchecked by default** — the SMS opt-in checkbox should be unchecked by default.
5. **Political or Charity use cases soliciting donations** — add "Donations may be solicited" to the opt-in disclaimers.
6. **Marketing use cases** — add language such as "You are opting into marketing texts" to the opt-in disclaimers.

For non-digital opt-in flows, see [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md).

## Message Flow Requirements

The Message Flow field documents the entire opt-in workflow. It must be 40–2048 characters and explain how the end user opts in before the first message is sent. If opt-in is via a website form, provide the link to the specific page where opt-in is gathered; optionally include a screenshot (for example a publicly accessible Google Drive link); include a link to the privacy policy.

Example:

> Patient's click "Book an appointment" on [www.example.com](http://www.example.com), then there is an sms opt in form which communicates clearly the purpose, frequency, and terms of joining this campaign. It is not required to accept sms notifications to submit the form. Screenshot of opt in: <https://imgur.com/a/4XCk7ga>. Privacy Policy which indicates no sharing or selling of PII with third parties for promotional or marketing purposes: [www.example2.com/privacy](http://www.example2.com/privacy).

### Keyword Opt-In Example

> **Opt-In by Keyword or Inbound Message**
>
> **Message Flow:**
>
> - The [brand] provides a keyword (e.g., "START") and a number (e.g., 123456) via [a channel such as a website, flyer, or QR code.]
> - The keyword opt-in process includes a disclaimer:
>   - *"Text [START or similar] to [123456] to opt in to receive SMS [use case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. [Brand Privacy Policy URL or privacy policy verbiage around mobile data sharing"*
> - When the user texts "START," the system responds with:
>   - *"Thank you for opting in to [Brand Name] SMS updates! Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*
> - *Link to where phone number or qr code is advertised or link to screenshot of where phone number or qr code is advertised*
