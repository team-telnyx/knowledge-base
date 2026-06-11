---
title: 'Telnyx Number Management: Search, Ordering, Assignment, and Compliance'
summary: A practical guide to finding, purchasing, assigning, and managing Telnyx
  phone numbers worldwide—including number types and coverage, account-based ordering
  restrictions, international regulatory requirements, advanced (backorder) requests,
  portal management tools, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
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
