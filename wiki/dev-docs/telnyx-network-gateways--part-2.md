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

*Part 2 of 4 — see also: [Part 1](telnyx-network-gateways--part-1.md), [Part 3](telnyx-network-gateways--part-3.md), [Part 4](telnyx-network-gateways--part-4.md)*

Telnyx offers three primary network gateway elements that route traffic across its backbone and the public internet: the Internet Gateway (IGW), the Private Wireless Gateway (PGW), and the WireGuard Gateway (WGW). Each gateway is provisioned on a Telnyx Network, has a per-instance monthly recurring cost, and can be combined with the others to build architectures ranging from simple VPNs to multi-cloud, multi-region, and SIM-connected private networks.

## Private Wireless Gateway (PGW)

The Private Wireless Gateway routes traffic between a group of Telnyx SIMs and other network elements. See the [Private Wireless Gateways](https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways) guide for additional background.

### Creating a PGW

- **Coverage filter:** `filter[available_services][contains]=private_wireless_gateway`. Currently, **Ashburn, VA** is the only supported site; more sites are in progress.
- **Endpoint:** `POST /v2/private_wireless_gateways`
- **Provisioning time:** approximately 15 minutes.

Request:

```
POST /v2/private_wireless_gateways HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 115

{
  "network_id": "f09e6854-fdef-4581-b3bc-63c2008fc4b5",
  "name": "pgw-08160937",
  "region_code": "ashburn-va"
}
```

Response (status `provisioning`):

```json
{
    "data": {
        "assigned_resources": [
            {
                "count": null,
                "record_type": "sim_card_group"
            }
        ],
        "created_at": "2024-08-16T14:37:47Z",
        "id": "2280aa63-b9b8-4d8a-867a-ff153e5ec422",
        "ip_range": "100.64.199.0/24",
        "name": "pgw-08160937",
        "network_id": "f09e6854-fdef-4581-b3bc-63c2008fc4b5",
        "record_type": "private_wireless_gateway",
        "region_code": "ashburn-va",
        "status": {
            "error_code": null,
            "error_description": null,
            "value": "provisioning"
        },
        "updated_at": "2024-08-16T14:37:47Z"
    }
}
```

Poll status with `GET /v2/private_wireless_gateways/{id}`.

### Attaching a SIM Group

A PGW is of little use without attached SIMs. Individual SIMs must be added to a SIM group, which can then be attached to the PGW via the Mission Control Portal. After a successful attachment, the PGW reflects the SIM group in `assigned_resources`:

```json
{
    "data": {
        "assigned_resources": [
            {
                "count": 1,
                "record_type": "sim_card_group"
            }
        ],
        "created_at": "2024-08-16T14:37:47Z",
        "id": "2280aa63-b9b8-4d8a-867a-ff153e5ec422",
        "ip_range": "100.64.199.0/24",
        "name": "pgw-08160937",
        "network_id": "f09e6854-fdef-4581-b3bc-63c2008fc4b5",
        "record_type": "private_wireless_gateway",
        "region_code": "ashburn-va",
        "status": {
            "error_code": null,
            "error_description": null,
            "value": "provisioned"
        },
        "updated_at": "2024-08-16T15:08:15Z"
    }
}
```

### PGW Use Cases

The following abbreviations are used throughout the examples: **PWG** = Private Wireless Gateway, **WGW** = WireGuard Gateway, **IGW** = Internet Gateway, **VXC** = Virtual Cross Connect.

**PWG + WGW.** Useful when traffic to and from SIMs must be segmented and private, and a high-bandwidth connection back to your internal service is not required.

![PWG + WGW Architecture](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/pgw-wgw.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=fb0a2047a8a44b33d20e145e8a37180e)

In the example, the connected device is an iPhone with access only to peers attached to the WGW (no default route). The Internal Service Peer is a DigitalOcean Droplet running a toy Apache web server, and the Admin Peer is a local host. On both peers, ensure that both the WGW subnet and the PGW subnet are listed in the `[Peer]` config's `AllowedIPs`:

```
[Peer]
PublicKey = XXX
AllowedIPs = 172.27.0.0/24, 100.64.199.0/24
Endpoint = XXX
PersistentKeepalive = XXX
```

From the internal service peer, a route to the iPhone is visible:

