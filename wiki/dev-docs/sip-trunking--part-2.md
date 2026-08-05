---
title: SIP Trunking
summary: Telnyx SIP trunking uses SIP Connections for inbound traffic and authentication,
  and Outbound Voice Profiles for outbound call routing. This page covers the core
  components, network configuration, routing options, and troubleshooting for SIP
  trunks.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/failover-and-retries/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
updated_at: 2026-08-05T14:05:40Z
---

# SIP Trunking

*Part 2 of 3 — see also: [Part 1](sip-trunking--part-1.md), [Part 3](sip-trunking--part-3.md)*

Telnyx SIP trunking uses SIP Connections for inbound traffic and authentication, and Outbound Voice Profiles for outbound call routing. This page covers the core components, network configuration, routing options, and troubleshooting for SIP trunks.

## STUN/TURN Servers

STUN (Session Traversal Utilities for NAT) and TURN (Traversal Using Relays around NAT) servers enable NAT traversal for SIP clients behind firewalls and private networks.

### When to Use STUN/TURN

Use STUN/TURN servers when the SIP client is:

- Behind a firewall or NAT gateway
- On a private network without public IP addresses
- Unable to receive inbound connections directly
- Experiencing one-way audio issues

### Telnyx STUN/TURN Endpoints

| Type | Endpoint | Port | Protocol |
| --- | --- | --- | --- |
| STUN | `stun.telnyx.com` | 3478 | UDP |
| TURN | `turn.telnyx.com` | 3478 | UDP/TCP |

### Configuration

**Standard STUN configuration** — configure the SIP client to use Telnyx STUN servers for NAT traversal:

```
STUN Server: stun.telnyx.com:3478
```

