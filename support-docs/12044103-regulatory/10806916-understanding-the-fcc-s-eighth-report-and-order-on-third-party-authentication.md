---
source_url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
scraped: 2026-06-11
---

Understanding the FCC’s Eighth Report and Order on Third-Party Authentication | Telnyx Help Center

[Skip to main content](#main-content)

# Understanding the FCC’s Eighth Report and Order on Third-Party Authentication

Written by Telnyx Engineering

April 10, 2026

Table of contents

# What Telnyx Customers Need to Know

The Federal Communications Commission (FCC) has issued new compliance requirements in its [Eighth Report and Order concerning third-party authentication](https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf). These rules, which impact **originating service providers (OSPs) with a STIR/SHAKEN obligation**, will take effect September 18, 2025. It is crucial for Telnyx customers to understand these requirements to ensure compliance and avoid potential service disruptions.

In this Report and Order, the FCC prohibits the use of “third-party authentication,” which it defines as an arrangement in which a provider subject to a STIR/SHAKEN implementation obligation under the Commission’s rules contracts with a third party to perform the technical function of signing calls on the provider’s behalf. The FCC limits permissible third-party authentication arrangements to those in which the provider subject to the STIR/SHAKEN implementation obligation: (1) independently determines attestation levels in accordance with STIR/SHAKEN technical standards, and (2) ensures that all calls are authenticated using its own certificate obtained from a STIR/SHAKEN Certificate Authority, rather than relying on a third party’s certificate. Any use of a third party to sign traffic without meeting these requirements constitutes a **violation of the Commission’s caller ID authentication rules**.

Additionally, the FCC mandates that any provider certifying to **partial or full STIR/SHAKEN implementation in the Robocall Mitigation Database must be registered with the STIR/SHAKEN Policy Administrator**, obtain its own SPC token from the Policy Administrator, use that token to generate a certificate with the Certificate Authority, and authenticate all calls using that certificate.

# Who Is Required to Secure Their Own SPC Tokens?

The Eighth Report and Order clarifies that **originating service providers (OSPs) with control over their network infrastructure** must obtain a Service Provider Code (SPC) token from the STIR/SHAKEN Policy Administrator and then present that token to a STIR/SHAKEN Certificate Authority to obtain a certificate.

For Telnyx customers, this means, **we will require you to obtain your own SPC token** to properly sign and authenticate your calls:

* **If you use both Telnyx and another provider and either:**

  1. Send calls using numbers from another operator across our network, **or**
  2. Send calls from Telnyx numbers across another provider’s network
* If you intend to **spoof caller ID** (which you also may only do so if you are **whitelisted** for legitimate caller ID spoofing)

However, our internal policies **will not require** you to obtain an SPC token:

* If you **exclusively use Telnyx numbers** for both origination and termination.
* If you only use a **limited number of outside [Verified Numbers](https://support.telnyx.com/en/articles/6790265-verified-numbers-faq)**.

# FCC Compliance and the Robocall Mitigation Database

The FCC maintains a record of originating, intermediate, and gateway service providers and their STIR/SHAKEN implementation status in the Robocall Mitigation Database (RMD). In the Eighth Report & Order, the FCC mandates that any OSP certifying that they have "Partial" or "Complete" STIR/SHAKEN implementation in the RMD must have an SPC token and digital certificate.

* Pure resellers who **do not have control over their network infrastructure** **cannot** claim to have **“Partial” or “Complete” STIR/SHAKEN Implementation** in their RMD filings.

  + Instead, these providers must select **“No STIR/SHAKEN Implementation”** and include an explanatory note indicating their exemption due to a lack of control over the network infrastructure necessary to implement STIR/SHAKEN, pursuant to [47 CFR 64.6305(d)(2)(i)](https://www.ecfr.gov/current/title-47/part-64/subpart-HH#p-64.6305(d)(2)).
* If you have stated in the RMD that your company has “Complete” or “Partial” STIR/SHAKEN implementation, **Telnyx will no longer be able to sign calls on your behalf.**
* If you have improperly certified and instead are a **pure reseller with no control over the network infrastructure**, you must **update your RMD registration** to properly reflect your status.

# Next Steps

If you determine that you do qualify as an OSP with a STIR/SHAKEN implementation obligation, you must do the following under the new regulations:

* **STEP ONE: Obtain an OCN (or “Company Code”).** Before you can obtain an SPC token, your company must have an Operating Company Number (OCN) from the Nation Exchange Carrier Association (NECA). OCNs are used to uniquely identify telecommunications service providers per industry standard ATIS-0300251. NECA assigns all Company Codes. For more information, visit the [NECA website](https://www.neca.org/business-solutions/company-codes).
* **STEP TWO: Register to File 499-A.** You must be prepared to file FCC Form 499-A before securing an SPC token. Registration with the Commission includes obtaining an FCC registration number (“FRN”) from the Commission registration system (“CORES”) and obtaining a Filer ID from USAC’s E-File system. Read the [2025 Telecommunications Reporting Worksheet Instructions](https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf) for more information.
* **STEP THREE: Register in the Robocall Mitigation Database.** Your company must have also a valid active registration in the FCC’s Robocall Mitigation Database (RMD.) As when filing a 499-A, before you can file in the RMD your company must have a CORES account and FRN. For more information on how to file in the RMD, we encourage you to read the FCC’s [external filing instructions](https://www.fcc.gov/sites/default/files/rmd-instructions.pdf).
* **STEP FOUR: Register with iConectiv.** Next, you must register with the Secure Telephone Identity Policy Administrator (STI-PA), which is currently managed by iConectiv. Start by filling out the iConectiv Service Provider registration form available on the STI-PA website. You will need to provide:

  + Legal business name and contact information
  + Type of voice service provider (e.g., facilities-based, VoIP, reseller)
  + Evidence of your authorization to provide voice services in the U.S. (such as an FCC 499 Filer ID or Operating Company Number)
  + For detailed instructions, refer to the official [iConectiv Service Provider Guide](https://authenticate.iconectiv.com/service-provider-authenticate). iConectiv will walk you through the next steps.
* **STEP FIVE: Select a Certificate Authority.** Once your organization has successfully activated its account with the STI-PA and received its SPC token, the next step is to select a Certification Authority (CA) authorized by the STI- PA. This CA will issue your organization's STIR/SHAKEN certificate, which is required to begin signing calls under your own identity. The CA will validate your eligibility using the SPC token issued by the STI-PA. Only CAs on the official STI-PA approved list are permitted to issue these certificates.
* **STEP SIX: Sign Your Own Calls With Telnyx.** After obtaining your STIR/SHAKEN certificate from an approved Certification Authority, you’re ready to begin signing your outbound calls using your own credentials. Telnyx’s Hosted Signing Service will allow you to use your certificate without building signing infrastructure in-house. This service will enable your organization to:

  + Digitally sign calls with your own certificate, meeting industry and regulatory standards; and
  + Maintain full control over attestation levels (A, B, or C) for your U.S. traffic.
  + For more information on our Hosted Stir/Shaken Product Offering, see our [Product Guide](https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert).

**Disclaimer: The information provided in this Telnyx support article is for general informational purposes only and should not be construed as legal advice. Please consult with a qualified attorney for guidance on legal or regulatory compliance.**

---

Related Articles

[Telnyx - How to Handle Spam Scam Likely](https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely)[STIR/SHAKEN With Telnyx](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx)[Robocall Mitigation Database](https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database)[Inbound Call Screening](https://support.telnyx.com/en/articles/8037040-inbound-call-screening)[Understanding SIP 603+ carrier rejections](https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections)

Did this answer your question?

😞😐😃

Table of contents
