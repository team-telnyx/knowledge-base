---
title: Messaging Compliance and Registration Reference
summary: A consolidated reference covering Telnyx messaging compliance topics including
  10DLC brand verification, toll-free verification changes, traffic type selection,
  P2P exemption, country-specific SMS guidelines, UK TPS regulations, and DID requirements
  for Bangladesh.
sources:
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
- url: https://support.telnyx.com/en/articles/12748292-bangladesh-did-requirements
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/articles/6545140-spain-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574037-belize-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596161-bangladesh-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679259-palestinian-territory-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680171-sri-lanka-sms-guidelines
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-08-05T13:25:18Z
---

# Messaging Compliance and Registration Reference

*Part 1 of 2 — see also: [Part 2](messaging-compliance-and-registration-reference--part-2.md)*

A consolidated reference covering Telnyx messaging compliance topics including 10DLC brand verification, toll-free verification changes, traffic type selection, P2P exemption, country-specific SMS guidelines, UK TPS regulations, and DID requirements for Bangladesh.

## 10DLC Brand Verification

A brand remains unverified when the legal company name, address, or EIN does not exactly match IRS records (for US brands). Even small differences such as writing "Street" instead of "St." can keep a brand permanently unverified. To correct this, provide the IRS Form CP-575 (EIN Confirmation Letter). On the IRS EIN letter, the first contact name is the legal company name and the second is the DBA; the address and EIN must match exactly.

