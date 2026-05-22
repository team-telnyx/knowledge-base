---
title: Telnyx Overview, Account Levels, Billing, and Resources
summary: This page consolidates key information about Telnyx—what we offer, how our
  global network and interoperability work, account level frameworks and verification,
  billing and refund policies, reseller options, hardware compatibility, support for
  call centers, company locations, account cancellation/restore steps, and where to
  find more resources.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130675-what-kind-of-equipment-do-you-use
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
updated_at: 2026-05-20T14:40:10Z
---

# Telnyx Overview, Account Levels, Billing, and Resources

This page consolidates key information about Telnyx—what we offer, how our global network and interoperability work, account level frameworks and verification, billing and refund policies, reseller options, hardware compatibility, support for call centers, company locations, account cancellation/restore steps, and where to find more resources.

## What Telnyx Offers
Telnyx is a Communications Platform as a Service (CPaaS) delivering voice, SMS/MMS, numbers, WebRTC, and Elastic SIP Trunking over a privately owned global IP network. Beyond core CPaaS, Telnyx also provides:
- Inference (AI): speech-to-text, text-to-speech, sentiment analysis, and language detection for intelligent IVRs and voice bots.
- Storage: secure, API-accessible media storage for call recordings and message attachments with encryption and compliance features.
- Flow: a visual, drag-and-drop builder for multi-channel communication workflows, triggers, and integrations.

## Global Network and Tech Specs
- Points of Presence and telephony/network specs: see sip endpoint sites by region: [sip.telnyx.com](https://sip.telnyx.com/), [sip.telnyx.ca](https://sip.telnyx.ca/), [sip.telnyx.eu](https://sip.telnyx.eu/), [sip.telnyx.com.au](https://sip.telnyx.com.au/).
- Carrier partners include major North American and international operators (e.g., AT&T, Verizon, CenturyLink/Lumen, Level 3, Inteliquent, Tata, BT, Telefónica, IDT, Comcast, Peerless, Windstream, Bandwidth, etc.).
- Interoperability: configuration guides are available for popular platforms and devices such as 3CX, Asterisk/FreePBX/FreeSWITCH, Cisco CallManager/CUBE, Avaya, AudioCodes, Grandstream, Mitel, Yealink, Zoiper, and more: [Configuration Guides](https://support.telnyx.com/en/collections/133118-configuration-guides).

## Account Levels and Verification
Telnyx uses two frameworks. Your portal determines which applies to you.

- Legacy Level 1/Level 2 (you’ll see an Account Settings > “Verifications” tab):
  - Level 1 (default after email confirmation):
    - Buy a local number in your home country, assign connections/messaging profiles, set up messaging and US-only voice, create a multi-user org.
    - Outbound messages limited to 50/day.
  - Level 2 (upon approval):
    - Buy international numbers; enable international calling and call forwarding; increase messaging send rates (account-wide 600→3000; toll-free 6→1200); use alphanumeric sender ID internationally; submit hosted SMS and 10DLC orders; order SIMs internationally or with freemail; removes certain payment address restrictions and top-up limits.
  - Apply for Level 2 (org owners): [Account Settings > Verifications](https://portal.telnyx.com/#/account/my-account/verifications). Fill the Level 2 form; allow up to 48 hours. If declined, see appeal guidance: [Appeal Level 2 Verification Status](https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status).

- TPVE (Trial–Paid–Verified–Enterprise) framework (you’ll see an “Account Levels” page):
  - Access: [Account Levels](https://portal.telnyx.com/#/account/account-levels).
  - Levels: Trial (default), Paid (after adding a payment method), Verified (after business verification), Enterprise (via Sales at [telnyx.com/contact-us](https://telnyx.com/contact-us)).
  - Characteristics: org-wide level sharing; privileges and API access by level; clear upgrade paths.
  - Details: [Account Levels docs](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities), plus API access tables for V2 ([reference](https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/api.telnyx.com.html)) and S3 ([reference](https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/telnyxstorage.com.html)).
  - Note: New signups from June 2025 onward may see this revised framework.

## Billing, Contracts, and Refunds
- Billing model: strictly pre-paid; no post-paid service at this time.
- Pay-as-you-go: charges for services already used aren’t refundable.
- Refund policy: no refunds for Bitcoin (BTC) payments; no refunds for payments ≥180 days old. Other remaining balances may be refunded—email [billing@telnyx.com](mailto:billing@telnyx.com).
- Contracts: no contract required to use Telnyx; you can open a free account anytime.
- Cancellation fees: none.

## Reselling and Multi-Tenancy
- Mission Control is built for multi-tenant use—segregate traffic, tag for organization, and run real-time reporting.
- All functionality is API-first: build ordering and provisioning into your own platform via the public APIs at [developers.telnyx.com](https://developers.telnyx.com).

## Hardware and Interoperability
- Telnyx does not supply hardware; we’re compatible with nearly any SIP-enabled device or platform.
- You can enable call forwarding to external numbers for flexible routing.
- See device/PBX setup resources in the interoperability guides, including popular IP phones and softphones.

## Call Centers and Ideal Customers
- Telnyx actively supports call centers (an ideal customer profile). Get in touch to tailor routing, SIP trunking, compliance, and scaling.
- Context: there are at least 32,000 call centers in the U.S. (IBISWorld).

## Corporate Info and Locations
- Founded: 2009. Headquarters: Austin, Texas.
- Offices: Austin (HQ), Denver, Dublin, Amsterdam. Many team members work remotely worldwide.
- Address: 600 Congress Avenue, 14th Floor, Austin, TX 78701.

## Network Equipment and Infrastructure
- Core/edge routing: Cisco ASR.
- Aggregation switches: Juniper QFX5100.
- Cloud CE routing: Brocade Vyatta and virtualized routing platforms.
- Learn more: Telnyx network overview at [telnyx.com/our-network](https://telnyx.com/our-network).

## Account Management: Cancel, Remove Members, or Re-enable
- Remove a member from your organization: use the portal’s Organization and Members page: [https://portal.telnyx.com/#/advanced-features/members](https://portal.telnyx.com/#/advanced-features/members).
- Cancel your own account: email [support@telnyx.com](mailto:support@telnyx.com) from the account owner’s email and include your Security Passphrase.
  - Find your Security Passphrase (not your login password) in Account Security: [https://portal.telnyx.com/#/account/my-account/security](https://portal.telnyx.com/#/account/my-account/security).
  - Only requests from the account owner’s email can be approved.
- Re-enable a cancelled account: email [support@telnyx.com](mailto:support@telnyx.com) from the email to be reactivated (org owners can provide a sub-member’s email).

## Resources, Community, and Support
- Blog and resources hub: [telnyx.com/resources](https://telnyx.com/resources) (subscribe for updates).
- Community forum: accessible via the Telnyx Mission Control Portal.
- Contribute content: email [andrewm@telnyx.com](mailto:andrewm@telnyx.com).
- Support channels:
  - AI Assistant (24/7): [Portal AI Chat Support Assistant](https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant)
  - NOC best practices (24/7): [Best practices for contacting support](https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support)
  - Porting team (9am–7pm CT, Mon–Fri): [Contact Porting](https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting)
  - Numbering team (9am–5pm CT, Mon–Fri): [Numbering team best practices](https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices)
