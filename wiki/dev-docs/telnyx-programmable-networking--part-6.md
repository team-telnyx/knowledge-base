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

*Part 6 of 7 — see also: [Part 1](telnyx-programmable-networking--part-1.md), [Part 2](telnyx-programmable-networking--part-2.md), [Part 3](telnyx-programmable-networking--part-3.md), [Part 4](telnyx-programmable-networking--part-4.md), [Part 5](telnyx-programmable-networking--part-5.md), [Part 7](telnyx-programmable-networking--part-7.md)*

Telnyx Programmable Networking provides private connectivity to Telnyx SIP, API, and storage endpoints via logically isolated networks, three types of gateways (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS, GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific VXC setup procedures and pricing.

## Virtual Cross Connects (VXC)

The VXC guide first gives an overview of the product's availability, costs, and the general API structure. Subsequently, it branches into cloud provider specific guides. The reader should only concern themselves with the section about the cloud provider that's relevant to their use case.

### VXC API

The API resource in question is `/v2/virtual_cross_connects`. The following group of parameters needs to be provided regardless of the cloud provider.

| Parameter | Value |
| --- | --- |
| `network_id` | A VXC must be associated with a network. If no network exists on your account, you need to [create one](https://developers.telnyx.com/docs/network/networks) first. |
| `name` | Human readable text; something meaningful to you. |

The rest of the parameters are cloud provider specific. Please consult the subsequent sections.

### VXC Cost

You will be charged by Telnyx AND your cloud provider. Telnyx charges an MRC for each VXC instance according to the following schedule, which may change at our discretion according to the general T&C. We can neither interpret nor advise how your cloud provider may charge your account. Please consult your cloud provider's documentation.

#### AWS

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 100 |
| 100 Mbps | 125 |
| 200 Mbps | 150 |
| 300 Mbps | 175 |
| 400 Mbps | 200 |
| 500 Mbps | 225 |
| 1 Gbps | 450 |

#### GCP

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 100 |
| 100 Mbps | 125 |
| 200 Mbps | 150 |
| 300 Mbps | 175 |
| 400 Mbps | 200 |
| 500 Mbps | 225 |
| 1 Gbps | 450 |

#### Azure

| Virtual Cross Connects | Monthly Recurring Charge (USD) |
| --- | --- |
| 50 Mbps | 200 |
| 100 Mbps | 250 |
| 200 Mbps | 300 |
| 300 Mbps | 400 |
| 400 Mbps | 500 |
| 500 Mbps | 600 |
| 1 Gbps | 1000 |

### AWS VXC Setup

#### Architecture

We will construct the following architecture:

![AWS Architecture](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-architecture.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=3118f9be68c0be92402c302eeafdd860)

#### Prerequisites

**VPC** — this step is performed on AWS.

![AWS VPC](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-aws-vpc.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=1055bee5e69beb2178a8c5f702d3350e)

⚠️ Note: Ensure the intended region is selected. In this example, we are using eu-central-1 as the region.

![AWS Create VPC](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-create-vpc.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=5799d68a2689180ff08c81af69529048)

| Parameter | Value |
| --- | --- |
| Resources to create | VPC only |
| IPv4 CIDR block | IPv4 CIDR manual input |
| IPv4 CIDR | RFC1918, e.g. 10.10.11.0/24 |
| IPv6 CIDR block | No IPv6 CIDR block |
| Tenancy | Default |

**Virtual Private Gateway** — this step is performed on AWS. Create and attach a virtual private gateway to the VPC created.

![AWS Virtual Private Gateway](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-virtual-private-gateway.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=a2bc951aa9202fb28b584262476b722c)

⚠️ Note: Ensure the intended region is selected. In this example, we are using eu-central-1 as the region.

![AWS Create Virtual Private Gateway](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-create-virtual-private-gateway.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=4a267c0a430bb2ff82e45bca98c04d23)

⚠️ Note: Amazon default ASN value is 64512. You will need this value for VXC creation.

Next, attach the virtual private gateway to the VPC created in the first step.

![AWS Attach Virtual Private Gateway](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-attach-virtual-private-gateway.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=f43fe9fafdc2ce555f10b4da2a7a8dee)

![AWS Attach Virtual Private Gateway 2](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-attach-virtual-private-gateway-2.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=0c52b0ded5b7bdfe2ed2722e0d9e402f)

The state of the virtual private gateway will go from "Detached" to "Attaching" and finally "Attached".

**VPC Route Table** — this step is performed on AWS.

![AWS VPC Route Table 1](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-vpc-route-table-1.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=b8a99c82994bade9ca442ad67e094d16)

![AWS VPC Route Table 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-aws-vpc-route-table-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=032de07d534eb9034b63c74d4727225d)

![AWS VPC Route Table 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-aws-vpc-route-table-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=1bbdcd253a066d96d1f3f3379f18b531)

**Internet Gateway** — this step is performed on AWS. This is optional. Create and attach an internet gateway to the VPC created.

![AWS Internet Gateway 1](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-1.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=bc7c29c08f56ac75387cbe743cdf8d41)

![AWS Internet Gateway 2](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=9ec9aef9360d2e6adba32e3e4f0c45f6)

![AWS Internet Gateway 3](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=19f1ed51005e3ac1671f586881e82476)

![AWS Internet Gateway 4](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-4.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=9008082c8a591d7bb5a0445ea2ba997f)

![AWS Internet Gateway 5](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-5.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=f5581bd70910137a8f1e90d648268b35)

![AWS Internet Gateway 6](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-internet-gateway-6.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=c2901b79ab51a710bd1d5d4f429160ba)

**Subnet** — this step is performed on AWS. Assuming you don't have a subnet setup — choose the VPC created. Subnet CIDR block should be chosen from within the VPC block.

![AWS Subnet](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-subnet.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=cf557eb5a9cb6bbd926bd1b9f1231a75)

**EC2** — this step is performed on AWS. Assuming you don't have an EC2 instance — spin one up in the same region. Assign the VPC and Subnet created previously. Enable public IP on the instance so you can ssh into it.

![AWS EC2](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-ec2.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=619fabe5d2861d7e755f3d4adffa0c1e)

**Account ID** — this step is performed on AWS. ⚠️ You would need this number when you create the Telnyx VXC later.

![AWS Account ID](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-account-id.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=32d6a5f54b1393128d05aefe7a6215fb)

**Telnyx Network** — this step is performed on Telnyx. If you don't have a network created already, you may follow the [Networks](networks.md) guide to create one.

#### Procedure

**Create a VXC resource** — this step is performed on Telnyx.

```
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
| `cloud_provider_region` | Match what you selected on the AWS |
| `primary_cloud_account_id` | AWS account ID from the last step |
| `bgp_asn` | AWS's bgp asn which is 64512 |
| `bandwidth_mbps` | Chosen from available bandwidth of the VXC coverage API |

Take note of the VXC id returned in the response.

**Direct Connect** — this step is performed on AWS. If you haven't accepted the connection from your AWS account within 1 hour of the VXC creation, the VXC would be deleted and you will have to start over.

![AWS Direct Connect](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-direct-connect.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=9193a8c58d79ab0a7a9d7ecadb51896e)

![AWS Direct Connect 2](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-direct-connect-2.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=d9ffd2b0896e2a04dcd57a6201060487)

**Enable Primary Connection** — this step is performed on Telnyx. The connection must be enabled to be used.

```
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

![AWS Enable Primary Connection](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-enable-primary-connection.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=ad91e94a1103127c02f37bd7d4f58b66)

**Virtual Interface** — this step is performed on AWS. The connection created above needs to have an interface to which to connect.

![AWS Virtual Interface 1](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-virtual-interface-1.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=13982cb85cf0f2140ce949a101f769b7)

![AWS Virtual Interface 2](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-virtual-interface-2.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=bf535b09b24d3e10faf1cda7a18536a8)

Interface Parameters:

| Parameter | Value |
| --- | --- |
| Type | Private |
| Connection | Choose the Direct Connection you accepted previously. |
| Virtual interface owner | My AWS account |
| Gateway Type | Virtual Private Gateway and select the one you created in Prerequisite – AWS → Virtual Private Gateway |
| BGP ASN | 63440 - Telnyx ASN |
| Your router peer IP - optional | `primary_telnyx_ip` |
| Amazon router peer IP - optional | `primary_cloud_ip` |
| BGP authentication key - optional | `primary_bgp_key` |

Lastly you should see the following – the interface is "available".

![AWS Interface Parameters](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-interface-parameters.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=31f26b071f9376c6c3e4e606db6832c0)

**Validate Connection** — this step is performed on AWS. ssh into your EC2 instance and either ping or traceroute to one of the IP in the route table of the VPC. You can see the route went over the VXC instead of the public internet.

![AWS Validate Connection](https://mintcdn.com/telnyx/PAJh-h3FEJ6U1KdT/img/vxc-aws-validate-connection.png?fit=max&auto=format&n=PAJh-h3FEJ6U1KdT&q=85&s=6a02925c265334859c594ab7e1f9a677)

### Google VXC Setup

#### Architecture

We will construct the following architecture on Google Cloud.

![GCP Architecture](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-architecture.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=fcfacd63759b5ba8de5fc3b9abf8654d)

#### Prerequisites

**VLAN Attachment** — this step is performed on Google.

![GCP VLAN Attachment](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-vlan-attachment.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=8d98795910a7d462aa41e4616a165e67)

Parameters:

- "Partner Interconnect Connection"
- "Set up unencrypted Interconnect"

![GCP VLAN Attachment Parameters](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=c8847d3a4f7f238d4598ba0e152e856f)

![GCP VLAN Attachment Parameters 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=1eb0a30a9ed468bc5f583e551e79fd13)

- "Network": Choose the one you are connecting from
- "Region": Choose the one that there is a Telnyx PoP in proximity
- "MTU": 8896

![GCP VLAN Attachment Parameters 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=834a0f4fb39943d93e334b3a4880bc81)

- Create a router or choose an existing one.

![GCP VLAN Attachment Parameters 4](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-4.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=705bb1b7c4f25366882f14777f7edb81)

![GCP VLAN Attachment Parameters 5](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-5.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=2f790fad8e52f03a0f9eaf956db92964)

![GCP VLAN Attachment Parameters 6](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-attach-parameters-6.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=f9d615c9aefbedff31c702b46c7599f9)

**Telnyx Network** — this step is performed on Telnyx. If you don't have a network created already, you may follow the [Networks](networks.md) guide to create one.

#### Procedure

**Create a VXC resource** — this step is performed on Telnyx.

```
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

**Activate Connection** — this step is performed on Google.

![GCP Activate Connection](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-procedure-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=f3d0fae2b74f1ec9661712a4222f2f32)

![GCP Activate Connection 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-procedure-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=a9b90a47dc25ebd2fd6160dc882c8d5a)

![GCP Activate Connection 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-procedure-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=7cf0dcc2a918425bad78519a28984e2f)

- "Peer ASN": 63440 (Telnyx)
- "MD5 Authentication": `primary_bgp_key`

![GCP Activate Connection 4](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-procedure-4.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=7ad8f7bd1beaffa824dd4293e0371fb4)

**Update BGP Peering** — this step is performed on Telnyx. At this point, the connection is "Down". We need to take the Google assigned GBP IPs and set them on the VXC.

![GCP Update BGP Peering 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-update-bgp-peering-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=7a47ad9d7f1d3095874a7c2b9db70a7a)

![GCP Update BGP Peering 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-update-bgp-peering-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=ff61757620cebaf227dce38c685c782a)

Use the PATCH method.

- `primary_cloud_ip` — "Cloud Router BGP IP" or "Remote IP" in the "Troubleshooting" page
- `primary_telnyx_ip` — "BGP peer IP" or "Local IP" in the "Troubleshooting" page

```
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

At this point, on Google, it will show the "Status" as "Up"

![GCP Update BGP Peering 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-update-bgp-peering-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=ea682b879e59d9e84995dbb8c55469a3)

**Validate Connection** — this step is performed on Google.

- Under VPC networks, you should see the routes advertised over the cloud router created.
- You can also ssh in one of your instances in the same network and perform a traceroute.

![GCP Verify Connection](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-gcp-verify-connection.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=1f57ccda3c27d65c306e59192062085e)

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

### Azure VXC Setup

#### Architecture

We will construct the following architecture.

![Azure Architecture](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-architecture.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=e35bec4b3be2ea797f07c5af244f13a1)

#### Prerequisites

**Create ExpressRoute Circuit** — this step is performed on Azure.

![Azure Prerequisite 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-prerequisite-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=8ecb3b35c167c00b1669216fb2bc0e9c)

![Azure Prerequisite 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-prerequisite-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=6ae38680a122e174aa5b09e52f338b42)

| Parameter | Value |
| --- | --- |
| Region | Choose the matching available region from the VXC coverage API |
| Port Type | Provider |
| Provider | Equinix |
| Peering location | matching available region from the VXC coverage API |
| Bandwidth | Choose the available bandwidth from the VXC coverage API |
| SKU | Standard |

Choose the rest of the parameters at your own discretion.

![Azure Pre-requisite 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-prerequisite-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=d87e8afd35b134018df2d3d7cd496eed)

At the end of this step, the "Provider status" should say "Not provisioned".

**Telnyx Network** — this step is performed on Telnyx. If you don't have a network created already, you may follow the [Networks](networks.md) guide to create one.

#### Procedure

**Create a VXC resource** — this step is performed on Telnyx.

```
POST /v2/virtual_cross_connects HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 286

{
    "network_id": "{{you network UUID}}",
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
| `bgp_asn` | Azure's bgp asn which is 12076 |

Take note of the following info in the response; you will need it later.

- `id`
- `primary_cloud_ip`
- `primary_bgp_key`

**Enable Primary Connection** — this step is performed on Telnyx.

```
PATCH /v2/virtual_cross_connects/:vxc_uuid HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 31

{
    "primary_enabled": true
}
```

You must make sure the VXC `status` is `provisioned` before proceeding to the next step. You can poll the status using GET request on the specific VXC.

**Azure Private Peering** — this step is performed on Azure. "Provider status" must show "Provisioned" before performing this step.

![Azure Private Peering 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-private-peering-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=5a5c8302c2f5dde0a6fc364370434920)

![Azure Private Peering 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-private-peering-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=887a0c573b184e45d3f49af243bc6b5a)

![Azure Private Peering 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-private-peering-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=9eb6140da6f89798db5937185b14735d)

| Parameter | Value |
| --- | --- |
| Peer ASN | Telnyx's BGP ASN which is 63440 |
| Subnets | IPv4 |
| IPv4 Primary subnet | Choose the /30 block that includes `primary_cloud_ip` |
| IPv4 Secondary subnet | Choose the next /30 block |
| VLAN ID | Choose any number from a valid VLAN range |
| Shared key | primary bgp key |
| Public IP address | Create new |
| Public IP address SKU | Standard |

After saving, you may need to wait for some time before performing the next step.

![Azure Private Peering 4](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-private-peering-4.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=180b4a27c32f8b98c37f41222ad25231)

At this point, you should see Telnyx IPs advertised in the result after you click into "View route table."

![Azure Private Peering 5](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-private-peering-5.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=701693b6e7cda4f21b752b3d0e8ed208)

At this point, you are all set. Perform the following steps only if you are trying to test things out before putting it into your own production environment.

**Virtual Network**

![Azure Virtual Network 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-virtual-network-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=2742a0addc2e03f7819be705e9bcfc37)

| Parameters | Value |
| --- | --- |
| Region | Match that of the virtual network created from the previous step |

Next, add a Gateway subnet. Keep all parameters as default.

![Azure Virtual Network 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-virtual-network-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=404506dedad0146cc4d270ed3225b1d8)

**Virtual Network Gateways**

![Azure Virtual Network Gateways 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-virtual-network-gateways-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=d2a692e3e170e24b3669e07b55d46309)

| Parameters | Value |
| --- | --- |
| Name | Something meaningful to you |
| Region | Match that of the virtual network created from the previous step |
| Gateway type | Express Route |
| SKU | Standard |
| Virtual network | Choose the one created from the previous step |
| Public IP address | Create new |
| Public IP address SKU | Standard |

The gateway creation will take a while; upward of 20 minutes. In the meantime, you can proceed to the following step.

**Virtual Machines**

![Azure Virtual Machines 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-virtual-machines-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=ff6e3e15d71639783832ad04299ae649)

| Parameters | Value |
| --- | --- |
| Region | Match that of the virtual network created from the previous step |

![Azure Virtual Machines 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-virtual-machines-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=279172fc4bac8fccc9c5438fe7f9814b)

| Parameters | Value |
| --- | --- |
| Virtual network | Choose the one created from the previous step |

You can keep the rest default or choose at your discretion.

**Add Gateway Connection** — this step is performed on Azure. The Virtual Gateway you created must be successfully deployed before this step is performed.

![Azure Add Gateway Connection 1](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-add-gateway-connection-1.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=3f7968410132f719ad23760de8e97513)

![Azure Add Gateway Connection 2](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-add-gateway-connection-2.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=735aa9d8780f9244f66fa49145747855)

| Parameters | Value |
| --- | --- |
| Connection type | Express Route |

![Azure Add Gateway Connection 3](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-add-gateway-connection-3.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=af7e2db735d748a51262df96521285e0)

| Parameters | Value |
| --- | --- |
| Virtual network gateway | Choose the one created from the previous step |
| ExpressRoute circuit | Choose the one created from the previous step |
| Routing weight | 0 |

**Validate Connection** — this step is performed on Azure. Ensure all of the following are successfully deployed:

- ExpressRoute
- Virtual network
- Virtual network gateway & connection
- Virtual machine

SSH into the VM and perform a traceroute to sip.telnyx.com and sip.telnyx.eu. You can see the next hop is the next hop indicated on the Azure Private Peering under the express route.

![Azure Validate Connection](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/vxc-azure-verify-connection.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=5b4700da413d218b9683451abd28307e)
