---
title: SIM Cards
summary: How to order physical SIMs and eSIMs, and what happens after.
sources:
  - url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
    content_hash: 11528d9fffac0b768a2f3ebaaa816141c4bb873e7dc8c8b1b534c0a65fbee8dd
updated_at: 2026-04-10T00:00:00Z
---

# SIM Cards

How to order physical SIMs and eSIMs, and what happens after.

## Getting SIMs

### Physical SIMs

Physical SIM orders go through [Mission Control](https://portal.telnyx.com/#/wireless/buy-sim-cards) — you can't order them via API.

1. **Order** — Set quantity, add to cart, and check out. Telnyx ships triple-cut SIM cards (2FF/3FF/4FF) to your address.
2. **Register** — Each physical SIM has a 10-digit registration code printed on the card. Register via the portal ([Register SIM Cards](https://portal.telnyx.com/#/wireless/buy-sim-cards) tab, manual or CSV) or the API ([`POST /actions/register/sim_cards`](https://developers.telnyx.com/api-reference/sim-cards/register-sim-cards)). During registration you assign a SIM Card Group and optional tags.
3. **Enable** — Once registered, activate the SIM on the network via [`POST /sim_cards/{id}/actions/enable`](https://developers.telnyx.com/api-reference/sim-cards/request-a-sim-card-enable) or the portal.

After registration, the SIM appears as a standard SIM Card resource. All further management is via the API.

### eSIMs

eSIMs are downloadable SIM profiles for consumer devices (phones, tablets, laptops) — not embedded SIM hardware. For eUICC hardware solutions, contact [Sales](https://telnyx.com/contact-us).

Purchase through [Mission Control](https://portal.telnyx.com/#/wireless/buy-esims) or the API (`POST /actions/purchase_esims`):

* **Portal** — Set quantity, assign a SIM Card Group, choose initial status, add tags. \$0.70 activation fee per eSIM. No cart — purchase is immediate.
* **API** — [`POST /actions/purchase/esims`](https://developers.telnyx.com/api-reference/sim-cards/purchase-esims). Same parameters, same instant provisioning.

Either way, you get an activation code immediately. Provide it to the device via QR code or direct input for OTA provisioning. No shipping, no registration step.

> **Warning:** eSIM activation codes are one-time use. If the device loses the profile, you need a new eSIM purchase — you can't re-download the same profile.

After provisioning, eSIMs become the same SIM Card resource as physical SIMs. All API operations are identical.

## Next Steps

Once you have SIMs in your account, see [Lifecycle](sim-lifecycle.md) for state management (enable, disable, standby, delete) and [SIM Card Groups](sim-card-groups.md) for fleet configuration.


## Related Pages

- [SIM Card Groups](../runbooks/sim-card-groups.md)
