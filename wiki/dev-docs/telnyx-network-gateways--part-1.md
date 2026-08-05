---
title: Telnyx Network Gateways
summary: 'Telnyx offers three primary network gateway elements that route traffic
  across its backbone and the public internet: the Internet Gateway (IGW), the Private
  Wireless Gateway (PGW), and the WireGuard Gateway (WGW). Each gateway is provisioned
  on a Telnyx Network, has a per-instance monthly recurring cost, and can be combined
  with the others to build architectures ranging from simple VPNs to multi-cloud,
  multi-region, and SIM-connected private networks.'
sources:
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
updated_at: 2026-08-05T13:59:30Z
---

# Telnyx Network Gateways

*Part 1 of 4 — see also: [Part 2](telnyx-network-gateways--part-2.md), [Part 3](telnyx-network-gateways--part-3.md), [Part 4](telnyx-network-gateways--part-4.md)*

Telnyx offers three primary network gateway elements that route traffic across its backbone and the public internet: the Internet Gateway (IGW), the Private Wireless Gateway (PGW), and the WireGuard Gateway (WGW). Each gateway is provisioned on a Telnyx Network, has a per-instance monthly recurring cost, and can be combined with the others to build architectures ranging from simple VPNs to multi-cloud, multi-region, and SIM-connected private networks.

## Overview

Telnyx provides three gateway elements that can be deployed on a [Network](networks.md) to route traffic between your environment, the Telnyx backbone, and the public internet:

- **Internet Gateway (IGW)** — routes traffic between the Telnyx network and the public internet. Currently a beta feature.
- **Private Wireless Gateway (PGW)** — routes traffic between a group of Telnyx SIMs and other network elements.
- **WireGuard Gateway (WGW)** — a VPN concentrator built on [WireGuard](https://www.wireguard.com/) to which peers can connect over the public internet.

> **Naming note:** In the API reference, legacy documentation, and the Mission Control Portal, WireGuard Gateways are referred to as "Wireguard Interfaces". In this guide and across the Networking collection, the term **WireGuard Gateway** is used consistently. Devices that connect to a WGW are called **WireGuard Peers** or simply **Peers**.

## Common Provisioning Workflow

All three gateways follow the same four-step provisioning pattern. Once a gateway is created on a specific network, it cannot be migrated to another network — it must be recreated.

1. **Create a Network** — see the [Networks](networks.md) guide.
2. **Check for Coverage** — see the [Coverage](coverage.md) guide, using the appropriate `filter[available_services][contains]` value for the gateway type.
3. **Create the Gateway** — `POST` to the gateway-specific endpoint with the `network_id`, `name`, and `region_code`.
4. **Wait for Status Transition** — poll the gateway until its status moves from `provisioning` to `provisioned`.

## Internet Gateway (IGW)

The Internet Gateway routes traffic between your Telnyx network and the public internet. It is intended to be used with other network elements such as the WGW or PGW.

### Creating an IGW

- **Coverage filter:** `filter[available_services][contains]=public_internet_gateway` (e.g. `frankfurt-de`).
- **Endpoint:** `POST /v2/public_internet_gateways`
- **Provisioning time:** approximately 10 minutes.

Request:

```
POST /v2/public_internet_gateways HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 125

{
  "network_id": "5647b6cf-b204-42d6-9c63-f2fd12253113",
  "name": "my_first_igw",
  "region_code": "frankfurt-de"
}
```

Response (status `provisioning`):

```json
{
    "data": {
        "created_at": "2024-08-01T14:36:39.938006Z",
        "region_code": "frankfurt-de",
        "name": "my_first_igw",
        "network_id": "5647b6cf-b204-42d6-9c63-f2fd12253113",
        "id": "06d65677-f1aa-43b6-8a6c-4f1abfe93754",
        "status": "provisioning",
        "updated_at": "2024-08-01T14:36:41.497785Z",
        "record_type": "public_internet_gateway",
        "public_ip": "64.16.243.172"
    }
}
```

Poll status with `GET /v2/public_internet_gateways/{{igw_uuid}}`.

### IGW Use Cases

**Pure-play VPN (IGW + WGW).** Combine an IGW with a WGW and a peer to create a simple VPN service. On the peer config, set `DNS` to a resolver of your choice (e.g. `8.8.8.8`) and append `0.0.0.0/0` to `AllowedIPs` so reachability extends beyond the private subnet:

```
[Interface]
PrivateKey = XXX
Address = 172.27.0.2/32
DNS = 8.8.8.8

[Peer]
PublicKey = YYY
AllowedIPs = 172.27.0.0/24, 0.0.0.0/0
Endpoint = 64.16.243.7:5022
PersistentKeepalive = 1
```

After deactivating and reactivating the WireGuard tunnel, the peer's public IP should resolve to the IGW's `public_ip`:

```
user@localhost ~ % dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com
"64.16.243.172"
```

**IGW + Private Wireless Gateway (PWG).** Coming soon.

### IGW Costs

- Monthly recurring cost (MRC): **$50 per IGW instance**.
- Traffic is not metered during the beta phase; metering will be introduced at GA.

### IGW API Reference

- [Create a Public Internet Gateway](/api-reference/public-internet-gateways/create-a-public-internet-gateway)
