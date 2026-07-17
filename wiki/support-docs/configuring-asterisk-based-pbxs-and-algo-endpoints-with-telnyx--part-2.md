---
title: Configuring Asterisk-Based PBXs and Algo Endpoints with Telnyx
summary: This page describes how to connect Asterisk-based PBX platforms and SIP endpoints
  to Telnyx as a SIP provider. It covers raw Asterisk (both IP-authentication and
  credentials-based trunks), FreePBX V15, VitalPBX (credentials and IP authentication),
  and Algo 8xxx series SIP endpoints, including installation, trunk configuration,
  dialplan setup, codec selection, optional TLS/SRTP encryption, and basic troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
updated_at: 2026-07-17T09:04:09Z
---

# Configuring Asterisk-Based PBXs and Algo Endpoints with Telnyx

*Part 2 of 5 — see also: [Part 1](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-1.md), [Part 3](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-3.md), [Part 4](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-4.md), [Part 5](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-5.md)*

This page describes how to connect Asterisk-based PBX platforms and SIP endpoints to Telnyx as a SIP provider. It covers raw Asterisk (both IP-authentication and credentials-based trunks), FreePBX V15, VitalPBX (credentials and IP authentication), and Algo 8xxx series SIP endpoints, including installation, trunk configuration, dialplan setup, codec selection, optional TLS/SRTP encryption, and basic troubleshooting.

## Asterisk Credentials Trunk

This section walks through configuring an Asterisk PBX with Telnyx using credentials-based authentication (username/password).

**Pre-requisites:**

- [Download](http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz) and [install](https://docs.asterisk.org/Getting-Started/Installing-Asterisk/Installing-Asterisk-From-Source/What-to-Download/) Asterisk version 18.
- Create a [Credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, [assign this connection to a DID](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection) and outbound profile in order to make and receive calls.

### Configure the Telnyx Mission Control Portal

For step-by-step instructions on each of the requirements on the Telnyx Mission Control Portal, follow the [Get Started with a Mission Control Account](get-started-with-a-mission-control-account.md) guide.

### Configure the Asterisk SIP Trunk

Open `/etc/asterisk/pjsip_wizard.conf` with your preferred editor and edit the following rows:

```
[trunk_defaults]
type = wizard

[telnyx]
endpoint/transport = 0.0.0.0-udp
endpoint/allow = !all,ulaw,alaw,G729,G722
endpoint/rewrite_contact = yes
endpoint/dtmf_mode = rfc4733 ; Most PBXs will also support 2833.
endpoint/context = from-pstn
endpoint/force_rport = yes
aor/qualify_frequency = 60
sends_auth = yes
sends_registrations = yes
remote_hosts = sip.telnyx.com:5060
outbound_auth/username = username
outbound_auth/password = password
registration/expiration = 600
```

> **Note:** For this configuration to work, the module `res_pjsip_config_wizard.so` must be installed and loaded. This is available through Asterisk 13.2.0.

### Configure Asterisk to Make and Accept Calls

Modify extension `1001` in `/etc/asterisk/pjsip_wizard.conf` to add the global configurations for the extensions and specific ones for the sample. Parameters that reference `1001` and `password` can be customized for your requirements:

```
[user_defaults](!)
type = wizard
accepts_registrations = yes
sends_registrations = no
accepts_auth = yes
sends_auth = no
endpoint/context = from-internal
endpoint/allow = !all,ulaw,alaw,G729,G722
endpoint/force_rport = yes
endpoint/dtmf_mode = rfc4733
endpoint/rewrite_contact = yes
aor/max_contacts = 1
aor/remove_existing = yes
aor/minimum_expiration = 30
```

After creating the template, setting up a new phone is often as simple as setting up a username/password, as the Phone object inherits from the Wizard template. You won't even need to specify a type:

```
[Bart](user_defaults)
hint_exten = 1001
endpoint/callerid = Bart <1001>
inbound_auth/username = Bart
inbound_auth/password = strong@pass123$
```

```
[Lisa](user_defaults)
hint_exten = 1001
endpoint/callerid = Lisa <1001>
endpoint/allow = !all,ulaw
inbound_auth/username = Lisa
inbound_auth/password = strong@pass246$
has_phoneprov = yes ; defaults to no
phoneprov/MAC = hereweGOaga1n ;must specify if has_phoneprov=yes
phoneprov/PROFILE = profile1 ;must specify if has_phoneprov=yes
```

### Complete the Basic PJSIP Configuration

Edit the following lines in `/etc/asterisk/pjsip.conf` for installations behind NAT:

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

- If the PBX is not in a NATed network, you can safely remove the following parameters: `external_media_address` and `external_signaling_address`.
- With the above configurations added to the respective files, your PBX should now be registered to Telnyx, and the extension `1001` in your IP phone/softphone should be registered to your PBX.

### Set Up the Dialplan

Open `extensions.conf` and add the following:

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

- `[from-pstn]` is the context that captures inbound calls to the PBX coming from Telnyx and sends them to extension `1001`. The block will capture every call towards CLDs in US national (10 digit) or +E164 and send it to extension `1001`.
- `[from-internal]` serves to route calls towards the world through Telnyx. The block will capture calls towards US national numbers, convert to +E164 or towards any other number, prepend "+", and send the call to Telnyx.
