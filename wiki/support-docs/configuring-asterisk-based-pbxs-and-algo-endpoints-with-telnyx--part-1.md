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

*Part 1 of 5 — see also: [Part 2](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-2.md), [Part 3](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-3.md), [Part 4](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-4.md), [Part 5](configuring-asterisk-based-pbxs-and-algo-endpoints-with-telnyx--part-5.md)*

This page describes how to connect Asterisk-based PBX platforms and SIP endpoints to Telnyx as a SIP provider. It covers raw Asterisk (both IP-authentication and credentials-based trunks), FreePBX V15, VitalPBX (credentials and IP authentication), and Algo 8xxx series SIP endpoints, including installation, trunk configuration, dialplan setup, codec selection, optional TLS/SRTP encryption, and basic troubleshooting.

## Overview

This page covers how to connect several Asterisk-based PBX platforms and SIP endpoints to Telnyx as a SIP provider. The platforms covered include raw Asterisk (both IP-authentication and credentials-based trunks), FreePBX V15, and VitalPBX, as well as Algo 8xxx series SIP endpoints.

[Asterisk](https://www.asterisk.org/) is an open source framework for building communications applications. It turns an ordinary computer into a communications server and powers IP PBX systems, VoIP gateways, conference servers, and other custom solutions. It is used by small businesses, large businesses, call centers, carriers, and government agencies worldwide.

There are two standard methods to connect an Asterisk box to Telnyx:

- **Asterisk (SIP)** — uses the standard Session Initiation Protocol used to connect to SIP phones.
- **Asterisk (PJSIP)** — uses the Open Source Embedded SIP protocol stack.

> **Note:** Telnyx does not support IAX2 connections.

For more Asterisk documentation, see:

- [asteriskdocs.org](http://www.asteriskdocs.org/) — a free HTML book (the corresponding printed book is published conventionally by O'Reilly).
- [asterisk.org](https://www.asterisk.org/) — Asterisk's home site, operated by [Sangoma](https://www.sangoma.com/?source=digium_redirects_093021).

## Asterisk IP Trunk (IP Authentication)

This section walks through configuring an Asterisk PBX IP trunk with Telnyx using IP-based authentication.

**Pre-requisites:**

- [Download](http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz) and [install](https://docs.asterisk.org/) Asterisk version 18.
- Create an [IP authentication based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, [assign this connection to a DID](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection) and outbound profile in order to make and receive calls.

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
endpoint/dtmf_mode = rfc4733
endpoint/context = from-pstn
endpoint/force_rport = yes
aor/qualify_frequency = 60
sends_auth = no
sends_registrations = no
remote_hosts = sip.telnyx.com:5060
```

> **Note:** For this configuration to work, the module `res_pjsip_config_wizard.so` must be installed and loaded. This is available through Asterisk 13.2.0.

### Configure Asterisk to Make and Accept Calls

Modify `/etc/asterisk/pjsip_wizard.conf` to add the global configurations for the extensions and specific ones for the sample. In this example, extension `1001` is set up to make and accept calls. Parameters that reference `1001` and `password` can be customized for your requirements:

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

1001
endpoint/callerid = Bart <1001>
inbound_auth/username = Bart
inbound_auth/password = strong@pass123$
```

After creating the template, setting up a new phone is often as simple as setting up a username/password, as the Phone object inherits from the Wizard template. You won't even need to specify a type:

```
[Bart](user_defaults)
hint_exten = 1001
endpoint/callerid = Bart <1001>
inbound_auth/username = Bart
inbound_auth/password = strong@pass135$
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

Even though `pjsip_wizard.conf` is a great facilitator in setting up PJSIP endpoints, global configurations, or anything else that might be needed can still be added in `/etc/asterisk/pjsip.conf`. For installations behind NAT, add the following lines to `pjsip.conf`:

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

Asterisk uses dialplans saved in `/etc/asterisk/extensions.conf` to route calls between endpoints. To allow extension `1001` to call the world through Telnyx, as well as to send it any calls that arrive to the Telnyx DID assigned to the respective trunk, open `extensions.conf` and add the following:

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

> **IMPORTANT:** If your IP-based connection uses a tech prefix to authenticate, this must be reflected in the dialplan. For example, if you have set the tech prefix `9999` in Telnyx, your `[from-internal]` block should look like this:
>
> ```
> [from-internal]
> exten = _NXXNXXXXXX,1,Dial(PJSIP/9999+1${EXTEN}@telnyx)
> same = n,Hangup()
> exten = _X.,1,Dial(PJSIP/9999+${EXTEN}@telnyx)
> same = n,Hangup()
> ```
