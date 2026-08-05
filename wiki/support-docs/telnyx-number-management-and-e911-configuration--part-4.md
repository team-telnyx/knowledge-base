---
title: Telnyx Number Management and E911 Configuration
summary: This page consolidates Telnyx Mission Control guidance for managing phone
  numbers, configuring E911 emergency services, registering emergency addresses, testing
  emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency
  settings.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Number Management and E911 Configuration

*Part 4 of 4 — see also: [Part 1](telnyx-number-management-and-e911-configuration--part-1.md), [Part 2](telnyx-number-management-and-e911-configuration--part-2.md), [Part 3](telnyx-number-management-and-e911-configuration--part-3.md)*

This page consolidates Telnyx Mission Control guidance for managing phone numbers, configuring E911 emergency services, registering emergency addresses, testing emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency settings.

## Number Lookup

The [Your Number Lookup Guide](your-number-lookup-guide.md) describes the Telnyx Number Lookup tool, which retrieves carrier details, CNAM, and routing information for phone numbers. It helps make calls more productive, reduce undelivered messages, and protect from spam and fraud.

### Prerequisites

- A Telnyx account.
- A positive account balance (Number Lookup requires funds).
- An API key generated from **API Keys** in Mission Control.

Number Lookup is not available if your account balance is negative.

### Using Number Lookup in the Portal

