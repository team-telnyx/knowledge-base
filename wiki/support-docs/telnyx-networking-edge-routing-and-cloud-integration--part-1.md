---
title: Telnyx Networking, Edge Routing, and Cloud Integration
summary: This page consolidates Telnyx support documentation covering the Telnyx Edge
  Router and Global Edge Routing product, WireGuard-based networking on multiple platforms
  (AWS Lightsail, AWS VPC, Azure, Google Cloud, Android/iOS, Ubuntu, Oracle VMs, pfSense),
  Virtual Cross Connect (VXC) setup for AWS, Azure, and Google Cloud, and general
  account topics such as cancellation policy, post-paid service availability, and
  the Telnyx blog and community resources.
sources:
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
updated_at: 2026-08-05T13:29:11Z
---

# Telnyx Networking, Edge Routing, and Cloud Integration

*Part 1 of 2 — see also: [Part 2](telnyx-networking-edge-routing-and-cloud-integration--part-2.md)*

This page consolidates Telnyx support documentation covering the Telnyx Edge Router and Global Edge Routing product, WireGuard-based networking on multiple platforms (AWS Lightsail, AWS VPC, Azure, Google Cloud, Android/iOS, Ubuntu, Oracle VMs, pfSense), Virtual Cross Connect (VXC) setup for AWS, Azure, and Google Cloud, and general account topics such as cancellation policy, post-paid service availability, and the Telnyx blog and community resources.

## Telnyx Edge Router Overview

The [Telnyx Edge Router](https://telnyx.com/products/global-edge-router) lets you operate in multi-cloud and/or self-hosted environments using Telnyx's global, high-speed, high-bandwidth edge network to connect customers and team members to your applications. It dynamically advertises a single global IP, providing redundancy across 25+ edge Points of Presence (PoPs). In the event of a failure, traffic is rerouted to a working server using BGP Anycast, typically in five seconds or less.

The Edge Router is built on WireGuard, an open-source VPN technology and protocol. WireGuard uses a peer-to-peer model in which every connected device is considered equal and can communicate directly with any other peer. Each peer generates a private/public key pair, exchanges public keys during a handshake, and then encrypts traffic using the recipient's public key. WireGuard operates at the kernel level, encapsulates encrypted packets in UDP, supports dynamic roaming across network changes, and uses periodic keepalive packets to detect unreachable peers.

### Benefits

- **Increased cloud redundancy** — Diversified infrastructure across multiple providers minimizes the risk of data loss and downtime from outages.
- **Increased cloud flexibility** — Multi-cloud lets you choose the best provider per workload and quickly release new features.
- **Controlling cloud costs** — Multi-cloud and self-hosting reduce cloud spend and increase negotiating leverage with vendors.
- **Automatic failover** — BGP Anycast reroutes traffic instantly when a site or provider goes offline.
- **No data caps** — A single low monthly recurring cost based on the maximum speed bandwidth tier, starting at $5 per month. See the [Global Edge Router pricing page](https://telnyx.com/pricing/global-edge-router) for current rates.

### Supported Cloud Vendors

Telnyx Edge Router supports Microsoft Azure, AWS, Google Cloud, and IBM Softlayer.

### Common Use Cases

- **Migrations** — Move from a single cloud provider to multi-cloud, hybrid, or fully self-hosted assets without performance degradation.
- **Mergers and acquisitions** — Mesh different technology platforms to share resources, leverage new feature sets, and migrate between providers.
- **Siloed lines of business** — Consolidate redundant operations across departments that have spun up infrastructure from different vendors.
- **IoT and Wireless SIMs** — Control IoT and wireless data end-to-end using Telnyx global carrier partnerships combined with the global edge network.
- **Mid-market enterprise** — Diversify cloud portfolios and introduce self-hosted infrastructure while maintaining uptime and performance.

For deployment instructions, see [How to configure Global Edge Router with Telnyx](how-to-configure-global-edge-router-with-telnyx.md).

## WireGuard Networking on Individual Platforms

The following platform-specific guides walk through deploying a host, installing WireGuard, and connecting it to the Telnyx Edge Routing network using the Peer Configuration file and private key generated from the [Global IP & Edge Routing](global-ip-edge-routing.md) setup.

### AWS Lightsail

1. **Configure for Telnyx** — Copy the Peer Configuration file and private key from the [Global IP & Edge Routing](global-ip-edge-routing.md) tutorial.
2. **Deploy a Lightsail VPS** — In Amazon Lightsail, click *Create instance*, change the AWS Region and Availability Zone, choose *Linux/Unix* with *Ubuntu 20.04 LTS*, name the instance, and note its public IP address. Any distribution that supports WireGuard will work; see the [WireGuard installation site](https://www.wireguard.com/install/).
3. **Configure networking** — Open the instance's *Networking* tab, delete the HTTP rule, and add a custom UDP rule on port 51820 for WireGuard.
4. **Connect via SSH** — Download the SSH key from the *Account* section, set permissions with `chmod 600`, and connect: `ssh -i ~/Desktop/vpn.cer ubuntu@[PUBLIC_IP_ADDRESS]`.
5. **Enable port forwarding** — Create `/etc/sysctl.d/10-wireguard.conf` containing `net.ipv4.ip_forward=1`, then run `sudo sysctl -p /etc/sysctl.d/10-wireguard.conf`.
6. **Install WireGuard and generate keys** — Run `sudo apt update && sudo apt install wireguard -y`, then generate server and client keys in `/etc/wireguard/`.
7. **Create the WireGuard server configuration** — Create `wg0.conf` with the configuration from Step 1, then enable and start the service with `wg-quick@wg0`.
8. **Test** — Verify the *last seen* status in the [Mission Control Portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) or ping the configured Global IP.

### AWS VPC

1. **Telnyx configuration** — Copy the Peer Configuration file and private key from the [Global IP & Edge Routing](global-ip-edge-routing.md) tutorial.
2. **Install WireGuard** — Run `apt install wireguard-tools`. WireGuard listens on UDP port 51280. If routing traffic through the EC2 instance, disable source/destination checks with the AWS CLI: `aws ec2 modify-instance-attribute --no-source-dest-check --instance-id <instance-id>`.
3. **Configure Telnyx with WireGuard** — Create `/etc/wireguard/wg0.conf` with the `[Interface]` and `[Peer]` sections, including `PostUp`/`PostDown` iptables rules for NAT, `ListenPort = 51280`, and `PersistentKeepalive = 1`. The NAT configuration presents VPN traffic as originating from the VPN instance within the VPC, eliminating the need to disable source/destination checks or update routing tables.
4. **Test** — Verify the *last seen* status in the [Mission Control Portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) or ping the configured Global IP.

### Android and iOS

1. **Telnyx configuration** — Copy the Peer Configuration file and private key from the [Global IP & Edge Routing](global-ip-edge-routing.md) tutorial.
2. **WireGuard setup** — Install the [Android](https://play.google.com/store/apps/details?id=com.wireguard.android) or [iOS](https://apps.apple.com/us/app/wireguard/id1441195209?ls=1) WireGuard client, tap the **+** button, and add the configuration from Step 1.
3. **Test** — Verify the *last seen* status in the [Mission Control Portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) or ping the configured Global IP.
