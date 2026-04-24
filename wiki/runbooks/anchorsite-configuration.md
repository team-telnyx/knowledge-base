---
title: AnchorSite Configuration
summary: Configure AnchorSite to control which Telnyx PoP handles media routing for SIP calls, with latency-based and manual selection modes.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration/index
    content_hash: c8be6508d14b3a4a655676cd227bc9388101761af790cf6bbda85e40946204a6
updated_at: 2026-04-10T00:00:00Z
---

# AnchorSite Configuration

Configure AnchorSite to control which Telnyx PoP handles media routing for SIP calls, with latency-based and manual selection modes.

AnchorSite determines which Telnyx Point of Presence (PoP) handles media routing for SIP calls.

## Configuration modes

### Latency mode

Automatically selects the optimal PoP based on ICMP ping latency measurements to the SIP endpoint.

**Requirements:**

* IP/FQDN authentication: Whitelist Telnyx media IP addresses for ICMP.
* Credential authentication: Include username in `Contact` header or `X-Telnyx-Username` header:

```
Contact: <sip:user@192.0.2.10:5060>
X-Telnyx-Username: connection_username
```

* TeXML: PoP selected based on latency to webhook URL IP.

### Manual mode

Explicitly select a PoP for predictable routing behavior.

**Available PoPs:**

| Value                    | Location                |
| ------------------------ | ----------------------- |
| `Chicago, IL`            | North America Central   |
| `Ashburn, VA`            | North America East      |
| `San Jose, CA`           | North America West      |
| `Toronto, Canada`        | North America Northeast |
| `Montreal, Canada`       | North America Northeast |
| `Vancouver, Canada`      | North America Northwest |
| `London, UK`             | Europe West             |
| `Amsterdam, Netherlands` | Europe                  |
| `Frankfurt, Germany`     | Europe Central          |
| `Sydney, Australia`      | Asia Pacific            |

## Configuration

You can configure AnchorSite in the [Telnyx Portal](https://portal.telnyx.com/#/app/sip-trunking/ip-connections) by editing an IP Connection:

  <img alt="IP Connection settings in the Telnyx Portal showing the AnchorSite Override dropdown with Latency and manual PoP options" />

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection):

```json theme={null}
{
  "anchorsite_override": "latency"
}
```

For manual selection:

```json theme={null}
{
  "anchorsite_override": "Chicago, IL"
}
```

## Failover

If the selected PoP is unavailable (maintenance, outage, health check failure), calls automatically reroute through the next available PoP.


## Related Pages

- [Configuration](../runbooks/configuration.md)
- [Configuration](../runbooks/configuration-2.md)
- [Configuration](../runbooks/configuration-3.md)
- [Phone Number Messaging Configuration](../runbooks/phone-number-messaging-configuration.md)
