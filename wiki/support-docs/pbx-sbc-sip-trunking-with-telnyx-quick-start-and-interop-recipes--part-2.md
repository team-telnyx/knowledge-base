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

*Part 2 of 3 — see also: [Part 1](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-1.md), [Part 3](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-3.md)*

A single, concise reference that unifies Telnyx-tested SIP trunk settings, NAT/security guidance, caller ID and dial plan tips, plus minimal working configs for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH, Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business Server, and Yeastar P‑Series.

## Platform quick-starts
### Cisco CUBE/CUCM (IP or credentials)
Minimal CUBE dial-peer toward Telnyx (replace numbering plan to suit):
```
dial-peer voice 100 voip
 destination-pattern 1[2-9]..[2-9]......
 session protocol sipv2
 session target sip.telnyx.com
 voice-class codec 1
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
 ! optional header/SDP tweaks
!
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
 codec preference 3 g729br8
!
voice service voip
 mode border-element
 allow connections sip to sip
 sip
  early-offer forced
  midcall-signaling passthru
```
NAT rewrite via SIP Profiles (private→public):
```
voice class sip-profiles 1
 response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 request  ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
```
Inbound DID→extension translation example:
```
voice translation-rule 100
 rule 1 /13125489677/ /3005/
voice translation-profile 100
 translate called 100
! apply under dial-peer:
translation-profile incoming 100
```
Credentials (if using registration):
```
sip-ua
 credentials username <user> password <pass> realm sip.telnyx.com
 authentication username <user> password <pass> realm sip.telnyx.com
 registrar dns:sip.telnyx.com
```
Notes: Some IOS versions support an IP trusted list. CUCM versions 8.6–12.x supported; ensure proper Early Offer.

### Asterisk (PJSIP wizard)
Trunk (no registration for IP-auth): /etc/asterisk/pjsip_wizard.conf
```
[trunk_defaults]
 type = wizard

[telnyx]
 endpoint/transport = 0.0.0.0-udp
 endpoint/allow = !all,ulaw,alaw,G729,G722
 endpoint/rewrite_contact = yes
 endpoint/dtmf_mode = rfc4733
 endpoint/context = from-pstn
 endpoint/force_rport = yes
 aor/qualify_frequency = 60
 sends_auth = no
 sends_registrations = no
 remote_hosts = sip.telnyx.com:5060
```
Example extension template and users:
```
[user_defaults](!)
 type = wizard
 accepts_registrations = yes
 endpoint/context = from-internal
 endpoint/allow = !all,ulaw,alaw,G729,G722
 aor/max_contacts = 1

[Bart](user_defaults)
 endpoint/callerid = Bart <1001>
 inbound_auth/username = Bart
 inbound_auth/password = strong@pass135$
```
NAT (pjsip.conf):
```
[global]
 type = global
[transport-udp-nat]
 type = transport
 protocol = udp
 bind = 0.0.0.0:5060
 local_net = X.X.X.X/24
 external_media_address = X.X.X.X
 external_signaling_address = X.X.X.X
```
Dialplan (extensions.conf) including US/E.164 and “catch‑all”:
```
[from-pstn]
 exten => _+1NXXXXXXXXX,1,Dial(PJSIP/1001)
 exten => _NXXXXXXXXX,1,Dial(PJSIP/1001)

[from-internal]
 exten => _NXXNXXXXXX,1,Dial(PJSIP/+1${EXTEN}@telnyx)
 same  => n,Hangup()
 exten => _X.,1,Dial(PJSIP/+${EXTEN}@telnyx)
 same  => n,Hangup()
```
Tech Prefix variant (IP-auth only): prepend the prefix before the destination (e.g., 9999+1${EXTEN}).

### FreeSWITCH (IP trunk)
Gateway: /usr/local/freeswitch/conf/sip_profiles/external/telnyx.xml
```
<include>
  <gateway name="telnyx">
    <param name="proxy" value="sip.telnyx.com"/>
    <param name="register" value="false"/>
    <param name="caller-id-in-from" value="true"/>
  </gateway>
</include>
```
External profile NAT:
```
<param name="ext-rtp-ip" value="$${external_rtp_ip}"/>
<param name="ext-sip-ip" value="$${external_sip_ip}"/>
```
Sample public dialplan bridging via Telnyx:
```
<extension name="domestic.com">
  <condition field="destination_number" expression="^(\d{11})$">
    <action application="bridge" data="sofia/gateway/telnyx/+${destination_number}"/>
  </condition>
</extension>
```
Security: change the default FreeSWITCH password (vars.xml) before going live.

