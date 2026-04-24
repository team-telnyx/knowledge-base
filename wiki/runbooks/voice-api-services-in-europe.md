---
title: Voice API Services in Europe
summary: Telnyx's Voice API Services in Europe provides developers with a way to build voice-based applications and services.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
    content_hash: 346bc2d397768be90765c65e590a6240be82954df41fce4cb95fa3dd8ca5e69f
updated_at: 2026-04-10T00:00:00Z
---

# Voice API Services in Europe

Telnyx's Voice API Services in Europe provides developers with a way to build voice-based applications and services. With this API, you can access our voice network and make calls to any destination in the world.

## Overview

Telnyx now has a dedicated endpoint - [https://api.telnyx.eu](https://api.telnyx.eu), that can be used to help reduce the latency on calls held in Europe.

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```bash theme={null}
curl --location --request POST 'https://api.telnyx.com/v2/calls' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data-raw '{
    "to":"+18727726004",
    "from":"+18022455739",
    "connection_id":"1684641123236054244"
    }'
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

To receive Voice API calls in Europe, Telnyx users should set the AnchorSite® for the application to one of the European Anchorsites—either Frankfurt, London or Amsterdam.

Users can change the AnchorSite® on any given application by editing their existing application and scrolling to the AnchorSite® Selection filed, as below:

<img alt="Voice API services in Europe" />

> Please note that all the participants of the conferences and the calls to add to the queue must be in the same region.
