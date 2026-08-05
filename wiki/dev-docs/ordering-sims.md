---
title: Ordering SIMs
summary: How to obtain physical SIMs and eSIMs on Telnyx, including ordering, registration,
  and activation steps for each form factor.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
updated_at: 2026-08-05T13:46:57Z
---

# Ordering SIMs

How to obtain physical SIMs and eSIMs on Telnyx, including ordering, registration, and activation steps for each form factor.

## Getting SIMs

Telnyx offers two SIM form factors: physical SIM cards and eSIMs. The acquisition path differs for each.

### Physical SIMs

Physical SIM orders are placed through [Mission Control](https://portal.telnyx.com/#/wireless/buy-sim-cards) and cannot be ordered via the API.

1. **Order** — Set the desired quantity, add to cart, and check out. Telnyx ships triple-cut SIM cards (2FF/3FF/4FF) to your address.
2. **Register** — Each physical SIM has a 10-digit registration code printed on the card. Register via the portal (Register SIM Cards tab, manual or CSV) or the API using `POST /actions/register/sim_cards`. During registration you assign a SIM Card Group and optional tags.
3. **Enable** — Once registered, activate the SIM on the network via `POST /sim_cards/{id}/actions/enable` or the portal.

After registration, the SIM appears as a standard SIM Card resource. All further management is via the API.

### eSIMs

eSIMs are downloadable SIM profiles for consumer devices such as phones, tablets, and laptops — they are not embedded SIM hardware. For eUICC hardware solutions, contact [Sales](https://telnyx.com/contact-us).

Purchase through [Mission Control](https://portal.telnyx.com/#/wireless/buy-esims) or the API (`POST /actions/purchase_esims`):

- **Portal** — Set quantity, assign a SIM Card Group, choose initial status, and add tags. There is a $0.70 activation fee per eSIM. There is no cart — purchase is immediate.
- **API** — `POST /actions/purchase/esims`. Same parameters, same instant provisioning.

Either way, you receive an activation code immediately. Provide it to the device via QR code or direct input for over-the-air provisioning. There is no shipping and no registration step.

eSIM activation codes are one-time use. If the device loses the profile, you need a new eSIM purchase — you cannot re-download the same profile.

After provisioning, eSIMs become the same SIM Card resource as physical SIMs. All API operations are identical.

## Next Steps

Once you have SIMs in your account, see [SIM Lifecycle](sim-lifecycle.md) for state management (enable, disable, standby, delete) and [SIM Card Groups](sim-card-groups.md) for fleet configuration.