### Avaya IP Office (SIP Line and Short Code)
SIP Line (example):
- ITSP Domain: sip.telnyx.com
- Transport: UDP, Send Port 5060, Proxy: sip.telnyx.com
- SIP URI: Via = your public IP; Local URI/Contact/Display/PAI = *; In/Out Group = line group; Max Calls per Channel as required
Short Code (dial plan example):
- Code: 9N;  Feature: Dial  Telephone Number: 1N  Line Group: (your SIP line group)  Locale: US
Avaya also publishes Telnyx‑specific interop notes: https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf

### Elastix 4 (ChanSIP)
NAT basics: PBX → PBX > Tools > Asterisk File Editor → sip_nat.conf: set localnet= and externip=, then reload Asterisk.
IP trunk (peer) essentials (Outgoing SIP Settings):
- host=sip.telnyx.com, type=peer, qualify=yes, disallow=all, allow=ulaw&alaw
Inbound SIP Settings (typical): host=sip.telnyx.com, type=friend, insecure=port,invite, disallow=all, allow=ulaw, dtmfmode=RFC2833, nat=force_rport,comedia. Registration string: (leave blank for IP-auth).
Credentials trunk variant includes username/secret and a registration string: your_username:your_password@sip.telnyx.com
Set Outbound Routes (dial patterns like NXXNXXXXXX and 1NXXNXXXXXX) and Inbound Routes (DID → destination).

### Vicidial and OSDial (Carriers)
Carrier basics (similar on both):
- Host: sip.telnyx.com
- Type: peer  Insecure: port,invite
- Disallow: all  Allow: ulaw (and g729 if licensed)
- DTMF: rfc2833  Context: default  Protocol: SIP
- Global String example: Telnyx=SIP/telnyx
Dial plan sample with “9” access code (Vicidial):
```
exten => _91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _91NXXNXXXXXX,3,Hangup
```
Set campaign “Carrier to use” = Telnyx. Configure per‑user or per‑campaign Caller ID to meet Telnyx policy.

### GOautodial (V4)
Add Carrier (Manual):
- Authentication: IP‑Based (IP trunk) or Registration (credentials)
- SIP Server: sip.telnyx.com  Codecs: ulaw/alaw/g722/g729  DTMF: RFC2833  Protocol: SIP
Advanced Account Entry (sample):
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
Dialplan Entry (examples):
```
exten => _NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
exten => _1NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
```
Assign the Telnyx carrier to inbound/outbound campaigns, then import leads as needed.

### Thirdlane PBX
Create Trunk:
- Outbound proxy/Hostname: sip.telnyx.com
- For credentials trunks: set Username/Password; for IP trunks leave Registration blank.
- Codecs: enable ulaw/alaw/g722/g729 as needed; DTMF: RFC2833/in‑audio as required.
Trunk Dialing & Caller ID tabs: set digit strip/prepend rules to match your access codes and normalization.
DIDs/Phone Numbers: add your Telnyx DIDs (with optional prefix) and assign to tenants; build Inbound Routes.
SMS: System Management → SMS Gateways → Provider: Telnyx; set Domain and Telnyx API Key (https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them), then assign an SMS Gateway to numbers.

### Skype for Business Server (on‑prem)
Add PSTN Gateway via Topology Builder:
- Gateway FQDN: sip.telnyx.com
- Listening Port: 5060  Transport: TCP
- Associate with your Mediation Server pool (default Mediation listening port 5068).
Publish topology.
Example EV PowerShell (baseline US plan; customize before production):
```
Set-CsDialPlan -Identity Global -SimpleName Global -DialinConferencingRegion US
New-CsVoiceNormalizationRule -Name 'US-National' -Parent Global -Pattern '^1?([2-9]\d\d[2-9]\d{6})\d*(\D+\d+)?$' -Translation '+1$1' -Priority 0
Set-CsVoicePolicy -Identity Global -PstnUsages @{add="US-Basic-PSTN-Usage"}
New-CsVoiceRoute -Identity "US-Basic-Voice-Route" -NumberPattern ^+ -PstnGatewayList @{add="PstnGateway:sip.telnyx.com"} -PstnUsages @{add="US-Basic-PSTN-Usage"}
Set-CsTrunkConfiguration -Identity Global -SRTPMode Optional -ConcentratedTopology $true -EnableReferSupport $false
```

### Yeastar P‑Series
Registration (credentials) trunk:
- Use the Telnyx ITSP template if available; set Username/Password (Authentication Name typically same as Username). Host/Domain: sip.telnyx.com. Enable Outbound Proxy if required.
Peer/IP trunk:
- Trunk Type: Peer (Port Based); Hostname/IP: sip.telnyx.com; Port per transport (UDP/TCP 5060, TLS commonly 5061). Add your PBX static IP/port to the Telnyx IP Connection.
Routing:
- Outbound Route: set dial pattern (e.g., prefix 8., strip 1) and select the Telnyx trunk.
- Inbound Route: choose Telnyx trunk, match DID pattern, set destination.
