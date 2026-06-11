---
title: Telnyx Programmable Networking
summary: Telnyx Programmable Networking provides private, high-performance connectivity
  between your infrastructure and Telnyx SIP, API, and storage endpoints without traversing
  the public internet. It is built around networks, gateways (Wireguard, Internet,
  Private Wireless), and Virtual Cross Connects, all managed via the Telnyx API.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
- url: https://developers.telnyx.com/docs/network/networks
- url: https://developers.telnyx.com/docs/network/overview/index
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
updated_at: 2026-06-11T10:37:56Z
---

# Telnyx Programmable Networking

*Part 1 of 2 — see also: [Part 2](telnyx-programmable-networking--part-2.md)*

Telnyx Programmable Networking provides private, high-performance connectivity between your infrastructure and Telnyx SIP, API, and storage endpoints without traversing the public internet. It is built around networks, gateways (Wireguard, Internet, Private Wireless), and Virtual Cross Connects, all managed via the Telnyx API.

## Overview

Telnyx programmable networking lets users and their applications access Telnyx SIP and API endpoints without traversing the public internet, offering improved latency and throughput. The key endpoints accessible privately are:

- `api.telnyx.com`
- `sip.telnyx.com` and regional counterparts
- `*.telnyxcloudstorage.com` (all available storage regions, e.g. `us-central-1`)

Applications can reside in any major hyperscaler (AWS, GCP, Azure) or in users' own data centers (if they have a presence in Equinix). The model is analogous to AWS Direct Connect — from the outside world, a user can connect to private resources (e.g. EC2 instances) or public resources (e.g. S3).

## Coverage

Individual networking resource availability is not universal across all Telnyx regions. Use the Coverage API to check which services are available at which locations before creating resources.

### Generic Coverage API

`GET /v2/network_coverage` returns available services per location. The `location` parameter is hierarchical:

| Parameter | Value |
| --- | --- |
| `region` | `EMEA`, `AMER`, `APAC` |
| `site` | Broad geographical area within the region, e.g. `ORD` in `AMER` |
| `pop` | Specific data center within the site, e.g. `CH1` in `ORD` |
| `name` | Human-readable name, e.g. `Chicago IL, US` |
| `code` | Unique ID for the site, e.g. `chicago-il` |

The `available_services` array lists all resources that can be created at that location. Possible values:

- `virtual_cross_connect`
- `cloud_vpn` (Wireguard Gateway / Wireguard Interface)
- `private_wireless_gateway`
- `public_internet_gateway`

Common query patterns:

- By product: `GET /v2/network_coverage?filter[available_services][contains]=cloud_vpn`
- By product with location constraint: `GET /v2/network_coverage?filter[available_services][contains]=cloud_vpn&filter[location.region]=AMER`
- By location: `GET /v2/network_coverage?filter[location.region]=EMEA`

### Virtual Cross Connect Coverage API

Because a VXC has two terminating endpoints (a cloud provider endpoint and a Telnyx endpoint), the generic coverage API is insufficient — it only shows one side. Use `GET /v2/virtual_cross_connects_coverage` to check valid endpoint pairings.

- Fix the Telnyx endpoint: `GET /v2/virtual_cross_connects_coverage?filter[location.pop]=CH1` — returns all possible cloud provider endpoints.
- Fix the cloud provider endpoint: `GET /v2/virtual_cross_connects_coverage?filter[cloud_provider]=aws&filter[cloud_provider_region]=us-east-1` — returns all possible Telnyx endpoints.

The response includes `available_bandwidth` (in Mbps) for each pairing.

## Networks

A network is a logically isolated virtual network and is a prerequisite for creating all other elements (gateways, VXC). Create one with:

```
POST /v2/networks
```

```json
{
  "name": "my_first_virtual_network"
}
```

The response returns the network `id` which is required by all subsequent resource creation calls.

## Gateways Types

Gateways are virtual nodes that facilitate traffic routing between your Telnyx network and an outside network. There are three types.

### Wireguard Gateway (WGW)

A Wireguard Gateway is a virtual VPN concentrator built on the open-source Wireguard protocol. It is analogous to Virtual Private Gateway (AWS), VPN Gateway (GCP), or Virtual Network Gateway (Azure). In the API and Mission Control Portal, WGWs may be referred to as "Wireguard Interfaces." Connected devices are called Wireguard Peers (or simply Peers).

**Creating a WGW:**

1. Create a [Network](telnyx-programmable-networking-networks.md).
2. Check coverage with `filter[available_services][contains]=cloud_vpn`.
3. Create the WGW via `POST /v2/wireguard_interfaces` with `network_id`, `name`, and `region_code`.
4. Wait ~5 minutes for status to transition from `provisioning` to `provisioned`.

The creation response includes:

- `endpoint` — the publicly routable IP:port that peers connect to.
- `server_ip_address` — the private subnet range; the WGW occupies the first usable IP (e.g. `172.27.0.1/24`).
- `public_key` — the WGW's Wireguard public key.

**Creating Peers:**

Peers are created via `POST /v2/wireguard_peers` with `name` and `wireguard_interface_id`. The response includes a `private_key` (shown only once — store it immediately) and `public_key`.

A peer config template is available at `GET /v2/wireguard_peers/{peer_id}/config`. After inserting the `private_key`, import the conf file on the host.

In the peer config:

- `[Interface]` refers to the local peer. `PrivateKey` is the peer's private key; `Address` is the next available IP in the subnet.
- `[Peer]` refers to the WGW. `PublicKey` is the WGW's public key; `AllowedIPs` defines the networks this peer can reach; `Endpoint` is the WGW's public IP:port.

**Cost:** MRC is $10 per WGW instance. Connected peers are free.

### Internet Gateway (IGW)

An Internet Gateway routes traffic between your Telnyx network and the public internet. It is analogous to Internet Gateway or NAT Gateway in AWS.

**Creating an IGW:**

1. Create a [Network](telnyx-programmable-networking-networks.md).
2. Check coverage with `filter[available_services][contains]=public_internet_gateway`.
3. Create the IGW via `POST /v2/public_internet_gateways` with `network_id`, `name`, and `region_code`.
4. Wait ~10 minutes for status to transition from `provisioning` to `provisioned`.

The creation response includes `public_ip`, which is the internet-facing IP assigned to the IGW.

Once created on a network, an IGW cannot be migrated to another network — it must be recreated.

**Cost:** MRC is $50 per IGW instance. Traffic is not metered during the beta phase but will be in GA.

### Private Wireless Gateway (PGW)

A Private Wireless Gateway routes traffic between a group of Telnyx SIMs and other network elements. It concentrates, routes, and segments SIM traffic.

**Creating a PGW:**

1. Create a [Network](telnyx-programmable-networking-networks.md).
2. Check coverage with `filter[available_services][contains]=private_wireless_gateway`. Currently, Ashburn, VA (`ashburn-va`) is the only supported site.
3. Create the PGW via `POST /v2/private_wireless_gateways` with `network_id`, `name`, and `region_code`.
4. Wait ~15 minutes for `status.value` to transition from `provisioning` to `provisioned`.
5. Attach a SIM group via the Mission Control Portal. Individual SIMs must be added to a SIM group, which is then attached to the PGW.

The creation response includes `ip_range` (the private subnet assigned to the PGW, e.g. `100.64.199.0/24`).

Once created on a network, a PGW cannot be migrated to another network — it must be recreated.

**Cost:** MRC is $100 per PGW instance. Additional SIM and data costs apply.
