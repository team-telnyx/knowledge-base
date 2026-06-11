---
title: Telnyx 10DLC Process and Compliance Guide
summary: All US A2P messaging sent from local 10-digit long code (10DLC) numbers must
  be registered. This guide consolidates Telnyx’s end‑to‑end 10DLC process, deadlines,
  brand and campaign setup, opt-in/opt-out requirements, privacy policy language,
  shared and sole proprietor workflows, number assignment, review timelines, and troubleshooting
  tips.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
updated_at: 2026-05-20T14:06:51Z
---

# Telnyx 10DLC Process and Compliance Guide

*Part 2 of 2 — see also: [Part 1](telnyx-10dlc-process-and-compliance-guide--part-1.md)*

All US A2P messaging sent from local 10-digit long code (10DLC) numbers must be registered. This guide consolidates Telnyx’s end‑to‑end 10DLC process, deadlines, brand and campaign setup, opt-in/opt-out requirements, privacy policy language, shared and sole proprietor workflows, number assignment, review timelines, and troubleshooting tips.

## Bring existing TCR campaigns to Telnyx (Shared Campaigns)
What “Shared Campaigns” are
• Campaigns registered directly in TCR and then shared to a connectivity partner. When you select Telnyx as the connectivity partner, Telnyx acts as the upstream CNP for your campaign.

How to import
• Provide your CSP ID (from the TCR CSP Portal) to Telnyx via your account team or support@telnyx.com; association typically completes within two business days.
• In the TCR CSP Portal, select the campaign and choose Telnyx as the connectivity partner. Telnyx reviews and approves the share.

Assign Telnyx numbers to Shared Campaigns
• Use the Telnyx Bulk Phone Number Campaigns API to associate numbers. Ensure all numbers are on the same Messaging Profile, and have the TCR Campaign ID ready. You can check job and per‑number status via API.

Limitations
• Shared Campaign brand/campaign details cannot be edited in the Telnyx Portal; manage them in the TCR CSP Portal.
• While sharing is Pending, you cannot rescind or change the selected upstream CNP.

See also [10DLC Shared Campaigns](10dlc-shared-campaigns.md).

## Sole Proprietor registrations
Who should use this
• Single individuals without an EIN who need low‑volume A2P messaging (typically up to ~1,000 messages/day).

Steps
1) Create a Sole Proprietor Brand in the Portal (Messaging → 10DLC → Brands; entity type “Sole Proprietorship”). Provide legal name, permanent email (free domains allowed), mobile phone (for OTP), physical address (no PO Boxes/PMBs), and a website or social profile proving business legitimacy.
2) Brand verification via OTP PIN: email 10dlcquestions@telnyx.com to request the PIN after creating the brand. Telnyx sends the PIN to your mobile; reply with the PIN within 24 hours or it expires and you must restart.
3) Create a 10DLC Campaign using the Sole Proprietor use case. Provide clear Message Flow and at least two sample messages that include your Brand name and opt‑out instructions.
4) After carrier approval (typically 3–7 business days), assign your number(s) to the campaign and save.

Fees (carrier pass‑through, subject to change)
• Brand registration: $4 one‑time
• Campaign vetting: ~$15 per submission/resubmission
• Monthly maintenance: ~$2/month

See [Guide to Sole Proprietor 10DLC Brand and Campaign Registration](guide-to-sole-proprietor-10dlc-brand-and-campaign-registration.md).

## Publicly traded brands (Auth Plus)
• Publicly traded (Public_Profit) brands must complete TCR’s Auth Plus 2FA before any new campaigns can be created. 
• Process: email 10dlcquestions@telnyx.com with the brand ID and a business contact email that matches the brand’s web domain (individual mailbox). Telnyx triggers a 2FA email from noreply@auth.campaignregistry.com. The contact has 7 days to submit name, title, and the PIN to authenticate the brand.
• A small fee applies to Auth Plus attempts after August 1, 2025; check the Telnyx Portal for current pricing. See [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md).

## Common errors and troubleshooting
• Brand unverified: usually IRS/EIN or legal-name mismatch (US). Correct data; see [10DLC Unverified Brand](10dlc-unverified-brand.md).
• Campaign creation failures: TCR ID begins with “4b3”, “Failed TCR Review”, or “TCR Creation Failed/invalid date” indicate formatting/sequence issues (e.g., brand not yet verified, missing samples per use case, field length violations). Correct and recreate; contact 10dlcquestions@telnyx.com for specifics.
• Carrier declines: review decline email and error codes; adjust content/use case/message flow and resubmit. See [10DLC Carrier Error Codes and Explanations](10dlc-carrier-error-codes-and-explanations.md).
• Number assignment issues: confirm the campaign is Approved, the number isn’t already on another campaign, and you haven’t hit the 49‑number cap. See [10DLC Number Assignment Status](10dlc-number-assignment-status.md).

## Contacts and support
• Campaign review and correction threads: reply to the same email chain.
• Add recipients for status notifications: email 10dlcquestions@telnyx.com from your account’s main username email.
• General compliance or Portal issues: support@telnyx.com.

Additional references
• [Register for 10DLC Messaging](register-for-10dlc-messaging.md)
• [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md)
• [How to create a 10DLC campaign](how-to-create-a-10dlc-campaign.md)
• [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md)
• [10DLC Use Cases](10dlc-use-cases.md)
• [10DLC Fees and Charges](10dlc-fees-and-charges.md)
