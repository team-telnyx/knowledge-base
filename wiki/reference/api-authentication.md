---
title: API Authentication
summary: Authentication methods and security best practices for all Telnyx APIs.
sources:
  - url: https://developers.telnyx.com/development/api-fundamentals/authentication/index
    content_hash: 7dbee8fdb28a2806c370db997c4401e2e7db73d63eabb2fca778375f95764c84
updated_at: 2026-04-10T00:00:00Z
---

# API Authentication

Authentication methods and security best practices for all Telnyx APIs.

All Telnyx APIs use consistent authentication mechanisms to ensure secure access to your resources. This guide covers the universal authentication patterns used across Voice, Messaging, Cloud Storage, IoT, and all other Telnyx services.

## API Keys

### Overview

Telnyx uses API Keys as the primary authentication method across all services. Your API Keys carry significant privileges and provide access to all Telnyx resources associated with your account.

### Security Best Practices

* **Keep API Keys secure**: Never share API Keys in publicly accessible areas such as GitHub, client-side code, or logs
* **Use environment variables**: Store API Keys in environment variables or secure configuration files
* **Rotate keys regularly**: Periodically generate new API Keys and deactivate old ones
* **Use least privilege**: If available, use API Keys with minimal required permissions

### Managing API Keys

You can view and manage your API Keys in the Auth section of your [Mission Control portal](https://portal.telnyx.com).

## Authentication Methods

### Bearer Token Authentication

Most Telnyx APIs use Bearer token authentication in the Authorization header:

```bash theme={null}
curl -X GET \
  --header "Authorization: Bearer YOUR_API_KEY" \
  "https://api.telnyx.com/v2/endpoint"
```

### SDK Authentication

When using Telnyx SDKs, authentication is typically configured once during initialization:

```javascript theme={null}
// Node.js SDK
const telnyx = require('telnyx')('YOUR_API_KEY');

// Python SDK  
import telnyx
telnyx.api_key = "YOUR_API_KEY"

// Ruby SDK
Telnyx.api_key = "YOUR_API_KEY"
```

## Common Authentication Patterns

### RESTful APIs

* **Voice API**: Bearer token in Authorization header
* **Messaging API**: Bearer token in Authorization header
* **Cloud Storage**: AWS Signature Version 4 or Bearer token
* **IoT APIs**: Bearer token in Authorization header

### Real-time Connections

* **WebRTC**: JWT tokens for client authentication
* **WebSocket connections**: Bearer token during connection establishment

## Error Handling

### Authentication Errors

Common authentication-related HTTP status codes:

* **401 Unauthorized**: Invalid or missing API Key
* **403 Forbidden**: Valid API Key but insufficient permissions
* **429 Too Many Requests**: Rate limit exceeded

### Debugging Authentication Issues

1. **Verify API Key format**: Ensure the key is correctly formatted and complete
2. **Check headers**: Confirm the Authorization header is properly set
3. **Validate permissions**: Ensure your API Key has the required permissions for the resource
4. **Test with curl**: Use curl to isolate authentication issues from SDK problems

## Environment-Specific Considerations

### Development vs Production

* Use separate API Keys for development and production environments
* Never use production API Keys in development or testing
* Consider using restricted API Keys for development

### Regional Considerations

Some Telnyx services may have regional API endpoints. Always check the specific service documentation for the correct base URL.

## Account Management

### Account Levels and Access

Account levels determine which APIs and features are available to you. For detailed information about account types, capabilities, and verification requirements, see [Account Levels and Capabilities](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities).

## Next Steps

* **API Reliability & Retries** - Handle authentication failures gracefully
* **Webhook Security** - Secure your webhook endpoints
* **SDKs & Tools** - Language-specific authentication setup


## Related Pages

- [CLI Authentication](../reference/cli-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [Legacy CLI Authentication](../reference/legacy-cli-authentication.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
- [Tech Prefix Authentication](../runbooks/tech-prefix-authentication.md)
