---
title: Networks
summary: A `network` instance is a prerequisite for the creation of all other elements.
sources:
  - url: https://developers.telnyx.com/docs/network/networks/index
    content_hash: 90c5259ac73df6de72a8e5b10b3782cf4e93c10e3f907acbad0b146e8779ccef
updated_at: 2026-04-10T00:00:00Z
---

# Networks

A `network` instance is a prerequisite for the creation of all other elements.

Here is a sample request:

## Request sample

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```json theme={null}
POST /v2/networks HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
Content-Length: 40

{
  "name": "my_first_virtual_network"
}
```

Here is a sample response:

```json theme={null}
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

API reference is available [here](https://developers.telnyx.com/api-reference/networks/create-a-network).
