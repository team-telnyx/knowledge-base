---
title: CLI Authentication
summary: Configure your API key for the Telnyx CLI.
sources:
  - url: https://developers.telnyx.com/development/cli/getting-started/authentication
    content_hash: 8ba22da839a8b55f4fe3ade4ca5d22dc6fc025c3517c40a27983d35f294e9240
updated_at: 2026-04-10T00:00:00Z
---

# CLI Authentication

Configure your API key for the Telnyx CLI

The Telnyx CLI authenticates using an API key set via environment variable.

## Setting Your API Key

Set the `TELNYX_API_KEY` environment variable:

```bash theme={null}
export TELNYX_API_KEY=KEY_xxxxxxxxxxxxx
```

  Add this line to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) to persist it across terminal sessions.

## Verify Authentication

Test that your credentials are working by running any command:

```bash theme={null}
telnyx balance retrieve
```

If authenticated successfully, you'll see your account balance. If not, you'll receive an authentication error.

## Getting Your API Key

1. Log in to the [Telnyx Portal](https://portal.telnyx.com/)
2. Navigate to [API Keys](https://portal.telnyx.com/#/app/api-keys)
3. Click **Create API Key**
4. Copy the key (it won't be shown again)

> **Note:** API keys start with `KEY_`. If you're using a v1 API key (starting with a different prefix), you'll need to create a new v2 key.

## Multiple Accounts

If you work with multiple Telnyx accounts (e.g., production and staging), you have several options:

### Option 1: Shell Aliases

Create aliases for different accounts:

```bash theme={null}


## Related Pages

- [API Authentication](../reference/api-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [Legacy CLI Authentication](../reference/legacy-cli-authentication.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
- [Tech Prefix Authentication](../runbooks/tech-prefix-authentication.md)
