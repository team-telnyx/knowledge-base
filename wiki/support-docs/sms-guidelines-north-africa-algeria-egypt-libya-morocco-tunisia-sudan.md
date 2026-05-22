---
title: 'SMS Guidelines: North Africa (Algeria, Egypt, Libya, Morocco, Tunisia, Sudan)'
summary: Consolidated Telnyx SMS guidance for Algeria, Egypt, Libya, Morocco, Tunisia,
  and Sudan, including MCC and dial codes, Alphanumeric Sender ID requirements, network-specific
  caveats, and how to submit Sender ID registration requests.
sources:
- url: https://support.telnyx.com/en/articles/6592441-algeria-sms-guidelines
  content_hash: f048aac09ce353c6edd0b2324f502c7a3f9e45bb75ca680a7de39d7942d80900
- url: https://support.telnyx.com/en/articles/6670411-egypt-sms-guidelines
  content_hash: 484f4d31fa56dc9d6128d3d1079c545598ea7b7f979d3349943196e54e7a2364
- url: https://support.telnyx.com/en/articles/6674989-libya-sms-guidelines
  content_hash: 9ad2d481df8edb2ad49098db6dba2602437269287c47d6269214567a566b33bb
- url: https://support.telnyx.com/en/articles/6677982-morocco-sms-guidelines
  content_hash: 9f9b5297284570cc27c9f8f3a3be4bdc1eca49999925a92ebbdc97e846da96c6
- url: https://support.telnyx.com/en/articles/6683385-tunisia-sms-guidelines
  content_hash: 3567410b22707a9c8737312fd67a77bed098cf3263ac43aa33f2317ce3f049a3
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
  content_hash: 431d7f39d36e12526f1be36edf1b5528291db6bf4eca653692c3f8b6ede8e761
updated_at: 2026-05-21T08:21:11Z
---

# SMS Guidelines: North Africa (Algeria, Egypt, Libya, Morocco, Tunisia, Sudan)

Consolidated Telnyx SMS guidance for Algeria, Egypt, Libya, Morocco, Tunisia, and Sudan, including MCC and dial codes, Alphanumeric Sender ID requirements, network-specific caveats, and how to submit Sender ID registration requests.

## Regional overview and compliance basics
- Obtain consent (proof of opt-in) before sending, especially for marketing SMS.
- Include clear opt-out options in all applicable traffic.
- Always review Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- In Tunisia and Sudan, the use of generic Alphanumeric Sender IDs is not recommended; the Sender ID should be directly related to the message content. Treat this as a best practice across the region.

## Sender ID registration package requirements (Algeria, Libya, Tunisia)
For these markets, Alphanumeric Sender ID registration is mandatory before sending. Submit the following, along with a copy of your Business Registration, to alpha_sender_id@telnyx.com:
- Sender ID to be registered
- Message/content type
- Message/content example
- Company name (and brand name if different)
- Website of brand or company
- Company country of origin
- Expected volumes per month
- Email linked to your Telnyx account

Notes:
- You must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested ID isn’t clear, include supporting documentation.

## Algeria (MCC 603, Dial Code 213)
- Alphanumeric Sender ID registration is required; messages from unregistered Sender IDs will be rejected.
- See Sender ID registration package requirements above and submit to alpha_sender_id@telnyx.com.

## Egypt (MCC 602, Dial Code 20)
- Alphanumeric Sender IDs are supported.
- Network Etisalat (60203): Alphanumeric Sender IDs are only supported through registration. Without registration, Sender IDs may be overwritten to generic Alpha IDs or will not deliver.
- For registration details, contact alpha_sender_id@telnyx.com.

## Libya (MCC 606, Dial Code 218)
- Alphanumeric Sender ID registration is required; messages from unregistered Sender IDs will be rejected.
- See Sender ID registration package requirements above and submit to alpha_sender_id@telnyx.com.

## Morocco (MCC 604, Dial Code 212)
- Alphanumeric Sender IDs are supported with registration; registration is required.
- For registration details, contact alpha_sender_id@telnyx.com.

## Tunisia (MCC 605, Dial Code 216)
- Alphanumeric Sender ID registration is required; messages from unregistered Sender IDs will be rejected.
- Generic Alpha Sender IDs are not recommended; the Sender ID should directly relate to the message content.
- See Sender ID registration package requirements above and submit to alpha_sender_id@telnyx.com.

## Sudan (MCC 634, Dial Code 249)
- Alphanumeric Sender IDs are supported.
- Network MTN (63402): Alphanumeric Sender IDs are only supported with registration. Without registration, Sender IDs may be overwritten to generic Alpha IDs or will not deliver.
- Generic Alpha Sender IDs are not recommended; the Sender ID should directly relate to the message content.
- For registration details, contact alpha_sender_id@telnyx.com.

## Contact and references
- Sender ID registration requests and questions: alpha_sender_id@telnyx.com
- Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
