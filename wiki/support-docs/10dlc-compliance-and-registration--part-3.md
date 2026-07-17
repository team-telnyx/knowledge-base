---
title: 10DLC Compliance and Registration
summary: 10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent
  from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including
  who it applies to, how to register a Brand and Campaign, throughput and vetting
  rules, message flow templates, fees and non-compliance fines, and the February 3,
  2025 enforcement deadline after which unregistered traffic is blocked.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-07-17T09:00:19Z
---

# 10DLC Compliance and Registration

*Part 3 of 5 — see also: [Part 1](10dlc-compliance-and-registration--part-1.md), [Part 2](10dlc-compliance-and-registration--part-2.md), [Part 4](10dlc-compliance-and-registration--part-4.md), [Part 5](10dlc-compliance-and-registration--part-5.md)*

10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including who it applies to, how to register a Brand and Campaign, throughput and vetting rules, message flow templates, fees and non-compliance fines, and the February 3, 2025 enforcement deadline after which unregistered traffic is blocked.

## Message Flow Field

The CTA/Message Flow field is often the most challenging part of campaign registration. It documents how subscribers opt in to your campaign. SMS opt-in can be gathered in one of four ways: Digital, Verbal, Paper, or by Inbound message.

### Digital Consent (e.g., Web Form or Contact Us Page)

- The user navigates to [Brand Name]'s website and subscribes via a specific opt-in page at [url] or [path subscriber takes if gated] and [link to screenshot].
- The opt-in form clearly states: *"By providing your phone number and clicking 'Submit,' you agree to receive SMS [update type] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. [Privacy Verbiage such as: Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.] or [Link to compliant Privacy Policy]."*

### Verbal Consent (Over the Phone or In-Person)

- When a customer calls or walks in to [phone number or office address] which is published at [url or how user learns number/address], the representative explains the consent process verbally:
  - *Agent states: "By providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes."*
- Once the customer verbally agrees, the phone number is recorded, and a confirmation SMS is sent: *"You have agreed to receive SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*

**Verbal Consent for Marketing Use Case:**

- *"Would you like to sign up for SMS notifications from [BRAND] so we can send you [use cases + marketing]? By providing your phone number to [BRAND] you are consenting to receive [use cases + marketing] via text messages from us. Message and data rates may apply. Message frequency may vary. You can text HELP for support or more information and STOP to unsubscribe at any time. We won't share your mobile information with third parties for marketing. You can also find our privacy policy and terms of service on our website at [URL]."*
- Confirmation SMS: *"[BRAND]: You have agreed to receive SMS updates. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe, HELP for help. To confirm you also want to receive marketing messages please reply YES."*
- If the user replies YES: *"[BRAND] Thanks, you've now been subscribed to SMS notifications, including promotions from [BRAND]. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe or HELP for help."*
- If the user does NOT reply YES, they will not be opted in to promotional messaging and will only receive informational messaging.

**Verbal Consent for Political Use Case:**

- *"Would you like to sign up for SMS from [BRAND]? By providing your phone number to [BRAND] and agreeing you are consenting to receive [other use cases + political] messaging? [Donations will/will not be solicited.] Message and data rates may apply. Message frequency may vary. You can text HELP for support or more information and STOP to unsubscribe at any time. We won't share your mobile information with third parties for marketing. You can also find our privacy policy and terms of service on our website at [URL]."*
- Confirmation SMS: *"[BRAND]: You have agreed to receive SMS [use case(s)] updates. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe, HELP for help. To confirm you also want to receive political messages please reply YES."*
- If the user replies YES: *"[BRAND] Thanks, you've now been subscribed to SMS, including political messages from [BRAND]. Msg frequency varies. Msg&data rates may apply. Reply STOP to unsubscribe or HELP for help."*
- If the user does NOT reply YES, they will not be opted in to political messaging and will only receive informational messaging.

### Physical Consent (e.g., Paper Form)

- The user fills out a paper form during [appointment/onboarding/renewal/etc.] at [address] which they learn at [website/social/whatever], providing their phone number and signing their consent.
- The form includes a disclaimer: *"By signing this form and providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."*
- Once the information is entered into the system, the user receives a confirmation SMS: *"Thank you for signing up for SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*
- Include a link to a Dropbox or similar of the paper form.

### Opt-In by Keyword Message Flow

- The brand provides a keyword (e.g., "START") and a number (e.g., 123456) via a channel such as a website, flyer, or QR code.
- When the user texts the keyword, the system responds: *"Thank you for opting in to [Brand Name] SMS [update type] or [We will be with you shortly]! Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."*
- Include a link to where the phone number or QR code is advertised, or a screenshot of where it is advertised.

### Opt-In by Inbound Message

- The brand provides a number (e.g., 123456789) via a channel such as a website, flyer, QR code, business card, email signature, etc.
- When the user texts the number, the system responds: *"Thank you for your message to [Brand Name]! We will be with you shortly. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. We will not share or sell your mobile information for marketing/promotional purposes."*
- Include a link to where the phone number or QR code is advertised, or a screenshot of where it is advertised.

### Additional Message Flow Requirements

- If you have a marketing use case, marketing must be mentioned on the opt in (e.g., "You are opting in to receive marketing sms from [Brand Name].").
- If you have a political or charity use case and there is any fundraising (or it is perceived that there will be fundraising), you must mention "Donations may be solicited." on the opt in.
