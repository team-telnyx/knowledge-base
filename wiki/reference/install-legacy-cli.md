---
title: Install Legacy CLI
summary: Install the legacy Node.js CLI (@telnyx/api-cli).
sources:
  - url: https://developers.telnyx.com/development/cli/legacy/install
    content_hash: 7112205dbfa2ae42a9c79806fec5ea1d23b9e499591663fdb89a3ef46b90bf25
updated_at: 2026-04-10T00:00:00Z
---

# Install Legacy CLI

Install the legacy Node.js CLI (@telnyx/api-cli)

> **Warning:** **This CLI is deprecated.** For new projects, use the [current Telnyx CLI](install-the-telnyx-cli.md) instead.

## Requirements

The legacy CLI requires **Node.js 20 or later**.

## Installation

Install globally via npm:

```bash theme={null}
npm install -g @telnyx/api-cli
```

This makes the `telnyx` command available from any directory.

## Verify Installation

```bash theme={null}
telnyx --version
```

Expected output:

```
@telnyx/api-cli/1.1.0 darwin-arm64 node-v20.10.0
```

## Update

To update to the latest version:

```bash theme={null}
npm update -g @telnyx/api-cli
```

## Troubleshooting

### "command not found: telnyx"

If the command isn't found after installation:

1. Verify it installed:
   ```bash theme={null}
   npm list -g @telnyx/api-cli
   ```

2. Check npm's global bin is in your PATH:
   ```bash theme={null}
   npm config get prefix
   # Add <prefix>/bin to your PATH if needed
   ```

3. Restart your terminal or reload your shell config:
   ```bash theme={null}
   source ~/.bashrc  # or ~/.zshrc
   ```

### Permission errors

If you get `EACCES` permission errors:

1. Follow [npm's guide to fix permissions](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)

2. Or use a Node version manager (nvm, fnm) which doesn't require sudo

## Next Steps

- [Authentication](legacy-cli-authentication.md) — Configure API keys and profiles


## Related Pages

- [Install the Telnyx CLI](../reference/install-the-telnyx-cli.md)
