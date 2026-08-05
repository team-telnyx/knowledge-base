---
title: SIP Trunking on Telnyx
summary: Telnyx Elastic SIP Trunking provides elastic, programmable telephony over
  IP with multiple authentication methods, configurable outbound policies, call-quality
  features, and emergency calling support. This page consolidates the authentication
  options, configuration guides, caller ID and concurrency policies, advanced features,
  and emergency calling capabilities available on Telnyx SIP trunks.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
updated_at: 2026-08-05T14:05:52Z
---

# SIP Trunking on Telnyx

*Part 1 of 5 — see also: [Part 2](sip-trunking-on-telnyx--part-2.md), [Part 3](sip-trunking-on-telnyx--part-3.md), [Part 4](sip-trunking-on-telnyx--part-4.md), [Part 5](sip-trunking-on-telnyx--part-5.md)*

Telnyx Elastic SIP Trunking provides elastic, programmable telephony over IP with multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling support. This page consolidates the authentication options, configuration guides, caller ID and concurrency policies, advanced features, and emergency calling capabilities available on Telnyx SIP trunks.

## Overview

Telnyx Elastic SIP Trunking connects IP-PBX systems, SBCs, softphones, and other SIP infrastructure to the PSTN. Trunks support multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling. Configuration guides are available for a wide range of third-party vendors and platforms.

## Authentication Methods

Telnyx SIP connections support multiple authentication methods based on network topology and security requirements.

| Method | Description |
| --- | --- |
| Credential-based | Username/password for SIP registration |
| IP + Token | `X-Telnyx-Token` header with IP validation |
| IP + Tech Prefix | 4-digit prefix prepended to dial string |
| IP + P-Charge-Info | Phone number in `P-Charge-Info` header |
| FQDN | Hostname-based inbound routing |

### Credential-based authentication

Username and password for SIP registration.

```
{
  "connection_name": "my-connection",
  "user_name": "username",
  "password": "secure-password"
}
```

For WebRTC applications requiring dynamic credentials or JWT tokens, see [WebRTC Authentication](webrtc-authentication.md).

### IP + Token authentication

The `X-Telnyx-Token` header distinguishes multiple SIP connections sharing the same IP address.

| Requirement | Value |
| --- | --- |
| Characters | Alphanumeric (a-z, A-Z, 0-9) and hyphens |
| Length | 12-48 characters |
| Scope | Globally unique across all Telnyx connections |

SIP header format:

```
X-Telnyx-Token: your-token-value
```

Include this header in all outbound SIP INVITE requests. Configuration is performed via `PATCH /v2/ip_connections/`:

```
{
  "outbound": {
    "outbound_voice_profile_id": "uuid",
    "ip_authentication_token": "your-token-value"
  }
}
```

| Condition | Result |
| --- | --- |
| IP matches + token matches | Authenticated |
| IP matches + token missing/incorrect | Rejected |
| IP mismatch + token matches | Rejected |

Both the source IP and `X-Telnyx-Token` value must match the connection configuration.

### IP + Tech Prefix authentication

A 4-digit identifier prepended to outbound calls to differentiate multiple SIP connections sharing the same IP address.

Dial string format:

```
[tech_prefix][destination_number]
```

Example: Tech prefix `1234` + destination `+18005678912` = `123418005678912`.

Use cases include multiple SIP connections from the same IP address, granular call routing and billing per connection, and traffic stream separation. The PBX or SIP client must prepend the tech prefix to all outbound calls on the trunk. The tech prefix value is assigned by Telnyx and visible in the connection settings.

| Condition | Result |
| --- | --- |
| Correct tech prefix included | Call authenticated |
| Missing or incorrect prefix | `407 Proxy Authentication Required` |

### IP + P-Charge-Info authentication

The `P-Charge-Info` header contains a phone number associated with the connection and identifies the billing number (DID) for outbound calls.

```
P-Charge-Info: <sip:+15551234567@sip.telnyx.com>
```

The value must be a valid DID associated with the Telnyx SIP connection, in E.164 format, and wrapped in SIP URI format. Use cases include multiple DIDs on a single SIP connection, CDR attribution per DID, billing and usage tracking per number, and carrier-side call routing based on originating number.

Requirements: a Telnyx SIP connection configured for outbound calling, valid DID ownership and assignment to the connection, and PBX access to modify dialplan or trunk configuration.

