---
title: International Number Porting
summary: A guide to porting phone numbers to Telnyx across Australia, New Zealand,
  Turkey, and Singapore, covering portable number types, port categories, expected
  timeframes, document requirements, and the porting process for each country.
sources:
- url: https://support.telnyx.com/en/articles/3266212-australia-number-porting
- url: https://support.telnyx.com/en/articles/3267206-new-zealand-number-porting
- url: https://support.telnyx.com/en/articles/6138781-turkey-number-porting
- url: https://support.telnyx.com/en/articles/7235002-singapore-number-porting
updated_at: 2026-06-11T11:13:46Z
---

# International Number Porting

*Part 1 of 2 — see also: [Part 2](international-number-porting--part-2.md)*

A guide to porting phone numbers to Telnyx across Australia, New Zealand, Turkey, and Singapore, covering portable number types, port categories, expected timeframes, document requirements, and the porting process for each country.

## Portable Number Types by Country

Not all number types are portable in every country. The table below summarises availability.

| Number Type | Australia | New Zealand | Turkey | Singapore |
|---|---|---|---|---|
| Local | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes (Level 6) |
| National | ✅ Yes | ✅ Yes | ✅ Yes | ❌ Not available |
| Toll-Free | ✅ Yes (1800) | ✅ Yes | — | ❌ Not available |
| Mobile | ✅ Yes (+614) | ❌ Not available | — | ❌ Not available |

## Port Categories and Types

Port categories determine the complexity and processing path of a port request.

### Australia

- **CAT A (Simple Port)** — for single telephone numbers, "home phone" style numbers, or numbers with no complex services attached.
- **CAT C (Complex Port)** — **must** be selected for ISDN lines, hunt groups, PBX services, bundled service packages, or multiple numbers on a single service. Complex services associated with the number(s) will be cancelled during the porting process.
- **CAT Special** — required for toll-free (1800) and shared-cost numbers.
- **Mobile** — a separate category for +614 mobile numbers.

### Singapore

- **DEL (Direct Exchange Line) — Simple Port** — for single-line PSTN services, standard telephone services, or numbers without complex features.
- **DID/DDI (Direct Inward Dialling) — Complex Port** — for number ranges or blocks, numbers with complex services, PABX/private system numbers, or numbers allowing direct dialling without operator intervention. When porting a number block, you must port the **full range** or have your current carrier disassociate the specific numbers you wish to port.

New Zealand and Turkey do not define distinct port categories in their requirements.

## Expected Timeframes

Timeframes are measured from submission to FOC (Firm Order Commitment) and may vary based on the losing carrier and request complexity.

| Country | Port Type / Number Type | Expected Timeframe |
|---|---|---|
| Australia | CAT A (Simple) | 3–6 business days |
| Australia | CAT C (Complex) | 5+ weeks |
| Australia | CAT Special (Toll-Free) | 3–6 business days |
| Australia | Mobile | 1–5 business days |
| New Zealand | Local / National / Toll-Free | 5–10 business days (some sources indicate 10+ business days) |
| Turkey | Local / National | 1–7 business days |
| Singapore | DEL (Simple) | 6–7 business days |
| Singapore | DID/DDI (Complex) | 8–18 business days |

## Document Requirements

### Australia

**Local / National / Toll-Free Numbers:**

- **LOA** — Letter of Authorization with a local Australian address
- **ABN** — Australian Business Number (for business accounts)
- **Latest Invoice** — from current carrier, dated within the last 30 days

**Mobile Numbers** require additional verification:

- **LOA** — with a local Australian address
- **Latest Invoice** — from current service provider
- **Service Type** — specify Prepaid or Postpaid
- **Identity Documents** — 2 forms of Australian Government-issued ID (see list below)
- For prepaid services, also provide: end-user's full name, date of birth, and account number

**Accepted Identity Documents (2 required for mobile ports):**

- State or Territory Driver's Licence
- Australian Passport
- Australian Citizenship Certificate
- Proof-of-Age card
- Australian Birth Certificate
- Foreign military ID card
- Current foreign passport with valid entry stamp or visa
- Australian Government-issued Photo ID card
- Trade/work/business licence

**Mobile Verification Requirement:** Before submitting an Australian mobile port, each number must be verified. A unique code is sent to each phone number via SMS or call during the "Mobile Verification" step. Enter each code to verify ownership. All numbers must be verified before the port can proceed; otherwise, it remains in draft status.

### New Zealand

**For Personal Accounts:**

- Full name
- Contact phone number
- Local address within New Zealand

**For Business Accounts:**

- Full name of authorised person
- Contact phone number
- Company name
- Local address within New Zealand

**Common requirements:**

- **LOA** — signed by the authorised person
- **Latest Invoice** — from current carrier, dated within the last 30 days
- **Contact Details** — full contact information for the authorised person
- **Local Address** — address within New Zealand is required

### Turkey

**Local / National Numbers:**

- Most recent invoice with the carrier
- LOA with name and address of the business, plus local company registration number
- Copy of the ID of the authorised person
- Copy of official TAX ID issued by the Turkish government
- Copy of corporate signatories filed with the Turkish government
- A description of the activities of the business

### Singapore

**For Company Accounts:**

- **LOA** — country-specific LOA signed by the authorised person
- **Business Registration** — Business Registration Certificate or Certificate of Incorporation
- **Work Permit** — Work Permit or Employment Pass (for non-citizen applicants)
- **Latest Invoice** — from current carrier

**For Personal Accounts:**

- **LOA** — country-specific LOA signed by the end-user
- **NRIC/Passport** — National Registration Identity Card or Passport
- **Work Permit** — Work Permit or Employment Pass (for non-citizen applicants)
- **Latest Invoice** — from current carrier

## Letter of Authorization

Each country has its own LOA template. Always save the completed LOA in PDF format (non-editable), fill in all required fields completely, and ensure the information matches your current carrier's records exactly.

- [Download the Australia LOA](https://assets.ctfassets.net/taysl255dolk/72Cl4rcgvAl9N3Lt4iUalk/34cad211371dd434f52088f573a5f6b4/LoA_-_TELNYX_-_australia.pdf) — must include a local Australian address (required for emergency services)
- [Download the New Zealand LOA](https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/c9e0cb60d5051829eb44349be299df79/LoA_-_Telnyx_-_INTL.pdf) — uses the same format as the Australian LOA; must include a valid New Zealand address
- [Download the International LOA (Turkey)](https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf)
- [Download the Singapore LOA](https://images.telnyx.com/Telnyx-Singapore-LOA.pdf) — signature must be from the authorised person (company) or end-user (personal)

## Common Rejection Reasons

The following rejection reasons are documented for Australia but are broadly applicable across countries:

| Reason | How to Resolve |
|---|---|
| Company information mismatch | Verify exact company name and details with your current carrier before submitting |
| Complex services not declared | Check for hunt groups, ISDN, or bundled services — select the appropriate complex port category if any exist |
| Associated numbers | Ask current carrier to disassociate linked numbers, or port all associated numbers together |
| Disconnected number | Ensure all numbers are still in-service — do not cancel with your current carrier before the port completes |

## Changing Your FOC Date

Once a port request reaches FOC confirmed status, date changes may be possible but require advance notice:

- **Australia** — at least 48 business hours' notice before the scheduled FOC
- **Singapore** — at least 72 business hours (SGT) notice before the scheduled cutover

Contact [Telnyx porting support](porting-policy-procedure.md) to request a change.
