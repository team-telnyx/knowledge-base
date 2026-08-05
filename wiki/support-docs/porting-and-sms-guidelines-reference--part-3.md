---
title: Porting and SMS Guidelines Reference
summary: A consolidated reference covering Telnyx porting requirements, how to fill
  out and auto-generate a Letter of Authorization (LOA), El Salvador-specific porting
  and DID requirements, and SMS guidelines for a range of countries including Andorra,
  El Salvador, Dominican Republic, Macao, Saint Pierre and Miquelon, Sao Tome and
  Principe, Trinidad & Tobago, Turks and Caicos Islands, and South Korea.
sources:
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/5179083-el-salvador-number-porting
- url: https://support.telnyx.com/en/articles/5464176-el-salvador-did-requirements
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/6563890-andorra-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574078-el-salvador-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665730-dominican-republic-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679441-saint-pierre-and-miquelon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680003-sao-tome-and-principe-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683379-trinidad-tobago-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683396-turks-and-caicos-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683734-korea-sms-guidelines
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
updated_at: 2026-08-05T13:34:48Z
---

# Porting and SMS Guidelines Reference

*Part 3 of 3 — see also: [Part 1](porting-and-sms-guidelines-reference--part-1.md), [Part 2](porting-and-sms-guidelines-reference--part-2.md)*

A consolidated reference covering Telnyx porting requirements, how to fill out and auto-generate a Letter of Authorization (LOA), El Salvador-specific porting and DID requirements, and SMS guidelines for a range of countries including Andorra, El Salvador, Dominican Republic, Macao, Saint Pierre and Miquelon, Sao Tome and Principe, Trinidad & Tobago, Turks and Caicos Islands, and South Korea.

## El Salvador DID Requirements

For local numbers in El Salvador, a traffic forecast is required: a forecast of the expected traffic must be provided.

Telnyx Global DID Numbers are future-ready and start at only $1. DID numbers are virtual and can be assigned or reassigned to any phone or device. They are also flexible, meaning businesses can create unlimited El Salvador DID numbers on a single SIP trunk, with few limitations.

Telnyx continuously expands global calling services for seamless connectivity in El Salvador. Local calls are currently offered in 49 countries and PSTN replacement in 35+ (with more coming soon).

Telnyx streamlines VoIP operations by providing both DID numbers and SIP trunking, which is more affordable, simplifies phone infrastructure, and reduces how many invoices you manage each month. Telnyx owns and operates its own IPs, so calls bypass congestion on the public internet, making them more secure and reliable.

Benefits of El Salvador DIDs:

- Potential customers in El Salvador are 400% more likely to answer calls from local numbers.
- Improve call routing where individual DIDs can be assigned to specific business functions.
- El Salvador DIDs are scalable and grow as your business grows.
- Enhanced privacy for individuals — keep your personal number personal.
- Advanced call tracking and analytical capabilities to measure volume, duration, and more.

## SMS Guidelines by Country

The following table summarizes Telnyx SMS guidelines for the countries covered in this reference. Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).

| Country | MCC | Dial Code | Sender ID Support | Notes |
| --- | --- | --- | --- | --- |
| Andorra | 213 | 376 | Alphanumeric Sender IDs supported and maintained; no registration required | No content restrictions |
| El Salvador | 706 | 503 | Alphanumeric Sender IDs overwritten to a random Local Long Code or Short Code to ensure delivery | — |
| Dominican Republic | 370 | 1809 | Alphanumeric Sender IDs supported; no registration required | Occasionally overwritten to a random Short Code to ensure delivery |
| Macao | 455 | 853 | Alphanumeric Sender IDs supported; registration not necessary | Can be overwritten to a random Hong Kong Long Code to ensure delivery towards Network China Telecom (45507); no content restrictions |
| Saint Pierre and Miquelon | 308 | 508 | Alphanumeric Sender IDs supported and maintained; no registration required | No content restrictions |
| Sao Tome and Principe | 626 | 239 | Alphanumeric Sender IDs supported and maintained; no registration required | No content restrictions |
| Trinidad & Tobago | 374 | 1868 | Alphanumeric Sender IDs supported; no registration required | Occasionally overwritten to a random Long Code to ensure delivery towards Network Bmobile (37412) |
| Turks and Caicos Islands | 376 | 1649 | Alphanumeric Sender IDs supported and maintained; no registration required | No content restrictions |
| Republic of Korea (South Korea) | 450 | 82 | All Alphanumeric Sender IDs overwritten to a random Local Long Code to ensure delivery | All messages have `[Web 발신]` (indicates A2P traffic) and `[국제발신]` (indicates sent from abroad) added by default; gambling and adult content not permitted |

### Country-Specific SMS Notes

- **Andorra:** No content restrictions. See the [SMS API](https://telnyx.com/products/sms-api), [MMS API](https://telnyx.com/products/mms-api), and [messaging pricing](https://telnyx.com/pricing/messaging) for more.
- **El Salvador:** Alphanumeric Sender IDs are overwritten to a random Local Long Code or Short Code to ensure delivery.
- **Dominican Republic:** Alphanumeric Sender IDs are supported with no registration required; occasionally overwritten to a random Short Code to ensure delivery.
- **Macao:** Alphanumeric Sender IDs can be overwritten to a random Hong Kong Long Code to ensure delivery towards Network China Telecom (45507). No content restrictions.
- **Saint Pierre and Miquelon:** Alphanumeric Sender IDs are supported and maintained; no registration required. No content restrictions.
- **Sao Tome and Principe:** Alphanumeric Sender IDs are supported and maintained; no registration required. No content restrictions.
- **Trinidad & Tobago:** Alphanumeric Sender IDs are supported with no registration required; occasionally overwritten to a random Long Code to ensure delivery towards Network Bmobile (37412).
- **Turks and Caicos Islands:** Alphanumeric Sender IDs are supported and maintained; no registration required. No content restrictions. See the [SMS API](https://telnyx.com/products/sms-api), [MMS API](https://telnyx.com/products/mms-api), and [messaging pricing](https://telnyx.com/pricing/messaging) for more.
- **Republic of Korea (South Korea):** All Alphanumeric Sender IDs are overwritten to a random Local Long Code to ensure delivery. All messages have `[Web 발신]` (indicates A2P traffic) and `[국제발신]` (indicates sent from abroad) added by default. Gambling and adult content are not permitted.

## Related Articles

- [How to fill out an LOA](how-to-fill-out-an-loa.md)
- [Porting Requirements](porting-requirements.md)
- [Auto-generated Letter of Authorization (LOA)](auto-generated-letter-of-authorization-loa.md)
- [LOA Template Download](loa-template-download.md)
- [El Salvador Number Porting](el-salvador-number-porting.md)
- [El Salvador DID Requirements](el-salvador-did-requirements.md)
- [Andorra: SMS Guidelines](andorra-sms-guidelines.md)
- [El Salvador: SMS Guidelines](el-salvador-sms-guidelines.md)
- [Dominican Republic: SMS Guidelines](dominican-republic-sms-guidelines.md)
- [Macao: SMS Guidelines](macao-sms-guidelines.md)
- [Saint Pierre and Miquelon: SMS Guidelines](saint-pierre-and-miquelon-sms-guidelines.md)
- [Sao Tome and Principe: SMS Guidelines](sao-tome-and-principe-sms-guidelines.md)
- [Trinidad & Tobago: SMS Guidelines](trinidad-tobago-sms-guidelines.md)
- [Turks and Caicos Islands: SMS Guidelines](turks-and-caicos-islands-sms-guidelines.md)
- [Korea SMS Guidelines](korea-sms-guidelines.md)
