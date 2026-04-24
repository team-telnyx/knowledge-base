---
title: Traffic Policy Profiles
summary: Control what traffic your SIMs can send and receive — by service, IP range, or domain.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles/index
    content_hash: b5d382d2d25accf7e39f817f88f531506db1f6e2bf110eda03653a31d9215311
updated_at: 2026-04-10T00:00:00Z
---

# Traffic Policy Profiles

Control what traffic your SIMs can send and receive — by service, IP range, or domain.

Traffic Policy Profiles define what network traffic your SIMs are allowed (or denied). Assign a profile to filter traffic at the network level before it reaches your devices.

## Profile Types

| Type           | Behavior                                                     |
| :------------- | :----------------------------------------------------------- |
| **whitelist**  | Only listed traffic is allowed. Everything else is blocked.  |
| **blacklist**  | Listed traffic is blocked. Everything else is allowed.       |
| **throttling** | Traffic is allowed but bandwidth-limited to `limit_bw_kbps`. |

## Filter Criteria

Each profile can include one or more of:

* **services** — PCEF service IDs (predefined traffic categories). Use `GET /traffic/policy/profiles/services` to list available services.
* **ip\_ranges** — CIDR notation (`10.0.0.0/8`, `203.0.113.0/24`). Block or allow specific IP ranges.
* **domains** — Domain names (`example.com`, `*.internal.corp`). DNS-level filtering.

At least one of `services`, `ip_ranges`, or `domains` is required when creating a profile.

## Example: IoT Device Lockdown

Whitelist-only profile that restricts a fleet of sensors to your backend servers:

```json theme={null}
{
  "type": "whitelist",
  "ip_ranges": ["10.100.0.0/16"],
  "domains": ["api.yourcompany.com", "telemetry.yourcompany.com"]
}
```

Devices can only reach your internal network and two API endpoints. All other traffic is dropped.

## Example: Bandwidth Throttling

Limit data-hungry devices to prevent runaway costs:

```json theme={null}
{
  "type": "throttling",
  "limit_bw_kbps": 256
}
```

## Assigning Profiles

Profiles are assigned at the SIM Card Group level. Create the profile via `POST /traffic/policy/profiles`, then reference its ID when configuring the group.
