---
title: API Endpoints and Organization
summary: 'Discover Telnyx Cloud Storage API endpoints, regions, S3 compatibility, and API usage instructions.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
    content_hash: 2ed58874a9257b5f5872d0ace8b930041c4ad103c03aedb9e5014c2179af85e5
updated_at: 2026-04-10T00:00:00Z
---

# API Endpoints and Organization

Discover Telnyx Cloud Storage API endpoints: Key details on regions, S3 compatibility, and API usage instructions.

There exists two suites of Storage APIs:

* S3 compatible, and
* JSON companion

## S3 Compatible APIs

This suite of APIs is compatible with AWS S3; as a result, minimal changes to existing integration are needed for migration to Telnyx.

<table>
  <tbody>
    <tr>
      <td><strong>Endpoint URL</strong></td>
      <td>Region</td>
    </tr>

    <tr>
      <td>us-central-1.telnyxcloudstorage.com</td>
      <td>us-central-1</td>
    </tr>

    <tr>
      <td>us-east-1.telnyxcloudstorage.com</td>
      <td>us-east-1</td>
    </tr>

    <tr>
      <td>us-west-1.telnyxcloudstorage.com</td>
      <td>us-west-1</td>
    </tr>

    <tr>
      <td>eu-central-1.telnyxcloudstorage.com</td>
      <td>eu-central-1</td>
    </tr>
  </tbody>
</table>

Any US endpoint can be used for `ListBuckets` and `GetBucketLocation` across all US buckets, while the European endpoint (`eu-central-1`) will return only buckets located in Europe. However, all other API methods need to be directed at the regional endpoint that the bucket is homed. Otherwise an error will be returned. Hence, it is advisable to query the location of the bucket first before forming the correct regional endpoint for all subsequent API operations.

Supported S3 APIs are documented in [this table](compatibility-matrix.md).

## JSON Companion API

This suite of APIs is an extension to the S3 API, accommodating the following functionalities:

* [Querying usage](billing.md)
* [Create presigned URL](presigned-urls.md)
* [Manage SSL](https-with-custom-domain.md)
* [Migrating data from AWS S3](migrating-from-s3.md)

API endpoint to be used is `api.telnyx.com`.
