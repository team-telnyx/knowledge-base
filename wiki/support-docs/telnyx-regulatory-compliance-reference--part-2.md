---
title: Telnyx Regulatory & Compliance Reference
summary: A consolidated reference for Telnyx customers covering U.S. and state regulatory
  requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security
  certifications, traffic surcharges, and number lifecycle policies that affect voice
  and messaging services.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Regulatory & Compliance Reference

*Part 2 of 5 — see also: [Part 1](telnyx-regulatory-compliance-reference--part-1.md), [Part 3](telnyx-regulatory-compliance-reference--part-3.md), [Part 4](telnyx-regulatory-compliance-reference--part-4.md), [Part 5](telnyx-regulatory-compliance-reference--part-5.md)*

A consolidated reference for Telnyx customers covering U.S. and state regulatory requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security certifications, traffic surcharges, and number lifecycle policies that affect voice and messaging services.

## U.S. Reassigned Numbers Database (RND)

The FCC's [Reassigned Numbers Database](https://www.fcc.gov/reassigned-numbers-database), authorized in December 2018, enables callers to determine whether a telephone number has been permanently disconnected and is therefore no longer assigned to the person they intended to reach. The RND has been fully operational for paid subscribers since November 2021.

### How It Works

Voice service providers (including Telnyx) report permanently disconnected U.S. phone numbers into the RND on an ongoing basis, typically monthly. The official RND system at [reassigned.us](https://www.reassigned.us) allows registered callers to query a phone number with a date of last contact or consent. The database returns one of three results:

- **Yes** – the number has been permanently disconnected (likely reassigned) after the provided date; calling it could reach the wrong person.
- **No** – the number has not been disconnected since that date, suggesting it still belongs to the same consumer. This result grants a safe harbor if the number was actually reassigned.
- **No Data** – the database has no record for the query (for example, if the consent date was before the RND started tracking in 2021); no safe harbor applies.

Telnyx offers customers a 15-day window to reclaim a number after disconnecting it, before it is reported as permanently disconnected in the next RND update. After 15 days, the number is permanently disconnected and reported in the next monthly cycle (the 15th of each month). Once reported, the wider industry is made aware of the disconnect and should no longer attempt to contact that number. Any prior consent given to third parties (for example, pharmacies) is no longer applicable, and any settings previously associated with the number must be reset manually if it is later repurchased.

### Who Must Use the RND

Businesses making outbound calls or texts to U.S. numbers are required by law to check the RND when relying on prior consumer consent. This includes contact centers, CPaaS providers, sales and marketing platforms, debt collectors, and robocall/auto-dialer operators. Under the TCPA and FCC rules, callers must have consent from the current subscriber of a telephone number. The FCC has eliminated the old "one-call" exception and instead provides a safe harbor for callers who properly use the RND.

If the RND returns "Yes," the caller must not call that number without fresh consent or risk TCPA penalties. If it returns "No," the caller has documented proof that the number was good as of the query date. Failing to check the RND when required can lead to unwanted calls to random individuals and potential fines of $500 to $1,500 per call for willful TCPA violations.

### Benefits

Using the RND helps businesses avoid TCPA lawsuits and fines, demonstrate due diligence, and benefit from the FCC's safe harbor. It also improves call delivery and contact rates by eliminating wrong numbers from outbound campaigns.

### How to Register

Before submitting queries, customers must register as a Caller (or Caller Agent) at the official RND portal:

1. Visit [reassigned.us](https://www.reassigned.us) and review the instructions on the Query page.
2. Email [support@reassigned.us](mailto:support@reassigned.us) to request a login.
3. Choose a prepaid, tiered subscription based on expected query volume and preferred term (1-, 3-, 6-, or 12-month). Pricing is published at [reassigned.us/pricing](https://reassigned.us/pricing).
4. The RND Administrator (currently SomosGov) will walk registrants through the rest of the process.

## Texas Mini-TCPA (Senate Bill 140)

Texas Senate Bill 140 ("[SB 140](https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB00140F.pdf)"), an amendment to the state's "Mini-TCPA," expands and revises the telemarketing framework under the Texas Business & Commerce Code. Companies based in Texas or marketing to Texas residents, including via text, must register as a telemarketer by **September 1, 2025**.

### Key Changes

- **Text message solicitations are now explicitly regulated.** A "telephone solicitation" includes any voice or other transmission, including a text or graphic message or image, initiated by a seller or salesperson to induce a person to purchase, rent, claim, or receive an item.
- **Quiet hours extended to texting.** Restrictions on when solicitations can be made now apply equally to text messages:
  - Monday–Saturday: not before 9 a.m. or after 9 p.m. (recipient's local time)
  - Sunday: only between 12 p.m. and 9 p.m.
  - Exceptions under [Sec. 301.051](https://statutes.capitol.texas.gov/SOTWDocs/BC/htm/BC.301.htm) include communications sent in direct response to a consumer's explicit request or to an individual with whom the sender has an existing business relationship.
- **Registration requirements.** Businesses sending marketing texts may need to register with the Texas Secretary of State if they are based in Texas or send solicitations to individuals located in Texas, unless an exemption applies. A "purchaser" is an individual who is solicited to become or becomes obligated for the purchase or rental of an item, or is offered an opportunity to claim or receive an item. Registration requires filing a registration statement with the Texas Secretary of State, paying a $200 filing fee, and posting a $10,000 security deposit for the benefit of any person injured by the seller's breach of the law. See the [Texas Secretary of State's website](https://www.sos.state.tx.us/statdoc/faqs3400.shtml) for details. Failure to properly register includes potential civil penalties of up to $5,000 per violation, enforced by the Attorney General.
- **Exemptions** include companies soliciting business from a former or current customer, securities brokers/dealers (state or SEC qualified/exempt), publicly traded corporations (and subsidiaries/agents), licensed insurance professionals (when selling insurance), banks and other supervised financial institutions (and affiliates), utilities regulated by the PUC (except for use of autodialers), companies selling subscriptions to newspapers, magazines, or cable TV, schools, colleges, and §501(c)(3) nonprofits, and persons soliciting the sale of food. Additional exemptions are listed in [Sec. 302.051](https://statutes.capitol.texas.gov/docs/BC/htm/BC.302.htm).
- **Expanded right to sue.** SB 140 creates a new private right of action for telemarketing violations, including ignoring call time restrictions, failing to register, not honoring opt-outs, and using autodialers/robocall systems. Consumers can seek both economic and mental anguish damages, and each violation is actionable with no cap, even if a consumer has already recovered for similar violations.

Organizations marketing to Texas residents by phone or text, or based within Texas, should review their outreach practices and evaluate whether they qualify for exemptions or must register. For additional guidance, contact [regulatory@telnyx.com](mailto:regulatory@telnyx.com).
