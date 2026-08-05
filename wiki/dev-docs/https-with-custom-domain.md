---
title: HTTPS with Custom Domain
summary: Walks through configuring a Telnyx Cloud Storage bucket to serve content
  over HTTPS using a custom domain, including bucket creation, public access policy,
  DNS aliasing, and SSL/TLS certificate upload.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
updated_at: 2026-08-05T13:39:31Z
---

# HTTPS with Custom Domain

Walks through configuring a Telnyx Cloud Storage bucket to serve content over HTTPS using a custom domain, including bucket creation, public access policy, DNS aliasing, and SSL/TLS certificate upload.

## Overview

HTTPS with a custom domain is currently supported for buckets located in the US and APAC (`ap-southeast-1`) regions. The setup involves creating a bucket that matches the desired subdomain, making it publicly readable, aliasing the subdomain to the bucket, and uploading a matching SSL/TLS certificate.

## 1. Validate availability of bucket

The subdomain you intend to use must be available as a bucket name. If it is, create the bucket. In the example, the bucket `asset.gardening-homes.com` was created.

![SSL Certificate 1](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-ssl-1.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=2ccf8110ad14474abfa11e903ad59091)

## 2. Make the bucket public

Because the bucket's contents will be publicly accessible, apply a public read policy. See [Put Bucket Policy](put-bucket-policy.md) for instructions.

![SSL Certificate 2](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-ssl-2.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=770ba33003648488efa24afc6b8e7350)

## 3. Configure DNS

Through your domain or DNS provider, set up an alias to the bucket using virtual-host-style addressing. See [Bucket Addressing](bucket-addressing.md) for details.

![SSL Certificate 3](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-ssl-3.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=7b1a33faeae741de287749cded7dc706)

## 4. Upload certificate and matching key

Select the bucket you created and, under **SSL/TLS**, upload the certificate and its matching key.

![SSL Certificate 4](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-ssl-4.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=5865ae094fcd5680447b4bd1d954c428)

When uploading a certificate file, ensure the following:

- The bucket name must match one of the certificate's SNIs (Server Name Indication) exactly. With a wildcard SNI such as `*.example.com`, `help.example.com` will work, but `example.com` will not.
- If intermediate certificates are required, include them in the certificate file with the leaf certificate at the top.
- The root certificate may be omitted because known root certificates are verified automatically. However, including the root certificate is recommended to guarantee acceptance.

## 5. Test

Once the previous steps are complete and an object such as `demo-image.jpg` exists in the bucket, visit `https://asset.gardening-homes.com/demo-image.jpg` in a browser. The expected result is:

- The image loads in the browser.
- The browser reports "Connection is secure" and "Certificate is valid".

![SSL Certificate 5](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-ssl-5.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=79a057d89372af743695b0b8ca725132)
