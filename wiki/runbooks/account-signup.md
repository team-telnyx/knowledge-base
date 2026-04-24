---
title: Account Signup
summary: Understand the trust and safety checks applied to every Telnyx signup attempt.
sources:
  - url: https://developers.telnyx.com/docs/account-setup/signup
    content_hash: 2ddd81f6c764a993b0fc300f755781c7c63b4805d064f1f5401217c25781cc97
updated_at: 2026-04-10T00:00:00Z
---

# Account Signup

Understand the trust and safety checks applied to every Telnyx signup attempt.

Every signup attempt is subjected to a battery of trust and safety checks. Among them, in no particular order, are the following:

* Domain age
* Domain reputation
* Host reputation
* IP reputation
* Signup origin
* reCAPTCHA verification

An attempt will be unsuccessful if **any** of the above fails.

Some attempts may also be subjected to additional requirements, including:

* Successfully validating a legitimate mobile number
* Successfully passing Know Your Customer (KYC) documentation verification

Telnyx constantly adjusts the logic, sequence, and thresholds to combat signup abuse and fraudulent usage of the platform.


## Related Pages

- [Account Upgrade](../runbooks/account-upgrade.md)
