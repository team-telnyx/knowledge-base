---
title: Telnyx Compliance, Security, and Platform Reference
summary: A comprehensive reference for Telnyx regulatory compliance obligations, security
  certifications, privacy practices, and key platform operational details — covering
  STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers
  Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
  content_hash: 67ee5a4378cda34b22669a4edc5f1925fb15b17fb7d3df43185bfd41478988d4
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
  content_hash: 2b00e4c40be23e8f5e6d8b498837c82ac949e40bf00070dafa1b2855e5b545d6
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
  content_hash: 056e70a4c1d28bc5d0d9d3df1ccdbf278417fe9bf3ba3ed4050e840cc711fe77
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
  content_hash: 8c00b9aa07357e8d25a598fbdf4427471e341bc0884ddfc96abd5d756eb2cad8
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
  content_hash: c5df94264f27b812390ce017f8ef890db223f16fca99b9434ec0d8ea51d4a2d1
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
  content_hash: 52b9cee458ba618dd725be8b39606bb73124227173e321b447a07b61e0fd2b48
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
  content_hash: 3ed45bcc93c15873a6b90d4faa89b4c1848b163dd9f3183fa9ab31f0860dbd45
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
  content_hash: 8e5e86140d4a3301f5ae5a654f92de4fdbc0631efe3a1f4b50e599e6a89b36f8
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
  content_hash: c7f2d8d7965abfc1368a2b9ca731972644ec147a989d7d4c14bd0c1615163242
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
  content_hash: d9cee1dd07e51e4df40626dbca4595f63c0bfa52827c904524a8a59c8cdf6554
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
  content_hash: 531786ea6bae25ec05258db23e53bb7eebaeac53bcaff8eddadaf61dd2b6040f
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
  content_hash: 86b9d3397acf1f7f2d3720fd46fcb02ce272d955298f4e81764795dd321fb8b7
updated_at: 2026-06-11T11:44:06Z
---

# Telnyx Compliance, Security, and Platform Reference

*Part 1 of 3 — see also: [Part 2](telnyx-compliance-security-and-platform-reference--part-2.md), [Part 3](telnyx-compliance-security-and-platform-reference--part-3.md)*

A comprehensive reference for Telnyx regulatory compliance obligations, security certifications, privacy practices, and key platform operational details — covering STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.

## STIR/SHAKEN Caller ID Authentication

STIR/SHAKEN (Secure Telephony Identity Revisited / Secure Handling of Asserted information using toKENs) is an FCC-mandated framework to reduce fraudulent calls and robocalls over IP networks. Originating service providers assign an attestation level to each call and include a signed token in the SIP INVITE header; terminating providers validate the token before connecting the call.

### Attestation Levels

| Level | Name | Meaning |
|-------|------|--------|
| A | Full Attestation | The provider knows the customer, confirms their right to use the originating number, and confirms the call originated on its network. Expected for numbers purchased or ported into Telnyx. |
| B | Partial Attestation | The provider knows the customer but cannot fully verify the originating number (e.g., the number was not purchased from Telnyx). The call is still legitimate. |
| C | Gateway Attestation | The provider cannot verify the customer or the number; the token simply marks that the call originated on the provider's network. |
| Unavailable | — | The origination provider did not add the necessary information, or the token was lost when the call hit the PSTN. |
| Invalid | — | The provider did not properly authenticate the customer or number; Telnyx could not verify the token's authenticity. |

