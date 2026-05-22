---
title: Toll-Free Verification Request Guide
summary: 'A complete, up-to-date guide to verifying Toll-Free numbers with Telnyx:
  what you must submit, how to document opt-in, choosing use cases, recent 2026 compliance
  changes, common rejection reasons with fixes, and regional legal considerations—so
  you can get approved and keep traffic compliant and deliverable.'
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
updated_at: 2026-05-20T14:20:59Z
---

# Toll-Free Verification Request Guide

*Part 2 of 2 — see also: [Part 1](toll-free-verification-request-guide--part-1.md)*

A complete, up-to-date guide to verifying Toll-Free numbers with Telnyx: what you must submit, how to document opt-in, choosing use cases, recent 2026 compliance changes, common rejection reasons with fixes, and regional legal considerations—so you can get approved and keep traffic compliant and deliverable.

## Opt‑Out and Help Keywords for Toll‑Free
- Network‑recognized keywords for Toll‑Free:
  - Opt‑out: “stop”
  - Opt‑in (after a STOP): “start” or “unstop”
- Auto‑responses for Toll‑Free are handled outside Telnyx and cannot be customized. If you use custom keyword rules on a messaging profile, place Toll‑Free numbers on a separate profile to avoid conflicts.
- Note: The verification form may ask you to list an opt‑in keyword (e.g., START/YES/BEGIN) for disclosure; however, actual network behavior for Toll‑Free accepts “stop” and “start/unstop.” See [Toll Free Opt-Out Words](toll-free-opt-out-words.md) and [SMS Opt-Out Keywords and Stop Words](sms-opt-out-keywords-and-stop-words.md).

## Common Rejections and How to Fix Them
Frequent carrier decline reasons and remedies include:
- Business details mismatch or unverifiable: Ensure your site shows the same legal/DBA name, address, email, and contact as in your submission; fix and resubmit.
- Business email not on official domain: Use your business domain and list it on your site.
- BRN missing/invalid: Often a name mismatch with EIN records or brand‑new companies not yet visible in IRS updates. Email tfverification@telnyx.com with your registration document; do not resubmit until advised.
- Entity misclassification: If you selected Sole Proprietor but you have a BRN, update classification and resubmit.
- Website inaccessible/password‑protected/new: Make the site public, complete required pages, and ensure uptime; then resubmit.
- Opt‑in missing/illegible/unbranded or link 404: Provide a clear, branded, legible screenshot or working URL.
- Consent bundled or mandatory: SMS must be optional and separate from other agreements; add an unchecked checkbox for SMS.
- Marketing without express written consent: Create a separate marketing SMS opt‑in (don’t mix “promotional/marketing and informational” in one disclosure).
- Use‑case mismatch with opt‑in: Align use‑case selection, description, and disclosure.
- Prohibited content (e.g., cannabis, third‑party leads, gambling) or SHAFT without age gate: Remove/rectify content, or (for limited internal alerts like 2FA/HR) consult support on a case‑by‑case basis.
- High‑risk domain (new/flagged) or known spam: Contact tfverification@telnyx.com to appeal; success is rare for known‑spam flags.
More detail and remediation steps are in [Toll-Free Carrier Rejections](toll-free-carrier-rejections.md).

## Error Codes and Resubmission Eligibility Highlights
- Not eligible to resubmit: Known spam/phishing/fraud campaigns; SHAFT content; disallowed content (loans, 3rd‑party leads, gambling, sweepstakes, stock/crypto, debt reduction/credit repair, federally illegal substances); numbers not provisioned to your organization.
- Eligible after fixes: Add robust age gate; switch public shorteners to branded domains; change HTTP to HTTPS; correct business details and URLs; provide express consent, proper opt‑in proof, or justification for >5 numbers; assign unique numbers per business.
- Submission editing timed out: You have 7 days from carrier submission for Telnyx to resubmit without changes (portal users can make a small edit and Save to generate a new request; API users may need to recreate).

