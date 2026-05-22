---
title: Configure Telnyx SIP Trunks for Cisco, Avaya, Thirdlane, Vicidial, OSDial,
  and GOautodial
summary: A practical, consolidated setup guide for connecting popular PBXs and SBCs
  to Telnyx SIP Trunking, including Cisco CUBE/CUCM and CME (IP and credentials),
  Avaya IP Office, Thirdlane, Vicidial (IP and credentials), OSDial, and GOautodial
  (IP and credentials), with shared settings, NAT tips, dialing examples, and key
  references.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
  content_hash: 9f53070e318f4093db77f45d208a88ba442f8fc6b701289748e7f2d81bf11e1c
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
  content_hash: 3806a4300cffd35bf8a51cdb444a548f0b0ce5b53e6bb6a8aba19b5061ce78b5
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
  content_hash: 3b7dc4d18433b1b5095cfa6dc1edfdd8968a4db6d07f485ae773b71254f50084
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
  content_hash: 3821a9503cf5d598ce4e3b201645f3ef0e525c14937189bd5fdc65c84b80eade
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
  content_hash: c6c5e5131bc60074f16759deefae79b98a1fcb8c1a915b63451194442070e61c
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
  content_hash: 02f5d44cb2d3f71bbbb1f41695755d43ff2c13212b3d3f6cb7612fb8776297b5
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
  content_hash: 78e4fae839d64dbcdb85203971bdc39e1047ee77145ff9aa9572430e63f4a7c2
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
  content_hash: 5decfe53ed448f801e5c00c5cc5c50eb60e28a09a62e721028c4fb31712a3130
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
  content_hash: acc54c5742e78fb56ceaa86e0730df7b00407e8779457f1ba9ff1ca4d910bd9b
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
  content_hash: dfea424979422c26a7ec8400bf9e4d2b1045dd18b440b4801c1e125d85bf92df
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
  content_hash: a898edce72275cfa8708972b43692dc548983b36eb860545e6fe9173fcca1e84
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
  content_hash: 7b74c86a02158305eedc73d5a2e8e828dbc5a8df0a253f6250345afd29d167a1
updated_at: 2026-05-20T14:57:05Z
---

# Configure Telnyx SIP Trunks for Cisco, Avaya, Thirdlane, Vicidial, OSDial, and GOautodial

*Part 1 of 2 — see also: [Part 2](configure-telnyx-sip-trunks-for-cisco-avaya-thirdlane-vicidial-osdial-and-goautodial--part-2.md)*

A practical, consolidated setup guide for connecting popular PBXs and SBCs to Telnyx SIP Trunking, including Cisco CUBE/CUCM and CME (IP and credentials), Avaya IP Office, Thirdlane, Vicidial (IP and credentials), OSDial, and GOautodial (IP and credentials), with shared settings, NAT tips, dialing examples, and key references.

## Who this guide is for

Admins who need concise, working examples to register or IP-authenticate PBXs/SBCs to Telnyx and quickly place inbound/outbound calls across Cisco CUBE/CUCM and CME, Avaya IP Office, Thirdlane PBX, Vicidial, OSDial, and GOautodial.

## Before you begin: Telnyx and network prerequisites

- Telnyx Mission Control Portal
  - Create a SIP Connection (IP-based or Credentials) and assign it to your numbers and an Outbound Profile. See Getting Started: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
  - Purchase/provision numbers: https://portal.telnyx.com/#/app/numbers/search-numbers and assign to your Connection.
- Caller ID requirement: Telnyx requires a valid caller ID from your device or an enabled caller ID override on your SIP Connection. Policy: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- Cisco versions (where applicable): CUCM 8.6–12.x (note sub-11.x EoL/EoS per Cisco), IOS 15.1(2)T or later. Cisco recommends no DNS on the system for these examples.
- Encryption (optional but recommended): enable TLS/SRTP where supported. See: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication

## Shared SIP trunk settings (codecs, DTMF, early offer)

- SIP server: sip.telnyx.com
- Codecs: prefer G.711 µ-law, A-law; G.729 as needed. Some platforms also support G.722.
- DTMF: RFC2833 (rtp-nte). Cisco examples may include cisco-rtp, KPML, and NOTIFY in addition.
- Cisco “early-offer forced” and “midcall-signaling passthru” are recommended in examples.
- UDP 5060 by default; TLS typically on 5061 when enabled.

## Cisco CUBE/CUCM with IP authentication (sample config)

Example topology: Telnyx ↔ CUBE ↔ CUCM

Dial-peer toward Telnyx and core SIP/codec settings:

```
dial-peer voice 100 voip                ! arbitrary ID
 translation-profile incoming 100       ! DID → ext (see mapping section)
 destination-pattern 1[2-9]..[2-9]......
 session protocol sipv2
 voice-class sip profiles 1             ! optional SIP header edits
 session target ipv4:192.76.120.10      ! or use session target sip.telnyx.com
 incoming called-number 1[2-9]..[2-9]......
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
 voice-class codec 1
!
voice service voip
 mode border-element
 allow connections sip to sip
 sip
  early-offer forced
  midcall-signaling passthru
  sip-profiles 1                        ! apply SIP Profile if used
!
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
 codec preference 3 g729br8
```

