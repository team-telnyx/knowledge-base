---
title: Edge Compute Configuration
summary: Covers all aspects of configuring Telnyx Edge Compute functions, including
  the func.toml file, environment variables, secrets management, routing, cron triggers,
  deployment versions, and best practices for performance, reliability, security,
  and observability.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-06-11T10:26:17Z
---

# Edge Compute Configuration

*Part 2 of 3 — see also: [Part 1](edge-compute-configuration--part-1.md), [Part 3](edge-compute-configuration--part-3.md)*

Covers all aspects of configuring Telnyx Edge Compute functions, including the func.toml file, environment variables, secrets management, routing, cron triggers, deployment versions, and best practices for performance, reliability, security, and observability.

## Secrets

Secrets are encrypted key-value pairs for storing sensitive configuration data like API keys, database passwords, and authentication tokens. They provide secure storage that is:

- **Encrypted at rest** — Stored with AES-256 encryption
- **Encrypted in transit** — All API calls use HTTPS/TLS
- **Injected at runtime** — Available as environment variables in your functions
- **Organization-scoped** — Shared across all functions in your organization
- **Never displayed** — Secret values are never shown in CLI output or logs

### Adding Secrets

```bash
telnyx-edge secrets add DATABASE_PASSWORD "super-secret-password"
telnyx-edge secrets add PAYMENT_API_KEY "sk_live_abc123"
telnyx-edge secrets add JWT_SECRET "your-jwt-signing-key"
```

### Listing Secrets

```bash
telnyx-edge secrets list
```

This displays secret IDs, names, and creation dates. Secret values are never displayed for security.

### Updating and Deleting Secrets

Use the same `add` command to update an existing secret:

```bash
telnyx-edge secrets add DATABASE_PASSWORD "new-password-456"
```

Delete a secret with:

```bash
telnyx-edge secrets delete OLD_API_KEY
```

### Accessing Secrets in Your Code

Secrets are injected as environment variables when your function runs:

In JavaScript:

```javascript
async function handler(request) {
    const dbPassword = process.env.DATABASE_PASSWORD;
    const apiKey = process.env.PAYMENT_API_KEY;

    if (!dbPassword) {
        return { error: "DATABASE_PASSWORD not configured" };
    }

    const db = await connectDatabase({ password: dbPassword });
    return { status: "connected" };
}
```

In Python:

```python
import os

def handler(request):
    db_password = os.environ.get("DATABASE_PASSWORD")
    api_key = os.environ.get("PAYMENT_API_KEY")

    if not db_password:
        return {"error": "DATABASE_PASSWORD not configured"}

    db = connect_database(password=db_password)
    return {"status": "connected"}
```

In Go:

```go
func handler(w http.ResponseWriter, r *http.Request) {
    dbPassword := os.Getenv("DATABASE_PASSWORD")
    apiKey := os.Getenv("PAYMENT_API_KEY")

    if dbPassword == "" {
        http.Error(w, "DATABASE_PASSWORD not configured", 500)
        return
    }
    // Use secrets to connect to services
}
```

### Secret Rotation

Rotate secrets regularly for security compliance:

```bash
# 1. Update the secret with new value
telnyx-edge secrets add DATABASE_PASSWORD "new-secure-password"

# 2. Redeploy functions to pick up the new value
telnyx-edge ship

# 3. Verify the function works with new credentials
curl https://your-function.telnyxcompute.com/health
```

Rotate monthly for security compliance, after suspected credential compromise, after team member offboarding, or when third-party services rotate their keys.

### Secret Naming Conventions

- Use `UPPER_SNAKE_CASE`
- Include service name: `STRIPE_API_KEY`, `TWILIO_AUTH_TOKEN`
- Use standard suffixes: `_KEY`, `_SECRET`, `_TOKEN`, `_PASSWORD`

| ✅ Good | ❌ Avoid |
|---|---|
| `DATABASE_PASSWORD` | `PASSWORD` |
| `STRIPE_API_KEY` | `API_KEY` |
| `JWT_SIGNING_SECRET` | `SECRET` |
| `SENDGRID_API_KEY` | `EMAIL_KEY` |

### Per-Environment Secrets

