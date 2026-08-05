---
title: Cloud Storage authentication
summary: Telnyx Cloud Storage authenticates API requests using an AWS Signature Version
  4 authorization header in which the Telnyx API key is substituted as the `access-key-id`.
  The remaining SigV4 components are ignored, preserving S3 compatibility for use
  with AWS CLI and other S3-compatible tools.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
updated_at: 2026-08-05T13:38:30Z
---

# Cloud Storage authentication

Telnyx Cloud Storage authenticates API requests using an AWS Signature Version 4 authorization header in which the Telnyx API key is substituted as the `access-key-id`. The remaining SigV4 components are ignored, preserving S3 compatibility for use with AWS CLI and other S3-compatible tools.

## Overview

API requests to Telnyx Cloud Storage are authenticated with [API Keys](https://portal.telnyx.com/#/api-keys). Telnyx Storage requires passing an [AWS Signature Version 4 authorization header](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html) in the API request, with the Telnyx API key substituted into the header as the `access-key-id`. When a request is made, Telnyx parses the API key from the header, validates it, and then authorizes the request.

## Authorization header format

The remaining components of the SigV4 authorization header — `date`, `aws-region`, `aws-service`, and `secret-key` — are not validated by Telnyx. The generated signature from the secret key is also ignored. These values remain in the header only to maintain S3 compatibility. As long as an AWS Signature Version 4 authorization header is passed and the Telnyx API key is supplied as the `access-key-id`, the request will be authenticated.

Example header (substitute your Telnyx API key where indicated):

```
Authorization: AWS4-HMAC-SHA256 Credential={{your_telnyx_api_key_here}}/20221129/us-east-1/s3/aws4_request, SignedHeaders=host;range;x-amz-date, Signature=d82d11938fe5edf39a778ec710ac79899bae1d9a46ae36607be30fb55f655a3c
```

After pasting the above content, remove any new line added.

## AWS CLI and S3 third-party applications

When configuring Telnyx Storage with a third-party application that expects S3-style credentials, use the following mapping:

- `Access Key` — substitute in the Telnyx API token.
- `Secret Access Key` — leave blank, type a random placeholder, or duplicate the Telnyx API token.

This allows standard S3-compatible tools, including the AWS CLI, to be pointed at Telnyx Storage without requiring a real AWS secret key.
