---
title: Coverage
summary: Telnyx exposes coverage APIs that let you discover which networking resources
  (virtual cross connects, cloud VPN, private wireless gateways, public internet gateways)
  are available at a given region, site, or point of presence, and — for virtual cross
  connects — which cloud provider endpoints can be paired with a given Telnyx PoP.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
updated_at: 2026-08-05T13:58:37Z
---

# Coverage

Telnyx exposes coverage APIs that let you discover which networking resources (virtual cross connects, cloud VPN, private wireless gateways, public internet gateways) are available at a given region, site, or point of presence, and — for virtual cross connects — which cloud provider endpoints can be paired with a given Telnyx PoP.

## Generic Coverage

Individual networking resource availability is not universal across all Telnyx regions. To determine whether a desired resource is offered at a desired region, use the coverage API: `GET /v2/network_coverage`.

The `location` parameter is hierarchical:

| Parameter | Description | Example |
| --- | --- | --- |
| `region` | One of the Telnyx regions | `EMEA`, `AMER`, `APAC` |
| `site` | A broad geographical area within the region | `ORD` in `AMER` |
| `pop` | A specific data center within the site | `CH1` in `ORD` |
| `name` | A human readable name | `Chicago IL, US` |
| `code` | The unique ID for the site | `chicago-il` |

The `available_services` parameter is an array of all available resources that can be created at a specific location. Possible values are:

- `virtual_cross_connect`
- `cloud_vpn` (also known as a WireGuard interface or WireGuard gateway)
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

### Sample response

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

## Virtual Cross Connects (VXC) Coverage

A virtual cross connect (VXC) has two terminating endpoints: a cloud provider endpoint and a Telnyx endpoint. Because of this, the generic coverage check is **insufficient** — it only indicates that one end of the VXC *can* be terminated at a given Telnyx PoP, and provides no information about the other terminating endpoint.

To address this, Telnyx offers a dedicated VXC coverage API: `GET /v2/virtual_cross_connects_coverage`, which augments the generic coverage API.

### Querying by fixing the Telnyx endpoint

```
GET /v2/virtual_cross_connects_coverage?filter[location.pop]=CH1
```

The response lists all the possible cloud provider endpoints at which a VXC — whose one end is terminated at the Telnyx `CH1` PoP — can be terminated.

### Querying by fixing the cloud provider endpoint

```
GET /v2/virtual_cross_connects_coverage?filter[cloud_provider]=aws&filter[cloud_provider_region]=us-east-1
```

The response lists all the possible Telnyx endpoints at which a VXC — whose one end is terminated at `us-east-1` of AWS — can be terminated.

### Sample response

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

The `available_bandwidth` field is expressed in Mbps.