```
root@ubuntu-s-1vcpu-512mb-10gb-nyc1-01:~# traceroute 100.64.199.1
traceroute to 100.64.199.1 (100.64.199.1), 64 hops max
  1   172.27.0.1  21.591ms  21.000ms  20.677ms 
  2   *  *  * 
  3   *  *  * 
  4   *  *  * 
  5   100.64.199.1  885.269ms  179.245ms  171.923ms
```

From the iPhone, the internal service peer is reachable.

![Connection to Apache](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/ping-apache-1.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=fdc3ca59ebe1e38983d3535f4101abd9)

**PWG + WGW + IGW.** The previous architecture lacks internet reachability. Attaching an IGW to the same network provides it.

![PWG + WGW + IGW Architecture](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/pgw-wgw-igw.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=755c9f8e5053ba1ab1a4c451840a5afa)

Follow the [Internet Gateway (IGW)](internet-gateway-igw.md) guide to set up an IGW on the same network. At this point, the iPhone has internet reachability in addition to the WGW and PGW subnets.

![Device Network Stats](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/device-network-stats.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=8001ec7fb519dc5eeb3c5abb98887e7c)
![Device Internet Reachability](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/internet-reachability.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=a69b2afd34f08305a08bdaef5cc44a54)

In the screenshots above, the iPhone's Wi-Fi is turned off, its **Default Gateway IP** is `100.64.199.1` (the PGW), its **External IP** is `64.16.243.172` (the IGW), and it can ping `google.com`. Roundtrip ping time is high because the PGW is in Ashburn, US while the IGW is in Frankfurt, DE.

**PWG + WGW + IGW + VXC.** When internal services reside in a cloud provider, a VXC can be attached to the network. This combination currently only works when the WGW, IGW, and VXC are all at the Frankfurt site; universal coverage is in progress.

![PWG + WGW + IGW + VXC Architecture](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/pgw-wgw-igw-vxc.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=7308864ae7d91401c93bbf7766e7b104)

The example establishes a VXC from AWS `eu-central-1` and an EC2 instance in `eu-central-1` running a toy Apache server. See the [VXC guides](https://developers.telnyx.com/docs/network/vxc/intro) for AWS and other providers.

In the AWS VPC, routes from Telnyx's public APIs and the SIMs' private IP ranges are advertised and propagated:

![Route Table](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/route-table.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=21495f10b50fdf4cf105fa135f110f24)

This is validated by `traceroute` from within the EC2 instance. Latency is high because the EC2 is in Frankfurt while the device is attached to a PGW in Ashburn:

```
ubuntu@ip-10-10-11-9:~$ traceroute 100.64.199.1
traceroute to 100.64.199.1 (100.64.199.1), 64 hops max
  1   169.254.237.21  0.916ms  1.091ms  1.079ms 
  2   169.254.69.2  0.911ms  0.827ms  0.816ms 
  3   169.254.69.1  1.398ms  1.347ms  1.338ms 
  4   100.100.100.1  1.833ms  1.782ms  1.769ms 
  5   100.65.72.1  120.938ms  120.001ms  119.756ms 
  6   64.16.254.219  119.999ms  119.879ms  119.924ms 
  7   64.16.254.71  119.758ms  119.691ms  120.006ms 
  8   *  *  * 
  9   169.254.208.167  119.488ms  119.552ms  119.599ms 
 10   172.22.25.82  120.438ms  120.072ms  119.640ms 
 11   100.64.199.1  274.343ms  252.264ms  246.660ms
```

Finally, validate the connection from the device to the EC2. Since the EC2 runs a toy Apache server, open inbound HTTP port 80 for the SIM subnet:

![EC2 Inbound Rule](https://mintcdn.com/telnyx/tKcWw-YZ6CuwkRsC/img/inbound-rule.png?fit=max&auto=format&n=tKcWw-YZ6CuwkRsC&q=85&s=602b68f9d450030eb0dbc784f3154f7f)

From the iPhone, the server is accessible via its private IP:

![iPhone to Apache](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/iphone-apache-fr.jpg?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=a3487b567a06bf0ef49560b4d6a3a977)

### PGW Costs

- Monthly recurring cost (MRC): **$100 per PGW instance**.
- Additional SIM and data costs apply; see the [IoT Pricing](https://developers.telnyx.com/docs/iot-sim/iot-pricing) guide.

### PGW API Reference

- [Create a Private Wireless Gateway](/api-reference/private-wireless-gateways/create-a-private-wireless-gateway)