## Sole Proprietors in 2026
Carriers now strongly prefer an EIN, even for sole proprietors without employees. Submissions without an EIN may be routed to manual verification (government ID and potentially a live selfie), increasing timelines. When submitting as Sole Proprietor: leave BRN/type/country blank and select Sole Proprietor. If rejected for BRN issues, email tfverification@telnyx.com with your documents to request a manual carrier review.

## Regional and Legal Considerations
- Canada: Double opt‑in is required for Toll‑Free programs in addition to general CASL compliance.
- Texas Mini‑TCPA (SB 140): Marketing texts to Texas residents (or by Texas‑based companies) are subject to quiet hours and potential telemarketer registration with the Secretary of State (fees and bond apply). Non‑compliance risks enforcement and private lawsuits. See [Legal Update: Texas’s Mini-TCPA Now Applies to Texts](legal-update-texass-mini-tcpa-now-applies-to-texts.md).
- UK TPS/CTPS: Screen marketing call lists against the TPS/CTPS registers and honor do‑not‑call rules. See [UK TPS Register: Guidelines](uk-tps-register-guidelines.md).
- Industry standards: Follow CTIA principles and applicable laws. See also [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## Best Practices That Improve Approval and Deliverability
- Call‑to‑action clarity: Clearly identify your brand, the number messages come from, program purpose, opt‑out (“Reply STOP to opt out”), HELP, fees, and links to Terms/Privacy.
- Frequency: Do not send more than 10 messages to a recipient in 24 hours unless it’s two‑way conversation or the user explicitly opted into higher frequency.
- Spoofing/fraud: Never misrepresent identity or phish for information.
- Message samples: Include brand and opt‑out language in every sample you submit.
- Links: Use HTTPS and avoid public URL shorteners; use a branded domain.

## Timelines, Approvals, and Traffic Blocking
- Review time: Commonly ~5 business days; can be faster or slower based on carrier volume.
- Enforcement: Unverified or pending numbers are blocked from sending in US/CA.
- Tracking: Monitor status in the portal or via webhook notifications and respond quickly to Waiting for Customer requests to avoid delays.

## Submission Checklist (Save This)
- Legal name exactly matches government records; DBA/brand shown consistently.
- BRN (e.g., EIN/BN) and Registration Type provided (except Sole Proprietor flow), with issuing country.
- Live, established website with matching contact details; business email on same domain.
- Use case(s) selected; description aligns with opt‑in; message samples include brand and “Reply STOP to opt out.”
- Opt‑in workflow description and a public link/screenshot of the actual CTA (Digital, Paper, Verbal, or Inbound) showing required disclosures.
- Separate, unchecked SMS consent checkbox(es); distinct marketing SMS consent if applicable.
- Privacy Policy link stating mobile info won’t be shared/sold for third‑party marketing; Terms link present.
- Age gate (DOB‑based) for age‑restricted content; political/charity disclosures and separate checkboxes where required.
- HTTPS links; no public URL shorteners; no prohibited content.
- Justification included if requesting more than five Toll‑Free numbers.

## Related Reading
- [Toll-Free Messaging](toll-free-messaging.md)
- [Toll Free Opt in Workflow Description](toll-free-opt-in-workflow-description.md)
- [How to Pick a Toll Free Use Case](how-to-pick-a-toll-free-use-case.md)
- [Toll Free Opt-Out Words](toll-free-opt-out-words.md)
- [SMS Opt-Out Keywords and Stop Words](sms-opt-out-keywords-and-stop-words.md)
- [Toll-Free Carrier Rejections](toll-free-carrier-rejections.md)
- [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md)
- [Legal Update: Texas’s Mini-TCPA Now Applies to Texts](legal-update-texass-mini-tcpa-now-applies-to-texts.md)
- [UK TPS Register: Guidelines](uk-tps-register-guidelines.md)
