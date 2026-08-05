---
title: Networks
summary: A `network` instance is a prerequisite for the creation of all other elements
  in the Telnyx platform. This page describes how to create a network via the API.
sources:
- url: https://developers.telnyx.com/docs/network/networks
updated_at: 2026-08-05T13:58:41Z
---

# Networks

A `network` instance is a prerequisite for the creation of all other elements in the Telnyx platform. This page describes how to create a network via the API.

## Overview

A `network` instance is a prerequisite for the creation of all other elements in the Telnyx platform.

## Create a network

The following example shows how to create a new network. Remember to replace `YOUR_API_KEY` with your actual API key.

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

A successful response returns the created network resource:

```
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

The response includes the network's unique `id`, the `name` you provided, timestamps for `created_at` and `updated_at`, and a `record_type` of `network`.

## API reference

For full details on the create network endpoint, including all available parameters and response fields, see the [API reference](https://developers.telnyx.com/api-reference/networks/create-a-network).