CUCM-facing dial-peer (example extension range 3XXX):

```
dial-peer voice 300 voip
 destination-pattern 3...
 session protocol sipv2
 session target ipv4:172.16.8.10        ! CUCM IP
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
```

Optional trusted IP list (IOS-dependent):

```
voice service voip
 ip address trusted list
  ipv4 192.76.120.10                    ! Telnyx signaling example
  ipv4 64.16.240.36                     ! Telnyx media example
  ipv4 172.0.0.0                        ! CUCM private IP (example)
```

## Cisco CUBE/CUCM with credentials authentication (sample config)

As above, but with DNS target and SIP registration:

```
dial-peer voice 100 voip
 session target sip.telnyx.com
 ... (rest as above)
!
sip-ua
 credentials username <connection_username> password <connection_password> realm sip.telnyx.com
 authentication username <connection_username> password <connection_password> realm sip.telnyx.com
 registrar dns:sip.telnyx.com
```

## Cisco CME with IP authentication (sample config)

Dial-peer and CME mode specifics:

```
dial-peer voice 100 voip
 translation-profile incoming 100
 destination-pattern 1[2-9]..[2-9]......
 session protocol sipv2
 voice-class sip profiles 1
 session target ipv4:192.76.120.10      ! or sip.telnyx.com
 incoming called-number 1[2-9]..[2-9]......
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
 voice-class codec 1
!
voice service voip
 mode cme
 allow connections sip to sip
 sip
  bind all source-interface              ! bind if applicable
  early-offer forced
  midcall-signaling passthru
!
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
 codec preference 3 g729br8
```

## Cisco CME with credentials authentication (sample config)

Same as CME IP-auth, plus SIP registration:

```
sip-ua
 credentials username <connection_username> password <connection_password> realm sip.telnyx.com
 authentication username <connection_username> password <connection_password> realm sip.telnyx.com
 registrar dns:sip.telnyx.com
```

## NAT traversal on Cisco IOS/CUBE/CME (SIP Profiles and loopback)

If the CUBE/CME sits behind NAT (no public interface), rewrite private IPs in SIP/SDP using a SIP Profile and consider a loopback with the public IP:

```
voice class sip-profiles 1
 response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 request  ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Connection-Info      modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Session-Owner        modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Connection-Info      modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Session-Owner        modify "172.x.y.z" "1.2.3.4"
!
interface Loopback0
 ip address 1.2.3.4 255.255.255.0         ! public IP; do not route internally
```

Apply with:

```
voice-class sip profiles 1
```

## Avaya IP Office: basic SIP line to Telnyx

- SIP Line
  - Line Number: available
  - ITSP Domain Name: sip.telnyx.com
  - URI Type: SIP; Location: Cloud; In service: Enable; Check OOS: Enable
- Transport
  - ITSP Proxy Address: sip.telnyx.com; Layer 4: UDP; Port: 5060
  - Use Network Topology Info: select appropriate LAN; set DNS as needed
- SIP URI (channel)
  - Via: your public IP; Local URI/Contact/Display/PAI: *; Reg: 0
  - Incoming/Outgoing Group: match Line number; Max Calls per Channel as required
- Dial Plan (Short Code example)
  - Code: 9N;
  - Feature: Dial; Telephone Number: 1N; Line Group: match SIP Line group; Locale as needed

## Avaya IP Office and Avaya SBC: Telnyx-certified guide

Avaya provides a Telnyx-specific interop document for IP Office 10 with Avaya SBCE R7.1 (UDP). See: https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf

## Thirdlane PBX: trunk, dialing, caller ID, routes, SMS

- Create a SIP Trunk
  - Host/Outbound proxy: sip.telnyx.com
  - Username/Password: your Telnyx credentials (if using registration)
  - Codecs: enable ulaw, alaw, g722, g729; DTMF: RFC2833
- Trunk Dialing and Caller ID tabs: set strip/prepend to match your dialing plan
- Phone Numbers (DIDs): add ranges from Telnyx-provisioned numbers, assign to tenant
- Inbound Routes: build time-based or direct routes to users/IVRs
- Extensions: create user extensions; use SIP username/password for device registration
- SMS (optional): System Management → SMS Gateways → Provider Telnyx; add API Key (see https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them). Enable SMS on numbers and build Inbound SMS routes

Thirdlane docs: https://www.thirdlane.com/docs/platform/introduction

## Vicidial with IP authentication

Admin → Carriers → Add new carrier

- Key fields
  - Carrier ID/Name: Telnyx
  - Type: peer; Host: sip.telnyx.com
  - Disallow: all; Allow: ulaw and g729
  - Insecure: port,invite; DTMF mode: rfc2833; Context: default; Protocol: SIP
  - Global String: Telnyx=SIP/telnyx
- Dialplan example (9 as outside prefix):

```
exten => _91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _91NXXNXXXXXX,3,Hangup
```

Set outbound caller ID per user or per campaign in Vicidial as required by Telnyx policy (link in prerequisites).
