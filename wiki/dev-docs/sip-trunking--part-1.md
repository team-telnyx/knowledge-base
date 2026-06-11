---
title: SIP Trunking
summary: Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections
  for inbound traffic and Outbound Voice Profiles for outbound routing, with features
  including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external
  transfers, and configurable routing with automatic failover.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
- url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/failover-and-retries/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
updated_at: 2026-06-11T10:45:55Z
---

# SIP Trunking

*Part 1 of 3 — see also: [Part 2](sip-trunking--part-2.md), [Part 3](sip-trunking--part-3.md)*

Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections for inbound traffic and Outbound Voice Profiles for outbound routing, with features including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external transfers, and configurable routing with automatic failover.

## Architecture Overview

Telnyx SIP trunking uses **SIP Connections** for inbound traffic and authentication, and **Outbound Voice Profiles** for outbound call routing.

A SIP Connection authenticates traffic with Telnyx SIP proxies and configures inbound call handling. Authentication can be credential-based, IP address-based, or FQDN-based. Phone numbers are assigned to a connection for inbound routing, and an AnchorSite (regional PoP) can be selected for media optimization.

An Outbound Voice Profile controls outbound call routing, allowed destinations, rate limits, and spending limits. Each SIP connection must have an outbound voice profile assigned to make outbound calls.

## SIP Connections

### Authentication Methods

| Method | Description |
| --- | --- |
| Credential | Username/password (SIP digest authentication) |
| IP address | Matches calls by source IP |
| FQDN | Matches calls by fully qualified domain name |

For credential-authenticated connections, Telnyx identifies the connection by the username in the SIP `Contact` header or a custom `X-Telnyx-Username` header. This is important in shared or cloud environments where multiple connections may share the same source IP — always include the username to ensure correct authentication against your FQDN connection.

### Connection Types

Connections can be created as credential, IP, or FQDN types. Each type supports the same core features (jitter buffer, noise suppression, routing) but differs in how traffic is authenticated. FQDN connections are commonly used for integrations with platforms like LiveKit.

## Outbound Voice Profiles

Outbound voice profiles define:

- Which SIP connection is used for outbound calls
- Service plan and allowed destinations
- Daily spend limits and concurrent call limits
- Rate limits per minute

A connection without an assigned outbound voice profile will reject outbound calls (response code D38/D7).

## Network Configuration

### IP Whitelisting and Ports

