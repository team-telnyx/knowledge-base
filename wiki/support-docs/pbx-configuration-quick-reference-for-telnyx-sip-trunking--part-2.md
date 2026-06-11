---
title: PBX Configuration Quick Reference for Telnyx SIP Trunking
summary: A consolidated, platform-agnostic quick-start and best‑practice guide for
  connecting popular PBXs to Telnyx for voice (and where supported, messaging). It
  summarizes common Telnyx settings, authentication choices, routing patterns, codecs/DTMF,
  TLS/SRTP, caller ID/number formats, 3CX compatibility notes, and per‑PBX setup highlights.
sources:
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
- url: https://support.telnyx.com/en/articles/3185933-vodia-multi-tenant-pbx-setup
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5728748-epygi-ip-pbx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
- url: https://support.telnyx.com/en/articles/5790910-positron-ip-pbx
- url: https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx
- url: https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup
- url: https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware
- url: https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-05-20T15:00:35Z
---

# PBX Configuration Quick Reference for Telnyx SIP Trunking

*Part 2 of 2 — see also: [Part 1](pbx-configuration-quick-reference-for-telnyx-sip-trunking--part-1.md)*

A consolidated, platform-agnostic quick-start and best‑practice guide for connecting popular PBXs to Telnyx for voice (and where supported, messaging). It summarizes common Telnyx settings, authentication choices, routing patterns, codecs/DTMF, TLS/SRTP, caller ID/number formats, 3CX compatibility notes, and per‑PBX setup highlights.

## Per‑PBX quick starts (highlights)
- Yeastar P‑Series  
  - Use the Telnyx ITSP template for a credentials trunk; fill in username/password; enable outbound proxy if prompted.  
  - Peer/IP trunk: set Trunk Type to Peer (Port Based), Hostname/IP to sip.telnyx.com, choose transport/port, set Domain same as Hostname/IP. Add your PBX public IP/port to the Telnyx Connection.  
  - Outbound: example prefix 8, strip 1, select the Telnyx trunk.  
  - Inbound: set DID/Caller ID patterns, choose the Telnyx trunk, route to destination.
- Vodia Multi‑Tenant PBX  
  - Trunks → VoIP Providers → Add → Provider: Telnyx (built‑in template), then enter Telnyx username/password.  
  - Inbound: Routing/Redirection → “Send all calls to a specific account” (or other inbound methods). DID Management can map multiple numbers to specific accounts.
- VitalPBX  
  - PJSIP or SIP trunk. Contacts/Match: sip.telnyx.com.  
  - Credentials auth: Require Registration = Yes; IP auth: Require Registration = No.  
  - Codecs: ulaw, g722, g729.  
  - Build comprehensive outbound patterns (emergency, local, toll‑free, LD, international, mobiles, special).  
  - Inbound: DID Pattern must match exact delivered format. Advanced options include CID Lookup, language, MoH, privacy manager, fax detection.
- Xorcom CompletePBX  
  - Technology: SIP. Host sip.telnyx.com, Port 5060. Set Remote Username/Secret (Telnyx creds), From User/Domain, Insecure: port,invite, Qualify Yes, Allow Inbound Calls Yes.  
  - Advanced: sendrpid=PAI to pass caller identity.  
  - Outbound/In‑bound routes: create patterns (e.g., NXXNXXXXXX/1NXXNXXXXXX) and DID mappings.
- Epygi QX (VoIP Carrier Wizard)  
  - Manual carrier: Account Name (Telnyx username), Password, SIP Registrar sip.telnyx.com, SIP Server Port 5060, Use RTP Proxy Enabled.  
  - Define Access code (e.g., 011), Emergency code (911/999), and route inbound to a chosen extension/auto‑attendant.
- Wildix  
  - WMS → Trunks → + (SIP). Basic: Title/Trunk name, Auth login/From user (Telnyx username), Address sip.telnyx.com, Password, Dialplan (e.g., main).  
  - Advanced: audio codecs (ulaw/alaw/g722/g729), H.264 if needed, T.38 Yes, Session timer 90–600, Registration expiry 180, Transport UDP, DTMF RFC2833.
- PhoneSuite Voiceware  
  - Trunk Type SIP; Host sip.telnyx.com, Port 5060, NAT enabled, Register checked, Insecure invite.  
  - Credentials: Username (account number), Secret (Telnyx password).  
  - Codecs: ulaw/alaw/g722/g729. Set channels as needed.
