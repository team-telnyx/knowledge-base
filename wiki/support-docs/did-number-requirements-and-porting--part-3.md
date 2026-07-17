---
title: DID Number Requirements and Porting
summary: Consolidated reference for Telnyx DID number purchase requirements and number
  porting requirements across multiple countries, including Italy, Sweden, Switzerland,
  Denmark, Norway, Portugal, Iceland, South Africa, Zambia, Mozambique, Angola, Spain,
  and Portugal. Covers identity, business, and address verification requirements by
  number type, the mandatory Requirement Groups framework for several European countries,
  and porting documentation for Spain, South Africa, and Portugal.
sources:
- url: https://support.telnyx.com/en/articles/10058901-zambia-did-requirements
- url: https://support.telnyx.com/en/articles/11843417-mozambique-did-requirements
- url: https://support.telnyx.com/en/articles/1311462-italy-did-requirements
- url: https://support.telnyx.com/en/articles/1311477-sweden-did-requirements
- url: https://support.telnyx.com/en/articles/3267595-spain-number-porting
- url: https://support.telnyx.com/en/articles/3739458-iceland-did-requirements
- url: https://support.telnyx.com/en/articles/3739576-south-africa-did-requirements
- url: https://support.telnyx.com/en/articles/3739580-switzerland-did-requirements
- url: https://support.telnyx.com/en/articles/4400326-south-africa-number-porting
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5464149-denmark-did-requirements
- url: https://support.telnyx.com/en/articles/5466855-norway-did-requirements
- url: https://support.telnyx.com/en/articles/5466980-portugal-did-requirements
- url: https://support.telnyx.com/en/articles/6129696-angola-did-requirements
updated_at: 2026-07-17T08:59:22Z
---

# DID Number Requirements and Porting

*Part 3 of 3 — see also: [Part 1](did-number-requirements-and-porting--part-1.md), [Part 2](did-number-requirements-and-porting--part-2.md)*

Consolidated reference for Telnyx DID number purchase requirements and number porting requirements across multiple countries, including Italy, Sweden, Switzerland, Denmark, Norway, Portugal, Iceland, South Africa, Zambia, Mozambique, Angola, Spain, and Portugal. Covers identity, business, and address verification requirements by number type, the mandatory Requirement Groups framework for several European countries, and porting documentation for Spain, South Africa, and Portugal.

## Zambia

### Mobile Numbers

For **personal identity** verification:

- Name, last name
- Contact phone number
- Contact e-mail
- Passport or ID copy

For **business identity** verification:

- Name, last name of an authorized representative
- Contact phone number
- Contact e-mail
- Company name
- Company registration certificate

For **address** verification:

- Address in Zambia (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

Additional information:

- Service usage description

Once documentation is received, it takes approximately 72 hours to validate the information and activate the number for use.

## Mozambique

### Mobile Numbers

For **personal identity** verification:

- Name, last name
- Contact phone number
- Passport or ID copy
- LOI (provided by Telnyx — [LOI Template.docx](https://downloads.intercomcdn.com/i/o/ltcafuzd/1974079146/f3eb9460203bfedda610a97379a8/LOI+Template.docx))

For **business identity** verification:

- Name, last name of an authorized representative
- Company name
- Contact phone number
- Company registration certificate
- LOI (provided by Telnyx — [LOI Template.docx](https://downloads.intercomcdn.com/i/o/ltcafuzd/1974079146/f3eb9460203bfedda610a97379a8/LOI+Template.docx))

For **address** verification:

- Worldwide Address (street, building number, postal code, city and country)
- Proof of address (dated within 3 months)

## Angola

### Local Numbers

For **personal identity** verification:

- Name, last name
- Contact phone number
- Passport or ID copy

For **business identity** verification:

- Company name
- Contact phone number
- Company registration certificate

For **address** verification:

- Address Worldwide (street, building number, postal code, city and country)

## Number Porting

### Spain

For **Local, National and Toll-free numbers**:

1. LOA
2. CIF/NIF
3. Latest Invoice
4. Copy of Authorized person Passport/ID
5. Number Type
6. Proof of address

**Number Type** options:

- **Analog Geographic (AG)** — Select this option if the port request is a simple port of a geographic number with no associated services.
- **PBX Geographic (PBX G)** — Select this option if the port request is for number(s) part of a PBX extension.
- **Intelligent Network (IN)** — Select this option if the port request is for [VoIP number](https://telnyx.com/resources/voip-number)(s).

Download the Spain LOA [here](https://assets.ctfassets.net/taysl255dolk/4mfyR6jMGb8TvN0p5GQOUZ/b98742b348ba0c623ffab3d99ba3db31/TELNYX_ES_LOA.pdf).

### South Africa

For **Local Number type**:

1. LOA (local address is required)
2. Latest Invoice
3. ID / Passport copy
4. Company Registration certificate
5. Proof of address

For **National / Toll-Free Number type**:

1. LOA (National address is required) — For requests made on behalf of a company, the LOA must be signed by an Authorized Person (no E-signatures) and either issued on that company's letterhead or include a company stamp.
2. Latest Invoice
3. ID / Passport copy
4. Company Registration certificate
5. Proof of address

Download the South Africa LOA [here](https://www.dropbox.com/s/fvfhmlarpen9ucb/SouthAfrica-portingform.pdf?dl=0).

Please note: Details of DSL functionality or any other services linked to the line must be confirmed in the service request. If this information is not provided to Telnyx and there are services on the line, these will be lost and will not be recoverable after the port takes place. In the case of special services linked to the line, please confirm a number that will remain with the losing communications carrier, to link the services on.

### Portugal

For **Local / National Number in Portugal**:

1. LoA with a local address within the city as the number prefix is mandatory; the LoA must be signed with a wet signature.
2. Copy of the Latest Invoice
3. Copy of the Passport / ID of the Authorized Person
4. Power of attorney (any document that proves the Authorized Person who signed the LoA has the power to do it in the name of the company)
5. CVP (Portability Validation Code / Migration code)
6. TAX ID / VAT
7. Proof of address

Please note:

- Telnyx does not currently support Number Portability for PT local Mainline numbers with associated services. If the DID is ported to Telnyx, it will cancel the local services delivered by the current provider.
- Outage during the porting may occur. The number(s) may be out of service all the porting window time for approximately 3 hours; usually the loss of service lasts a maximum of 30 minutes or most are smooth transfers.

Download the Portugal LoA [here](https://assets.ctfassets.net/taysl255dolk/1Oaa0QNqequee3pdi3izCY/1e82e26ba0ef6789315a0f0d19e20188/Loa_-_Telnyx-_Portugal__PRT_.pdf).

## Additional Resources

- Product Info: [Global DID Numbers](https://telnyx.com/products/phone-numbers)
- Pricing Info: [Number Pricing](https://telnyx.com/pricing/numbers)
- Number Coverage: [Number Feature Availability by Country](https://telnyx.com/global-coverage)
- Blog: [What is direct inward dialing](https://telnyx.com/resources/what-is-direct-inward-dialing)
- Blog: [SIP vs DID](https://telnyx.com/resources/sip-did)
- Blog: [How to get a VoIP number](https://telnyx.com/resources/how-to-get-a-voip-number)

Telnyx continuously expands global calling services for seamless connectivity. Local calls are currently offered in 49 countries and PSTN replacement in 35+ (with more coming soon).
