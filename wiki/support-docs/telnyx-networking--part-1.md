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

*Part 1 of 4 — see also: [Part 2](telnyx-networking--part-2.md), [Part 3](telnyx-networking--part-3.md), [Part 4](telnyx-networking--part-4.md)*

Telnyx Networking provides private, direct cloud interconnections via Virtual Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity, and offers Global Edge Router for BGP-anycast failover across 25+ points of presence with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.

Telnyx Networking encompasses two primary connectivity models: **Virtual Cross Connects (VXCs)**, which establish private, direct Layer 3 connections between cloud providers and the Telnyx backbone; and **Global Edge Router / Cloud VPN**, which uses WireGuard tunnels to provide BGP-anycast edge routing, Global IPs, and encrypted VPN connectivity across a global network of 25+ points of presence (PoPs). Both approaches bypass the public internet to reduce hops, packet loss, and jitter while adding the security of direct interconnection. Telnyx recommends encrypting both signaling and media with TLS and Z/SRTP to protect against man-in-the-middle attacks.
