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

*Part 1 of 2 — see also: [Part 2](telnyx-networking-with-wireguard-multi-platform-setup--part-2.md)*

A consolidated guide to deploy Telnyx Networking (Cloud VPN/Edge Routing) with WireGuard across Linux servers, AWS (Lightsail and EC2/VPC), Azure VMs, Oracle Cloud, pfSense, and Android/iOS. It covers required Telnyx objects, client configuration, platform-specific nuances, and simple ways to test connectivity.

## What you’ll build
Set up a WireGuard-based tunnel that connects your device or server to the Telnyx network. You’ll create Telnyx networking objects (Network, WireGuard Interface, WireGuard Peer), apply the generated peer configuration on your platform, and verify end-to-end reachability to the Telnyx interface IP.

## Prerequisites and Telnyx-side setup
- Telnyx account and API key.
- A Telnyx Network created (optional via API example below).
- A WireGuard Interface in a Telnyx region and at least one WireGuard Peer. You’ll download the peer configuration from Telnyx and add your private key to it.

API examples (as shown in the docs):

Create a Network
```
curl --request POST \
  --url https://api.telnyx.com/v2/networks \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "Test Network"
}'
```

Create a WireGuard Interface (example)
```
curl -i -X POST \
  https://api.telnyx.com/v2/wireguard_interfaces \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "network_id": "<NETWORK_ID_HERE>",
    "name": "test interface",
    "region_code": "ashburn-va"
  }'
```
Example response fields include: endpoint (e.g., 64.16.243.3:<port>) and server_ip_address (e.g., 172.27.1.17/29).

Create a WireGuard Peer (example)
```
curl -i -X POST \
  https://api.telnyx.com/v2/wireguard_peers \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "wireguard_interface_id": "<WIREGUARD_INTERFACE_ID_HERE>"
  }'
```

## Retrieve your Telnyx peer configuration
- From the Telnyx portal (Networking > Cloud VPN/Edge Router), copy the Peer Configuration that includes the Interface and Peer sections.
- Or via API (example from docs):
```
curl -X GET \
 --header "Content-Type: application/json" \
 --header "Accept: application/json" \
 --header "Authorization: Bearer YOUR_API_KEY" \
 https://api.telnyx.com/v2/<WIREGUARD_PEER_ID>/Config
```
You will insert your private key into the returned configuration and save it as a .conf file (e.g., /etc/wireguard/wg0.conf).

## Common WireGuard configuration template
Use the template below and replace placeholders with values from your Telnyx peer configuration and keys you generated on your device:
```
[Interface]
Address = <your_assigned_peer_ip/cidr>
PrivateKey = <your_private_key>
# Optional NAT if this node will route/masquerade traffic from LANs behind it
PostUp   = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
# ListenPort is optional for many client-only scenarios; use if your config specifies it
ListenPort = <51280_or_51820_if_required>

[Peer]
PublicKey  = <telnyx_interface_public_key>
Endpoint   = <telnyx_endpoint_ip:port>
AllowedIPs = <ip/cidr_from_config>
# Recommended when behind NATs
PersistentKeepalive = 25
```
Notes:
- Address is the peer IP assigned by Telnyx (often /32).
- Endpoint and AllowedIPs come from the Telnyx peer configuration.
- If you will route other networks via this peer, add those networks to AllowedIPs as documented.

## Linux servers (generic Ubuntu/Debian)
- Install WireGuard:
```
sudo apt update && sudo apt install wireguard -y
```
- (Optional) Generate keys if you are not using keys from Telnyx steps:
```
wg genkey | tee privatekey | wg pubkey > publickey
cat privatekey
cat publickey
```
- Enable IPv4 forwarding if this host will route traffic:
```
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/10-wireguard.conf
sudo sysctl -p /etc/sysctl.d/10-wireguard.conf
```
- Save your config to /etc/wireguard/wg0.conf and bring the interface up:
```
sudo wg-quick up wg0
```
- Enable at boot (systemd hosts):
```
sudo systemctl enable wg-quick@wg0
```

## AWS Lightsail specifics
- Create a Linux/Unix instance (e.g., Ubuntu 20.04 LTS) and note its public IP.
- In the instance Networking tab, add a Custom UDP firewall rule for port 51820 (per the guide), and remove unneeded HTTP if not used.
- SSH using your Lightsail key, install WireGuard, and enable IPv4 forwarding as shown above.
- Place the Telnyx-provided peer config into /etc/wireguard/wg0.conf and start the service:
```
sudo systemctl start wg-quick@wg0
sudo systemctl enable wg-quick@wg0
```

