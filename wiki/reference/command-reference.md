---
title: Command Reference
summary: Complete reference for all Telnyx CLI commands.
sources:
  - url: https://developers.telnyx.com/development/cli/reference
    content_hash: 0dea876e74136ddf661756b9124964308452294e2a1e8221c91ff797a4f22f8a
updated_at: 2026-04-10T00:00:00Z
---

# Command Reference

Complete reference for all Telnyx CLI commands

This page provides a comprehensive reference for all available CLI commands. Use `telnyx <command> --help` for detailed options.

> **Note:** The CLI is auto-generated from the [Telnyx REST API](https://developers.telnyx.com/api-reference/overview). For full request/response schemas, see the corresponding API reference for each resource.

## Global Options

These flags work with all commands:

```bash theme={null}
--debug                   # Enable debug logging (shows HTTP requests/responses)
--base-url <url>          # Override the API base URL
--format <format>         # Output format: auto, json, jsonl, pretty, yaml, raw
--format-error <format>   # Error output format
--transform <gjson>       # Transform output using GJSON syntax
--help, -h                # Show help
--version, -v             # Show version
```

## Phone Numbers

> **Note:** See [Phone Numbers API](https://developers.telnyx.com/api-reference/numbers/list-phone-numbers) for full response schemas.

### List & Manage Numbers

```bash theme={null}


## Related Pages

- [Legacy Command Reference](../reference/legacy-command-reference.md)
- [Command Retries](../runbooks/command-retries.md)
