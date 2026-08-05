---
title: Making Bucket Public
summary: Explains how to make a Telnyx cloud storage bucket public, including regional
  availability and the verification requirement for this privileged action.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
updated_at: 2026-08-05T13:39:23Z
---

# Making Bucket Public

Explains how to make a Telnyx cloud storage bucket public, including regional availability and the verification requirement for this privileged action.

## Overview

Making a bucket public is supported only for buckets located in the US and APAC (`ap-southeast-1`) regions.

This is a privileged action and must be performed via either a [bucket policy](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index#put-bucket-policy) or an [ACL](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index#put-bucket-acl).

## Prerequisites

Before making a bucket public, you must complete [Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) on your Telnyx account.

## Procedure

1. **Verify your account.** Request and obtain Level 2 verification status.
2. **Apply bucket policy or ACL.** Use the [CLI](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index#put-bucket-policy), API, or SDK to apply the desired policy to your bucket.
