---
title: Create and Manage API Keys
summary: Step-by-step guide to create, manage, and secure your Telnyx API keys for all services.
sources:
  - url: https://developers.telnyx.com/development/api-fundamentals/create-api-keys/index
    content_hash: 53d1dbb6a9637042b5fe8ed25b7bf3780548fbab440f7d999f8a4c3c645a2534
updated_at: 2026-04-10T00:00:00Z
---

# Create and Manage API Keys

Step-by-step guide to create, manage, and secure your Telnyx API keys for all services.

API keys are essential for authenticating your requests to any Telnyx API. This guide shows you how to create and manage your API keys through the Mission Control Portal.

## Creating Your API Key

1. In the Mission Control Portal, click on your name in the upper right corner, and click **API Keys**.
2. Click the **Create API Key** button.

<img alt="API Keys Page" />

3. In the Create API Key dialog, add a descriptive tag (e.g., "Voice API Development", "SMS Production", etc.) and choose your expiration settings.

<img alt="Create API Key Dialog" />

4. Click **Create**.

## Important: Save Your API Key Securely

<Callout type="warning" title="Security Notice">
  We'll show the full API key value only once at creation. If you lose the key, you'll need to generate a new one.

  We recommend using a secure password manager or secrets vault once you've created it. We're doing this to reduce the risk of accidental key leaks and help keep your account secure. This approach aligns with our best-in-class security standards and helps prevent accidental key exposures.

## Storing Your API Key

**Best Practices:**

* Never commit API keys to version control (Git, SVN, etc.).
* Use environment variables in your applications.
* Rotate keys regularly for production applications.
* Use separate keys for development and production.

Example of setting an environment variable:

```bash theme={null}
export TELNYX_API_KEY="YOUR_API_KEY"
```

## Using Your API Key

Once created, you can use your API key with any Telnyx service:

### REST API

```bash theme={null}
curl -X GET \
  --header "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/endpoint"
```

### SDKs

```javascript theme={null}
// Node.js
const telnyx = require('telnyx')('YOUR_API_KEY');

// Python
import telnyx
telnyx.api_key = "YOUR_API_KEY"

// Ruby
Telnyx.api_key = "YOUR_API_KEY"
```