1. Sign in to the [Telnyx portal](https://portal.telnyx.com/).
2. Navigate to <https://portal.telnyx.com/#/lookup>.
3. Enter the phone number and select a **Lookup Type**:
   - **None:** Basic info (LRN only).
   - **Carrier:** Adds carrier details.
   - **Caller Name:** Adds CNAM.
   - **Both:** Returns all available data.
4. Click **Lookup Number**.

### Lookup types and pricing

| Service | Cost |
| --- | --- |
| Local Routing Number (LRN) | $0.0015 per query |
| MCC/MNC (Carrier Codes) | $0.0025 per query (mobile only) |
| CNAM (Caller ID Name) | $0.003 per query |
| Inbound CNAM | $0.40 per number/month |
| Outbound CNAM Listing | Free |

**Examples:**

- Landline with Carrier + Caller Name: $0.0015 + $0.003 = $0.0045.
- Mobile with Carrier + Caller Name: $0.0015 + $0.0025 + $0.003 = $0.007.

### Reviewing your usage

- **Invoice:** Charges appear at the start of each month.
- **Usage Reports:** Go to **Reporting > Usage Reports** and select a date range. Reports are not real-time; today's lookups appear tomorrow.

### Important notes

- To view full LRN data, go to **Account Settings > Profile** and enable **Permitted NPAC User** (allow ~15 minutes to apply).
- Access is restricted to Organization Owners only (no sub-accounts).
- US Toll-Free: Resporg ID is not returned.

### Troubleshooting

| Error | Cause | Solution |
| --- | --- | --- |
| Number Lookup unavailable | Zero/negative balance | [Add funds](https://portal.telnyx.com/#/app/billing/add-credit) |
| LRN data incomplete | NPAC User not enabled | Enable in Account Settings |
| 401 Unauthorized | Invalid API key | Verify key and header format |
| Sub-user access denied | Owner-only feature | Use org owner credentials |

## Exhausted NPA Codes

The [What is an Exhausted NPA?](what-is-an-exhausted-npa.md) article explains Numbering Plan Area (NPA) codes, the three-digit area codes that identify regions across North America. A rate center can be found by combining the NPA and NXX of a phone number. For example, in (858) 922-1234, 858 is the area code assigned in California, 858-922 is the exchange assigned to Verizon Wireless associated with the La Jolla rate center, and 1234 is the line number.

- **NPA:** Number Plan Area (area code).
- **NXX:** Number Prefix (first 3 digits of the telephone number).
- **N** can be any number from 2 to 9.
- **P, A** can be any number from 0 to 9.
- **X** can be any number from 0 to 9.

An exhausted NPA refers to an area code where almost all numbering resources are assigned and the industry has minimal available numbers. The only way to establish more resources within an active NPA's operational area is through an industry overlay — an area code added to a region already serviced by another area code. Overlays require the industry to switch from seven-digit to ten-digit dialing, which is straightforward for Telnyx because it already operates on ten-digit dialing.

For example, in 2010 the New York City area code 212 became exhausted. To provide relief, the industry added 917 and 646 as overlays, bringing new available numbers to the area. All of these area codes service the same geographic region as 212.

The current list of exhausted NPAs includes:

| NPA | State/Province |
| --- | --- |
| 201 | New Jersey |
| 202 | District of Columbia |
| 203 | Connecticut |
| 205 | Alabama |
| 208 | Idaho |
| 209 | California |
| 210 | Texas |
| 212 | New York |
| 214 | Texas |
| 215 | Pennsylvania |
| 217 | Illinois |
| 240 | Maryland |
| 248 | Michigan |
| 256 | Alabama |
| 267 | Pennsylvania |
| 270 | Kentucky |
| 281 | Texas |
| 301 | Maryland |
| 303 | Colorado |
| 304 | West Virginia |
| 305 | Florida |
| 310 | California |
| 312 | Illinois |
| 314 | Missouri |
| 315 | New York |
| 317 | Indiana |
| 323 | California |
| 330 | Ohio |
| 336 | North Carolina |
| 347 | New York |
| 360 | Washington |
| 402 | Nebraska |
| 404 | Georgia |
| 405 | Oklahoma |
| 407 | Florida |
| 408 | California |
| 410 | Maryland |
| 415 | California |
| 419 | Ohio |
| 443 | Maryland |
| 469 | Texas |
| 470 | Georgia |
| 480 | Arizona |
| 484 | Pennsylvania |
| 503 | Oregon |
| 508 | Massachusetts |
| 510 | California |
| 512 | Texas |
| 513 | Ohio |
| 516 | New York |
| 518 | New York |
| 540 | Virginia |
| 541 | Oregon |
| 561 | Florida |
| 570 | Pennsylvania |
| 573 | Missouri |
| 601 | Mississippi |
| 603 | New Hampshire |
| 609 | New Jersey |
| 610 | Pennsylvania |
| 614 | Ohio |
| 615 | Tennessee |
| 617 | Massachusetts |
| 618 | Illinois |
| 619 | California |
| 630 | Illinois |
| 631 | New York |
| 646 | New York |
| 678 | Georgia |
| 702 | Nevada |
| 703 | Virginia |
| 704 | North Carolina |
| 706 | Georgia |
| 707 | California |
| 708 | Illinois |
| 713 | Texas |
| 714 | California |
| 717 | Pennsylvania |
| 718 | New York |
| 720 | Colorado |
| 724 | Pennsylvania |
| 732 | New Jersey |
| 740 | Ohio |
| 757 | Virginia |
| 760 | California |
| 770 | Georgia |
| 773 | Illinois |
| 781 | Massachusetts |
| 786 | Florida |
| 800 | US/CA |
| 801 | Utah |
| 803 | South Carolina |
| 805 | California |
| 812 | Indiana |
| 813 | Florida |
| 814 | Pennsylvania |
| 815 | Illinois |
| 817 | Texas |
| 818 | California |
| 832 | Texas |
| 843 | South Carolina |
| 845 | New York |
| 847 | Illinois |
| 850 | Florida |
| 860 | Connecticut |
| 864 | South Carolina |
| 870 | Arkansas |
| 903 | Texas |
| 909 | California |
| 910 | North Carolina |
| 916 | California |
| 917 | New York |
| 918 | Oklahoma |
| 919 | North Carolina |
| 920 | Wisconsin |
| 937 | Ohio |
| 954 | Florida |
| 972 | Texas |
| 973 | New Jersey |
| 978 | Massachusetts |

## Getting Help

Contact [support@telnyx.com](mailto:support@telnyx.com) for any of the following:

- The Portal rejects an emergency address.
- A number remains pending or does not show as ready/active for emergency service.
- The 933 readback is incorrect.
- A call does not present the E911-enabled Telnyx number.
- You are configuring Dynamic E911, MLTS, WebRTC, mobile, IoT, or another advanced emergency-calling workflow.

Include the Telnyx phone number, the emergency service address, the approximate time of the test or attempted setup, and any screenshot or exact error message from the Portal.
