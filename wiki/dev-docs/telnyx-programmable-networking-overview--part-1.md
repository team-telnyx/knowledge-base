---
title: Telnyx Programmable Networking Overview
summary: 'A single overview of Telnyx programmable networking: how to privately reach
  Telnyx SIP, API, and Storage over Telnyx’s backbone; the building blocks (coverage,
  networks, gateways, VXC); common architectures; provisioning timelines; pricing;
  and key API endpoints.'
sources:
- url: https://developers.telnyx.com/docs/network/overview/index
  content_hash: 2a26be9e1ea7aa9c2c7b72303d9a8eb1cf5e0b9fe3f3b22f108ea376658e4c9c
- url: https://developers.telnyx.com/docs/network/coverage
  content_hash: bd20269393b84716e15ad07c2f8f59785803d57c0e4df7cf6e447da67233307a
- url: https://developers.telnyx.com/docs/network/networks
  content_hash: b8d4ab8f2ef8080f515aa944e60c7dd3054964e0c3083b458834250a73ccbcf9
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
  content_hash: d8c95a9b4664e9879fc22e60487c135564217d914415a98705660425317b48c5
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
  content_hash: 3514348876e4bc8c6fda332d7ab179f3f6c41e2adb7f1bb6353db51b6d24a3c7
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
  content_hash: 10d83c048c778c23a3f89df442a398d8504c79e9e8cf22fe24038efc8026729b
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
  content_hash: 883fd961a6c1a37a02bf04f4a8a43a61125ee9c4e31e439e964d4baed7dc039d
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
  content_hash: bf660e956d538dcbf5493fc0ef9dc68cd5a5952a4a4fd8b139c974f663b2a029
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
  content_hash: d08e536f2c6a7cfb6fb82418579d89c8bc70d58d925dd02bcfd4e75d0eb8121e
updated_at: 2026-05-20T09:16:29Z
---

# Telnyx Programmable Networking Overview

*Part 1 of 2 — see also: [Part 2](telnyx-programmable-networking-overview--part-2.md)*

A single overview of Telnyx programmable networking: how to privately reach Telnyx SIP, API, and Storage over Telnyx’s backbone; the building blocks (coverage, networks, gateways, VXC); common architectures; provisioning timelines; pricing; and key API endpoints.

## What Telnyx Programmable Networking Delivers
Telnyx programmable networking lets your applications access Telnyx SIP, APIs, and Storage without traversing the public internet, improving latency, throughput, and control. You can host workloads in AWS, GCP, Azure, or in your own data centers (with an Equinix presence), and connect into the Telnyx backbone.

Privately reachable Telnyx services include:
- api.telnyx.com
- sip.telnyx.com (and regional variants)
- *.telnyxcloudstorage.com (all storage regions, e.g., us-central-1)

## Location Model and Coverage APIs
Resource availability varies by Telnyx location. Always check coverage before creating resources.

- Generic coverage API: GET /v2/network_coverage
  - Location hierarchy: region (EMEA | AMER | APAC) → site (e.g., ORD) → pop (e.g., CH1) → name (e.g., “Chicago IL, US”) → code (e.g., “chicago-il”).
  - available_services can include: virtual_cross_connect, cloud_vpn (Wireguard Gateway), private_wireless_gateway, public_internet_gateway.
  - Example filters:
    - By product: GET /v2/network_coverage?filter[available_services][contains]=cloud_vpn
    - By product in region: …&filter[location.region]=AMER
    - By location only: GET /v2/network_coverage?filter[location.region]=EMEA
  - Guide: https://developers.telnyx.com/docs/network/coverage

- VXC coverage API: GET /v2/virtual_cross_connects_coverage
  - Use when planning a Virtual Cross Connect: you must validate both the Telnyx endpoint and the cloud provider endpoint.
  - Fix Telnyx PoP: GET /v2/virtual_cross_connects_coverage?filter[location.pop]=CH1
  - Fix provider & region: GET /v2/virtual_cross_connects_coverage?filter[cloud_provider]=aws&filter[cloud_provider_region]=us-east-1
  - available_bandwidth is returned in Mbps.

## Networks: The Required Prerequisite
A Network is a logically isolated virtual network in Telnyx and is a prerequisite for all other elements (gateways, VXCs, etc.).
- Create: POST /v2/networks with a name
- API reference: https://developers.telnyx.com/api-reference/networks/create-a-network

Key constraint: resources created on a network (e.g., WGW/IGW/PGW) cannot be migrated to another network; recreate them on the target network.

## Gateway Types and When to Use Them
Telnyx provides three gateway types to move traffic between your Telnyx network and external domains.

### Wireguard Gateway (WGW)
- What it is: A Wireguard-based VPN concentrator. In the API and some UI, WGWs are called “Wireguard Interfaces.”
- Typical uses:
  - Build a site-to-site or hub-and-spoke VPN for multi-cloud/private connectivity.
  - Optionally enable private access to Telnyx API/SIP/Storage via enable_sip_trunking.
