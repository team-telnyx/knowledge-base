---
title: "Update Webhook Sign Key Guide"
summary: "This article explains how to rotate the public key that signs webhook events sent by Telnyx in API V2. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--8370064-update-webhook-sign-key-guide.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--8370064-update-webhook-sign-key-guide.md -->

# Update Webhook Sign Key Guide

This article explains how to rotate the public key that signs webhook events sent by Telnyx in API V2. See Telnyx guidance and requirements.




## How to update the Public Key used to sign webhook events

Telnyx signs the webhook events it sends to clients so that the authenticity of the request can be verified. Webhook signing in API V2 uses public key encryption.

The public key is available to you in the [Mission Control Portal](https://portal.telnyx.com/#/app/account/public-key) under account settings in the left hand navigation bar > Keys & Credentials > Public Key sub tab.

If your public key has been compromised and you need to update it, or if you would like to rotate it as a regular practice, please follow the steps outlined in this article.

This article will explain:

1. How to create a new inactive public key.
2. How to activate the new public key.

---

## Step 1 - Creating an inactive public key

To create a new inactive public signing key, run the following curl command in a terminal or import it into Postman:

```
curl -X POST https://api.telnyx.com/v2/inactive_key -H "Authorization: Bearer $API_KEY"
```

**Note:** Replace $API\_KEY with your Telnyx API V2 key.

If the request succeeds, you will receive a response similar to this:

```
{
    "data": {
        "id": "a896de0d-b250-450d-8ac4-ca901dcc73d6",
        "public": "iGtB96aTJO4SmJPzRPqW20Zc10AWCiN8OQLE5Tg330U=",
        "record_type": "public_key"
    }
}
```

Take note of the `"id"` field since it will be required in order to activate this key in the next step.

## Step 2 - Activating the inactive public key

Once you are ready to rotate the existing public key, you will activate the key you created in the previous step. To achieve this, run the following curl command in a terminal or import it into Postman:

```
curl -X POST https://api.telnyx.com/v2/inactive_key/a896de0d-b250-450d-
8ac4-ca901dcc73d6/activate -H "Authorization: Bearer $API_KEY"
```

**Note:** Replace $API\_KEY with your Telnyx API V2 key.

The key is referenced by its `"id"`, which you received in the previous step. You can use the example below and replace `{id}` with the actual value:

```
https://api.telnyx.com/v2/inactive_key/{id}/activate
```

If the activation is successful, you will receive a response similar to this:

```
{
    "data": {
        "result": "success"
    }
}
```

And that's it! You have successfully updated your public signing key.

---

## Important notes

Some important notes regarding public signing key rotation:

1. Only 1 inactive key can be added to an organization (managed account). Subsequent requests to create a new inactive key will override the previous inactive key
2. Activation of inactive keys is not immediate and can take up to 60 minutes to propagate across the entire account. There is a period of time that both (current and new) keys could be active at the same.
