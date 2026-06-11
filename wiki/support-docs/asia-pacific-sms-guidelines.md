---
title: Asia-Pacific SMS Guidelines
summary: Country-specific SMS guidelines for Asia-Pacific destinations on the Telnyx
  platform, covering Alphanumeric Sender ID support, registration requirements, content
  restrictions, and compliance recommendations.
sources:
- url: https://support.telnyx.com/en/articles/6592387-afghanistan-sms-guidelines
  content_hash: dc5459d3ea09d257d00806b68dd1c9db375a4f6877304ac310f72b6b86840c4e
- url: https://support.telnyx.com/en/articles/6601049-cambodia-sms-guidelines
  content_hash: fbf14ace5cf39102c0e84306455c10a588f784501632315004e9e725ee00b0e7
- url: https://support.telnyx.com/en/articles/6601144-china-sms-guidelines
  content_hash: b0a817380cd4b231d0aab587154fef28d1e95e423098d19a7d0f4b920f071b29
- url: https://support.telnyx.com/en/articles/6670784-fiji-sms-guidelines
  content_hash: 61ef6441a885f075dab202bda678e7bb1306745308e052f4fc7c136bb7fb64e6
- url: https://support.telnyx.com/en/articles/6674383-india-sms-guidelines
  content_hash: ec27a5a0a23528ef258ce86cb5d19f03318e77dd2ec71e056e5bd2fc33ac69c7
- url: https://support.telnyx.com/en/articles/6674396-indonesia-sms-guidelines
  content_hash: acaa45beaa4a589c02d3e9e8a815658d931709caeb41596d9988867a6a8feb6c
- url: https://support.telnyx.com/en/articles/6674798-laos-pdr-sms-guidelines
  content_hash: b339cb32020b57414b978f8231c26ceb9334e09d969ee9924d210337c013ce44
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
  content_hash: fb5aa51b6537bdd3e3b0f9bfb3802f35b6dce1d9d2f933447a74a5b931e20c4f
- url: https://support.telnyx.com/en/articles/6675110-malaysia-sms-guidelines
  content_hash: 6d2a80375e758f730fbce77163c6a5ff9524537aabed9522e0b7c59502ef91af
- url: https://support.telnyx.com/en/articles/6675222-maldives-sms-guidelines
  content_hash: 02f4d0ff6d561aa5489e716bb94493cc98220263dac8649b4bfccdf37bdd31d9
- url: https://support.telnyx.com/en/articles/6677958-mongolia-sms-guidelines
  content_hash: 773fc476d73385c3b826cfffb546002d1fceeb540e0d55a8162336fb6de07cf8
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
  content_hash: 89c828d0068e70b73d931e6615ab7d9b13ef20742033e34be746fbfbaab450fc
- url: https://support.telnyx.com/en/articles/6679279-papua-new-guinea-sms-guidelines
  content_hash: 38b70780bb4a3b1ae830bc201311eb00cb4b7a7eeba4382bc3edab5114dc74f9
- url: https://support.telnyx.com/en/articles/6680123-solomon-islands-sms-guidelines
  content_hash: a4ebeec5413d60a708281ff946fa05224b49d2216dded909b119383f3de8663c
- url: https://support.telnyx.com/en/articles/6680171-sri-lanka-sms-guidelines
  content_hash: d452fbacef622847fae0147b5ff981bad1b843fb33cc3e6117934ae344a78f78
- url: https://support.telnyx.com/en/articles/6683287-tajikistan-sms-guidelines
  content_hash: 41613eb150f97d7b39677b4643ed1a461f9655338cd95a92a81f94d9057dd7b2
- url: https://support.telnyx.com/en/articles/6683340-timor-leste-sms-guidelines
  content_hash: b1316ca05507633ce80de3c6ae9488076db673592dbfb24b032ed37a5a5f502c
updated_at: 2026-06-11T11:21:48Z
---

# Asia-Pacific SMS Guidelines

Country-specific SMS guidelines for Asia-Pacific destinations on the Telnyx platform, covering Alphanumeric Sender ID support, registration requirements, content restrictions, and compliance recommendations.

## Country Reference Table

