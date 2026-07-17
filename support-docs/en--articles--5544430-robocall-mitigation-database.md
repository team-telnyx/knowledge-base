---
source_url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
title: "Robocall Mitigation Database"
description: "In this article we outline the SHAKEN/STIR order taking effect on September 28, 2021, See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: a3dbd07e137e53fdd153db793328c9e53ec5a0303a420f64adab82ebcfd5756c
---







# Robocall Mitigation Database

In this article we outline the SHAKEN/STIR order taking effect on September 28, 2021, See Telnyx guidance and requirements.




## **Robocall Mitigation Database and Call Blocking**

*Disclaimer: The information provided herein is for informational purposes only and should not be construed as legal advice. While we strive to provide accurate and up-to-date information, regulations and legal interpretations may vary and change over time. It is important to consult with qualified legal counsel to address specific legal questions or concerns regarding regulatory compliance.*

The Federal Communications Commission (FCC) mandates that, beginning September 28, 2021, in furtherance of its robocall mitigation efforts, intermediate providers and voice service providers (VSPs) may no longer accept traffic directly from voice service providers that are not listed in the Robocall Mitigation Database (the “Database”).

In accordance with FCC directives (FCC 24-73, FCC 23-18), this means that all carriers, including Telnyx, have an obligation to begin blocking incoming calls leveraging US Calling Line Identity (CLI) from voice service providers not registered on the Database. This includes both US and foreign voice service providers that use US North American Numbering Plan resources to send voice traffic to residential or business subscribers in the United States. Foreign voice service providers were temporarily exempted from the September 28th blocking date until further notices of proposed rule-makings are determined. The FCC actually updated this rule to include foreign service providers that use US numbers starting April 11, 2023.

## **Who Qualifies As a Voice Service Provider?**

A voice service provider is defined as “any service that is interconnected with the public switched telephone network and that furnishes voice communications to an end user using resources from the North American Numbering Plan or any successor to the North American Numbering Plan adopted by the Commission under section 251(e)(1) of the Communications Act of 1934, as amended.” (47 C.F.R. 64.1600(r)(1)).

Registration in the Database is highly recommended, if applicable. The FCC’s *[Second Report and Order](https://docs.fcc.gov/public/attachments/FCC-20-136A1.pdf)* provides guidance on how to define “voice services” and subsequently a “provider of voice services.”

## **How Do I Register?**

Before you can submit a filing on the Robocall Mitigation Database website, you will need a Commission Registration System (CORES) account and an FCC Registration Number (FRN). Visit <https://apps.fcc.gov/cores/userLogin.do> for account setup and tutorials.

## **What Should Be Included In My Registration?**

The FCC requires businesses to provide:

* Business name, contact information, FRN number, and ownership information
* Type of filing (voice service provider, gateway provider, or non-gateway intermediate provider)

  + If you serve more than one role in the call chain, the FCC has instructed providers to select all options that apply.
* Whether you are a U.S. or foreign service provider.
* Certification of full, partial, or no STIR/SHAKEN implementation.

  + Telnyx authenticates every outbound call with a valid U.S. Caller ID that originates on the Telnyx platform. As a carrier, we have been approved by the STI-PA to participate in the SHAKEN/ STIR framework and are fully SHAKEN/STIR compliant. For more information, see our [support article](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx) on STIR/SHAKEN.
* A robocall mitigation plan.

  + All providers, regardless of whether they are required to implement STIR/SHAKEN—including all intermediate providers and providers that lack control over the network infrastructure necessary to implement STIR/SHAKEN—are now required to file certifications and robocall mitigation plans. These plans must describe the specific “reasonable steps” the provider has taken to avoid the origination, carrying, or processing of illegal robocall traffic as part of its robocall mitigation program, along with other information detailed in FCC 24-73.

For more detailed guidance, see the FCC’s Second Report and Order, paragraphs 19–23, and the Sixth Caller ID Authentication Report and Order at 20, 22-23, paras. 36, 40-41; 47 CFR § 64.6305(d)(2),(e)(2), (f)(2). Additionally, as a carrier, Telnyx authenticates every outbound call with a valid U.S. Caller ID that originates on the Telnyx platform and is fully SHAKEN/STIR compliant. More information can be found in our support article on STIR/SHAKEN.

## **Consulting Legal Counsel**

It is advisable for Telnyx customers and other entities to consult legal counsel to determine if registering with the RMD is required for your entity. Please note that Telnyx has registered with the RMD to ensure uninterrupted service and compliance with FCC regulations.
​

---

Related Articles

[What is Telnyx?](https://support.telnyx.com/en/articles/1130637-what-is-telnyx)[STIR/SHAKEN With Telnyx](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx)[Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)[Understanding the FCC’s Eighth Report and Order on Third-Party Authentication](https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication)[What is the U.S. Reassigned Numbers Database?](https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database)

Did this answer your question?

😞😐😃
