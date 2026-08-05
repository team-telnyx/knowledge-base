---
title: Bucket Addressing
summary: Bucket addressing in Telnyx Cloud Storage supports both path-style and virtual-hosted-style
  request formats, allowing clients to access objects using either the bucket name
  as a path segment or as a subdomain of the regional endpoint.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
updated_at: 2026-08-05T13:38:50Z
---

# Bucket Addressing

Bucket addressing in Telnyx Cloud Storage supports both path-style and virtual-hosted-style request formats, allowing clients to access objects using either the bucket name as a path segment or as a subdomain of the regional endpoint.

## Path-style requests

`https://[region].telnyxcloudstorage.com/[bucketname]/[objectname]`

## Virtual-hosted-style requests

`https://[bucketname].[region].telnyxcloudstorage.com/[objectname]`
