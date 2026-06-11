---
title: European Number Porting Requirements
summary: A comprehensive reference for number porting requirements across European
  countries supported by Telnyx, covering required documentation, letter of authorization
  (LOA) templates, porting procedures, and country-specific rules.
sources:
- url: https://support.telnyx.com/en/articles/3266409-austria-number-porting
  content_hash: 82469caddf0b985ff9be106ced7b05eb4963aed5097a16eb9706ae62d5dab023
- url: https://support.telnyx.com/en/articles/3266421-belgium-number-porting
  content_hash: 0351c6e3a5e9ab0ef70989a271040350c6ade7bfeac7ffa1ae3f94f55d093e80
- url: https://support.telnyx.com/en/articles/3266720-denmark-number-porting
  content_hash: 0dcce4fb29ca472e3489ff1951219e954608410956935eebe45e1afca6f1b5e8
- url: https://support.telnyx.com/en/articles/3266934-finland-number-porting
  content_hash: d906bac2ae47ad45de90405df6105f4994a8947416c1ea04a8e59968e45392ba
- url: https://support.telnyx.com/en/articles/3266956-france-number-porting
  content_hash: bd375f2bf0a88b526eca1bdc985ddfc4c218ae50c7e16c1b61ada40421baf5b0
- url: https://support.telnyx.com/en/articles/3266960-germany-number-porting
  content_hash: 70268072127acd5897ccf0c242036ccef92ad73672f3b63b41749946fc288a20
- url: https://support.telnyx.com/en/articles/3266983-ireland-number-porting
  content_hash: 7d2314f80660aeb69419d220d5f5bbd151d0ef33b1bd290b5d46317e80b0f878
- url: https://support.telnyx.com/en/articles/3267012-italy-number-porting
  content_hash: b6e30e31e661f8466c8079ee4238ca2f32d8949d8828c3cd28593abfd26e99ef
- url: https://support.telnyx.com/en/articles/3267124-netherlands-number-porting
  content_hash: 499404ea49b980c7605fa7d7f974da472fa48569e78cd14247a16348bf0c31d9
- url: https://support.telnyx.com/en/articles/3267566-cyprus-number-porting
  content_hash: 825501aa920f46d2378d4b74fc24632fedc4d0c3f10356e9a8acb5cc0696b4e3
- url: https://support.telnyx.com/en/articles/3267595-spain-number-porting
  content_hash: 1df43f9d77a27b583eaab7bc08a4be062afbe7d3b739e2e395ebeccd7b8e6707
- url: https://support.telnyx.com/en/articles/3267626-switzerland-number-porting
  content_hash: 17a9605b07c1944d81eb45cdbd06f61d6c36e599dc52409dbf680f3aa914c927
- url: https://support.telnyx.com/en/articles/3267693-united-kingdom-number-porting
  content_hash: 00c548b19b2ba3e1289e3e74cb5c0988e34ada4953800bbc8f99acde9cdce3b0
- url: https://support.telnyx.com/en/articles/3275772-sweden-number-porting
  content_hash: 2081ad7083c6d94cbdca622fa6c4d39f0143a3d7d47c145d447ecec7262437a5
- url: https://support.telnyx.com/en/articles/4377462-norway-number-porting
  content_hash: 6f66439e325cecc97a475c8ec20a207def5a8702a71f96633f0b93562d3caeb1
- url: https://support.telnyx.com/en/articles/5188555-luxembourg-number-porting
  content_hash: ac2ddf880b45ae74934e26c06e2d35e10cee41fec96bd1bff11f54c147935b87
updated_at: 2026-06-11T11:16:01Z
---

# European Number Porting Requirements

*Part 3 of 3 — see also: [Part 1](european-number-porting-requirements--part-1.md), [Part 2](european-number-porting-requirements--part-2.md)*

A comprehensive reference for number porting requirements across European countries supported by Telnyx, covering required documentation, letter of authorization (LOA) templates, porting procedures, and country-specific rules.

