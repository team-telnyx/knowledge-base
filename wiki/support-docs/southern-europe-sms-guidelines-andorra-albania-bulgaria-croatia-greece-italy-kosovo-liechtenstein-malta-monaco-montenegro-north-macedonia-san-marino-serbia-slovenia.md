---
title: 'Southern Europe SMS Guidelines: Andorra, Albania, Bulgaria, Croatia, Greece,
  Italy, Kosovo, Liechtenstein, Malta, Monaco, Montenegro, North Macedonia, San Marino,
  Serbia, Slovenia'
summary: Consolidated Telnyx SMS rules for select Southern European and Balkan destinations,
  including MCCs, dial codes, alphanumeric Sender ID support and registration requirements,
  network-specific caveats, content guidance, and where to get registration help.
sources:
- url: https://support.telnyx.com/en/articles/6531722-italy-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675252-malta-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677954-monaco-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677964-montenegro-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679992-san-marino-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563843-croatia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561195-slovenia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563879-albania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563890-andorra-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563817-greece-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563862-bulgaria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674999-liechtenstein-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683745-serbia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674651-kosovo-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675034-macedonia-north-macedonia-sms-guidelines
updated_at: 2026-05-21T08:13:05Z
---

# Southern Europe SMS Guidelines: Andorra, Albania, Bulgaria, Croatia, Greece, Italy, Kosovo, Liechtenstein, Malta, Monaco, Montenegro, North Macedonia, San Marino, Serbia, Slovenia

Consolidated Telnyx SMS rules for select Southern European and Balkan destinations, including MCCs, dial codes, alphanumeric Sender ID support and registration requirements, network-specific caveats, content guidance, and where to get registration help.

## Overview and scope
This page summarizes Telnyx SMS delivery requirements for the following destinations: Andorra, Albania, Bulgaria, Croatia, Greece, Italy, Kosovo, Liechtenstein, Malta, Monaco, Montenegro, North Macedonia, San Marino, Serbia, and Slovenia. It focuses on Mobile Country Code (MCC), country dial code, whether Alphanumeric Sender IDs are supported and need registration, and any known delivery caveats. Always adhere to Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.

## Country-by-country quick reference
- No registration required; Alphanumeric Sender IDs supported and maintained; no additional content restrictions reported:
  - Albania — MCC 276, Dial +355
  - Andorra — MCC 213, Dial +376
  - Croatia — MCC 219, Dial +385
  - Italy — MCC 222, Dial +39
  - Kosovo — MCC 221, Dial +383
  - Liechtenstein — MCC 295, Dial +423
  - Malta — MCC 278, Dial +356
  - Monaco — MCC 212, Dial +377
  - Montenegro — MCC 297, Dial +382
  - San Marino — MCC 292, Dial +378
  - Slovenia — MCC 293, Dial +386

- No registration required, but delivery may occasionally use a Generic Alphanumeric Sender ID to ensure delivery:
  - North Macedonia — MCC 294, Dial +389

- Registration required; unregistered Sender IDs are rejected:
  - Greece — MCC 202, Dial +30

- Registration required (monthly fees apply); without registration, Alphanumeric Sender IDs are overwritten to a Generic Alphanumeric Sender ID:
  - Serbia — MCC 220, Dial +381

- Partial support; registration not possible; network-specific behavior:
  - Bulgaria — MCC 284, Dial +359
    - Maintained toward Vivacom (24803) and Telenor (24805)
    - Overwritten to a random local long code, short code, or generic alphanumeric toward A1 (28401)

## Greece: Alphanumeric Sender ID registration checklist
Greece requires Alphanumeric Sender ID registration. Unregistered traffic is rejected. Submit the following, along with a copy of your Business Registration, to alpha_sender_id@telnyx.com:
- Sender ID to be registered
- Message/content type
- Example message/content
- Company name (and Brand name if different)
- Company or brand website
- Company country of origin
- Expected monthly volumes
- Email associated with your Telnyx account
Additional notes:
- Provide a clear, valid business case; if the link between brand and requested Sender ID is not obvious, include supporting documentation.
- Obtain consent (proof of opt-in) before sending, especially for marketing.
- Include a clear opt-out mechanism in SMS.

## Serbia: registration notes and fees
Serbia supports Alphanumeric Sender IDs with registration; monthly fees apply. Without registration, Sender IDs are overwritten to a Generic Alphanumeric Sender ID. For registration details, contact alpha_sender_id@telnyx.com.

## Bulgaria: network-specific behavior
Bulgaria offers partial Alphanumeric Sender ID support and does not allow registration:
- Vivacom (24803) and Telenor (24805): alphanumeric Sender IDs are maintained.
- A1 (28401): alphanumeric Sender IDs are overwritten to a random local long code, short code, or generic alphanumeric to ensure delivery.

## Content and compliance guidance
- For Andorra, Albania, Croatia, Italy, Kosovo, Liechtenstein, Malta, Monaco, Montenegro, North Macedonia, San Marino, and Slovenia: no additional content restrictions were reported. Standard anti-spam and abuse rules still apply.
- For Greece, Bulgaria, and Serbia: no special content prohibitions were listed beyond the general policy; ensure you comply with consent and opt-out best practices where applicable.
- Always follow Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.

## Support and references
- Alphanumeric Sender ID registration assistance (Greece, Serbia): alpha_sender_id@telnyx.com
- Alphanumeric Sender ID overview: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id
- Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
