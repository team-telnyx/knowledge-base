---
title: VXC API
summary: The API resource in question is `/v2/virtual_cross_connects`.
sources:
  - url: https://developers.telnyx.com/docs/network/vxc/api/index
    content_hash: b26cc3eb09eebed7af8a884580cf5f83ec774b19d5f42d3137f06819d87374cf
updated_at: 2026-04-10T00:00:00Z
---

# VXC API

The API resource in question is `/v2/virtual_cross_connects`. The following group of parameters needs to be provided regardless of the cloud provider.

| Parameter    | Value                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `network_id` | A VXC must be associated with a network. If no network exists on your account, you need to [create one](https://developers.telnyx.com/docs/network/networks) first. |
| `name`       | Human readable text; something meaningful to you.                                                                                                                   |

The rest of the parameters are cloud provider specific. Please consult the subsequent sections.
