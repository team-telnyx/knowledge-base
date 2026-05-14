---
title: Telnyx Voice and SIP Essentials
summary: 'A practical guide to core Telnyx voice features and policies: E911 setup
  and testing, Caller ID and CNAM, DTMF configuration, organizing SIP traffic and
  outbound controls, SIP headers for transfers and billing, short-duration call policy,
  fax over T.38/G.711, and conference calling options.'
sources:
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
updated_at: 2026-05-14T11:30:56Z
---

# Telnyx Voice and SIP Essentials

*Part 1 of 2 — see also: [Part 2](telnyx-voice-and-sip-essentials--part-2.md)*

A practical guide to core Telnyx voice features and policies: E911 setup and testing, Caller ID and CNAM, DTMF configuration, organizing SIP traffic and outbound controls, SIP headers for transfers and billing, short-duration call policy, fax over T.38/G.711, and conference calling options.

## E911 setup, addresses, and testing

Enable E911 per number in the Mission Control Portal.
- On the target number, click the ambulance icon, toggle Emergency Services, choose an existing emergency address or add a New Address, then Save and accept the monthly charge to enable. A green confirmation banner indicates success.
- We recommend enabling emergency notifications so you’re alerted if this number dials emergency services. Create channels in Advanced Features → Notifications in the portal, then save on the number.

Register emergency addresses before enabling on numbers that may place 911 calls.
- Numbers → My Numbers → Emergency Address → Add Address. Provide first/last or business name, and the address (search or enter country, state/province, city, ZIP/postal, street, extended address).
- Important: 911 calls without a registered address or with invalid Caller ID are considered unregistered and may incur a $100 penalty.

Test with 933 (address readback) in the US and Canada.
- Dial 933 from a device registered to the same Telnyx account that owns the number. The service confirms the registered address.
- Requirements: your Caller ID must be in +E.164 format (must include the + and country code). Header preference order is typically: P-Preferred-Identity, P-Asserted-Identity, Remote-Party-ID, then From. Ensure the chosen header contains the +E.164 CLI.
- Limitations: 933 is US/Canada only. For international availability, email numbering@telnyx.com and see Supported Emergency Numbers: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- 933 confirms address only; business name is provided on live 911 calls.

## Caller ID and CNAM (inbound and outbound)

- Caller ID Number (CID) displays your phone number. Caller ID Name (CNAM) displays a name associated with your number.

Inbound
- By default, Telnyx passes the inbound caller’s number to you.
- Enable inbound CNAM lookup per number (My Numbers → edit number → CNAM Caller ID Lookup). Accept the monthly recurring charge (commonly $0.40/mo per number; subject to change) and save.

Outbound
- Your outbound calls present the CLI you send. If none is provided, the callee may see “anonymous.”
- You can set a connection-level Caller ID Override (Voice → SIP Trunking → edit connection → Outbound tab). Choose when to apply (Always, Normal Only, Emergency Only), set Localization Country, optional Channel Limit and Expert Settings, then save.
- International spoofing isn’t supported. Many carriers reject calls with non-local or spoofed CLIs; expect 503 responses in such cases.

Outbound CNAM Listing (name delivery)
- Enable CNAM Listing on the number and set up to 15 alphanumeric characters (spaces allowed). Outbound CNAM is free.
- Propagation: typically 12–24 hours, up to 72 hours; for numbers on underlying carriers, 3–5 business days. Use the Number Lookup tool to verify when updated: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- US: receiving carriers dip third-party CNAM databases.
- Canada: CNAM is passed in SIP headers (FROM, P-ASSERTED-IDENTITY).
- Not supported on toll-free or international numbers. Display is ultimately controlled by the receiving carrier; wireless carriers often don’t use the industry CNAM dip.

Formatting reminder
- For emergency calls and consistent delivery, always send Caller ID in +E.164 with the leading + in your chosen identity header.

