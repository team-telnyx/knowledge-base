---
title: Telnyx Programmable Networking
summary: Telnyx Programmable Networking provides private connectivity to Telnyx SIP,
  API, and storage endpoints via logically isolated networks, three types of gateways
  (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS,
  GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway
  setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific
  VXC setup procedures and pricing.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
- url: https://developers.telnyx.com/docs/network/networks
- url: https://developers.telnyx.com/docs/network/overview/index
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
updated_at: 2026-07-17T09:20:17Z
---

# Telnyx Programmable Networking

*Part 1 of 7 — see also: [Part 2](telnyx-programmable-networking--part-2.md), [Part 3](telnyx-programmable-networking--part-3.md), [Part 4](telnyx-programmable-networking--part-4.md), [Part 5](telnyx-programmable-networking--part-5.md), [Part 6](telnyx-programmable-networking--part-6.md), [Part 7](telnyx-programmable-networking--part-7.md)*

Telnyx Programmable Networking provides private connectivity to Telnyx SIP, API, and storage endpoints via logically isolated networks, three types of gateways (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS, GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific VXC setup procedures and pricing.

## Introduction

Telnyx Programmable Networking allows users and their applications to access Telnyx SIP and API endpoints without traversing the public internet, offering a path with better latency and throughput. The SIP and API endpoints include:

- `api.telnyx.com`
- `sip.telnyx.com` and their regional counterparts
- `*.telnyxcloudstorage.com` where `*` is all available storage regions, e.g. `us-central-1`

Users' applications can reside in any one of the major hyperscalers (AWS, GCP, Azure) or in the users' own data centers (as long as the user has a presence in Equinix). This model is analogous to certain AWS concepts — from the "outside" world, a user can use a Direct Connect to connect to private resources (e.g. EC2 instances) or public resources (e.g. S3), though to AWS the "outside" world is largely limited to their users' on-premise data centers.

## API Concepts

### Coverage

The Coverage API enumerates all the supported products at each of Telnyx's PoPs. Before creating any resources, ensure that:

1. There is a PoP in the vicinity from where you want to connect, and
2. The desired resources are available at that PoP.

Equally important, depending on the resource, there are product-specific coverage endpoints you must consult. Refer to the [Coverage](coverage.md) guide for more detail.

### Networks

A network is a logically isolated virtual network. It is a prerequisite for the creation of other elements. Refer to the [Networks](networks.md) guide for more detail.

### Gateways

A gateway is a virtual node that facilitates traffic routing between your Telnyx network and an outside network. There are three types of gateways:

- **WireGuard Gateways (WGW)** — in the API, named `interface`
- **Internet Gateways (IGW)**
- **Private Wireless Gateways (PWG)**

WireGuard Gateways are virtual VPN concentrators implemented with the open source WireGuard protocol. They are similar to Virtual Private Gateway in AWS, VPN Gateway in GCP, and Virtual Network Gateway in Azure. Refer to the [WireGuard Gateway (WGW)](wireguard-gateway-wgw.md) guide for more detail.

Internet Gateways route traffic to and from the internet, similar to Internet Gateway or NAT Gateway in AWS. Refer to the [Internet Gateway (IGW)](internet-gateway-igw.md) guide.

Private Wireless Gateways are private packet gateways that concentrate, route, and segment traffic for a group of SIMs. Refer to the [Private Wireless Gateway (PGW)](private-wireless-gateway-pgw.md) guide for more detail.

### Virtual Cross Connects

A Virtual Cross Connect (VXC) is a virtual direct connection between a supported cloud provider and Telnyx. Refer to the [VXC Introduction](vxc-introduction.md) for more detail.

## Coverage

Individual networking resource availability is not universal across all Telnyx regions. The user must ensure the desired resource is offered at the desired region. To this end, Telnyx offers a coverage API (`GET /v2/network_coverage`).

The `location` parameter is hierarchical:

| Parameter | Value |
| --- | --- |
| `region` | `EMEA`, `AMER`, `APAC` |
| `site` | a broad geographical area within the region, e.g. `ORD` in `AMER` |
| `pop` | a specific data center within the site, e.g. `CH1` in `ORD` |
| `name` | a human readable name, e.g. `Chicago IL, US` |
| `code` | the unique ID for the site, e.g. `chicago-il` |

The `available_services` parameter is an array of all available resources that can be created at this specific location. Possible values are:

- `virtual_cross_connect`
- `cloud_vpn` aka wireguard interface aka wireguard gateway
- `private_wireless_gateway`
- `public_internet_gateway`

### Querying by the desired product

```
GET /v2/network_coverage?filter[available_services][contains]=cloud_vpn
```

### Querying by the desired product with a location constraint

```
GET /v2/network_coverage?filter[available_services][contains]=cloud_vpn&filter[location.region]=AMER
```

### Querying by the desired location

```
GET /v2/network_coverage?filter[location.region]=EMEA
```

Sample response:

```json
{
    "data": [
        {
            "available_services": [
                "virtual_cross_connect"
            ],
            "location": {
                "region": "EMEA",
                "site": "FRA",
                "pop": "FR5",
                "name": "Frankfurt, DE",
                "code": "frankfurt-de"
            },
            "record_type": "network_coverage"
        }
    ],
    "meta": {
        "total_pages": 1,
        "total_results": 1,
        "page_number": 1,
        "page_size": 25
    }
}
```

### Virtual Cross Connects (VXC) Coverage

In the case of virtual cross connect (VXC) there are two terminating endpoints to every single connection: a cloud provider endpoint and a Telnyx endpoint. As a result, it is insufficient to simply perform the coverage check. The above API response only indicates that one end of the VXC can be terminated at the Telnyx's FR5 PoP. It provides no information about the other terminating endpoint. To that end, Telnyx offers a VXC coverage API (`GET /v2/virtual_cross_connects_coverage`) to augment the generic coverage API.

Querying by fixing Telnyx endpoint:

```
GET /v2/virtual_cross_connects_coverage?filter[location.pop]=CH1
```

The response to the above query shows all the possible cloud provider endpoints at which a VXC, whose one end is terminated at Telnyx `CH1` PoP, can be terminated.

Querying by fixing cloud provider endpoint:

```
GET /v2/virtual_cross_connects_coverage?filter[cloud_provider]=aws&filter[cloud_provider_region]=us-east-1
```

The response to the above query shows all the possible Telnyx endpoints at which a VXC, whose one end is terminated at `us-east-1` of AWS, can be terminated.

Sample response:

```json
{
    "data": [
        {
            "cloud_provider": "aws",
            "cloud_provider_region": "us-east-2",
            "location": {
                "region": "AMER",
                "site": "ORD",
                "pop": "CH1",
                "name": "Chicago IL, US",
                "code": "chicago-il"
            },
            "available_bandwidth": [
                50
            ],
            "record_type": "virtual_cross_connects_coverage"
        }
    ],
    "meta": {
        "total_pages": 1,
        "total_results": 1,
        "page_number": 1,
        "page_size": 25
    }
}
```

The `available_bandwidth` is in Mbps.

## Networks

A `network` instance is a prerequisite for the creation of all other elements.

Request sample (don't forget to update `YOUR_API_KEY`):

```
POST /v2/networks HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
Content-Length: 40

{
  "name": "my_first_virtual_network"
}
```

Sample response:

```json
{
    "data": {
        "created_at": "2024-07-17T15:19:10.640289Z",
        "id": "58b42010-de88-4d9b-a164-d0b8170100bc",
        "updated_at": "2024-07-17T15:19:10.640289Z",
        "name": "my_first_virtual_network",
        "record_type": "network"
    }
}
```
