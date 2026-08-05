---
title: Telnyx Number Management Guide
summary: A consolidated reference for managing phone numbers on Telnyx, covering ordering
  restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF
  verification flows, use-case selection, and the sunset Google Verified Calls product.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Number Management Guide

*Part 1 of 5 — see also: [Part 2](telnyx-number-management-guide--part-2.md), [Part 3](telnyx-number-management-guide--part-3.md), [Part 4](telnyx-number-management-guide--part-4.md), [Part 5](telnyx-number-management-guide--part-5.md)*

A consolidated reference for managing phone numbers on Telnyx, covering ordering restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF verification flows, use-case selection, and the sunset Google Verified Calls product.

## Overview

Telnyx provides a range of number management capabilities spanning ordering, porting, verification, and feature configuration. This guide consolidates the key workflows and policies you need to know when acquiring, verifying, and using phone numbers on the Telnyx platform.

## Phone Number Ordering Restrictions

Telnyx enforces ordering restrictions to combat fraudulent activity and enhance platform security. Restrictions are tied to your account verification level under one of two frameworks:

- The **Level 1 / Level 2 (Legacy)** framework
- The **Trial-Paid-Verified-Enterprise (TPVE)** framework

See [Account Verification](account-verification.md) to determine your account's framework and level.

### +1 Toll-Free Ordering Restrictions

Effective September 22, 2025, accounts created with a freemail domain (e.g., gmail.com, yahoo.com, outlook.com) face restrictions when ordering +1 toll-free phone numbers:

- **Freemail accounts created on or after September 22, 2025** cannot order +1 toll-free phone numbers, regardless of verification level or framework.
- **Freemail accounts created before September 22, 2025** remain eligible if they meet other account qualifications.
- **Non-freemail accounts (corporate or custom domains)** remain eligible if they meet other account qualifications.

### Level 1 / Level 2 (Legacy) Restrictions

- **Accounts created after March 24, 2025 with Level 1 (L1) status** can only order local phone numbers in their account's country of origin.
- **Pre-existing L1 accounts (created before March 24, 2025)** cannot order toll-free phone numbers but have no other restrictions. Telnyx reserves the right to update these restrictions.
- **All Level 2 (L2) accounts** have no ordering restrictions.

In summary:

- Before March 24, 2025: L1 cannot order toll-free; L2 has no restrictions.
- After March 24, 2025: L1 can only order local numbers from their country of origin; L2 has no restrictions.

**Sub users:** Ordering restrictions are based on the organization owner's account signup date and verification status, not the sub-user's account.

**Managed accounts:** Restrictions are based on each individual ManagER or ManagED account's signup date and verification status.

### TPVE Framework Restrictions

If your account is part of the Trial-Paid-Verified-Enterprise framework, refer to the [TPVE levels and capabilities documentation](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities) for details on applicable restrictions and upgrade paths.
