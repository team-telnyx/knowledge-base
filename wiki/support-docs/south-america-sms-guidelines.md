---
title: 'South America: SMS Guidelines'
summary: Key Telnyx SMS requirements and restrictions for South American countries
  and nearby territories, including Sender ID behavior, any registration needs, delivery
  receipt nuances, timing and consent rules, and notable carrier exceptions. Always
  review Telnyx’s Acceptable Use Policy for Messaging before sending.
sources:
- url: https://support.telnyx.com/en/articles/6531712-brazil-sms-guidelines
  content_hash: 20c1b40cc31113ff38e8a0ed52d53d7764dbb839f6b3d77893f2236e9d50020a
- url: https://support.telnyx.com/en/articles/6534652-colombia-sms-guidelines
  content_hash: 7b44def3d3fc1e1f958328181b0ad8753d0529233b6ab74024083accb707e7c0
- url: https://support.telnyx.com/en/articles/6564188-argentina-sms-guidelines
  content_hash: af8ed34e60e491ac151f7becd0a06f27895a39b865530a264fd15c972626311d
- url: https://support.telnyx.com/en/articles/6564249-bolivia-sms-guidelines
  content_hash: 396b1dd909af4a462e00c7f621c908111ff7b7dc4a7e8355c5fca11504d1cdb5
- url: https://support.telnyx.com/en/articles/6564549-peru-sms-guidelines
  content_hash: c2ff6e7772969a9882a6826ffbf450402af8b947b4a7532d0a3dde27ffd722f9
- url: https://support.telnyx.com/en/articles/6570309-uruguay-sms-guidelines
  content_hash: 240c306cfaa6bf66af0c7028a4255f940765406dc02b0d38a2511a1cc8f33d56
- url: https://support.telnyx.com/en/articles/6570320-paraguay-sms-guidelines
  content_hash: f22db735c6dad204ab3611a5b5f1adcd67fe331302994ade8326dbeb9d1ae51f
- url: https://support.telnyx.com/en/articles/6570364-chile-sms-guidelines
  content_hash: 948b830c077f4da50610d0d54bd527496efcadead21fa03406e70d3e6d1c0d11
- url: https://support.telnyx.com/en/articles/6570385-ecuador-sms-guidelines
  content_hash: 264836b5eb568aabfb81f56b8a55b9b41408ad34b5eabc5b2cad7b12235df932
- url: https://support.telnyx.com/en/articles/6573669-venezuela-sms-guidelines
  content_hash: 0448d998c344f8f642d654ec410bbd0e9a1d0e50a2cb275a2379000cc3657663
- url: https://support.telnyx.com/en/articles/6589563-suriname-sms-guidelines
  content_hash: c2761bb11bd086b2ed3300ca518629f603306cbcf2862b30d5393e9d6839f33b
- url: https://support.telnyx.com/en/articles/6671856-guyana-sms-guidelines
  content_hash: 3e3381d673e6d8606d771f80a020a7ac1e4c9dd9f472db1f57e47fa0806a4b6b
- url: https://support.telnyx.com/en/articles/6670802-french-guyana-sms-guidelines
  content_hash: f95b7bc38aabb8c1cbb68f6ce93fd16819531d74adc18c3a5350ae2640c20ec9
- url: https://support.telnyx.com/en/articles/6670750-falkland-islands-sms-guidelines
  content_hash: 4de242c892e8066a60fe04037577bcd8605d87843ee5c8e0ae54d64614a5748b
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
