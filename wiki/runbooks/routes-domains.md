---
title: Routes & Domains
summary: Configure custom domains, URL routing, and placement for Edge Compute functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
    content_hash: 7e773eec1d11d33ee1ae9e0382ee4d2d8556d47f62b4fc4ee29eb1b80f52041b
updated_at: 2026-04-10T00:00:00Z
---

# Routes & Domains

Configure custom domains, URL routing, and placement for Edge Compute functions.

After deploying a function with `telnyx-edge ship`, your function is automatically assigned a public URL that makes it accessible from the internet.

## Public URL Patterns

Every deployed function receives a unique public URL based on your function name and organization:

```
https://{funcName}-{orgId}.telnyxcompute.com
```

For development environments, URLs use the `.dev` subdomain:

```
https://{funcName}-{orgId}.dev.telnyxcompute.com
```

### URL Components

| Component  | Description                                     |
| ---------- | ----------------------------------------------- |
| `funcName` | The function name specified in your `func.toml` |
| `orgId`    | Your Telnyx organization identifier             |

### Example

If your function is named `hello-world` and your organization ID is `abc123`, your production URL would be:

```
https://hello-world-abc123.telnyxcompute.com
```

## Accessing Your Functions

Once deployed, your function can handle HTTP requests at its public URL:

```bash theme={null}
