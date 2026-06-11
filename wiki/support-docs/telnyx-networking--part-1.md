---
title: Telnyx Networking
summary: Telnyx Networking provides private, direct cloud interconnections via Virtual
  Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It
  supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity,
  and offers Global Edge Router for BGP-anycast failover across 25+ points of presence
  with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.
sources:
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
  content_hash: 38e8fb4b062ccf333a01a85a5c55cf64f2a1ce8797170dd06db9a09bca43e0c4
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
  content_hash: 81d586d17af9f2151be09fe3f9289dbf02e7e4d2f7cce377254f924862d1dab0
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
  content_hash: 726d23e81b11439d8039430039f438f3503381e9c4b88908f52211bfe4fac4e3
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
  content_hash: 137fa43047fbd7d22d781b409a0e2a2f4e387aa94a2488b9a518216f906c661e
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
  content_hash: 4b3912e5814e8f4b2dbdc10c3384690d65381edc57c55b911479a2ebdb2e8c54
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
  content_hash: 2373069f1cef6255f3f94a0f33b392d1203ec69ff2e4d094023d76d0a7d43c10
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
  content_hash: c37bb3e5d49609b5635ede08b2a2c669160584424a75cc36e4a4c8075b36c10d
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
  content_hash: b538845e2550e649d97c28739b2be8b6debe089aeffcdf227abdbf3dd639a43e
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
  content_hash: b0f1c9dc3d23558e86f3c597cdd2f145310ebe46847582ce216344f006211aac
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
  content_hash: 2f499dc9b50c9eebb60bb8ac8698ab06cb039f5328292ed78ac9660a23753a17
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
  content_hash: ef6618967bf0d5287c1ff2e058d8044aa93fb5fa777ede9f83164b663117aff8
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
  content_hash: fe7493e7086d57112ec02adfe56ec3c410defb86328adbad1fb63a472707d948
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
  content_hash: 3e9f78a1f33849dd29e047c5fb0f6c2e549d80e10ad1904e74dc4fe60719a306
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
  content_hash: 469c54c3c55c87e20370fc3fb2b6b1e02871b93ee3bf1fd9c072ab1585951dad
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
  content_hash: c6bb4e02ed9f4a7193d32bed3c1d18687c43ffd311fddb57cece9f865b3b245e
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
  content_hash: ecb3d37aecd93e9912ae01c3a43a967b45c015bcf792ebe7e0e38c0f5ee06878
updated_at: 2026-06-11T11:41:32Z
---

# Telnyx Networking

*Part 1 of 4 — see also: [Part 2](telnyx-networking--part-2.md), [Part 3](telnyx-networking--part-3.md), [Part 4](telnyx-networking--part-4.md)*

Telnyx Networking provides private, direct cloud interconnections via Virtual Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity, and offers Global Edge Router for BGP-anycast failover across 25+ points of presence with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.

Telnyx Networking encompasses two primary connectivity models: **Virtual Cross Connects (VXCs)**, which establish private, direct Layer 3 connections between cloud providers and the Telnyx backbone; and **Global Edge Router / Cloud VPN**, which uses WireGuard tunnels to provide BGP-anycast edge routing, Global IPs, and encrypted VPN connectivity across a global network of 25+ points of presence (PoPs). Both approaches bypass the public internet to reduce hops, packet loss, and jitter while adding the security of direct interconnection. Telnyx recommends encrypting both signaling and media with TLS and Z/SRTP to protect against man-in-the-middle attacks.
