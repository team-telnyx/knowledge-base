---
title: Telnyx SIP Routing, DNS, and Protocol Behavior
summary: A practical guide to how Telnyx handles SIP signaling, DNS/SRV resolution,
  media anchoring, SDP/codecs, PRACK, and record-route/route handling—plus key connection
  settings and the most common Telnyx-specific SIP response codes to aid configuration
  and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
updated_at: 2026-05-20T14:34:53Z
---

# Telnyx SIP Routing, DNS, and Protocol Behavior

*Part 1 of 2 — see also: [Part 2](telnyx-sip-routing-dns-and-protocol-behavior--part-2.md)*

A practical guide to how Telnyx handles SIP signaling, DNS/SRV resolution, media anchoring, SDP/codecs, PRACK, and record-route/route handling—plus key connection settings and the most common Telnyx-specific SIP response codes to aid configuration and troubleshooting.

## SIP transports and media overview
- SIP transports supported: UDP, TCP, TLS.
- Media is carried with RTP; SDP negotiates codecs, ports, and parameters. RTP commonly runs over UDP; TCP is possible but less typical for real-time media.
- Typical audio codecs supported include G.711 μ-law/A-law, G.722, G.729, and Opus; common video codecs include H.263, H.264, and MPEG-4. See Telnyx specs and media IPs at [sip.telnyx.com](https://sip.telnyx.com/).

## DNS and SRV handling for SIP
Telnyx honors SRV records when routing calls to external FQDNs and when receiving calls toward customer FQDNs.
- If the Request-URI (RURI) includes a port (e.g., sip:+1...@sip.example.com:5060): Telnyx performs an A-record lookup and bypasses SRV.
- If the RURI omits a port (e.g., sip:+1...@sip.example.com): Telnyx performs an SRV lookup based on transport; if no SRV exists, it falls back to A-record and uses default SIP ports (UDP/TCP 5060, TLS 5061).
- On SRV failover: if the highest-priority target returns SIP 503, Telnyx tries the next priority target.
- If neither SRV nor A resolve, calls fail with SIP 478 Unresolvable Destination.
Best practices
- Omit the port in your dial “to”/RURI to leverage SRV load balancing and failover.
- Ensure SRV targets each resolve to A/AAAA as appropriate and are globally resolvable.

## SIP URI and subdomain calling
- SIP URI calling (credential-auth connections): enable “Receive SIP URI calls” to allow inbound to username@sip.telnyx.com. Options: disabled, from anyone (unrestricted), or only from my SIP Connections (internal). Billing: $0.002/min if the origin is not identified as on-net; on-net calls follow your rate deck. As an anti-spoofing measure, SIP usernames must begin with a non-numeric character to be considered valid.
- SIP subdomain calling (IP/FQDN/MS Teams auth): set a SIP subdomain and allow “Receive SIP subdomain calls” so calls to user@your-subdomain.sip.telnyx.com are accepted (from anyone or only your connections).
See [SIP URI Calling](sip-uri-calling.md) and [SIP Connection: Inbound & Outbound Settings](sip-connection-inbound-outbound-settings.md).

## Number formats on inbound and outbound
Inbound formatting (DNIS/ANI)
- +E.164: include leading + (default).
- E.164: country code without +.
- National (10 digits): local national format (e.g., 10D for US).
- SIP Username (DNIS only): INVITE presents the connection’s username.
- Hybrid ANI options: +E.164/National and E.164/National dynamically choose 10D for domestic US-to-US; otherwise E.164 (+ optional per selection).
Outbound dialing
- Localization Country: lets users dial local and exit-code formats for the chosen country without explicitly adding +country code.
See [SIP Connection: Number Formats](sip-connection-number-formats.md).

## AnchorSite media anchoring
AnchorSite determines where Telnyx anchors your RTP.
- Latency (default): Telnyx proactively pings your endpoint IPs from all PoPs to select the lowest-latency site. Whitelist Telnyx media IPs so latency checks succeed.
- Manual site selection: choose a specific PoP; Telnyx will fail over media to the next closest site if an issue arises.
- Credential-auth nuance: include your SIP Connection username in the Contact header of your first INVITE (or add X-Telnyx-Username: <username>) so Telnyx can reliably apply your selected AnchorSite.
- Applications: if using a Voice API application, Telnyx uses the webhook host IP for latency site determination.
Note: Setting a webhook URL on a SIP Connection treats calls as programmable; in regions without programmable voice, media may anchor at a different site. Remove the webhook URL if you are not using programmable voice to avoid unintended anchoring. See [Guide to SIP AnchorSite® Settings](guide-to-sip-anchorsite-settings.md) and [SIP Connection: Settings](sip-connection-settings.md).

## SIP connection controls and timeouts
Inbound controls (highlights)
- SIP transport and SIP region: select per Connection (IP/FQDN/MS Teams auth types).
- Timeouts: No Ringback Timeout (default 5s) and No Answer Timeout (default 5s), with configurable bounds.
- Channel limit: cap concurrent inbound calls.
- Ringback behavior: Default pass-through; Generate Ringback Tone (183 with SDP + US tone) or Enable Instant Ringback (180) until early media arrives.
- Codec offer order: choose audio/video codecs and priority.
- Compact headers: enable short-form SIP headers to reduce bandwidth.
- Enable PRACK: require reliable 1xx with PRACK acknowledgements.
- ISUP-to-SIP header conversion: translates incoming ISUP MIME into standard SIP headers.
- STIR/SHAKEN header: include attestation info in webhooks.
- Enable 3rd Party Call Control: for late-media flows (e.g., Cisco UCM).
- Simultaneous Ringing: ring multiple devices on the same credential connection.
Outbound controls (highlights)
- Outbound Voice Profile: must be assigned for termination.
- Outbound channel limit, Caller ID override (including emergency-only), T.38 re-INVITE authority (Telnyx/Customer/Disabled), encrypted media (SRTP), and ringback options (Default/180/183).
Advanced and media options
- DTMF types: RFC 2833 (recommended), Inband, or SIP INFO.
- Encode Contact Header: obscures private addresses to work around NAT/ALG.
- T.38 passthrough on-net; comfort noise generation while on hold.
- RTCP: RTCP+1 vs RTCP mux; optional capture and storage; configure report frequency.
See [SIP Connection: Inbound & Outbound Settings](sip-connection-inbound-outbound-settings.md) and [SIP Connection: Settings](sip-connection-settings.md).

## SDP, codecs, and DTMF/Fax notes
- Telnyx uses early offer on inbound (INVITE contains SDP). If you send no SDP on outbound (late offer), Telnyx will include SDP in 183/200 OK and your ACK must align. The answering UA typically selects the codec.
- Packetization: Telnyx uses ptime:20. Mismatched or unsupported ptimes can degrade audio.
- RTCP: use RTCP+1 (RTP port + 1) by default or RTCP mux to simplify NAT.
- DTMF: works reliably with G.711; is not reliable in G.729 and may be unreliable in G.722. Out-of-band (RFC 2833/telephone-event) is recommended with any codec.
- Fax: use G.711 μ-law/A-law or T.38. Fax does not work over G.729 and is not expected over G.722.
- SDP pitfalls that cause 488/INCOMPATIBLE_DESTINATION: private IP addresses in c= lines, IPv6 media addresses (not supported), unsupported codecs, and SRTP offer/requirement mismatches.
See [Audio and Codecs](audio-and-codecs.md).

## PRACK reliability and behavior
- Telnyx supports PRACK per RFC 3262 on inbound and outbound.
- If your INVITE advertises “Supported: 100rel,” Telnyx will send reliable provisional responses and expect PRACK. If you advertise 100rel but fail to PRACK, the call will time out with 504 Gateway Timeout (reason: prack timeout).
- You can enable Telnyx to request PRACK on inbound by toggling “Enable PRACK” on your Connection. See [Understanding SIP PRACK Protocol](understanding-sip-prack-protocol.md).
