---
title: Telnyx Voice Features and Configuration Guide
summary: 'A concise, practical guide to key Telnyx voice capabilities and setup: DTMF
  options, conferencing, external call transfers, toll‑free calling, inbound call
  screening, outbound call frequency controls, and configuring Voice (Call Control/TeXML)
  applications.'
sources:
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
  content_hash: eca05760ac52d8939755113da7cac2cb309d80dd4d2a63799b7946e8bce56a88
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
  content_hash: 48ed94a538de2afcbf2edd6c99979d2bd18e84f6e857546d4de93687d98bd561
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
  content_hash: 87a3ef8934a4ea295cfbee20770cfba6e6fbd4cba3b7303f292cf958b925a3e8
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
  content_hash: e58bb49536560bf0e727e6e9ea7478dfb4ce5578f29b5fb421d269fa39274aef
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
  content_hash: 7fb265531404f200ca6089ea7f6aa3dbcfbac7016ef1d65241ea23dad88bbe80
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
  content_hash: bb88f080367abb94e438da1c2c95948b2d5cd8f82ada4e1bb61a04b837aa5803
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
  content_hash: 5d6f46157248ab1f327f97d5be84ed00858bc94461190530a3a0b8f663ad21a8
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
  content_hash: ceed70d8d1185bedf8a5d4bf2518f0deadb9132aea3c87943cf02d2900e85d78
updated_at: 2026-05-20T14:31:30Z
---

# Telnyx Voice Features and Configuration Guide

A concise, practical guide to key Telnyx voice capabilities and setup: DTMF options, conferencing, external call transfers, toll‑free calling, inbound call screening, outbound call frequency controls, and configuring Voice (Call Control/TeXML) applications.

## DTMF Basics and Configuration
DTMF (Dual-Tone Multi-Frequency) encodes keypad presses as pairs of audio frequencies. Over VoIP/SIP, Telnyx supports three transmission methods you can choose per SIP Connection or Voice Application:

- RFC 2833 (RTP Events) – Recommended default. Digits ride in RTP as named telephony events (separate from audio), codec‑agnostic, broadly supported.
- Inband – Tones are embedded in the audio. Useful for legacy analog/ATA gear. Susceptible to compression (e.g., G.729, Opus) and may cause missed digits.
- SIP INFO – Digits travel in SIP signaling. Immune to codec issues; not universally supported and timing can vary. Often used for SIP‑to‑SIP.

Choosing: For most deployments use RFC 2833. If the far end requires it, use SIP INFO. Use Inband only when compatibility with legacy devices mandates it and avoid compressed codecs.

Configure on a SIP Connection (Portal):
1) Log in to the Telnyx Portal. 2) Real Time Communications → Voice → SIP Trunking. 3) Edit your connection → Configuration tab. 4) Set DTMF type (RFC 2833, Inband, SIP INFO) → Save.

Configure in Voice Apps: Both Call Control and TeXML apps expose a DTMF Type setting (same three options). SIP INFO is mainly for SIP‑to‑SIP and final DTMF behavior is negotiated end‑to‑end.

Learn more: What DTMF is and recommended usage, with timing guidance and codec caveats, in the Telnyx Help Center.

## Conference Calling Options
Telnyx supports conferencing in multiple ways:
- Voice API (Call Control) – Full programmatic control to create and manage conferences.
- TeXML – Simple XML‑driven conference rooms via the <Conference> verb.
- SIP Trunking – Use your PBX (e.g., Asterisk, 3CX) with Telnyx trunks.
- Video API – Build audio/video conferencing apps.

Developer resources:
- TeXML Conference: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- Voice API conference commands: https://developers.telnyx.com/api-reference/conference-commands
- Conferencing tutorial: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo

## Toll‑Free Calling and Numbers
- Outbound: You can dial toll‑free numbers from your Telnyx number.
- Inbound: You can buy domestic or international toll‑free numbers from Telnyx. International toll‑free is typically reachable only in‑country and must follow local dialing rules.
- US/CA share: 800, 833, 844, 855, 866, 877, 888.
- Document requirements for international numbers: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents

## External Call Transfers (Keeping Original Caller ID)
Scenario: Your SIP endpoint receives a PSTN call (A → your Telnyx number B) and transfers it out to C while preserving A as the caller ID.

