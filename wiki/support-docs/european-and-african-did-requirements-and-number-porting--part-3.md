---
title: European and African DID Requirements and Number Porting
summary: This page consolidates Telnyx documentation covering DID (Direct Inward Dialing)
  number requirements and number porting procedures for several European and African
  countries, including Italy, Sweden, Switzerland, Denmark, Norway, Portugal, Mozambique,
  and Angola. It also explains the Requirement Groups feature, which became mandatory
  for ordering numbers in six European countries on September 16, 2024.
sources:
- url: https://support.telnyx.com/en/articles/11843417-mozambique-did-requirements
- url: https://support.telnyx.com/en/articles/1311462-italy-did-requirements
- url: https://support.telnyx.com/en/articles/1311477-sweden-did-requirements
- url: https://support.telnyx.com/en/articles/3266720-denmark-number-porting
- url: https://support.telnyx.com/en/articles/3266934-finland-number-porting
- url: https://support.telnyx.com/en/articles/3266983-ireland-number-porting
- url: https://support.telnyx.com/en/articles/3275772-sweden-number-porting
- url: https://support.telnyx.com/en/articles/3739580-switzerland-did-requirements
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5464149-denmark-did-requirements
- url: https://support.telnyx.com/en/articles/5466855-norway-did-requirements
- url: https://support.telnyx.com/en/articles/5466980-portugal-did-requirements
- url: https://support.telnyx.com/en/articles/5720521-estonia-number-porting
- url: https://support.telnyx.com/en/articles/6129696-angola-did-requirements
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-08-05T13:32:26Z
---

# European and African DID Requirements and Number Porting

*Part 3 of 3 — see also: [Part 1](european-and-african-did-requirements-and-number-porting--part-1.md), [Part 2](european-and-african-did-requirements-and-number-porting--part-2.md)*

This page consolidates Telnyx documentation covering DID (Direct Inward Dialing) number requirements and number porting procedures for several European and African countries, including Italy, Sweden, Switzerland, Denmark, Norway, Portugal, Mozambique, and Angola. It also explains the Requirement Groups feature, which became mandatory for ordering numbers in six European countries on September 16, 2024.

## Number Porting

### Denmark Number Porting

For local, national, and toll-free numbers in Denmark:

1. LOA (a local address is mandatory; the signature must be a wet signature)
2. Local TAX ID / VAT
3. Latest invoice with the current provider

### Finland Number Porting

**Local / National Numbers:**

1. LOA
2. VAT/TAX ID or social security number
3. Latest invoice

**Toll-Free Numbers:**

1. LOA
2. VAT/TAX ID or social security number
3. Attorney's authorization for representative (if the number belongs to a company)
4. Latest invoice

**Most common rejections for portability:**

- Wrong end-user on document
- Signature not readable or valid on the LOA

### Ireland Number Porting

For local, national, and toll-free numbers in Ireland:

1. LOA
2. UAN / Account Number (required)
3. Latest invoice

A **UAN** is eight digits in length and can be found on the end-user's invoice. If it is not mentioned on the invoice, the end-user must contact their current provider and request it.

Customers porting away from EIR or Open EIR must confirm with the current provider prior to the port that numbers do not have special services, as these services may be cancelled as a result of the port to Telnyx.

**Porting hours:** Porting hours in Ireland are from 10:00 to 15:30 local time. Telnyx strongly advises against requesting a port to occur after 15:00. If an issue occurs with the port, there is a limited amount of time for escalation within business hours, which may result in the DIDs being down until the following business day.

### Sweden Number Porting

For local, national, and toll-free numbers in Sweden:

1. LOA (a local address is mandatory; the signature must be a wet signature)
2. Local TAX ID / VAT (must be 12 characters long)
3. Latest invoice

### Portugal Number Porting

For local and national numbers in Portugal:

1. LoA with a local address within the city matching the number prefix; the LoA must be signed with a wet signature
2. Copy of the latest invoice
3. Copy of the passport / ID of the authorized person
4. Power of attorney (any document proving the authorized person who signed the LoA has the power to do so in the name of the company)
5. CVP (Portability Validation Code / Migration code)
6. TAX ID / VAT
7. Proof of address

**Please note:**

- Telnyx does not currently support number portability for PT local Mainline numbers with associated services. Porting the DID to Telnyx will cancel the local services delivered by the current provider.
- An outage during the porting may occur. The number(s) may be out of service for the entire porting window (approximately 3 hours), but usually the loss of service lasts a maximum of 30 minutes or is a smooth transfer.

### Estonia Number Porting

For local, national, and toll-free numbers in Estonia:

1. LoA
2. Latest invoice
3. Company registration number if the number belongs to a company, or personal code if the number belongs to a private customer

After the porting request is confirmed (status: FOC confirmed), it will no longer be possible to cancel the port. The number will have to port back to the original carrier after the port is fully executed.

## Benefits of Telnyx DIDs

Telnyx Global DID Numbers are virtual and can be assigned or reassigned to any phone or device. They are flexible, allowing businesses to create unlimited DIDs on a single SIP trunk with few limitations. Telnyx owns and operates its own IP network, so calls bypass congestion on the public internet, making them more secure and reliable.

Key benefits include:

- Potential customers are 400% more likely to answer calls from local numbers.
- Improved call routing where individual DIDs can be assigned to specific business functions.
- Scalability as your business grows.
- Enhanced privacy for individuals.
- Advanced call tracking and analytical capabilities to measure volume, duration, and more.

Telnyx currently offers local calls in 49 countries and PSTN replacement in 35+ countries (with more coming soon).
