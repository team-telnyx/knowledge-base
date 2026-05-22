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

*Part 2 of 2 — see also: [Part 1](telnyx-programmable-networking-overview--part-1.md)*

A single overview of Telnyx programmable networking: how to privately reach Telnyx SIP, API, and Storage over Telnyx’s backbone; the building blocks (coverage, networks, gateways, VXC); common architectures; provisioning timelines; pricing; and key API endpoints.

## Operational Notes and Limitations
- Always check coverage before deployment; availability differs by region/site/PoP and by product.
- Network affinity is immutable: WGW/IGW/PGW cannot be migrated between networks.
- Provisioning timelines (approximate): WGW ~5 min; IGW ~10 min; PGW ~15 min.
- Store WGW peer private_key at creation time—it is shown once.
- Regions use human-readable codes (e.g., “ashburn-va”, “frankfurt-de”).
- IGW is in beta; traffic unmetered for now and will be metered at GA.
- Some multi-element topologies (e.g., PGW+WGW+IGW+VXC) currently have site constraints (e.g., Frankfurt only) pending expanded coverage.

## Pricing Summary
- Wireguard Gateway (WGW): $10 MRC per instance; peers are free.
- Internet Gateway (IGW): $50 MRC per instance; traffic unmetered in beta, will be metered at GA.
- Private Wireless Gateway (PGW): $100 MRC per instance; SIM and data charges apply (see pricing guide).

## API Endpoints Reference
- Coverage
  - Generic: GET /v2/network_coverage (guide: https://developers.telnyx.com/docs/network/coverage)
  - VXC: GET /v2/virtual_cross_connects_coverage
- Core resources
  - Networks: POST /v2/networks (API: https://developers.telnyx.com/api-reference/networks/create-a-network)
  - Wireguard Gateway: POST /v2/wireguard_interfaces (API: https://developers.telnyx.com/api-reference/wireguard-interfaces/create-a-wireguard-interface)
  - Wireguard Peers: POST /v2/wireguard_peers; GET /v2/wireguard_peers/{id}/config
  - Internet Gateway: POST /v2/public_internet_gateways (API: https://developers.telnyx.com/api-reference/public-internet-gateways/create-a-public-internet-gateway)
  - Private Wireless Gateway: POST /v2/private_wireless_gateways (API: https://developers.telnyx.com/api-reference/private-wireless-gateways/create-a-private-wireless-gateway)
- VXC guides: https://developers.telnyx.com/docs/network/vxc/intro
