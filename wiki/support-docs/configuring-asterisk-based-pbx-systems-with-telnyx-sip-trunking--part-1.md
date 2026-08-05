---
title: Configuring Asterisk-Based PBX Systems with Telnyx SIP Trunking
summary: This page consolidates Telnyx guidance for connecting Asterisk-based PBX
  platforms — including bare Asterisk, FreePBX, and VitalPBX — to Telnyx SIP Trunking
  using either IP authentication or credentials-based authentication. It covers Mission
  Control Portal prerequisites, trunk configuration, PJSIP transport settings, dialplan/routing
  setup, and notes on FIPS-aligned cryptography for SIP Trunking.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
updated_at: 2026-08-05T13:28:37Z
---

# Configuring Asterisk-Based PBX Systems with Telnyx SIP Trunking

*Part 1 of 5 — see also: [Part 2](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-2.md), [Part 3](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-3.md), [Part 4](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-4.md), [Part 5](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-5.md)*

This page consolidates Telnyx guidance for connecting Asterisk-based PBX platforms — including bare Asterisk, FreePBX, and VitalPBX — to Telnyx SIP Trunking using either IP authentication or credentials-based authentication. It covers Mission Control Portal prerequisites, trunk configuration, PJSIP transport settings, dialplan/routing setup, and notes on FIPS-aligned cryptography for SIP Trunking.

## Overview

[Asterisk](https://www.asterisk.org/) is an open source framework for building communications applications. It turns an ordinary computer into a communications server and powers IP PBX systems, VoIP gateways, conference servers, and other custom solutions. It is used by small and large businesses, call centers, carriers, and government agencies worldwide.

There are two standard methods to connect an Asterisk box to Telnyx:

- **Asterisk (SIP)** — uses the standard Session Initiation Protocol used to connect to SIP phones.
- **Asterisk (PJSIP)** — uses the Open Source Embedded SIP protocol stack.

> **Note:** Telnyx does not support IAX2 connections.

For more Asterisk documentation, see:

- [http://www.asteriskdocs.org](http://www.asteriskdocs.org/) — a free HTML book (the corresponding printed book is published conventionally by O'Reilly).
- [http://www.asterisk.org](https://www.asterisk.org/) — Asterisk's home site, operated by [Digium.com](https://www.sangoma.com/?source=digium_redirects_093021).

This page also covers FreePBX (a web-based GUI that manages Asterisk) and VitalPBX (a Unified Communications PBX system based on Asterisk, developed by Telesoft S.A.).

## Prerequisites

Before configuring any of the platforms below:

- [Download](http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz) and [install](https://docs.asterisk.org/) Asterisk version 18 (for bare Asterisk).
- Create a connection on the Telnyx Mission Control Portal — either an [IP authentication based connection](https://portal.telnyx.com/#/app/connections) or a [Credentials-based connection](https://portal.telnyx.com/#/app/connections).
- [Assign the connection to a DID](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection) and an outbound profile so you can make and receive calls.
- For FreePBX V15: [download](https://www.freepbx.org/downloads/) and [install](https://sangomakb.atlassian.net/wiki/spaces/PP/pages/10682958) FreePBX V15, and complete the [initial Telnyx Mission Control Portal setup](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- For VitalPBX: [download](https://vitalpbx.com/pbx-system-download/) and [install](https://wiki.vitalpbx.com/wiki/installation/system-specifications/) VitalPBX, and complete [initial configurations](https://wiki.vitalpbx.com/documentation/vitalpbx-manual/initial-configurations/) such as security settings.

> **Recommendation:** Use PJSIP rather than Chan_SIP. Chan_SIP is outdated, and the majority of users are moving to PJSIP, which provides more future-proof options and is still actively being improved by the community. See [PJSIP](https://www.pjsip.org/about.htm) for more information.

## Configuring the Telnyx Mission Control Portal

For step-by-step instructions on each of the requirements on the Telnyx Mission Control Portal, follow the [Get started with a Mission Control account](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) guide.

## Asterisk: IP Authentication Trunk

Open `/etc/asterisk/pjsip_wizard.conf` with your preferred editor and add the following:

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

> **Note:** For this configuration to work, the module `res_pjsp_config_wizard.so` must be installed and loaded. This is available through Asterisk 13.2.0.

## Asterisk: Credentials-Based Trunk

Open `/etc/asterisk/pjsip_wizard.conf` and add the following, replacing `username` and `password` with your Telnyx SIP connection credentials:

```
[trunk_defaults]
type = wizard

[telnyx] endpoint/transport = 0.0.0.0-udp
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

> **Note:** For this configuration to work, the module `res_pjsp_config_wizard.so` must be installed and loaded. This is available through Asterisk 13.2.0.

## Asterisk: Extensions for Making and Accepting Calls

Modify `/etc/asterisk/pjsip_wizard.conf` to add global configurations for extensions and specific ones for the sample. In this example, extension `1001` is set up to make and accept calls. Parameters that reference `1001` and `password` can be customized for your requirements.

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

## Asterisk: Basic PJSIP Configuration

Even though `pjsip_wizard.conf` is a great facilitator in setting up PJSIP endpoints, global configurations or anything else that might be needed can still be added in `/etc/asterisk/pjsip.conf`. For installations behind NAT, add the following to `pjsip.conf`:

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

- If the PBX is not in a NATed network, you can safely remove the parameters `external_media_address` and `external_signaling_address`.
- With the above configurations added to the respective files, your PBX should now be registered to Telnyx, and the extension `1001` in your IP phone/softphone should be registered to your PBX.
