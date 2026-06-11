---
title: 'South America: SMS Guidelines'
summary: Key Telnyx SMS requirements and restrictions for South American countries
  and nearby territories, including Sender ID behavior, any registration needs, delivery
  receipt nuances, timing and consent rules, and notable carrier exceptions. Always
  review Telnyx’s Acceptable Use Policy for Messaging before sending.
sources:
- url: https://support.telnyx.com/en/articles/6531712-brazil-sms-guidelines
- url: https://support.telnyx.com/en/articles/6534652-colombia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564188-argentina-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564249-bolivia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564549-peru-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570309-uruguay-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570320-paraguay-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570364-chile-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570385-ecuador-sms-guidelines
- url: https://support.telnyx.com/en/articles/6573669-venezuela-sms-guidelines
- url: https://support.telnyx.com/en/articles/6589563-suriname-sms-guidelines
- url: https://support.telnyx.com/en/articles/6671856-guyana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670802-french-guyana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670750-falkland-islands-sms-guidelines
updated_at: 2026-05-21T08:16:51Z
---

# South America: SMS Guidelines

Key Telnyx SMS requirements and restrictions for South American countries and nearby territories, including Sender ID behavior, any registration needs, delivery receipt nuances, timing and consent rules, and notable carrier exceptions. Always review Telnyx’s Acceptable Use Policy for Messaging before sending.

## Overview
- Across much of South America, alphanumeric (alpha) Sender IDs are either not supported or are overwritten to a local long code or a Telnyx [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.
- Some destinations fully support alphanumeric Sender IDs without registration; a few have partial support with network-specific exceptions.
- Observe local content and consent rules where applicable. In all cases, comply with Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.

## Country-specific requirements
### Argentina
- MCC: 722; Dial Code: 53
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or Short Code to ensure delivery.

### Bolivia
- MCC: 736; Dial Code: 591
- Sender ID: Alphanumeric Sender IDs are not supported and cannot be registered. All alphas are overwritten to a random local long code or Short Code to ensure delivery.

### Brazil
- MCC: 724; Dial Code: 55
- Sender ID: Alphanumeric Sender IDs are overwritten to a random local long code or Short Code. Registration is not possible.
- Delivery receipts: Brazil supports SMSC-DLR only; handset delivery reports are not available. Positive DLRs should be expected.

### Chile
- MCC: 730; Dial Code: 56
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or Short Code to ensure delivery.

### Colombia
- MCC: 732; Dial Code: 57
- Sender ID: Alphanumeric Sender IDs are overwritten to a random local long code or Short Code.
- Timing for commercial/marketing traffic: Permitted 8:00 a.m.–9:00 p.m. local time. To send outside these hours, explicit end-user consent is required.
- Opt-outs: Must be included, using the keywords “Salir” or “Cancelar.”
- Adult content: Only to users of legal age and only if previously requested by them.

### Ecuador
- MCC: 740; Dial Code: 593
- Sender ID: Partially supported. Registration is not possible. By default, alphanumeric Sender IDs are overwritten to a random local long code or Short Code.
- Exception: Network CNT (74002) maintains alpha Sender IDs and delivers dynamically on this network.

### Falkland Islands
- MCC: 750; Dial Code: 500
- Sender ID: Alphanumeric Sender IDs are supported and maintained; no registration required.
- Content: No specific restrictions noted for this destination (still follow the Acceptable Use Policy).

### French Guyana
- MCC: 742; Dial Code: 594
- Sender ID: Alphanumeric Sender IDs are supported and maintained; no registration required.
- Content: No specific restrictions noted for this destination (still follow the Acceptable Use Policy).

### Guyana
- MCC: 738; Dial Code: 592
- Sender ID: Alphanumeric Sender IDs are supported and maintained; no registration required.
- Content: No specific restrictions noted for this destination (still follow the Acceptable Use Policy).

### Paraguay
- MCC: 744; Dial Code: 595
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or Short Code to ensure delivery.

### Peru
- MCC: 716; Dial Code: 51
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or Short Code to ensure delivery.

### Suriname
- MCC: 746; Dial Code: 597
- Sender ID: Alphanumeric Sender IDs are supported and maintained; no registration required.
- Content: No specific restrictions noted for this destination (still follow the Acceptable Use Policy).

### Uruguay
- MCC: 748; Dial Code: 598
- Sender ID: All alphanumeric Sender IDs are overwritten to a random local long code or Short Code to ensure delivery.

### Venezuela
- MCC: 734; Dial Code: 58
- Sender ID: Partially supported. Registration is not possible. By default, alphanumeric Sender IDs are overwritten to a random local long code or Short Code.
- Exception: Network Movilnet (73406) maintains alpha Sender IDs and delivers dynamically on this network.

## Compliance and best practices
- Always include clear opt-out instructions where required by local regulation (e.g., “Salir” or “Cancelar” in Colombia for Spanish-language audiences).
- Obtain and document consent for marketing, especially when sending outside permitted hours (see Colombia’s rules above as an example).
- Avoid restricted content and follow Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.
- Where alphanumeric Sender IDs are overwritten, plan branding and reply handling accordingly (use local long codes or Short Codes).
