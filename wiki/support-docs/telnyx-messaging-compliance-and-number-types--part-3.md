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

*Part 3 of 4 — see also: [Part 1](telnyx-messaging-compliance-and-number-types--part-1.md), [Part 2](telnyx-messaging-compliance-and-number-types--part-2.md), [Part 4](telnyx-messaging-compliance-and-number-types--part-4.md)*

Comprehensive guide to Telnyx messaging compliance, covering US short code ordering and registration, 10DLC use cases and trust scores, ISV requirements, long code deliverability, short code keyword and CTA standards, acceptable use policies, forbidden messaging categories, supported carriers, and country-specific SMS guidelines for Norway, Belize, and the Palestinian Territory.

## US Short Code Keywords: HELP, STOP, and Opt-In Confirmation

All US-based Telnyx short codes must respond appropriately to HELP and STOP keywords regardless of the sender's subscription status.

### Opt-Out Handling

Subscribers must be able to opt out by texting STOP or equivalent keywords (END, CANCEL, UNSUBSCRIBE, QUIT). When received, the application must process the request and maintain the opt-out list. STOP responses must be sent regardless of prior subscription status.

**STOP response example:**

> You are unsubscribed from {Campaign Name} {Description} Alerts. No more messages will be sent. Reply HELP for help or {toll-free number}.

### HELP Handling

HELP responses must be sent regardless of subscription status.

**HELP response example:**

> {Campaign Name} {Description} Alerts: Help available at {source of help #1} or {toll-free number}. Msg&data rates may apply. {Message frequency}. Text STOP to cancel.

The description should succinctly define the alert type (e.g., "Account Alerts," "News Alerts," "Promo Alerts"). The help source must be either a toll-free phone number or a support email address (other forms are permissible but one of these is required at minimum). Message frequency must be specific (e.g., "1 message per day," "4 messages per month," "2 messages per transaction") or "Message frequency varies."

### Regulatory Compliance

These standards adhere to the CTIA Short Code Monitoring Handbook. Short code initiatives may be reviewed for compliance by a carrier or regulatory body. Carriers have discretion to terminate short code services without notice. Additional regulatory obligations may apply under the Telephone Consumers Protection Act of 1991 (TCPA) depending on campaign nature.

## US Short Code Marketing and Opt-In Procedures

Wherever a short code is promoted or where individuals opt in to receive short code messages, specific details must be included. This applies to any medium through which a phone number is provided (paper forms, online platforms, etc.).

### Call to Action (CTA) Requirements

An SMS keyword CTA example:

> Text {Keyword} to ##### to subscribe to alerts.

Wherever the short code is advertised (online, in print, etc.), include:

> Message and data rates may use. {Message frequency}. Text HELP to ##### for assistance. Text STOP to ##### to unsubscribe. For terms: {URL to SMS terms of service}. For privacy: {URL to privacy policy}

### CTA Drafting Considerations

- Message frequency must be precise (e.g., "1 message/day," "4 messages/month"). If frequency depends on user interaction, phrase as "1 message/user request." For variable frequencies, "Message frequency varies" is permissible but may require justification.
- The privacy policy must be tailored to the text messaging campaign and clearly marked.
- Terms and conditions must clearly explain campaign operation.
- The word "STOP" should be emphasized in bold wherever it appears.
- Additional language may be required depending on the campaign's nature.

## Acceptable Use Policy for Messaging

Telnyx reserves the right to suspend or close accounts that violate these guidelines or the [Terms and Conditions](https://telnyx.com/terms-and-conditions). These guidelines do not replace all prohibited activities covered by the Telnyx General Terms & Conditions.

### Sending Unsolicited Messages

SMS recipients must have explicitly opted in. The opt-in process must be clearly explained. The following do not qualify as valid opt-ins:

- Collecting a phone number for another purpose (e.g., payment validation) then sending messages to it
- Purchasing, borrowing, renting, or obtaining phone numbers or lead lists from third parties
- Having a customer opt in for transactional messages (e.g., package delivery) then subscribing them to recurring campaigns

Telnyx reserves the right to request proof of opt-in at any time.

### Prohibited Content

The following content types are explicitly prohibited:

- Sexual or pornographic
- Abusive or harassing
- Firearms (including fireworks)
- Alcohol, tobacco, or illegal drugs
- High Risk Financial: loans or loan forgiveness, credit repair, debt collection or tax-related content, cryptocurrency-related content including OTPs
- Gambling
- Investment opportunities
- Unsolicited real estate enquiries (e.g., WeBuyHomes)
- Multilevel marketing
- Persistent receiving or sending of one-time passcodes from or on behalf of other service providers

### Unsubscribe Requests

Recipients may unsubscribe by sending stop words such as STOP or UNSUBSCRIBE. These messages are delivered via webhook. Upon receipt, recipients must be removed from the list within 24 hours.

### High-Frequency Messaging

No more than 10 messages may be sent to a recipient in any 24-hour period unless:

- The recipient has engaged in two-way SMS communication (e.g., chat feature)
- The customer has explicitly opted in to receiving frequent messages

### Identity Misrepresentation

Representing or identifying yourself as another individual or business is prohibited. The message body or phone number must not lead recipients to believe you are another individual or business.

### Fraud and Phishing

Sending messages with fraudulent information or phishing to obtain confidential information is explicitly prohibited.

### Additional Regulations

**CAN-SPAM (United States)**: Federal law regulating commercial email and Internet-to-phone SMS commercial messages. Full text: [PLAW-108publ187](http://www.gpo.gov/fdsys/pkg/PLAW-108publ187/pdf/PLAW-108publ187.pdf).

**CASL (Canada)**: Canadian federal law regulating commercial electronic messages (CEMs). Requires prior consent and prescribed form/content requirements. Applies to CEMs sent to or from computer systems in Canada. Full text: [Justice Laws](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/index.html).

**CTIA Messaging Principles**: [CTIA Messaging Principles and Best Practices](https://api.ctia.org/docs/default-source/default-document-library/170119-ctia-messaging-principles-and-best-practices.pdf) provides recommendations for the wireless messaging ecosystem.
