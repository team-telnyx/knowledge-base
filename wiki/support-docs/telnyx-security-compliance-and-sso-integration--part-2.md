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

*Part 2 of 4 — see also: [Part 1](telnyx-security-compliance-and-sso-integration--part-1.md), [Part 3](telnyx-security-compliance-and-sso-integration--part-3.md), [Part 4](telnyx-security-compliance-and-sso-integration--part-4.md)*

This page consolidates Telnyx's security, compliance, and identity management documentation. It covers Telnyx's SOC 2 Type I, SOC 2 Type II, and SOC 3 certifications, the security practices validated by these audits, and how to request reports via the Trust Center. It also provides step-by-step instructions for configuring SAML-based Single Sign-On with the Telnyx Mission Control Portal using OneLogin, Okta, LastPass, Microsoft Azure AD, Auth0, and GSuite.

## OneLogin SAML Identity Setup

[OneLogin](https://www.onelogin.com/) is an identity management system that uses single sign-on (SSO) and a cloud directory to manage user access to on-premises and cloud applications.

### Create an SSO App on OneLogin

1. Log into your [OneLogin admin panel](https://telnyxtest.onelogin.com/login2/).
2. From the top navigation, click the **Applications** drop-down and select **Applications**.
3. Click the blue **Add App** button in the top right corner.

   ![OneLogin Applications interface.](_images/40770c30e40c5abd.png)
4. On the Find Applications page, search for *SAML test* and select the **SAML Test Connector (Advanced)** option.

   ![Application selector on OneLogin.](_images/0b86512fdc61ba3f.png)
5. Enter your desired **Display Name**.

   ![SAML Test Connector administration portal.](_images/359a531f62155cda.png)
6. Click **Save**.
7. Click the **SSO** tab from the left-hand side menu.

   ![The SSO tab.](_images/b80b4a76941c95a1.png)
8. From the SSO page, copy the **Issuer URL** link. It should resemble: `https://app.onelogin.com/saml/metadata/<onelogin-idp-id>`.

   ![A screenshot of the SSO tab with a highlighted issuer link.](_images/e92dee2c89448c7c.png)

### Configure Telnyx with OneLogin

1. Log into your Telnyx Mission Control Portal.
2. Navigate to the **Single Sign-On** section and click **Enable Single Sign-On**.

   ![Single Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
3. Enter an **Authentication Provider name** and **Short Name** (the Short Name will be part of the SSO URLs).
4. Paste the **IdP Metadata URL** (the Issuer URL from OneLogin).

   ![Single Sign-On details including Authentication provider name and short name details](_images/5667381e10f6dc6b.png)
5. Click **Import IdP Settings & Save**.
6. Note the **Assertion Consumer Service URL** and **Service Provider Entity ID** from the **Authentication Provider Generated Config** section.

   ![Authentication provider page.](_images/16507273ea29aea1.png)

### Complete OneLogin Configuration

1. Return to your OneLogin admin portal and click **Configuration** in the left-hand menu.
2. Fill in the following fields:
   - **Audience (Entity ID)**: Service Provider Entity ID from Telnyx.
   - **Recipient**: Assertion Consumer Service URL from Telnyx.
   - **ACS (Consumer) URL\***: Assertion Consumer Service URL from Telnyx.
   - **ACS (Consumer) URL Validator\***: `https:\/\/api\.telnyx\.com\/sso\/saml\/auth\/telnyxtest`
   - **Login URL**: `https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME`
   - **SAML nameID format**: Select *Email*.

   ![SAML Test Connector (Advanced).](_images/a13da014027fc62a.png)

   ![OneLogin configuration page.](_images/9268e21bd4f62181.png)

   ![SAML Test connector section.](_images/fb448cd641129548.png)
3. Click **Save**.
4. In the Telnyx Mission Control Portal, select **Enable Single Sign-On** and click **Save Changes**.

   ![Single sign-on button.](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of OneLogin's features at [status.onelogin.com](https://www.onelogin.com/status).

## Okta SAML Identity Setup

[Okta](https://www.okta.com/) is an identity management system that uses single sign-on (SSO) and a cloud directory to help companies manage and secure user authentication into applications.

### Create an SSO App on Okta

1. Log into your Okta Admin panel.
2. Click **Applications** in the left-hand navigation and click **Browse App Catalog**.

   ![The Applications section of the Okta admin panel.](_images/10ada4a2b4653eaa.png)
3. Search for *SAML* and choose **SAML Service Provider**.

   ![unnamed image](_images/1eb950b7df87b4cc.png)
4. Click **Add**.

   ![The blue Add button in for Okta.](_images/7acf630c4a1de654.png)
5. Change the **Application Label** to your desired name.

   ![General SAML Service Provider settings.](_images/e11b94797d3023b2.png)
6. Click **Next**.
7. On the **Sign-On Options** page, select **SAML 2.0**.
8. Set the **Default Relay State** to `https://portal.telnyx.com`.
9. Click **View Setup Instructions** and retrieve your **Identity Provider Entity Id**. The link should resemble: `https://<okta-org>.okta.com/app/<okta-idp-id>/sso/saml/metadata`.

   ![unnamed image](_images/b99e9a197ce71fd2.png)

### Configure Telnyx with Okta

1. Log into your Telnyx Mission Control Portal.
2. Navigate to **Single Sign-On** and click **Enable Single Sign-On**.

   ![Single Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
3. Enter an **Authentication Provider name** and **Short Name**.
4. Paste the **IdP Metadata URL** (the Identity Provider Entity ID from Okta).
5. Click **Import IdP Settings & Save**. **NOTE:** After saving, the *IdP Entity ID* field may show "not found"; extract the `<okta-idp-id>` from the IdP Metadata URL and paste it into this field manually.

   ![Single sign-on section.](_images/55d52616f51494a3.png)
6. Click **Save Changes**.
7. Note the **Assertion Consumer Service URL** and **Service Provider Entity ID** from the **Authentication Provider Generated Config** section.

   ![Authentication Provider Generated Config section.](_images/62e52cf65ebdf2bc.png)

### Complete Okta Configuration

1. Return to your Okta Admin page and fill in the **Advanced Sign-On** settings and **Credential** details using the values from Telnyx.
2. In the **Application username format** field, select *Email*.

   ![Advanced Sign-On settings page.](_images/aa11ed36e994d967.png)
3. Click **Save**.
4. In the Telnyx Mission Control Portal, select **Enable Single Sign-On** and click **Save Changes**.

   ![Single sign-on enablement page.](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of Okta's features at [status.okta.com](https://status.okta.com/).
