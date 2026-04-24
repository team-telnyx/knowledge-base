---
title: Troubleshooting
summary: Common issues and solutions for the Telnyx CLI.
sources:
  - url: https://developers.telnyx.com/development/cli/troubleshooting
    content_hash: e3b6d5657d6f7b9692ebd25600e93790a919c6c05ef9e602e4fa3cf2819c71c6
updated_at: 2026-04-10T00:00:00Z
---

# Troubleshooting

Common issues and solutions for the Telnyx CLI

This reference covers common issues you may encounter when using the Telnyx CLI and how to resolve them.

  Most CLI errors map directly to API error codes. For a complete list, see [API Error Codes](api-error-codes.md).

## Authentication Errors

### "Unauthorized" (401)

```
Error: Request failed with status 401: Unauthorized
```

**Causes:**

* Invalid or expired API key
* API key not set
* API key has extra whitespace or characters

**Solutions:**

1. Verify your API key is set:
   ```bash theme={null}
   echo $TELNYX_API_KEY
   ```

2. Check the key format (should start with `KEY_`):
   ```bash theme={null}
   # Correct format
   export TELNYX_API_KEY=KEY_xxxxxxxxxxxxx
   ```

3. Verify the key in the [Telnyx Portal](https://portal.telnyx.com/#/app/api-keys)

4. Test with a simple command:
   ```bash theme={null}
   telnyx balance retrieve
   ```

### "No API key" Error

**Causes:**

* Environment variable not set
* Environment variable not exported

**Solutions:**

1. Set the environment variable:
   ```bash theme={null}
   export TELNYX_API_KEY=KEY_xxxxxxxxxxxxx
   ```

2. Verify it's exported (not just set):
   ```bash theme={null}
   # Wrong (not exported)
   TELNYX_API_KEY=KEY_xxx

   # Correct (exported)
   export TELNYX_API_KEY=KEY_xxx
   ```

3. Add to your shell profile for persistence:
   ```bash theme={null}
   echo 'export TELNYX_API_KEY=KEY_xxx' >> ~/.bashrc
   source ~/.bashrc
   ```

## Permission Errors

### "Forbidden" (403)

```
Error: Request failed with status 403: Forbidden
```

**Causes:**

* API key doesn't have permission for this action
* Resource belongs to a different account
* Account verification required

**Solutions:**

1. Check API key permissions in the Portal
2. Verify you're using the correct API key for the account
3. Some features require account verification ([verify here](https://portal.telnyx.com/#/account/verification))

## Resource Errors

### "Not Found" (404)

```
Error: Request failed with status 404: Not Found
```

**Causes:**

* Resource ID is incorrect
* Resource was deleted
* Resource belongs to a different account

**Solutions:**

1. Verify the resource exists:
   ```bash theme={null}
   telnyx phone-numbers list
   telnyx messaging-profiles list
   ```

2. Check for typos in the resource ID

3. Ensure you're using the correct API key if you have multiple accounts

### "Phone number not found"

**Solution:**
List your numbers to see what's available:

```bash theme={null}
telnyx phone-numbers list
```

## Rate Limiting

### "Too Many Requests" (429)

```
Error: Request failed with status 429: Too Many Requests
```

**Causes:**

* Exceeded API rate limits
* Too many requests in short period

**Solutions:**

1. Add delays between requests in scripts:
   ```bash theme={null}
   for number in "${NUMBERS[@]}"; do
     telnyx messages send --from "$FROM" --to "$number" --text "$MSG"
     sleep 0.5  # Add delay
   done
   ```

2. Use bulk endpoints when available

3. Check [rate limits documentation](rate-limiting.md)

## Messaging Errors

### "Number not enabled for messaging"

```
Error: The phone number +15551234567 is not enabled for messaging
```

**Solutions:**

1. Enable messaging on the number via the Portal or API

2. Or purchase a messaging-enabled number:
   ```bash theme={null}
   telnyx available-phone-numbers list --filter.country-code US --filter.features sms
   ```

### "10DLC campaign required"

```
Error: US A2P messaging requires 10DLC registration
```

**Solution:**
Register for 10DLC via the Portal or API. See the [10DLC documentation](../tutorial/getting-started-with-10dlc.md).

### "Invalid 'to' number"

```
Error: The 'to' phone number is invalid
```

**Solutions:**

1. Use E.164 format (include country code):
   ```bash theme={null}
   # Wrong
   telnyx messages send --to 5551234567 ...

   # Correct
   telnyx messages send --to +15551234567 ...
   ```

2. Verify the number is valid:
   ```bash theme={null}
   telnyx number-lookup retrieve --phone-number +15551234567
   ```

## Installation Issues

### "command not found: telnyx"

**Causes:**

* CLI not installed
* Go bin directory not in PATH
* Shell not reloaded after install

**Solutions:**

1. Verify Go's bin directory contains telnyx:
   ```bash theme={null}
   ls $(go env GOPATH)/bin/telnyx
   ```

2. Add Go bin to PATH:
   ```bash theme={null}
   export PATH="$PATH:$(go env GOPATH)/bin"
   ```

3. Reinstall if needed:
   ```bash theme={null}
   go install github.com/team-telnyx/telnyx-cli/cmd/telnyx@latest
   ```

4. Reload your shell config:
   ```bash theme={null}
   source ~/.bashrc  # or ~/.zshrc
   ```

### "command not found: go"

**Causes:**

* Go not installed

**Solutions:**

Install Go:

```bash theme={null}


## Related Pages

- [Troubleshooting](../reference/troubleshooting-2.md)
- [10DLC Troubleshooting Guide](../runbooks/10dlc-troubleshooting-guide.md)
- [Android Push Troubleshooting](../reference/android-push-troubleshooting.md)
- [Flutter Push Troubleshooting](../reference/flutter-push-troubleshooting.md)
- [SIM Connectivity Troubleshooting](../runbooks/sim-connectivity-troubleshooting.md)
