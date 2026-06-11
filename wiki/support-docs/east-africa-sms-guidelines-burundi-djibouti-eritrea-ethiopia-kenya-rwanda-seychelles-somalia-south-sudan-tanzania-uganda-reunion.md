---
title: 'East Africa: SMS Guidelines (Burundi, Djibouti, Eritrea, Ethiopia, Kenya,
  Rwanda, Seychelles, Somalia, South Sudan, Tanzania, Uganda, Réunion)'
summary: Consolidated Telnyx SMS delivery rules for selected East African and Western
  Indian Ocean markets, covering alphanumeric sender ID support/registration, operator-specific
  caveats, and known content restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6601042-burundi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665699-djibouti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670452-eritrea-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670465-ethiopia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674630-kenya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679407-rwanda-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680053-seychelles-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680135-somalia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680141-south-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683295-tanzania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683433-uganda-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679378-reunion-sms-guidelines
updated_at: 2026-05-21T08:23:42Z
---

# East Africa: SMS Guidelines (Burundi, Djibouti, Eritrea, Ethiopia, Kenya, Rwanda, Seychelles, Somalia, South Sudan, Tanzania, Uganda, Réunion)

Consolidated Telnyx SMS delivery rules for selected East African and Western Indian Ocean markets, covering alphanumeric sender ID support/registration, operator-specific caveats, and known content restrictions.

## Overview
This page summarizes Telnyx SMS requirements for Burundi, Djibouti, Eritrea, Ethiopia, Kenya, Rwanda, Seychelles, Somalia, South Sudan, Tanzania, Uganda, and Réunion. It focuses on alphanumeric sender ID (alpha) policies, per-operator registration needs, and notable content rules. Always ensure compliance with Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.

## How to register an alphanumeric sender ID
Where registration is required, submit the following to alpha_sender_id@telnyx.com:
- Sender ID to be registered
- Message/content type and a content example
- Company name (and brand name if different)
- Company/brand website
- Company country of origin
- Expected monthly volumes
- Email linked to your Telnyx account
- Copy of your Business Registration

Notes
- You must have a valid business case. If the link between your brand and the requested Sender ID isn’t obvious, include supporting documentation explaining the use case.
- Unregistered traffic to routes requiring registration may be rejected, overwritten to a generic alpha, or fail to deliver.

## Country-specific requirements
### Burundi
- MCC: 642 | Dial Code: 257
- Alpha Sender IDs: Registration required; messages from unregistered Sender IDs will be rejected.
- Additional: Valid business case required; ensure the brand-Sender ID relationship is clear.

### Djibouti
- MCC: 253 | Dial Code: 638
- Alpha Sender IDs: Supported and maintained; no registration required.
- Content: No restrictions noted for this destination.
- Recommendation: Avoid generic Sender IDs; Sender should directly relate to message content.

### Eritrea
- MCC: 657 | Dial Code: 291
- Alpha Sender IDs: Supported and maintained; no registration required.
- Content: Religious, political, or adult traffic is prohibited.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### Ethiopia
- MCC: 636 | Dial Code: 251
- Alpha Sender IDs: Supported.
- Operator caveat: MTN (63601) supports alpha only with registration; without it, Sender IDs may be overwritten to a generic alpha or not delivered.
- Content: Traffic related to local Banking or Promotional content is not allowed.

### Kenya
- MCC: 639 | Dial Code: 254
- Alpha Sender IDs: Supported with registration; registration is required.
- Content: Political, religious, gambling, adult, and P2P content is prohibited.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### Rwanda
- MCC: 635 | Dial Code: 250
- Alpha Sender IDs: Supported.
- Operator caveat: MTN (63510) supports alpha only with registration; without it, Sender IDs may be overwritten to a generic alpha or not delivered.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### Seychelles
- MCC: 633 | Dial Code: 248
- Alpha Sender IDs: Supported and maintained; no registration required.
- Content: No restrictions noted for this destination.

### Somalia
- MCC: 637 | Dial Code: 252
- Alpha Sender IDs: Supported and maintained; no registration required.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### South Sudan
- MCC: 659 | Dial Code: 211
- Alpha Sender IDs: Supported.
- Operator caveat: MTN (65902) supports alpha only with registration; without it, Sender IDs may be overwritten to a generic alpha or not delivered.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### Tanzania
- MCC: 640 | Dial Code: 255
- Alpha Sender IDs: Supported with registration; registration is required.

### Uganda
- MCC: 641 | Dial Code: 256
- Alpha Sender IDs: Supported.
- Operator caveat: MTN (64110) supports alpha only with registration; without it, Sender IDs may be overwritten to a generic alpha or not delivered.
- Recommendation: Avoid generic Sender IDs; align Sender with content.

### Réunion
- MCC: 647 | Dial Code: 262
- Alpha Sender IDs: Supported and maintained; no registration required.
- Content: No restrictions noted for this destination.

## Compliance and best practices
- Obtain prior consent (opt-in) before sending outreach such as marketing SMS, and include a clear opt-out path in every message where applicable.
- Use brand-specific sender IDs closely tied to message content; avoid generic terms.
- Where operator-specific registration is required (commonly MTN networks cited above, plus markets like Kenya and Tanzania), complete registration before sending to prevent overwriting or delivery failures.
- Adhere to local content prohibitions (e.g., political/religious/adult/gambling/P2P where noted; promotional/banking restrictions in Ethiopia).
- Always review the latest Telnyx Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.
