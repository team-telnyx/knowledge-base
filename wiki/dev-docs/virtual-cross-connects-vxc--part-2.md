---
title: Virtual Cross Connects (VXC)
summary: Virtual Cross Connects (VXC) provide private network connectivity between
  a Telnyx network and a public cloud provider (AWS, Azure, or GCP). This page covers
  the VXC API, coverage, pricing, and provider-specific setup procedures.
sources:
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
updated_at: 2026-08-05T13:59:16Z
---

# Virtual Cross Connects (VXC)

*Part 2 of 2 — see also: [Part 1](virtual-cross-connects-vxc--part-1.md)*

Virtual Cross Connects (VXC) provide private network connectivity between a Telnyx network and a public cloud provider (AWS, Azure, or GCP). This page covers the VXC API, coverage, pricing, and provider-specific setup procedures.

## Azure VXC Setup

### Architecture

The Azure VXC architecture connects a Telnyx network to Azure via ExpressRoute.

![Azure Architecture](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-architecture.png)

### Prerequisites

#### Create ExpressRoute Circuit (Azure)

| Parameter | Value |
| --- | --- |
| Region | Choose the matching available region from the VXC coverage API |
| Port Type | Provider |
| Provider | Equinix |
| Peering location | Matching available region from the VXC coverage API |
| Bandwidth | Choose the available bandwidth from the VXC coverage API |
| SKU | Standard |

Choose the rest of the parameters at your own discretion. At the end of this step, the "Provider status" should say "Not provisioned".

#### Telnyx Network

If you don't have a Telnyx network created already, follow the [Networks](networks.md) guide to create one.

### Procedure

#### Create a VXC Resource

```http
POST /v2/virtual_cross_connects HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 286

{
    "network_id": "{{your network UUID}}",
    "name": "my-first-azure-vxc",
    "cloud_provider": "azure",
    "cloud_provider_region": "Frankfurt",
    "primary_cloud_account_id": "xxxxxx",
    "bgp_asn": 12076
}
```

| Parameter | Value |
| --- | --- |
| `cloud_provider` | `azure` |
| `cloud_provider_region` | Choose the matching region from the ExpressRoute circuit |
| `primary_cloud_account_id` | "Service key" on the ExpressRoute created previously |
| `bgp_asn` | Azure's BGP ASN, which is `12076` |

Take note of the following info in the response; you will need it later:

- `id`
- `primary_cloud_ip`
- `primary_bgp_key`

#### Enable Primary Connection

```http
PATCH /v2/virtual_cross_connects/:vxc_uuid HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 31

{
    "primary_enabled": true
}
```

You must make sure the VXC `status` is `provisioned` before proceeding to the next step. You can poll the status using a GET request on the specific VXC.

#### Azure Private Peering

The "Provider status" must show "Provisioned" before performing this step.

| Parameter | Value |
| --- | --- |
| Peer ASN | Telnyx's BGP ASN, which is `63440` |
| Subnets | IPv4 |
| IPv4 Primary subnet | Choose the `/30` block that includes `primary_cloud_ip` |
| IPv4 Secondary subnet | Choose the next `/30` block |
| VLAN ID | Choose any number from a valid VLAN range |
| Shared key | `primary_bgp_key` |
| Public IP address | Create new |
| Public IP address SKU | Standard |

After saving, you may need to wait for some time before performing the next step. At this point, you should see Telnyx IPs advertised in the result after you click into "View route table." The connection is now ready for production use. The following steps are only needed for testing before deploying to your own production environment.

#### Virtual Network

| Parameter | Value |
| --- | --- |
| Region | Match that of the virtual network created from the previous step |

Next, add a Gateway subnet. Keep all parameters as default.

#### Virtual Network Gateways

| Parameter | Value |
| --- | --- |
| Name | Something meaningful to you |
| Region | Match that of the virtual network created from the previous step |
| Gateway type | ExpressRoute |
| SKU | Standard |
| Virtual network | Choose the one created from the previous step |
| Public IP address | Create new |
| Public IP address SKU | Standard |

