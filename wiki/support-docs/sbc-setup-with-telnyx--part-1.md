---
title: SBC Setup with Telnyx
summary: Configuration guides for integrating Session Border Controllers with Telnyx
  SIP trunks, covering Oracle Acme Packet, AudioCodes, Ribbon EdgeMarc 6000, and Sansay
  VSXi platforms.
sources:
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
updated_at: 2026-06-11T11:43:59Z
---

# SBC Setup with Telnyx

*Part 1 of 2 — see also: [Part 2](sbc-setup-with-telnyx--part-2.md)*

Configuration guides for integrating Session Border Controllers with Telnyx SIP trunks, covering Oracle Acme Packet, AudioCodes, Ribbon EdgeMarc 6000, and Sansay VSXi platforms.

## Prerequisites

Before configuring any SBC with Telnyx, ensure the following:

- Your [Mission Control Portal](mission-control-portal.md) account is set up correctly
- You have purchased a DID and assigned it to a SIP connection
- You have created an outbound voice profile and (where applicable) an IP authentication connection
- Your SBC is already set up with your IP-PBX, with one or more clients configured and running calls between them
- **Recommended:** Enable TLS to encrypt your traffic

Telnyx accepts called numbers on outbound calls in 10-digit, 11-digit, and +11-digit format, so no modification rules are needed for the called number. However, Telnyx requires the calling number to be in +E.164 format per the [caller ID policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).

## Oracle Acme Packet SBC Configuration

The [Acme Packet platform family](https://www.oracle.com/industries/communications/acme-packet-platforms/) delivers trusted, real-time communications across IP network borders. Configuration is performed through the terminal in superuser mode.

### Configure the SIP Trunk Interface

1. Enter configuration mode:

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# sip-interface
```

2. Apply the following parameters:

```
sip-interface
  state                enabled
  realm-id             OUTSIDE
  sip-port
    address              X.X.X.X
    port                 5060
    transport-protocol   UDP
  allow-anonymous      agents-only
  carriers
  trans-expire         0
```

Key parameter details:

- **state** — `enabled` or `disabled` (default: `enabled`)
- **realm-id** — The realm to which the SIP interface is connected
- **address** — IP address of the host for the sip-port entry
- **port** — Port number (range 1025–65535, default `5060`)
- **transport-protocol** — `TCP`, `UDP`, or `TLS`
- **allow-anonymous** — Controls which SIP requests are accepted. `agents-only` allows only requests from configured session agents; other values include `all`, `realm-prefix`, `registered`, and `register-prefix`
- **trans-expire** — TTL expiration timer in seconds for SIP transactions (range 0–999999999, default `0` uses global SIP config)

### Configure the Session Agent Towards Telnyx

1. Enter configuration mode:

```
ORACLE# configure terminal
ORACLE(configure)# session-router
ORACLE(session-router)# session-agent
```

2. Apply the following parameters:

```
session-agent
  hostname              sip.telnyx.com
  port                  5060
  state                 enabled
  app-protocol          SIP
  transport-method      UDP
  realm-id              OUTSIDE
  description           Telnyx
  allow-next-hop-lp     enabled
  constraints           disabled
```

Key parameter details:

- **hostname** — Host name, FQDN, or IP address. Must be unique across session agents. If entered as FQDN, DNS resolves it; a failed DNS query puts the agent out-of-service until an address responds
- **port** — Port number (0 means the SBC will not initiate communication; range 1025–65535, default `5060`)
- **transport-method** — Options include `UDP`, `UDP+TCP`, `DynamicTCP`, `StaticTCP`, `DynamicTLS`, `StaticTLS`
- **realm-id** — Identifies the realm for sessions coming from or going to this session agent
- **allow-next-hop-lp** — Whether this agent can be used as a next hop in local policy (`enabled`/`disabled`)
- **constraints** — Whether individual constraints are applied to sessions sent to the agent (`enabled`/`disabled`)

### Configure Number Translation

To meet Telnyx's +E.164 caller ID requirement, configure a translation rule that prepends `+1` to the calling number.

1. Create a session translation:

```
ORACLE(configure)# session-router
ORACLE(session-router)# session-translation

session-translation
  id                    includeCallingPlus
  rules-calling         includePlus
  rules-called
```

2. Define the translation rule:

```
ORACLE(session-router)# translation-rules

translation-rules
  id                    includePlus
  type                  add
  add-string            +1
  add-index             0
  delete-string
  delete-index          0
```

Translation rule properties:

- **type** — `add`, `delete`, `replace`, or `none`
- **add-string** — String to add to the address (default: blank)
- **add-index** — Position to insert the string, 0 = leftmost (range 0–999999999)
- **delete-string** — String to delete; `@` denotes unspecified characters (default: blank)
- **delete-index** — Position to start deletion (range 0–999999999)

3. Apply the translation to the outside realm:

```
realm-config
  identifier            OUTSIDE
  out-translationid     includeCallingPlus
```

### Configure Codecs on Acme Packet

Set a codec policy as needed. See [Telnyx supported codecs](https://sip.telnyx.com/#codecs). To prefer PCMU for all clients making outbound calls:

```
realm-config
  identifier             clients
  options                preferred-codec=PCMU
```

For more details, refer to the [Acme SBC user guide](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-3D090BC0-31D0-419D-A1F9-E7B1E5D3D55D.htm) and Oracle's [codec policy documentation](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-49ECD7A3-8663-44ED-ADD4-EB01B76CC527.htm).

## AudioCodes SBC Configuration

[AudioCodes SBC devices](https://www.audiocodes.com/solutions-products/products/session-border-controllers-sbcs) provide connectivity, security, and quality assurance for VoIP networks, supporting both enterprise and service provider environments. Configuration is done through INI files.

### Define the IP Group

```
[ IPGroup ]
  IPGroup_Description:  Telnyx
  IPGroup_SIPGroupName: sip.telnyx.com
[ \IPGroup ]
```

### Define the SIP Proxy

```
[ ProxyIp ]
  FORMAT ProxyIp_Index = ProxyIp_IpAddress, ProxyIp_TransportType, ProxyIp_ProxySetId;
  ProxyIp 1 = "192.76.120.10/32:5060", 0, 1;
  ProxyIp 2 = "64.16.250.10/32:5060", 0, 1;
[ \ProxyIp ]
```

### Define Coders

```
[ CodersGroup0 ]
  CodersGroup0_Name:        g711ulaw64k
  CodersGroup0_pTime:       20
  CodersGroup0_PayloadType: 0
[ \CodersGroup0 ]
```

Depending on your requirements, you may also need to configure IP profiles and routing. For more information, see [AudioCodes SBC documentation](https://www.audiocodes.com/library/technical-documents?productFamilyGroup=1637), the [interoperability list](https://www.audiocodes.com/partners/interoperability-list), and [AudioCodes support](https://www.audiocodes.com/services-support).
