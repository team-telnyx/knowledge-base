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

*Part 4 of 4 — see also: [Part 1](international-did-requirements-and-number-porting--part-1.md), [Part 2](international-did-requirements-and-number-porting--part-2.md), [Part 3](international-did-requirements-and-number-porting--part-3.md)*

This page consolidates Telnyx's documentation requirements for acquiring new DID numbers and porting existing numbers across multiple countries, including Spain, Germany, Austria, Israel, Italy, the Netherlands, Switzerland, the United Kingdom, Bolivia, South Africa, Argentina, and Hungary. It covers identity, business, and address verification requirements, country-specific porting procedures, timelines, and key operational considerations such as contract termination, partial porting, and physical presence rules.

## United Kingdom Number Porting

### Local Number

1. UK template LOA (underlying carrier's name and/or Cupid code must be mentioned, line type {single or multi}, a local address along with a valid postcode is required)
2. Latest invoice with the current carrier

### National / Toll-Free Number

1. UK template LOA (underlying carrier's name and/or Cupid code must be mentioned, a local address along with a valid postcode is required, a billing account number must be included on the LOA)
2. Latest invoice with the current carrier

### Mobile Number

1. LOA
2. Latest invoice
3. PAC number (porting authorization code, an alphanumeric number required when transferring an existing mobile phone number to a new network)

Providing that all documentation is correct and there are no rejections, a UK mobile request submitted before 12 noon local can be ported within the next business day.

### Before Completing the LOA

- All pages on the LOA must be signed, dated, and include the page numbers
- The LOA should be saved in non-editable PDF format
- Fill in the correct details in the designated areas
- The signature should be a valid e-signature or manually signed

### Useful Information for UK Portability

When porting UK numbers, consider the following factors:

- **Number detail**: Confirm whether the numbers are geographic (linked to a specific area in the UK, requiring a local address) or non-geographic (not tied to a specific area, requiring a national address), and whether they are part of a single line (terminating on a single socket, with no associated numbers) or a multi-line (terminating on equipment such as a PBX, which may include associated numbers).
- **Partial porting**: Whether partial porting is possible depends on the current service provider. Most UK carriers do not allow number ranges to be split, meaning the entire range (typically where the first number ends in 0 and the last ends in 9) usually needs to be ported together, along with any associated DIDs. In most cases, a Main Billing Number (BTN) cannot be ported while leaving associated numbers active with the current provider.
- **Underlying carrier**: This refers to the current communications provider, which may not be the company sending the monthly bill if that company is a reseller. A reseller does not have a CUPID code. If the current provider is a reseller, contact them directly to obtain the name of the underlying carrier and/or their CUPID code.
- **Range holder**: The carrier who owns the number block originally, i.e., the assigned block from OFCOM.

### Pre-Order Validation Process

If you are unsure of the information currently on file with your existing carrier, Telnyx can, depending on the carrier, initiate a Pre-Order Validation (POV) to confirm the details associated with the DID(s). The POV process typically takes between 5 to 7 business days. There are no formal SLAs in place for this process, so it cannot be escalated and is dependent on the current provider's cooperation and response time.

### Time Frame for Local / National / Toll-Free UK Numbers

| Line Type | LCP is RH | LCP is not RH |
| --- | --- | --- |
| Single line | 5 | 7 |
| Multi-line (including associated & other numbers) | 7 | 10 |
| Multi-line (150 lines or less) | 10 | 13 |
| Multi-line (151 lines or more) | 17 | 20 |
| Complex DDI | 22 | 25 |

These time frames are expected SLAs between carriers. In the event of no response from the losing communications provider or the range holder within the time frame above, an escalation will be made to the relevant party.

### Time and Date of Port

It is possible to request a specific porting date; this date must fall within the time frame outlined above. If the requested porting date and time do not comply with the applicable SLAs, the team will proceed by submitting the request for the earliest available date provided by the losing carrier.

The standard activation time for local and national ports is 10:00 AM GMT. All toll-free ports, unless otherwise specified, take place between 00:00 and 04:00 AM GMT on the FOC date. However, this does not mean that the number will port at that specific time on FOC; in the UK, porting can take up to six hours to complete once it has been triggered. If, on the FOC date, the losing communications provider does not release the numbers, the team will follow up with the carrier every two hours until completion.

### Port Date Changes After FOC

Once a port has reached FOC Confirmed status, it is possible to request a change to the porting date if an issue arises. Any date change requested after submission to the current carrier incurs a fee of $40 per order. If the losing communications provider is the range holder, a minimum of 24 hours' notice prior to the FOC date is required to postpone the port. If the losing communications provider is not the range holder, a minimum of 72 hours' notice prior to the FOC date is required.

See also [United Kingdom Number Porting](united-kingdom-number-porting.md).

## South Africa Number Porting

### Local Number Type

1. LOA (local address is required)
2. Latest invoice
3. ID / passport copy
4. Company registration certificate
5. Proof of address

### National / Toll-Free Number Type

1. LOA (national address is required) — for requests made on behalf of a company, the LOA must be signed by an authorized person (no e-signatures) and either issued on that company's letterhead or include a company stamp
2. Latest invoice
3. ID / passport copy
4. Company registration certificate
5. Proof of address

Details of DSL functionality or any other services linked to the line must be confirmed in the service request. If this information is not provided to Telnyx and there are services on the line, these will be lost and will not be recoverable after the port takes place. In the case of special services linked to the line, confirm a number that will remain with the losing communications carrier to link the services on.

See also [South Africa Number Porting](south-africa-number-porting.md).

## Hungary Number Porting

For all number types in Hungary:

1. LOA with account number
2. VAT / TAX ID
3. Latest invoice
4. Company registration certificate
5. Passport or ID copy of the authorized person

Contact porting@telnyx.com for the LOA template for porting in Hungary.

See also [Hungary Number Porting](hungary-number-porting.md).

## Additional Resources

- [Global DID Numbers](https://telnyx.com/products/phone-numbers)
- [Number Pricing](https://telnyx.com/pricing/numbers)
- [Number Feature Availability by Country](https://telnyx.com/global-coverage)
- [What is direct inward dialing](https://telnyx.com/resources/what-is-direct-inward-dialing)
- [SIP vs DID](https://telnyx.com/resources/sip-did)
- [How to get a VoIP number](https://telnyx.com/resources/how-to-get-a-voip-number)
- [How to setup SIP trunk](https://telnyx.com/resources/how-to-setup-sip-trunk)
