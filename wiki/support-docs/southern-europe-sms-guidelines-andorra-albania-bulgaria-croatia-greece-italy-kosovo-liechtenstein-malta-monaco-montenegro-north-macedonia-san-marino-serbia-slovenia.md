---
title: 'Southern Europe SMS Guidelines: Andorra, Albania, Bulgaria, Croatia, Greece,
  Italy, Kosovo, Liechtenstein, Malta, Monaco, Montenegro, North Macedonia, San Marino,
  Serbia, Slovenia'
summary: Consolidated Telnyx SMS rules for select Southern European and Balkan destinations,
  including MCCs, dial codes, alphanumeric Sender ID support and registration requirements,
  network-specific caveats, content guidance, and where to get registration help.
sources:
- url: https://support.telnyx.com/en/articles/6531722-italy-sms-guidelines
  content_hash: e326d156b1e925abf8567ea6e7ec80de98a92446cb9ee84d9df3102f1205c8ed
- url: https://support.telnyx.com/en/articles/6675252-malta-sms-guidelines
  content_hash: 92c1d8476f9fd1d2a9e5f08b3b16e25e1acbca285ea188962019c45f0339aa94
- url: https://support.telnyx.com/en/articles/6677954-monaco-sms-guidelines
  content_hash: 591c838401fb989d61e068290ee1d80036285f7663415907cc3816ccc73bd76f
- url: https://support.telnyx.com/en/articles/6677964-montenegro-sms-guidelines
  content_hash: b5b636c986810d684b9bbad0961586619d03e36ba02827576e0f73078c2b0f9e
- url: https://support.telnyx.com/en/articles/6679992-san-marino-sms-guidelines
  content_hash: 12798ab5be2d7f2014e6419637b2ebbd0b0c6bdc26f39157fd1767ab434f39cf
- url: https://support.telnyx.com/en/articles/6563843-croatia-sms-guidelines
  content_hash: 3988fceeee77cf31fd51d33e49fa96f22de64f0544366f0d4b66aa969f81a3b6
- url: https://support.telnyx.com/en/articles/6561195-slovenia-sms-guidelines
  content_hash: c8615cd525e9732d8c2beb2ebb608533635f4594a55066e6ec9d352e7f3b4227
- url: https://support.telnyx.com/en/articles/6563879-albania-sms-guidelines
  content_hash: 8119863f2f9b2d4b7e958411d44a8f94a3011aa17cbcb0c859a8b4b7277d7711
- url: https://support.telnyx.com/en/articles/6563890-andorra-sms-guidelines
  content_hash: f112ce27f4a0a55df495f585bde14c9b34cb44708548a8f3162ab80cf231092a
- url: https://support.telnyx.com/en/articles/6563817-greece-sms-guidelines
  content_hash: 6230a36fd8978aca4557eb6507c69cd35043da9b04d9fca6556756d40962a4c7
- url: https://support.telnyx.com/en/articles/6563862-bulgaria-sms-guidelines
  content_hash: 57365fb95710144bd833c95a81261a836e92d6460e4ca890446533f88325c014
- url: https://support.telnyx.com/en/articles/6674999-liechtenstein-sms-guidelines
  content_hash: 8b8ac821021e76ee94ee52ebe2241bebb8b1d618c6632748600ff0459ad5bacc
- url: https://support.telnyx.com/en/articles/6683745-serbia-sms-guidelines
  content_hash: fd7384455cf0ac4551ab1fc4671bbf3ab5b9fe6a9be253f17b07e389b3d7f352
- url: https://support.telnyx.com/en/articles/6674651-kosovo-sms-guidelines
  content_hash: ef3eed5fedfcb9aa72c5a5551312db4cfe221ca620a02dafaa887054a68dc749
- url: https://support.telnyx.com/en/articles/6675034-macedonia-north-macedonia-sms-guidelines
  content_hash: 00c11c93b02012c021f7e2fe8f6bdead745d80e4ecc38a459501d2d517f306ac
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
