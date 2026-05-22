---
title: Bucket ACLs and Policies (S3-Compatible Storage)
summary: How to view and update Telnyx S3‑compatible bucket access controls using
  ACLs and bucket policies, with REST and AWS CLI examples, supported headers, and
  public access checks.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
  content_hash: ca56825b92b6c41c73c641eec4964cf3411a71a4198f5409b799a0d38fc14ae3
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
  content_hash: 97a1667010203728d9751b55be7ef727d5c897ad6bab3df855ad1d55298a5b87
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
  content_hash: 1b3ec565a514ba7e38939830177fe651a4783d8c1ec1779ce7a56a7f4face90a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
  content_hash: 7e600abd20a26051fe87fed576f9e628b4fb27fddc0c7b498d88caa1f7fbed41
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
  content_hash: c0b1b8fefce2fed46577b9ba63b3195f70605d0427695b87d58ea5f56e804a35
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
  content_hash: 3e5871c2c8ea78827c257542f4cd932c85200117750b32546e5083e37dcde36a
updated_at: 2026-05-19T16:01:22Z
---

# Bucket ACLs and Policies (S3-Compatible Storage)

How to view and update Telnyx S3‑compatible bucket access controls using ACLs and bucket policies, with REST and AWS CLI examples, supported headers, and public access checks.

## What you can control
- Bucket ACLs (Access Control Lists): simple, canned permissions applied at the bucket level. Telnyx supports the x-amz-acl header values private and public-read.
- Bucket policies: JSON documents that define fine-grained permissions (who can perform which actions on which resources). Useful for enabling public read access to objects. See AWS references: GetBucketAcl, PutBucketAcl, GetBucketPolicy, PutBucketPolicy, DeleteBucketPolicy, GetBucketPolicyStatus.

## Requirements and authentication
- Updating bucket policies requires a verified account (KYC). To verify, use the Telnyx Portal Account Verifications page.
- Telnyx Cloud Storage uses AWS Signature Version 4 for authentication. Sign requests with your Telnyx API key as credentials.
- Endpoint pattern: [region].telnyxcloudstorage.com.
- The AWS CLI s3api commands work with Telnyx’s S3‑compatible API when pointed at the appropriate endpoint/credentials.

## Get a bucket’s ACL (REST)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html

Example request:
```
GET /your-bucket?acl HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T174306Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=...
```

Example response (truncated):
```
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

## Set a bucket’s ACL (REST)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html

Supported header: x-amz-acl with values:
- private
- public-read

Example request:
```
PUT /your-bucket?acl HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: public-read
X-Amz-Date: 20230927T174201Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=...
```

## Get a bucket policy (AWS CLI)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html

Example command (prints the policy JSON):
```
aws s3api get-bucket-policy --bucket your-bucket
```

## Put a bucket policy (AWS CLI)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html

1) Create a local policy file (for example, to allow public read of all objects in a bucket):
- Version: 2012-10-17
- Statement:
  - Sid: PublicReadGetObject
  - Effect: Allow
  - Principal: *
  - Action: s3:GetObject
  - Resource: arn:aws:s3:::<your-bucket-name>/*

2) Apply the policy:
```
aws s3api put-bucket-policy --bucket your-bucket --policy file://public_read_policy.json
```

Note: Only verified (KYC) Telnyx accounts can update bucket policies.

## Delete a bucket policy (AWS CLI)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html

Example command:
```
aws s3api delete-bucket-policy --bucket your-bucket
```

## Check bucket policy status (AWS CLI)
Reference: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html

Example command (returns whether a bucket’s policy makes it public):
```
aws s3api get-bucket-policy-status --bucket your-bucket
```
The response includes PolicyStatus.IsPublic set to true or false.

## Making a bucket publicly readable
You can enable public read of objects in two ways:
- ACL approach: Set the bucket ACL to public-read using x-amz-acl.
- Policy approach: Attach a bucket policy that allows Action s3:GetObject on Resource arn:aws:s3:::<your-bucket-name>/* with Principal set to *.

Caution: Public read allows anyone on the internet to GET objects in the bucket. Validate with the policy status command and review your security posture before enabling public access.
