---
title: How to Register for 10DLC via CLI
summary: Register your business for US A2P messaging using the Telnyx CLI.
sources:
  - url: https://developers.telnyx.com/development/cli/workflows/10dlc
    content_hash: e94ecf6525b8d70658c623294e693a80adb8858834059d78de8b446a36d74709
updated_at: 2026-04-10T00:00:00Z
---

# How to Register for 10DLC via CLI

Register your business for US A2P messaging using the Telnyx CLI

This guide shows you how to complete 10DLC (10-Digit Long Code) registration using the Telnyx CLI, from brand creation through campaign approval.

## Why 10DLC?

US carriers require 10DLC registration for Application-to-Person (A2P) messaging from local phone numbers. Without it, your messages may be blocked or throttled. Registration establishes your business identity with carriers and unlocks higher throughput based on your trust score.

> **Note:** For a deeper explanation of 10DLC, trust scores, and carrier requirements, see [Understanding 10DLC](../tutorial/getting-started-with-10dlc.md).

## Prerequisites

* Telnyx account with [verified status](https://portal.telnyx.com/#/account/verification)
* [Telnyx CLI installed](install-the-telnyx-cli.md)
* `TELNYX_API_KEY` environment variable set
* Business information ready (EIN, address, website)
* At least one US phone number

## Registration Steps

### Step 1: Create a Brand

A brand represents your business identity for 10DLC registration.

#### Standard Business

```bash theme={null}
telnyx messaging-10dlc:brand create \
  --entity-type PRIVATE_PROFIT \
  --display-name "Acme Corp" \
  --company-name "Acme Corporation Inc" \
  --ein 12-3456789 \
  --phone +15551234567 \
  --street "123 Main Street" \
  --city "San Francisco" \
  --state CA \
  --postal-code 94102 \
  --country US \
  --vertical TECHNOLOGY \
  --website https://acme.com
```

#### Sole Proprietor

For sole proprietors, additional SMS OTP verification is required:

```bash theme={null}
