---
title: Telnyx Programmable Networking
summary: Telnyx Programmable Networking provides private, high-performance connectivity
  between your infrastructure and Telnyx SIP, API, and storage endpoints without traversing
  the public internet. It is built around networks, gateways (Wireguard, Internet,
  Private Wireless), and Virtual Cross Connects, all managed via the Telnyx API.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
  content_hash: e560141acf3c980660a17d208e8fa7a02bf9f3da3e800be58d3cb1e2b1c4de3c
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
  content_hash: f5c352ce452482ce3541e2b867a08a74e9addad8a95ef29ed539297ac5994ef8
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
  content_hash: 552d19a05c1066b8c41bec822602cfa8b063a207d539b6b4be07ba49a437045f
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
  content_hash: 804d52f680f2d0f4fe5aca8040d9cf279558832ce9b0f717b887199ac6f22365
- url: https://developers.telnyx.com/docs/network/networks
  content_hash: 7c53f682c8fa4357cdfe59588b1963c4b7b90f994c26753e5cfe860d8fbd0a34
- url: https://developers.telnyx.com/docs/network/overview/index
  content_hash: b86e23574be1b400af97a7c92a76eddc57e1f3238fdf54b057f55473968c14e6
- url: https://developers.telnyx.com/docs/network/vxc/api
  content_hash: fa19a1191d6fbe7b713db0237d924066d091e0a61ed30bac7a63eb063721d539
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
  content_hash: 7534f09db65a277e88534c363dcbec0b4823a9c7148eca6b0fd027770f65437e
updated_at: 2026-06-11T10:37:56Z
---

# Telnyx Programmable Networking

*Part 2 of 2 — see also: [Part 1](telnyx-programmable-networking--part-1.md)*

Telnyx Programmable Networking provides private, high-performance connectivity between your infrastructure and Telnyx SIP, API, and storage endpoints without traversing the public internet. It is built around networks, gateways (Wireguard, Internet, Private Wireless), and Virtual Cross Connects, all managed via the Telnyx API.

## Virtual Cross Connects (VXC)

A VXC is a virtual direct connection between a supported cloud provider and Telnyx. It is analogous to AWS Direct Connect.

The API resource is `POST /v2/virtual_cross_connects`. Common parameters regardless of cloud provider:

| Parameter | Value |
| --- | --- |
| `network_id` | Must be associated with an existing network |
| `name` | Human-readable label |

Additional parameters are cloud-provider-specific. For AWS, these include `cloud_provider`, `cloud_provider_region`, `primary_cloud_account_id`, `bgp_asn`, and `bandwidth_mbps`.

### AWS VXC Setup

**Prerequisites (on AWS):**

- **VPC** — Create in the intended region (e.g. `eu-central-1`) with an RFC1918 CIDR block.
- **Virtual Private Gateway** — Create and attach to the VPC. Note the default Amazon ASN (64512), needed for VXC creation.
- **VPC Route Table** — Configure route propagation for the virtual private gateway.
- **Internet Gateway** (optional) — Create and attach for public internet access from the VPC.
- **Subnet** — Within the VPC CIDR block.
- **EC2 Instance** — In the same region/VPC/subnet; enable public IP for SSH access.
- **AWS Account ID** — Needed as `primary_cloud_account_id` when creating the VXC.

**Procedure:**

1. **Create the VXC resource** on Telnyx via `POST /v2/virtual_cross_connects` with the AWS-specific parameters. The `bandwidth_mbps` value must be chosen from the VXC coverage API's `available_bandwidth` list.
2. **Accept the Direct Connect** on AWS within 1 hour of creation, otherwise the VXC is deleted.
3. **Enable the primary connection** on Telnyx via `PATCH /v2/virtual_cross_connects/{vxc_uuid}` with `{"primary_enabled": true}`.
4. **Create a Virtual Interface** on AWS: type Private, select the Direct Connection, Gateway Type = Virtual Private Gateway, BGP ASN = 63440 (Telnyx's ASN), and fill in the peer IPs and BGP key from the VXC details.
5. **Validate the connection** — SSH into the EC2 instance and traceroute to verify traffic flows over the VXC.

## Use Cases

### Multi-Cloud Network (WGW only)

A WGW can serve as a VPN concentrator connecting peers across different cloud providers. For example, an EC2 instance in AWS and a Droplet in DigitalOcean — both unreachable from the public internet due to restrictive firewall rules — can communicate over the Wireguard subnet. By connecting both as peers to the same WGW and setting `AllowedIPs = 172.27.0.0/24`, each peer can reach the other via the Wireguard private IP.

### Private Access to Telnyx Services (WGW with SIP trunking)

If a WGW is created with `enable_sip_trunking: true`, routing to all Telnyx public API, SIP, and storage endpoints is enabled. Additional routes for Telnyx service IPs are added to `AllowedIPs` in the peer config. Traffic from the peer to `sip.telnyx.com`, `api-direct.telnyx.com`, and `*.telnyxcloudstorage.com` then flows through the WGW, entirely bypassing the public internet. This is useful for locking down public routing during events like DDoS attacks.

### Pure-Play VPN (IGW + WGW)

An IGW combined with a WGW creates a simple VPN service. On the Wireguard peer config, set `DNS` to a resolver (e.g. `8.8.8.8`) and append `0.0.0.0/0` to `AllowedIPs` so reachability extends beyond the private subnet. After reactivating the tunnel, the peer's outbound traffic exits via the IGW's public IP.

### PWG + WGW

This architecture is useful when SIM traffic must be segmented and private but does not require high bandwidth to internal services. On each Wireguard peer, include both the WGW subnet and the PGW subnet in `AllowedIPs`:

```
[Peer]
PublicKey = XXX
AllowedIPs = 172.27.0.0/24, 100.64.199.0/24
```

The SIM-connected device can then reach internal service peers, and vice versa, via the PGW's private IP range.

### PWG + WGW + IGW

Adding an IGW to the PWG+WGW architecture provides internet reachability to SIM devices. The device's default gateway IP is that of the PGW, while its external IP is the IGW's public IP. This avoids the need for a peer-based exit node workaround.

### PWG + WGW + IGW + VXC

When internal services reside in a cloud provider, a VXC can be added to the network. Currently, the PWG + WGW + IGW + VXC combination only works when the WGW, IGW, and VXC are at the Frankfurt site. The VXC advertises the PGW's SIM private IP ranges into the cloud provider's VPC route table, enabling direct private connectivity from cloud-hosted resources (e.g. an EC2 instance) to SIM devices. Inbound rules on the cloud side must allow traffic from the SIM subnet.

### Cross-Region Network

Multiple WGWs in different Telnyx sites can be connected, allowing peers in different regions to communicate over the Telnyx backbone rather than the public internet.

## Common Provisioning Notes

- All gateway types and VXC resources enter a `provisioning` state upon creation and must be polled until they reach `provisioned`.
- Typical provisioning times: WGW ~5 min, IGW ~10 min, PGW ~15 min.
- Gateways cannot be migrated between networks after creation — they must be recreated on the target network.
