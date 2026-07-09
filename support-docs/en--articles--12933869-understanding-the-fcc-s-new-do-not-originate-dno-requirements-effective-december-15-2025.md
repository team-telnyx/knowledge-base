---
source_url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
scraped: 2026-07-08
content_hash: 8c00b9aa07357e8d25a598fbdf4427471e341bc0884ddfc96abd5d756eb2cad8
---

Understanding the FCC’s New Do-Not-Originate (DNO) Requirements (Effective December 15, 2025) | Telnyx Help Center

[Skip to main content](#main-content)

# Understanding the FCC’s New Do-Not-Originate (DNO) Requirements (Effective December 15, 2025)

Written by Telnyx Engineering

November 25, 2025

Table of contents

## **Overview**

The Federal Communications Commission (FCC) has adopted new rules that expand the industry’s responsibilities around blocking calls from Do-Not-Originate (DNO) numbers. A DNO list identifies numbers that should *never* be used to originate outbound calls—for example, inbound-only government hotlines or numbers associated with impersonation scams.

Historically, only gateway providers (U.S.-based intermediate providers that receive and pass along calls from foreign service providers) were required to block outbound calls originating from numbers on their own DNO lists.

**Under the FCC’s new rules ([FCC 25-15](https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls)****), all U.S. voice service providers in the call path must block calls that appear to originate from a number on a “reasonable DNO list.” These rules take effect on December 15, 2025.**

# **What Is a DNO List?**

A DNO list contains telephone numbers that should *never* place outbound calls. When a provider sees an outbound call that appears to be originating from one of these numbers, the provider is required to block it before it reaches the end user.

The FCC’s goal is to prevent a common scam pattern:

* A bad actor spoofs a trusted inbound-only number—such as an IRS hotline or a bank’s customer-support line—and then blasts outbound calls pretending to be that legitimate institution.

DNO protection helps break this pattern by ensuring that these inbound-only and fraud-associated numbers cannot be used to originate calls.

# **What’s Changing?**

Previously, only gateway providers were obligated to maintain and enforce DNO lists. Under the FCC’s updated rules, all U.S. voice service providers throughout the call path must block outbound calls that present a number appearing on a “reasonable DNO list.”

**This obligation applies regardless of your position in the call path. If you are listed in the Robocall Mitigation Database as a voice service provider, gateway provider, or non-gateway intermediate provider** — **this rule applies to you.**

# **What Counts as a “Reasonable DNO List”?**

The FCC does *not* mandate a single centralized DNO list. Instead, providers must maintain and consult a DNO list covering **four categories of numbers**:

1. **Invalid Numbers**

   * Numbers that are not dialable under the North American Numbering Plan.  
     ​
   * Example: numbers with invalid NPA-NXX formats.  
     ​
2. **Unallocated Numbers**

   * Valid NANP numbers that have never been assigned to a provider.  
     ​
3. **Unused Numbers**

   * Numbers that a provider has been allocated but has not yet assigned to an end user.​  
     ​
4. **Numbers Requested for DNO Blocking**

   * Inbound-only numbers that the owner of the number has requested be added to the DNO list
   * Inbound-only government numbers when the government entity has requested DNO protection
   * Private-sector inbound-only numbers used in impersonation scams, when the number owner requests blocking.  
     ​  
     ​

Providers may also include additional categories, as long as the overall list remains “reasonable” as defined in the Order.

---

Related Articles

[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[STIR/SHAKEN With Telnyx](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx)[Robocall Mitigation Database](https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database)[Understanding the FCC’s Eighth Report and Order on Third-Party Authentication](https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
