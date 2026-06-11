---
title: 'Europe: SMS Guidelines'
summary: A consolidated reference of Telnyx SMS guidelines for European destinations,
  covering MCC, dial codes, alphanumeric sender ID support, registration requirements,
  and content restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6531722-italy-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561195-slovenia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561206-hungary-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561237-czech-republic-czechia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561262-romania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563817-greece-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563843-croatia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563862-bulgaria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563879-albania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563890-andorra-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665171-cyprus-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675034-macedonia-north-macedonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677964-montenegro-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683745-serbia-sms-guidelines
updated_at: 2026-06-11T11:19:29Z
---

# Europe: SMS Guidelines

A consolidated reference of Telnyx SMS guidelines for European destinations, covering MCC, dial codes, alphanumeric sender ID support, registration requirements, and content restrictions.

## Quick Reference Table

| Country | MCC | Dial Code | Alpha Sender ID Support | Registration Required? | Content Restrictions |
|---|---|---|---|---|---|
| Albania | 276 | 355 | Supported, maintained | No | None |
| Andorra | 213 | 376 | Supported, maintained | No | None |
| Bulgaria | 284 | 359 | Partial (network-dependent) | Not possible | None noted |
| Croatia | 219 | 385 | Supported, maintained | No | None |
| Cyprus | 357 | 280 | Supported, maintained | No | None |
| Czech Republic (Czechia) | 230 | 420 | Partial (network-dependent) | Possible for some networks | None noted |
| Greece | 202 | 30 | Supported with registration | Yes | Opt-in and opt-out recommended |
| Hungary | 216 | 36 | Not supported (overwritten) | N/A | None noted |
| Italy | 222 | 39 | Supported, maintained | No | None |
| Montenegro | 297 | 382 | Supported, maintained | No | None |
| North Macedonia | 294 | 389 | Supported (occasionally replaced) | No | None |
| Romania | 226 | 40 | Partial (network-dependent) | No | URLs may be blocked |
| Serbia | 220 | 381 | Supported with registration | Yes (monthly fees apply) | None noted |
| Slovenia | 293 | 386 | Supported, maintained | No | None |

## Full Alphanumeric Sender ID Support

The following countries support alphanumeric sender IDs without any registration requirement. Sender IDs are maintained as sent and there are no content restrictions:

- **Albania** (MCC 276, Dial Code 355)
- **Andorra** (MCC 213, Dial Code 376)
- **Croatia** (MCC 219, Dial Code 385)
- **Cyprus** (MCC 357, Dial Code 280)
- **Italy** (MCC 222, Dial Code 39)
- **Montenegro** (MCC 297, Dial Code 382)
- **Slovenia** (MCC 293, Dial Code 386)

**North Macedonia** (MCC 294, Dial Code 389) also supports alphanumeric sender IDs without registration, but they may occasionally be replaced by a generic alphanumeric sender ID to ensure delivery.

## Partial Alphanumeric Sender ID Support

### Bulgaria (MCC 284, Dial Code 359)

Alphanumeric sender IDs are partially supported; registration is not possible. Behaviour varies by network:

- **Maintained** on Vivacom (28403) and Telenor (28405)
- **Overwritten** to a random local long code, short code, or generic alphanumeric sender ID on A1 (28401)

### Czech Republic / Czechia (MCC 230, Dial Code 420)

Alphanumeric sender IDs are partially supported. Registration is possible towards T-Mobile (23001) and O2 (23002). Without registration to these networks, alphanumeric sender IDs may be overwritten to a random short code or a generic sender to ensure delivery. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for registration details.

### Romania (MCC 226, Dial Code 40)

Alphanumeric sender IDs are partially supported:

- **Maintained** on Telekom (22603) and Lycamobile (22616)
- **Overwritten** to a random short code on Vodafone (22601), Orange (22610), and DigiMobil (22605)

Messages containing URLs can be blocked by local operators. URL whitelisting is possible — contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for more information.

## Alphanumeric Sender ID Registration Required

### Greece (MCC 202, Dial Code 30)

Alphanumeric sender ID registration is required. All messages from unregistered sender IDs will be rejected.

To register, send the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/content type
3. Message/content example
4. Company name (and brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested alphanumeric sender ID. If the relationship between your company/brand and the requested sender ID is not clear, provide additional supporting documentation detailing your business case.

**Additional recommendations for Greece:**

- Consent (proof of opt-in) should be obtained before sending any marketing SMS
- Traffic should include clear opt-out options

### Serbia (MCC 220, Dial Code 381)

Alphanumeric sender IDs are supported with registration. Without registration, alpha senders will be overwritten to generic alphanumeric sender IDs. Registration of alphanumeric senders involves monthly fees. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for more information.

## Alphanumeric Sender IDs Not Supported

### Hungary (MCC 216, Dial Code 36)

All alphanumeric sender IDs will be overwritten to either a random local long code or short code to ensure delivery. See [country-specific guidelines for Hungary](https://telnyx.com/country-specific-guidelines) for additional information.

## General Compliance

For all destinations listed above, always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging) to ensure compliance with Telnyx messaging requirements.

For alphanumeric sender ID registration inquiries across any destination, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).
