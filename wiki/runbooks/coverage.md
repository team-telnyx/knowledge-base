---
title: Coverage
summary: Individual networking resource availability is not universal across all Telnyx regions.
sources:
  - url: https://developers.telnyx.com/docs/network/coverage/index
    content_hash: 2f601a2f5dcbb6f65a25d42c36116eeb38c273e34d94778fc2346175610ce363
updated_at: 2026-04-10T00:00:00Z
---

# Coverage

## Generic Coverage

Individual networking resource availability is not universal across all Telnyx regions. Hence the user must ensure the desired resource is offered at the desired region. To this end, we offer a coverage API (`GET /v2/network_coverage`).

The `location` parameter is hierarchical:

| Parameter | Value                                                             |
| --------- | ----------------------------------------------------------------- |
| `region`  | `EMEA`, `AMER`, `APAC`                                            |
| `site`    | a broad geographical area within the region, e.g. `ORD` in `AMER` |
| `pop`     | a specific data center within the site, e.g. `CH1` in `ORD`       |
| `name`    | a human readable name, e.g. `Chicago IL, US`                      |
| `code`    | the unique ID for the site, e.g. `chicago-il`                     |

The `available_services` parameter is an array of all available resources that can be created at this specific location. Possible values are:

* `virtual_cross_connect`
* `cloud_vpn` aka wireguard interface aka wireguard gateway
* `private_wireless_gateway`
* `public_internet_gateway`

Here are some common usage patterns of this API.

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

Here is a sample response:

```
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

In the case of virtual cross connect (VXC) there are two terminating endpoints to every single connection: a cloud provider endpoint and a Telnyx endpoint.

As a result, it's ***insufficient*** to simply perform the coverage check. For example, the above API response only indicates that one end of the VXC ***can*** be terminated at the Telnyx's FR5 PoP. It provides no information about the other terminating endpoint. To that end, we offer a VXC coverage API (`GET /v2/virtual_cross_connects_coverage`) to augment the generic coverage API.

Here are some common usage patterns of this API.

Querying by fixing Telnyx endpoint

```
GET /v2/virtual_cross_connects_coverage?filter[location.pop]=CH1
```

The response to the above query shows all the possible cloud provider endpoints at which a VXC, whose one end is terminated at Telnyx `CH1` PoP, can be terminated.

Querying by fixing cloud provider endpoint

```
GET /v2/virtual_cross_connects_coverage?filter[cloud_provider]=aws&filter[cloud_provider_region]=us-east-1
```

The response to the above query shows all the possible Telnyx endpoints at which a VXC, whose one end is terminated at `us-east-1` of AWS, can be terminated.

Here is a sample response:

```
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
