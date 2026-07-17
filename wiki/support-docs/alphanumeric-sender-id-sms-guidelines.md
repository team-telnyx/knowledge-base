---
title: Alphanumeric Sender ID SMS Guidelines
summary: Consolidated Telnyx SMS guidelines for destinations where Alphanumeric Sender
  ID handling is the primary compliance consideration. Covers MCC, dial code, registration
  requirements, and destination-specific content restrictions for Bangladesh, Belarus,
  Bhutan, Burundi, Central African Republic, Chad, Comoros, Gabon, Indonesia, Madagascar,
  Myanmar, Niger, Nigeria, Sri Lanka, and Togo.
sources:
- url: https://support.telnyx.com/en/articles/6596161-bangladesh-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596227-belarus-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601042-burundi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601081-central-african-republic-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601133-chad-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601152-comoros-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670834-gabon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674396-indonesia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675096-madagascar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679062-niger-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679084-nigeria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680171-sri-lanka-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683355-togo-sms-guidelines
updated_at: 2026-07-17T09:11:18Z
---

# Alphanumeric Sender ID SMS Guidelines

Consolidated Telnyx SMS guidelines for destinations where Alphanumeric Sender ID handling is the primary compliance consideration. Covers MCC, dial code, registration requirements, and destination-specific content restrictions for Bangladesh, Belarus, Bhutan, Burundi, Central African Republic, Chad, Comoros, Gabon, Indonesia, Madagascar, Myanmar, Niger, Nigeria, Sri Lanka, and Togo.

## Overview

This page consolidates Telnyx SMS guidelines for a set of destinations where Alphanumeric Sender ID handling is the primary compliance consideration. For each country, the Mobile Country Code (MCC), international dial code, and Sender ID policy are listed. Most destinations in this set require Alphanumeric Sender ID registration before traffic can be sent; a small number allow Alphanumeric Sender IDs without registration.

## Destinations Requiring Alphanumeric Sender ID Registration

For the destinations below, Alphanumeric Sender ID registration is required and all messages from unregistered Sender IDs will be rejected. Registration requests, along with a copy of the Business Registration, must be sent to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@mailto:alpha_sender_id@telnyx.com).

| Country | MCC | Dial Code |
| --- | --- | --- |
| Bangladesh | 470 | 880 |
| Belarus | 257 | 375 |
| Bhutan | 402 | 975 |
| Burundi | 642 | 257 |
| Chad | 622 | 235 |
| Comoros | 654 | 269 |
| Gabon | 628 | 241 |
| Indonesia | 510 | 62 |
| Madagascar | 646 | 261 |
| Myanmar | 414 | 95 |
| Niger | 614 | 227 |
| Nigeria | 621 | 234 |
| Sri Lanka | 413 | 94 |

### Information Required for Registration

When submitting a registration request, include the following details along with a copy of the Business Registration:

1. SenderID to be registered
2. Message/Content type
3. Message/Content example
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company Country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between the company/brand and the requested Alphanumeric Sender ID is not clear, additional supporting documentation detailing the business case should be provided.

### General Recommendations

For all destinations in this group, the following best practices apply:

- Consent (proof of opt-in) should be obtained before sending any communications, including marketing SMS.
- Traffic should include clear opt-out options.
- Senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

### Destination-Specific Restrictions

A subset of these destinations imposes additional content or Sender ID rules beyond the standard registration requirements:

- **Indonesia** — Religious, gambling, political, or adult traffic is prohibited.
- **Nigeria** — Religious, gambling, political, or adult traffic is prohibited. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.
- **Sri Lanka** — Network Mobitel (41301) only allows OTP and transactional traffic; messages carrying non-OTP traffic will be rejected by the network. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.

## Destinations Without Registration Requirements

For the destinations below, Alphanumeric Sender IDs are supported and will be maintained without registration. There are no content restrictions for these destinations, but the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) still applies.

| Country | MCC | Dial Code |
| --- | --- | --- |
| Central African Republic | 623 | 236 |
| Togo | 615 | 228 |

## Related Pages

- [Bangladesh: SMS Guidelines](bangladesh-sms-guidelines.md)
- [Belarus: SMS Guidelines](belarus-sms-guidelines.md)
- [Bhutan: SMS Guidelines](bhutan-sms-guidelines.md)
- [Burundi: SMS Guidelines](burundi-sms-guidelines.md)
- [Central African Republic: SMS Guidelines](central-african-republic-sms-guidelines.md)
- [Chad: SMS Guidelines](chad-sms-guidelines.md)
- [Comoros: SMS Guidelines](comoros-sms-guidelines.md)
- [Gabon: SMS Guidelines](gabon-sms-guidelines.md)
- [Indonesia: SMS Guidelines](indonesia-sms-guidelines.md)
- [Madagascar: SMS Guidelines](madagascar-sms-guidelines.md)
- [Myanmar: SMS Guidelines](myanmar-sms-guidelines.md)
- [Niger: SMS Guidelines](niger-sms-guidelines.md)
- [Nigeria: SMS Guidelines](nigeria-sms-guidelines.md)
- [Sri Lanka: SMS Guidelines](sri-lanka-sms-guidelines.md)
- [Togo: SMS Guidelines](togo-sms-guidelines.md)
