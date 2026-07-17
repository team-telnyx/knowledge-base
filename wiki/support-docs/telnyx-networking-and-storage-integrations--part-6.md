---
title: Telnyx Networking and Storage Integrations
summary: This page consolidates Telnyx networking and storage integration guides,
  covering virtual cross connect (VXC) setup with AWS, Azure, Google Cloud, and Megaport,
  configuration of S3-compatible clients (Cyberduck, WAL-G, Arq Backup, Backup4all,
  Duplicati, WinSCP, CrossFTP) with Telnyx Storage, and a WireGuard-based Cloud VPN
  tutorial for connecting a Digital Ocean Ubuntu server to the Telnyx network.
sources:
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
updated_at: 2026-07-17T09:09:23Z
---

# Telnyx Networking and Storage Integrations

*Part 6 of 7 — see also: [Part 1](telnyx-networking-and-storage-integrations--part-1.md), [Part 2](telnyx-networking-and-storage-integrations--part-2.md), [Part 3](telnyx-networking-and-storage-integrations--part-3.md), [Part 4](telnyx-networking-and-storage-integrations--part-4.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md), [Part 7](telnyx-networking-and-storage-integrations--part-7.md)*

This page consolidates Telnyx networking and storage integration guides, covering virtual cross connect (VXC) setup with AWS, Azure, Google Cloud, and Megaport, configuration of S3-compatible clients (Cyberduck, WAL-G, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP) with Telnyx Storage, and a WireGuard-based Cloud VPN tutorial for connecting a Digital Ocean Ubuntu server to the Telnyx network.

## Telnyx Networking on Ubuntu (WireGuard)

This tutorial walks through connecting a Digital Ocean Ubuntu Server via WireGuard to a [Cloud VPN](https://telnyx.com/products/cloud-vpn) interface on the Telnyx network.

**Pre-requisites**

- A Telnyx Account, API key, and a Network (see the Networking Quickstart Guide)
- A [Digital Ocean Ubuntu Server](https://docs.digitalocean.com/products/droplets/how-to/create/) with [additional security setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)

**Step 1: Install WireGuard on the server**

Log onto your Digital Ocean Ubuntu Server and execute:

```
sudo apt install wireguard
```

**Step 2: Generate public and private keys**

Use the WireGuard key generation tool to create the public and private keys needed to communicate with the Cloud VPN server on the Telnyx network:

```
wg genkey | tee privatekey | wg pubkey > publickey
```

Print both keys to screen — you will need both of them soon:

```
cat privatekey
cat publickey
```

> The `private_key` will be needed later to build the Cloud VPN peer configuration. The `public_key` will be used when creating the Cloud VPN peer.

**Step 3: Create a Cloud VPN Interface**

Create a Cloud VPN Interface associated with the Network that you created in the Networking Quickstart Guide. This network interface is configured on the Telnyx network and acts as a tunnel interface.

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

> The `server_ip_address` is the private IP of the Cloud VPN interface and will be used later to test connectivity between the added peer and the interface.

**Step 4: Create a Cloud VPN Peer**

Create a Cloud VPN Peer associated with the Cloud VPN Interface. This adds a peer to the server configuration created on the Cloud VPN server on the Telnyx network. Input your `public_key` generated on the Digital Ocean Ubuntu server in step 2.

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "wireguard_interface_id": "9122b687-30aa-47a6-8f64-2b8681476ec2",
    "name": "ubuntu_peer01",
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

Save the peer configuration file in the `/etc/wireguard` directory on the Digital Ocean Ubuntu server. The peer configuration can be retrieved via API. You will need to add the private key to the configuration file. Give the configuration a meaningful name (e.g., `wg0.conf` or `wg_ubuntu.conf`). It must have `.conf` as the file extension.

Cloud VPN Peer Configuration Template:

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
[Interface]
PrivateKey = <! INSERT PEER PRIVATE KEY HERE !>
Address = 172.27.1.18/32

[Peer]
PublicKey = ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=
AllowedIPs = 172.27.1.16/29
Endpoint = 64.16.243.3:5034
PersistentKeepalive = 25
```

**Step 6: Bring up the WireGuard interface on your peer**

Bring up the WireGuard VPN interface on the peer. The command must contain the name of the peer configuration file you created in Step 5, without the `.conf` extension:

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

Show the current peer configuration:

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
peer: qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU=
  endpoint: 203.0.113.0:51871
  allowed ips: 198.51.100.0/29
  latest handshake: 2 minutes, 12 seconds ago
  transfer: 10.20 KiB received, 5.05 KiB sent
```

Test connectivity to the Cloud VPN interface:

```
ping <server_ip_address>
```

> The `server_ip_address` is the private IP of the Cloud VPN interface and can be found in the response of the Cloud VPN Interface create endpoint in Step 3.

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

By repeating these steps for multiple peers, you can link apps, devices, and services together across the Telnyx backbone for low-latency, secure communications across the globe.
