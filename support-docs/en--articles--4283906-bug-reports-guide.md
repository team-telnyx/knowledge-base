---
source_url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
title: "Bug Reports Guide"
description: "This article explains how to submit a bug report to the Telnyx support team. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 021f3acd5e1875d28b86bcaf8ec6a4700ff656a9446b4efff31027ab2c3e38e0
---







# Bug Reports Guide

This article explains how to submit a bug report to the Telnyx support team. See Telnyx guidance and requirements.




***Developer: There is no I in TEAM.***
​***Tester: We can’t spell BUGS without U***

![Breaking Line](_images/682991ade0be9812.png)

## **Explanation of Bug Reports**

At Telnyx, we're very much engineering focused. We're agile and iterate quickly, shipping improvements and new features regularly.

![Two insects with names "Bug" and "Feature." ](_images/bcd51a6beda3c460.jpg)

We're always grateful to our customers when it comes to identifying any and all [improvements](https://support.telnyx.com/en/articles/4283783-feature-requests), especially bugs!

Let us know if you find any by contacting our support team by email **[support@telnyx.com](mailto:support@telnyx.com),** we're always quick on hand to bring this feedback to the attention of our engineers, in order to ensure a better customer experience.
​
We always appreciate a detailed description of the bug, as well as any screenshots or videos you may have.

Don't forget! Our [mission control portal](https://portal.telnyx.com/#/login/sign-in) user interface is built on top of our [API](https://developers.telnyx.com), so check out your browsers console logs (front-end issues) or network logs (back-end issues) which can significantly help when it comes to reproducing your concerns.

**Step by Step Guide:**

1. Make sure to let us know what browser you are using and the version you are on.
2. Open the developer tools. In most browsers, you can do this by pressing F12 on your keyboard or by right-clicking on the page and selecting "Inspect" or "Inspect element" from the context menu.
3. Navigate to the website page you may have an issue with.
4. Once the developer tools are open, look for a tab labelled "Network" or "Console". Depending on your browser, this tab may be in a different location or have a different name, but it should be fairly easy to find.
5. For back-end issues click on the "Network" tab to inspect the network traffic for the page. You should see a list of requests that the browser made to load the page, including the URL, response code, and timing information.

   1. You can save a HAR file by right clicking the request that's failing and clicking "save har file".
6. For front-end issues click on the "Console" tab to inspect the console logs for the page. This is where developers often log messages and errors for debugging purposes. You can filter the logs by type, such as "Errors" or "Warnings".

   1. If you see any red logs you can right click the whitespace and save the console logs.
7. These files will be very useful to determine the cause!

If the bug is mission critical (service affecting), please open a chat with ourselves in support and we will investigate it immediately.

## Security related bugs

If you believe you have found a security vulnerability, please report it to **security@telnyx.com** rather than general support.

Telnyx welcomes responsible security research on our products and infrastructure. We value reports that demonstrate real security impact and follow the guidelines below.

## Telnyx Vulnerability Disclosure Program

## Overview

Telnyx welcomes responsible security research on our products and infrastructure. We value reports that demonstrate real security impact and follow the guidelines below.

## Scope

**In scope:** Telnyx-owned web applications, APIs, and infrastructure, including `portal.telnyx.com`, `api.telnyx.com`, and other `*.telnyx.com` properties.

**Out of scope:** Third-party services and integrations, physical security, social engineering against employees, and denial-of-service testing.

## What We’re Looking For

We want to hear about vulnerabilities with **demonstrated, real-world security impact**, such as:

* Remote code execution
* Injection flaws
* Authentication or authorization bypass
* Access to other users’ data
* Significant data exposure

## What Doesn’t Qualify

Reports are likely to be declined if they describe:

* Configuration hardening suggestions or best-practice recommendations without a working exploit
* Informational findings with no demonstrated security impact, such as version disclosure, missing headers, or cookie attributes
* Issues requiring unlikely user interaction or only affecting the reporter’s own session
* Automated scanner output without manual validation and a clear proof of concept
* Telecom service abuse, carrier routing, or call quality issues

This list is not exhaustive. Telnyx reserves the right to determine whether any reported issue constitutes a valid security vulnerability.

## Report Requirements

All security submissions must include:

1. A description of the vulnerability and affected component
2. Step-by-step reproduction instructions
3. Proof of concept, such as screenshots, requests and responses, video, or exploit code
4. Demonstrated impact — what can an attacker achieve?

Incomplete reports may be returned for clarification and may be closed if not updated.

## Rules

Researchers must follow these rules:

* Do not access or modify other users’ data
* Do not degrade service availability
* Test only against your own accounts
* Do not disclose the issue publicly before Telnyx has had reasonable time to remediate
* Stop and report immediately if you encounter customer data

## Rewards

Telnyx may offer rewards for qualifying reports at our sole discretion, based on severity, exploitability, and impact.

Informational findings and out-of-scope reports are not eligible for rewards.

## Submission

Send security reports to **security@telnyx.com** with the subject:

`[Vulnerability Report] <Brief Description>`

## Safe Harbor

Telnyx will not pursue legal action against researchers who act in good faith, follow this policy, and report findings to Telnyx before any public disclosure.

*Last updated: May 2026 · Questions? security@telnyx.com*
​

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[Best Practices for Contacting Support](https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support)[Understanding Telnyx SOC Compliance and Certifications](https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications)[Guide to Sole Proprietor 10DLC Brand and Campaign Registration](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)[Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)

Did this answer your question?

😞😐😃
