---
title: Legacy CLI Authentication
summary: Configure API keys and manage multiple profiles in the legacy CLI.
sources:
  - url: https://developers.telnyx.com/development/cli/legacy/authentication
    content_hash: d1fde9e0eafb2182a49196908a10b38bc66c7f2809dd130f75ab4bc469c2991d
updated_at: 2026-04-10T00:00:00Z
---

# Legacy CLI Authentication

Configure API keys and manage multiple profiles in the legacy CLI

> **Warning:** **This CLI is deprecated.** The new [Telnyx CLI](telnyx-cli.md) uses environment variables only (`TELNYX_API_KEY`). Profile management is not available in the new CLI.

## Authentication Methods

The legacy CLI supports three authentication methods, checked in order: flag → environment variable → config file.

### 1. Interactive Setup (Recommended)

```bash theme={null}
telnyx auth setup
```

You'll be prompted to enter your API key. Configuration is stored in `~/.config/telnyx/config.json`.

### 2. Environment Variable

```bash theme={null}
export TELNYX_API_KEY=KEY_xxxxxxxxxxxxx
```

### 3. Command-Line Flag

```bash theme={null}
telnyx number list --api-key KEY_xxxxxxxxxxxxx
```

## Verify Authentication

```bash theme={null}
telnyx auth status
```

Example output:

```
✓ Authenticated

Account:     My Company
Email:       developer@example.com
Balance:     $125.50
Profile:     default
```

## Multiple Profiles

Use named profiles to manage multiple Telnyx accounts or environments.

### Create a Profile

```bash theme={null}
telnyx auth setup --profile production
telnyx auth setup --profile staging
```

### List Profiles

```bash theme={null}
telnyx profile list
```

### Use a Profile

```bash theme={null}
telnyx number list --profile production
telnyx billing balance --profile staging
```

### Set Default Profile

```bash theme={null}
telnyx profile set-default production
```

### Delete a Profile

```bash theme={null}
telnyx profile delete staging
```

## Configuration File

The CLI stores configuration in `~/.config/telnyx/config.json`:

```json theme={null}
{
  "defaultProfile": "production",
  "profiles": {
    "default": {
      "apiKey": "KEY_xxxxxxxxxxxxx"
    },
    "production": {
      "apiKey": "KEY_yyyyyyyyyyyyy"
    },
    "staging": {
      "apiKey": "KEY_zzzzzzzzzzzzz"
    }
  }
}
```

> **Warning:** Keep your config file secure. It contains sensitive API keys. The file is created with restricted permissions (600) by default.

## Environment Variables

| Variable            | Description                     |
| ------------------- | ------------------------------- |
| `TELNYX_API_KEY`    | API key (overrides config file) |
| `TELNYX_PROFILE`    | Default profile name            |
| `TELNYX_CONFIG_DIR` | Custom config directory         |

## Getting Your API Key

1. Log in to the [Telnyx Portal](https://portal.telnyx.com/)
2. Navigate to [API Keys](https://portal.telnyx.com/#/app/api-keys)
3. Click **Create API Key**
4. Copy the key (it won't be shown again)

> **Note:** API keys start with `KEY_`. If you're using a v1 API key, you'll need to create a new v2 key.

## Next Steps

- [Command Reference](legacy-command-reference.md) — Full command reference for the legacy CLI


## Related Pages

- [CLI Authentication](../reference/cli-authentication.md)
- [API Authentication](../reference/api-authentication.md)
- [Tech Prefix Authentication](../runbooks/tech-prefix-authentication.md)
- [Authentication](../runbooks/authentication.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
