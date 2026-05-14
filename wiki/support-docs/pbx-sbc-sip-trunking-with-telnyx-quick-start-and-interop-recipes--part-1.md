---
title: 'PBX/SBC SIP Trunking with Telnyx: Quick-start and Interop Recipes'
summary: A single, concise reference that unifies Telnyx-tested SIP trunk settings,
  NAT/security guidance, caller ID and dial plan tips, plus minimal working configs
  for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH,
  Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business
  Server, and Yeastar P‑Series.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
updated_at: 2026-05-14T11:27:37Z
---

# PBX/SBC SIP Trunking with Telnyx: Quick-start and Interop Recipes

*Part 1 of 3 — see also: [Part 2](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-2.md), [Part 3](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-3.md)*

A single, concise reference that unifies Telnyx-tested SIP trunk settings, NAT/security guidance, caller ID and dial plan tips, plus minimal working configs for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH, Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business Server, and Yeastar P‑Series.

## Pre-requisites and Mission Control setup
- Create a Telnyx account and complete initial setup: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Buy DIDs: https://portal.telnyx.com/#/app/numbers/search-numbers
- Create a SIP Connection:
  - IP-based (peer/IP) or Credentials-based (registration). https://portal.telnyx.com/#/app/connections
- Assign your DID(s) to the Connection (Provision numbers): https://portal.telnyx.com/#/app/numbers/my-numbers
- Create an Outbound Voice Profile and attach your Connection: https://portal.telnyx.com/#/app/outbound

## Authentication options
- IP (peer) authentication: Your PBX/SBC’s public IP/port is authorized. No SIP registration. Some platforms call this “Peer Trunk,” “IP trunk,” or “Gateway.”
- Credentials (registration) authentication: PBX registers with username/password (“VoIP Register Trunk,” “SIP trunk (registration),” etc.).
- Tech Prefix (IP-auth only): If your IP Connection uses a tech prefix, prepend it in your outbound dial plan (see Asterisk example below). Background: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix

## Core SIP and media defaults (Telnyx)
- SIP domain/proxy: sip.telnyx.com
- Ports: 5060 (UDP/TCP). TLS available (commonly 5061) where supported.
- Codecs: ulaw (G.711u), alaw (G.711a), G.729, G.722. Prefer ulaw/alaw unless you need compression.
- DTMF: RFC2833/RFC4733 (commonly labeled RFC2833 in GUIs).
- Early Offer/SDP in INVITE: Enable where available (e.g., Cisco CUBE “early-offer forced”).

## Network, NAT and security
- Firewall/Allowlisting: Permit outbound/inbound SIP/RTP to Telnyx. Example CUBE trusted list IPs: 192.76.120.10 and 64.16.240.36 (adjust per your region/routing).
- NAT traversal:
  - Cisco CUBE: use SIP Profiles to rewrite private to public IPs in Contact/SDP; consider a loopback with public IP (do not route it internally).
  - Asterisk PJSIP: set local_net, external_signaling_address, and external_media_address in pjsip.conf.
  - FreeSWITCH: set ext-sip-ip and ext-rtp-ip (or autonat) in external profile.
- Encryption (optional but recommended): Enable TLS/SRTP where supported. Overview: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication

## Caller ID and dial plan basics
- Outbound Caller ID requirement: Telnyx requires a valid CLI from your device or a Caller ID override enabled on the SIP Connection. Policy and enablement: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- Common US patterns (examples; adapt to your locale):
  - 10D: NXXNXXXXXX
  - 11D: 1NXXNXXXXXX
  - E.164: +1NXXNXXXXXX
- Normalization examples:
  - Add country code: 10D → +1${EXTEN}
  - Pass 11D as +E.164: 1NXXNXXXXXX → +${EXTEN}
- Tech Prefix (IP-auth only): prepend e.g., 9999+1${EXTEN} in your outbound dial.
