---
title: "Webhook Issue: CA Error"
summary: "Join Telnyx's Reseller Program. See Telnyx guidance and requirements Learn more about Webhook Issue: CA Error with Telnyx."
sources:
- url: "https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--8268648-webhook-issue-ca-error.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--8268648-webhook-issue-ca-error.md -->

# Webhook Issue: CA Error

Join Telnyx's Reseller Program. See Telnyx guidance and requirements Learn more about Webhook Issue: CA Error with Telnyx.

K




## Primary Webhook Not Triggering because of Error: certificate authority (CA) isn’t recognized

If the error says the certificate authority (CA) isn’t recognized and your payload is being sent to the failover webhook url instead of the primary then that means the connection can’t be established over https.

We have two options here:

(a) make sure your server has a certificate that is signed by a known CA

or

(b) use http instead of https
​
​[More about Certificate Authority.](https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com)
