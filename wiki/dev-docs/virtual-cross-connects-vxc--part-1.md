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

*Part 1 of 2 — see also: [Part 2](virtual-cross-connects-vxc--part-2.md)*

Virtual Cross Connects (VXC) provide private network connectivity between a Telnyx network and a public cloud provider (AWS, Azure, or GCP). This page covers the VXC API, coverage, pricing, and provider-specific setup procedures.

## Overview

Virtual Cross Connects (VXC) provide private network connectivity between a Telnyx network and a public cloud provider. Telnyx supports VXC setups for AWS, Azure, and Google Cloud Platform (GCP). Each VXC is billed as a Monthly Recurring Charge (MRC) by Telnyx, and your cloud provider may charge additional fees on its own account.

## VXC API

The VXC API resource is `/v2/virtual_cross_connects`. The following parameters are required regardless of the cloud provider:

| Parameter | Value |
| --- | --- |
| `network_id` | A VXC must be associated with a network. If no network exists on your account, you need to [create one](networks.md) first. |
| `name` | Human readable text; something meaningful to you. |

The remaining parameters are cloud provider specific and are described in the provider-specific sections below.

## Coverage

Before provisioning a VXC, refer to the [Coverage](coverage.md) API to ensure the desired resource is offered at the desired region. The available regions and bandwidths returned by the coverage API are used to populate the `cloud_provider_region` and `bandwidth_mbps` parameters when creating a VXC.

## Pricing

You will be charged by Telnyx AND your cloud provider. Telnyx charges an MRC for each VXC instance according to the following schedule, which may change at Telnyx's discretion according to the general T&C. Telnyx cannot interpret or advise how your cloud provider may charge your account; consult your cloud provider's documentation for those details.

### AWS

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 100 |
| 100 Mbps | 125 |
| 200 Mbps | 150 |
| 300 Mbps | 175 |
| 400 Mbps | 200 |
| 500 Mbps | 225 |
| 1 Gbps | 450 |

### GCP

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 100 |
| 100 Mbps | 125 |
| 200 Mbps | 150 |
| 300 Mbps | 175 |
| 400 Mbps | 200 |
| 500 Mbps | 225 |
| 1 Gbps | 450 |

### Azure

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 200 |
| 100 Mbps | 250 |
| 200 Mbps | 300 |
| 300 Mbps | 400 |
| 400 Mbps | 500 |
| 500 Mbps | 600 |
| 1 Gbps | 1000 |

## AWS VXC Setup

### Architecture

The AWS VXC architecture connects a Telnyx network to an AWS VPC via AWS Direct Connect.

![AWS Architecture](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-architecture.png)

### Prerequisites (AWS)

#### VPC

Create a VPC in the intended region (for example, `eu-central-1`).

| Parameter | Value |
| --- | --- |
| Resources to create | VPC only |
| IPv4 CIDR block | IPv4 CIDR manual input |
| IPv4 CIDR | RFC1918, e.g. `10.10.11.0/24` |
| IPv6 CIDR block | No IPv6 CIDR block |
| Tenancy | Default |

#### Virtual Private Gateway

Create and attach a virtual private gateway to the VPC. The Amazon default ASN value is `64512`; you will need this value for VXC creation. The gateway state will transition from "Detached" to "Attaching" and finally "Attached".

#### VPC Route Table

Configure the VPC route table to direct traffic over the VXC.

#### Internet Gateway (Optional)

Create and attach an internet gateway to the VPC if outbound internet access is required.

#### Subnet

Create a subnet within the VPC. The subnet CIDR block should be chosen from within the VPC block.

#### EC2

Spin up an EC2 instance in the same region. Assign the VPC and subnet created previously. Enable a public IP on the instance so you can SSH into it.

#### Account ID

Note the AWS account ID; you will need it when creating the Telnyx VXC.

### Telnyx Network

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
    "network_id": "314ae4ed-04f0-4111-be40-240beb7fdcf0",
    "name": "xd-frankfurt-vxc-aws",
    "cloud_provider": "aws",
    "cloud_provider_region": "eu-central-1",
    "primary_cloud_account_id": "YYY",
    "bgp_asn": 64512,
    "bandwidth_mbps": 50
}
```

| Parameter | Value |
| --- | --- |
| `cloud_provider` | `aws` |
| `cloud_provider_region` | Match what you selected on AWS |
| `primary_cloud_account_id` | AWS account ID from the prerequisite step |
| `bgp_asn` | AWS's BGP ASN, which is `64512` |
| `bandwidth_mbps` | Chosen from available bandwidth of the VXC coverage API |

Take note of the VXC `id` returned in the response.

#### Direct Connect

If you haven't accepted the connection from your AWS account within 1 hour of the VXC creation, the VXC will be deleted and you will have to start over.

#### Enable Primary Connection

The connection must be enabled to be used.

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

At this point, the connection on AWS will show as "available".

#### Virtual Interface

The connection created above needs an interface to which to connect.

| Parameter | Value |
| --- | --- |
| Type | Private |
| Connection | Choose the Direct Connection you accepted previously |
| Virtual interface owner | My AWS account |
| Gateway Type | Virtual Private Gateway — select the one you created in the Virtual Private Gateway prerequisite |
| BGP ASN | `63440` — Telnyx ASN |
| Your router peer IP (optional) | `primary_telnyx_ip` |
| Amazon router peer IP (optional) | `primary_cloud_ip` |
| BGP authentication key (optional) | `primary_bgp_key` |

Once complete, the interface should show as "available".

#### Validate Connection

SSH into your EC2 instance and either ping or traceroute to one of the IPs in the route table of the VPC. You can see the route went over the VXC instead of the public internet.
