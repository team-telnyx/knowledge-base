---
title: Best Practices
summary: Code patterns and configuration guidance for building fast, reliable, and secure edge functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/best-practices/index
    content_hash: fa28957846d556a3664de121b18207814427364666ed3aa3de8646632793f264
updated_at: 2026-04-10T00:00:00Z
---

# Best Practices

Code patterns and configuration guidance for building fast, reliable, and secure edge functions.

Best practices for Edge Compute based on production patterns and common issues.

## Configuration

### Use Environment Variables for Secrets

Never hardcode secrets. Use the secrets API:

```bash theme={null}
telnyx-edge secrets add --name API_KEY --value "sk-..."
```

Access in code:

```javascript theme={null}
const apiKey = process.env.API_KEY;
```

### Set Appropriate Timeouts

Configure timeouts based on your function's needs:

```toml theme={null}


## Related Pages

- [Verify Security Best Practices](../runbooks/verify-security-best-practices.md)
