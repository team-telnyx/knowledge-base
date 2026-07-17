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

*Part 1 of 7 — see also: [Part 2](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-2.md), [Part 3](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-3.md), [Part 4](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-4.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 6](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-6.md), [Part 7](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-7.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## Overview of U.S. Telecommunications Regulatory Requirements for Telnyx Customers

Telnyx customers operating in the United States must navigate a complex web of FCC regulations, industry frameworks, and state-level laws governing voice and messaging services. This page consolidates the key compliance obligations that affect how customers originate, sign, and route calls, as well as how they manage telephone numbers and outbound communications.

## STIR/SHAKEN Call Authentication Framework

STIR/SHAKEN is an industry framework mandated by the Federal Communications Commission (FCC) to reduce fraudulent calls and robocalls made over IP networks. The acronym stands for **Secure Telephony Identity Revisited (STIR)** and **Secure Handling of Asserted information using toKENs (SHAKEN)**. The framework was implemented on June 30, 2021, and the FCC has since moved up deadlines requiring small service providers to sign their own outbound calls with their own SHAKEN tokens starting June 30, 2022.

Originating service providers assign an **attestation** level to calls made on their network and embed a token in the SIP INVITE header. The terminating service provider validates the signature and connects the call, and may pass along validation results for additional action such as blocking.

### Attestation Levels

There are three levels of attestation, plus two unavailable states:

- **Full Attestation (A)**: The provider knows the customer, knows they have the right to use the originating number, and knows the call originated on their network. Numbers purchased in the Telnyx portal typically receive this level.
- **Partial Attestation (B)**: The provider knows the customer but may not know the number they are using. The call is legitimate but the provider is missing information that would classify it as Full Attestation. Numbers not bought on the Telnyx portal typically receive this level.
- **Gateway Attestation (C)**: The origination provider cannot verify the customer or the phone number, and has no way to verify if the traffic is legitimate. The call is still given a token to mark that it originated on the provider's network.
- **Unavailable**: The origination provider did not add the necessary information for the call to be verified, or the call hit the PSTN so the token was lost.
- **Invalid**: The origination provider did not properly authenticate the customer or phone number; the call has a token but Telnyx was not able to verify its authenticity.

Attestation values are available for review via CSV files downloaded from the [reporting section](https://portal.telnyx.com/#/reporting/detailed-records) in the Mission Control portal.

### Telnyx's STIR/SHAKEN Implementation

Telnyx is fully compliant with STIR/SHAKEN, and all calls originating on the Telnyx network receive attestation with no action required by the customer. Telnyx has been approved by the STI-PA to participate in the SHAKEN/STIR framework and authenticates every outbound call with a valid U.S. Caller ID that originates on the Telnyx platform. Inbound calls with A attestation and a valid token will have the `verstat` parameter added to P-Asserted-Identity headers.

Customers who would like to receive an A attestation should consider porting their numbers over using the Telnyx portal. With [Fastport](https://telnyx.com/products/number-porting), customers can port their numbers to Telnyx in just a few clicks.

### Signing Your Own Calls

Some service providers are eligible to sign their own calls, even if they buy their numbers from Telnyx. To sign your own calls, a company must:

1. Be approved by the [Secure Telephone Identity Policy Administrator](https://authenticate.iconectiv.com/) (STI-PA), which is vetted by the [Secure Telephone Identity Governance Administrator](https://sti-ga.atis.org/) (STI-GA).
2. Have a 499A (Telecommunications Reporting Worksheet) on file with the FCC.
3. Have an Operating Company Number (OCN) used to identify CLEC and Reseller usage data.
4. Have a robocalling mitigation plan filed with the FCC.
5. Have obtained valid certificates from an approved Certificate Authority.
6. Have implemented a SHAKEN/STIR solution on their network.

For more information, see [STIR/SHAKEN With Telnyx](stir-shaken-with-telnyx.md).

### SHAKEN/STIR verstat Parameters

Telnyx has introduced additional values to the `verstat` parameter in SIP headers to provide more granular information about originating Caller ID attestation and verification results. The `verstat` parameter is included in the P-Asserted-Identity SIP header.

Previously, the possible values were `TN-Validation-Passed`, `TN-Validation-Failed`, or `No-TN-Validation`. Two additional values have been introduced:

- `TN-Validation-Passed-B`: Identity header verification is successful, and the call has a B attestation.
- `TN-Validation-Passed-C`: Identity header verification is successful, and the call has a C attestation.

| Verstat value | Description |
| --- | --- |
| TN-Validation-Passed | Identity header verification is successful, and the caller has an A attestation |
| TN-Validation-Failed | Identity header verification failed as the certificate Telnyx received was deemed invalid |
| No-TN-Validation | No verification took place because the Identity header was not provided |
| TN-Validation-Passed-B | Identity header verification is successful, and the caller has a B attestation |
| TN-Validation-Passed-C | Identity header verification is successful, and the call has a C attestation |

Example P-Asserted-Identity header:

```
P-Asserted-Identity:"John Doe"<sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

When using SHAKEN/STIR, the `shaken_stir_param` controls whether the identity header is present in the B leg. It requires that both of the following conditions be true to successfully pass the identity header:

- `shaken_stir_enabled` is `true` (from CPB connection settings — the B-leg)
- `cpb_transport_protocol` is `"TCP"` or `"TLS"`

Identity headers are not sent over UDP to prevent fragmentation issues.

### On-Net Calling

Where customers are receiving calls from other Telnyx customers and want to receive identity headers, ensure you register with your credentials connection via TCP, or for IP/FQDN connection specify TCP as the inbound transport protocol. This prevents packet fragmentation and call completion issues since the Identity header is very large.
