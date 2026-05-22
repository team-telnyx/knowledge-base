---
title: 'Telnyx Networking with WireGuard: Multi-platform Setup'
summary: A consolidated guide to deploy Telnyx Networking (Cloud VPN/Edge Routing)
  with WireGuard across Linux servers, AWS (Lightsail and EC2/VPC), Azure VMs, Oracle
  Cloud, pfSense, and Android/iOS. It covers required Telnyx objects, client configuration,
  platform-specific nuances, and simple ways to test connectivity.
sources:
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
  content_hash: 254bf5e167fa9003070f942bc4bb4a211beff4fd9f91b6a9a67edf7481d68312
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
  content_hash: 1ee16c0d7fc1679bbc38742d9ebe1e41f21ed643893e18f44908dc2cce4c355b
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
  content_hash: ffb5539922fb3477e239a904d7009910166a595be0a3270861d9c3c939844026
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
  content_hash: 3cbd2b05629c7b6ef01df5757a7918593141d76c5fe90b5d9a9b3b8056e8b133
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
  content_hash: 6eb5ebb4bfcd656562b3af1c4b1f3813d5179a9ca8c05e2b3f34900d7071e1bf
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
  content_hash: 8bfad25c1e5317063aeff4dfa3bc75d4a10a4ab10a2da0380bd9fb0b05ea9bf7
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
  content_hash: bc6d354532f640d44777442cb4a1c31cc50c5b08a1b07014d195a1a8cc25d3e5
updated_at: 2026-05-20T15:24:02Z
---

# Telnyx Networking with WireGuard: Multi-platform Setup

*Part 2 of 2 — see also: [Part 1](telnyx-networking-with-wireguard-multi-platform-setup--part-1.md)*

A consolidated guide to deploy Telnyx Networking (Cloud VPN/Edge Routing) with WireGuard across Linux servers, AWS (Lightsail and EC2/VPC), Azure VMs, Oracle Cloud, pfSense, and Android/iOS. It covers required Telnyx objects, client configuration, platform-specific nuances, and simple ways to test connectivity.

## pfSense firewall specifics
- Install the WireGuard package in pfSense.
- Configure VPN > WireGuard:
  - Add a Tunnel (e.g., telnyx_wg), paste the Private Key from your Telnyx WireGuard Peer into Interface Keys.
  - Add a Peer, uncheck Dynamic Endpoint, and paste the Endpoint, Public Key, and Allowed IPs from the Telnyx Peer.
- Assign the WireGuard tunnel as an Interface (Interfaces > Assignments), set IPv4 Configuration Type to Static IPv4, and set the IPv4 address to the Interface Address provided in your Telnyx peer configuration (use /16 mask as shown in the guide).
- NAT configuration:
  - 1:1 NAT on the WireGuard interface: External subnet = WireGuard interface address; Internal IP = your service VM IP.
  - Outbound NAT: Interface = WAN (or where your VM listens), translate to Interface Address (adjust protocols/scope as desired).
- Note from the guide: at this stage, only ports 80/443 are supported (subject to change in future updates per the source).

## Android and iOS mobile clients
- Install WireGuard for Android (Google Play) or iOS (App Store).
- Tap + to add a tunnel, then import/paste the Telnyx-provided configuration (insert your private key if not already present).
- Toggle the tunnel on and verify status.

## Starting, enabling, and testing the tunnel
- Bring the interface up on Linux:
```
sudo wg-quick up wg0
```
- Show status:
```
sudo wg show
```
- Enable at boot (systemd):
```
sudo systemctl enable wg-quick@wg0
```
- Test reachability by pinging the Telnyx interface server_ip_address shown when creating the WireGuard Interface (example):
```
ping 172.27.1.17
```
- In the Telnyx portal (Networking > Cloud VPN/Edge Router), check that Last Seen updates for your peer.

## Troubleshooting tips and port notes
- UDP ports: the examples use common WireGuard ports such as 51280 and 51820. Use the port present in your configuration and allow it in any host/cloud firewall where required.
- IP forwarding: if this host will route traffic for other devices, enable net.ipv4.ip_forward=1 and use MASQUERADE as shown.
- AWS EC2: when routing for other subnets, consider disabling source/destination checks on the WireGuard instance per the example.
- Oracle Cloud: use the helper scripts to address NAT/routing quirks.
- AllowedIPs: ensure they include your Telnyx interface subnet and any additional networks you plan to route.
- Keepalive: PersistentKeepalive helps peers behind NATs maintain connectivity.
- WireGuard installation references: https://www.wireguard.com/install/
