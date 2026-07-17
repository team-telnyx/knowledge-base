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

*Part 4 of 7 — see also: [Part 1](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-1.md), [Part 2](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-2.md), [Part 3](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-3.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 6](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-6.md), [Part 7](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-7.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## U.S. Reassigned Numbers Database (RND)

The U.S. Reassigned Numbers Database (RND) is a centralized FCC-authorized database that tracks telephone numbers that have been permanently disconnected and potentially reassigned to new users. It was established by the FCC as part of efforts to curb unwanted calls, particularly those intended for a phone number's former owner. When a number is reassigned, callers might inadvertently reach a new consumer who never gave consent, which can be annoying to the recipient and can expose the caller to liability under the Telephone Consumer Protection Act (TCPA).

The RND's purpose is to help voice service providers and businesses determine *before placing a call* whether a phone number has been disconnected (and thus possibly reassigned) since the time the original consent was obtained.

### How the RND Works

Voice service providers (like Telnyx) report permanently disconnected U.S. phone numbers into the RND on an ongoing basis (typically monthly). The official RND system (accessible at reassigned.us) allows registered callers to query a phone number with a date of last contact or consent. The database responds with one of three results:

- **Yes**: The number has been permanently disconnected (i.e., likely reassigned) after the provided date, so calling it could reach the wrong person.
- **No**: The number has not been disconnected since that date, suggesting it still belongs to the same consumer. This "No" result grants a safe harbor if it later turns out the number was reassigned.
- **No Data**: The database has no record for the query (for example, if the consent date was before the RND started tracking in 2021). In that case, no safe harbor applies.

The FCC's 2018 order created the RND to address calls to reassigned numbers on a nationwide scale. Since November 2021, the RND has been fully operational for paid subscribers (callers) to use in their compliance workflows. The FCC requires all telephone service providers to supply their disconnected number data to the RND, making it a comprehensive resource covering all U.S. geographic and toll-free numbers. Telnyx complies by submitting monthly reports of numbers that have been permanently disconnected. Telnyx also offers customers a 15-day window to reclaim a number after disconnecting it, before it gets reported as permanently disconnected in the next RND update.

### Who Is Required to Use the RND

Businesses making outbound calls or texts to U.S. numbers are required by law to check the RND when relying on prior consumer consent to contact those numbers. In practice, any entity that places telemarketing, informational, or automated calls/SMS should be using the RND to verify numbers. This includes contact centers, CPaaS providers, sales and marketing platforms, debt collectors, and robocall/auto-dialer operators—essentially, if your organization sends outbound voice calls or text messages to consumers, you need to ensure the number you're dialing still belongs to the same person who gave you consent.

Under the TCPA and FCC rules, callers must have consent from the current subscriber of a telephone number. Because phone numbers frequently get reassigned to new users, the FCC has eliminated the old "one-call" exception and instead provided a safe harbor for callers who properly use the RND.

If the RND returns "Yes" (indicating a reassignment), you must not call that number without getting fresh consent, or you risk TCPA penalties. If the RND returns "No," you have documented proof that the number was good as of the query date, which grants protection in case it was actually reassigned unbeknownst to you. Failing to check the RND when required can lead to unwanted calls to random individuals and potential fines of $500 to $1,500 per call for willful violations of the TCPA.

### Benefits of Using the RND

- **Avoid TCPA Lawsuits and Fines**: Incorporating the RND into your workflow is a cost-efficient way to maintain compliance. It is far cheaper to query the database than to deal with the fallout of compliance violations or to manually track number changes. Companies that use the database can demonstrate due diligence and benefit from the FCC's safe harbor.
- **Improve Call Delivery and Contact Rates**: Scrubbing your contact lists against the RND means you won't waste time and resources calling numbers that have been disconnected or reassigned. By eliminating wrong numbers from your campaigns, your calls are more likely to reach the intended recipients.

### How to Register for the RND

Before you can submit queries, you must register as a Caller (or Caller Agent) at the official RND portal:

- Go to <https://www.reassigned.us> and read the instructions on the "Query" page. To request a login, you must send an email to [support@reassigned.us](mailto:support@reassigned.us).
- You must choose a prepaid, tiered subscription based on your expected query volume and preferred term (1-, 3-, 6-, or 12-month). The subscription price is the price per query × number of queries in that tier. The RND webpage publicly lists their pricing structure at <https://reassigned.us/pricing>.
- The RND Administrator (currently SomosGov) is a company chosen by the FCC to administer the RND. The RND Administrator will walk registrants through the rest of the process.
