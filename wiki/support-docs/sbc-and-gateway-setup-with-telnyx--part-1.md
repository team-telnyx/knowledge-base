---
title: SBC and Gateway Setup with Telnyx
summary: Consolidated setup guides for configuring Oracle Acme Packet, Audiocodes,
  Ribbon EdgeMarc 6000, Sansay VSXi, and Mediatrix C7/4100 SBCs and gateways with
  the Telnyx Mission Control Portal, including SIP trunk, session agent, codec, and
  telephony port configuration.
sources:
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
updated_at: 2026-07-17T09:10:12Z
---

# SBC and Gateway Setup with Telnyx

*Part 1 of 3 — see also: [Part 2](sbc-and-gateway-setup-with-telnyx--part-2.md), [Part 3](sbc-and-gateway-setup-with-telnyx--part-3.md)*

Consolidated setup guides for configuring Oracle Acme Packet, Audiocodes, Ribbon EdgeMarc 6000, Sansay VSXi, and Mediatrix C7/4100 SBCs and gateways with the Telnyx Mission Control Portal, including SIP trunk, session agent, codec, and telephony port configuration.

## SBC and Gateway Setup with Telnyx

This page consolidates setup guides for several Session Border Controllers (SBCs) and VoIP gateways commonly deployed with the Telnyx Mission Control Portal. Each section walks through the prerequisites, configuration steps, and additional resources for a specific device family.

### Common Prerequisites

Before configuring any of the devices below, ensure the following Telnyx-side items are in place:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is configured.
- You have purchased a DID and provisioned it to a SIP connection.
- You have set up a Telnyx SIP connection and created an outbound voice profile.
- (Recommended) TLS is enabled to encrypt your traffic.
- The SBC or gateway is already set up with your IP-PBX, with one or more clients configured and running calls between them.

---

## Oracle: Acme Packet SBC Setup

Oracle's [Acme Packet platforms](https://www.oracle.com/industries/communications/acme-packet-platforms/) deliver trusted, real-time communications across IP network borders for a range of performance and capacity needs. The configuration covers four areas: the SIP trunk, the session agent toward Telnyx, number translation, and codecs.

### 1. Configure the SIP Trunk

Enter configuration mode and define the SIP interface:

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# sip-interface
ORACLE(sip-interface)#
```

Reference parameters:

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

Key parameter notes:

- **state** — Enable or disable the SIP interface. Default: `enabled`.
- **realm-id** — Name of the realm to which the SIP interface is connected.
- **address** — IP address of the host associated with the sip-port entry (e.g., `192.168.11.101`).
- **port** — Port number for this sip-port. Default: `5060`. Range: 1025–65535.
- **transport-protocol** — `TCP`, `UDP`, or `TLS`.
- **allow-anonymous** — Controls which SIP elements may send requests. Options include `all`, `agents-only`, `realm-prefix`, `registered`, and `register-prefix`. With `agents-only`, requests from unconfigured agents are refused (TCP) or answered with `403 Forbidden` (UDP).
- **carriers** — Optional list of carriers related to the SIP interface (1–24 characters).
- **trans-expire** — TTL expiration timer in seconds for SIP transactions (Timer B, F, H, TEE). Default: `0` (uses global SIP config). Range: 0–999999999.

### 2. Configure the Session Agent Toward Telnyx

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# session-agent
ORACLE(sip-interface)#
```

Reference parameters:

```
session-agent
hostname              sip.telnyx.com
ip-address
port                  5060
state                 enabled
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

Key parameter notes:

- **hostname** — Hostname, FQDN, or IP address. Must be unique per session agent. If DNS resolution fails, the session agent is taken out of service until a ping succeeds.
- **ip-address** — Optional IP address for the FQDN; leave blank to allow DNS resolution.
- **port** — Port for the session agent. `0` means the SBC will not initiate communication (but will accept calls). Range: 1025–65535. Default: `5060`.
- **state** — `enabled` or `disabled`. Default: `enabled`.
- **app-protocol** — `SIP` or `H.323`. Default: `SIP`.
- **app-type** — For H.323, `H.323-GW` (gateway) or `H.323-GK` (gatekeeper).
- **transport-method** — `UDP`, `UDP+TCP`, `DynamicTCP`, `StaticTCP`, `DynamicTLS`, or `StaticTLS`. Default: `UDP`.
- **realm-id** — Realm in which the session agent resides. Must match the realm identifier configured elsewhere.
- **description** — Optional descriptive name.
- **carriers** — Optional carrier list to restrict sessions originating from this agent.
- **allow-next-hop-lp** — Whether this session agent can be used as a next hop in local policy. Default: `enabled`.
- **constraints** — Whether individual constraints are applied to sessions sent to this agent. Default: `disabled`.

### 3. Configure Number Translation

E.164 Number Mapping (ENUM) translates standard telephone numbers into an Internet-friendly form. The example below appends `+1` to US calling numbers. Telnyx accepts the called number in 10-digit, 11-digit, or +11-digit format, but the calling number must be in +E.164 format per the [caller ID policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).

Create the session translation:

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

- **id** — Descriptive name for the session translation.
- **rules-calling** — Rules applied to the calling number, in order.
- **rules-called** — Rules applied to the called number, in order.

Define the translation rule that prepends `+1`:

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

- **type** — `add`, `delete`, `replace`, or `none` (disabled). Default: `none`.
- **add-string** — String to add during translation. Must be a real value (no `@` or `$`).
- **add-index** — Position (0 = leftmost) where the string is added. Range: 0–999999999.
- **delete-string** — String to delete. `@` is a wildcard and only works when `type=delete`.
- **delete-index** — Position (0 = leftmost) where the string is deleted. Range: 0–999999999.

Apply the rule to the outside realm:

```
realm-config
identifier            OUTSIDE
...
in-translationid
out-translationid     includeCallingPlus
...
```

### 4. Configure Codecs

Codec policy can be set per Oracle's [codec policy documentation](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-49ECD7A3-8663-44ED-ADD4-EB01B76CC527.htm#GUID-9CEACADB-5A28-4367-9B7B-813C75F11289). See the [Telnyx supported codecs list](https://sip.telnyx.com/#codecs). The example below makes PCMU the preferred codec for outbound calls from the `clients` realm:

```
realm-config
identifier             clients
...
options                preferred-codec=PCMU
...
```

Additional resources: [Acme SBC user guide](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-3D090BC0-31D0-419D-A1F9-E7B1E5D3D55D.htm).

---