**TURN with authentication** — TURN requires credentials. Contact [Telnyx support](https://telnyx.com/support) to obtain TURN server credentials for the account.

```
TURN Server: turn.telnyx.com:3478
Username: [provided by Telnyx]
Password: [provided by Telnyx]
```

### Alternative STUN Servers

While Telnyx provides its own STUN infrastructure, third-party STUN servers may also be used:

```
stun.l.google.com:19302
stun1.l.google.com:19302
stun2.l.google.com:19302
```

### Network Requirements

Ensure the firewall allows outbound traffic:

| Service | Port | Protocol | Direction |
| --- | --- | --- | --- |
| STUN | 3478 | UDP | Outbound |
| TURN | 3478 | UDP/TCP | Outbound |
| RTP media | 16384-32768 | UDP | Bidirectional |

### ICE Candidate Types

When using STUN/TURN, the client will gather different types of ICE candidates:

- **host**: Local network addresses (cannot traverse NAT)
- **srflx**: Server reflexive addresses (via STUN)
- **relay**: Relayed addresses (via TURN)
- **prflx**: Peer reflexive addresses (discovered during connectivity checks)

For successful call establishment across NAT, at least one of the following candidate types must be available:

- `srflx` (server reflexive via STUN)
- `relay` (relayed via TURN)
- `prflx` (peer reflexive)

### Troubleshooting

**One-way audio:**

1. Verify STUN server is reachable: `stun.telnyx.com:3478`
2. Check that UDP port 3478 is allowed outbound
3. Ensure RTP media ports (16384-32768) are open bidirectionally

**Connection failures:**

1. Verify firewall rules allow outbound UDP to port 3478
2. Check that the SIP client supports STUN/TURN
3. Confirm TURN credentials are correct (if using TURN)
4. Review ICE candidate gathering logs in the client

**Restrictive networks** — in highly restrictive networks that block UDP traffic:

- Use TURN over TCP: `turn.telnyx.com:3478` (TCP)
- Consider using TLS for SIP signaling: port 5061
- Contact support for additional configuration options

## AnchorSite Configuration

AnchorSite determines which Telnyx Point of Presence (PoP) handles media routing for SIP calls.

### Configuration Modes

**Latency mode** — automatically selects the optimal PoP based on ICMP ping latency measurements to the SIP endpoint.

Requirements:

- IP/FQDN authentication: Whitelist Telnyx media IP addresses for ICMP.
- Credential authentication: Include username in `Contact` header or `X-Telnyx-Username` header:

```
Contact: <sip:user@192.0.2.10:5060>
X-Telnyx-Username: connection_username
```

- TeXML: PoP selected based on latency to webhook URL IP.

**Manual mode** — explicitly select a PoP for predictable routing behavior.

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
| `Dubai, UAE` | Middle East |

### Configuration

You can configure AnchorSite in the [Telnyx Portal](https://portal.telnyx.com/#/app/sip-trunking/ip-connections) by editing an IP Connection:

![IP Connection settings in the Telnyx Portal showing the AnchorSite Override dropdown with Latency and manual PoP options](https://mintcdn.com/telnyx/53Uwze2vwQbIRyze/img/anchorsite-configuration-dropdown.png?fit=max&auto=format&n=53Uwze2vwQbIRyze&q=85&s=c05c8c10406c1dbb8502530c7dd2d9bf)

[PATCH /v2/ip_connections/](/api-reference/ip-connections/update-an-ip-connection):

```json
{
  "anchorsite_override": "latency"
}
```

For manual selection:

```json
{
  "anchorsite_override": "Chicago, IL"
}
```

### Failover

If the selected PoP is unavailable (maintenance, outage, health check failure), calls automatically reroute through the next available PoP.

## Failover and Retries

Telnyx SIP connections automatically retry failed call attempts through different routes and IP addresses.

### Signaling IP Addresses

Telnyx uses two geographically redundant signaling IPs per region:

| Region | Primary (IP1) | Secondary (IP2) |
| --- | --- | --- |
| US | `192.76.120.10` | `64.16.250.10` |
| EU | `5.172.39.10` | `5.172.39.25` |
| Canada | `193.108.220.10` | `193.108.220.25` |
| Australia | `103.135.104.10` | `103.135.104.25` |

### Failover Behavior

**Single route:**

1. SIP INVITE sent from IP1
2. On failure, retry from IP2

**Multiple routes:**

1. Attempt all routes via IP1 in configured order
2. On failure, retry all routes via IP2

Route order depends on configured preference (Sequential or Round Robin).

**Credential authentication** — calls route through the registered KSS instance with three levels of internal failover.

**Call forward on failure** — when enabled, calls that fail on all SIP routes forward to PSTN (up to 10 termination carriers).

### Response Codes

**Triggers failover:**

| Code | Meaning |
| --- | --- |
| `408` | Request Timeout |
| `480` | Temporarily Unavailable |
| `503` | Service Unavailable |
| `504` | Server Timeout |
| Transport error | Network/TCP failure |

**Does NOT trigger failover** (call considered connected):

| Code | Meaning |
| --- | --- |
| `180` | Ringing |
| `200` | OK (answered) |
| `404` | Not Found |
| `486` | Busy Here |
| `603` | Decline |

### DNS Configuration

**SRV records (recommended):**

```
_sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.
```

Regional domains: `sip.telnyx.com` (US), `sip-eu.telnyx.com` (EU). SRV records automatically resolve to both IP1 and IP2.

**A records (alternative):** Configure separate A records for each signaling IP and add both as routes.

### Configuration

[PATCH /v2/ip_connections/](/api-reference/ip-connections/update-an-ip-connection):

```json
{
  "default_routing_method": "sequential",
  "call_forwarding": {
    "forwarding_type": "on_failure"
  }
}
```

## Round Robin Routing

Round robin routing distributes inbound calls sequentially across all configured IP addresses in a SIP connection. Each IP receives equal call volume regardless of active call load.

### How It Works

Calls route to IPs in sequential order:

```
Call 1 → IP 1
Call 2 → IP 2
Call 3 → IP 3
Call 4 → IP 1 (cycle repeats)
```

**Failover behavior** — if the target IP fails, the system attempts remaining IPs in sequence. All IPs function as backups for each other. Example: If IP 2 is selected first and fails, the system tries IP 3, then IP 1.

### Configuration

[PATCH /v2/ip_connections/](/api-reference/ip-connections/update-an-ip-connection)

```json
{
  "default_routing_method": "round-robin"
}
```

### Limitations

- Only counts inbound call distribution, not active call load
- An IP handling 100 active calls receives the same incoming call rate as an IP handling 10 active calls

### Use Cases

- Distributing load across multiple PBX instances
- High-availability setups without dedicated failover systems
- Deployments where simple call distribution is sufficient