For current SIP signaling addresses, media IP ranges, supported codecs, and regional FQDNs, see [sip.telnyx.com](https://sip.telnyx.com).

**Required ports:**

| Service | Ports | Protocol |
| --- | --- | --- |
| SIP signaling | 5060 | UDP/TCP |
| SIP signaling (TLS) | 5061 | TCP |
| RTP media | 16384–32768 | UDP |
| Webhooks | 443 | TCP |

**Webhook IP addresses** to whitelist:

| Region | CIDR Block |
| --- | --- |
| US-Central (CH1) | `192.76.120.128/29` |
| US-East (DC2) | `192.76.120.136/29` |
| US-West (SV1) | `192.76.120.144/29` |
| London (LD6) | `185.246.41.0/29` |
| Frankfurt (FR5) | `185.246.41.8/29` |
| Amsterdam (AM6) | `185.246.41.16/29` |
| Sydney (SY1) | `103.115.244.0/29` |
| Singapore (SG1) | `103.115.244.8/29` |

These ranges also apply to WebSocket stream connections.

### SRV Records

DNS SRV records enable automatic failover and load distribution by resolving to multiple Telnyx signaling IPs with priority and weight parameters. SRV records follow RFC 2782:

```
_sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.
```

**Regional FQDNs:**

| Region | FQDN | Resolves to IPs |
| --- | --- | --- |
| US | `sip.telnyx.com` | `192.76.120.10`, `64.16.250.10` |
| Europe | `sip-eu.telnyx.com` | `5.172.39.10`, `5.172.39.25` |
| Canada | `sip-ca.telnyx.com` | `193.108.220.10`, `193.108.220.25` |
| Australia | `sip-au.telnyx.com` | `193.108.104.10`, `193.108.104.25` |

For TLS, use `_sip._tcp` with port 5061. For multi-region redundancy, use different priority values:

```
_sip._udp.example.com. 3600 IN SRV 10 50 5060 sip.telnyx.com.
_sip._udp.example.com. 3600 IN SRV 20 50 5060 sip-eu.telnyx.com.
```

SRV records provide automatic IP failover, port specification, weight-based load balancing, and protocol awareness — none of which are available with plain A records. Verify with `dig _sip._udp.example.com SRV`.

When configuring with DNS providers, note the trailing dot on the target FQDN. For example, in AWS Route 53 the value format is `10 10 5060 sip.telnyx.com.`.

### STUN/TURN Servers

STUN and TURN servers enable NAT traversal for SIP clients behind firewalls and private networks. Use them when experiencing one-way audio or when clients cannot receive inbound connections directly.

| Type | Endpoint | Port | Protocol |
| --- | --- | --- | --- |
| STUN | `stun.telnyx.com` | 3478 | UDP |
| TURN | `turn.telnyx.com` | 3478 | UDP/TCP |

TURN requires credentials — contact Telnyx support to obtain them. Third-party STUN servers (e.g., `stun.l.google.com:19302`) can also be used.

Ensure outbound traffic is allowed on port 3478 (UDP/TCP) and RTP media ports 16384–32768 are open bidirectionally. In restrictive networks that block UDP, use TURN over TCP and TLS for SIP signaling (port 5061).

## Routing Configuration

### AnchorSite

AnchorSite determines which Telnyx Point of Presence (PoP) handles media routing.

**Latency mode** (default) automatically selects the optimal PoP based on ICMP ping latency. For IP/FQDN authentication, whitelist Telnyx media IPs for ICMP. For credential authentication, include the username in the `Contact` header or `X-Telnyx-Username` header.

**Manual mode** explicitly selects a PoP:

| Value | Location |
| --- | --- |
| `Chicago, IL` | North America Central |
| `Ashburn, VA` | North America East |
| `San Jose, CA` | North America West |
| `Toronto, Canada` | North America Northeast |
| `Montreal, Canada` | North America Northeast |
| `Vancouver, Canada` | North America Northwest |
| `London, UK` | Europe West |
| `Amsterdam, Netherlands` | Europe |
| `Frankfurt, Germany` | Europe Central |
| `Sydney, Australia` | Asia Pacific |

Configure via API:

```json
{ "anchorsite_override": "latency" }
```

If the selected PoP is unavailable, calls automatically reroute through the next available PoP.

### Failover and Retries

Telnyx uses two geographically redundant signaling IPs per region:

| Region | Primary (IP1) | Secondary (IP2) |
| --- | --- | --- |
| US | `192.76.120.10` | `64.16.250.10` |
| EU | `5.172.39.10` | `5.172.39.25` |
| Canada | `193.108.220.10` | `193.108.220.25` |
| Australia | `103.135.104.10` | `103.135.104.25` |

**Failover behavior:**

- **Single route:** INVITE from IP1; on failure, retry from IP2.
- **Multiple routes:** Attempt all routes via IP1 in configured order; on failure, retry all via IP2.
- **Credential authentication:** Calls route through the registered KSS instance with three levels of internal failover.
- **Call forward on failure:** When enabled, calls that fail on all SIP routes forward to PSTN (up to 10 termination carriers).

**Response codes that trigger failover:** 408, 480, 503, 504, and transport errors.

**Codes that do NOT trigger failover:** 180, 200, 404, 486, 603.

Configure via API:

```json
{
  "default_routing_method": "sequential",
  "call_forwarding": { "forwarding_type": "on_failure" }
}
```

### Round Robin Routing

Round robin routing distributes inbound calls sequentially across all configured IP addresses. Each IP receives equal call volume regardless of active call load.

```
Call 1 → IP 1
Call 2 → IP 2
Call 3 → IP 3
Call 4 → IP 1
```

If the target IP fails, the system attempts remaining IPs in sequence. Configure with `"default_routing_method": "round-robin"`. Note that round robin only counts inbound call distribution, not active call load — an IP handling 100 active calls receives the same incoming call rate as one handling 10.
