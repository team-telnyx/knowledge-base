---
title: Cloud Storage API Reference
summary: Reference documentation for Telnyx Cloud Storage S3-compatible API operations,
  covering bucket configuration, multipart uploads, and object management endpoints
  with example requests and responses.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object/index
updated_at: 2026-08-05T13:38:44Z
---

# Cloud Storage API Reference

*Part 2 of 4 — see also: [Part 1](cloud-storage-api-reference--part-1.md), [Part 3](cloud-storage-api-reference--part-3.md), [Part 4](cloud-storage-api-reference--part-4.md)*

Reference documentation for Telnyx Cloud Storage S3-compatible API operations, covering bucket configuration, multipart uploads, and object management endpoints with example requests and responses.

## Bucket operations

### ListBuckets

Returns a list of all buckets owned by the authenticated account. See the [ListBuckets S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html).

**Example request:**

```http
GET / HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T165213Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=5e8edce90f122eaf3810bb5934d8a4208530da8fe9bf634a1950f5eb49bf6197
```

**Example response:**

```xml
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

### PutBucketAcl

Sets the access control list (ACL) on a bucket. See the [PutBucketAcl S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html).

**Supported headers:**

- `x-amz-acl` — accepts `private` or `public-read`

**Example request:**

```http
PUT /versionedbucket?acl=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: public-read
X-Amz-Date: 20230927T174201Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=3e206ed8dfb07bddf453f4735e4685527f2d7fb207ccaf00826353bb21db2164
```

### PutBucketCors

Configures Cross-Origin Resource Sharing (CORS) rules on a bucket. See the [PutBucketCors S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html).

Prepare a JSON file describing the CORS rules:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["http://www.example.com"],
      "AllowedMethods": ["PUT", "POST", "DELETE"],
      "AllowedHeaders": ["*"]
    },
    {
      "AllowedOrigins": ["*"],
      "AllowedMethods": ["GET"]
    }
  ]
}
```

Then apply it to the target bucket using the AWS CLI:

```bash
aws s3api put-bucket-cors --bucket my_bucket --cors-configuration file://cors.json
```

### PutBucketLifecycleConfiguration

Defines lifecycle rules for objects in a bucket, such as automatic expiration. See the [PutBucketLifecycleConfiguration S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html).

**Supported XML elements:**

- `ID`
- `Status`
- `Prefix`
- `Expiration`
- `AbortIncompleteMultipartUpload`

**Example request — non-versioned bucket:**

```http
PUT /mybucket?lifecycle=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T171857Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=bf5f1ef0813a985a4798dbbd63a722555f45a04de648f6bb7e975b4808974d80
Content-Length: 355

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
        <ID>id2</ID>
        <Filter>
            <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        <Expiration>
            <Days>30</Days>
        </Expiration>
    </Rule>
</LifecycleConfiguration>
```

**Example request — versioned bucket:**

```http
PUT /versionedbucket?lifecycle=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T172104Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-content-sha256;x-amz-date, Signature=a831851b8259ffb9e222ef5c755e5e44549972db7643d28f0570ac07b0600401
Content-Length: 436

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
        <ID>DeleteAfterBecomingNonCurrent</ID>
        <Filter>
            <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        <NoncurrentVersionExpiration>
            <NoncurrentDays>100</NoncurrentDays>
        </NoncurrentVersionExpiration>
    </Rule>
</LifecycleConfiguration>
```

### PutBucketPolicy

Attaches a JSON-based access policy to a bucket. See the [PutBucketPolicy S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html).

> **Warning:** Only verified users can update bucket policy. To request KYC on your account, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

The following example creates a bucket where the objects stored in it can be read publicly without authentication. Create a JSON file locally, e.g. `public_read_policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<your-bucket-name>/*"
    }
  ]
}
```

Then apply it to an existing bucket using the AWS CLI:

```bash
aws s3api put-bucket-policy --bucket pubreadbuc --policy file://public_read_policy.json
```

### PutBucketTagging

Adds or updates tags on a bucket. See the [PutBucketTagging S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html).

**Example request:**

```http
PUT /versionedbucket?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T182056Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=7eb598e87b95668e4502fef0694a515e960a98890c30185fc974bea5d8e72fe6
Content-Length: 310

<?xml version="1.0" encoding="UTF-8"?>
<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <TagSet>
      <Tag>
         <Key>dimention_1</Key>
         <Value>value_1</Value>
      </Tag>
      <Tag>
         <Key>dimention_2</Key>
         <Value>value_2</Value>
      </Tag>
   </TagSet>
</Tagging>
```

### PutBucketVersioning

Enables or suspends versioning on a bucket. See the [PutBucketVersioning S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html).

**Supported XML element:**

- `Status`

**Example request:**

```http
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
