---
title: Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service for files,
  media, backups, and static assets. It is reachable over the standard AWS S3 API
  or directly from inside a Telnyx Edge Function, with buckets available in US, EU,
  and AP regions and a usage-based pricing model.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/overview
updated_at: 2026-08-05T13:39:18Z
---

# Cloud Storage

Telnyx Cloud Storage is an S3-compatible object storage service for files, media, backups, and static assets. It is reachable over the standard AWS S3 API or directly from inside a Telnyx Edge Function, with buckets available in US, EU, and AP regions and a usage-based pricing model.

## Overview

Telnyx Cloud Storage is an S3-compatible object storage service designed for files, media, backups, and static assets. It is reached over the AWS S3 API you already know, or directly from inside a Telnyx Edge Function.

With Telnyx Cloud Storage, you can:

- **Use your existing S3 tooling** — the AWS SDKs, AWS CLI, and third-party S3 clients work unchanged; authenticate with your Telnyx API key.
- **Store data in the US, EU, or AP** — buckets in `us-central-1`, `us-east-1`, `us-west-1`, `eu-central-1`, and `ap-southeast-1`.
- **Reach buckets from Edge Compute** — bind a bucket to a function and read or write objects with no S3 keys in your code.
- **Control access and lifecycle** — presigned URLs, public buckets, object lock and retention, SSE-C encryption, and lifecycle rules.
- **Pay for what you use** — a monthly free tier plus simple usage-based pricing.

## Getting started

The documentation is organised around a few common entry points:

- **Quick Start** — create a bucket, generate S3 credentials, and upload your first object.
- **Use from an Edge Function** — bind a bucket and read or write objects with no S3 keys in your code.
- **SDK Examples** — copy-paste examples for Node, Python, Java, Go, Ruby, PHP, .NET, and Elixir.
- **API Endpoints & Regions** — regional endpoints and how requests are routed.

## Ways to access

Telnyx Cloud Storage can be reached through several interfaces, depending on whether you are writing application code, scripting from a terminal, or running serverless workloads on Telnyx Edge Compute.

- **Cloud Storage binding** — from inside a Telnyx Edge Function, with pre-authenticated access and no S3 keys required.
- **AWS SDK** — Node, Python, Java, Go, Ruby, PHP, .NET, or Elixir.
- **AWS CLI** — scripting and one-off operations from a terminal.
- **Third-party S3 tools** — move data at scale without writing code.

## Learn the essentials

Some behaviour differs from AWS S3 — review these topics before going to production:

- [Compatibility matrix](compatibility-matrix.md) — which S3 operations are supported, by region.
- [Authentication](authentication.md) — using your Telnyx API key as the S3 credential.
- [Presigned URLs](presigned-urls.md) — the Telnyx-specific way to generate them safely.
- [Billing](billing.md) — storage and request pricing.
