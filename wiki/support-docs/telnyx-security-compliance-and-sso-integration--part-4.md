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

*Part 4 of 4 — see also: [Part 1](telnyx-security-compliance-and-sso-integration--part-1.md), [Part 2](telnyx-security-compliance-and-sso-integration--part-2.md), [Part 3](telnyx-security-compliance-and-sso-integration--part-3.md)*

This page consolidates Telnyx's security, compliance, and identity management documentation. It covers Telnyx's SOC 2 Type I, SOC 2 Type II, and SOC 3 certifications, the security practices validated by these audits, and how to request reports via the Trust Center. It also provides step-by-step instructions for configuring SAML-based Single Sign-On with the Telnyx Mission Control Portal using OneLogin, Okta, LastPass, Microsoft Azure AD, Auth0, and GSuite.

## Auth0 SSO Integration

[Auth0](https://auth0.com/) is a flexible, drop-in SaaS solution to add authentication and authorization services to your applications.

### Create the Web Application in Auth0

1. Log into your Auth0 admin dashboard.
2. In the left-hand navigation, click **Applications**, then **Applications** in the submenu. Click the purple **+ Create Application** button.

   ![Auth0 Admin dashboard.](_images/5a5f8c7a3ad1f486.png)
3. Enter the desired name and select **Regular Web Applications**.

   ![Auth0 Admin dashboard application page.](_images/73dc90e6dff253d9.png)
4. Click **Create**.
5. Scroll to the bottom of the **Settings** tab and click **Advanced Settings**.
6. Select the **Certificates** tab and click **Download Certificates**, choosing **PEM** format. Save the `YOUR_TENANT.pem` file.
7. Select the **Endpoints** tab and copy the **SAML Protocol URL**.

   ![Auth0 Authorization page.](_images/6d30686bab2e7c48.png)
8. Select the **Addons** tab and enable the **SAML2 Web App** toggle.

   ![Telnyx SSO Test page.](_images/2baff368d5c84b4a.png)
9. On the **Settings** tab, enter the **Application Callback URL** (the Assertion Consumer Service URL).

   ![Addon: SAML 2 Web App interface.](_images/ff3d34f8cab35a46.png)
10. Click **Enable**.

### Configure SAML SSO for Telnyx

1. Go to the SAML Addon **Usage** tab and download the **Identity Provider Metadata** file.

   ![Addon: SAML 2 configuration parameters interface.](_images/0e8d3535f6955c99.png)
2. In the Telnyx Mission Control Portal, navigate to **Single Sign-On** and click **Enable Single Sign-On**.

   ![Single Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
3. Enter an **Authentication Provider Name** and **Short Name**.
4. Paste the **IdP Metadata URL**.

   ![Single Sign-on page.](_images/2395e0a1962bd345.png)
5. Click **Import IdP Settings & Save**.
6. Note the **Assertion Consumer Service URL**, **Service Provider Entity ID**, and **Name Identifier Format** from the **Authentication Provider Generated Config** section.

   ![Authentication Provider Generated Config page.](_images/e6279a5f5412b860.png)
7. Return to the Auth0 Admin portal and click the **Settings** tab.
8. Paste the **Assertion Consumer Service URL** into the **Application Callback URL** field.

   ![Application Callback URL page.](_images/7ffa6ddd8656339b.png)
9. In the **Settings** field below, enter a JSON object using the values from Telnyx:

   ```
   {"audience": "https://apidev.telnyx.com/sso/saml/metadata/SHORTNAME", "recipient": "https://apidev.telnyx.com/sso/saml/auth/SHORTNAME", "signResponse": true, "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress", "nameIdentifierProbes": [ "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" ], "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified"}
   ```

   ![WebAPP settings page.](_images/7eadb544fef687ce.png)
10. Click **Enable**.
11. In the Telnyx Mission Control Portal, click **Enable Single Sign-On** and **Save Changes**.

    ![Single Sign on page.](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of Auth0's features at [status.auth0.com](https://status.auth0.com/).

## GSuite SSO Integration

[GSuite](https://workspace.google.com/) is a collection of business, productivity, collaboration, and education software developed and powered by Google.

### Add a SAML App to GSuite

1. Open the Google GSuite admin portal, log in, and click the **Apps** icon.

   ![Google GSuite admin portal](_images/87dbdd25a832d3c5.png)
2. Click the **Web and mobile apps** tile.

   ![Web and mobile apps tile.](_images/98cd5a49b833f9e6.png)
3. On the Web & Mobile apps page, click **Add Apps** and select **Add custom SAML app**.

   ![image.png](_images/3328e87133b6e9eb.png)
4. Enter an app name and click **Continue**.

   ![image.png](_images/c267553b7512791c.png)
5. In step 2 of the Google Identity Provider details page, note the **SSO URL**, **Entity ID**, and **SHA-256 fingerprint**.

   ![image.png](_images/568662e8be1640cc.png)

### Enable SSO for Your Organization

1. In the Telnyx Mission Control Portal, navigate to **Single Sign-On** and click **Enable Single Sign-On**.

   ![Single Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
2. Provide the following information:
   - **Authentication Provider Name** and **Short Name**.
   - Select **Manually enter configuration**.
   - **IdP Certificate Fingerprint**: SHA-256 fingerprint from GSuite.
   - **IdP Certificate Fingerprint Algorithm**: *sha256*.
   - **IdP Entity ID**: Entity ID from GSuite.
   - **IdP SSO Target URL**: SSO URL from GSuite.

   ![image.png](_images/d9d231c94569270f.png)
3. Click **Save Changes**.
4. Note the **Assertion Consumer Service URL**, **Service Provider Entity ID**, and **Name Identifier Format** from the **Authentication Provider Generated Config** section.

   ![Authentication Provider Generated Config section.](_images/e6279a5f5412b860.png)
5. Return to GSuite and click **Continue**.

### Configure Telnyx as the SSO Provider

1. On the **Service Provider Details** page, provide:
   - **ACS URL**: Assertion Consumer Service URL from Telnyx.
   - **Entity ID**: Service Provider Entity ID from Telnyx.
   - **Start URL**: `https://portal.telnyx.com`.
   - **Name ID format**: *EMAIL*.
   - **Name ID**: *Basic Information > Primary email*.

   ![image.png](_images/82dc3a6079968c8d.png)
2. Click **Continue**, then **Finish**.

### Enable SSO on Your Telnyx Account

1. In the Telnyx Mission Control Portal, check **Enable Single-Sign-On** and click **Save Changes**.

   ![Single sign-on section.](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of GSuite's features at the [GSuite status dashboard](https://www.google.com/appsstatus/dashboard/#hl=en&v=status).

## Related Articles

- [What is Telnyx?](what-is-telnyx.md)
- [Intro to Telnyx Edge Router](intro-to-telnyx-edge-router.md)
- [Okta: SAML Identity Setup](okta-saml-identity-setup.md)
- [LastPass: SAML Identity Setup](lastpass-saml-identity-setup.md)
- [Azure AD: SAML Identity Setup](azure-ad-saml-identity-setup.md)
- [Auth0 SSO Integration With Telnyx](auth0-sso-integration-with-telnyx.md)
- [GSuite SSO Integration With Telnyx](gsuite-sso-integration-with-telnyx.md)
