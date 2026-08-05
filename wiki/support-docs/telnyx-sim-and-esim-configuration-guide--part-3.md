---
title: Telnyx SIM and eSIM Configuration Guide
summary: This page consolidates Telnyx guidance on SIM and eSIM provisioning, activation,
  and security. It covers manual eSIM activation, QR-code eSIM setup, SIM theft prevention
  via IMEI authorization, manual IMSI selection for engineering troubleshooting, and
  the underlying VoIP/SIP/SDP/codec concepts that govern how Telnyx SIM-backed devices
  interoperate with the network.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-08-05T13:24:33Z
---

# Telnyx SIM and eSIM Configuration Guide

*Part 3 of 4 — see also: [Part 1](telnyx-sim-and-esim-configuration-guide--part-1.md), [Part 2](telnyx-sim-and-esim-configuration-guide--part-2.md), [Part 4](telnyx-sim-and-esim-configuration-guide--part-4.md)*

This page consolidates Telnyx guidance on SIM and eSIM provisioning, activation, and security. It covers manual eSIM activation, QR-code eSIM setup, SIM theft prevention via IMEI authorization, manual IMSI selection for engineering troubleshooting, and the underlying VoIP/SIP/SDP/codec concepts that govern how Telnyx SIM-backed devices interoperate with the network.

## SBC Configuration with Telnyx

Telnyx SIP trunks can be terminated on a variety of Session Border Controllers (SBCs). Two common options are the Oracle Acme Packet SBC and the Sansay VSXi.

### Oracle Acme Packet SBC

