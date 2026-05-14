---
title: '10DLC carrier errors, brand verification issues, and campaign suspension:
  causes and fixes'
summary: A practical guide to understanding common 10DLC carrier error codes, fixing
  inconsistent registrations (602/603), correcting CTA and opt‑in compliance failures
  (806 and related), resolving unverified brand problems, and handling TCR campaign
  suspensions due to inactivity.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
updated_at: 2026-05-14T11:22:21Z
---

# 10DLC carrier errors, brand verification issues, and campaign suspension: causes and fixes

*Part 1 of 2 — see also: [Part 2](10dlc-carrier-errors-brand-verification-issues-and-campaign-suspension-causes-and-fixes--part-2.md)*

A practical guide to understanding common 10DLC carrier error codes, fixing inconsistent registrations (602/603), correcting CTA and opt‑in compliance failures (806 and related), resolving unverified brand problems, and handling TCR campaign suspensions due to inactivity.

## How carriers review 10DLC campaigns for consistency
Carriers expect complete consistency and accuracy across all parts of a campaign. Mismatches are a leading cause of declines.

Verify alignment across:
- Use cases selected at creation time (e.g., 2FA vs. Marketing vs. Account Notifications)
- Campaign description
- Message flow and opt-in method/form
- Brand website (on the brand and in the message flow/CTA)
- Sample messages (each selected use case must have at least one representative sample; Marketing or Mixed requires two or more)

If any of these conflict (e.g., you choose 2FA but samples mention marketing), expect a 602/603 decline.

## Common carrier decline/error codes and how to resolve
Below are frequent error categories with concrete fixes. Address root causes before resubmitting a campaign.

- Content prohibitions and age-gated categories
  - 701 Cannabis: Any cannabis/CBD/hemp content (including shipping) is rejected.
  - 702 Guns/Ammo: Sales require age verification. Educational/non-sales content may be acceptable.
  - 703 Explicit sexual content: Illegal, non-consensual, or underage themes are prohibited (even if presented as family-friendly).
  - 704 Gambling: Casino, sports betting, lottery, and online gambling are prohibited. Bingo may be allowed with proper age gating.
  - 705 Hate/profanity: Prohibited.
  - 706 Alcohol (age-gated): Must comply with law and use a functioning DOB gate (DD/MM/YYYY or MM/DD/YYYY), not a simple “Are you 21?” button.
  - 707 Tobacco/Vape (age-gated): Same standard as alcohol.
  - 708 Lead gen/affiliate marketing: No sharing/selling of user data to third parties for leads. Mentions of lead gen/SEO on the site can cause decline.
  - 709 High-risk financial services: Payday loans, non-direct lenders, debt collection/repair/forgiveness, crypto, stock trading are prohibited as lead-gen/affiliate models.
  - Fixes: Remove prohibited content, implement compliant age-gating with DOB entry, and eliminate any lead-gen/affiliate data sharing.

- Registration consistency/inaccuracies
  - 601 Attributes don’t match website/samples (e.g., Embedded Link/Phone flagged “Yes” but not present in samples).
  - 602 Inconsistent samples/description/attributes/CTA with the selected use case.
  - 603 Website/brand content doesn’t match sample messages.
  - Fixes: Align use case, description, website, message flow, opt-in, and samples. Include a representative sample per use case; ensure samples reflect any declared embedded links/phone numbers.

