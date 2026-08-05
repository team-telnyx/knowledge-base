---
title: Telnyx Compliance and SSO Identity Provider Setup
summary: This page consolidates Telnyx guidance on HIPAA, Business Associate Agreements,
  and the conduit exception, alongside step-by-step instructions for configuring SAML-based
  Single Sign-On with OneLogin, Okta, LastPass, Azure AD, Auth0, and GSuite.
sources:
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
updated_at: 2026-08-05T13:35:57Z
---

# Telnyx Compliance and SSO Identity Provider Setup

*Part 1 of 4 — see also: [Part 2](telnyx-compliance-and-sso-identity-provider-setup--part-2.md), [Part 3](telnyx-compliance-and-sso-identity-provider-setup--part-3.md), [Part 4](telnyx-compliance-and-sso-identity-provider-setup--part-4.md)*

This page consolidates Telnyx guidance on HIPAA, Business Associate Agreements, and the conduit exception, alongside step-by-step instructions for configuring SAML-based Single Sign-On with OneLogin, Okta, LastPass, Azure AD, Auth0, and GSuite.

## HIPAA, BAAs and the Conduit Exception

The Health Insurance Portability & Accountability Act (HIPAA) governs the confidentiality and security of personal health information (PHI) within the United States for "covered entities" and their "business associates." HIPAA requires covered entities — such as healthcare providers, hospital systems, and pharmacies — to implement policies and procedures to ensure the protection of this highly sensitive information. The HIPAA rules generally require a covered entity to enter into a Business Associate Agreement (BAA) with certain third-party vendors who access, receive, transmit, or store PHI (also known as business associates). Whether or not a third-party vendor should fall within the definition of a "business associate" and be required to sign a BAA is very fact specific.

Some third-party vendors fall within the HIPAA "conduit exception" and are therefore not required to enter into a BAA. Telecommunications companies often fall within this conduit exception. A BAA is not needed for an individual or organization that "acts merely as a conduit for protected health information, for example, the US Postal Service, certain private couriers, and their electronic equivalents." Temporarily storing PHI incident to a transmission does not disqualify such an individual or organization from the conduit exception. See [Department of Health and Human Services, 78 FR 5571-72](https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf).

In general, Telnyx's services fall within this conduit exception under HIPAA, and therefore there is no need for Telnyx to sign a BAA. However, Telnyx is always happy to further discuss. If you have any additional questions, please reach out to [sales@telnyx.com](mailto:Sales@telnyx.com).

*This is not, and is not a substitute for obtaining, legal advice.*

## SSO Prerequisites and Common Workflow

Telnyx supports SAML-based Single Sign-On (SSO) for the Mission Control Portal across multiple identity providers. Before configuring any provider, complete the following prerequisites:

- Ensure that your [Telnyx Mission Control Portal](get-started-with-a-mission-control-account.md) is configured properly.
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
- Create an Organization in the [Organization](https://portal.telnyx.com/#/app/advanced-features/organizations) section of the Telnyx Mission Control Portal and record the **Assertion Consumer Service URL**.

Most providers follow a common workflow:

1. Create an SSO application in the identity provider and capture its IdP metadata (URL, Entity ID, certificate fingerprint, or SSO target URL).
2. In the Telnyx Mission Control Portal, navigate to the [Single Sign-On](https://portal.telnyx.com/#/app/advanced-features/managed-accounts) section and click **Enable Single Sign-On**. Provide an **Authentication Provider name**, **Short Name** (used in SSO URLs), and the IdP metadata. Click **Import IdP Settings & Save**.
3. Copy the generated **Assertion Consumer Service URL** and **Service Provider Entity ID** from the **Authentication Provider Generated Config** section.
4. Return to the identity provider and paste those values into the corresponding fields.
5. Back in the Telnyx portal, check **Enable Single Sign-On** and click **Save Changes**.

After enabling SSO, all users in the organization receive an email informing them that SSO is now enabled. Users can still log in with username/password for 72 hours; after that, SSO is required.

## OneLogin SAML Identity Setup

[OneLogin](https://www.onelogin.com/) is an identity management system that uses single sign-on (SSO) and a cloud directory to enable organizations to manage user access to on-premises and cloud applications.

### Create an SSO app on OneLogin

1. Log into your [OneLogin admin panel](https://telnyxtest.onelogin.com/login2/).
2. From the top navigation, click the **Applications** drop-down and select **Applications**.
3. Click the blue **Add App** button in the top right corner.

   ![OneLogin Applications interface.](_images/40770c30e40c5abd.png)
4. On the Find Applications page, search for *SAML test* and select the **SAML Test Connector (Advanced)** option.

   ![Application selector on OneLogin.](_images/0b86512fdc61ba3f.png)
5. Enter your desired **Display Name**.

   ![SAML Test Connector administration portal.](_images/359a531f62155cda.png)
6. Click **Save**, then click the **SSO** tab from the left-hand side menu.

   ![The SSO tab.](_images/b80b4a76941c95a1.png)
7. From the SSO page, copy the **Issuer URL**. It should resemble `https://app.onelogin.com/saml/metadata/<onelogin-idp-id>`.

   ![A screenshot of the SSO tab with a highlighted issuer link.](_images/e92dee2c89448c7c.png)

### Configure Telnyx and complete the OneLogin setup

1. In the Telnyx Mission Control Portal, navigate to the [Single Sign-On](https://portal.telnyx.com/#/app/advanced-features/managed-accounts) section and click **Enable Single Sign-On**.

   ![Singe Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
2. Enter an **Authentication Provider name** and **Short Name**, then paste the **IdP Metadata URL** (the Issuer URL from OneLogin).

   ![Single Sign-On details including Authentication provider name and short name details](_images/5667381e10f6dc6b.png)
3. Click **Import IdP Settings & Save**. The authentication provider settings will be filled in automatically.

   ![IdP settings and save page.](_images/140de6dbfee4c4b7.png)
4. From the **Authentication Provider Generated Config** section, copy the **Assertion Consumer Service URL** and **Service Provider Entity ID**.

   ![Authentication provider page.](_images/16507273ea29aea1.png)
5. In OneLogin, open the **Configuration** link in the left-hand menu and fill in:
   - **Audience (Entity ID):** Service Provider Entity ID from Telnyx.
   - **Recipient:** Assertion Consumer Service URL from Telnyx.
   - **ACS (Consumer) URL:** Assertion Consumer Service URL from Telnyx.
   - **ACS (Consumer) URL Validator:** `https:\/\/api\.telnyx\.com\/sso\/saml\/auth\/telnyxtest`
   - **Login URL:** `https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME`
   - **SAML nameID format:** *Email*

   ![SAML Test Connector (Advanced).](_images/a13da014027fc62a.png)

   ![OneLogin configuration page.](_images/9268e21bd4f62181.png)

   ![SAML Test connector section.](_images/fb448cd641129548.png)
6. Click **Save**, then return to the Telnyx Mission Control Portal and select **Enable Single Sign-On**.

   ![Single sign-on button.](_images/a521794ca2f3529a.png)
7. Click **Save Changes**.

If you experience technical difficulties, check the status of OneLogin's features at [https://www.onelogin.com/status](https://www.onelogin.com/status).

Additional resources: [OneLogin developer portal](https://developers.onelogin.com/), [OneLogin's SAML quickstart guide](https://developers.onelogin.com/quickstart/saml), [OneLogin videos](https://www.onelogin.com/resource-center#f:language=%5BEnglish%5D).
