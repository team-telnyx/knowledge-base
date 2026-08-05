---
title: Messaging Compliance and Registration Reference
summary: A consolidated reference covering Telnyx messaging compliance topics including
  10DLC brand verification, toll-free verification changes, traffic type selection,
  P2P exemption, country-specific SMS guidelines, UK TPS regulations, and DID requirements
  for Bangladesh.
sources:
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
- url: https://support.telnyx.com/en/articles/12748292-bangladesh-did-requirements
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574037-belize-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596161-bangladesh-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679259-palestinian-territory-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680171-sri-lanka-sms-guidelines
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-08-05T13:25:18Z
---

# Messaging Compliance and Registration Reference

*Part 2 of 2 — see also: [Part 1](messaging-compliance-and-registration-reference--part-1.md)*

A consolidated reference covering Telnyx messaging compliance topics including 10DLC brand verification, toll-free verification changes, traffic type selection, P2P exemption, country-specific SMS guidelines, UK TPS regulations, and DID requirements for Bangladesh.

## UK TPS Register Guidelines

The Telephone Preference Service (TPS) is a list of consumers who do not wish to receive unsolicited direct marketing calls. Businesses running marketing campaigns in the UK must screen call lists against the TPS register.

### Legal Framework

The Privacy and Electronic Communications (EC Directive) Regulations 2003 (PECR) complements the UK GDPR and Data Protection Act 2018. It applies to all businesses (including charities and voluntary organizations) making direct marketing calls or sending direct marketing faxes to individuals or corporate subscribers.

### Required Protocol

1. State who is calling (typically the organization name).
2. Display a traceable telephone number on every call.
3. Provide contact details or telephone number if asked.

It is unlawful to call any number registered with TPS or the Corporate Telephone Preference Service (CTPS), or to contact any individual or corporate subscriber who has previously objected. The same applies to faxes via the Fax Preference Service (FPS). The only exception is when the subscriber has consented to receive communications from the organization.

### Enforcement

The Information Commissioner's Office (ICO) is the UK supervisory authority for enforcement. Telephone Preference Service Limited (TPSL), a subsidiary of the Data and Marketing Association (DMA), maintains the TPS, CTPS, and FPS registers under contract with the ICO and supports ICO investigations.

### Data Cleaning Frequency

Clean data as frequently as possible to ensure anyone on the register for 28 days or more is not contacted. A TPS license is required to screen the register; see [TPS license options](https://corporate.tpsonline.org.uk/prices).

## Country-Specific SMS Guidelines

The following countries require alphanumeric Sender ID registration. All messages from unregistered Sender IDs will be rejected. To register, send the required details along with a copy of the Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

### Standard Registration Requirements

For each Sender ID, provide:

1. Sender ID to be registered.
2. Message/content type.
3. Message/content example.
4. Company name (and brand name if different).
5. Website of brand or company.
6. Company country of origin.
7. Expected monthly volumes.
8. Email linked to the Telnyx account.

Companies must have a valid business case for the requested Sender ID. If the relationship between the company/brand and the Sender ID is unclear, additional supporting documentation is required. Consent (proof of opt-in) should be obtained before sending marketing SMS, and traffic should include clear opt-out options. Always refer to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

### Country-Specific Notes

- **Norway (MCC 242, dial code 47):** Messages containing URLs are filtered by local operators; valid URLs can be whitelisted. Lottery and gambling traffic is blocked.
- **Belize (MCC 702, dial code 501):** Standard alphanumeric registration required.
- **Bangladesh (MCC 470, dial code 880):** Standard alphanumeric registration required.
- **Bhutan (MCC 402, dial code 975):** Standard alphanumeric registration required.
- **Hong Kong (MCC 454, dial code 852):** Handsets commonly use the "2 numbers 1 SIM Card" model with one Chinese (+86) and one HK (+85) number, which can cause delivery issues.
- **Myanmar (MCC 414, dial code 95):** Standard alphanumeric registration required.
- **Palestinian Territory (MCC 425, dial code 970):** Personal loans, gambling, adult, and cryptocurrency traffic is prohibited.
- **Sri Lanka (MCC 413, dial code 94):** Network Mobitel (41301) only allows OTP and transactional traffic; non-OTP messages will be rejected. Generic alpha Sender IDs are not recommended; alpha senders should be directly related to message content.

### Spain (MCC 214, dial code 34)

Spain's telecoms regulator, the CNMC, is rolling out a new Alias Registry under Circular 1/2026. Starting September 15, 2026, any alphanumeric Sender ID used to send messages to Spanish numbers (+34) must be registered in advance.

To register, send the following to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

- **Company details:** Full legal company name, NIF/CIF (Spanish tax ID) or EU-VAT number if based outside Spain, and registered company address.
- **Legal representative:** Full name, NIF or passport number, mobile number, and email address.
- **Sender ID details (one set per alias):** Exact alias as it appears in messages, use case (transactional, OTP, marketing, etc.), and planned start and end date. Registrations are valid for a maximum of 24 months.
- **Proof of ownership (one per alias):** Trademark or trade name certificate from OEPM (Spain) or EUIPO (EU); company name certificate from the Spanish Mercantile Registry; or proof of ownership of a `.es` or ICANN-registered domain matching the alias.

## Bangladesh DID Requirements

To purchase a Bangladesh national or mobile number, the following must be provided.

### Business Identity Verification

- Name and last name of an authorized representative.
- Company name.
- Contact phone number.
- Passport or ID copy of an authorized representative.
- Business Registration Certificate.
- Signed LOI (dated within 1 month).

### Address Verification

- Worldwide address (street, building number, postal code, city, and country).
- Proof of address matching the address on the Business Registration Certificate (dated within 3 months).

Business use is required; private use is not allowed. Once documentation is received, validation and number activation take approximately 72 hours.

See also [Russia DID Requirements](russia-did-requirements.md), [South Africa DID Requirements](south-africa-did-requirements.md), [Thailand DID Requirements](thailand-did-requirements.md), [Mozambique DID Requirements](mozambique-did-requirements.md), and [Oman DID Requirements](oman-did-requirements.md).
