---
title: 'Europe Number Porting: Country Requirements and Key Rules'
summary: This guide consolidates Telnyx’s public requirements and special rules for
  porting Local, National, Toll-Free, and select mobile numbers across key European
  countries, with links to the correct Letters of Authorization (LoA) and important
  timing, address, and documentation caveats.
sources:
- url: https://support.telnyx.com/en/articles/3266409-austria-number-porting
- url: https://support.telnyx.com/en/articles/3266421-belgium-number-porting
- url: https://support.telnyx.com/en/articles/3266956-france-number-porting
- url: https://support.telnyx.com/en/articles/3266960-germany-number-porting
- url: https://support.telnyx.com/en/articles/3266983-ireland-number-porting
- url: https://support.telnyx.com/en/articles/3267012-italy-number-porting
- url: https://support.telnyx.com/en/articles/3267124-netherlands-number-porting
- url: https://support.telnyx.com/en/articles/3267595-spain-number-porting
- url: https://support.telnyx.com/en/articles/3267626-switzerland-number-porting
- url: https://support.telnyx.com/en/articles/3267693-united-kingdom-number-porting
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5188555-luxembourg-number-porting
updated_at: 2026-05-20T15:47:35Z
---

# Europe Number Porting: Country Requirements and Key Rules

*Part 2 of 2 — see also: [Part 1](europe-number-porting-country-requirements-and-key-rules--part-1.md)*

This guide consolidates Telnyx’s public requirements and special rules for porting Local, National, Toll-Free, and select mobile numbers across key European countries, with links to the correct Letters of Authorization (LoA) and important timing, address, and documentation caveats.

## Portugal
- Local/National: LoA with a local address (must match the city/number prefix) and wet signature, latest invoice, passport/ID of authorized person, power of attorney (proves signer’s authority), CVP (Portability Validation Code/migration code), TAX/VAT ID, proof of address.
- Notes: Telnyx does not support portability for PT local “Mainline” numbers with associated services—porting a DID may cancel those services at the current provider. Outage during porting may occur (window up to ~3 hours; typically ≤30 minutes; often smooth).
- LoA: https://assets.ctfassets.net/taysl255dolk/1Oaa0QNqequee3pdi3izCY/1e82e26ba0ef6789315a0f0d19e20188/Loa_-_Telnyx-_Portugal__PRT_.pdf

## Spain
- Local/National/Toll-Free: LoA, CIF/NIF, latest invoice, authorized person’s ID/passport copy, number type, proof of address.
- Number type (select one): Analog Geographic (AG) for simple geographic numbers; PBX Geographic (PBX G) for PBX-associated numbers; Intelligent Network (IN) for VoIP numbers.
- LoA: https://assets.ctfassets.net/taysl255dolk/4mfyR6jMGb8TvN0p5GQOUZ/b98742b348ba0c623ffab3d99ba3db31/TELNYX_ES_LOA.pdf

## Switzerland
- Local/National: LoA (must include desired port date; wet signature required; business signer must have full authority), latest invoice, VAT/TAX ID, proof of address dated within the last 3 months (e.g., invoice/utility/insurance).
- Toll-Free: LoA (must include desired port date), latest invoice, ownership proof from BAKOM (with reference number).
- DDI ranges: A single number within a DDI range cannot port alone. Port at least 10 successive numbers (or multiples thereof), with the first ending in 0 and the last in 9. Confirm specifics with the current provider.
- LoA: https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf

## United Kingdom
- Local (Geographic): UK template LoA (include underlying carrier name and/or CUPID code; specify line type single/multi; provide local address with valid postcode), latest invoice.
- National/Toll-Free: UK template LoA (include underlying carrier name and/or CUPID; local address with valid postcode; include Billing Account Number), latest invoice.
- Mobile: LoA, latest invoice, PAC (Porting Authorization Code for mobile). If submitted before 12:00 local and clean, mobile can port next business day.
- LoA completion tips: All pages must be signed/dated with page numbers, saved as non-editable PDF, completed accurately, and signed (valid e-signature or manual).
- LoA: https://assets.ctfassets.net/taysl255dolk/4e1xrif0j3u8PU1qrl6GY5/bc86537edcb4e1f903da88ea986bd293/TELNYX_-_UK_CLOA_2023.pdf
- Number details to confirm: Type (Geographic requires local address; Non-Geographic requires national address) and line type (Single vs. Multi-line/PBX with associated numbers).
- Partial porting: Case-by-case with current provider. Most carriers won’t split ranges; typically the full 0–9 block (and associated DIDs) must port together. A BTN generally can’t port while leaving associated numbers active—include them or cease with the current provider.
- Underlying carrier vs. reseller: If billed by a reseller (no CUPID), obtain the true underlying carrier name and/or CUPID. Know the Range Holder (original OFCOM assignee).
- Pre-Order Validation (POV): Where supported, Telnyx can validate on-file details. Typical 5–7 business days; no formal SLAs and not escalable; depends on losing provider responsiveness.
- Timeframes (expected SLAs; business days):
  - Single line: 5 (if LCP is Range Holder), 7 (if not).
  - Multi-line (including associated & other numbers): 7 (LCP is RH), 10 (not).
  - Multi-line ≤150 lines: 10 (LCP is RH), 13 (not).
  - Multi-line ≥151 lines: 17 (LCP is RH), 20 (not).
  - Complex DDI: 22 (LCP is RH), 25 (not).
- Port timing: You may request a specific date within SLA windows. Standard activation for Local/National is 10:00 GMT; Toll-Free generally 00:00–04:00 GMT on FOC. Actual cutover can take up to 6 hours after trigger. If the losing provider doesn’t release, Telnyx chases every 2 hours until completion.
- Date changes after FOC: $40 per order. If LCP is Range Holder, provide ≥24 hours’ notice; if not, ≥72 hours’ notice.
