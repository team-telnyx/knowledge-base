---
title: Adaptive jitter buffer for SIP Trunking
summary: Jitter buffering smooths out packet arrival variation on SIP connections to reduce audio artifacts such as choppy or distorted speech.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer/index
    content_hash: 786a34f36734c51c5bcf1f4efe0a92847b8050d9e0545c622d84b5d2b741e624
updated_at: 2026-04-10T00:00:00Z
---

# Adaptive jitter buffer for SIP Trunking

Jitter buffering smooths out packet arrival variation on SIP connections to reduce audio artifacts such as choppy or distorted speech. Enable this feature at the connection level to improve call quality on networks with inconsistent latency.

## How it works

An adaptive jitter buffer temporarily holds incoming voice packets before playing them out, compensating for uneven packet arrival times (jitter). The buffer dynamically adjusts its size between configurable minimum and maximum values based on observed network conditions — expanding when jitter increases and shrinking when the network stabilizes.

## Configuration settings

| Setting                 | Purpose                        | Default | Range  |
| ----------------------- | ------------------------------ | ------- | ------ |
| `enable_jitter_buffer`  | Toggle jitter buffering on/off | `false` | —      |
| `jitterbuffer_msec_min` | Minimum buffer size (ms)       | `60`    | 40–400 |
| `jitterbuffer_msec_max` | Maximum buffer size (ms)       | `200`   | 40–400 |

<Callout type="warning">
  `jitterbuffer_msec_min` cannot exceed `jitterbuffer_msec_max`. The API will reject requests where the minimum is greater than the maximum.

## Configuration via API

### Credential connections

[PATCH /v2/credential\_connections/](https://developers.telnyx.com/api-reference/credential-connections/update-a-credential-connection)

```json theme={null}
{
  "jitter_buffer": {
    "enable_jitter_buffer": true,
    "jitterbuffer_msec_min": 60,
    "jitterbuffer_msec_max": 200
  }
}
```

### FQDN connections

[PATCH /v2/fqdn\_connections/](https://developers.telnyx.com/api-reference/fqdn-connections/update-an-fqdn-connection)

```json theme={null}
{
  "jitter_buffer": {
    "enable_jitter_buffer": true,
    "jitterbuffer_msec_min": 60,
    "jitterbuffer_msec_max": 200
  }
}
```

### IP connections

[PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection)

```json theme={null}
{
  "jitter_buffer": {
    "enable_jitter_buffer": true,
    "jitterbuffer_msec_min": 60,
    "jitterbuffer_msec_max": 200
  }
}
```

## Tuning guidance

* **Higher values** increase latency tolerance and work better for high-jitter networks (e.g., international routes or mobile carriers).
* **Lower values** reduce latency and are suited for stable, low-jitter networks (e.g., dedicated fiber or local connections).
* **Default values** (`60`–`200` ms) work well for most deployments and are a good starting point.

<Callout type="info">
  Jitter buffer configuration is currently available via API only. Portal UI support is coming soon.

## Best practices

1. **Start with defaults** before tuning — the default range of 60–200 ms handles most network conditions
2. **Monitor call quality metrics** after enabling to validate the impact on your specific traffic
3. **Increase the maximum** for routes with known high jitter rather than raising the minimum, which adds baseline latency to all calls
4. **Enable on specific connections** rather than globally if only certain routes experience jitter issues
5. **Test during peak hours** when network congestion and jitter are most likely to occur
