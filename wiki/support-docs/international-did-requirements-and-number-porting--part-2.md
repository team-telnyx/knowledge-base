---
title: International DID Requirements and Number Porting
summary: This page consolidates Telnyx's documentation requirements for acquiring
  new DID numbers and porting existing numbers across multiple countries, including
  Spain, Germany, Austria, Israel, Italy, the Netherlands, Switzerland, the United
  Kingdom, Bolivia, South Africa, Argentina, and Hungary. It covers identity, business,
  and address verification requirements, country-specific porting procedures, timelines,
  and key operational considerations such as contract termination, partial porting,
  and physical presence rules.
sources:
- url: https://support.telnyx.com/en/articles/1311073-spain-did-requirements
- url: https://support.telnyx.com/en/articles/1311450-germany-did-requirements
- url: https://support.telnyx.com/en/articles/3266409-austria-number-porting
- url: https://support.telnyx.com/en/articles/3266960-germany-number-porting
- url: https://support.telnyx.com/en/articles/3266993-israel-number-porting
- url: https://support.telnyx.com/en/articles/3267012-italy-number-porting
- url: https://support.telnyx.com/en/articles/3267124-netherlands-number-porting
- url: https://support.telnyx.com/en/articles/3267626-switzerland-number-porting
- url: https://support.telnyx.com/en/articles/3267693-united-kingdom-number-porting
- url: https://support.telnyx.com/en/articles/3506001-bolivia-did-requirements
- url: https://support.telnyx.com/en/articles/3739576-south-africa-did-requirements
- url: https://support.telnyx.com/en/articles/3760805-argentina-did-requirements
- url: https://support.telnyx.com/en/articles/4400326-south-africa-number-porting
- url: https://support.telnyx.com/en/articles/5188524-hungary-number-porting
- url: https://support.telnyx.com/en/articles/5463877-austria-did-requirements
updated_at: 2026-08-05T13:33:11Z
---

# International DID Requirements and Number Porting

*Part 2 of 4 — see also: [Part 1](international-did-requirements-and-number-porting--part-1.md), [Part 3](international-did-requirements-and-number-porting--part-3.md), [Part 4](international-did-requirements-and-number-porting--part-4.md)*

This page consolidates Telnyx's documentation requirements for acquiring new DID numbers and porting existing numbers across multiple countries, including Spain, Germany, Austria, Israel, Italy, the Netherlands, Switzerland, the United Kingdom, Bolivia, South Africa, Argentina, and Hungary. It covers identity, business, and address verification requirements, country-specific porting procedures, timelines, and key operational considerations such as contract termination, partial porting, and physical presence rules.

## South Africa DID Requirements

### Local Numbers

For **personal identity** verification:
- Name, last name
- Contact phone number
- Passport or South African ID copy

For **business identity** verification:
- Name, last name of an authorized representative
- Contact phone number
- Passport or South African ID copy of an authorized representative
- Company name
- Company registration certificate

