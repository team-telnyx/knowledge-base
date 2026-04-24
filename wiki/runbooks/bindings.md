---
title: Bindings
summary: Access Telnyx platform services from your edge functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
    content_hash: 108be1e7c1461246d989b59bdc5cc6cf6666656a85e7596e7ee8074717f85e4f
updated_at: 2026-04-10T00:00:00Z
---

# Bindings

Access Telnyx platform services from your edge functions.

Bindings allow your edge functions to interact with Telnyx platform services. They provide secure, auto-authenticated access without managing API keys in your code.

## Available Bindings

| Binding                                      | Description            | Status         |
| -------------------------------------------- | ---------------------- | -------------- |
| [Voice](https://developers.telnyx.com/docs/voice/programmable-voice)      | Make and receive calls | ✅ Available    |
| [Messaging](https://developers.telnyx.com/docs/messaging)                 | Send SMS/MMS           | ✅ Available    |
| [Phone Numbers](https://developers.telnyx.com/docs/numbers/phone-numbers) | Manage numbers         | ✅ Available    |
| [Fax](https://developers.telnyx.com/docs/programmable-fax)                | Send faxes             | ✅ Available    |
| [Verify](https://developers.telnyx.com/docs/identity/verify)              | 2FA/verification       | ✅ Available    |
| [Cloud Storage](https://developers.telnyx.com/docs/cloud-storage)         | S3-compatible storage  | ✅ Available    |
| KV                                           | Key-value store        | 🔜 Coming soon |
| SQL DB                                       | Serverless database    | 🔜 Coming soon |

## What is a Binding?

When you configure a binding for your function, you grant it the capability to access Telnyx services. The binding handles authentication automatically — your API key is never exposed in your code or logs.

```
Your Function → Binding Proxy → Telnyx API
      ↓              ↓              ↓
  Placeholder    Resolves      Actual API
  API Key        Credentials   Call Made
```

When you deploy a function with an active binding:

1. Your function receives placeholder credentials as environment variables
2. When your code calls the Telnyx SDK, the binding proxy intercepts the request
3. The proxy resolves the placeholder to your real API key
4. The API call proceeds with proper authentication

**Benefits:**

* API key never appears in function code
* API key never appears in logs
* Credentials can be rotated without code changes

## Creating a Binding

One-time setup per organization:

```bash theme={null}
