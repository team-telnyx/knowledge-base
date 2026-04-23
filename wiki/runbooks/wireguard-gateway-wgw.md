---
title: Wireguard Gateway (WGW)
summary: 'Wireguard Gateway configuration. Note: legacy docs and Mission Control Portal refer to these as Wireguard Interfaces.'
sources:
  - url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
    content_hash: 65d6a1293622c1616216c4fe500d08d9e525f825a23cee5f299b19c8c3cfaaaf
updated_at: 2026-04-10T00:00:00Z
---

# Wireguard Gateway (WGW)

<Callout type="warning">
  On naming convention: in the [API Reference](https://developers.telnyx.com/api-reference/wireguard-interfaces/list-all-wireguard-interfaces), certain legacy documentations, and the Mission Control Portal, Wireguard Gateways are referred to as "Wireguard Interfaces".
  In this guide and all guides under the "Networking" collection, the term **Wireguard Gateway** is used consistently.
  The devices that connect to it are referred to as **Wireguard Peers** or simply **Peers**

## Introduction

Wireguard Gateway (WGW) is an element to which peers can connect and form a VPN over the public internet. It's built on top of the [Wireguard](https://www.wireguard.com/) implementation.

## Creating a WGW

### Step 1: Create a Network

Follow [this guide](https://developers.telnyx.com/docs/network/networks).

### Step 2: Check for Coverage

Follow [this guide](https://developers.telnyx.com/docs/network/coverage). Use `filter[available_services][contains]=cloud_vpn` to look for a desired site at which to deploy the WGW. `ashburn-va` is chosen for the subsequent steps.

### Step 3: Create a WGW

Using the network created from Step 1 and the chosen region from Step 2, create the WGW.

<Callout type="warning">
  Once a WGW is created on a specific network, it cannot be "migrated" to another one; it needs to be recreated on the other network. Double check the correct `network_id` is used in the following API request.

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

It's not yet ready to be used immediately after the creation since its status is `provisioning`.

```
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

* `endpoint` denotes the publicly routable IP to which peers will connect over the public internet.
* `server_ip_address` is the private subnet range the WGW and peers will use with WGW occupying the first usable IP.

### Step 4: Wait for Status Transition

The expected time for `status` to transition to `provisioned` is approximately 5 minutes. You can poll the WGW to check for `status`.

```
GET /v2/wireguard_interfaces/b6a10cb9-6c1a-40bd-96e3-d4f8eb2bd6c5 HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

## Creating Peers

In the following example, a peer is created for the WGW from the previous section.

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

In the response, you are given the key pair with which to configure your peer. `private_key` is only given to you **ONCE** in the creation API response. It must be stored by you.

```
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

Simpler still, you may use the following API to obtain the `conf` file template.

```
GET /v2/wireguard_peers/7fc4c14e-ff94-4a97-b156-35f1feeb29b8/config HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

After inserting the `private_key`, you can import the `conf` file on the peer.

```bash theme={null}


## Related Pages

- [Internet Gateway (IGW)](../runbooks/internet-gateway-igw.md)
- [Private Wireless Gateway (PGW)](../runbooks/private-wireless-gateway-pgw.md)
