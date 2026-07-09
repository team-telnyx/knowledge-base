---
source_url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
scraped: 2026-07-08
content_hash: 330252b32ac1fb45a47251b787e1bc0544cb49b895132f43194e7468710374bb
---

What is the U.S. Reassigned Numbers Database? | Telnyx Help Center

[Skip to main content](#main-content)

# What is the U.S. Reassigned Numbers Database?

Written by Telnyx Engineering

May 10, 2025

Table of contents

The U.S. Reassigned Numbers Database (RND) is a centralized FCC-authorized database that tracks telephone numbers that have been permanently disconnected and potentially reassigned to new users. It was established by the Federal Communications Commission (FCC) as part of efforts to curb unwanted calls, particularly those intended for a phone number’s former owner. When a number is reassigned, callers might inadvertently reach a new consumer who never gave consent, which can be annoying to the recipient and can expose the caller to liability under the Telephone Consumer Protection Act (TCPA). The RND’s purpose is to help voice service providers and businesses determine *before placing a call* whether a phone number has been disconnected (and thus possibly reassigned) since the time the original consent was obtained.

**How it works:** Voice service providers (like Telnyx) report permanently disconnected U.S. phone numbers into the RND on an ongoing basis (typically monthly). The official RND system (accessible at reassigned.us) allows registered callers to query a phone number with a date of last contact or consent. The database will respond with one of three results – “Yes,” “No,” or “No Data” – indicating the status of that number since the provided date. A “Yes” means the number *has* been permanently disconnected (i.e. likely reassigned) after your provided date, so calling it could reach the wrong person. A “No” means the number has not been disconnected since that date, suggesting it still belongs to the same consumer (this “No” result is what grants a safe harbor if it later turns out the number was reassigned). “No Data” means the database has no record for the query (for example, if the consent date was before the RND started tracking in 2021), and in that case no safe harbor applies.

**Regulatory background:** The FCC’s 2018 order created the RND to address calls to reassigned numbers on a nationwide scale. Since November 2021, the RND has been fully operational for paid subscribers (callers) to use in their compliance workflows. The FCC requires all telephone service providers to supply their disconnected number data to the RND, making it a comprehensive resource covering all U.S. geographic and toll-free numbers. Telnyx, as a service provider, complies by submitting monthly reports of numbers that have been permanently disconnected. (Telnyx also offers customers a 15-day window to reclaim a number after disconnecting it, before it gets reported as permanently disconnected in the next RND update.) This industry-wide reporting ensures that when you query the RND, you’re getting up-to-date information on whether a number has changed hands.

## **Who is Required to Use the RND?**

Businesses making outbound calls or texts to U.S. numbers are required by law to check the RND when relying on prior consumer consent to contact those numbers. In practice, any entity that places telemarketing, informational, or automated calls/SMS should be using the RND to verify numbers. This includes Telnyx customers such as contact centers, CPaaS providers, sales and marketing platforms, debt collectors, and robocall/auto-dialer operators – essentially, if your organization sends outbound voice calls or text messages to consumers, you need to ensure the number you’re dialing still belongs to the same person who gave you consent.

Under the TCPA and FCC rules, callers must have consent from the current subscriber of a telephone number. Because phone numbers frequently get reassigned to new users, the FCC has eliminated the old “one-call” exception and instead provided a safe harbor for callers who properly use the RND. This means that to comply with the law and avoid liability, you should query the RND before calling a number if you obtained consent in the past.

If the RND returns “Yes” (indicating a reassignment), you must not call that number without getting fresh consent, or you risk TCPA penalties. If the RND returns “No,” you have documented proof that the number was good as of the query date, which grants protection in case it was actually reassigned unbeknownst to you. Failing to check the RND when required can lead to unwanted calls to random individuals and potential fines of $500 to $1,500 per call for willful violations of the TCPA. In short, any business that contacts consumers by phone should integrate RND checks into their compliance process to adhere to U.S. regulations and maintain their safe harbor protections.

## **Benefits of Using the RND**

In addition to being a legal requirement, using the Reassigned Numbers Database provides several important benefits for businesses that engage in outbound calling:

* **Avoid TCPA Lawsuits and Fines:** Incorporating the RND into your workflow is a cost-efficient way to maintain compliance. It is far cheaper to query the database (which is available via subscription tiers based on query volume) than to deal with the fallout of compliance violations or to manually track number changes. Proactively checking the RND reduces the risk of accidentally calling the wrong person, which in turn lowers your exposure to TCPA litigation. Companies that use the database can demonstrate due diligence and benefit from the FCC’s safe harbor, protecting them if a number was mistakenly marked as safe.
* **Improve Call Delivery and Contact Rates:** Scrubbing your contact lists against the RND means you won’t waste time and resources calling numbers that have been disconnected or reassigned. By eliminating wrong numbers from your campaigns, your calls are more likely to reach the intended recipients – the customers who expect to hear from you.

## **How Do I Register for the RND?**

Before you can submit queries, you must register as a **Caller** (or **Caller Agent**) at the official RND portal:

* Go to<https://www.reassigned.us> and read the instructions on the “Query” page. To request a login, you must send an email to [support@reassigned.us](mailto:support@reassigned.us).
* You must choose a prepaid, tiered subscription based on your expected query volume and preferred term (1-, 3-, 6-, or 12-month). The **subscription price** is the *price per query* × *number of queries* in that tier. The RND webpage publicly lists their pricing structure here: <https://reassigned.us/pricing>
* The RND Administrator (currently, SomosGov) is a company chosen by the FCC to administer the RND. The RND Administrator will walk registrants through the rest of the process.

---

Related Articles

[Your Number Lookup Guide](https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide)[Robocall Mitigation Database](https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database)[What is the Reassigned Numbers Database](https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database)[Verified Numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