- Create: POST /v2/wireguard_interfaces with network_id, name, region_code (e.g., “ashburn-va”).
- Provisioning: ~5 minutes (status transitions from provisioning → provisioned).
- Returned properties:
  - endpoint: public IP:port peers connect to over the internet.
  - server_ip_address: Wireguard subnet, with WGW at the first usable IP (e.g., 172.27.0.1/24).
- Peers:
  - Create: POST /v2/wireguard_peers with name and wireguard_interface_id.
  - private_key is returned once at creation—store it securely.
  - Fetch template config: GET /v2/wireguard_peers/{peer_id}/config, then insert private_key.
  - AllowedIPs controls reachable subnets; include the WGW subnet and any additional routes (e.g., Telnyx ranges when enable_sip_trunking is true, or 0.0.0.0/0 when using IGW for internet egress).
- Costs: $10 MRC per WGW; Peers are free.
- Guide: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway
- API reference: https://developers.telnyx.com/api-reference/wireguard-interfaces/create-a-wireguard-interface

### Internet Gateway (IGW) [Beta]
- What it is: Routes traffic between your Telnyx network and the public internet; pair with WGW for egress.
- Create: POST /v2/public_internet_gateways with network_id, name, region_code (e.g., “frankfurt-de”).
- Provisioning: ~10 minutes; poll status.
- Pure VPN egress pattern:
  - Combine WGW + IGW.
  - On each peer, set DNS (e.g., 8.8.8.8) and include 0.0.0.0/0 in AllowedIPs so default traffic exits via IGW; you should observe the IGW’s public IP as your external address.
- Costs: $50 MRC per IGW. Traffic not metered during beta; will be metered at GA.
- Guide: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- API reference: https://developers.telnyx.com/api-reference/public-internet-gateways/create-a-public-internet-gateway

### Private Wireless Gateway (PGW)
- What it is: A private packet core for Telnyx SIMs—segments, routes, and concentrates mobile traffic.
- Create: POST /v2/private_wireless_gateways with network_id, name, region_code.
- Coverage: As of the cited guide, Ashburn, VA (“ashburn-va”) is supported; more sites are coming. Check coverage for private_wireless_gateway.
- Provisioning: ~15 minutes; poll status.value to transition to provisioned.
- SIMs: Attach SIMs to a SIM Group, then attach the group to the PGW in Mission Control; PGW exposes an IP range (e.g., 100.64.199.0/24).
- Compositions:
  - PGW + WGW for private segmented access to resources over VPN.
  - PGW + WGW + IGW adds internet reachability for devices.
  - PGW + WGW + IGW + VXC extends into a cloud VPC via private circuits (see constraints below).
- Costs: $100 MRC per PGW; SIM and data usage billed separately (pricing: https://developers.telnyx.com/docs/iot-sim/iot-pricing).
- Guide: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- API reference: https://developers.telnyx.com/api-reference/private-wireless-gateways/create-a-private-wireless-gateway

## Virtual Cross Connects (VXC) At A Glance
- What it is: A private Layer 2/Layer 3 connection between Telnyx and a supported cloud provider region (e.g., AWS).
- Plan with both coverage APIs:
  - Confirm Telnyx site offers virtual_cross_connect in /v2/network_coverage.
  - Validate cloud-provider pairings and bandwidth options via /v2/virtual_cross_connects_coverage.
- Bandwidth options are returned per pairing (available_bandwidth in Mbps).
- VXC guides: https://developers.telnyx.com/docs/network/vxc/intro

## Common Architectures
- Multi-cloud VPN with WGW
  - Place peers in different clouds (e.g., AWS + DigitalOcean), connect both to a WGW, and route over the Wireguard subnet—no public exposure required.

- Private access to Telnyx APIs/SIP/Storage via WGW
  - Create WGW with enable_sip_trunking; update peers’ AllowedIPs to include the provided Telnyx routes so traffic to api.telnyx.com, sip.telnyx.com, and *.telnyxcloudstorage.com traverses the Telnyx backbone.

- WGW + IGW “pure VPN” egress
  - Add IGW to the same network; set peers’ DNS and AllowedIPs=… , 0.0.0.0/0; peers will egress to the internet with the IGW’s public IP.

- PGW + WGW
  - Segment SIM traffic on PGW and privately reach admin and internal-service peers via WGW; ensure AllowedIPs include both the WGW and PGW subnets on peers.

- PGW + WGW + IGW
  - Add IGW to give devices both private (WGW/PGW) and internet reachability; cross-site placements can add latency.

- PGW + WGW + IGW + VXC
  - Extend into a cloud VPC over VXC; as noted in the guide, this combination currently requires WGW, IGW, and VXC at the Frankfurt site; broader coverage is in progress.

## Wireguard Peer Setup Quickstart
- Linux
  - Install: sudo apt install wireguard
  - Bring up: place config at /etc/wireguard/<name>.conf, then sudo wg-quick up <name>
  - Verify: sudo wg show and ping other peers over the Wireguard subnet.

- macOS
  - Install the official Wireguard client from https://www.wireguard.com/install/
  - Import the .conf and Activate; verify you can reach other peers.

- Windows
  - Install the Windows Wireguard client from https://www.wireguard.com/install/
  - Import the .conf and Activate; verify by pinging or run a simple test service and curl it from the other peer.
