---
title: 10DLC Errors, Opt-In Compliance, and Troubleshooting
summary: A practical guide to avoiding 10DLC campaign declines, documenting compliant
  opt-in flows, verifying brands, resolving number assignment problems, and reactivating
  suspended campaigns on Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
  content_hash: 9b6044d0b967707a06966ae9c750424519d3d24b6d0118951e910d3ae8f1afb7
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
  content_hash: 52724a201fd5374074a0eb90e9410468b85a7658feedbe8a9d47840d78861363
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
  content_hash: c58866e0f474718c88333b11758004e24d0a2a29cbe655c05b629857b4914695
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
  content_hash: f648f47c5ea3437cf3f55620791c2f4363f1563426f0ddb8249ba348f03ef69a
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
  content_hash: 37dc405587bd56e3e374454fbad57992200523b656a9c987ad3e34d2ee3999d9
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
  content_hash: df854549a7915277c5db4ee826ccd16ccb0ccdd7353f26fa06513efe8a2fc298
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
  content_hash: 7be63f684b68b93446849d31a371a99d5e89179c5f4b75c8fe2e97f6119da1e2
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
  content_hash: 5695a125b887d6ce58992c100db1af80399f925aa5b3dbf4f323ff550d0dc73a
updated_at: 2026-05-20T14:08:45Z
---

# 10DLC Errors, Opt-In Compliance, and Troubleshooting

*Part 1 of 2 — see also: [Part 2](10dlc-errors-opt-in-compliance-and-troubleshooting--part-2.md)*

A practical guide to avoiding 10DLC campaign declines, documenting compliant opt-in flows, verifying brands, resolving number assignment problems, and reactivating suspended campaigns on Telnyx.

## What carriers review and common decline reasons
Carriers look for consistency, compliant consent, authentic identity, and permitted content across everything you submit (brand, website, campaign description, message flow/CTA, and sample messages). Common decline codes and what they indicate:

- Consistency/accuracy
  - 601/602/603: Attributes, use case, website, CTA/message flow, and sample messages don’t match.
- Opt-in, CTA, and confirmations
  - 611: Opt-in confirmation missing program name, message frequency, HELP/STOP, and message/data-rate disclosures (and lacks express consent, e.g., a checkbox).
  - 803: Website that collects phone numbers lacks opt‑in language.
  - 804: Broken links or incomplete/inaccessible CTA info.
  - 805/851/852: Privacy policy non‑compliant; must clearly state SMS opt‑in data is not shared/sold to third parties; include required disclaimers and support contact in confirmations.
  - 806: CTA/message flow missing path or required elements (HELP/STOP, frequency, “message & data rates may apply,” and T&Cs/privacy links or language).
  - 861: CTA missing program name, frequency, opt‑in disclosures, and T&Cs link.
- KYC/identity
  - 710: The actual sending brand must be the registered brand (not an agency/reseller).
  - 711: Reusing the same EIN across brands requires a valid explanation.
  - 712: Regulated entities (e.g., direct lenders) must self‑identify accurately.
  - 713: Large companies should use an official email domain.
  - 801/802: Sole Proprietor eligibility/authorization issues.
  - 807: Inauthentic or incomplete website (common in real estate/insurance) prevents verification.
- Prohibited/restricted content
  - 701: Cannabis/CBD/hemp content (incl. shipping) is automatically rejected.
  - 702: Guns/ammo sales require age verification; educational content only if no sales.
  - 703: Explicit/illegal sexual content or any underage themes are prohibited.
  - 704: Gambling (casino, betting, lottery, online); bingo may be allowed with proper age gating.
  - 705: Hate speech/profanity/inappropriate content prohibited.
  - 706/707: Alcohol and tobacco/vape require functional DOB age gating (DD/MM/YYYY), not simple “Are you 21?” prompts.
  - 708: Lead gen/affiliate marketing and sharing/selling data for leads is prohibited.
  - 709: High‑risk financial services (payday loans, non‑direct lenders, collections, credit repair/debt forgiveness) and crypto/stock‑trading traffic are prohibited.