The [Acme Packet platforms](https://www.oracle.com/industries/communications/acme-packet-platforms/) are designed to help customers deliver trusted, real-time communications across IP network borders based on different needs for performance and capacity. See the [Acme SBC user guide](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-3D090BC0-31D0-419D-A1F9-E7B1E5D3D55D.htm) for additional reference.

**Pre-requisites:**
- Ensure your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers).
- [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections).
- [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (assign it to a SIP connection).
- [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound).
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
- Have the SBC set up with your IP-PBX, with one or more clients configured and running calls between them.

#### 1. Configure the SIP trunk

In superuser mode:

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# sip-interface
ORACLE(sip-interface)#
```

Use the following configuration parameters as a guide:

```
sip-interface
state                enabled
realm-id             OUTSIDE
description
sip-port
address              X.X.X.X
port                 5060
transport-protocol   UDP
tls-profile
allow-anonymous      agents-only
ims-aka-profile
carriers
trans-expire         0
...
```

Key parameters:

- **state** — Enable or disable the SIP interface. Default: `enabled`. Values: `enabled | disabled`.
- **realm-id** — Name of the realm to which the SIP interface is connected.
- **sip-ports** — Access the `sip-ports` subelement.
- **address** — IP address of the host associated with the sip-port entry on which to listen (e.g. `192.168.11.101`).
- **port** — Port number for this sip-port. Default: `5060`. Range: 1025–65535.
- **transport-protocol** — Transport protocol for the SIP port. Default: `UDP`. Values: `TCP`, `UDP`, `TLS`.
- **allow-anonymous** — Criteria for accepting and processing SIP requests from another SIP element. Default: `all`. Values: `all`, `agents-only`, `realm-prefix`, `registered`, `register-prefix`.
- **carriers** — List of carriers related to the SIP interface (1–24 characters).
- **trans-expire** — TTL expiration timer in seconds for SIP transactions (controls Timers B, F, H, and TEE from RFC 3261). Default: `0`. Range: 0–999999999.

#### 2. Configure the session agent towards Telnyx

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# session-agent
ORACLE(sip-interface)#
```

Use the following configuration parameters as a guide:

```
session-agent
hostname              sip.telnyx.com
ip-address
port                  5060
state enabled
app-protocol          SIP
app-type
transport-method      UDP
realm-id              OUTSIDE
egress-realm-id
description           Telnyx
carriers
allow-next-hop-lp     enabled
constraints           disabled
...
```

Key parameters:

- **hostname** — Hostname, FQDN, or IP address of the session agent. Must be unique. If the initial DNS query fails, the session agent is put out-of-service and the query is repeated on ping.
- **ip-address** — Optional. IP address for the FQDN hostname; leave blank to allow DNS resolution.
- **port** — Port associated with the session agent. `0` means the SBC will not initiate communication (but will accept calls). Range: 1025–65535. Default: `5060`.
- **state** — Enable or disable the session agent. Default: `enabled`.
- **app-protocol** — Protocol for sending messages. Default: `SIP`. Values: `SIP | H.323`.
- **app-type** — For H.323, indicates gateway (`H.323-GW`) or gatekeeper (`H.323-GK`).
- **transport-method** — IP protocol for communication with the session agent. Default: `UDP`. Values: `UDP`, `UDP+TCP`, `DynamicTCP`, `StaticTCP`, `DynamicTLS`, `StaticTLS`.
- **realm-id** — ID of the realm in which the session agent resides. Identifies the ingress realm for requests from this agent and the egress realm for requests sent to it.
- **description** — Optional descriptive name.
- **carriers** — Optional list to restrict carriers used for sessions originating from this session agent.
- **allow-next-hop-lp** — Whether this session agent can be used as a next hop in the local policy. Default: `enabled`.
- **constraints** — Whether individual constraints configured in the next step are applied to sessions sent to the session agent. Default: `disabled`.

#### 3. Configure number translation

E.164 Number Mapping (ENUM) translates standard telephone numbers to an Internet-friendly form. The example below appends `+1` to US calling numbers. This is the session translation rule on the calling number.

> Telnyx accepts the called number on outbound calls in 10-digit, 11-digit, and +11-digit format, so there is no need to modify rules for the called number. However, Telnyx has a [caller ID policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) and requires the calling number to be in +E.164 format.

```
ORACLE(configure)# session-router
ORACLE(session-router)# session-translation
ORACLE(session-translation)#
```

```
session-translation
id                    includeCallingPlus
rules-calling         includePlus
rules-called
```

- **ID** — Descriptive name for this session translation.
- **rules-calling** — Rules applied to the calling number, in order. Multiple rules should be quoted and space-separated.
- **rules-called** — Rules applied to the called number, in order.

Then define the translation rule to append `+1` to the calling number:

```
ORACLE(session-router)# translation-rules
ORACLE(session-translation)#
```

```
translation-rules
id                    includePlus
type                  add
add-string            +1
add-index             0
delete-string
delete-index          0
```

- **ID** — Descriptive ID for this translation rule.
- **type** — Type of translation rule. Default: `none`. Values: `add`, `delete`, `replace`, `none`.
- **add-string** — String to be added during address translation. Should always be a real value (no `@` or `$`).
- **add-index** — Position (0 = leftmost) where the string is added. Default: `0`. Range: 0–999999999.
- **delete-string** — String to be deleted from the original address. Unspecified characters are denoted by `@`. Only works when `type` is `delete`.
- **delete-index** — Position (0 = leftmost) where the string is deleted. Default: `0`. Range: 0–999999999.

Apply the translation rule to the outside realm:

```
realm-config
identifier            OUTSIDE
...
in-translationid
out-translationid     includeCallingPlus
...
```

#### 4. Configure codecs

In the Acme SBC, set your [codec policy](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-49ECD7A3-8663-44ED-ADD4-EB01B76CC527.htm#GUID-9CEACADB-5A28-4367-9B7B-813C75F11289) as desired. See the list of supported codecs on the [Telnyx codecs page](https://sip.telnyx.com/#codecs).

The example below changes the codec list for all clients making outbound calls through the SBC's realm so that PCMU is the preferred codec offered:

```
realm-config
identifier             clients
...
options                preferred-codec=PCMU
...
```

### Sansay VSXi

The [Sansay VSXi session controller](https://www.sansay.com/products/vsxi/) is a high-performance software-based SBC that provides security and DDoS protection, network address translation, protocol interworking, and traffic management. It selects optimal routes for voice traffic and provides packet-header manipulation and digit mapping for ANI and DNIS services.

Additional resources:
- [VSXi datasheet](https://www.sansay.com/wp-content/uploads/2013/05/Sansay_VSXi_Session-Controller_9_2013.pdf) (PDF)
- [Contact Sansay](https://www.sansay.com/contact-us/)
- [VSXi REST API](https://support.sansay.com/t/36d6tz/vsxi-rest-api)
- [VSXi knowledgebase](https://www.sinsay.com/sq/en/faq)

**Pre-requisites:**
- Ensure your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
- Set up your Sansay SBC with your IP-PBX and have one or more clients configured and running calls between them.

#### 1. Create resources

1. Log into your Sansay portal and select **Resources** from the navigation.
2. Create two new resources — one for your inbound trunk and one for your outbound trunk.

#### 2. Define resource settings for your inbound trunk

Configure the SIP server information for the inbound trunk with the following settings:

- **Resource Type:** *Inbound*
- **Resource Type:** *Peering*
- **Protocol:** *SIP*
- **SIP Profile:** *SIP_Peering:0*

**General Info:**

- **SIP Trunk ID:** *1000*
- **Trunk name:** *Telnyx Inbound*
- **Company Name:** *Telnyx*
- **Route Table:** *0*
- **Remote Port:** *5060*
- **Service Port:** *SIP Public Default 1:1*
- **Aggregate Capacity:** *1200*
- **Average CPS Limit:** *500*
- **Authorized RPS:** *500*
- **Unauthorized RPS:** *500*
- **Group Policy:** *Round Robin*
- **Digit Mapping Table:** *no-translation:0*
- **Min Call Duration:** *0*
- **Max Call Duration:** *43200*
- **RTP TOS:** *B8*
- **Direction:** *Both*
- **Service State:** *inservice*
- **Allow Direct Media:** *No*
- **No Answer Timeout:** *120*
- **No Ring Timeout:** *30*
- **Option Poll:** *Disable*
- **Cause Code Profile:** *Default:0*
- **Stop Route Profile:** *Default:0*
- **PAI:** *Disable*

**Digit Translation & RN Handling:**

- **Ingress & Egress:** *all*
- **Outbound ANI:** *pass*
- **Tech Prefix:** *default*

**Codec Info:**

- **Policy:** *enforced*
- **Codec 1:** *g711u64k*
- **Codecs 2–8:** *None*

**Fqdns Info:**

Depending on which Telnyx SIP proxies and media servers you interact with, review the [signalling IP addresses](https://sip.telnyx.com/#signaling-addresses) and [media IP addresses](https://sip.telnyx.com/#media).

![SIP signaling addresses for outbound calls.](_images/ac264450a060b368.png)

![Media IPs section of the Media tab.](_images/b06fb6edf5f851a4.png)

Click **Save as** and then **Submit**.

#### 3. Define resource settings for your outbound trunk

Configure the outbound trunk with the following settings:

- **Resource Type:** *Outbound*
- **Resource Type:** *Peering*
- **Protocol:** *SIP*
- **SIP Profile:** *SIP_Peering:0*

**General Info:**

- **SIP Trunk ID:** *1001*
- **Trunk name:** *Telnyx Outbound*
- **Company Name:** *Telnyx*
- **Route Table:** *0*
- **Remote Port:** *5060*
- **Service Port:** *SIP Public Default 1:1*
- **Aggregate Capacity:** *1200*
- **Average CPS Limit:** *500*
- **Authorized RPS:** *500*
- **Unauthorized RPS:** *500*
- **Group Policy:** *Round Robin*
- **Digit Mapping Table:** *no-translation:0*
- **Min Call Duration:** *0*
- **Max Call Duration:** *43200*
- **RTP TOS:** *B8*
- **Direction:** *Both*
- **Service State:** *inservice*
- **Allow Direct Media:** *No*
- **No Answer Timeout:** *120*
- **No Ring Timeout:** *30*
- **Option Poll:** *Disable*
- **Cause Code Profile:** *Default:0*
- **Stop Route Profile:** *Default:0*
- **PAI:** *Disable*

**Digit Translation & RN Handling:**

- **Ingress & Egress:** *all*
- **Outbound ANI:** *pass*
- **Tech Prefix:** *default*

**Codec Info:**

- **Policy:** *enforced*
- **Codec 1:** *g711u64k*
- **Codecs 2–8:** *None*

**Fqdns Info:**

Review the [signalling IP addresses](https://sip.telnyx.com/#signaling-addresses) and [media IP addresses](https://sip.telnyx.com/#media) for your location.

![Signaling addresses for outbound calls.](_images/ac264450a060b368.png)

![Media IPs for subnets.](_images/b06fb6edf5f851a4.png)

Click **Save as & Submit** to push the configuration to Sansay.
