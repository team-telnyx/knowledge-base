---
title: Authentication
summary: Learn how to authenticate with Telnyx Storage using API keys and AWS Signature Version 4 for secure API requests.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/authentication/index
    content_hash: 7fcafd72ec1dd070f280e97c6f8c2b62604914fb9d4166c2888423f155103bda
updated_at: 2026-04-10T00:00:00Z
---

# Authentication

Learn how to authenticate with Telnyx Storage using API keys and AWS Signature Version 4 for secure API requests.

API requests are authenticated with [API Keys](https://portal.telnyx.com/#/api-keys).

Telnyx Storage requires passing an <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html">AWS Signature Version 4 authorization header</a> in the API request. Telnyx Storage also requires that the Telnyx API key is substituted into the authorization header as the `access-key-id`. When an API request is made, Telnyx will parse the API key from the header, validate it, and then authorize the request.

The remaining components of the authorization header (`date`, `aws-region`, `aws-service`, `secret-key`) are irrelevant to us. These values, as well as the generated signature from the secret key are all ignored. They only remain in the authorization header to maintain S3 compatibility. As long as you are passing an AWS Signature Version 4 authorization header, and the Telnyx API key is substituted into the header as the `access-key-id`, the request can be authenticated.

An example is shown below, where `{{your_telnyx_api_key_here}}` is where you will substitute in your Telnyx API Key:

```bash theme={null}
Authorization: AWS4-HMAC-SHA256 
Credential={{your_telnyx_api_key_here}}/20221129/us-east-1/s3/aws4_request, 
SignedHeaders=host;range;x-amz-date,
Signature=d82d11938fe5edf39a778ec710ac79899bae1d9a46ae36607be30fb55f655a3c
```

<Callout type="info">
  After pasting the above content, remove any new line added.

## AWS CLI and S3 third party applications

A general rule of thumb when trying to use Telnyx Storage with a third party application is:

* `Access Key` → substitute in the Telnyx API token
* `Secret Access Key` → either leave blank, or type something random in as a placeholder, or duplicate Telnyx API tokens


## Related Pages

- [API Authentication](../reference/api-authentication.md)
- [CLI Authentication](../reference/cli-authentication.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
- [Legacy CLI Authentication](../reference/legacy-cli-authentication.md)
- [SIP Authentication Methods](../runbooks/sip-authentication-methods.md)
