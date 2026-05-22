---
title: Toll-Free Verification Request Guide
summary: 'A complete, up-to-date guide to verifying Toll-Free numbers with Telnyx:
  what you must submit, how to document opt-in, choosing use cases, recent 2026 compliance
  changes, common rejection reasons with fixes, and regional legal considerations—so
  you can get approved and keep traffic compliant and deliverable.'
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
  content_hash: 44584fe2bd9466b05a3041955608bbff2bd4e5f40a93c535182671727e290194
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
  content_hash: 0135186e7b4fd205be673cc95b9ad6c8e30e89e905c085cd4157bf7efe3aabc3
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
  content_hash: 206304a57044394aac7a609baf4be472c03ceee1447f9d2acf7f69b396d0235a
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
  content_hash: 5ee6a03aefda713deafa0ae83b16bf07fd2dec44809ec471d7c40c5ac40f1e26
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
  content_hash: 90b0c70ada6407870bc07052bff78540976edce04455165db02bf20eca7d547f
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
  content_hash: ebc1ea1b7e1300291f098ad0cf9165887a070c6f407aae70dc981af6a7adfd9d
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
  content_hash: 55dac840ba20800e1bef10796e05cd09ec25f8054649ed7af83da5a5c785ce79
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
  content_hash: f7af4f1a86f999ec2bd84d27e110c87e6ebecc7307ba3a19bf7df4924f090d0b
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
  content_hash: 893eb870d30dcd50296b49b25c760fe5992d116c669d492c517d395ff23ef4df
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
  content_hash: 3d84d9f16afa2941c930560e572b4e15b7686bdedbb8e91829115ac823a05308
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
  content_hash: 5ed9f37f1580e1c39cebfc35e7878b652e87711ffe3ba4bc8e87266875cc6256
updated_at: 2026-05-20T14:20:59Z
---

# Toll-Free Verification Request Guide

*Part 1 of 2 — see also: [Part 2](toll-free-verification-request-guide--part-2.md)*

A complete, up-to-date guide to verifying Toll-Free numbers with Telnyx: what you must submit, how to document opt-in, choosing use cases, recent 2026 compliance changes, common rejection reasons with fixes, and regional legal considerations—so you can get approved and keep traffic compliant and deliverable.

## Why Toll‑Free Verification Matters
Toll‑Free numbers must be verified before sending outbound SMS/MMS in the US and Canada. Unverified numbers are blocked industry‑wide, and verified traffic sees better deliverability and fewer false spam blocks. MMS on Toll‑Free is supported in the US/CA only. Typical review time is about 5 business days, but can vary by carrier volume.

## How to Submit and Track Your Request
- Portal: portal.telnyx.com → Real Time Communications → Messaging → Compliance → Toll‑Free Verification → Submit Verification Request
- API: Use the Toll‑Free Verification endpoints (see developers.telnyx.com → Messaging → Toll‑Free)
- Status lifecycle: Waiting for Telnyx → Waiting for Customer → Waiting for Vendor → Verified or Rejected. If Telnyx requests changes, your request moves to Waiting for Customer with guidance in the decline reason.
- Overwrites: Submitting a new request for an already‑verified Toll‑Free number will overwrite the prior approval and place the number back into unverified state until the new request is approved.
- Webhooks: You can receive status updates (Verified, Rejected, Waiting for Customer, Waiting for Vendor) to a webhook URL you provide.

## Mandatory Business Identity (2026 Update)
Effective Feb 17, 2026, a Business Registration Number (BRN) is required on new submissions to align Toll‑Free with 10DLC standards.
- Business Registration Number: US = EIN (9 digits). Canada = BN. If outside US/CA, use your applicable government ID.
- Registration Type: One of EIN, CBN, CRN, NEQ, PROVINCIAL_NUMBER, VAT, ACN, ABN, BRN, SIREN, SIRET, NZBN, UST-IDNR, CIF, NIF, CNPJ, UID.
- Legal Entity/Organization Type: Private Company, Publicly Traded, Charity/Non‑Profit, Government, or Sole Proprietor.
- Issuing Country: Where your business is legally registered.
- Exact Legal Name and DBA: Legal name must match government records; the customer‑facing brand (DBA) can differ but must be consistent across your site, opt‑in, and submission.
- Business Website: Must be live and established (Home, About, Products/Services, Contact details, Privacy Policy, Terms). Social pages used as your primary site must show business contact details and branding.
- Business Email: Should use the same domain as your website and appear on the website. Freemail domains can trigger declines.
- Contact Person: Provide a real first/last name (not a department).
- ISV/Reseller: If your Telnyx account domain differs from the end business domain, fill the Reseller/ISV field; otherwise leave blank.
- Privacy and Terms Links: Your Privacy Policy must state that mobile information (SMS opt‑in data) will not be sold or shared with third parties for promotional or marketing purposes.
- Opt‑In Keyword (form field): Carriers may request a restart keyword (e.g., START/YES/BEGIN) for disclosure consistency. Network behavior for Toll‑Free opt‑in/out differs; see “Opt‑Out and Help Keywords for Toll‑Free.”