## AWS EC2 in a VPC specifics
- Install tools:
```
sudo apt update && sudo apt install wireguard-tools -y
```
- If routing traffic through the instance, you may need to disable source/destination check on the EC2 instance:
```
aws ec2 modify-instance-attribute --no-source-dest-check --instance-id <instance-id>
```
- Example wg0.conf pattern (from guide):
```
[Interface]
PrivateKey = <this_machine_private_key>
Address    = <wg_interface_ip/cidr>
PostUp     = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown   = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = 51280

[Peer]
PublicKey  = <telnyx_public_key>
AllowedIPs = <peer_wg_ip_or_additional_CIDRs>
PersistentKeepalive = 1
```
Notes from the guide:
- NAT (PostUp/PostDown) presents VPN traffic as originating from the instance.
- Add additional CIDRs to route more networks across the tunnel as needed.

## Azure Linux VM specifics
- Create an Azure Linux VM, SSH in, install WireGuard:
```
sudo apt update
sudo apt install wireguard
```
- Edit /etc/wireguard/wg0.conf with the Telnyx configuration, then bring up the interface:
```
sudo wg-quick up wg0
```

## Oracle Cloud VM specifics
- Create an Oracle Compute instance and install WireGuard.
- Example wg0.conf base (from guide):
```
[Interface]
PrivateKey = <this_machine_private_key>
Address    = <wg_interface_ip/cidr>
PostUp     = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown   = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = 51280

[Peer]
PublicKey  = <telnyx_public_key>
AllowedIPs = <peer_wg_ip_or_additional_CIDRs>
PersistentKeepalive = 1
```
- Oracle-specific NAT/routing fix: add these to wg0.conf instead of the basic PostUp/Down lines:
```
PostUp = /etc/wireguard/helper/add-nat-routing.sh
PostDown = /etc/wireguard/helper/remove-nat-routing.sh
```
Create the helper scripts (ensure execute permissions) at /etc/wireguard/helper/:

add-nat-routing.sh
```
#!/bin/bash
IPT="/sbin/iptables"
IPT6="/sbin/ip6tables"
IN_FACE="ens3"
WG_FACE="wg0"
SUB_NET="10.66.66.0/24"
WG_PORT="59075"
SUB_NET_6="fd42:42:42::/64"
$IPT -t nat -I POSTROUTING 1 -s $SUB_NET -o $IN_FACE -j MASQUERADE
$IPT -I INPUT 1 -i $WG_FACE -j ACCEPT
$IPT -I FORWARD 1 -i $IN_FACE -o $WG_FACE -j ACCEPT
$IPT -I FORWARD 1 -i $WG_FACE -o $IN_FACE -j ACCEPT
$IPT -I INPUT 1 -i $IN_FACE -p udp --dport $WG_PORT -j ACCEPT
# IPv6 (uncomment to use)
$IPT6 -t nat -I POSTROUTING 1 -s $SUB_NET_6 -o $IN_FACE -j MASQUERADE
$IPT6 -I INPUT 1 -i $WG_FACE -j ACCEPT
$IPT6 -I FORWARD 1 -i $IN_FACE -o $WG_FACE -j ACCEPT
$IPT6 -I FORWARD 1 -i $WG_FACE -o $IN_FACE -j ACCEPT
```

remove-nat-routing.sh
```
#!/bin/bash
IPT="/sbin/iptables"
IPT6="/sbin/ip6tables"
IN_FACE="ens3"
WG_FACE="wg0"
SUB_NET="10.66.66.0/24"
WG_PORT="59075"
SUB_NET_6="fd42:42:42::/64"
$IPT -t nat -D POSTROUTING -s $SUB_NET -o $IN_FACE -j MASQUERADE
$IPT -D INPUT -i $WG_FACE -j ACCEPT
$IPT -D FORWARD -i $IN_FACE -o $WG_FACE -j ACCEPT
$IPT -D FORWARD -i $WG_FACE -o $IN_FACE -j ACCEPT
$IPT -D INPUT -i $IN_FACE -p udp --dport $WG_PORT -j ACCEPT
# IPv6 (uncomment to use)
$IPT6 -t nat -D POSTROUTING -s $SUB_NET_6 -o $IN_FACE -j MASQUERADE
$IPT6 -D INPUT -i $WG_FACE -j ACCEPT
$IPT6 -D FORWARD 1 -i $IN_FACE -o $WG_FACE -j ACCEPT
$IPT6 -D FORWARD 1 -i $WG_FACE -o $IN_FACE -j ACCEPT
```
This works around Oracle’s default NAT/routing behavior so the WireGuard peer functions correctly.