- Positron IP PBX  
  - Trunk: sip.telnyx.com:5060 with Telnyx username/password.  
  - Edit trunk: clear “From User”. Set P‑Asserted‑Identity (Custom) to your Telnyx DID.
- PBXes.org  
  - Add SIP Trunk: set DTMF Auto, sendrpid No. Account: username/password, SIP server/domain sip.telnyx.com, register Yes (inbound and outbound).  
  - Outbound: route via SIP/Telnyx; basic pattern NXXNXXXXXX.
- ScopTEL IP PBX  
  - Telephony Settings → SIP Channel: adjust early media options as needed.  
  - (Optional) Enable SIP TLS and disable server certificate verification if required by environment.  
  - VoIP Account: Type SIP, Trunk Type Friend, Username/Password, Host sip.telnyx.com:5060, Register as UA, (TLS if enabled), Contact = username.  
  - Network: transport UDP/TCP or TLS only if using TLS; Insecure invite.  
  - Options: DTMF Automatic, Send Remote‑Party-ID, select Telnyx‑supported codecs, disallow SIP UPDATE.  
  - Inbound Lines: map Extension (DNIS) to your DID and select the Telnyx trunk.
- sipXecs (SIPfoundry)  
  - Initial setup: set Domain and SIP Domain to sip.telnyx.com; define SIP Realm.  
  - Phones: auto‑provision where possible; manual phones typically require User ID (extension), Domain sip.telnyx.com, Auth (Telnyx account/sub‑account password).  
  - Caller ID naming guidance: capital letters, no special characters, ≤15 chars for best interoperability.
- Bicom PBXware (SMS focus)  
  - PBXware supports Telnyx for messaging. Follow Bicom’s Telnyx integration doc (vendor‑authored) and ensure your Telnyx hosted SMS/messaging profiles and DIDs are provisioned.

## Dial plan tips and examples
- Normalize to +E.164 where possible. If users dial 1NXXNXXXXXX domestically, strip the leading 1 and prepend +1 before sending; for international 011, strip 011 and prepend +.  
- Yeastar example: prefix 8, strip 1 to reach public format.  
- VitalPBX: use X/Z/N/[ranges] patterns for flexible routing; separate emergency, local, toll‑free, LD, international, mobile, and special routes.  
- PBXes.org: basic NXXNXXXXXX with optional 1+NXXNXXXXXX.  
- 3CX: add rules to convert 001… to +… for international; set outbound caller ID per route or per user when needed.

## Messaging (where supported)
- 3CX: enable SMS under the trunk’s SMS tab (or Admin → Voice & Chat → SMS in V20), set Provider URL https://api.telnyx.com/v2/messages, add your Telnyx API key, and paste the 3CX‑provided webhook URL into your Telnyx messaging profile. Assign DIDs to users for send/receive. 
- Bicom PBXware: supports Telnyx provider selection for unified messaging; ensure hosted SMS/DID provisioning on Telnyx.

## Testing and troubleshooting checklist
- Trunk state: registered/green (if using credentials) or reachable (IP auth).  
- Inbound: confirm DID format received by the PBX matches your inbound route pattern. If not, adjust Telnyx inbound number format or PBX pattern.  
- Outbound: verify rules are applying strip/prepend to reach +E.164. Test emergency, local, toll‑free, LD, and international.  
- Caller ID: if missing or rejected, set sendrpid/PAI (PBX) and/or Caller ID Override (Telnyx).  
- DTMF: confirm RFC2833 is negotiated (portal “Auto” ok). Use vendor DTMF test where available.  
- Media: one‑way/no audio? Check NAT/SBC, RTP ports, and that Telnyx media IPs are allowed.  
- TLS/SRTP: confirm matching settings on both ends and that TLS ports/certs are correct.  
- 3CX‑specific: ensure the Generic template is available in your edition; whitelist Telnyx IPs; watch Admin → Advanced → Event Logs for normalization errors (e.g., 001 vs +).  
- DNS: if devices can’t register, validate DNS from the PBX (sipXecs has a DNS Advisor tool).

## Useful external references
- Telnyx Mission Control Portal getting started: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account  
- Telnyx SIP trunking overview: https://telnyx.com/products/sip-trunks  
- Telnyx signaling/media IPs: https://sip.telnyx.com/  
- Codecs and VoIP quality: https://telnyx.com/resources/codecs-affect-voip-sound-quality  
- Caller ID number policy: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy  
- 3CX outbound rules examples: https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/
