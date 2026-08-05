---
title: Telnyx Network Gateways
summary: 'Telnyx offers three primary network gateway elements that route traffic
  across its backbone and the public internet: the Internet Gateway (IGW), the Private
  Wireless Gateway (PGW), and the WireGuard Gateway (WGW). Each gateway is provisioned
  on a Telnyx Network, has a per-instance monthly recurring cost, and can be combined
  with the others to build architectures ranging from simple VPNs to multi-cloud,
  multi-region, and SIM-connected private networks.'
sources:
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
updated_at: 2026-08-05T13:59:30Z
---

# Telnyx Network Gateways

*Part 3 of 4 — see also: [Part 1](telnyx-network-gateways--part-1.md), [Part 2](telnyx-network-gateways--part-2.md), [Part 4](telnyx-network-gateways--part-4.md)*

Telnyx offers three primary network gateway elements that route traffic across its backbone and the public internet: the Internet Gateway (IGW), the Private Wireless Gateway (PGW), and the WireGuard Gateway (WGW). Each gateway is provisioned on a Telnyx Network, has a per-instance monthly recurring cost, and can be combined with the others to build architectures ranging from simple VPNs to multi-cloud, multi-region, and SIM-connected private networks.

## WireGuard Gateway (WGW)

The WireGuard Gateway is a VPN concentrator built on [WireGuard](https://www.wireguard.com/) to which peers can connect over the public internet.

### Creating a WGW

- **Coverage filter:** `filter[available_services][contains]=cloud_vpn` (e.g. `ashburn-va`).
- **Endpoint:** `POST /v2/wireguard_interfaces`
- **Provisioning time:** approximately 5 minutes.

Request:

```
POST /v2/wireguard_interfaces HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 115

{
  "network_id": "91446ee3-9f6a-49ed-8d9b-1bd3e1529324",
  "name": "wgw-08071029",
  "region_code": "ashburn-va"
}
```

Response (status `provisioning`):

```json
{
    "data": {
        "name": "wgw-08071029",
        "status": "provisioning",
        "public_key": "XXX",
        "created_at": "2024-08-07T15:29:52.068774Z",
        "network_id": "91446ee3-9f6a-49ed-8d9b-1bd3e1529324",
        "enable_sip_trunking": false,
        "id": "b6a10cb9-6c1a-40bd-96e3-d4f8eb2bd6c5",
        "region_code": "ashburn-va",
        "updated_at": "2024-08-07T15:29:53.493104Z",
        "region": {
            "code": "ashburn-va",
            "name": "Ashburn VA, US",
            "record_type": "region"
        },
        "record_type": "cloud_vpn",
        "endpoint": "64.16.243.3:5107",
        "server_ip_address": "172.27.0.1/24"
    }
}
```

- `endpoint` is the publicly routable IP to which peers connect over the public internet.
- `server_ip_address` is the private subnet range used by the WGW and its peers, with the WGW occupying the first usable IP.

Poll status with `GET /v2/wireguard_interfaces/{id}`.

### Creating Peers

Create a peer for the WGW:

```
POST /v2/wireguard_peers HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 102

{
    "name": "mbp-local-peer",
    "wireguard_interface_id": "b6a10cb9-6c1a-40bd-96e3-d4f8eb2bd6c5"
}
```

The response includes the key pair. `private_key` is returned **only once** in the creation response and must be stored by you:

```json
{
    "data": {
        "name": "mbp-local-peer",
        "public_key": "ZZZ",
        "last_seen": null,
        "created_at": "2024-08-07T15:45:13.569576Z",
        "id": "7fc4c14e-ff94-4a97-b156-35f1feeb29b8",
        "wireguard_interface_id": "b6a10cb9-6c1a-40bd-96e3-d4f8eb2bd6c5",
        "updated_at": "2024-08-07T15:45:13.922425Z",
        "record_type": "wireguard_peer",
        "private_key": "YYY"
    }
}
```

You can also fetch a `conf` template:

```
GET /v2/wireguard_peers/7fc4c14e-ff94-4a97-b156-35f1feeb29b8/config HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

After inserting the `private_key`, import the `conf` file on the peer:

```
# Telnyx CloudVPN config. Target OS: Linux

[Interface]
PrivateKey = YYY
Address = 172.27.0.2/32

[Peer]
PublicKey = XXX
AllowedIPs = 172.27.0.0/24
Endpoint = 64.16.243.3:5107
PersistentKeepalive = 1
```

`[Interface]` refers to the local peer:

- `PrivateKey` should be the value returned in `private_key`.
- `Address` is the next available IP in the subnet range. For the first peer, this is the next IP after the WGW.

`[Peer]` refers to the WGW:

- `PublicKey` is that of the WGW.
- `AllowedIPs` is the network this peer has access to. See [this explanation](https://github.com/pirate/wireguard-docs?tab=readme-ov-file#allowedips).
- `Endpoint` is the publicly exposed IP to which peers connect.
- `PersistentKeepalive` is a default parameter that can be ignored.

### Configuring Peers

With the `conf` file, import it onto the host. Environment-specific guides:

- [Linux-like environment](https://developers.telnyx.com/docs/network/wireguard-peer-config/linux)
- [macOS](https://developers.telnyx.com/docs/network/wireguard-peer-config/macos)

### WGW Use Cases

**Multi-Cloud Network.** A WGW can act as a VPN concentrator to facilitate traffic between peers in different clouds.

![Multi Cloud Peers](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/multi-cloud-peers.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=3aab3b7b813ed04c40b1852f230d45a2)

In the example, Peer in Cloud A is an EC2 instance in AWS and Peer in Cloud B is a Droplet in DigitalOcean. Both run an Apache server but only allow inbound SSH traffic, so they are unreachable from the public internet:

```
user@localhost ~ % ping 34.201.0.189
PING 34.201.0.189 (34.201.0.189): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
^C
--- 34.201.0.189 ping statistics ---
3 packets transmitted, 0 packets received, 100.0% packet loss
user@localhost ~ % curl 34.201.0.189
^C
```

However, both are connected to the WGW:

```
ubuntu@ip-10-10-11-10:~$ sudo wg show
interface: peer1
  public key: Jt1zAJD6W2BZgOwtUsNY2KrMO0oRfUmfAEZGNEUZKiQ=
  private key: (hidden)
  listening port: 33174

peer: XYy8e5EKtE1F0fwwMgr792/9noYs53uRZBX5O3XJ4Eg=
  endpoint: 64.16.243.3:5107
  allowed ips: 172.27.0.0/24
  latest handshake: 14 seconds ago
  transfer: 124 B received, 596 B sent
  persistent keepalive: every 1 second
```

```
root@ubuntu-s-1vcpu-512mb-10gb-nyc1-01:~# sudo wg show
interface: peer2
  public key: eAvskX/cBw10DpxPPcvItsFcBr2meAKOVgwFjysZnF4=
  private key: (hidden)
  listening port: 33951

peer: XYy8e5EKtE1F0fwwMgr792/9noYs53uRZBX5O3XJ4Eg=
  endpoint: 64.16.243.3:5107
  allowed ips: 172.27.0.0/24
  latest handshake: 4 seconds ago
  transfer: 124 B received, 308 B sent
  persistent keepalive: every 1 second
```

Despite the firewall rules, Peer 1 can talk to Peer 2 over the WireGuard subnet:

```
ubuntu@ip-10-10-11-10:~$ curl 172.27.0.3
<!DOCTYPE html>
<html>
    <head>
        <title>I am the Droplet Peer in DigitalOcean</title>
    </head>
</html>
```

```
root@ubuntu-s-1vcpu-512mb-10gb-nyc1-01:~# curl 172.27.0.2
<!DOCTYPE html>
<html>
    <head>
        <title>I am the EC2 Peer in AWS</title>
    </head>
</html>
```

This pattern is readily extensible to peers running web services in various environments.

**Private Access to Other Telnyx Services.** If a WGW is created with `enable_sip_trunking`, the WGW enables routing for all Telnyx public API endpoints.

![Private Access](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/private-access.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=ef20621bfbd695d5829924988770116b)

On the peer config, additional routes are added under `AllowedIPs`:

```
[Interface]
PrivateKey = XXX
Address = 172.27.0.2/32

[Peer]
PublicKey = jSSaLXXVEzYUM8N8IM+65YuuScL+Sf2DytZCdLhFSGo=
AllowedIPs = 172.27.0.0/24, 64.16.250.10/32, 64.16.250.11/32, 64.16.250.13/32, 103.115.244.145/32, 103.115.244.146/32, 185.246.41.140/32, 185.246.41.141/32, 192.76.120.10/32, 192.76.120.11/32, 192.76.120.31/32, 64.16.226.0/24, 64.16.227.0/24, 64.16.228.0/24, 64.16.230.0/24, 64.16.248.0/24, 64.16.249.0/24, 50.114.144.0/21, 185.246.41.128/25, 103.115.244.128/25, 64.16.239.98/32, 64.16.239.39/32, 64.16.239.82/32, 64.16.224.44/32
Endpoint = 64.16.243.15:5016
PersistentKeepalive = 1
```

Traffic between a connected peer and Telnyx API, SIP, and Storage services then flows through the WGW (`172.27.0.1`) onto the Telnyx network:

```
user@localhost ~ % traceroute sip.telnyx.com        
traceroute to sip.telnyx.com (192.76.120.10), 64 hops max, 40 byte packets
 1  172.27.0.1 (172.27.0.1)  6.708 ms  7.726 ms  7.133 ms
 2  *^C
user@localhost ~ % traceroute api-direct.telnyx.com  
traceroute to api-direct.telnyx.com (64.16.224.44), 64 hops max, 40 byte packets
 1  172.27.0.1 (172.27.0.1)  7.673 ms  6.239 ms  6.488 ms
 2  *^C
user@localhost ~ % traceroute us-central-1.telnyxcloudstorage.com
traceroute to us-central-1.telnyxcloudstorage.com (64.16.239.39), 64 hops max, 40 byte packets
 1  172.27.0.1 (172.27.0.1)  6.885 ms  6.898 ms  6.621 ms
 2  * *^C
user@localhost ~ % aws s3api list-buckets --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
{
    "Buckets": [
        {
            "Name": "bucket1",
            "CreationDate": "2024-03-26T17:54:09.271000+00:00"
        },
        {
            "Name": "bucket2",
            "CreationDate": "2024-03-26T16:51:51.967000+00:00"
        },
        {
            "Name": "bucket3",
            "CreationDate": "2023-11-29T13:50:59.837000+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "xxx",
        "ID": "xxx"
    }
}
```

This arrangement is useful when public routing must be locked down, for example during an extreme DDoS attack.

**Cross-Region Network.** The previous architecture can be extended across regions.

![Cross Regional Network](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/multi-site-network.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=a9d10d5789a39813fd4ea9753019a535)

In this example, Site A is Telnyx Ashburn, Site B is Telnyx Amsterdam, Cloud A is AWS, and Cloud B is DigitalOcean. Traffic between the two peers rides the Telnyx backbone between Ashburn and Amsterdam. *Coming soon.*

**Other use cases:**

- Global IP *(coming soon)*
- [Internet Gateway (IGW)](internet-gateway-igw.md)
- Private Wireless Gateway (PGW) *(coming soon)*

### WGW Costs

- Monthly recurring cost (MRC): **$10 per WGW instance**.
- Connected Peers are free of charge.

### WGW API Reference

- [Create a WireGuard Interface](/api-reference/wireguard-interfaces/create-a-wireguard-interface)
- [List all WireGuard Interfaces](/api-reference/wireguard-interfaces/list-all-wireguard-interfaces)
