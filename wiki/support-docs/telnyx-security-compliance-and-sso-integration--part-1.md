---
title: Telnyx Security, Compliance, and SSO Integration
summary: This page consolidates Telnyx's security, compliance, and identity management
  documentation. It covers Telnyx's SOC 2 Type I, SOC 2 Type II, and SOC 3 certifications,
  the security practices validated by these audits, and how to request reports via
  the Trust Center. It also provides step-by-step instructions for configuring SAML-based
  Single Sign-On with the Telnyx Mission Control Portal using OneLogin, Okta, LastPass,
  Microsoft Azure AD, Auth0, and GSuite.
sources:
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
updated_at: 2026-07-17T09:08:09Z
---

# Telnyx Security, Compliance, and SSO Integration

*Part 1 of 4 — see also: [Part 2](telnyx-security-compliance-and-sso-integration--part-2.md), [Part 3](telnyx-security-compliance-and-sso-integration--part-3.md), [Part 4](telnyx-security-compliance-and-sso-integration--part-4.md)*

This page consolidates Telnyx's security, compliance, and identity management documentation. It covers Telnyx's SOC 2 Type I, SOC 2 Type II, and SOC 3 certifications, the security practices validated by these audits, and how to request reports via the Trust Center. It also provides step-by-step instructions for configuring SAML-based Single Sign-On with the Telnyx Mission Control Portal using OneLogin, Okta, LastPass, Microsoft Azure AD, Auth0, and GSuite.

## Telnyx Security, Compliance, and SSO Integration Overview

Telnyx maintains a robust security and compliance posture validated through independent third-party audits, and supports SAML-based Single Sign-On (SSO) integration with multiple identity providers for the Mission Control Portal.

## SOC Compliance and Certifications

Telnyx undergoes independent audits to validate its security and compliance controls. These SOC reports provide third-party assurance that Telnyx follows industry-recognized standards around data security, availability, confidentiality, and integrity.

- **SOC 2 Type I**: Evaluates whether the design of controls is appropriate at a specific point in time.
- **SOC 2 Type II**: Assesses whether those controls operate effectively over a defined period.
- **SOC 3**: A high-level, publicly shareable summary of the SOC 2 report.

Telnyx holds SOC certifications covering services such as Programmable Voice, Messaging, Wireless, and Video, demonstrating robust controls across multiple domains.

### Requesting SOC Reports

Detailed audit reports like SOC 2 Type II are sensitive and generally made available under NDA. Telnyx publishes them via the **Trust Center** at [trust.telnyx.com](https://trust.telnyx.com/).

1. Navigate to **trust.telnyx.com**.
2. Choose the report you want (e.g. SOC 2 Type II).
3. Log in or complete the request form.
4. Telnyx may require a signed NDA before sharing the full report.

### Security Posture and Practices

While the full report is confidential, the audit confirms or supports the following security and operational practices:

- **Governance and Policy Structure**: A formal information security program with documented policies covering security, availability, and confidentiality.
- **Risk and Compliance Management**: Periodic, structured risk assessments with ownership and remediation tracking, and alignment with recognized frameworks (e.g. NIST, ISO, CIS) through a risk-based security program.
- **Access Control Mechanisms**: Role-based access control (RBAC) and least-privilege principles; multi-factor authentication (MFA) for elevated or administrative access; routine access reviews and prompt removal of access on role changes or termination; and physical security controls at data centers (surveillance, controlled entry, visitor logs).
- **Operations, Monitoring, and Incident Response**: Continuous system monitoring and alerting for anomalies, and defined incident response workflows to respond promptly to security events.
- **Change Management and Secure Development**: Structured approval and review process for infrastructure and software changes, and use of static/dynamic scanning, penetration testing, and threat modeling prior to deployment.
- **Vendor and Third-Party Controls**: Security assessments of vendors before engagement; contracts with confidentiality, security, and data return/deletion clauses; and periodic vendor reviews for ongoing compliance.

### Why SOC Compliance Matters

- Gain **third-party validation** that Telnyx's controls are well designed and operate reliably.
- Increase confidence that **sensitive or regulated data** is handled appropriately.
- Ease your own audit and compliance efforts by referencing vetted vendor controls.

| Certification | Scope | Customer Impact |
| --- | --- | --- |
| SOC 2 Type I | Control design | Confirms security processes are properly structured |
| SOC 2 Type II | Operational effectiveness | Demonstrates consistency and reliability over time |
| SOC 3 | Public summary | Allows broad sharing of trust without disclosing sensitive detail |

## Privacy and Data Handling

In addition to security controls, Telnyx is committed to privacy and data protection. Key points drawn from the [Telnyx Privacy Policy](https://telnyx.com/privacy-policy) include:

- **GDPR and CCPA Compliance**: Telnyx complies with data privacy laws and ensures that personal data is processed according to legal obligations.
- **Limited Use and Purpose Restriction**: Customer data and personal information are only used for purposes you authorize or as required by law.
- **Data Subject Rights**: You may access, correct, erase, or object to processing of your personal data through Telnyx's "request to control and review data" mechanism.
- **Data Locality Options**: Telnyx offers a choice of where to store call detail records (CDRs) and message detail records (MDRs) at rest (data locality).
- **Processor and Controller Roles**: Depending on usage, Telnyx may act as a data processor or controller, but always ensures compliance with contractual and legal privacy obligations.

## SAML Single Sign-On (SSO) for the Telnyx Mission Control Portal

Telnyx supports SAML 2.0 Single Sign-On for the Mission Control Portal, allowing organizations to authenticate users through their preferred identity provider. Supported providers include OneLogin, Okta, LastPass, Microsoft Azure AD, Auth0, and GSuite.

### Common Prerequisites

Before configuring any SAML identity provider with Telnyx:

- Ensure that your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) is configured properly.
- RECOMMENDED: Enable TLS to encrypt your traffic.
- Create an Organization in the Organization section of the Telnyx Mission Control Portal and record the **Assertion Consumer Service URL**.

### General SSO Configuration Flow

While each identity provider has provider-specific steps, the general flow is:

1. Create a SAML application in your identity provider.
2. In the Telnyx Mission Control Portal, navigate to **Single Sign-On** and click **Enable Single Sign-On**.
3. Provide an **Authentication Provider Name**, **Short Name** (used in SSO URLs), and either an **IdP Metadata URL** or manually entered configuration values (IdP Certificate Fingerprint, Entity ID, SSO Target URL).
4. Click **Import IdP Settings & Save** (or **Save Changes** for manual entry).
5. Note the generated **Assertion Consumer Service URL**, **Service Provider Entity ID**, and (where applicable) **Name Identifier Format**.
6. Return to your identity provider and enter these values into the corresponding SAML configuration fields.
7. In the Telnyx Mission Control Portal, check **Enable Single Sign-On** and click **Save Changes**.

After enabling SSO, all users in your organization receive an email notification. Users can still log in with username/password for 72 hours, after which SSO is required.
