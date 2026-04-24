---
title: SIMs & eSIMs
summary: SIM types, lifecycle, resource model, and multi-IMSI networking.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/get-started/index
    content_hash: edb577368779c716b739d45858e43d1508a825fdd32882246d090ad566d07dea
updated_at: 2026-04-10T00:00:00Z
---

# SIMs & eSIMs

SIM types, lifecycle, resource model, and multi-IMSI networking.

## SIM Types

All Telnyx SIMs are eUICC-enabled. Three form factors:

| Type         | Form Factor                      | Delivery              | Use Case                                          |
| :----------- | :------------------------------- | :-------------------- | :------------------------------------------------ |
| **SIM Card** | Triple-cut plastic (2FF/3FF/4FF) | Shipped               | Routers, gateways, traditional devices            |
| **eSIM**     | Software profile                 | Over-the-air download | Phones, tablets, laptops — no physical SIM needed |

## Resource Model

Three core resources, all API-managed:

* **SIM Card** — the connectivity entity. Has an ICCID, status, data settings, optional voice flag. Covers both physical SIMs and eSIMs (eSIMs are purchased via a separate endpoint but become the same SIM Card resource with an activation code for OTA provisioning). Everything starts here.
* **SIM Card Group** — bulk management. Apply data limits, network preferences, and Private Wireless Gateway configs to all SIMs in a group at once.
* **Mobile Phone Number** — optional. Created when you enable voice or messaging on a SIM. Controls call forwarding, caller ID, messaging profile.

## SIM Lifecycle

```
Order → Register → `enabled` → [Active Use] → `disabled` / `standby`
```

| Status         | MRC       | Data | Description                                    |
| :------------- | :-------- | :--- | :--------------------------------------------- |
| **Registered** | \$2/mo    | No   | SIM exists in your account, not yet on network |
| `enabled`      | \$2/mo    | Yes  | Active on network, consuming data              |
| `disabled`     | \$0.20/mo | No   | Off network, reduced cost, retains config      |
| `standby`      | \$0.20/mo | No   | Same as disabled, ready for quick re-enable    |

## Multi-IMSI

Every Telnyx SIM carries multiple IMSIs (Telnyx, Sparkle, BICs, T-Mobile, US Cellular). An on-SIM applet automatically selects the best IMSI per location — local network attachment instead of roaming, lower latency, better rates.

Default is automatic selection. You can override to manual per-SIM or per-group via API if you need to pin a specific IMSI for regulatory or testing purposes.

## Pricing

Three cost components:

| Component        | Cost                                                                                                                        |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **SIM purchase** | $1/SIM, $0.70/eSIM. \$10 shipping outside US mainland.                                                                      |
| **Monthly**      | $2/active SIM, $0.20/disabled or standby                                                                                    |
| **Data**         | Tiered by zone and volume. [Full breakdown →](https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing) |
