---
title: 'Telnyx Cloud Storage: Bucket Operations (S3-Compatible)'
summary: How to create, inspect, list, configure versioning for, and delete S3‑compatible
  buckets on Telnyx Cloud Storage, including supported headers, XML elements, naming
  rules, and example requests/responses.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
  content_hash: 326c06e96f637f4fcc6e16d21f6c2bf56089388fc9d219ad6c7f2ce10ecb2e5c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
  content_hash: fe528c18246d7031f8b9c75ca8d69a0c56f2e8b293935576eab066afff039ec8
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
  content_hash: 9837d27028df063ac73c6cdd615029f089a59d660e92e75582a81b15caac014b
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
  content_hash: fe2628ba885f90d8954f22a05c197acf3754a4c7733e0c64293cb1e2f803c235
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
  content_hash: 82557fa197c5ffebe3f32e9006b5be711f9cdf72d4527535397334912006f016
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
  content_hash: 2b83456768771f3fff43d7ab65601a56a686bfda4eb3407ff0f0da0ede18c2ac
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
  content_hash: ab7db45408ecd463eed7f37cdbf532758a6240dcaec649fb9d570e12bd4d4a61
updated_at: 2026-05-19T15:59:51Z
---

# Telnyx Cloud Storage: Bucket Operations (S3-Compatible)

How to create, inspect, list, configure versioning for, and delete S3‑compatible buckets on Telnyx Cloud Storage, including supported headers, XML elements, naming rules, and example requests/responses.

## Overview
Telnyx Cloud Storage provides S3‑compatible bucket APIs at regional endpoints such as [region].telnyxcloudstorage.com. Requests are signed with AWS Signature Version 4. The examples below show the on‑wire HTTP and XML that Telnyx accepts and returns for common bucket operations.

## Create a bucket
Supported header: x-amz-acl with values:
- private
- public-read

Supported XML element in the request body:
- LocationConstraint

Example request:
```
PUT /mybucket HTTP/1.1
Host:  [region].telnyxcloudstorage.com
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

## Bucket naming and region rules
- Bucket location is inherited from the regional endpoint you use for CreateBucket. If you include LocationConstraint, it must match the region of the endpoint or an error is returned.
- Bucket names must be globally unique, follow DNS naming, and:
  - cannot be an IP address
  - length: 3–63 characters
  - no uppercase letters or underscores
  - start with a lowercase letter or number
  - may include dashes (-)
  - consist of one or more labels separated by single dots (.), each label starting and ending with a lowercase letter or number

Example InvalidLocationConstraint error:
```
<?xml version="1.0" encoding="UTF-8"?>
<Error>
    <Code>InvalidLocationConstraint</Code>
    <Message>The specified location-constraint is not valid</Message>
    <BucketName>mybucket</BucketName>
    <RequestId>tx00000e9df2217c8f5a351-00651445e0-e3e7-fl1</RequestId>
    <HostId>e3e7-fl1-us-east-1</HostId>
</Error>
```

Example InvalidBucketName error:
```
<?xml version="1.0" encoding="UTF-8"?>
<Error>
    <Code>InvalidBucketName</Code>
    <BucketName>invalidBucket</BucketName>
    <RequestId>tx0000040523d3a2d1ba956-006514716b-e3a0-fl1</RequestId>
    <HostId>e3a0-fl1-us-east-1</HostId>
</Error>
```

## Check bucket existence (HeadBucket)
Example request:
```
HEAD /versionedbucket HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T174619Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=8cf0e5ebf1a74d2607aa36eb085659f696de84dd491a4b62adaf584572c8e90b
```

Example response:
```
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

## List buckets (ListBuckets)
Example request:
```
GET / HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T165213Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=5e8edce90f122eaf3810bb5934d8a4208530da8fe9bf634a1950f5eb49bf6197
```

Example response:
```
<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyBucketsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Owner>
        <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
        <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
    </Owner>
    <Buckets>
        <Bucket>
            <Name>mybucket</Name>
            <CreationDate>2023-09-27T15:15:47.026Z</CreationDate>
        </Bucket>
        <Bucket>
            <Name>publicbucket</Name>
            <CreationDate>2023-09-27T15:50:14.996Z</CreationDate>
        </Bucket>
        <Bucket>
            <Name>testpostdeploybxx</Name>
            <CreationDate>2023-09-26T14:26:19.996Z</CreationDate>
        </Bucket>
        <Bucket>
            <Name>versionedbucket</Name>
            <CreationDate>2023-09-27T16:51:50.678Z</CreationDate>
        </Bucket>
    </Buckets>
</ListAllMyBucketsResult>
```

## Get bucket location (GetBucketLocation)
Example request:
```
GET /versionedbucket?location=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T170849Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=107fa2b75c0af7f1982923de787b767f407718c4f1eb19937ff3445f2c0be332
```

Example response:
```
<?xml version="1.0" encoding="UTF-8"?>
<LocationConstraint xmlns="http://s3.amazonaws.com/doc/2006-03-01/">us-east-1</LocationConstraint>
```

## Get bucket versioning (GetBucketVersioning)
Example request:
```
GET /versionedbucket?versioning=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T165704Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=8d8723b48a60f1fef06b43a2f34ca9f4426efa5ae01f9dce8fcc49cba893b69e
```

Example response:
```
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Status>Enabled</Status>
    <MfaDelete>Disabled</MfaDelete>
</VersioningConfiguration>
```

## Set bucket versioning (PutBucketVersioning)
Supported XML element:
- Status

Example request:
```
PUT /versionedbucket?versioning=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T165559Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=b9e0ced3fbf8e42c75b98f84c91758b74916b5bfe2d8a0208a67dffdbcb168e2
Content-Length: 167

<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Status>Enabled</Status>
</VersioningConfiguration>
```

## Delete a bucket (DeleteBucket)
Example request:
```
curl --location --request DELETE 'https:// [region].telnyxcloudstorage.com/[bucket_name]' \
--header 'X-Amz-Date: 20230927T175031Z' \
--header 'Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=06c306e4a75de6aa98a875cfe76ee3977a1c99d60aee86b6db1f53a47539d464'
```