## Choosing and Describing Your Use Case
Pick the option that best describes your traffic. Common choices include:
- 2FA, App Notifications, Booking Confirmations, Conversational/Alerts, Courier/Delivery Notifications, Fundraising, General Marketing, Mixed (two or more), Order Notifications, Political, System Alerts. See the full list and guidance in [How to Pick a Toll Free Use Case](how-to-pick-a-toll-free-use-case.md).
Requirements:
- Consistency: The selected use case(s), your description, message samples, and your opt‑in disclosure must all match.
- Samples: Provide message examples for every use case selected. Include your brand name and compliant opt‑out language (e.g., “Reply STOP to opt out”).
- One program per number: Avoid multiple Toll‑Free numbers sending the same content across a single program; this is considered an industry bad practice and can trigger spam blocks.

## Documenting a Compliant Opt‑In Workflow
Choose one of four methods and provide a link (publicly accessible) to the live page or a hosted screenshot/scan:
1) Digital: Link to the live signup page; if behind login, host clear screenshots.
2) Paper: Upload/host the signed or onboarding form section with the SMS consent language.
3) Verbal: Provide the exact script and where/how subscribers encounter it (e.g., phone number advertised on site/social, in‑store address).
4) Inbound Message: Show where the number is published for users to text you first.

Disclosures required (before first message, except inbound text where they may appear in the first message):
- “You are subscribing to [Brand] for [use case: transactional or marketing]. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Conditions [link]. View our Privacy Policy [link].”
Key rules:
- Branding: Include the business/brand name in the disclosure and on the form/screenshot.
- Separate consent: SMS consent must be distinct from other consents (e.g., email). The SMS checkbox must be optional and unchecked by default. If marketing is included, provide a separate marketing SMS checkbox from transactional SMS.
- Privacy statement: Your Privacy Policy must explicitly state you do not sell/share mobile information for third‑party marketing.
- Canadian programs: Require double opt‑in (confirmation message and affirmative reply).
- If you lack a public URL: Share a public link to a hosted document that diagrams the opt‑in flow and includes the exact disclosure text.
- Templates for each method are provided in [Toll Free Opt in Workflow Description](toll-free-opt-in-workflow-description.md).

## Programs Requiring Extra Care (Age‑Gated, Political, Charity)
- Age‑restricted products (e.g., alcohol): Use a robust date‑of‑birth gate (not Yes/No). If your business sells alcohol but will not promote it via SMS, state that clearly in your submission; otherwise, add an age gate before exposure to alcohol content.
- Political: If donations are solicited, disclose that in your use‑case summary. Mixed campaigns need a separate political consent checkbox.
- Charity/Fundraising: Select Fundraising (or Mixed, if multiple use cases). The opt‑in must include a separate fundraising/charity consent and disclose that donations will be solicited; reflect this in your use‑case summary.

## Prohibited and High‑Risk Content
Traffic may be blocked regardless of opt‑in if it involves prohibited categories. Examples include:
- SHAFT: Sex, Hate, Alcohol (without age gate), Firearms, Tobacco/Vape; Marijuana/CBD.
- Loans and high‑risk financial content (payday, short‑term, subprime, consolidation/debt relief, credit repair), third‑party debt collection.
- Gambling/sweepstakes, free prizes/gift cards, get‑rich‑quick, investment/stock/crypto.
- Third‑party lead generation or MLM, deceptive marketing, phishing/fraud.
- Insurance (marketing), unsolicited real‑estate lead gen.
- Illicit substances (including cannabis where illegal).
- Technical risks: public URL shorteners and non‑HTTPS links (fix by using a branded domain and HTTPS).
See also [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) for platform‑wide restrictions.

## Using Multiple Numbers and Mixed Use
- >5 numbers: If you submit more than five Toll‑Free numbers in one request (or across requests for the same business), include a specific justification (e.g., one dedicated number per store location with addresses, or per team handling client‑initiated conversations). Be detailed.
- One business per number: Do not use a single Toll‑Free number for multiple unrelated businesses.
