---
title: Bucket operations
summary: Reference for the S3-compatible bucket operations supported by Telnyx Cloud
  Storage, covering create, delete, head, and various get/delete subresource operations
  (ACL, CORS, lifecycle, location, policy, tagging, versioning).
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
updated_at: 2026-08-05T13:38:25Z
---

# Bucket operations

*Part 1 of 2 — see also: [Part 2](bucket-operations--part-2.md)*

Reference for the S3-compatible bucket operations supported by Telnyx Cloud Storage, covering create, delete, head, and various get/delete subresource operations (ACL, CORS, lifecycle, location, policy, tagging, versioning).

## Overview

Telnyx Cloud Storage exposes an S3-compatible API for managing buckets. The operations below mirror the corresponding Amazon S3 actions and are documented against the regional endpoint `[region].telnyxcloudstorage.com`. Requests are signed with AWS Signature Version 4 using your Telnyx API key as the credential.

For the upstream S3 specifications that Telnyx implements, see the [Amazon S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Bucket.html).

## CreateBucket

Creates a new bucket. The bucket's location is inherited from the regional endpoint used in the request. If `LocationConstraint` is supplied in the request body, its value must match the region of the endpoint, otherwise an `InvalidLocationConstraint` error is returned.

**Supported headers**

- `x-amz-acl` — values: `private`, `public-read`

**Supported XML elements**

- `LocationConstraint`

**Example request**

```http
PUT /mybucket HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T152207Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=eb67629c5cd507c56c5c5447323cc0190c605ab87c2b2fd3046825ca09a28425
Content-Length: 197

<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <LocationConstraint>us-east-1</LocationConstraint>
</CreateBucketConfiguration>
```

**Location constraint mismatch error**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Error>
    <Code>InvalidLocationConstraint</Code>
    <Message>The specified location-constraint is not valid</Message>
    <BucketName>mybucket</BucketName>
    <RequestId>tx00000e9df2217c8f5a351-00651445e0-e3e7-fl1</RequestId>
    <HostId>e3e7-fl1-us-east-1</HostId>
</Error>
```

**Bucket naming rules**

Bucket names should follow domain name constraints:

- Must be unique.
- Cannot be formatted as an IP address.
- Must be between 3 and 63 characters long.
- Must not contain uppercase characters or underscores.
- Must start with a lowercase letter or number.
- Can contain a dash (`-`).
- Must be a series of one or more labels separated by a single period (`.`). Each label must start and end with a lowercase letter or a number, and may contain lowercase letters, numbers, and hyphens.

Violating these rules returns an `InvalidBucketName` error:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Error>
    <Code>InvalidBucketName</Code>
    <BucketName>invalidBucket</BucketName>
    <RequestId>tx0000040523d3a2d1ba956-006514716b-e3a0-fl1</RequestId>
    <HostId>e3a0-fl1-us-east-1</HostId>
</Error>
```

See the upstream [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) reference for additional details.

## HeadBucket

Determines whether a bucket exists and is accessible. The response includes Ceph RGW (`x-rgw-*`) headers reporting storage usage and quota information.

**Example request**

```http
HEAD /versionedbucket HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T174619Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=8cf0e5ebf1a74d2607aa36eb085659f696de84dd491a4b62adaf584572c8e90b
```

**Example response**

```http
HTTP/1.1 200 OK
content-length: 0
date: Wed, 27 Sep 2023 17:48:02 GMT
x-amz-request-id: tx000007a82340b0a467215-0065146ad2-e3bf-fl1
x-rgw-bytes-used: 608686
x-rgw-object-count: 4
x-rgw-quota-bucket-objects: -1
x-rgw-quota-bucket-size: -1
x-rgw-quota-max-buckets: 1000
x-rgw-quota-user-objects: -1
x-rgw-quota-user-size: -1
server: Telnyx API
```

See the upstream [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) reference.

## DeleteBucket

Permanently deletes a bucket. The bucket must be empty before it can be removed.

**Example request**

```bash
curl --location --request DELETE 'https://[region].telnyxcloudstorage.com/[bucket_name]' \
--header 'X-Amz-Date: 20230927T175031Z' \
--header 'Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=06c306e4a75de6aa98a875cfe76ee3977a1c99d60aee86b6db1f53a47539d464'
```

See the upstream [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) reference.

## GetBucketLocation

Returns the region in which the bucket resides.

**Example request**

```http
GET /versionedbucket?location=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T170849Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=107fa2b75c0af7f1982923de787b767f407718c4f1eb19937ff3445f2c0be332
```

**Example response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LocationConstraint xmlns="http://s3.amazonaws.com/doc/2006-03-01/">us-east-1</LocationConstraint>
```

See the upstream [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html) reference.

## GetBucketAcl

Returns the access control list (ACL) for a bucket.

**Example request**

```http
GET /versionedbucket?acl=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: public-read
X-Amz-Date: 20230927T174306Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=050c7795578015f9b3f51bc6d3785d90f7394e5ef7e611ebb6ede54802faa996
```

**Example response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Owner>
        <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
        <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
                <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
            </Grantee>
            <Permission>READ</Permission>
        </Grant>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
                <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
                <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
            </Grantee>
            <Permission>FULL_CONTROL</Permission>
        </Grant>
    </AccessControlList>
</AccessControlPolicy>
```

See the upstream [GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html) reference.

## GetBucketCors

Returns the CORS configuration for a bucket.

**Example request**

```bash
aws s3api get-bucket-cors --bucket my_bucket
```

**Example response**

```json
{
    "CORSRules": [
        {
            "AllowedHeaders": [
                "*"
            ],
            "AllowedMethods": [
                "PUT",
                "DELETE",
                "POST"
            ],
            "AllowedOrigins": [
                "http://www.example.com"
            ]
        },
        {
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ]
        }
    ]
}
```

## DeleteBucketCors

Removes the CORS configuration from a bucket.

**Example request**

```bash
aws s3api delete-bucket-cors --bucket chatgpt-bucket-1696358562 --profile us-east-1.telnyxcloudstorage.com --endpoint-url https://us-east-1.telnyxcloudstorage.com
```
