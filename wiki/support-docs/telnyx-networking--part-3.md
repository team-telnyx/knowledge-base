---
title: Telnyx Networking
summary: Telnyx Networking provides private, direct cloud interconnections via Virtual
  Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It
  supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity,
  and offers Global Edge Router for BGP-anycast failover across 25+ points of presence
  with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.
sources:
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
updated_at: 2026-06-11T11:41:32Z
---

# Telnyx Networking

*Part 3 of 4 — see also: [Part 1](telnyx-networking--part-1.md), [Part 2](telnyx-networking--part-2.md), [Part 4](telnyx-networking--part-4.md)*

Telnyx Networking provides private, direct cloud interconnections via Virtual Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity, and offers Global Edge Router for BGP-anycast failover across 25+ points of presence with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.

## Global Edge Router

The [Telnyx Global Edge Router](https://telnyx.com/products/global-edge-router) provides access to a global edge network of 25+ PoPs to decrease latency for applications and services. It uses WireGuard VPN tunnels and BGP-anycast to dynamically advertise a single Global IP across multiple edge PoPs, providing automatic redundancy and failover across cloud providers.

### Benefits and Use Cases

**Compared to typical DNS-based routing:** When using DNS servers with static IPs, a server failure causes clients to time out until DNS records update, creating a poor experience. The Global Edge Router instead uses BGP-anycast to dynamically advertise a single Global IP; if a server goes down, traffic is automatically rerouted to a working server in seconds.

**Multi-cloud and self-hosted environments:** The Edge Router supports Microsoft Azure, AWS, Google Cloud, and IBM Softlayer. It provides:
- **Increased cloud redundancy** — no single-provider dependency
- **Increased cloud flexibility** — use the best features from each provider
- **Controlled cloud costs** — negotiate and reduce cloud spend by diversifying providers

**Key use cases:**
- **Migrations** — seamlessly transition between cloud providers or from cloud to hybrid/self-hosted without performance degradation
- **Mergers and Acquisitions** — mesh different technology platforms to share resources, utilize new feature sets, or migrate between providers
- **Siloed Lines of Business** — consolidate redundant operations across departments using different vendors
- **IoT and Wireless SIMs** — control IoT and wireless data end-to-end using Telnyx global carrier partnerships and the edge network
- **Mid-Market Enterprise Cost Savings** — diversify cloud portfolio while maintaining automatic failover, global coverage, and flat costs

**Pricing:** One low monthly recurring cost based on the selected bandwidth tier, starting at $5/month. There is no data cap on transmitted and received data. See the [Global Edge Router pricing page](https://telnyx.com/pricing/global-edge-router) for current rates.

### Global Edge Router Setup

> **Note:** Global IP for customers is currently disabled with no plans to re-enable it in the near future. The following steps document the full setup process for when it is available.

The setup process follows eight steps:

**Step 1 — Create a Network:** Sign into the Mission Control Portal, navigate to **Networking**, and click **Create Network**. Name the network and click **Create**.

**Step 2 — Create a WireGuard Interface:** Select **Cloud VPN** in the top menu and click **Create VPN Interface**. Enter a name and select a Network and region.

**Step 3 — Wait for provisioning:** The WireGuard interface takes a few minutes to provision (refresh the page to see the "provisioned" status).

**Step 4 — Create a WireGuard Peer:** Click the edit icon on the VPN interface, scroll to the **Peers** section, and select **Add new peer**. Name the peer, optionally provide your own public key, and click **Create Peer**.

**Step 5 — Copy the Private Key:** After peer creation, copy the returned private key.

**Step 6 — Acquire a Global IP:** In the **Networking** tab, select **Global IP** in the top menu, click **Buy Global IP**, name the IP, add a description, select a Tier, and click **Buy Global IP**. Pricing is based on port capacity, not egress.

**Step 7 — Assign the WireGuard Peer to the Global IP:** Click on the new Global IP, select **Assign new peer**, choose the WireGuard Peer, and click **Assign Peer**.

**Step 8 — Copy the WireGuard configuration:** Using the private key from Step 5, paste the WireGuard configuration onto the service VM.
