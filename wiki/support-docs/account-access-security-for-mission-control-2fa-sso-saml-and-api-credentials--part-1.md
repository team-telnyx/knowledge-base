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

*Part 1 of 2 — see also: [Part 2](account-access-security-for-mission-control-2fa-sso-saml-and-api-credentials--part-2.md)*

How to secure Telnyx Mission Control Portal access with two‑factor authentication, set up Single Sign‑On (SAML) with popular identity providers, and create/manage API credentials (v2 keys and legacy v1 tokens).

## Two‑factor authentication (2FA) in Mission Control
Two‑factor authentication adds a one‑time verification step when signing in to the Mission Control Portal.

- Where to enable: Account → Security settings in the Portal
- Methods:
  - Authenticator app (TOTP): Preferred. Works with Google Authenticator, Microsoft Authenticator, 1Password, and other standards‑based TOTP apps.
  - SMS/Call: Use if TOTP isn’t feasible. Delivery can be affected by device, carrier, coverage, roaming, and rate limits.

Set up TOTP
1) Sign in → Account → Security settings → enable Two‑Factor Authentication. 2) Choose TOTP, scan the QR with your authenticator app. 3) Enter the current code to confirm. 4) Save backup codes securely.

Set up SMS/Call
1) Sign in → Account → Security settings → enable Two‑Factor Authentication. 2) Choose SMS/Call and enter a reachable number. 3) Receive code via SMS or Call and confirm. 4) Save backup codes securely.

Backup codes and recovery
- Shown once; each code can be used one time only.
- Store separately from your 2FA device and never share.
- If you lose your 2FA device/number and have no backups, contact help@telnyx.com for account recovery.

Changing phones or authenticator apps
- Confirm you have valid backup codes first.
- For TOTP: add/transfer the Telnyx entry to the new app before removing the old one.
- For SMS/Call: update the phone number while you still receive codes on the old number, then test sign‑in.

SSO/SAML accounts
- If your organization uses SSO/SAML, MFA may be enforced by your identity provider rather than by Portal 2FA settings.

API access note
- Portal 2FA protects interactive logins only. It does not configure Telnyx Verify and does not replace API key security. Protect API keys separately.

Troubleshooting
- Authenticator code not working: Use the correct account entry; TOTP codes expire quickly; ensure device time is accurate (automatic time recommended); use a backup code if needed.
- Didn’t receive SMS/Call: Confirm the number can receive messages/calls; wait before retrying to avoid rate limits; consider switching to TOTP if delivery is unreliable.
- Request/login‑attempt limits: If you see “You have exceeded the maximum number of allowed requests/login attempts”, wait before trying again. For urgent access, contact help@telnyx.com.


## API authentication: API v2 keys and legacy API v1 tokens
Telnyx authenticates API requests with either an API v2 key (recommended) or an API v1 token (legacy endpoints only).

API v2 keys (recommended)
- Create: Portal → Account icon → Account Settings → API Keys → Create API Key.
- Use: Send as Bearer token in Authorization header.
- Visibility: The key is shown only once at creation. Store securely (environment variables, secrets vault, password manager). If lost, create a new key.
- Management: You can set an expiration date, temporarily disable a key, and add up to 10 tags per key.

API v1 tokens (legacy)
- Intended for legacy services (e.g., some reporting/debugging). Prefer v2 for new integrations.
- Create: Portal → Account icon → API Keys → API V1 Tokens → Create API Token, name it, and save the token (shown once).
- Use: Include headers x-api-user: your_account_email and x-api-token: your_v1_token in API v1 requests.

Best practices
- Store keys/tokens only in secure secret stores; never embed in source code or share.
- Rotate regularly and remove unused credentials.
- Limit blast radius with key expiration and disablement when appropriate.

Developer references
- API fundamentals and keys: https://developers.telnyx.com/development/api-fundamentals/create-api-keys
- API docs: https://developers.telnyx.com/api


## SSO with SAML: concepts and prerequisites
Telnyx Mission Control supports SAML‑based Single Sign‑On with common identity providers (IdPs) including Okta, OneLogin, Microsoft Azure AD (Entra ID), Auth0, LastPass, and Google Workspace (GSuite).

Prerequisites
- A Mission Control Portal Organization (Portal → Organization/Advanced features → Organizations).
- Access to your IdP with permission to create/configure SAML applications.
- TLS recommended for your environment.

Key terms used during setup
- IdP Metadata URL (or manual fields: Entity ID, SSO URL, certificate fingerprint)
- SP (Telnyx) values generated by Portal: Assertion Consumer Service (ACS) URL, Service Provider Entity ID, and Name Identifier Format
- Short Name: An identifier you choose in Portal; it becomes part of SSO URLs such as https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME


## Configure SSO in Mission Control Portal
1) Create or open your Organization in the Portal.
2) Go to Advanced features → Single Sign‑On and click Enable Single Sign‑On (to open configuration; you will enable it fully later).
3) Enter an Authentication Provider Name and Short Name (Short Name is embedded in SSO URLs).
4) Provide IdP settings:
   - If your IdP supports metadata, paste the IdP Metadata URL and import.
   - If not, choose manual configuration and enter: IdP Entity ID, IdP SSO Target URL, and IdP Certificate Fingerprint (algorithm: sha256 when applicable).
5) Save. The page will display the generated SP configuration: ACS URL, Service Provider Entity ID, and (where applicable) Name Identifier Format. You’ll use these in your IdP.

Notes by provider
- Okta: After importing metadata, IdP Entity ID may appear as “not found.” Extract the <okta-idp-id> from your metadata URL and enter it manually.
- Azure AD (Entra ID): Use the App Federation Metadata URL to import. Then set IdP Certificate Fingerprint to the Thumbprint shown in Azure.
