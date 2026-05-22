---
title: PBX Configuration Quick Reference for Telnyx SIP Trunking
summary: A consolidated, platform-agnostic quick-start and best‑practice guide for
  connecting popular PBXs to Telnyx for voice (and where supported, messaging). It
  summarizes common Telnyx settings, authentication choices, routing patterns, codecs/DTMF,
  TLS/SRTP, caller ID/number formats, 3CX compatibility notes, and per‑PBX setup highlights.
sources:
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
  content_hash: ca8b66dd212ee60aac67452ab468347098667aaccf38192b6f08cf12240618dc
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
  content_hash: 9dad394a2f23a7bda745386c3cdc1f5fef79c5be99d90996cfddad040dc0a5af
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
  content_hash: dd14b3ae5db0b472b77e401631fc62ce65c472011bcf388bc4447ffbef1aea59
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
  content_hash: b3351c0654fd9c0f3c952ee0bbdad1c060cfc7e72c773548b2f095e3fb94b7b4
- url: https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk
  content_hash: 119880c00ffca6c847217dbc826da5ec4734b483c51f51573693b665d38d5545
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
  content_hash: 9b3771307849c84657fc6552cab3ba47eb4f98fb074fe1f6f4a6741e80388e84
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
  content_hash: 27340de0b7342195b4012ac67eafd3f4da6a93f4affce90ea8dccb3837223dee
- url: https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx
  content_hash: d8d55c67a7f75f78892b702d533d8c1ca146874c1baa63d63bf36205729e2b04
- url: https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup
  content_hash: 829e62038f5e3df7e38d04d3ef5ad3747b26081a4011d53134f2e89ddcdf7bd4
- url: https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware
  content_hash: 49eb366a50fae38c0ce14ebd52542db63ae8267df11eaafe23365bd3072f364c
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
  content_hash: 3a5d2f05d3846d79ce1ea1f5e0c2131fed914b73cfdb2bb9db72dd55e9fbb4f3
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
  content_hash: 1beed8f31a42eec6d8077583b3e6c3cfd9d7868f31c2c4653c5b5f39b3daf00b
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
  content_hash: 5f1c06f9e784a5a550efde4a7a889e939ff8c174bbd62393c20da79ea4fb8325
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
  content_hash: 5a84022998015a0a424d0863ca842a777e3795064eeb5935acf83b084c5c26c6
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
  content_hash: 2960290b1891b0c9bfcdd18277c19049c41c43c560ae980f7b00b9b28859d4b5
updated_at: 2026-05-20T15:00:35Z
---

# PBX Configuration Quick Reference for Telnyx SIP Trunking

*Part 1 of 2 — see also: [Part 2](pbx-configuration-quick-reference-for-telnyx-sip-trunking--part-2.md)*

A consolidated, platform-agnostic quick-start and best‑practice guide for connecting popular PBXs to Telnyx for voice (and where supported, messaging). It summarizes common Telnyx settings, authentication choices, routing patterns, codecs/DTMF, TLS/SRTP, caller ID/number formats, 3CX compatibility notes, and per‑PBX setup highlights.

## Who this page is for
Engineers and admins onboarding a PBX to Telnyx across common vendor platforms (Yeastar, Vodia, VitalPBX, Xorcom, Epygi, Wildix, PhoneSuite, Positron, PBXes.org, ScopTEL, sipXecs, 3CX). Use it as a checklist and quick reference alongside your PBX’s admin guide.

## Core Telnyx SIP parameters
- Signaling domain: sip.telnyx.com (regional variants available: .ca, .au, .eu)  
  Port: 5060 (UDP/TCP). TLS is available (see Encryption).  
  Outbound proxy: if your PBX asks, set to the same as Hostname (sip.telnyx.com).  
  Domain/From Domain: sip.telnyx.com (use consistently in From/To/SIP URI fields if your PBX requires a Domain separate from Hostname).