Key points:
- The transfer creates a new outbound call (A → C). Telnyx validates it as an external transfer.
- Telnyx checks: (1) There’s an active inbound call from A to B, and (2) the outbound call includes a SIP Diversion header indicating B.
- If validation fails, Telnyx rejects with 403 Unverified origination number D51.

Programmable Voice methods that preserve the non‑Telnyx origination number:
- Voice API Transfer command – Transfer the established inbound call to a new destination.
- Voice API Dial + Bridge – Dial with link_to set to the existing call_control_id and bridge_intent=true.
- TeXML <Dial> – Place a new call and bridge it to the existing inbound call.

## Configuring Voice Applications (Call Control and TeXML)
Create and manage applications under Voice → Programmable Voice in the Portal.

Core settings (Call Control Voice API app):
- Webhooks: Primary and failover URLs (HTTPS), choose Webhook API version (use V2), optional hang‑up on timeout, and custom retry delay.
- Media routing: AnchorSite (latency‑optimised or fixed site).
- DTMF Type: RFC 2833 (default), Inband, SIP INFO.
- RTCP Capture: Enable to power QoS reports (Debugging → SIP Call Flow Tool).
- Call Cost webhook: Optional event on call completion.
- Inbound: SIP subdomain (optional), inbound channel limit, enable STIR/SHAKEN headers in webhooks, codecs to offer.
- Outbound: Assign an Outbound Voice Profile and set outbound channel limits.
- App ID: Visible in app settings; reference it in API calls.

TeXML app highlights:
- Voice/Status callback methods and URLs (primary/failover).
- Optional hang‑up on timeout.
- DTMF Type selection (same options as above).

Developer references: Call Control command set (Dial, Transfer, etc.) and TeXML setup are documented at https://developers.telnyx.com/

## Inbound Call Screening (Spam Protection)
Purpose: Protect Telnyx numbers from unwanted/spam calls by rejecting or flagging them based on reputation, number validity, and SHAKEN/STIR.

How it works:
- Reputation data: Aggregates multiple sources (e.g., Nomorobo, YouMail, CallerAPI) to assess the caller’s CLI.
- Number validation: Flags invalid/non‑existent originating numbers.
- SHAKEN/STIR: Screening applies to Attestation C and Attestation Invalid (North America). Reputation screening currently applies to calls originating in the US/CA.

Actions:
- Flag Calls: The call is delivered but marked as suspicious. Indicators: “SPAM LIKELY” appears in the display name of From and P‑Asserted‑ID; SIP header X‑Telnyx‑Call‑Screening: SPAM LIKELY is added. If webhooks are enabled, call.initiated includes call_screening_result (e.g., spam_likely).
- Reject Calls: Suspicious calls are blocked at the network and do not reach your infrastructure.

Configuration (per number):
1) Portal → My Numbers → select a number → Edit. 2) Voice tab → Enable Inbound Call Screening. 3) Choose Flag Calls or Reject Calls → Save.

Cost: Free (as of Mar 17, 2026).

Tip: Enable webhooks on your SIP Connection or Voice Application to receive the call_screening_result in call events.

## Outbound Repeat Call Guard (Per‑Number Frequency Limits)
Purpose: Limit how many times you can call the same destination number (CLD) within defined daily hours to prevent over‑dialing. Applies to calls placed via SIP connections and is enforced per Outbound Voice Profile.

Setup (Portal):
1) Voice → Outbound Voice Profiles → open/create a profile. 2) Find Repeat Call Guard. 3) Enable and set:
- Start Time (UTC) and End Time (UTC) for the active window.
- Calls per CLD (max allowed attempts per destination within the rolling window).

Behavior:
- When the limit is hit, further calls to that CLD return 403 Daily calling restriction to Destination Number … exceeded D66.
- Rolling reset within the daily window: new “slots” reopen on the 24‑hour marks from the prior day’s first allowed call within the window.

Tips:
- All times are UTC—convert from local time as needed.
- Limits are tracked independently per Outbound Voice Profile.

API configuration: You can PATCH outbound_voice_profiles via the Telnyx API (see API reference at https://developers.telnyx.com/).

## Where to Learn More
- [Voice API Essentials](voice-api-essentials.md) – Curated guides for Call Control/TeXML, STIR/SHAKEN, caller ID, and more.
- Developer docs home: https://developers.telnyx.com/
- Telnyx Portal: https://portal.telnyx.com

## Support
Telnyx Support is available 24/7:
- Email: support@telnyx.com
- Phone: +1 888 980 9750