- Opt-in, CTA, and privacy policy requirements
  - 611 Opt-in confirmation missing required elements: program (brand) name, message frequency, HELP, STOP, and message/data rate disclosure. Opt-in must reflect express consent (e.g., a checkbox next to CTA text).
  - 803 Opt-in language required on website when a phone number is collected.
  - 804 Unable to verify website/CTA (incomplete info or broken links).
  - 805 Non-compliant privacy policy (must state SMS opt-in data is not shared with third parties).
  - 806 CTA/message flow not compliant or specific path unclear; missing HELP/STOP, frequency, “message and data rates may apply,” and links to Terms & Conditions and Privacy Policy.
  - 851 Privacy policy and opt-in confirmation both missing key items (e.g., third-party sharing disclaimer, program name, opt-out, support contact details).
  - 852 Privacy policy missing explicit statement that mobile opt-in data isn’t shared with third parties.
  - 861 CTA information incomplete (program name, frequency, opt-in disclosures, and T&Cs link must be present).
  - Fixes: Ensure the online/verbal opt-in process and the Message Flow field describe a clear path and include all disclosures: program/brand name, product description, message frequency (e.g., “Message frequency may vary.”), standard message and data rate disclosure, “Reply STOP to opt out,” “Reply HELP for help,” and links to non-popup Terms & Conditions and a Privacy Policy stating SMS opt-in data isn’t shared with third parties.

- KYC and identity issues
  - 710 Reseller/non-compliant KYC: The sending brand must be the registered brand, not the agency.
  - 711 Repeated use of the same EIN across multiple brands without a valid explanation.
  - 712 Misleading registration: Direct lenders/regulatory entities must identify themselves correctly.
  - 713 Large companies using non-official email domains create fraud risk.
  - 801 Not a Sole Proprietor (doesn’t meet TCR/carrier SP criteria).
  - 802 Sole Proprietor not yet authorized (Syniverse authorization required).
  - 807 Inauthentic website (common in real estate/insurance when the site can’t verify the business).
  - Fixes: Register the true sender brand, use official domains, provide accurate business classification, and ensure the website can verify the business.

## Fixing 10DLC error 806 (CTA and message flow not compliant)
Error 806 points to the Message Flow field and your actual opt-in experience. The carrier could not confirm a compliant, specific opt-in path.

Do this:
- Document a clear, specific mobile opt-in path in the Message Flow (e.g., exact page path or flow for web forms; precise steps for verbal/POI/keyword).
- Ensure your opt-in form shows all required items: program/brand name, product description, message frequency, “Standard message and data rates may apply,” “Reply STOP to opt out,” “Reply HELP for help,” and links to non-popup Terms & Conditions and a Privacy Policy that states SMS opt-in data is not shared with third parties.
- Align your samples and attributes (e.g., include a link/phone in samples if attributes flag them as embedded).
- Helpful references: Guide to message flow formats (https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field) and opt-in form checklist (https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form).

## Resolving “Inaccurate Registration/Inconsistency” (602 and 603)
- Confirm the selected use case(s) match your description, opt-in flow, website/CTA, and every sample message.
- Provide at least one representative sample per selected use case; for Marketing or Mixed, provide two or more.
- Ensure brand details and the website shown in the brand and message flow belong to the same business described in the campaign.
- Cross-check attributes (e.g., Embedded Link/Phone) and mirror them in samples.

## Unverified brand: how to pass KYC verification
If your brand is “Unverified,” it’s almost always due to a mismatch with government records.

- US brands
  - Match the IRS CP‑575 (EIN Confirmation Letter) exactly for legal name, address (including abbreviations like “St.” vs “Street”), and EIN.
  - On the IRS letter: the first contact line is the legal company name; the second is the DBA.

- Canada
  - Enter only the first 9 numeric digits of your Business Number (e.g., from 123456789RM0001, enter 123456789).
  - Ensure legal name and address match Corporations Canada records. Helpful lookups: https://beta.canadasbusinessregistries.ca/search and https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html

- Non‑US/Canada
  - Enter the numeric portion of your VAT ID. Automated matching is optimized for: Croatia, Hungary, Ireland, Italy, Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, Northern Ireland, United Arab Emirates, Australia, Belarus, Iceland, Malaysia, New Zealand, Saudi Arabia, Singapore, Taiwan.
  - If your country isn’t listed, provide your primary corporation registration number or Tax ID and indicate the country of issuance.

- Publicly traded brands
  - Complete Aegis 2FA using an individual’s email at a domain that matches the website (no group aliases). Required for new campaigns and for previously verified brands before creating new campaigns (rule effective Q4 2024).
