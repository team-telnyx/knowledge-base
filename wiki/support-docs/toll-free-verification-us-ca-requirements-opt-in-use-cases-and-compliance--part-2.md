---
title: 'Toll-Free Verification (US/CA): Requirements, Opt-In, Use Cases, and Compliance'
summary: 'End-to-end guide to getting US/CA toll-free numbers verified for messaging
  with Telnyx: how to submit, mandatory 2026 business identity requirements, opt-in
  and privacy/T&Cs standards (now mirroring 10DLC/short code), use case selection,
  Canada-specific rules, prohibited content, statuses, timelines, and how to resolve
  common rejection reasons.'
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
updated_at: 2026-05-14T11:23:21Z
---

# Toll-Free Verification (US/CA): Requirements, Opt-In, Use Cases, and Compliance

*Part 2 of 2 — see also: [Part 1](toll-free-verification-us-ca-requirements-opt-in-use-cases-and-compliance--part-1.md)*

End-to-end guide to getting US/CA toll-free numbers verified for messaging with Telnyx: how to submit, mandatory 2026 business identity requirements, opt-in and privacy/T&Cs standards (now mirroring 10DLC/short code), use case selection, Canada-specific rules, prohibited content, statuses, timelines, and how to resolve common rejection reasons.

## Age Gating, Political, and Fundraising Nuances
- Age-gated content (e.g., alcohol): Require a DOB-based gate that blocks underage users; “Yes/No” is insufficient. If your brand sells alcohol but will not promote it via SMS, state that explicitly.
- Political messaging: Indicate if donations will be solicited; include a separate political consent checkbox for mixed programs; ensure privacy policy includes “No mobile information will be sold or shared with third parties for promotional or marketing purposes.”
- Fundraising/Charity: Select Fundraising (or Mixed) and disclose that donations will be solicited; include a dedicated fundraising/charity checkbox and mention donations in the consent text.

## Canada-Specific Requirements
- Canadian toll-free programs require double opt-in: after initial consent, send a confirmation message and obtain an affirmative reply (e.g., “YES”) before messaging.

## Prohibited Content and High-Risk Patterns
Carriers disallow or heavily restrict certain topics and practices across toll-free, 10DLC, and short code.
- Illegal products/substances, unapproved supplements.
- Gambling/betting (only potential exceptions via pre-approved short code programs).
- SHAFT: Sex/adult content, Hate, Alcohol (varies; US may allow with strict controls), Firearms, Tobacco/Vape (generally not permitted), Marijuana/CBD.
- Deceptive/high-risk: phishing/impersonation, misleading financial offers, risky investments, third‑party lead gen lacking one-to-one consent, collections.
- Risk signals: public URL shorteners, non-HTTPS links, unverifiable businesses.

Use branded, secure (HTTPS) URLs and keep content aligned with registered use cases. See: [Forbidden Messaging Use Cases in the US and Canada (10DLC, Toll-Free, and Short Code)](forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code.md).

## Common Rejection Reasons and How to Fix Them
Not eligible to resubmit (must change channel/use case):
- Content violations: SHAFT; federally illegal substances; known spam/phishing; high-risk fraud/deceptive marketing.
- Opt-in based on organizational/government exemption.
- Number not provisioned to your organization.

Eligible if corrected:
- Age gate missing/inadequate: Implement robust DOB gate.
- Public URL shortener: Replace with a branded domain.
- Non-secured URLs: Use HTTPS.
- Invalid business info/URL inaccessible/ISV contact used instead of end user: Correct details, ensure site is live.
- Opt-in issues: Provide explicit, documented consent; ensure consent isn’t a condition of service unless clearly documented; add required disclosures; remove language about sharing SMS data with third parties.
- Single number used for multiple businesses: Assign a unique toll-free per business.
- Missing justification for >5 numbers: Add detailed rationale.
- Additional info requested (opt-in/business info): Update and resubmit.
- Submission editing timed out: Within 7 days of carrier submission, Telnyx can resubmit without changes (easiest in portal; API users may need to create a new request ID).

## Short Codes: How Toll-Free Rules Compare and What to Know
Toll-free verification standards now closely mirror short code requirements. If you’re evaluating short codes:
- Ordering (new random/vanity) requires three parallel tracks:
  - Short Code Order Brief (for carriers).
  - Brand Registration Form (Short Code Registry, annual revet/vetting).
  - Content Provider Registration Form (may be same entity as brand).
- Migrating an existing short code requires the above plus a migration letter, LOA, and registry transfer from current provider. Provisioning typically completes ~6 weeks after approvals.
- The Short Code Registry mandates brand/content provider registration for new orders and renewals; brands must complete email verification and periodic re‑vetting. Entity details should match IRS EIN documentation (CP‑575) for US entities.
- Compliance quick reference (applies broadly to subscription programs and informs toll-free expectations):
  - Call to Action (CTA): clear product description, M&DR may apply, frequency, STOP/HELP, privacy policy and T&Cs links.
  - Welcome messages: brand/program name, frequency, M&DR may apply, HELP contact.
  - Ongoing broadcasts: include brand/program and opt‑out info.
  - Privacy policies must clearly state messaging data is not shared/sold for marketing (no share–no disclose–no transfer).
  - Carrier notes: T-Mobile scrutinizes political, cart reminders, donations; enforce consistency of program description and frequency. Verizon requires alternative OTP path (e.g., email) and disallows collections and certain financial marketing.

Deep dives: [US Short Code Ordering Process](us-short-code-ordering-process.md), [Short Code Brand and Content Provider Registration Process](short-code-brand-and-content-provider-registration-process.md), [Short Code Compliance Quick Reference Guide](short-code-compliance-quick-reference-guide.md).

## Voice vs. Messaging on Toll-Free (quick note)
- You can call toll-free numbers with Telnyx, and you can purchase US/CA toll-free for inbound voice. Messaging verification covered here is separate from voice calling capability. For porting numbers, see [US / CA Toll Free Number Porting](us-ca-toll-free-number-porting.md).

## Best Practices Checklist for a Fast Approval
- Legal identity
  - Exact legal name matches government records; include DBA if used publicly.
  - Provide EIN/BN and correct registration type; use business-domain email visible on your site.
- Website readiness
  - Live site (not “under construction”) with clear brand, contact details, Privacy Policy, and T&Cs.
  - HTTPS everywhere; use branded links (avoid public shorteners).
- Use case clarity
  - Select the right use case(s); if Mixed, describe each and keep consistent with opt-in and samples.
  - Provide brand-labeled sample messages with STOP/HELP.
- Consent and documentation
  - Verifiable opt-in evidence (URLs/screenshots/scripts) using one of the four allowed methods.
  - Separate unchecked SMS checkboxes; dedicated marketing checkbox if applicable.
  - Privacy policy explicitly: no selling/sharing SMS data with third parties for marketing.
  - Canada: implement and document double opt-in.
- Operational details
  - Justify >5 numbers specifically.
  - For ISVs/resellers, identify the reseller when domains differ.
  - Include the program’s Opt‑In keyword for re-subscription after STOP.

If you receive a rejection, review the reason, correct the issue using the guidance above, and resubmit via the Portal or API. For sole proprietor identity issues, contact tfverification@telnyx.com for manual verification assistance.
