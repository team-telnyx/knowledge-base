---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring SIP trunks between Telnyx and various
  open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and
  FusionPBX — using either IP-based or credentials-based authentication.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
updated_at: 2026-06-11T11:25:51Z
---

# PBX SIP Trunk Configuration with Telnyx

*Part 1 of 3 — see also: [Part 2](pbx-sip-trunk-configuration-with-telnyx-2--part-2.md), [Part 3](pbx-sip-trunk-configuration-with-telnyx-2--part-3.md)*

Comprehensive guide for configuring SIP trunks between Telnyx and various open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and FusionPBX — using either IP-based or credentials-based authentication.

Telnyx supports SIP trunking connections from a wide range of open-source PBX and dialer platforms. Two authentication methods are available: **IP-based authentication**, where your server's IP address authorizes traffic, and **Credentials-based authentication**, where a username/password pair registers against Telnyx's SIP proxy. Telnyx does not support IAX2 connections.

## Telnyx Mission Control Portal Setup

Before configuring any PBX, you must prepare your Telnyx account. The steps are consistent regardless of which PBX or authentication method you use.

### Purchase a Number

1. Navigate to **Numbers → Search Numbers**.
2. Choose a search type (NPA-NXX, Region, Toll Free, or Advanced).
3. Enter your criteria and click **Search**.
4. Click **+ Add to Cart** for the desired number(s).
5. Open the **Shopping Cart** and check out.
6. Purchased numbers appear on the **My Numbers** tab.

### Create a Connection

1. Navigate to **Connections** and click **Add Connection**.
2. Enter a name for the connection.
3. Choose an authentication method:
   - **IP Address** — enter your PBX's public IP (used for IP-based trunks).
   - **Credentials** — enter the desired username/password combination (used for credentials-based trunks).
4. Click **Create**.

### Assign a Number to the Connection

1. Go to **Numbers → My Numbers**.
2. Use the **Select Connection** dropdown next to your number and choose the connection you just created.

### Create an Outbound Profile

1. Navigate to **Outbound** and click **+ Add Outbound Profile**.
2. Select the connection you created from the dropdown.
3. Choose the **Traffic Type** and **Service Plan** that suit your needs.
4. Click **Add**.

For full portal setup details, refer to the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).

## Asterisk

Asterisk is an open-source communications framework that powers IP PBX systems, VoIP gateways, and conference servers. It connects to Telnyx using the PJSIP stack (via `res_pjsip_config_wizard.so`, available from Asterisk 13.20 onwards). Asterisk 18 is recommended.

### IP-Based Trunk

Edit `/etc/asterisk/pjsip_wizard.conf` and add the following trunk configuration:

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

### Credentials-Based Trunk

Edit `/etc/asterisk/pjsip_wizard.conf` with the following trunk configuration:

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
outbound_auth/username = username
outbound_auth/password = password
registration/expiration = 600
```

Replace `username` and `password` with the credentials you created in the Telnyx portal.

### Extension Configuration

Add a user template and individual extensions to `/etc/asterisk/pjsip_wizard.conf`:

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
```

Once the template is in place, adding new phones is simply a matter of specifying a username and password — the `type` line is not required because the object inherits from the wizard template.

### NAT Transport Configuration

For installations behind NAT, add the following to `/etc/asterisk/pjsip.conf`:

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

Replace `X.X.X.X` with your actual network and public IP addresses. If the PBX is not behind NAT, remove the `external_media_address` and `external_signaling_address` parameters.

### Dialplan

Edit `/etc/asterisk/extensions.conf`:

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

- `[from-pstn]` captures inbound calls from Telnyx and routes them to extension 1001 (matching US national 10-digit or +E.164 formats).
- `[from-internal]` routes outbound calls through Telnyx, converting US national numbers to +E.164 or prepending "+" for international numbers.

**Important:** If your IP-based connection uses a tech prefix to authenticate, it must be reflected in the dialplan. For example, with tech prefix `9999`:

```
[from-internal]
exten = _NXXNXXXXXX,1,Dial(PJSIP/9999+1${EXTEN}@telnyx)
same = n,Hangup()
exten = _X.,1,Dial(PJSIP/9999+${EXTEN}@telnyx)
same = n,Hangup()
```

## Vicidial

Vicidial is an enterprise-class open-source contact center suite. It connects to Telnyx via a SIP peer or friend configuration in its carrier management interface.

### IP-Based Trunk

In the Vicidial web portal, go to **Admin → Carriers → Add new carrier** and enter:

| Field | Value |
|---|---|
| Carrier ID | TelnyxCarrier |
| Name | telnyxRegistration |
| String | *(leave blank)* |
| Template ID | NONE |
| Account Entry | [telnyx] |
| Disallow | All |
| Allow | ulaw, g729 |
| Type | peer |
| Insecure | port,invite |
| Host | sip.telnyx.com |
| DTMF Mode | rfc2833 |
| Context | default |
| Protocol | SIP |
| Global String | Telnyx=SIP/telnyx |

**Dial Plan:**

```
exten => _91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _91NXXNXXXXXX,3,Hangup
```

In this dialplan, `9` is the prefix dialed to send calls to the Telnyx trunk.

### Credentials-Based Trunk

The configuration is similar to the IP-based trunk, with the following differences:

| Field | Value |
|---|---|
| Type | friend |
| Host | sip.telnyx.com |
| Username | *(your Telnyx portal username)* |
| Password | *(your Telnyx portal password)* |

The `Insecure` field is not used with credentials-based trunks. The dial plan remains the same as the IP-based configuration.

### Outbound Caller ID

You can configure outbound caller ID per user or per campaign to comply with Telnyx's [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).

**Per user:** Go to **Users → Modify** the user, set the **Outbound CallerID** field, and click **Submit**.

**Per campaign:** Go to **Campaigns → Modify** the campaign, click the **Detail** tab, set the **Campaign CallerID** field, and click **Submit**.
