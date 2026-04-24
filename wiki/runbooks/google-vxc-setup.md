---
title: Google VXC Setup
summary: We will construct the following architecture on Google Cloud.
sources:
  - url: https://developers.telnyx.com/docs/network/vxc/gcp/index
    content_hash: 940a8a47815885ada1a4f28cec432bc95606c56753eb315b97902532e791716c
updated_at: 2026-04-10T00:00:00Z
---

# Google VXC Setup

Google VXC Setup

## Architecture

We will construct the following architecture on Google Cloud.

<img alt="GCP Architecture" />

## Prerequisites

### VLAN Attachment

This step is performed on Google

<img alt="GCP VLAN Attachment" />

Parameters:

* "Partner Interconnect Connection"
* "Set up unencrypted Interconnect"

<img alt="GCP VLAN Attachment Parameters" />

<img alt="GCP VLAN Attachment Parameters 2" />

* "Network": Choose the one you are connecting from
* "Region": Choose the one that there is a Telnyx PoP in proximity
* "MTU": 8896

<img alt="GCP VLAN Attachment Parameters 3" />

* Create a router or choose an existing one.

<img alt="GCP VLAN Attachment Parameters 4" />

<img alt="GCP VLAN Attachment Parameters 5" />

<img alt="GCP VLAN Attachment Parameters 6" />

### Telnyx Network

This step is performed on Telnyx.

If you don't have a network created already, you may follow [this guide](https://developers.telnyx.com/docs/network/networks) to create one.

## Procedure

### Create a VXC resource

This step is performed on Telnyx.

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

### Activate Connection

This step is performed on Google.

<img alt="GCP Activate Connection" />

<img alt="GCP Activate Connection 2" />

<img alt="GCP Activate Connection 3" />

“Peer ASN”: 63440 (Telnyx)
“MD5 Authentication”: `primary_bgp_key`

<img alt="GCP Activate Connection 4" />

### Update BGP Peering

This step is performed on Telnyx.

At this point, the connection is “Down”. We need to take the Google assigned GBP IPs and set them on the VXC.

<img alt="GCP Update BGP Peering 1" />

<img alt="GCP Update BGP Peering 2" />

Use the PATCH method.

* `primary_cloud_ip` — “Cloud Router BGP IP” or “Remote IP” in the “Troubleshooting” page
* `primary_telnyx_ip` — “BGP peer IP” or “Local IP”in the “Troubleshooting” page

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

At this point, on Google, it will show the “Status” as “Up”

<img alt="GCP Update BGP Peering 3" />

### Validate Connection

This step is performed on Google.

* Under VPC networks, you should see the routes advertised over the cloud router created.
* You can also ssh in one of your instances in the same network and perform a traceroute.

<img alt="GCP Verify Connection" />

```bash theme={null}
xxx@instance-20240503-154050:~$ traceroute sip.telnyx.com
traceroute to sip.telnyx.com (192.76.120.10), 30 hops max, 60 byte packets
 1  * * *
 2  100.65.72.1 (100.65.72.1)  4.393 ms  4.367 ms  4.349 ms
 3  64.16.254.51 (64.16.254.51)  114.732 ms  114.715 ms  114.698 ms
 4  64.16.247.105 (64.16.247.105)  114.903 ms  114.877 ms  114.860 ms
 5  192.76.120.160 (192.76.120.160)  114.843 ms  114.825 ms  114.807 ms
 6  sip.telnyx.com (192.76.120.10)  114.857 ms  114.064 ms  114.038 ms
```


## Related Pages

- [Azure VXC Setup](../runbooks/azure-vxc-setup.md)
- [AWS VXC Setup](../runbooks/aws-vxc-setup.md)
