---
title: Legacy Command Reference
summary: Complete reference for legacy CLI commands (@telnyx/api-cli).
sources:
  - url: https://developers.telnyx.com/development/cli/legacy/reference
    content_hash: 7333fb5cf3da2fbb976e52cb915fccdcf58b3865d8c6b670650b9679f0334ded
updated_at: 2026-04-10T00:00:00Z
---

# Legacy Command Reference

Complete reference for legacy CLI commands (@telnyx/api-cli)

> **Warning:** **This CLI is deprecated.** For the current CLI commands, see [Command Reference](command-reference.md).

## Authentication & Profiles

```bash theme={null}
telnyx auth setup                    # Interactive API key setup
telnyx auth setup --profile prod     # Setup named profile
telnyx auth status                   # Check current auth status

telnyx profile list                  # List all profiles
telnyx profile set-default <name>    # Set default profile
telnyx profile delete <name>         # Delete a profile
```

## Phone Numbers

### Search & Purchase

```bash theme={null}


## Related Pages

- [Command Reference](../reference/command-reference.md)
