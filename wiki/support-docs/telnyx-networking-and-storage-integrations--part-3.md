---
title: Telnyx Networking and Storage Integrations
summary: This page consolidates Telnyx support documentation covering Megaport network
  integration, Telnyx Storage configuration with third-party S3-compatible clients
  (Cyberduck, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP), and Telnyx Networking
  setup across Global Edge Router, Ubuntu, Azure Linux VMs, Oracle VMs, and pfSense
  using WireGuard-based Cloud VPN.
sources:
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
updated_at: 2026-08-05T13:35:29Z
---

# Telnyx Networking and Storage Integrations

*Part 3 of 5 — see also: [Part 1](telnyx-networking-and-storage-integrations--part-1.md), [Part 2](telnyx-networking-and-storage-integrations--part-2.md), [Part 4](telnyx-networking-and-storage-integrations--part-4.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md)*

This page consolidates Telnyx support documentation covering Megaport network integration, Telnyx Storage configuration with third-party S3-compatible clients (Cyberduck, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP), and Telnyx Networking setup across Global Edge Router, Ubuntu, Azure Linux VMs, Oracle VMs, and pfSense using WireGuard-based Cloud VPN.

## Global Edge Router and Global IP Setup

Telnyx Global Edge Router provides access to a global edge network of 25+ points of presence to decrease latency for nightly-available applications and services, with redundancy across cloud providers via [BGP](https://telnyx.com/resources/what-is-bgp)-anycast.

> **Note:** Global IP for customers is currently disabled. At present there are no plans to re-enable it in the near future.

**Setup steps**

1. **Create your network.** Sign up to the Mission Control Portal and navigate to the **Networking** tab. In the **Networks** section, click **Create Network**, give it a name, and click **Create**.

   ![](_images/1fc7f501f15718c0.png)

2. **Create a WireGuard interface.** Select **Cloud VPN** in the top menu and click **Create VPN Interface**. Enter a name, select a Network and region, and create the interface.

   ![](_images/4d7ecc9d207690e4.png)

3. **Wait for the WireGuard interface to provision.** This typically takes a few minutes; you may need to refresh the page to see the `provisioned` status.

   ![](_images/67511a22e5111892.png)

4. **Create a WireGuard peer.** Click the edit icon on your VPN interface, scroll to the **Peers** section, and select **Add new peer**. Name the peer, choose to use your own public key, and click **Create Peer**.

   ![](_images/10264a1ea71afe67.png)

   ![](_images/0d50fc133cd8e3fa.png)

5. **Copy your new private key.** After peer creation, copy the private key and close the pop-up.

   ![](_images/d02b7939067e65cc.png)

6. **Acquire a Global IP.** In the **Networking** tab, select **Global IP** in the top menu. Click **Buy Global IP**, name it, add a description, and select your Tier. Global IP prices are based on port capacity, not egress fees. Click **Buy Global IP**.

   ![](_images/9957e09047ea1a5c.png)

7. **Assign WireGuard peer to your new Global IP.** Click on your new IP and select **Assign new peer** at the bottom of the page. Choose the WireGuard peer to associate and click **Assign Peer**.

   ![](_images/e34e9fb24ede170c.png)

8. **Copy and paste WireGuard configuration to service VM.** Using the private key from Step 5, paste your WireGuard configuration to your service VM.

   ![](_images/70383a83726099b2.png)

## Telnyx Networking on Ubuntu

This tutorial walks through connecting a Digital Ocean Ubuntu Server via WireGuard to a [Cloud VPN](https://telnyx.com/products/cloud-vpn) interface on the Telnyx network.

**Pre-requisites**

- A Telnyx account, API key, and a Network (see the Networking Quickstart Guide).
- A [Digital Ocean Ubuntu Server](https://docs.digitalocean.com/products/droplets/how-to/create/) with [additional security setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04).

**Step 1: Install WireGuard on the server**

```
sudo apt install wireguard
```

**Step 2: Generate public and private keys**

```
wg genkey | tee privatekey | wg pubkey > publickey
cat privatekey
cat publickey
```

The `private_key` is needed later to build the Cloud VPN peer configuration; the `public_key` is used when creating the Cloud VPN peer.

**Step 3: Create a Cloud VPN Interface**

Create a Cloud VPN Interface associated with the Network you created. This network interface is configured on the Telnyx network and acts as a tunnel interface.

```
curl -X POST \
 --header "Content-Type: application/json" \
--header "Accept: application/json" \
 --header "Authorization: Bearer YOUR_API_KEY" \
--data '{
 "network_id": "7c3c05f4-7d53-4edb-9224-371c6d659cd4",
 "region_code": "ashburn-va",
 "name": "WG_net01_VA_interface01"
 }' \
 https://api.telnyx.com/v2/wireguard_interface
```

Example response:

```
{
"data": {
"status": "provisioning",
"network_id": "7c3c05f4-7d53-4edb-9224-371c6d659cd4",
"id": "9122b687-30aa-47a6-8f64-2b8681476ec2",
"updated_at": "2022-06-13T09:50:54.117345Z",
"created_at": "2022-06-13T09:50:53.627044Z",
"region_code": "ashburn-va",
"public_key": "4sHgXncx9tgswHmQvxq8B8O8iJ1AuJjLNmT9Qfs/VV0=",
"name": "WG_net01_VA_interface01",
"region": {
"code": "ashburn-va",
"name": "Ashburn",
"record_type": "region"
 },
"record_type": "wireguard_interface",
"endpoint": "64.16.243.3:5034",
"server_ip_address": "172.27.1.17/29"
 }
}
```

The `server_ip_address` is the private IP of the Cloud VPN interface and is used later to test connectivity.

**Step 4: Create a Cloud VPN Peer**

Create a Cloud VPN Peer associated with the Cloud VPN Interface. Input the `public_key` generated on the Ubuntu server in Step 2.

```
curl -X POST \
 --header "Content-Type: application/json" \
--header "Accept: application/json" \
 --header "Authorization: Bearer YOUR_API_KEY" \
--data '{
 "wireguard_interface_id": "9122b687-30aa-47a6-8f64-2b8681476ec2",
 "name": "ubuntu_peer01"
 "public_key": "ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4="
 }' \
 https://api.telnyx.com/v2/wireguard_peers
```

Example response:

```
{
"data": {
"updated_at": "2022-06-13T09:56:23.601577Z",
"id": "e4916505-a638-4b1d-b076-3142e7f1516a",
"wireguard_interface_id": "9122b687-30aa-47a6-8f64-2b8681476ec2",
"created_at": "2022-06-13T09:56:23.601577Z",
"public_key": "ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=",
"name": "ubuntu_peer01",
"last_seen": null,
"record_type": "wireguard_peer"
 }
}
```

**Step 5: Retrieve your configuration for the Cloud VPN Peer**

Save the peer configuration file in `/etc/wireguard` on the Ubuntu server. Add the private key to the configuration file. Give the configuration a meaningful name such as `wg0.conf` or `wg_ubuntu.conf`; it must have `.conf` as the file extension.

Configuration template:

```
[Interface]
Address = <server_private_ip_address>
PrivateKey = <contents-of-client-privatekey>

[Peer]
PublicKey = <contents-of-server-publickey>
Endpoint = <server-public-ip>:<port>
AllowedIPs = <ip/cidr>
```

Retrieve the configuration:

```
curl -X GET \
 --header "Content-Type: application/json" \
--header "Accept: application/json" \
 --header "Authorization: Bearer YOUR_API_KEY" \
https://api.telnyx.com/v2/19783d68-c893-4954-bfbf-815d9ab9b0f6/Config
```

Example response:

```
{
[Interface]
PrivateKey = <! INSERT PEER PRIVATE KEY HERE !>
Address = 172.27.1.18/32

[Peer]
PublicKey = ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=
AllowedIPs = 172.27.1.16/29
Endpoint = 64.16.243.3:5034
PersistentKeepalive = 25
}
```

**Step 6: Bring up the WireGuard interface on your peer**

```
sudo wg-quick up wg0
```

Example response:

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# wg-quick up wg0
[#] ip link add wg0 type wireguard
[#] wg setconf wg0 /dev/fd/63
[#] ip -4 address add 172.27.255.60/29 dev wg0
[#] ip link set mtu 1420 up dev wg0
```

**Step 7: Test connection**

```
sudo wg show
```

Example response:

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# wg show
interface: wg0
public key: ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=
private key: (hidden)
listening port: 45111
peer: qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU= endpoint: 203.0.113.0:51871 allowed ips: 198.51.100.0/29 latest handshake: 2 minutes, 12 seconds ago transfer: 10.20 KiB received, 5.05 KiB sent
```

Test connectivity by pinging the server IP address:

```
bash$ ping <server_ip_address>
```

Example response:

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# ping 172.27.1.17
PING 172.27.1.17 (172.27.1.17) 56(84) bytes of data.
64 bytes from 172.27.1.17: icmp_seq=1 ttl=64 time=145 ms
64 bytes from 172.27.1.17: icmp_seq=2 ttl=64 time=144 ms
64 bytes from 172.27.1.17: icmp_seq=3 ttl=64 time=144 ms
64 bytes from 172.27.1.17: icmp_seq=4 ttl=64 time=144 ms
64 bytes from 172.27.1.17: icmp_seq=5 ttl=64 time=144 ms
64 bytes from 172.27.1.17: icmp_seq=6 ttl=64 time=144 ms
```

By repeating these steps for multiple peers, you can link apps, devices, and services together across the Telnyx backbone for low-latency, secure communications.
