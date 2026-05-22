---
title: 'Oceania: SMS Guidelines (Australia, New Zealand, and Pacific Islands)'
summary: Consolidated Telnyx SMS guidance for Oceania, covering MCC/dial codes, sender
  ID behavior, registration requirements, and compliance notes for Australia, New
  Zealand, Fiji, New Caledonia, Norfolk Island, Papua New Guinea, Solomon Islands,
  and Vanuatu. Highlights include ACMA-mandated alphanumeric sender ID registration
  in Australia and short code overwrites in New Zealand, with links to resources and
  contacts.
sources:
- url: https://support.telnyx.com/en/articles/6531656-australia-sms-guidelines
  content_hash: 2a8c6f9fd9442d8df64a7d0d20f47d89eda1aff5ba4b5b9c0f461680c65292d8
- url: https://support.telnyx.com/en/articles/6670784-fiji-sms-guidelines
  content_hash: 2dca89e5c376d563f8fbaf8cddd77e3644464518f26132eb6e27f0a265c0c8d9
- url: https://support.telnyx.com/en/articles/6679031-new-caledonia-sms-guidelines
  content_hash: 9a0c510196f0bf92ef537761ab36087cbabac6b7bfc3d9c004f7bf4fc506b9e3
- url: https://support.telnyx.com/en/articles/6679036-new-zealand-sms-guidelines
  content_hash: 1e8fb7539f24c1000b2f2362816985706dca70320b89483db68e416488ed508f
- url: https://support.telnyx.com/en/articles/6679129-norfolk-island-sms-guidelines
  content_hash: 4261d0572a0041421ffc31f62ec8e9c2fa66c5ac11514d33b8824c757ae97545
- url: https://support.telnyx.com/en/articles/6679279-papua-new-guinea-sms-guidelines
  content_hash: 57a1f8e830367f5014aac199d31e44acee6c6af9d45ac4eb13b52be1f4eed996
- url: https://support.telnyx.com/en/articles/6680123-solomon-islands-sms-guidelines
  content_hash: 1d29320cd0298f9dcabc51df97e7ae52a26ba99d7f4ffacd7cde0405b49738d1
- url: https://support.telnyx.com/en/articles/6683459-vanuatu-sms-guidelines
  content_hash: 70b735c3e0cf0194339279396fb9859fa86c4f348e2e0cc5cfaa01458d5c79b1
updated_at: 2026-05-21T08:29:40Z
---

# Oceania: SMS Guidelines (Australia, New Zealand, and Pacific Islands)

Consolidated Telnyx SMS guidance for Oceania, covering MCC/dial codes, sender ID behavior, registration requirements, and compliance notes for Australia, New Zealand, Fiji, New Caledonia, Norfolk Island, Papua New Guinea, Solomon Islands, and Vanuatu. Highlights include ACMA-mandated alphanumeric sender ID registration in Australia and short code overwrites in New Zealand, with links to resources and contacts.

## Overview
Use this guide to plan compliant SMS delivery across Oceania. It summarizes sender ID policies, registration rules, and content restrictions (if any), with quick-reference MCC and dial codes per destination.

## Country-specific guidelines
### Australia
- MCC: 505; Dial code: +61
- Alphanumeric Sender IDs: Mandatory registration by ACMA. Messages using non-registered alphanumeric sender IDs have been blocked since May 8, 2023.
- Upcoming regulation changes: Announced by ACMA on Oct 9, 2025; expected effective date July 1, 2026. Telnyx will register sender IDs via the ACMA portal; customers must confirm registration. Telnyx will contact customers with existing registrations about next steps.
- Registration process: Complete the Australia Alpha Sender ID Registration Form and email it with your Business Registration to alpha_sender_id@telnyx.com. Provide a clear business case matching the requested sender ID; if registering on behalf of a customer, include a signed LOA.
- Compliance: Commercial traffic must comply with the Australian Spam Act 2003 and include clear opt-out options. Obtain consent before sending (e.g., for marketing SMS). Always adhere to Telnyx’s Acceptable Use Policy for Messaging.
- Resources: Australian Spam Act guidance (https://www.acma.gov.au/avoid-sending-spam); Alphanumeric Sender ID overview (https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id).

### New Zealand
- MCC: 530; Dial code: +64
- Alphanumeric Sender IDs: Overwritten to a random short code to ensure delivery.
- Delivery best practice: Use a dedicated short code to improve delivery; without one, delivery is best-effort only.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.
- Additional resources:
  - SMS API (https://telnyx.com/products/sms-api)
  - MMS API (https://telnyx.com/products/mms-api)
  - Messaging pricing (https://telnyx.com/pricing/messaging)
  - SMS opt-in guide (https://telnyx.com/resources/sms-opt-in)
  - SMS number type guide (https://telnyx.com/resources/sms-numbers-traffic-types)
  - Hosted SMS guide (https://telnyx.com/resources/hosted-sms-how-to-guide)
  - CTIA guidelines (https://telnyx.com/resources/CTIA-SMS-guidelines)
  - Compliant bulk SMS (https://telnyx.com/resources/bulk-sms-guide)
  - SMS compliance and regulations (https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations)

### Fiji
- MCC: 542; Dial code: +679
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

### New Caledonia
- MCC: 546; Dial code: +687
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

### Norfolk Island
- MCC: 505; Dial code: +672
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

### Papua New Guinea
- MCC: 537; Dial code: +675
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

### Solomon Islands
- MCC: 540; Dial code: +677
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

### Vanuatu
- MCC: 541; Dial code: +678
- Alphanumeric Sender IDs: Supported and maintained; no registration required.
- Content restrictions: None noted for this destination.
- Acceptable Use: Follow Telnyx’s Acceptable Use Policy for Messaging.

## General compliance and best practices
- Obtain and retain proof of opt-in consent before sending marketing or promotional SMS.
- Include clear, functional opt-out instructions in every applicable message.
- Adhere to Telnyx’s Acceptable Use Policy for Messaging (https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).
- Australia-specific: Ensure alignment with the Australian Spam Act 2003 (https://www.acma.gov.au/avoid-sending-spam) and complete alphanumeric sender ID registration before sending.

## Contacts and forms
- Alphanumeric Sender ID registration support: alpha_sender_id@telnyx.com
- Australia Alpha Sender ID Registration Form (download): https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/ltcafuzd/2253013238/00833f07233d0c450aa41f247f72/Australia_Alpha+Sender+ID+Registration+Form.docx
- Alphanumeric Sender ID documentation: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id
