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