The gateway creation will take a while — upward of 20 minutes. In the meantime, you can proceed to the following step.

#### Virtual Machines

| Parameter | Value |
| --- | --- |
| Region | Match that of the virtual network created from the previous step |
| Virtual network | Choose the one created from the previous step |

You can keep the rest default or choose at your discretion.

#### Add Gateway Connection

The Virtual Network Gateway you created must be successfully deployed before this step is performed.

| Parameter | Value |
| --- | --- |
| Connection type | ExpressRoute |
| Virtual network gateway | Choose the one created from the previous step |
| ExpressRoute circuit | Choose the one created from the previous step |
| Routing weight | 0 |

#### Validate Connection

Ensure all of the following are successfully deployed:

- ExpressRoute
- Virtual network
- Virtual network gateway & connection
- Virtual machine

SSH into the VM and perform a traceroute to `sip.telnyx.com` and `sip.telnyx.eu`. You can see the next hop is the next hop indicated on the Azure Private Peering under the ExpressRoute.

## Google Cloud VXC Setup

### Architecture

The GCP VXC architecture connects a Telnyx network to Google Cloud via Partner Interconnect.

![GCP Architecture](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-architecture.png)

### Prerequisites

#### VLAN Attachment (Google)

Create a VLAN attachment with the following parameters:

- Connection type: **Partner Interconnect Connection**
- Encryption: **Set up unencrypted Interconnect**
- Network: Choose the one you are connecting from
- Region: Choose the one that has a Telnyx PoP in proximity
- MTU: `8896`
- Create a router or choose an existing one

#### Telnyx Network

If you don't have a Telnyx network created already, follow the [Networks](networks.md) guide to create one.

### Procedure

#### Create a VXC Resource

```http
POST /v2/virtual_cross_connects HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 286

{
    "network_id": "a843547c-3f08-4a7e-8a4b-270c3ffb13f2",
    "name": "xd-frankfurt-vxc-gcp",
    "cloud_provider": "gce",
    "cloud_provider_region": "europe-west3",
    "primary_cloud_account_id": "xxxx/europe-west3/2",
    "bgp_asn": 16550,
    "bandwidth_mbps": 50
}
```

#### Activate Connection (Google)

On the Google side, activate the connection with:

- **Peer ASN**: `63440` (Telnyx)
- **MD5 Authentication**: `primary_bgp_key`

#### Update BGP Peering (Telnyx)

At this point, the connection is "Down". Take the Google-assigned BGP IPs and set them on the VXC using the PATCH method:

- `primary_cloud_ip` — "Cloud Router BGP IP" or "Remote IP" in the Troubleshooting page
- `primary_telnyx_ip` — "BGP peer IP" or "Local IP" in the Troubleshooting page

```http
PATCH /v2/virtual_cross_connects/:vxc_uuid HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 31

{
    "primary_enabled": true,
    "primary_cloud_ip": "169.254.131.250/29",
    "primary_telnyx_ip": "169.254.131.249/29"
}
```

At this point, on Google, the status will show as "Up".

#### Validate Connection

- Under VPC networks, you should see the routes advertised over the cloud router created.
- You can also SSH into one of your instances in the same network and perform a traceroute.

Example traceroute output:

```
xxx@instance-20240503-154050:~$ traceroute sip.telnyx.com
traceroute to sip.telnyx.com (192.76.120.10), 30 hops max, 60 byte packets
 1  * * *
 2  100.65.72.1 (100.65.72.1)  4.393 ms  4.367 ms  4.349 ms
 3  64.16.254.51 (64.16.254.51)  114.732 ms  114.715 ms  114.698 ms
 4  64.16.247.105 (64.16.247.105)  114.903 ms  114.877 ms  114.860 ms
 5  192.76.120.160 (192.76.120.160)  114.843 ms  114.825 ms  114.807 ms
 6  sip.telnyx.com (192.76.120.10)  114.857 ms  114.064 ms  114.038 ms
```