### FQDN authentication

Hostname-based inbound routing combined with credentials or IP authentication for outbound.

| Inbound | Outbound |
| --- | --- |
| FQDN | Credentials |
| FQDN | IP address |

### Comparison

| Method | Inbound | Outbound | Dynamic IP | Static IP |
| --- | --- | --- | --- | --- |
| Credentials | ✓ | ✓ | ✓ | ✓ |
| IP + Tech prefix | ✓ | ✓ | - | ✓ |
| IP + Token | ✓ | ✓ | - | ✓ |
| IP + P-Charge-Info | ✓ | ✓ | - | ✓ |
| FQDN + Credentials | ✓ | ✓ | ✓ | ✓ |
| FQDN + IP | ✓ | ✓ | - | ✓ |

## Configuration Guides

Telnyx publishes configuration guides for connecting SIP infrastructure (IP-PBX, SBC, softphones, IP phones, conference phones, ATAs, and more) to an Elastic SIP Trunk. These are general guidelines rather than configuration templates; settings may differ depending on the version, add-ons, and options of the third-party system. Telnyx cannot provide direct support for third-party products — contact the manufacturer for assistance.

The following vendors are covered (selected examples; full list available in the source index):

- **3CX** — V14, V15, V16, V18 with IP and credentials trunks
- **Acrobits** — Groundwire, Softphone
- **Algo** — 8xxx Series IP endpoints
- **Asterisk** — Credentials and IP trunks
- **Audiocodes** — 400HD IP phones and SBCs
- **Avaya** — IP trunk
- **Bicom** — PBXware
- **Cisco** — 68xx/88xx, CME, CUBE/CUCM, SPA112/122
- **CounterPath** — Bria Teams, Bria Solo
- **Elastix by 3CX** — Elastix 4 and 5 with IP and credentials trunks
- **Epygi** — QX series
- **Fanvil** — H-series, X-series, V-series, A32i, and others
- **Flyingvoice** — All IP phones
- **Fortinet** — FortiFone FON series
- **FreePBX** — v13, v14, v15 with ChanSIP and PJSIP, IP and credentials trunks
- **FreeSWITCH** — Credentials and IP trunks
- **FusionPBX** — Credentials trunk
- **Gigaset** — A510, DX800a, A690/AS690
- **GOautodial** — IP and credentials trunks
- **Grandstream** — GXP, GRP, GXV, DP, UMC, HT, Wave Lite, GDS series
- **Konftel** — 300IPx, 300Wx
- **Linphone** — Softphone
- **Mediatrix** — C7/4100
- **Microsoft** — Azure AD SAML, Teams Direct Routing, Call2Teams
- **Mitel** — 5320E/5330E/5340E, 6800/6900
- **NCH Software** — ExpressTalk
- **OSDial** — Predictive dialer
- **Panasonic** — KX-HDV, TGP 550
- **PBXes** — Trunk
- **PhoneSuite** — Voiceware
- **Plantronics/Polycom** — Poly OBi300, VVX 300-series
- **Positron** — IP304/IP304C, IP408/IP408C, IP410C/IP410G, G-Series
- **Ribbon** — EdgeMarc 6000 SBC
- **Sansay** — VSXi SBC
- **ScopServ** — ScopTEL
- **SIPfoundry** — sipXecs
- **Skype** — Skype for Business (Office 365)
- **SNOM** — M100 KLE, D7xx, C520
- **Synway** — UC-200
- **Thirdlane** — PBX
- **Ubiquiti** — Unifi Talk with IP and credentials trunks
- **Vicidial** — IP and credentials trunks
- **VitalPBX** — PBX
- **Vodia** — Multi-tenant PBX
- **Voice Elements by Microsoft .NET** — Development environment
- **Vtech** — VCS754 ErisStation
- **Wildix** — PBX
- **Xorcom** — Complete PBX
- **Yealink** — IP phones
- **Yeastar** — S-Series
- **Zoiper** — Communicator, 5 Pro, 3 (Linux and MacOS)

SAML identity providers are also documented for Auth0, GSuite, LastPass, Microsoft Azure AD, Okta, and OneLogin. Virtual cross-connects are documented for Amazon AWS, Google VPC, and Microsoft Azure.