## Prohibited and restricted content highlights
- Cannabis or cannabinoid‑adjacent products (including teas/beauty products) and related shipping are auto‑declined (701).
- Firearms/ammunition require robust age verification; no sales messaging without it (702).
- Sexual content with illegal/non‑consensual/underage themes is disallowed, including disguised “family‑friendly” content with adult themes (703).
- Gambling of all forms requires compliance; bingo may pass with proper gating (704).
- Any hate/profanity/inappropriate content is prohibited (705).
- Alcohol and tobacco/vape require DOB age gating on opt‑in (706/707).
- Lead gen/affiliate marketing and data sharing for marketing is prohibited (708); high‑risk finance and crypto/stock‑trading content are not permitted (709).

## Opt-in, CTA, and confirmation requirements (what must appear)
Include these elements wherever you collect consent (web form, phone, paper, keyword, inbound text):
- Program/brand name and clear description of what users will receive.
- Message frequency disclosure (e.g., “Message frequency may vary.”).
- “Standard message and data rates may apply.” (where applicable).
- Opt‑out and support: “Reply STOP to opt out. Reply HELP for help.”
- Terms & Conditions and Privacy Policy: link to accessible pages (not pop‑ups) or include compliant privacy language stating mobile information won’t be sold/shared with third parties for promotional/marketing purposes.
- Express consent mechanism appropriate to the medium (e.g., a consent checkbox on web forms next to the call‑to‑action text).
- If marketing messages will be sent, the opt‑in must explicitly mention marketing.
- If political/charity messaging includes or may include fundraising, state “Donations may be solicited.”
- For alcohol/tobacco/vape, enforce DOB age gating at opt‑in.

## Message flow field: how to document it so it passes review
Document exactly how users discover and complete opt‑in, including URLs/paths/screenshots:
- Digital consent (web/contact page): Specify the opt‑in page URL or gated path and include the full disclosure language and privacy/T&Cs link.
- Verbal consent (phone/in‑person): Describe how users learn the number/address, the agent’s consent script, how numbers are recorded, and the confirmation SMS. For marketing/political, require an explicit follow‑up YES to enable promotional/political messaging; without YES, only informational messaging is allowed.
- Physical consent (paper): Note where/when form is completed, include the printed disclosure, link to a copy of the form, and describe the confirmation SMS.
- Keyword opt‑in: Show where the keyword/number/QR is advertised (URL/screenshot) and include the disclosure in the auto‑reply.
- Inbound message opt‑in: Show where the number is advertised and include the auto‑reply disclosure.
For detailed templates and example wording, see Telnyx’s guide: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field

## Fixing consistency and accuracy declines (602/603/601)
Audit the entire submission for alignment:
- Use cases selected during campaign creation.
- Website on the brand and in the message flow (for digital opt‑in).
- Campaign description.
- Message flow and any opt‑in forms/scripts.
- Sample messages: each selected use case must be represented; dedicated marketing or mixed use requires at least two representative samples. Do not include content outside selected use cases.

## Privacy policy and CTA pitfalls that trigger 805/851/852/861/611/806
- Privacy policy must clearly state mobile/SMS opt‑in data will not be sold/shared with third parties for marketing/promotional purposes (805/852).
- Opt‑in confirmations must include program name, opt‑out instructions, and a support contact (851), as well as frequency and data‑rate disclosures (611).
- CTA must include program name, frequency, opt‑in disclosures, and T&Cs link (861).
- The message flow must include the precise opt‑in path plus HELP/STOP, frequency, data‑rates, and privacy/T&Cs elements (806).

## Brand and identity verification (resolving “Unverified Brand” and related issues)
- United States: Match the IRS CP‑575 (EIN Confirmation Letter) exactly for legal name (first line), DBA (second line), address (e.g., “St.” vs “Street”), and EIN. Minor mismatches prevent verification.
- Canada: Enter only the first 9 digits of the CRA Business Number (e.g., from 123456789RM0001, enter 123456789). Ensure legal name/address match Corporations Canada records.
- Other countries: Provide the numeric VAT ID for supported countries (e.g., HR, HU, IE, IT, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, NI, AE, AU, BY, IS, MY, NZ, SA, SG, TW). If unsupported, provide the primary corporate registration or tax ID and the issuing country.
- Publicly traded brands: Complete Aegis 2FA using an email domain that matches your website and goes to an individual (not a group alias); required before creating new campaigns.
- Additional KYC checks: Avoid reseller submissions where the agency is registered instead of the actual sending brand (710); use official corporate email domains for large enterprises (713); explain repeated EIN usage across brands (711); select accurate regulated classifications (712); ensure the website is authentic and sufficient for business verification (807); confirm Sole Proprietor eligibility/authorization (801/802).