- Transport: UDP by default; TCP and TLS are supported where your PBX supports them.
- Registration expiry: 180 seconds is a safe default where configurable.
- Session timers: enable; min ~90s, max ~600s works well.
- RTP: standard RTP over UDP; some systems (e.g., Epygi) have an RTP proxy setting—enable if recommended by the vendor.
- DTMF: RFC2833 (a.k.a. RTP Events). “Auto” is acceptable if RFC2833 is included.
- Codecs (Telnyx-supported):  
  Audio: G.711 µ-law (ulaw), G.711 A-law (alaw), G.722, G.729.  
  Video (where used): H.264.  
  Fax: T.38 is supported on many PBXs (e.g., Wildix) when enabled.
- IPs and firewall: Allow/whitelist Telnyx SIP signaling and media IPs for your region. See https://sip.telnyx.com/#signaling-addresses and https://sip.telnyx.com/#media.

## Authentication: registration vs IP/FQDN
- Credentials (registration) trunks: authenticate with a username/password; most templates expect this and auto‑generate register strings.  
- IP/FQDN (peer/port-based) trunks: authenticate by your PBX’s public IP (or FQDN). Ensure your PBX’s static IP/port is configured on your Telnyx Connection. Disable registration on the PBX for pure IP auth.  
- Many PBXs support both (e.g., Yeastar P‑Series, VitalPBX). Choose based on your security model and NAT traversal needs.

## Caller ID, RPID/PAI, and number formats
- To pass network‑level caller ID reliably, enable Remote‑Party-ID/SIP P‑Asserted‑Identity where available (e.g., Xorcom: sendrpid=PAI; Positron: set P‑Asserted‑Identity to your DID). 
- Caller ID Name (CNAM) presentation in the US is typically database‑based; names set in SIP headers rarely display to US destinations. Canadian destinations may honor outbound CNAM if the device and network support it. Follow vendor guidance (some enforce: capital letters, up to 15 chars, no special characters).
- 3CX (and many modern PBXs) prefer +E.164 formatting. Set your Telnyx Connection inbound number formats to +E.164 to avoid rejections on inbound. Ensure outbound rules normalize to +E.164 (see Dial plan tips).
- If calls reach Telnyx without a caller ID, use a Caller ID Override in your Telnyx Connection outbound options or set a per‑user/per‑route caller ID in the PBX.

## Encryption (TLS/SRTP)
- Recommended when supported. Enable SIP TLS and SRTP on your PBX (e.g., ScopTEL has explicit TLS toggles; Vodia recommends TLS). Ensure you also enable SIP traffic encryption on your Telnyx Mission Control Portal Connection/profile. Use the appropriate TLS port/profile if your PBX separates UDP/TCP from TLS transports.

## Routing basics: dial plans and DID mapping
- Outbound: build patterns for emergency, local, toll‑free, long distance, international, mobiles, and special services. Strip or prepend digits to reach +E.164 when possible. Test with vendor “echo/DTMF” patterns where available (e.g., VitalPBX 4443 audio test, 4747 DTMF test).
- Inbound: match the DID exactly as delivered by Telnyx (e.g., +15551234567). If your PBX supports patterns, ensure they align to the delivered format. Route to an extension, ring group, IVR/auto‑attendant, or time condition.

## 3CX: compatibility and key setup notes
- Telnyx is no longer an official 3CX supported provider. Use the Generic VoIP Provider template in versions that allow third‑party providers (self‑hosted/dedicated). Hosted by 3CX (FREE/PRO/ENT) and StartUP may not expose the generic template. Existing Telnyx trunks continue to work across updates.
- V18: you can import a Telnyx provider XML (when supported) or configure generically. Set Registrar to sip.telnyx.com (or sip‑anycast endpoints if used). Configure inbound/outbound rules and, if using messaging, set Provider URL https://api.telnyx.com/v2/messages, add your Telnyx API key, and paste the 3CX webhook URL into your Telnyx messaging profile.
- V20: use Generic VoIP Provider in Admin → Voice & Chat. Registrar sip.telnyx.com:5060, Register/Account Based auth with your Telnyx SIP credentials. Add DIDs under DID Numbers and assign to users. For SMS, enable Messaging on the DID with your Telnyx API key and webhook.  
- Number formatting: 3CX prefers +E.164. If users dial 001… and calls fail, add an outbound rule to strip 00 and replace with +, or otherwise normalize.
