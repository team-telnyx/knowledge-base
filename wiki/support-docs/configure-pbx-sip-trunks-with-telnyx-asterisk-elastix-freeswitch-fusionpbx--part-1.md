---
title: Configure PBX SIP Trunks with Telnyx (Asterisk, Elastix, FreeSWITCH, FusionPBX)
summary: End-to-end reference for configuring SIP trunks to Telnyx across popular
  open-source PBXs. Covers IP/FQDN and credentials-based trunks, core dialplans, NAT/media
  settings, and key UI steps for Asterisk (PJSIP), Elastix 4/5, FreeSWITCH, and FusionPBX.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
updated_at: 2026-05-20T14:55:25Z
---

# Configure PBX SIP Trunks with Telnyx (Asterisk, Elastix, FreeSWITCH, FusionPBX)

*Part 1 of 2 — see also: [Part 2](configure-pbx-sip-trunks-with-telnyx-asterisk-elastix-freeswitch-fusionpbx--part-2.md)*

End-to-end reference for configuring SIP trunks to Telnyx across popular open-source PBXs. Covers IP/FQDN and credentials-based trunks, core dialplans, NAT/media settings, and key UI steps for Asterisk (PJSIP), Elastix 4/5, FreeSWITCH, and FusionPBX.

## Before you begin

- Create a Telnyx SIP Connection in Mission Control Portal:
  - IP/FQDN-based for static IP/FQDN systems, or Credentials-based for registration auth.
  - Assign the connection to your DID(s) and an Outbound Voice Profile to enable inbound/outbound calling.
- Purchase and provision numbers to your connection.
- Recommended: Enable TLS if supported by your PBX and network.
- Software versions: Asterisk 18+, current FreeSWITCH; FreeSWITCH v1.8 is EOL and must be upgraded.
- Telnyx does not support IAX2.

Useful links:
- Getting started with Mission Control: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Asterisk docs: https://docs.asterisk.org/
- FreeSWITCH docs: https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/

## Asterisk (PJSIP) – IP-based trunk

Edit /etc/asterisk/pjsip_wizard.conf:

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

Notes
- Requires res_pjsip_config_wizard (present in Asterisk 13.2.0+).
- Use your IP/FQDN in Mission Control for this connection type; no registration or auth is sent.

## Asterisk (PJSIP) – Credentials trunk

Edit /etc/asterisk/pjsip_wizard.conf:

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
sends_auth = yes
sends_registrations = yes
remote_hosts = sip.telnyx.com:5060
outbound_auth/username = <your_username>
outbound_auth/password = <your_password>
registration/expiration = 600
```

## Asterisk – Local extensions via PJSIP wizard

In /etc/asterisk/pjsip_wizard.conf, define a template and users:

```
[user_defaults](!)
type = wizard
accepts_registrations = yes
sends_registrations = no
accepts_auth = yes
sends_auth = no
endpoint/context = from-internal
endpoint/allow = !all,ulaw,alaw,G729,G722
endpoint/dtmf_mode = rfc4733
endpoint/rewrite_contact = yes
endpoint/force_rport = yes
aor/max_contacts = 1
aor/remove_existing = yes
aor/minimum_expiration = 30

[Bart](user_defaults)
hint_exten = 1001
endpoint/callerid = Bart <1001>
inbound_auth/username = Bart
inbound_auth/password = strong@pass123$

[Lisa](user_defaults)
hint_exten = 1002
endpoint/callerid = Lisa <1002>
endpoint/allow = !all,ulaw
inbound_auth/username = Lisa
inbound_auth/password = strong@pass246$
```

## Asterisk – PJSIP global/NAT

For NATed installs, add to /etc/asterisk/pjsip.conf:

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
allow_reload = no
```

If not behind NAT, omit external_* settings.

## Asterisk – Dialplan examples

In /etc/asterisk/extensions.conf:

```
[from-pstn]
exten => _+1NXXXXXXXXX,1,Dial(PJSIP/1001)
exten => _NXXXXXXXXX,1,Dial(PJSIP/1001)

[from-internal]
exten = _NXXNXXXXXX,1,Dial(PJSIP/+1${EXTEN}@telnyx)
same = n,Hangup()

exten = _X.,1,Dial(PJSIP/+${EXTEN}@telnyx)
same = n,Hangup()
```

Tech prefix (if configured on your IP connection) must be prepended when sending to Telnyx, for example with prefix 9999:

