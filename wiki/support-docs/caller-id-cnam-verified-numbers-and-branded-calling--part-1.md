---
title: Caller ID, CNAM, Verified Numbers, and Branded Calling
summary: Learn how Telnyx handles Caller ID number and name (CNAM) for inbound and
  outbound calls, how to verify non‑Telnyx numbers for CLI use, when to use Branded
  Calling, how to mitigate “Spam Likely” flags, and the limits, headers, error codes,
  and propagation behaviors to expect.
sources:
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
  content_hash: dd00c3b500e01915122a41df25a115bf5dce41b6a8aaaeaf9683ab306bf1f140
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
  content_hash: c3310a35da8736c228ac12fc321b994fece0d57ed4b4b9fa1e47ab392db16ec7
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
  content_hash: 7ed4c3695720dfa03bb3eb9d0e6a3b4482435cae85a34339584b6cf20b3b18cd
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
  content_hash: 6ee7563e902423b2190c4e495144e572d64a20d2026817495d1af0600e597543
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
  content_hash: f9f883ecd6abe5f848b7e06352ff8969dc2f27342b4f8eb37856e6fbb5f716f0
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
  content_hash: 0e98513b74878e6b415c2a231fda36c870bf1cef823ad3fa34b837d0e5db10aa
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
  content_hash: ef975a113b3f9aff3e16b560784dc65ae39e164ac12d9a84558ff1e321d82dc7
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
  content_hash: bf8b23fb6eade0e9ed5d5cfa8cb64d90406f24f8f3688a963929771755aa9477
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
  content_hash: 91b700ae3627be890dd0cb9f8ac2fa7b089ce289742650521036430c17761275
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
  content_hash: 02c93ada78c36152ee19b74c0b20f833f1db8cd4c325825eb28c0e4de066c482
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
  content_hash: ed8c0874d71606c6466945a7420ca07ce637f47e7cace07239ceee8f20b388a5
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
  content_hash: 2b414106d10c3c5b6fccd732adfd2894b2463b9dcdaa238beca204a12c513a68
updated_at: 2026-05-20T14:37:38Z
---

# Caller ID, CNAM, Verified Numbers, and Branded Calling

*Part 1 of 2 — see also: [Part 2](caller-id-cnam-verified-numbers-and-branded-calling--part-2.md)*

Learn how Telnyx handles Caller ID number and name (CNAM) for inbound and outbound calls, how to verify non‑Telnyx numbers for CLI use, when to use Branded Calling, how to mitigate “Spam Likely” flags, and the limits, headers, error codes, and propagation behaviors to expect.

## Caller ID vs CNAM at a glance
- Caller ID Number (CID/CLI): The phone number shown to the called party on outbound calls.
- Caller ID Name (CNAM): The display name associated with the calling number that may appear to the called party.

## Inbound Caller ID on Telnyx
- Inbound Caller ID Number is provided by default on Telnyx-provisioned numbers.
- Inbound CNAM lookup can be enabled per number in Mission Control (Numbers → select number → enable CNAM Caller ID Lookup). Telnyx dips industry CNAM databases and passes any found name in the SIP INVITE to your connection.
- Pricing: Standard inbound CNAM lookup is billed monthly per number (for example, $0.40/month per number; subject to change).

## Outbound Caller ID Number (CLI)
- Telnyx presents the CLI you send. If you send none, the call may appear as “anonymous” to the recipient.
- Connection-level Caller ID Override: In SIP Connections → Outbound, set “Caller ID Override” and choose when to apply it (Always, Normal Only, Emergency Only). You can also set a Localization Country, optional channel limits, and expert settings.
- Number format and localization: By default, localization is USA, accepting national, 11‑digit, and +E.164 for US destinations; most international destinations require +E.164. If validation fails, Telnyx attempts USA validation; otherwise a 404 invalid destination may be returned.
- SIP headers that can carry CLI (highest to lowest priority):
  1) P-Preferred-Identity (user)  2) P-Asserted-Identity (user)  3) Remote-Party-Id (user)  4) From (user)
  If multiple are present, the highest priority is used.
- Anonymizing CLI: Send a valid CLI and include header Privacy: id. Telnyx will anonymize downstream. Toll‑free and emergency destinations will not be anonymized. Invalid or missing CLI will be rejected with 403 Caller Origination Number is Invalid D35.
- EEA destinations: International calls terminating in the EEA must include a valid, dialable P-Asserted-Identity (PAI). Anonymous/invalid CLIs may be rejected or surcharged by terminating carriers.
- International spoofing: Not supported. Attempted international CLI spoofing is typically rejected (often 503) so you can route advance.

