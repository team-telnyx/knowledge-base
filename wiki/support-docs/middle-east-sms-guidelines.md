---
title: 'Middle East: SMS Guidelines'
summary: A consolidated reference for Telnyx SMS compliance across Middle Eastern
  markets (Bahrain, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Palestinian
  Territory, Qatar, Saudi Arabia, Syria, United Arab Emirates, and Yemen), covering
  MCC and dial codes, Sender ID registration requirements, prohibited content, timing
  rules, network-specific nuances, and how to register an Alphanumeric Sender ID.
sources:
- url: https://support.telnyx.com/en/articles/6589557-iraq-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596158-bahrain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674403-iran-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674453-israel-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674487-jordan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674713-kuwait-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674807-lebanon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679138-oman-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679259-palestinian-territory-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679369-qatar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680009-saudi-arabia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680256-syria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683438-united-arab-emirates-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683484-yemen-sms-guidelines
updated_at: 2026-05-21T08:25:55Z
---

# Middle East: SMS Guidelines

A consolidated reference for Telnyx SMS compliance across Middle Eastern markets (Bahrain, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Palestinian Territory, Qatar, Saudi Arabia, Syria, United Arab Emirates, and Yemen), covering MCC and dial codes, Sender ID registration requirements, prohibited content, timing rules, network-specific nuances, and how to register an Alphanumeric Sender ID.

## How to register an Alphanumeric Sender ID
Most Middle Eastern markets require Alphanumeric Sender ID registration before traffic will deliver. To register, email alpha_sender_id@telnyx.com with:

1) Sender ID to be registered
2) Message/Content type
3) Message/Content example(s)
4) Company name (and Brand name if different)
5) Website of brand or company
6) Company country of origin
7) Expected volumes per month
8) Email linked to your Telnyx account

Notes
- Provide a clear business case and ensure the requested Sender ID matches your brand; supply supporting documentation if the relationship is not obvious.
- Some countries/operators require their own forms and stamps (see Saudi Arabia and UAE below).
- Generic Sender IDs are discouraged in several markets; use a brand-aligned ID. See Telnyx guidance: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id
- For questions, contact alpha_sender_id@telnyx.com.

## Regional policies and best practices
- Consent and opt-out: Obtain proof of opt-in (especially for marketing) and include clear opt-out instructions in all traffic.
- Acceptable Use: Ensure content complies with Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- Prohibited content (common across the region): religious, political, adult, and gambling content are widely disallowed; some markets add further bans (see country notes).
- Unregistered traffic: Where registration is required, messages from unregistered Sender IDs are rejected (or in some cases overwritten to a numeric originator for best-effort delivery).
- Promotional labeling/time windows (where applicable):
  - Jordan: prefix “ADV” for promotional; send 07:00–21:00 local only.
  - Saudi Arabia & UAE: suffix “AD” for promotional; UAE blocks promotional sends 21:00–07:00 local (queued outside that window).
- Overwriting behavior (delivery fallback): In some networks/countries, unregistered (or even registered, rarely) alphanumeric Sender IDs may be overwritten to a random long code or short code to ensure delivery (see Iran, Oman, Yemen).

## Bahrain (MCC 426, Dial 973)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- Content blocked by operators: adult, political, religious.

## Iran (MCC 432, Dial 98)
- Alphanumeric Sender IDs partially supported.
  - Righttel (43220): alphanumeric supported and maintained.
  - MCI (43211): registration required.
  - Other networks: alphanumeric may be overwritten to a random long code to ensure delivery.
- Generic Sender IDs discouraged; use a brand-related ID.

## Iraq (MCC 418, Dial 964)
- Registration required; unregistered messages are rejected.

## Israel (MCC 425, Dial 972)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- Prohibited: religious, gambling, political, or adult traffic.

## Jordan (MCC 416, Dial 962)
- Registration required; unregistered messages are rejected.
- Promotional sends only 07:00–21:00 local; Sender IDs for promotional traffic must include prefix “ADV”.

## Kuwait (MCC 419, Dial 965)
- Registration required; unregistered messages are rejected.
- Prohibited: adult, religious, and political content.

## Lebanon (MCC 415, Dial 961)
- Registration required; unregistered messages are rejected.

## Oman (MCC 422, Dial 968)
- Registration required; alphanumeric supported with registration.
- Non-registered alphanumeric Sender IDs may be rejected or overwritten (best-effort).
- Generic Sender IDs discouraged; use a brand-related ID.

## Palestinian Territory (MCC 425, Dial 970)
- Registration required; unregistered messages are rejected.
- Prohibited: personal loans, gambling, adult, and cryptocurrency-related traffic.

## Qatar (MCC 427, Dial 974)
- Registration required; alphanumeric supported with registration.
- Generic Sender IDs discouraged; use a brand-related ID.
- Prohibited: religious, political, or adult traffic.

## Saudi Arabia (MCC 420, Dial 966)
- Registration required; only possible for international brands.
- Operator forms required (signed, on company letterhead with stamp) plus registration details via email:
  - STC template: https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796842/308d5690074fc8fb94e2f15f/NOC_Template_KSA+STC.docx
  - Zain template: https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796960/f3c608e829ed1e141d9801f0/NOC_Template_KSA+Zain.docx
- Promotional traffic must append suffix “AD” to the Sender ID.
- URLs in message content must be whitelisted during registration; URL shorteners are not allowed.
- Prohibited: gambling, political, or adult traffic.

## Syria (MCC 417, Dial 963)
- Registration required; unregistered messages are rejected.

## United Arab Emirates (MCC 424, Dial 971)
- Registration required; alphanumeric supported with registration.
- Required: signed/stamped form plus business registration or certificate of incorporation:
  - UAE SID registration form: https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073766982/9517e5f95b5cfd9c5d70ed94/UAE+SID+Reg+form.docx
- Promotional traffic must append suffix “AD”.
- Promotional sends are not allowed 21:00–07:00 local; traffic queued and delivered outside this window.
- Generic Sender IDs discouraged; use a brand-related ID.

## Yemen (MCC 421, Dial 967)
- Registration required; unregistered messages are rejected.
- Note: even registered alphanumeric Sender IDs may occasionally be overwritten to a random short code to ensure delivery.