```
[from-internal]
exten = _NXXNXXXXXX,1,Dial(PJSIP/9999+1${EXTEN}@telnyx)
same = n,Hangup()
exten = _X.,1,Dial(PJSIP/9999+${EXTEN}@telnyx)
same = n,Hangup()
```

## Elastix 4 – IP trunk (IP auth)

- PBX UI: PBX > Tools > Asterisk File Editor, edit sip_nat.conf:
  - localnet=<your_subnet>
  - externip=<your_public_ip>
- Add SIP Extension for endpoints (RFC2833 DTMF, NAT as required).
- Trunks (IP-based):
  - Outgoing SIP Settings:
    - Host: sip.telnyx.com
    - Type: peer
    - Qualify: Yes
    - Disallow: all; Allow: ulaw, alaw
  - Inbound SIP Settings:
    - Host: sip.telnyx.com
    - Type: friend
    - Insecure: port,invite
    - Disallow: all; Allow: ulaw
    - DTMFmode: RFC 2833
    - NAT: force_rport,comedia
    - Registration string: leave blank (IP trunk)
  - Dialed number manipulation (example): prepend 1 for NXXNXXXXXX; also 1NXXNXXXXXX.

## Elastix 4 – Credentials trunk

- Same NAT prep as above.
- Trunks (registration-based):
  - Outgoing SIP Settings:
    - Username/Secret: your Telnyx credentials
    - Host: sip.telnyx.com
    - Type: friend; Insecure: port,invite; Qualify: Yes
    - Disallow: all; Allow: ulaw, alaw
  - Inbound SIP Settings:
    - Username/Secret: your Telnyx credentials
    - Fromdomain/Host: sip.telnyx.com
    - Type: friend; Insecure: port,invite; Qualify: Yes
    - Disallow: all; Allow: ulaw; DTMFmode: RFC 2833; NAT: force_rport,comedia
    - Registration string: username:password@sip.telnyx.com
  - Dialed number manipulation (example): as above.

## Elastix 5 – FQDN/IP-based trunk

Initial setup (3CX-powered) highlights
- Confirm SIP Port 5060 (Settings > Network > Ports).
- Ensure Public IP/FQDN is correct; port forward as needed; match Telnyx connection IP/FQDN.

Create SIP Trunk (IP-based)
- SIP Trunks > +Add SIP Trunk:
  - Country: Worldwide; Provider: Telnyx LLC; Main Trunk No: your DID
- General > Trunk Details:
  - Name: Telnyx LLC
  - Registrar/Server: sip-anycast1.telnyx.com:5060 or sip.telnyx.com:5060
  - Outbound Proxy: sip.telnyx.com
- Authentication: Type = Do not require – IP Based
- Route calls to: set office/out-of-office destinations as needed
- Options: Require registration = Do not require; remove GSM-FR from Assigned Codecs
- Outbound Parameters: Contact User Part = Custom Field (leave blank)

## Elastix 5 – Credentials trunk

As above, except:
- Authentication: Register/Account based
- Authentication ID/Password: your Telnyx credentials

## FreeSWITCH – IP trunk

Harden defaults
- Change default password in conf/vars.xml (default_password).

External SIP profile
- In conf/sip_profiles/external.xml, ensure:
```
<param name="ext-rtp-ip" value="$${external_rtp_ip}"/>
<param name="ext-sip-ip" value="$${external_sip_ip}"/>
```

Gateway to Telnyx (no registration)
- File: conf/sip_profiles/external/telnyx.xml
```
<include>
  <gateway name="telnyx">
    <param name="proxy" value="sip.telnyx.com"/>
    <param name="register" value="false"/>
    <param name="caller-id-in-from" value="true"/>
    <param name="username" value="not-used"/>
    <param name="password" value="not-used"/>
  </gateway>
</include>
```

Sample dialplan (conf/dialplan/public/*.xml)
```
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(1{0,1}\d{10})$">
      <action application="set" data="effective_caller_id_number=13125489677"/>
      <action application="bridge" data="sofia/gateway/telnyx/$1"/>
    </condition>
  </extension>
  <extension name="local.com">
    <condition field="destination_number" expression="^(\d{7})$">
      <action application="bridge" data="sofia/gateway/telnyx/+1${default_areacode}$1"/>
    </condition>
  </extension>
</include>
```

NAT tips
- Use autonat to toggle local vs external IPs:
```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```
- If detection fails, hardcode your public IP in ext-rtp-ip and ext-sip-ip.