Per-environment secrets (dev/staging/prod) are planned for a future release. For now, use naming conventions to separate environments:

```bash
telnyx-edge secrets add DEV_DATABASE_PASSWORD "dev-password"
telnyx-edge secrets add PROD_DATABASE_PASSWORD "prod-password"
```

Then reference the appropriate variable in your code based on an environment flag.

### Local Development with Secrets

Local development with secrets (`.env` file support) is planned for a future release. For now, set environment variables manually when testing locally:

```bash
# Linux/macOS
export DATABASE_PASSWORD="local-test-password"
python your_function.py

# Or inline
DATABASE_PASSWORD="test" python your_function.py
```

### Secrets Troubleshooting

- **Secret not found in function**: Check that the secret exists with `telnyx-edge secrets list`. If missing, add it and redeploy with `telnyx-edge ship`.
- **Secret value seems wrong**: Update with `telnyx-edge secrets add MY_SECRET "correct-value"` and redeploy.
- **Permission denied**: Check authentication with `telnyx-edge auth status` or re-authenticate with `telnyx-edge auth login`.

## Environment Variables vs Secrets

| Feature | Environment Variables | Secrets |
|---|---|---|
| **Storage** | Plain text in `func.toml` | Encrypted in Telnyx infrastructure |
| **Scope** | Function-specific | Organization-wide |
| **Version Control** | ✅ Yes (in git) | ❌ No (separate secure storage) |
| **Use Case** | Configuration, feature flags | API keys, passwords, tokens |

**Use environment variables** for non-sensitive configuration:

- Application settings — `LOG_LEVEL`, `DEBUG_MODE`, `PORT`
- Feature flags — `ENABLE_CACHING`, `MAINTENANCE_MODE`
- Performance tuning — `MAX_FILE_SIZE`, `BATCH_SIZE`, `TIMEOUT`
- Public endpoints — `API_BASE_URL`, `CDN_URL`, `WEBHOOK_URL`
- Environment identifiers — `ENVIRONMENT`, `VERSION`, `SERVICE_NAME`

**Use secrets** for sensitive data:

- API keys — `STRIPE_API_KEY`, `TWILIO_API_KEY`
- Database credentials — `DATABASE_PASSWORD`, `REDIS_PASSWORD`
- Authentication tokens — `JWT_SECRET`, `OAUTH_TOKEN`
- Encryption keys — `ENCRYPTION_KEY`, `SIGNING_KEY`

## Routing and Domains

After deploying a function with `telnyx-edge ship`, your function is automatically assigned a public URL that makes it accessible from the internet.

### Public URL Patterns

Every deployed function receives a unique public URL based on your function name and organization:

```
https://{funcName}-{orgId}.telnyxcompute.com
```

For development environments, URLs use the `.dev` subdomain:

```
https://{funcName}-{orgId}.dev.telnyxcompute.com
```

| Component | Description |
|---|---|
| `funcName` | The function name specified in your `func.toml` |
| `orgId` | Your Telnyx organization identifier |

For example, if your function is named `hello-world` and your organization ID is `abc123`, your production URL would be `https://hello-world-abc123.telnyxcompute.com`.

### Accessing Deployed Functions

```bash
# GET request
curl https://my-function-abc123.telnyxcompute.com

# POST request with JSON body
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}' \
  https://my-function-abc123.telnyxcompute.com
```

The `telnyx-edge ship` command displays your function's live URL after successful deployment.

### Custom Domains and Region Placement

Custom domain support and region placement/pinning are both planned for future releases. These will allow you to map your own domains to Edge Compute functions and specify geographic regions where your functions should run for latency optimization or data residency requirements.

## Cron Triggers

Cron triggers are planned for a future release. They will let you schedule your edge functions to run automatically at specified intervals.

Until cron triggers are available, use an external scheduler to call your function's HTTP endpoint. For example, with GitHub Actions:

```yaml
# .github/workflows/cron.yml
name: Scheduled Function Call
on:
  schedule:
    - cron: '0 * * * *'  # Every hour

jobs:
  trigger:
    runs-on: ubuntu-latest
    steps:
      - run: curl -X POST https://my-func-org123.telnyxcompute.com/cron
```
