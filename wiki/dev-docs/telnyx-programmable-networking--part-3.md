---
title: Telnyx Programmable Networking
summary: Telnyx Programmable Networking provides private connectivity to Telnyx SIP,
  API, and storage endpoints via logically isolated networks, three types of gateways
  (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS,
  GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway
  setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific
  VXC setup procedures and pricing.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
- url: https://developers.telnyx.com/docs/network/networks
- url: https://developers.telnyx.com/docs/network/overview/index
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
updated_at: 2026-07-17T09:20:17Z
---

# Telnyx Programmable Networking

*Part 3 of 7 — see also: [Part 1](telnyx-programmable-networking--part-1.md), [Part 2](telnyx-programmable-networking--part-2.md), [Part 4](telnyx-programmable-networking--part-4.md), [Part 5](telnyx-programmable-networking--part-5.md), [Part 6](telnyx-programmable-networking--part-6.md), [Part 7](telnyx-programmable-networking--part-7.md)*

Telnyx Programmable Networking provides private connectivity to Telnyx SIP, API, and storage endpoints via logically isolated networks, three types of gateways (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS, GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific VXC setup procedures and pricing.

## Internet Gateway (IGW)

> This is a beta feature.

Internet Gateway (IGW) is an element that routes traffic between your Telnyx network and the internet. It is intended to be used with certain other elements.

### Creating an IGW

**Step 1: Create a Network** — follow the [Networks](networks.md) guide.

**Step 2: Check for Coverage** — follow the [Coverage](coverage.md) guide. Use `filter[available_services][contains]=public_internet_gateway` to look for a desired site at which to deploy the IGW. `frankfurt-de` is chosen for the subsequent steps.

**Step 3: Create an IGW** — using the network created from Step 1 and the chosen region from Step 2, create the IGW. Once an IGW is created on a specific network, it cannot be "migrated" to another one; it needs to be recreated on the other network. Double check the correct `network_id` is used in the following API request.

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

It's not yet ready to be used immediately after the creation since its status is `provisioning`.

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

**Step 4: Wait for Status Transition** — the expected time for status to transition to provisioned is approximately 10 minutes. You can poll the IGW to check for status.

```
GET /v2/public_internet_gateways/{{igw_uuid}} HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

### IGW Use Cases

#### Use Case 1: Pure play VPN

Internet Gateway (IGW) can be used with WireGuard Gateway (WGW) to create a simple VPN service.

1. Set up an IGW
2. Set up a WGW and a peer.
3. On the peer, amend its config with:
   - `DNS` — choose your resolver. In the following example, 8.8.8.8 is chosen.
   - `AllowedIPs` — append with `0.0.0.0/0` so that reachability is beyond the private subnet.

Here is an example config of the peer.

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

Deactivate and reactivate your WireGuard tunnel. You should see the IGW's public IP showing up when you query what your public IP is.

```
user@localhost ~ % dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com
"64.16.243.172"
```

#### Use Case 2: IGW + Private Wireless Gateway (PWG)

Coming Soon.

### IGW Costs

- The monthly recurring cost (MRC) for each instance of IGW is $50.
- Traffic is not currently metered in beta phase. We will meter traffic in GA phase.
