---
title: Telnyx Programmable Networking Overview
summary: 'A single overview of Telnyx programmable networking: how to privately reach
  Telnyx SIP, API, and Storage over Telnyx’s backbone; the building blocks (coverage,
  networks, gateways, VXC); common architectures; provisioning timelines; pricing;
  and key API endpoints.'
sources:
- url: https://developers.telnyx.com/docs/network/overview/index
- url: https://developers.telnyx.com/docs/network/coverage
- url: https://developers.telnyx.com/docs/network/networks
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
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