## Outbound Caller ID Name (CNAM)
- CNAM Listing (outbound) associates a name with a number so receiving carriers can show it. Enable per number in Mission Control (Numbers → Voice tab → Enable CNAM Listing) and set up to 15 alphanumeric characters plus spaces. Outbound CNAM listing is free.
- Propagation: Typically updates in 12–24 hours, up to 72 hours; numbers on underlying carriers can take 3–5 business days.
- Coverage and limitations:
  - US: Receiving carriers query third‑party CNAM databases; your listing is inserted there.
  - Canada: No national CNAM database; CNAM is carried in SIP headers (From and P-Asserted-Identity) where supported.
  - Toll‑free and international numbers: CNAM not supported. Some carriers maintain private data, but display isn’t guaranteed. Consider Branded Calling for better control where supported.
  - Display is ultimately decided by the receiving carrier and the subscriber’s settings. Wireless carriers often do not use the industry CNAM database; recipients may instead see the rate center/locality or their own contact name.
- Verification: Use the Telnyx Number Lookup tool in your account to check when your CNAM listing has updated.

## Verified Numbers (use non‑Telnyx numbers as CLI)
- Requirement: After Feb 15, 2023, you must verify any non‑Telnyx number you want to use as outbound CLI through Telnyx. Unverified attempts return 403 Unverified Caller Origination Number D51.
- How to verify (Mission Control → Verified Numbers): Choose SMS or Voice call to receive a verification code, enter it, and the number becomes authorized for CLI use. Telnyx also supports DTMF “press 1 to verify” and webhooks for event delivery.
- Pricing: $0.03 per successful verification plus the channel cost to deliver the OTP (Voice/SMS/Flash) based on destination and product pricing.
- Scope and sharing: Applies to Voice (SIP Trunking/Programmable Voice). Incoming calls/messages continue on the original provider. Numbers verified by the account owner are usable by all users; numbers verified by a sub‑user are limited to that user.
- Sending the CLI: After verification, ensure the verified number is sent in one of the accepted SIP headers (see priority list above).

## Branded Calling (enhanced display on supported US mobiles)
- What it does: Adds verified brand information (display name, and where supported, logo and call reason) to outbound SIP trunking calls.
- Coverage: Currently applies to US‑to‑US calls to US mobile numbers on T‑Mobile and Verizon. Display is not guaranteed.
- How it works: Telnyx attaches verified identity on top of STIR/SHAKEN authentication. Presentation depends on downstream carrier/device support and routing path.
- Setup (Mission Control → Other Products → Branded Calling):
  1) Accept terms. 2) Create/select an Enterprise (your verified organization). 3) Create a Display Identity Record (DIR) with display name, logo (if supported), call reasons, and business details. 4) Submit for review. 5) After approval, add eligible Telnyx numbers you’ll use as CLI. 6) Place calls as normal; no extra SIP headers required.
- Why branding might not appear: Receiving carrier/device may not support branded fields; intermediate carriers may not forward fields; provisioning/propagation delays; destination outside supported scope.

## Mitigating “Spam Likely” flags and call blocking
- First steps:
  - Register your numbers with Free Caller Registry (freecallerregistry.com).
  - Enable CNAM Listing for your numbers (toll‑free excluded). Accurate CNAM helps analytics engines.
  - Allow time and place normal, healthy calls so numbers can “age.” Avoid patterns that resemble unsolicited high‑volume robocalling.
  - Escalate to the terminating carrier using the contacts/forms listed by the USTelecom Industry Traceback Group.
- What you may see:
  - Increased 480/486 responses (Busy Here) when analytics flag traffic.
  - SIP 608 Rejected from some wireless carriers when calls are blocked as suspected fraud (under FCC review; other 6XX codes may appear).
- Best practices: Use Verified Numbers, maintain compliant traffic patterns, and leverage STIR/SHAKEN through Telnyx. Consider Branded Calling where supported to improve call trust.

## Organizing outbound traffic and limits
- Outbound Voice Profiles: Manage allowed international destinations, billing (rate deck), and associate SIP connections/apps. You can tag profiles for reporting and apply advanced controls:
  - Channel Limit (concurrent outbound call cap per profile)
  - Max Destination Rate (block calls above a set per‑minute rate)
  - Daily Spend Limit per connection (per‑connection budget reset at 00:00:00 UTC)
- Tags and reporting: Tag Numbers and Outbound Profiles for easier filtering in CDRs. For outbound calls, CDRs show the tag from the outbound voice profile (not the DID tag).
- Global concurrent outbound calls: New accounts default to 2 concurrent outbound calls; after Level 2 verification, 10 concurrent outbound calls. Higher limits can be requested from Support (provide your use case, especially for >100 channels). When exceeded, calls fail with 403 User channel limit exceeded D1.
