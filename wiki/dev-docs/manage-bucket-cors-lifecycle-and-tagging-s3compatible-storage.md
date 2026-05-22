---
title: Manage bucket CORS, lifecycle, and tagging (S3‑Compatible Storage)
summary: Configure, retrieve, and remove CORS rules, lifecycle policies, and bucket
  tags on Telnyx S3‑compatible buckets using standard S3 APIs and the AWS CLI, with
  ready‑to‑use request and response examples.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
  content_hash: 594fe337415df9881f480b8b920b9279be76e9ec7865d0f7c7c5f7f8145bcde4
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
  content_hash: 64ab508bc29a34349dac69289a9b734888e98d4564367adcef355311382fb9a3
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
  content_hash: 777d7464c9d641ee5c0a8e5f591d92a0e1d4e07e77f62a14332fbfd5bc5c8275
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
  content_hash: ee590c27de6f82dd5ff35aaef574ed96fccdca23b86ad652c7aa24d5b5bb8609
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
  content_hash: e2850199fdbf98dd0713691d12a275b1e2ca6a441d1e1dc970f56f6be0930ab9
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
  content_hash: 3a79f4d17cebfaf6ea236b2d682bf5229f7b84643d420e32262aeac42778845e
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
  content_hash: b3a92fdfe6e7eb56c080455f60df5756a5529d4c0b0e5ccb8b65d4e284c0e2ef
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
  content_hash: f68877e56a6fcdc19a2d6b4a9a76dab74a863d0501dbea639e116fae8615597c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
  content_hash: 6e200b58d05df83954f5ad2f7b61d4621ca9d77e92690f028789b2f27de1422d
updated_at: 2026-05-19T16:02:52Z
---

# Manage bucket CORS, lifecycle, and tagging (S3‑Compatible Storage)

Configure, retrieve, and remove CORS rules, lifecycle policies, and bucket tags on Telnyx S3‑compatible buckets using standard S3 APIs and the AWS CLI, with ready‑to‑use request and response examples.

## Prerequisites

- Telnyx Cloud Storage is S3‑compatible; operations mirror AWS S3.
- Authenticate with AWS Signature V4 and target your regional endpoint, for example: https://[region].telnyxcloudstorage.com.
- When using AWS CLI, pass your Telnyx credentials and, if needed, the --endpoint-url for your region. See [Authentication](authentication.md) and [API Endpoints & Organization](api-endpoints-organization.md).

## CORS configuration

Use CORS rules to control which origins and methods can access your bucket from browsers.

- Put CORS (apply rules)

  Prepare a JSON file (cors.json):

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

  Apply it:

  aws s3api put-bucket-cors \
    --bucket my_bucket \
    --cors-configuration file://cors.json

- Get CORS

  aws s3api get-bucket-cors --bucket my_bucket

  Example output:

  {
      "CORSRules": [
          {
              "AllowedHeaders": ["*"],
              "AllowedMethods": ["PUT", "DELETE", "POST"],
              "AllowedOrigins": ["http://www.example.com"]
          },
          {
              "AllowedMethods": ["GET"],
              "AllowedOrigins": ["*"]
          }
      ]
  }

- Delete CORS

  aws s3api delete-bucket-cors \
    --bucket my_bucket \
    --endpoint-url https://[region].telnyxcloudstorage.com

See also [AWS S3 Compatibility](aws-s3-compatibility.md) for schema compatibility notes.

## Lifecycle configuration

Create policies to expire objects, transition versions, or abort incomplete multipart uploads.

Supported XML elements include: ID, Status, Prefix, Expiration, AbortIncompleteMultipartUpload.

- Get lifecycle configuration (HTTP example)

  GET /versionedbucket?lifecycle=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  X-Amz-Date: 20230927T172450Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=... 

  Example response:

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

- Put lifecycle configuration (non‑versioned bucket)

  PUT /mybucket?lifecycle=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  Content-Type: application/xml
  X-Amz-Content-Sha256: ...
  X-Amz-Date: 20230927T171857Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

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

- Put lifecycle configuration (versioned bucket)

  PUT /versionedbucket?lifecycle=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  Content-Type: application/xml
  X-Amz-Content-Sha256: ...
  X-Amz-Date: 20230927T172104Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

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

- Delete lifecycle configuration

  DELETE /versionedbucket?lifecycle=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  X-Amz-Date: 20230927T173847Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

For versioning behavior, see [Put bucket versioning](put-bucket-versioning.md).

## Bucket tagging

Attach key/value tags to organize and track buckets.

- Get bucket tagging

  GET /versionedbucket?tagging=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  x-amz-acl: private
  X-Amz-Date: 20230927T182418Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

  Example response:

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

- Put bucket tagging

  PUT /versionedbucket?tagging=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  x-amz-acl: private
  Content-Type: application/xml
  X-Amz-Content-Sha256: ...
  X-Amz-Date: 20230927T182056Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

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

- Delete bucket tagging

  DELETE /versionedbucket?tagging=null HTTP/1.1
  Host:  [region].telnyxcloudstorage.com
  Accept: text/xml
  x-amz-acl: private
  X-Amz-Date: 20230927T182455Z
  Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, ...

## Related pages

- [Quick Start Guide](quick-start-guide.md)
- [Authentication](authentication.md)
- [API Endpoints & Organization](api-endpoints-organization.md)
- [Bucket Addressing](bucket-addressing.md)
- [AWS S3 Compatibility](aws-s3-compatibility.md)
- [Put bucket versioning](put-bucket-versioning.md)
