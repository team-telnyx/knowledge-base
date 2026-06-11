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

*Part 4 of 4 — see also: [Part 1](telnyx-networking--part-1.md), [Part 2](telnyx-networking--part-2.md), [Part 3](telnyx-networking--part-3.md)*

Telnyx Networking provides private, direct cloud interconnections via Virtual Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity, and offers Global Edge Router for BGP-anycast failover across 25+ points of presence with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.

## Cloud VPN / WireGuard Platform Guides

All platform-specific guides follow a common pattern: first complete the Telnyx-side configuration (create a Network, WireGuard Interface, WireGuard Peer, and optionally a Global IP), then configure the WireGuard client on the target platform using the peer configuration file and private key.

The peer configuration file follows this template:

```
[Interface]
PrivateKey = <peer-private-key>
Address = <server-private-ip-address>

[Peer]
PublicKey = <server-public-key>
Endpoint = <server-public-ip>:<port>
AllowedIPs = <ip/cidr>
PersistentKeepalive = 25
```

After configuration, verify connectivity by checking the "last seen" status in the [Mission Control Portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) or by pinging the Cloud VPN interface's private IP address.

### AWS Lightsail

1. Complete the Telnyx configuration steps and note the peer configuration and private key.
2. Deploy an Ubuntu 20.04 Lightsail VPS (or preferred distribution). Note the public IP.
3. **Configure networking:** In Lightsail, go to the instance's **Networking** section. Remove the HTTP rule, add a Custom UDP rule on port 51820.
4. **SSH into the instance:** Download the SSH key from Account > SSH keys. Connect with `ssh -i ~/Desktop/vpn.cer ubuntu@[PUBLIC_IP_ADDRESS]`.
5. **Enable port forwarding:** Create `/etc/sysctl.d/10-wireguard.conf` with `net.ipv4.ip_forward=1` and apply with `sudo sysctl -p /etc/sysctl.d/10-wireguard.conf`.
6. **Install WireGuard and generate keys:** Run `sudo apt update && sudo apt install wireguard -y`. Generate keys with `wg genkey | tee server.key | wg pubkey > server.pub`.
7. **Create the WireGuard server config:** Create `wg0.conf` in `/etc/wireguard/` with the configuration from Step 1. Enable and start the service with `sudo systemctl enable wg-quick@wg0` and `sudo systemctl start wg-quick@wg0`.
8. **Test:** Verify via the portal or by pinging the Global IP.

### AWS VPC

1. Complete the Telnyx configuration steps and note the peer configuration.
2. **Install WireGuard:** Run `apt install wireguard-tools`. Disable source/destination checks on the EC2 instance: `aws ec2 modify-instance-attribute --no-source-dest-check --instance-id <instance-id>`.
3. **Configure WireGuard:** Create `/etc/wireguard/wg0.conf` with the peer configuration. The configuration uses NAT (`PostUp`/`PostDown` iptables rules with MASQUERADE) so that VPN traffic appears to originate from the VPN instance, eliminating the need to update routing tables. Include `PersistentKeepalive = 1` if client devices are behind NAT. Specify additional CIDRs in `AllowedIPs` to route other VPC addresses through the connection.
4. **Test:** Verify via the portal or by pinging the Global IP.

### Azure Linux VMs

1. Complete the Telnyx configuration steps and note the peer configuration.
2. **Create an Azure Linux VM** and SSH into it.
3. **Install WireGuard:** Run `sudo apt update && sudo apt install wireguard`. Open `/etc/wireguard/wg0.conf` and paste the configuration from Step 1. Save and quit.
4. **Test:** Run `sudo wg-quick up wg0` and verify via the portal or by pinging the Global IP.

### Ubuntu (Digital Ocean)

1. **Install WireGuard** on the server: `sudo apt install wireguard`.
2. **Generate keys:** Run `wg genkey | tee privatekey | wg pubkey > publickey`. Print both with `cat privatekey` and `cat publickey`.
3. **Create a Cloud VPN Interface** via the Telnyx API (`POST /v2/wireguard_interface`) with your API key, network ID, region code, and name. Note the `server_ip_address` from the response.
4. **Create a Cloud VPN Peer** via the Telnyx API (`POST /v2/wireguard_peers`) with the interface ID, name, and the `public_key` from Step 2.
5. **Retrieve the peer configuration** via the Telnyx API (`GET /v2/{peer_id}/Config`). Add the private key to the configuration file. Save it as `/etc/wireguard/wg0.conf`.
6. **Bring up the interface:** Run `sudo wg-quick up wg0`.
7. **Test:** Run `sudo wg show` and `ping <server_ip_address>` (the private IP from Step 3).

