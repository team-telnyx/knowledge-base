---
title: U.S. Telecommunications Regulatory Compliance for Telnyx Customers
summary: This page consolidates the key U.S. telecommunications regulatory requirements
  affecting Telnyx customers, including the STIR/SHAKEN call authentication framework,
  the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation
  Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers
  Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and
  number lifecycle management after account abolishment.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-07-17T09:01:52Z
---

# U.S. Telecommunications Regulatory Compliance for Telnyx Customers

*Part 6 of 7 — see also: [Part 1](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-1.md), [Part 2](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-2.md), [Part 3](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-3.md), [Part 4](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-4.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 7](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-7.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## Numbering Plan Areas (NPAs) and Exhausted Area Codes

The Numbering Plan Area (NPA) refers to the three-digit numbers that identify the region of specific localities across North America. Several rate centers across a locality can also share the same NPA. A rate center can be found by finding the NPA-NXX of a phone number. For example, the Telnyx office in Austin, Texas has NPAs 512 and 737.

- **NPA**: Number Plan Area (aka Area Code)
- **NXX**: Number Prefix (first 3 digits of your telephone number)

Where:

- **N** can be any number from 2 to 9
- **P, A** can be any number from 0 to 9
- **X** can be any number from 0 to 9

For example, in (858) 922-1234:

- 858 is an area code assigned in California
- 858-922 is an exchange assigned to Verizon Wireless associated with the La Jolla rate center
- 1234 is the line number

### Exhausted NPAs

An exhausted NPA refers to area codes where almost all numbering resources are assigned and the industry has minimal available numbers. The only way to establish more resources within an active NPA's operational area is through an industry overlay.

**Overlay**: An area code added to a region already serviced by another area code. Overlays require the industry to switch from ten-digit dialing rather than seven-digit dialing—an easy switch for Telnyx because the platform already operates on 10-digit dialing.

If you're trying to order new telephone numbers in a desirable area code, you may find there are limited quantities available. In this case, expanding your search with an overlay can be helpful. For example, in 2010, the New York City area code 212 became exhausted. To provide relief, the industry added 917 and 646 as overlays, bringing new available numbers to the area.

The following is a list of exhausted NPAs:

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
| 443 | Maryland |
| 415 | California |
| 419 | Ohio |
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

## Number Lifecycle After Account Abolishment

If your account is left with a negative balance for a period of one month, an abolishing process will take place. In this process, the numbers in your account will be deleted from the account.

After the numbers are deleted from the account, they are set to a "hold" status for the next two weeks. While the numbers are in this "hold" status, you can still buy them again by looking for them in the "Search and Buy Numbers" section of the [portal](https://portal.telnyx.com/#/app/numbers/search-numbers). During this period, only you will be able to search for and purchase the numbers. No other customer can acquire these numbers.

If you do not buy back your numbers when they are in the "hold" status, the status will change to "Aging" and will remain like that for the next two weeks. While the numbers are in an "Aging" status, no one (including you) can buy them. This is part of the number recycling process required by the FCC.

After the numbers have been left in "Aging" for two weeks, they will be released so that they are generally available. At that point, anyone with a Telnyx account can find them and buy them.

**Important Note**: If your account was abolished, you will not be able to get your numbers back by simply adding balance to your account. If your numbers are still on the "hold" status, you need to buy them back after adding a balance to your account. If the numbers are in the "Aging" status, the numbering team can still get them back for you, but you need to reach out to them directly.

- Numbering team: [numbering@telnyx.com](mailto:numbering@telnyx.com)
- Support team: [support@telnyx.com](mailto:support@telnyx.com)

This general process also applies when you accidentally delete a number from your account. It immediately goes to the "hold" status and after two weeks it goes into "Aging," then after another two weeks it is released.

### Auto-Recharge

Numbers are charged a Monthly Recurring Cost (MRC) at the beginning of every month. The cost depends on the number. Even if you had a positive balance in your account, if you abandon your account for several months without setting up an auto-recharge for your balance, there is a chance your account can fall into the negative. See the [Billing setup article](https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups) for how to set up Auto-Recharge.

### Notifications

Recurring payments can fail because of issues such as card expiry dates. Make sure you have your notifications properly configured and that you've set up notifications to be sent to all the emails or numbers of the people that need to be alerted of anything going on in your account. You can add different notification events, including low balance alerts and notifications whenever a number is deleted from your account. See [Notification settings](https://support.telnyx.com/en/articles/4277896-notification-settings) for more information.
