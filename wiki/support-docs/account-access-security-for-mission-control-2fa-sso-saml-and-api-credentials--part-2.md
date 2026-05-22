---
title: 'Account access security for Mission Control: 2FA, SSO (SAML), and API credentials'
summary: How to secure Telnyx Mission Control Portal access with two‑factor authentication,
  set up Single Sign‑On (SAML) with popular identity providers, and create/manage
  API credentials (v2 keys and legacy v1 tokens).
sources:
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/1130624-how-do-i-create-an-api-v1-token
updated_at: 2026-05-20T14:48:03Z
---

# Account access security for Mission Control: 2FA, SSO (SAML), and API credentials

*Part 2 of 2 — see also: [Part 1](account-access-security-for-mission-control-2fa-sso-saml-and-api-credentials--part-1.md)*

How to secure Telnyx Mission Control Portal access with two‑factor authentication, set up Single Sign‑On (SAML) with popular identity providers, and create/manage API credentials (v2 keys and legacy v1 tokens).

## Identity provider quick‑starts
Use these summaries to finish configuration on your IdP side. Always map the user identifier as Email where prompted.

### Okta
- In Okta Admin: Applications → Browse App Catalog → add SAML Service Provider app.
- Set Default Relay State to https://portal.telnyx.com.
- Copy the Identity Provider metadata link; use it in Portal (IdP Metadata URL).
- In Okta Advanced Sign‑On/Credentials: paste the SP values from Portal (ACS URL and SP Entity ID). Set Application username format to Email.

### OneLogin
- In OneLogin Admin: Applications → Add App → SAML Test Connector (Advanced).
- From SSO tab, copy the Issuer URL/metadata link; use it in Portal (IdP Metadata URL) and import.
- In OneLogin Configuration: set Audience (Entity ID) to the Portal SP Entity ID; Recipient and ACS URL to the Portal ACS URL; SAML nameID format: Email. If required, set ACS URL Validator to the escaped ACS pattern provided by Telnyx.

### Microsoft Azure AD (Entra ID)
- In Azure: Enterprise Applications → New application → Microsoft Entra SAML toolkit → Set up single sign on (SAML).
- Copy App Federation Metadata URL and Thumbprint.
- In Portal SSO: import using the Metadata URL; then set IdP Certificate Fingerprint to the Azure Thumbprint and save.
- In Azure Basic SAML Configuration: set Identifier (Entity ID) = Portal SP Entity ID; Reply URL (ACS) = Portal ACS URL; Sign‑on URL = https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME; Relay State = https://portal.telnyx.com/.

### Auth0
- In Auth0: Applications → Create Application → Regular Web Application.
- Addons → enable SAML2 Web App.
- In the SAML addon Settings: set Application Callback URL = Portal ACS URL.
- Configure SAML settings to include:
  - audience = Portal SP Entity ID
  - recipient = Portal ACS URL
  - nameIdentifierFormat = the value shown in Portal
  - signResponse = true (and include the standard email claim probe as needed)
- Provide the Identity Provider Metadata (URL or file) to Portal via IdP Metadata URL import.

### LastPass
- In LastPass Admin: Applications → SSO Apps → Add unlisted app and note the Entity ID, SSO Endpoint, and Certificate Fingerprint (SHA256).
- In Portal SSO (manual configuration): set IdP Certificate Fingerprint (algorithm sha256), IdP Entity ID, and IdP SSO Target URL from LastPass.
- In LastPass Advanced Settings: set ACS = Portal ACS URL; Entity ID = Portal SP Entity ID; Identifier = Email; SAML signature method = SHA256; Sign Response = enabled.

### Google Workspace (GSuite)
- In Google Admin: Apps → Web and mobile apps → Add custom SAML app.
- Note Google’s SSO URL, Entity ID, and SHA‑256 fingerprint.
- In Portal SSO (manual configuration): set IdP Certificate Fingerprint (sha256), IdP Entity ID, and IdP SSO Target URL.
- In Google Service Provider details: set ACS URL = Portal ACS URL; Entity ID = Portal SP Entity ID; Start URL = https://portal.telnyx.com; Name ID format = Email; Name ID = Primary email.


## Enable SSO and user experience
- When IdP and Portal settings are complete, return to the Portal Single Sign‑On page, check Enable Single Sign‑On, and Save Changes.
- Users receive an email that SSO is enabled. A 72‑hour grace period allows username/password login; after that, SSO is required.


## Troubleshooting and support
- General SSO issues: Verify metadata URLs are reachable and current; ensure ACS URL, Entity ID, and NameID/email mapping match exactly; use SHA256 where required and enable “Sign Response” when specified.
- Provider status pages:
  - Okta: https://status.okta.com/
  - OneLogin: https://www.onelogin.com/status
  - Auth0: https://status.auth0.com/
  - Microsoft Azure: https://azure.status.microsoft/en-us/status
  - LastPass: https://status.lastpass.com/
  - Google Workspace: https://www.google.com/appsstatus/dashboard/
- Portal 2FA access problems: See the 2FA troubleshooting above; for urgent help or account recovery, contact help@telnyx.com.
