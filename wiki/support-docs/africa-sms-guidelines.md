---
title: Africa SMS Guidelines
summary: Consolidated Telnyx SMS guidelines for 15 African destinations, including
  MCC, dial codes, Alphanumeric Sender ID support, registration requirements, network-specific
  rules, and content restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6665699-djibouti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670411-egypt-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670452-eritrea-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670465-ethiopia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670843-gambia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674630-kenya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675247-mali-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675690-mauritania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677982-morocco-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680041-senegal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680089-sierra-leone-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680135-somalia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680141-south-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683295-tanzania-sms-guidelines
updated_at: 2026-07-17T09:11:24Z
---

# Africa SMS Guidelines

Consolidated Telnyx SMS guidelines for 15 African destinations, including MCC, dial codes, Alphanumeric Sender ID support, registration requirements, network-specific rules, and content restrictions.

## Overview

This page consolidates Telnyx SMS guidelines for 15 African destinations, covering Mobile Country Codes (MCC), international dial codes, Alphanumeric Sender ID support, registration requirements, and content restrictions. Use it as a quick reference when planning messaging traffic to these countries.

## Country Reference Table

| Country | MCC | Dial Code | Alpha Sender ID Support | Registration Required |
| --- | --- | --- | --- | --- |
| [Djibouti: SMS Guidelines](djibouti-sms-guidelines.md) | 253 | 638 | Supported and maintained | No |
| [Egypt: SMS Guidelines](egypt-sms-guidelines.md) | 602 | 20 | Supported (Etisalat 60203 requires registration) | Conditional |
| [Eritrea: SMS Guidelines](eritrea-sms-guidelines.md) | 657 | 291 | Supported and maintained | No |
| [Ethiopia: SMS Guidelines](ethiopia-sms-guidelines.md) | 636 | 251 | Supported (MTN 63601 requires registration) | Conditional |
| [Gambia: SMS Guidelines](gambia-sms-guidelines.md) | 628 | 241 | Supported and maintained | No |
| [Kenya: SMS Guidelines](kenya-sms-guidelines.md) | 639 | 254 | Supported with registration | Yes |
| [Mali: SMS Guidelines](mali-sms-guidelines.md) | 610 | 223 | Supported (local traffic requires registration) | Conditional |
| [Mauritania: SMS Guidelines](mauritania-sms-guidelines.md) | 609 | 222 | Supported and maintained | No |
| [Morocco: SMS Guidelines](morocco-sms-guidelines.md) | 604 | 212 | Supported with registration | Yes |
| [Senegal: SMS Guidelines](senegal-sms-guidelines.md) | 608 | 221 | Supported and maintained | No |
| [Sierra Leone: SMS Guidelines](sierra-leone-sms-guidelines.md) | 619 | 232 | Supported and maintained | No |
| [Somalia: SMS Guidelines](somalia-sms-guidelines.md) | 637 | 252 | Supported and maintained | No |
| [South Sudan: SMS Guidelines](south-sudan-sms-guidelines.md) | 659 | 211 | Supported (MTN 65902 requires registration) | Conditional |
| [Sudan: SMS Guidelines](sudan-sms-guidelines.md) | 634 | 249 | Supported (MTN 63402 requires registration) | Conditional |
| [Tanzania: SMS Guidelines](tanzania-sms-guidelines.md) | 640 | 255 | Supported with registration | Yes |

## Sender ID Best Practices

Across all destinations, Telnyx recommends that Alpha Senders be directly related to the message content. The use of generic Alpha Sender IDs is not recommended in Djibouti, Eritrea, Gambia, Mauritania, Senegal, Sierra Leone, Somalia, South Sudan, and Sudan.

## Network-Specific Registration Requirements

Several destinations require Alphanumeric Sender ID registration on specific mobile networks. Without registration, Alpha Senders may be overwritten to Generic Alpha Sender IDs or fail to deliver entirely:

- **Egypt** — Etisalat (MCC-MNC 60203)
- **Ethiopia** — MTN (MCC-MNC 63601)
- **South Sudan** — MTN (MCC-MNC 65902)
- **Sudan** — MTN (MCC-MNC 63402)

For Alpha Sender ID registration requests, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Content Restrictions

- **Djibouti** and **Mauritania** — No content restrictions.
- **Eritrea** and **Gambia** — Religious, political, or adult traffic is prohibited.
- **Ethiopia** — Local banking or promotional traffic is not allowed.
- **Kenya** — Political, religious, gambling, adult, and P2P content is prohibited.
- **Mali** — A distinction is made between local and international traffic; local traffic requires Alpha Sender ID registration while international traffic does not.

## Compliance

All messaging traffic must comply with the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).

## Related Country Pages

- [Djibouti: SMS Guidelines](djibouti-sms-guidelines.md)
- [Egypt: SMS Guidelines](egypt-sms-guidelines.md)
- [Eritrea: SMS Guidelines](eritrea-sms-guidelines.md)
- [Ethiopia: SMS Guidelines](ethiopia-sms-guidelines.md)
- [Gambia: SMS Guidelines](gambia-sms-guidelines.md)
- [Kenya: SMS Guidelines](kenya-sms-guidelines.md)
- [Mali: SMS Guidelines](mali-sms-guidelines.md)
- [Mauritania: SMS Guidelines](mauritania-sms-guidelines.md)
- [Morocco: SMS Guidelines](morocco-sms-guidelines.md)
- [Senegal: SMS Guidelines](senegal-sms-guidelines.md)
- [Sierra Leone: SMS Guidelines](sierra-leone-sms-guidelines.md)
- [Somalia: SMS Guidelines](somalia-sms-guidelines.md)
- [South Sudan: SMS Guidelines](south-sudan-sms-guidelines.md)
- [Sudan: SMS Guidelines](sudan-sms-guidelines.md)
- [Tanzania: SMS Guidelines](tanzania-sms-guidelines.md)
