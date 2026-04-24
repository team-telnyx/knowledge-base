---
title: Internet Gateway (IGW)
summary: This is a beta feature.
sources:
  - url: https://developers.telnyx.com/docs/network/gateways/internet-gateway/index
    content_hash: 1b276239a65e3dc67d8d3ce61e605ea29ade28a84b9aff279f8fe99a19b0a856
updated_at: 2026-04-10T00:00:00Z
---

# Internet Gateway (IGW)

<Callout type="warning">
  This is a beta feature

## Introduction

Internet Gateway (IGW) is an element that routes traffic between your Telnyx network and the internet. It is intended to be used with certain other elements.

## Creating an IGW

### Step 1: Create a Network

Follow [this guide](https://developers.telnyx.com/docs/network/networks).

### Step 2: Check for Coverage

Follow [this guide](https://developers.telnyx.com/docs/network/coverage).

Use `filter[available_services][contains]=public_internet_gateway` to look for a desired site at which to deploy the IGW. `frankfurt-de` is chosen for the subsequent steps.

### Step 3: Create an IGW

Using the network created from Step 1 and the chosen region from Step 2, create the IGW.

<Callout type="warning">
  Once an IGW is created on a specific network, it cannot be "migrated" to another one; it needs to be recreated on the other network. Double check the correct `network_id` is used in the following API request.

```
POST /v2/public_internet_gateways HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 125

{
  "network_id": "5647b6cf-b204-42d6-9c63-f2fd12253113",
  "name": "my_first_igw",
  "region_code": "frankfurt-de"
}
```

It's not yet ready to be used immediately after the creation since its status is `provisioning`.

```
{
    "data": {
        "created_at": "2024-08-01T14:36:39.938006Z",
        "region_code": "frankfurt-de",
        "name": "my_first_igw",
        "network_id": "5647b6cf-b204-42d6-9c63-f2fd12253113",
        "id": "06d65677-f1aa-43b6-8a6c-4f1abfe93754",
        "status": "provisioning",
        "updated_at": "2024-08-01T14:36:41.497785Z",
        "record_type": "public_internet_gateway",
        "public_ip": "64.16.243.172"
    }
}
```

### Step 4: Wait for Status Transition

The expected time for status to transition to provisioned is approximately 10 minutes. You can poll the IGW to check for status.

```
GET /v2/public_internet_gateways/{{igw_uuid}} HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

## Use Cases

### Use Case 1: Pure play VPN

Internet Gateway (IGW) can be used with Wireguard Gateway (WGW) to create a simple VPN service.

1. Set up an IGW
2. Set up a WGW and a peer.
3. On the peer, amend its config with:
   * `DNS` — choose your resolver. In the following example, 8.8.8.8 is chosen.
   * `AllowedIPs` — append with `0.0.0.0/0` so that reachability is beyond the private subnet.

Here is an example config of the peer.

```
[Interface]
PrivateKey = XXX
Address = 172.27.0.2/32
DNS = 8.8.8.8

[Peer]
PublicKey = YYY
AllowedIPs = 172.27.0.0/24, 0.0.0.0/0
Endpoint = 64.16.243.7:5022
PersistentKeepalive = 1
```

Deactivate and reactivate your Wireguard tunnel. You should see the IGW’s public IP showing up when you query what your public IP is.

```
user@localhost ~ % dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com
"64.16.243.172"
```

### Use Case 2: IGW + Private Wireless Gateway (PWG)

Coming Soon.

## Costs

* The monthly recurring cost (MRC) for each instance of IGW is \$50.
* Traffic is not currently metered in beta phase. We will meter traffic in GA phase.

## API References

* [IGW](https://developers.telnyx.com/api-reference/public-internet-gateways/create-a-public-internet-gateway)


## Related Pages

- [Wireguard Gateway (WGW)](../runbooks/wireguard-gateway-wgw.md)
- [Private Wireless Gateway (PGW)](../runbooks/private-wireless-gateway-pgw.md)