Attestation values are available in CSV downloads from the [reporting section](https://portal.telnyx.com/#/reporting/detailed-records) of the Mission Control Portal. To increase attestation to level A, customers should consider porting their numbers to Telnyx via [Fastport](https://telnyx.com/products/number-porting).

### Telnyx's STIR/SHAKEN Coverage

Telnyx is fully compliant with STIR/SHAKEN. Every outbound call with a valid U.S. Caller ID that originates on the Telnyx platform receives attestation at no additional charge and with no customer action required. Telnyx is approved by the STI-PA to participate in the framework and is listed in the FCC's Robocall Mitigation Database. Inbound calls with A attestation and a valid token receive a `verstat` parameter on P-Asserted-Identity headers.

### Canadian STIR/SHAKEN

Canadian STIR/SHAKEN uses the same attestation definitions (A, B, C). Outbound calls with Canadian CLI receive appropriate signings from Telnyx's Canadian partners automatically — no customer action is required. If your Canadian CLI is listed in the Telnyx Mission Control Portal (purchased or ported), you receive A attestation; otherwise, B attestation applies. There is no additional charge for Canadian SHAKEN/STIR services.

### On-Net Calling and Identity Headers

For customers receiving calls from other Telnyx customers who want identity headers, register with a credentials connection via TCP, or specify TCP as the inbound transport protocol for IP/FQDN connections. TCP is required because the Identity header is large and UDP would risk packet fragmentation and call-completion issues.

### Signing Your Own Calls

Some service providers are eligible to sign their own calls even if they buy numbers from Telnyx. Requirements include:

1. A 499-A (Telecommunications Reporting Worksheet) on file with the FCC.
2. An Operating Company Number (OCN).
3. A robocall mitigation plan filed with the FCC.
4. Valid certificates from an approved Certificate Authority.
5. A SHAKEN/STIR solution implemented on your network.

Approval must come from the [Secure Telephone Identity Policy Administrator (STI-PA)](https://authenticate.iconectiv.com/), which is vetted by the [Secure Telephone Identity Governance Administrator (STI-GA)](https://sti-ga.atis.org/). Once approved, Telnyx will pass your certificate to its terminating provider.

## FCC Eighth Report and Order on Third-Party Authentication

Effective September 18, 2025, the FCC's [Eighth Report and Order](https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf) prohibits "third-party authentication" — arrangements where a provider with a STIR/SHAKEN obligation contracts a third party to sign calls on its behalf — unless two conditions are met:

1. The provider **independently determines attestation levels** in accordance with STIR/SHAKEN technical standards.
2. All calls are authenticated using the provider's **own certificate** obtained from a STIR/SHAKEN Certificate Authority, not a third party's certificate.

Any third-party signing arrangement that fails to meet both conditions violates the FCC's caller ID authentication rules.

### Who Must Obtain an SPC Token

Originating service providers (OSPs) with control over their network infrastructure must obtain a Service Provider Code (SPC) token from the STIR/SHAKEN Policy Administrator and use it to get a certificate from a Certificate Authority.

**Telnyx requires you to obtain your own SPC token if:**
- You use both Telnyx and another provider and either send calls using numbers from another operator across the Telnyx network, or send calls from Telnyx numbers across another provider's network.
- You intend to spoof caller ID (which additionally requires whitelisting for legitimate caller ID spoofing).

**Telnyx does not require you to obtain an SPC token if:**
- You exclusively use Telnyx numbers for both origination and termination.
- You only use a limited number of outside [Verified Numbers](https://support.telnyx.com/en/articles/6790265-verified-numbers-faq).

### Steps to Obtain an SPC Token and Sign Your Own Calls

1. **Obtain an OCN (Company Code).** Apply through [NECA](https://www.neca.org/business-solutions/company-codes) for an Operating Company Number.
2. **Register to File 499-A.** Obtain an FRN from [CORES](https://apps.fcc.gov/cores/userLogin.do) and a Filer ID from USAC's E-File system. See the [2025 Telecommunications Reporting Worksheet Instructions](https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf).
3. **Register in the Robocall Mitigation Database.** Your company must have a valid active RMD registration (requires CORES account and FRN). See the [FCC's external filing instructions](https://www.fcc.gov/sites/default/files/rmd-instructions.pdf).
4. **Register with iConectiv (STI-PA).** Complete the [iConectiv Service Provider registration form](https://authenticate.iconectiv.com/service-provider-authenticate), providing legal business name, type of voice service provider, and evidence of authorization (e.g., FCC 499 Filer ID or OCN).
5. **Select a Certificate Authority.** Once your SPC token is issued, choose a CA from the STI-PA's approved list to obtain your STIR/SHAKEN certificate.
6. **Sign Your Own Calls With Telnyx.** Use Telnyx's [Hosted Signing Service](https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert) to digitally sign calls with your own certificate while maintaining full control over attestation levels (A, B, or C) — without building signing infrastructure in-house.

### Impact on the Robocall Mitigation Database

The Eighth Report and Order also mandates that any provider certifying "Partial" or "Complete" STIR/SHAKEN implementation in the RMD must have an SPC token and digital certificate. Pure resellers with no control over network infrastructure **cannot** claim "Partial" or "Complete" implementation; they must select "No STIR/SHAKEN Implementation" and include an explanatory note citing [47 CFR 64.6305(d)(2)(i)](https://www.ecfr.gov/current/title-47/part-64/subpart-HH#p-64.6305(d)(2)). If you have certified "Complete" or "Partial" in the RMD, Telnyx can no longer sign calls on your behalf. Improperly certified resellers must update their RMD registration.
