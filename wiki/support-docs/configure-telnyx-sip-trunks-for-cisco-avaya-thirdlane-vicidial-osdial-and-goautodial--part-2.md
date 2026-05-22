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
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
updated_at: 2026-05-20T14:57:05Z
---

# Configure Telnyx SIP Trunks for Cisco, Avaya, Thirdlane, Vicidial, OSDial, and GOautodial

*Part 2 of 2 — see also: [Part 1](configure-telnyx-sip-trunks-for-cisco-avaya-thirdlane-vicidial-osdial-and-goautodial--part-1.md)*

A practical, consolidated setup guide for connecting popular PBXs and SBCs to Telnyx SIP Trunking, including Cisco CUBE/CUCM and CME (IP and credentials), Avaya IP Office, Thirdlane, Vicidial (IP and credentials), OSDial, and GOautodial (IP and credentials), with shared settings, NAT tips, dialing examples, and key references.

## Vicidial with credentials authentication

As above, but:

- Type: friend; Username/Password: your Telnyx credentials; Host: sip.telnyx.com
- Global String and Dialplan remain the same pattern.

## OSDial: IP trunk

Admin → Carriers → Add new carrier

- Carrier ID/Name: Telnyx; Type: Peer; Host: sip.telnyx.com
- Disallow: all; Allow: ulaw and G729; Insecure: port,invite
- DTMFMode: RFC 2833; Context: default; Protocol: SIP; Global String: Telnyx=SIP/telnyx
- Dial Plan (9 as outside prefix):

```
exten => _9NXXXXXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _9NXXXXXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _9NXXXXXXXXXX,3,Hangup
```

## GOautodial with IP authentication

Settings → Carriers → Add (+) → Manual

- Authentication: IP-Based
- SIP Server: sip.telnyx.com; Protocol: SIP; DTMF: RFC2833; Codecs: ulaw/alaw/g722/g729 as needed
- Advanced → Account Entry example:

```
[telnyx]
disallow=all
allow=ulaw
allow=alaw
type=friend
dtmfmode=rfc2833
qualify=yes
nat=yes
host=sip.telnyx.com
insecure=invite
```

- Advanced → Dialplan Entry example:

```
exten => _X.,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
exten => _1NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
```

If using IP auth behind NAT/load balancers, see Telnyx IP auth guidance: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token

## GOautodial with credentials authentication

Settings → Carriers → Add (+) → Manual

- Authentication: Registration; Username/Password: Telnyx credentials
- Server/Host: sip.telnyx.com; Port: 5060 (UDP) or 5061 (TLS)
- DTMF/Codecs as above; use the same Advanced Account/Dialplan entries (host remains sip.telnyx.com)

## Inbound DID mapping examples (Cisco translation rules)

Translate a DID to a CUCM/CME extension and apply on the Telnyx-facing dial-peer:

```
voice translation-rule 100
 rule 1 /13125489677/ /3005/
!
voice translation-profile 100
 translate called 100
!
! Under the Telnyx-facing dial-peer
translation-profile incoming 100
```

Route the translated extension to CUCM (example 3XXX pattern) with a CUCM dial-peer as shown in Cisco sections.

## Allow-listing Telnyx signaling/media IPs

Some IOS versions support a trusted list. Example values used in Telnyx docs:

```
voice service voip
 ip address trusted list
  ipv4 192.76.120.10     ! signaling example
  ipv4 64.16.240.36      ! media example
```

Always verify current Telnyx IP ranges for your region and product before enforcing allow-lists.

## Caller ID and compliance reminder

For outbound calls to complete, present a valid caller ID or enable a caller ID override on your Telnyx SIP Connection: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy

## References

- Cisco CUBE/CUCM: https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html and integration example https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html
- Cisco CME admin and SIP trunking examples: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html and https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html
- Avaya support/docs: https://support.avaya.com/ and Telnyx interop guide https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf
- Thirdlane docs/support/API: https://www.thirdlane.com/docs/platform/introduction https://www.thirdlane.com/support https://www.thirdlane.com/docs/platform/api
- Vicidial support/manual: https://www.vicidial.com/?page_id=151 and https://www.vicidial.org/download_survey.php
- OSDial support/community: https://osdial.com/support/ and https://osdial.com/sitemap/
- GOautodial docs/forums: https://goautodial.org/projects/goautodialce/wiki and https://goautodial.org/projects/goautodialce/boards