## United Kingdom

**Local Numbers**

1. UK template LOA (must include underlying carrier's name and/or CUPID code, line type [single or multi], local address with valid postcode)
1. Latest Invoice with the current carrier

**National / Toll-Free Numbers**

1. UK template LOA (must include underlying carrier's name and/or CUPID code, local address with valid postcode, and Billing Account Number)
1. Latest Invoice with the current carrier

**Mobile Numbers**

1. LOA
1. Latest Invoice
1. PAC Number (Porting Authorization Code — an alphanumeric code required to transfer a mobile number to a new network)

If all documentation is correct and there are no rejections, a UK mobile request submitted before 12 noon local can be ported by the next business day.

**Before completing the LOA:**

- All pages must be signed, dated, and include page numbers.
- Save the LOA in non-editable PDF format.
- Fill in correct details in designated areas.
- The signature must be a valid e-signature or manual signature.

**Number detail considerations:**

- **Type of Numbers:** Geographic (linked to a specific area, requiring a local address) or Non-Geographic (not tied to a specific area, requiring a national address).
- **Line Type:** Single Line (terminates on a single socket, no associated numbers) or Multi-Line (terminates on equipment such as a PBX, may include associated numbers).

**Partial porting:** Whether partial porting is possible depends on the current provider. Most UK carriers do not allow number ranges to be split — the entire range (typically where the first number ends in 0 and the last in 9) must be ported together with any associated DIDs. A Main Billing Number (BTN) generally cannot be ported while leaving associated numbers active; they must be included in the port or ceased with the current provider. Check with the current provider before submitting.

**Underlying carrier vs. reseller:** The underlying carrier may differ from the company that sends the monthly bill (which may be a reseller). Resellers do not have a CUPID code. If the current provider is a reseller, contact them for the underlying carrier name and/or CUPID code.

**Range Holder:** The carrier who originally owns the number block as assigned by OFCOM.

**Pre-Order Validation (POV):** If you are unsure of the information on file with your existing carrier, Telnyx can initiate a POV to confirm DID details. This typically takes 5–7 business days with no formal SLAs; it cannot be escalated and depends on the current provider's cooperation.

**Time frames for Local / National / Toll-Free numbers (business days):**

| Line Type | LCP is Range Holder | LCP is not Range Holder |
|---|---|---|
| Single line | 5 | 7 |
| Multi-Line (including associated & other numbers) | 7 | 10 |
| Multi-Line (150 lines or less) | 10 | 13 |
| Multi-Line (151 lines or more) | 17 | 20 |
| Complex DDI | 22 | 25 |

If the losing carrier or range holder does not respond within these time frames, an escalation is made.

**Time and date of port:**

- A specific porting date can be requested, provided it falls within the time frame above.
- Standard activation for Local and National ports is **10:00 AM GMT**.
- Toll-Free ports take place between **00:00 and 04:00 AM GMT** on the FOC date, unless otherwise specified.
- Porting can take up to **6 hours** to complete once triggered.
- If the losing carrier does not release numbers on FOC, Telnyx follows up every 2 hours until completion.

**Port date changes after FOC:**

- A fee of **$40 per order** applies for any date change requested after submission.
- If the LCP is the Range Holder: minimum 24 hours' notice before FOC.
- If the LCP is not the Range Holder: minimum 72 hours' notice before FOC.

Download the UK template LOA [here](https://assets.ctfassets.net/taysl255dolk/4e1xrif0j3u8PU1qrl6GY5/bc86537edcb4e1f903da88ea986bd293/TELNYX_-_UK_CLOA_2023.pdf) (valid for all UK number types).

## Shared International LOA Template

Several European countries share a common international LOA template. This template is used for: Belgium, Denmark, Luxembourg, Netherlands, Norway, and Sweden. Download the international LOA [here](https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf).
