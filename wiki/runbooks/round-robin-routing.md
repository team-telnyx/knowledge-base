---
title: Round Robin Routing
summary: Round robin routing distributes inbound calls sequentially across all configured IP addresses in a SIP connection.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
    content_hash: ddc3b53b2c657ec45e42006a032037bc7a718dcaaae3cd7dd9a27da7c094e1de
updated_at: 2026-04-10T00:00:00Z
---

# Round Robin Routing

Round robin routing distributes inbound calls sequentially across all configured IP addresses in a SIP connection. Each IP receives equal call volume regardless of active call load.

## How it works

Calls route to IPs in sequential order:

```
Call 1 → IP 1
Call 2 → IP 2
Call 3 → IP 3
Call 4 → IP 1 (cycle repeats)
```

### Failover behavior

If the target IP fails, the system attempts remaining IPs in sequence. All IPs function as backups for each other.

Example: If IP 2 is selected first and fails, the system tries IP 3, then IP 1.

## Configuration

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection)

```json theme={null}
{
  "default_routing_method": "round-robin"
}
```

## Limitations

* Only counts inbound call distribution, not active call load
* An IP handling 100 active calls receives the same incoming call rate as an IP handling 10 active calls

## Use cases

* Distributing load across multiple PBX instances
* High-availability setups without dedicated failover systems
* Deployments where simple call distribution is sufficient