For Canadian brands, provide the Canadian Business Number (BN) issued by the CRA, entering only the first 9 numeric digits (for example, `123456789` from `123456789RM0001`). The legal company name must match the corporation registration, and the address must match the one used with Corporations Canada. Useful verification resources include [Canada's Business Registries](https://beta.canadasbusinessregistries.ca/search) and the [Corporations Canada search](https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html).

For non-US or Canadian brands, enter the numeric portion of the VAT ID. Automated VAT matching is optimized for: Croatia, Hungary, Ireland, Italy, Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, Northern Ireland, United Arab Emirates, Australia, Belarus, Iceland, Malaysia, New Zealand, Saudi Arabia, Singapore, and Taiwan. For other countries, provide the primary corporation registration number or Tax ID and note the country of issuance.

For publicly traded brands, a 2FA email from Aegis is required, sent to an individual email address (not a group alias) on a domain matching the company website. Brands verified before this rule took effect (around Q4 2024) must complete the 2FA email before creating a new campaign.

See also [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md) and [Guide to Sole Proprietor 10DLC Brand and Campaign Registration](guide-to-sole-proprietor-10dlc-brand-and-campaign-registration.md).

## Toll-Free Verification Changes (Effective February 17, 2026)

As of February 17, 2026, the Business Registration Number (BRN) is mandatory for all new toll-free submissions. This aligns toll-free verification with 10DLC standards to close the "Toll-Free Loophole" and reduce phishing, increase deliverability, and standardize consumer trust practices.

### Mandatory Fields

- **Business Registration Number (BRN):** 9-digit EIN for US businesses; Business Number (BN) for Canadian businesses.
- **Business Registration Type:** EIN, CBN, CRN, NEQ, PROVINCIAL_NUMBER, VAT, ACN, ABN, BRN, SIREN, SIRET, NZBN, UST-IDNR, CIF, NIF, CNPJ, or UID.
- **Legal Entity or Organization Type:** Private Company, Publicly Traded Company, Charity / Non-Profit Organization, Government, or Sole Proprietor.
- **Issuing Country:** Country where the business is legally registered.
- **Privacy Policy Links:** Must state that SMS opt-in data will not be sold or shared with third parties.
- **Terms and Conditions Link:** Services agreement between customer and provider.
- **Opt-In Keyword:** START, YES, BEGIN, or a custom keyword to restart SMS after STOP.

### Enforcement Timeline

| Milestone | Status | Impact |
| --- | --- | --- |
| Pre-2026 | Optional | BRN fields were recommended but not required. |
| Feb 17, 2026 | Mandatory | New submissions without a BRN are immediately rejected. |
| Ongoing | Verification Required | Unverified or "Pending" numbers remain blocked in the US/Canada. |

### Stricter Opt-In Requirements

Carriers now require verifiable evidence of consent (direct links to signup forms or screenshots of "Text-to-Join" CTAs), one-to-one consent specific to the sender's business (no purchased lead lists), and explicit privacy policy language prohibiting third-party sharing of SMS opt-in data.

### Submission Checklist

- Exact legal name matching EIN/IRS records.
- DBA (brand name, may differ from legal name).
- Live website with footer link to a Privacy Policy.
- BRN and Business Registration Type.
- Legal Entity or Organization Type.
- Issuing Country.
- Business contact email matching the website domain and visible on the site.
- Clear use case description (e.g., "Two-factor authentication" or "Appointment reminders").
- Use-case summary matching the opt-in disclosure.
- Opt-in workflow description.
- Sample messages including brand name and opt-out language (e.g., "Hi from Acme Corp! Your order is ready. Reply STOP to opt out.").
- Opt-in workflow image URL (digital, verbal, paper, or inbound).
- Privacy Policy and Terms and Conditions links.
- Opt-In Keyword.

### Company Verification

If a submission for a Private Company, Publicly Traded Company, Charity / Non-Profit Organization, or Government entity is rejected for a missing or invalid BRN, a screenshot of the Business Registration form must be attached before resubmission.

### Sole Proprietor Path

Sole proprietors should leave the BRN, Business Registration Type, and Issuing Country fields blank and select Sole Proprietor as the Legal Entity type. Carriers now strongly prefer (and often mandate) an EIN over an SSN. Submissions without an EIN may be subject to manual verification, which can require uploading a government-issued ID and a live selfie. If a sole proprietor submission is rejected for a missing or invalid BRN, contact [tfverification@telnyx.com](mailto:tfverification@telnyx.com) with business registration forms to file an appeal for manual verification.

See also [Toll-Free Messaging](toll-free-messaging.md), [Toll Free Verification Request Guide](toll-free-verification-request-guide.md), and [Toll-Free Carrier Rejections](toll-free-carrier-rejections.md).

## Traffic Type Feature (A2P vs P2P)

The Telnyx Traffic Type feature lets users route eligible numbers as Application-to-Person (A2P) or Person-to-Person (P2P) traffic. Selecting the traffic type that matches the messaging use case improves deliverability.

- **A2P:** Used for domestic messaging and one-way communication with large campaigns. Does not support international messaging.
- **P2P:** Ideal for two-way communication and supports international messaging.

Only numbers assigned to the Telnyx SPID can currently switch between A2P and P2P. For more guidance, see the [A2P vs P2P resource](https://telnyx.com/resources/sms-numbers-traffic-types) and [CTIA's Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

## P2P Definition and Exemption Process

P2P (Person-to-Person) SMS traffic is the exchange of text messages between individuals, typically using mobile devices. Characteristics include individual use, two-way communication, regular mobile phone numbers, non-commercial content, standard SMS rates, and lighter regulatory treatment compared to A2P. If a P2P exemption is approved, registration with The Campaign Registry is not required.

### P2P Exemption Questionnaire

To qualify for exemption from 10DLC requirements, all of the following must be true:

1. Messaging excludes business communication of any kind.
2. The sender is not a Cloud Communication Suite.
3. Traffic is roughly symmetrical (User to User, 1:1 to 1:3).
4. There are no automated text messages in the workflow.
5. The applicant has a Telnyx contract.

If all criteria are met, contact the Customer Success Manager to apply. Without an existing agreement, contact [sales@telnyx.com](mailto:sales@telnyx.com); commercial agreements start at $1,000 per month in spend for at least 12 months. Approval can take several months, and applicants should review the latest TCR P2P requirements before applying.