| Country | MCC | Dial Code | Alpha Sender ID Support | Registration Required |
|---|---|---|---|---|
| Afghanistan | 412 | 93 | Supported | Yes |
| Cambodia | 456 | 855 | Supported | No |
| China | 460 | 86 | Not supported | N/A |
| Fiji | 542 | 679 | Supported | No |
| India | 404–405 | 91 | Partial (local entities only) | Yes (DLT registration) |
| Indonesia | 510 | 62 | Supported | Yes |
| Laos PDR | 457 | 856 | Supported | No |
| Macao | 455 | 853 | Supported | No |
| Malaysia | 502 | 60 | Overwritten to Short Code | N/A |
| Maldives | 472 | 960 | Supported | No |
| Mongolia | 428 | 976 | Supported | No |
| Nepal | 429 | 977 | Supported (conditional) | Yes (for Ncell network) |
| Papua New Guinea | 537 | 675 | Supported | No |
| Solomon Islands | 540 | 677 | Supported | No |
| Sri Lanka | 413 | 94 | Supported | Yes |
| Tajikistan | 436 | 992 | Supported | Yes |
| Timor-Leste | 514 | 670 | Supported | No |

## Alphanumeric Sender ID Registration

Registration is required for Afghanistan, Indonesia, Sri Lanka, and Tajikistan. All messages from unregistered Sender IDs will be rejected in these countries.

To register, submit the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/content type
3. Message/content example
4. Company name (and brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Sender ID is not clear, provide additional supporting documentation detailing your business case.

### India — DLT Registration

India supports Alphanumeric Sender IDs only for local entities through the DLT registration process. International Alphanumeric Sender IDs cannot be registered and will be overwritten to a random Short Code to ensure delivery.

### Nepal — Ncell Network Registration

For Nepal's Ncell network (MCC 42902), Alphanumeric Sender IDs require registration. Without registration to this network, Alpha Senders will be overwritten to generic Alpha Sender IDs or will not deliver at all. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.

## Countries Without Alpha Sender ID Support

### China

Alphanumeric Sender IDs are not supported. All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery. All message content must be whitelisted by local operators; it is highly advised to pre-register message content templates. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for content whitelisting.

### Malaysia

All Alphanumeric Sender IDs will be overwritten to a Short Code to ensure delivery. Additional rules apply (see Content Restrictions below).

## Countries With Supported Alpha Sender IDs (No Registration)

The following countries support Alphanumeric Sender IDs without registration, and they will be maintained as sent:

- **Cambodia** — No content restrictions.
- **Fiji** — No content restrictions.
- **Laos PDR** — No content restrictions.
- **Maldives** — No content restrictions.
- **Mongolia** — No content restrictions.
- **Papua New Guinea** — No content restrictions.
- **Solomon Islands** — No content restrictions.

### Macao

Alphanumeric Sender IDs are supported without registration, but they can be overwritten to a random Hong Kong Long Code to ensure delivery towards the China Telecom network (45507). No content restrictions apply.

### Timor-Leste

Alphanumeric Sender IDs are supported without registration, but they may occasionally be overwritten to a random Short Code to ensure delivery.

## Content Restrictions

### China

All message content must be whitelisted by local operators. Pre-register message content templates to ensure delivery.

### Indonesia

Religious, gambling, political, or adult traffic is prohibited.

### Malaysia

- Message content must start with the header "RM0.00", "RM0.0", or "RM0". If this header is not included, local operators will add it, which can disrupt total message content length.
- Content must include a brand/identifier or company name. Without this, operators can filter traffic or impose fines for non-compliant traffic.
- Any messages containing URLs as part of the message body will be blocked.

### Sri Lanka

Network Mobitel (41301) only allows OTP and transactional traffic. Messages carrying non-OTP traffic will be rejected by the network. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.

## Compliance Recommendations

The following best practices apply across all destinations requiring registration (Afghanistan, Indonesia, Sri Lanka, Tajikistan):

- **Consent:** Obtain proof of opt-in before sending any communications, especially marketing SMS.
- **Opt-out:** Traffic should include clear opt-out options.

Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging) for all destinations.

For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Related Pages

- [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md)
- [SMS Short Codes](sms-short-codes.md)