For **address** verification:
- Address matching the DID area code (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

### National Numbers

For **personal identity** verification:
- Name, last name
- Contact phone number
- Passport or South African ID copy

For **business identity** verification:
- Name, last name of an authorized representative
- Contact phone number
- Passport or South African ID copy of an authorized representative
- Company name
- Company registration certificate

For **address** verification:
- Address within the country (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

### Mobile Numbers

For **personal identity** verification:
- Name, last name
- Contact phone number
- Passport or ID copy

For **business identity** verification:
- Name, last name of an authorized representative
- Company name
- Contact phone number
- Company registration certificate

For **address** verification:
- Address worldwide (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

### Toll-Free Numbers

For **personal identity** verification:
- Name, last name
- Contact phone number
- Passport or South African ID copy
- Signed LOI (dated within 1 month)

For **business identity** verification:
- Name, last name of an authorized representative
- Contact phone number
- Passport or South African ID copy of an authorized representative
- Company name
- Company registration certificate
- Signed LOI (dated within 1 month)

For **address** verification:
- Address worldwide (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

See also [South Africa DID Requirements](south-africa-did-requirements.md).

## Argentina DID Requirements

### Local and Shared-Cost Numbers

For **personal identity** verification:
- Name, last name
- Contact phone number
- Passport or ID copy

For **business identity** verification:
- Company name
- Contact phone number
- Company registration certificate

For **address** verification:
- Address worldwide (street, building number, postal code, city, and country)

### Toll-Free Numbers

For **personal identity** verification:
- Name, last name

For **business identity** verification:
- Company name

For **address** verification:
- Address worldwide (street, building number, postal code, city, and country)

## Austria Number Porting

### Local and National Numbers

1. LOA (local address required)
2. Account number
3. ID / passport copy
4. Company registration certificate
5. Latest invoice
6. Proof of address

### Toll-Free Numbers

1. LOA
2. Current underlying carrier's name
3. Porting history (if the number(s) were ported before)
4. Account number
5. Latest invoice

See also [Austria Number Porting](austria-number-porting.md).

## Germany Number Porting

### Number Length

The length of a number depends on the municipality within Germany and whether extensions are tied to the number(s):
- Numbers in Berlin, Frankfurt, Hamburg, and Munich have a standard length of 10 digits (excluding leading 0)
- Numbers in other municipalities have a standard length of 11 digits (excluding leading 0)

### Extensions

If a number is longer than 10/11 digits (depending on the municipality), it is an extended version of that number, typically a 10-block or 100-block. The whole block extension will not be ported; only the standard number itself will be ported. If you have an extra one or two digits, you must check with the current operator to ensure that these numbers can be ported (10/100 block), and you must be assigned the whole 10/100 block. If not, the port of the standard number will be blocked.

Example: +49 (0) 40 123456781 (Hamburg) is 11 digits long excluding the leading 0/country code. The actual number is +49 (0) 40 12345678, and 6789 are an extension of that number, not the physical number itself.

### Local / National Numbers

1. Porting form (local address from the same city as the number to be ported)
2. Latest invoice (from the current provider(s))
3. Proof of address
4. ID / passport copy / company registration certificate

### Toll-Free Numbers

1. Porting form (local address required within Germany)
2. Latest invoice from the current provider (only if the current provider is a reseller)
3. Number allocation document ("Zuteilungsbescheid")
4. ID / passport copy / company registration certificate

### Porting Hours

Germany porting requests are scheduled during the standard porting window (6 AM local to 8 AM local). On FOC, the port is triggered by Telnyx porting agents with the carrier at 6 AM local, and the carrier has 2 hours to release the number(s). Porting outside of the standard window is not available.

Once a port date has been confirmed with the current carrier, it is possible to change the date (the new date must be set at least 5 business days away from the date change request). A date change after the request has been submitted/confirmed with the current carrier comes with a date change fee.

### Important Notes Before Completing the Porting Form(s)

- Maximum of 10 numbers per porting form and/or 1 range
- For each city being ported, a different form is required, including the address within each city
- For each donor carrier, a different form is required
- Confirm the number(s) details with your current provider
- If there is a connection assigned to the number(s)

### Contract Type

In Germany, you cannot port your numbers until the end of your contract period with the current operator. If you have a future-dated contract in place, you must first notify your carrier of your intent to port your numbers away, as well as any other subsequent actions (cancel access line, etc.), before submitting your port to Telnyx. Depending on the contract in place with your current operator, you may be charged early termination fees. If this is not done prior to submitting the port request to Telnyx, then providing that the information on your port is accepted, the confirmed porting date will be the last day of your contract with your current provider.

### Termination of Connections

If there is a connection assigned to the DID(s), you must ensure you have discussed the details of the port with the current provider prior to submitting a request with Telnyx. Once the DID(s) port to Telnyx, any remaining connection will be terminated.

### Porting Out of Telnyx

The gaining provider must submit a request by email to porting.intl@telnyx.com providing the Standard German Porting Form (the same template required for porting into Telnyx). Once the request is received, Telnyx will create a Port out request in the end-user's Portal. This request must be authorized within 4 business days by the end-user. Once the port out is authorized on the end-user's end, Telnyx will approve the port out with the gaining provider.

See also [Germany Number Porting](germany-number-porting.md).

## Israel Number Porting

### Local / National / Mobile Numbers

1. LOA
2. VAT / TAX ID
3. Latest invoice

If porting a mobile number under a business, the invoice must be from the underlying carrier, and an official proof of ownership signed by the underlying carrier will be required to successfully port the numbers.

See also [Israel Number Porting](israel-number-porting.md).
