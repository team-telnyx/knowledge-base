---
title: 10DLC Campaign Registration and Compliance Guide
summary: A consolidated reference for registering and maintaining 10DLC (10-Digit
  Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms,
  keywords, privacy policy, sample messages, vetting, shared campaigns, and common
  carrier errors.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-08-05T13:25:10Z
---

# 10DLC Campaign Registration and Compliance Guide

*Part 2 of 5 — see also: [Part 1](10dlc-campaign-registration-and-compliance-guide--part-1.md), [Part 3](10dlc-campaign-registration-and-compliance-guide--part-3.md), [Part 4](10dlc-campaign-registration-and-compliance-guide--part-4.md), [Part 5](10dlc-campaign-registration-and-compliance-guide--part-5.md)*

A consolidated reference for registering and maintaining 10DLC (10-Digit Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms, keywords, privacy policy, sample messages, vetting, shared campaigns, and common carrier errors.

## Message Flow Field

The Message Flow field documents how subscribers opt in to the campaign. It is the most scrutinized field on the registration. There are four accepted opt-in methods; pick one and follow the matching template, replacing the bracketed variables with your brand and campaign details.

### Digital Consent (Web Form or Contact Us Page)

- The user navigates to [Brand Name]'s [website] and subscribes via a specific opt-in page at [url] (or [path subscriber takes if gated]) and [link to screenshot].
- The opt-in form clearly states:
  > "By providing your phone number and clicking 'Submit,' you agree to receive SMS [update type] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. [Privacy Verbiage such as: Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.] or [Link to compliant Privacy Policy]."

### Verbal Consent (Over the Phone or In-Person)

- When a customer [calls or walks] in to [phone number or office address] which is published at [url or how user learns number/address], the representative explains the consent process verbally:
  > Agent states to the customer: "By providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes."
- Once the customer verbally agrees, the phone number is recorded and a confirmation SMS is sent:
  > "You have agreed to receive SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."

**Verbal Consent for Marketing Use Case**

- A customer may call [the number] or be present in the office. An employee presents the consent process verbally:
  > "Would you like to sign up for SMS notifications from [BRAND] so we can send you [use cases + marketing]? By providing your phone number to [BRAND] you are consenting to receive [use cases + marketing] via text messages from us. Message and data rates may apply. Message frequency may vary. You can text HELP for support or more information and STOP to unsubscribe at any time. We won't share your mobile information with third parties for marketing. You can also find our privacy policy and terms of service on our website at [URL]."
- After verbal agreement, the phone number is recorded and a confirmation SMS is sent:
  > "[BRAND]: You have agreed to receive SMS updates. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe, HELP for help. To confirm you also want to receive marketing messages please reply YES."
- If the user replies YES:
  > "[BRAND] Thanks, you've now been subscribed to SMS notifications, including promotions from [BRAND]. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe or HELP for help."
- If the user does not reply YES, they are not opted in to promotional messaging and will only receive informational messaging.

**Verbal Consent for Political Use Case**

- A customer may call [the number] or be present in the office. An employee presents the consent process verbally:
  > "Would you like to sign up for SMS from [BRAND]? By providing your phone number to [BRAND] and agreeing you are consenting to receive [other use cases + political] messaging? [Donations will/will not be solicited.] Message and data rates may apply. Message frequency may vary. You can text HELP for support or more information and STOP to unsubscribe at any time. We won't share your mobile information with third parties for marketing. You can also find our privacy policy and terms of service on our website at [URL]."
- After verbal agreement, the phone number is recorded and a confirmation SMS is sent:
  > "[BRAND]: You have agreed to receive SMS [use case(s)] updates. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe, HELP for help. To confirm you also want to receive political messages please reply YES."
- If the user replies YES:
  > "[BRAND] Thanks, you've now been subscribed to SMS, including political messages from [BRAND]. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe or HELP for help."
- If the user does not reply YES, they are not opted in to political messaging and will only receive informational messaging.

### Physical Consent (Paper Form)

- The user fills out a paper form during [appointment/onboarding/renewal/etc.] at [address], which they learn about at [website/social/whatever], providing their phone number and signing their consent.
- The form includes a disclaimer:
  > "By signing this form and providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."
- Once the information is entered into the system, the user receives a confirmation SMS:
  > "Thank you for signing up for SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."
- Include a link to a Dropbox (or similar) copy of the paper form.

### Opt-In by Keyword or Inbound Message

- The [brand] provides a keyword (e.g., "START") and a number (e.g., 123456) via [a channel such as a website, flyer, or QR code].
- The keyword opt-in process includes a disclaimer. When the user texts "[Keyword]," the system responds with:
  > "Thank you for opting in to [Brand Name] SMS [update type] (or [We will be with you shortly])! Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."
- Include a link or screenshot of where the phone number or QR code is advertised.

For inbound-only opt-in, the [brand] provides a number (e.g., 123456789) via [a channel such as a website, flyer, QR code, business card, email signature, etc.]. When the user texts the number, the system responds with:

> "Thank you for your message to [Brand Name]! We will be with you shortly. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. We will not share or sell your mobile information for marketing/promotional purposes."

### Special Disclaimers

- If the campaign has a marketing use case, the opt-in must mention marketing, for example: "You are opting in to receive marketing SMS from [Brand Name]."
- If the campaign has a political or charity use case and any fundraising is involved (or perceived to be involved), the opt-in must state: "Donations may be solicited."