## DTMF over SIP: methods and configuration

Telnyx supports three DTMF methods. Configure per SIP connection (Voice → SIP Trunking → edit connection → Configuration → DTMF type), then save.
- RFC 2833 (recommended): sends digits as RTP named telephony events, codec-agnostic and widely supported.
- Inband: tones ride in the audio; can fail with compressed codecs (e.g., G.729, Opus). Best for legacy ATAs/hardware that require it.
- SIP INFO: digits travel in SIP signaling, immune to codec issues; may have timing differences and not universally supported. Use only if required by the far end.

Tip: Start with RFC 2833. Consider SIP INFO if using compressed codecs or the destination mandates it. Avoid Inband with compressed codecs.

## Organizing SIP traffic and controlling outbound behavior

SIP Connections and reporting
- SIP Connections handle inbound and outbound traffic. Reporting can be aggregated “By Connection,” and CDRs include the connection with filters for connection, record type, call type, CLI/CLD, and tags.

Tagging Numbers and Outbound Voice Profiles
- Use the tag icon on Numbers and Outbound Profiles to add/remove tags for organization and filtering in CDRs. Inbound CDRs show the DID’s tags; outbound CDRs show the outbound voice profile’s tags.

Repeat Call Guard (Outbound Voice Profiles)
- Enforce daily limits on how often a destination number (CLD) can be called within defined hours. Configure per Outbound Voice Profile (Voice → Outbound Voice Profiles → open profile → Repeat Call Guard).
  - Set Start Time and End Time (UTC) and the max Calls per CLD.
  - Once the limit is hit, additional calls to that destination are blocked until the counter rolls over. Telnyx responds with 403 “Daily calling restriction to Destination Number … exceeded D66.”
  - Counters use a rolling 24-hour reset from the time of the previous day’s first allowed call within the active window.
- API configuration is also available via PATCH to the Outbound Voice Profiles endpoint with the calling_window object.

Tips
- Convert local business hours to UTC when configuring.
- Disable temporarily if you need unrestricted dialing.

## SIP headers for transfers, identity, and billing

External Call Transfers (A → your number B → transfer to C)
- Your endpoint initiates a new outbound call from A to C. Telnyx allows this when:
  - There’s an active inbound call from A to B; and
  - The outbound INVITE includes a SIP Diversion header showing B (the originally called Telnyx number).
- If no match or Diversion is missing/incorrect, Telnyx rejects with 403 “Unverified origination number D51.”

Programmable Voice alternatives that preserve non-Telnyx origination
- Voice API Transfer command: instructs Telnyx to transfer an established inbound call.
- Voice API Dial + Bridge: place an outbound call and bridge to an existing inbound call by including link_to (bridging call’s call_control_id) and bridge_intent=true.
- TeXML <Dial>: place a new outbound call and connect it to the inbound call.

P-Charge-Info for private PBX billing
- Some scenarios (and carriers) use the P-Charge-Info header to identify a billing number. On FreePBX/Asterisk, add a predial hook macro (macro-dialout-trunk-predial-hook) to inject P-Charge-Info: +E.164_DID into outbound INVITEs. Reload the dialplan (fwconsole reload) and verify via SIP debug that the header is present. Apply the rule only to the intended IP-based trunk.

## Short-duration outbound calls policy

- Short Duration Calls (SDCs) are outbound calls of 6 seconds or less.
- Up to 15% of your monthly connected outbound calls may be SDCs. If you exceed 15% during the month you’ll be alerted; if still above 15% at month end, additional charges apply to all SDCs that month (see Telnyx Terms).
- International: as of Jan 1, 2024, SDCs to international destinations are subject to $0.01 per call when your monthly SDC rate exceeds 15%.
- Calculation is based on connected calls only and uses UTC timestamps.
- To investigate, export outbound detail reports, sort by duration, remove zero-duration calls, count calls ≤6s, and correlate to SIP connection names to find sources.
