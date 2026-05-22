---
title: 'Telnyx Number Management: Search, Ordering, Assignment, and Compliance'
summary: A practical guide to finding, purchasing, assigning, and managing Telnyx
  phone numbers worldwide—including number types and coverage, account-based ordering
  restrictions, international regulatory requirements, advanced (backorder) requests,
  portal management tools, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
  content_hash: b3f59ca610bd79a3198efcdce5cad274c9c3ccb4cd51d8ebcc54eae4f05e19cc
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
  content_hash: 0829abf4fd4e9361835ed3c86ab8a4452e06029811f1cda48f189cd861c4ad19
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
  content_hash: 07f397ad82d8f5deb6554408df4a319fc20feb2ed30c7a86807d9c913f5a007e
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
  content_hash: d7659c02143ca6f8fb165a1b580165a8270985091fd7c1ce0867a5b5e23e0453
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
  content_hash: 3a43cf590a6e8f2a7294c9004f8515d9dd060620f66964d4dc2fb74b62a88e06
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
  content_hash: efbb25485eb9d394d3faf614f4f8638d0748c595441bf9ba884ab4313da2f683
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
  content_hash: d5b8ffa755b61d3a619fcf8acfb98dc5dbf16215dd491fe2347c0739b1c34fa5
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
  content_hash: 281c794d0728949758a4ed7d72ef227a763cccc0220db671709ea512812a33e2
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
  content_hash: af5583dbe1f0101529e39b076386ce6fd59f116ca65087252c4a169e98a5d911
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
  content_hash: 9c3918e8cda4a3d8acd05a63f2c2c5fa50a36c3b8954a357686acfb3a4971554
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
  content_hash: 36e1dcd92959a114b93d62f2a72420c7e5ae49c6e69f2a260336eb2299f06a80
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
  content_hash: b9891f7eb69788a51aba2a2e1f35c185c3178e4f93bbaf7543ab91eb617c9f7c
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
  content_hash: 25d7a9772bcf31108efec46852cc7927f9fdb862acb4a4c4ef621dd2e614de70
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
  content_hash: 9b06ee1fcb0acced3af574a39b3fe9590b104e4117625116ada7a416c09492d0
updated_at: 2026-05-20T15:36:51Z
---

# Telnyx Number Management: Search, Ordering, Assignment, and Compliance

*Part 2 of 2 — see also: [Part 1](telnyx-number-management-search-ordering-assignment-and-compliance--part-1.md)*

A practical guide to finding, purchasing, assigning, and managing Telnyx phone numbers worldwide—including number types and coverage, account-based ordering restrictions, international regulatory requirements, advanced (backorder) requests, portal management tools, and how to get help.

## Managing numbers in My Numbers
Portal location: https://portal.telnyx.com/#/numbers/my-numbers

What you can do
- View all procured numbers; sort by order date, phone number, connection, billing method. Show up to 100 per page.
- Filters: by Connection/App, partial/full number, procurement Status, Billing Group, Voice Billing Method (per-minute or Channel Billing), and custom Tags.
- Export CSV of all or filtered numbers (downloads via browser).
- Bulk edit (up to 100 at a time): messaging profile, tags, voice settings, emergency settings, or delete.

Per-number configuration
- Settings:
  - General: status, purchase date, active services.
  - Number Management: tags for reporting/tenanting.
  - Porting: set a PIN to prevent unauthorized port-outs.
  - Delete Number.
- Messaging:
  - Routing: assign a Messaging Profile.
  - Deliverability: capabilities for SMS/MMS domestic/international.
- Voice Settings:
  - Routing: assign SIP Connection/Voice App.
  - Billing: assign Billing Group; choose Pay Per Minute or Channel Billing (about channel billing: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it).
- Services (highlights):
  - HD Voice (wideband codecs where supported): https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature.
  - Inbound Call Screening (spam/fraud mitigation; considers reputation and STIR/SHAKEN attestation).
  - CNAM (listings and incoming Caller ID Name): https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam.
  - Call Forwarding (Always or On-Failure).
  - Inbound Call Recording (WAV/MP3, single/dual channel; recordings at https://portal.telnyx.com/#/call-recordings).
  - Voicemail (PIN, email notifications): https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail.
  - Noise Suppression (connection-level setting overrides per-number; applies to both inbound and outbound media; Telnyx client is the media reference point).
- Advanced:
  - Translated Number (custom SIP INVITE/To header mapping—useful for certain ATAs).
  - Media Handling: RTP Auto Adjust; Accept any RTP packets for entire call if needed.
  - Tech Prefix (IP/FQDN-auth connections only). If both Translated Number and Tech Prefix are enabled, INVITE looks like prefix+translated+number.
- Emergency Services (E911): enabling incurs a monthly fee; associate a service address so PSAP sees caller ID and address. Guide: https://support.telnyx.com/en/articles/1130683-e911-setup-guide.

Important notes
- Calling 911 without Emergency Services enabled incurs a $100 fee per call. Ensure caller ID is in +E.164.
- Negative balance >30 days: your account may be abolished. Numbers are removed and held for 2 weeks (only your account can re-buy), then aged 2 more weeks before release to general inventory. Enable low balance alerts: https://support.telnyx.com/en/articles/4277896-notification-settings. Contact numbering@telnyx.com if you need to retain numbers.

## DID services at a glance
Common DID features (availability varies by number/country):
- E911, Call Forwarding, CNAM Listing/Incoming, Inbound Call Recording, HD Voice, Inbound Call Screening. See feature articles linked in sections above for details and limitations.

## Country-specific notes for Great Britain (GB)
- GB local, national, and toll-free numbers are not SMS-capable; only GB mobile numbers support SMS. If you have trouble locating GB local/national/toll-free or mobile numbers, see search tips: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal.

## NPA exhaustion and overlays (US/CA)
- NPA (area code) exhaustion occurs when most numbering resources are assigned. Relief is provided via overlays (new area codes covering the same geography). Overlays require 10-digit dialing (which Telnyx already uses).
- If a desirable NPA is scarce, expand your search to include its overlays. Background and examples: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa.

## Accessing Canadian LRN data
- Canadian LRN data is restricted. Telnyx can enable access for contracted customers who:
  - Obtain CLNPC non-member access approval (apply at https://clnpc.ca/non-member-access/).
  - Pay the CLNPC annual fee (~$2,000 USD) directly to CLNPC.
  - Meet Telnyx’s minimum monthly LRN lookup spend (~$225, about 150k lookups at $0.0015 each). Access is case-by-case.
- Provide proof of approval to your CSM or contact support@telnyx.com. Standard Telnyx Number Lookup pricing applies.

## Getting help from the Telnyx Numbering Team
- Before contacting: search and try ordering; if unavailable, submit a “Request Number.” If your order shows requirements, upload them within 2 days to avoid auto-cancellation; once submitted, the team reviews and will reach out if more info is needed.
- Support hours: Mon–Fri, 9am–5pm CT.
- How to contact:
  - Portal chat (bottom-right when signed in) for fastest updates on existing orders.
  - Email numbering@telnyx.com. Use chat/email to escalate urgent issues during work hours.
- For country documentation requirements, search at https://support.telnyx.com/ or use the International Number Requirements Tool linked above.