### Oracle VMs

1. Complete the Telnyx configuration steps and note the peer configuration.
2. **Create an Oracle Cloud Compute Instance** with WireGuard installed.
3. **Configure WireGuard:** Create `/etc/wireguard/wg0.conf` with the peer configuration, including NAT `PostUp`/`PostDown` rules and `PersistentKeepalive = 1`.
4. **Apply Oracle-specific NAT and routing fixes:** Oracle Cloud blocks WireGuard traffic by default due to NAT configuration. Update `wg0.conf` to use custom scripts:
   - `PostUp = /etc/wireguard/helper/add-nat-routing.sh`
   - `PostDown = /etc/wireguard/helper/remove-nat-routing.sh`
   - Create these scripts in `/etc/wireguard/helper/` with execute permissions. The `add-nat-routing.sh` script configures iptables/ip6tables rules for POSTROUTING, INPUT, and FORWARD chains on the internet-facing NIC (`ens3`) and WireGuard NIC (`wg0`). The `remove-nat-routing.sh` script removes those rules on service stop.
5. **Test:** Verify via the portal or by pinging the Global IP.

### PfSense

1. Complete the Telnyx configuration steps. Alternatively, use the Telnyx API to create the Network, WireGuard Interface, and WireGuard Peer programmatically.
2. **Configure WireGuard on PfSense:** Navigate to **VPN > Wireguard**, add a new Tunnel (name it, e.g., `telnyx_wg`, paste the Private Key). Add a new Peer with the Endpoint, Public Key, and Allowed IPs from the Telnyx peer configuration (uncheck Dynamic Endpoint).
3. **Set up the interface:** Go to **Interfaces > Assignments**, add the WireGuard tunnel, set IPv4 Configuration Type to Static IPv4, set the address to the Interface Address from the Telnyx configuration with a /16 subnet mask.
4. **Configure 1:1 NAT and Outbound NAT:**
   - **1:1 NAT:** Interface = WireGuard tunnel, External subnet = WireGuard tunnel interface address, Internal IP = your service VM's IP.
   - **Outbound NAT:** Interface = WAN, Address Family = IPv4 + IPv6, Protocol = any, Source = any, Destination = your VM's IP on the interface, Translation address = Interface Address.

> **Note:** Currently only ports 80/443 are supported through the PfSense WireGuard setup.

### Android and iOS

1. Complete the Telnyx configuration steps and note the peer configuration.
2. **Install the WireGuard app** from [Google Play](https://play.google.com/store/apps/details?id=com.wireguard.android) (Android) or the [App Store](https://apps.apple.com/us/app/wireguard/id1441195209) (iOS).
3. **Add a peer:** Tap the **+** button and enter the configuration settings from Step 1.
4. **Test:** Verify via the portal or by pinging the Global IP.

## API-Based Setup

The Telnyx Networking resources can also be managed via the Telnyx API:

- **Create a Network:** `POST https://api.telnyx.com/v2/networks`
- **Create a WireGuard Interface:** `POST https://api.telnyx.com/v2/wireguard_interfaces`
- **Create a WireGuard Peer:** `POST https://api.telnyx.com/v2/wireguard_peers`
- **Retrieve Peer Configuration:** `GET https://api.telnyx.com/v2/{peer_id}/Config`

All API calls require an `Authorization: Bearer YOUR_API_KEY` header and `Content-Type: application/json`.

## Round Robin Routing

Round Robin is a routing method that distributes inbound calls evenly between all IPs in a connection. It provides basic load balancing by sending the first call to IP 1, the second to IP 2, and so on in a repeating cycle.

Key behaviors:
- Load balancing is based on **inbound calls**, not active calls — each IP receives an equal share of new calls regardless of how many active calls it is managing.
- All IPs serve as **failover targets**: if a call to IP 1 fails, it retries IP 2, then IP 3, and so on. The failover order depends on which IP was the initial attempt.
- Round Robin provides both even load distribution and failover using the same set of systems.

To enable Round Robin routing, select it from the **Default Routing Method** dropdown in the **Basic Settings** of your connection.
