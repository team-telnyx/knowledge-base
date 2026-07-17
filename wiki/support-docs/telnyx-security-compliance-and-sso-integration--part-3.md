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

*Part 3 of 4 — see also: [Part 1](telnyx-security-compliance-and-sso-integration--part-1.md), [Part 2](telnyx-security-compliance-and-sso-integration--part-2.md), [Part 4](telnyx-security-compliance-and-sso-integration--part-4.md)*

This page consolidates Telnyx's security, compliance, and identity management documentation. It covers Telnyx's SOC 2 Type I, SOC 2 Type II, and SOC 3 certifications, the security practices validated by these audits, and how to request reports via the Trust Center. It also provides step-by-step instructions for configuring SAML-based Single Sign-On with the Telnyx Mission Control Portal using OneLogin, Okta, LastPass, Microsoft Azure AD, Auth0, and GSuite.

## LastPass SAML Identity Setup

[LastPass](https://www.lastpass.com/) provides a true SSO experience for end users, allowing them to access key apps without entering a unique password.

### Create an SSO App on LastPass

1. Log into your [LastPass admin portal](https://admin.lastpass.com/dashboard).
2. From the left-hand navigation, click **Applications → SSO Apps**.
3. Click **Add your first SSO App**.

   ![LastPass Admin Portal.](_images/6a7eb07f535e108b.png)
4. On the pop-up screen, click **Add unlisted app** and choose a name.
5. On the **Configure App** page, on the **Set up App** tab, click **Expand** and note the **Certificate Fingerprint (SHA256)**, **Entity ID**, and **SSO Endpoint** values.

   ![App setup section in the admin portal.](_images/43333705da12f219.png)

### Configure Telnyx with LastPass

1. Log into your Telnyx Mission Control Portal.
2. Navigate to **Single Sign-On** and click **Enable Single Sign-On**.

   ![](_images/0371203040f712f8.png)
3. Enter an **Authentication Provider name** and **Short Name**.
4. Select **Manually enter configuration**.
5. Provide the following values from LastPass:
   - **IdP Certificate Fingerprint**: Certificate Fingerprint (SHA256) from LastPass.
   - **IdP Certificate Fingerprint Algorithm**: *sha256*.
   - **IdP Entity ID**: Entity ID from LastPass.
   - **IdP SSO Target URL**: SSO Endpoint from LastPass.

   ![](_images/71cb35d1ac5bd8f9.png)
6. Click **Save Changes**.
7. Note the **Assertion Consumer Service URL** and **Service Provider Entity ID** from the **Authentication Provider Generated Config** section.

   ![Authentication Provider Generated Configuration settings](_images/4f908be88a3461aa.png)

### Complete LastPass Configuration

1. Return to the LastPass admin portal, open the **Set up LastPass** tab, and click **Expand**.
2. Click **Advanced Settings** and provide:
   - **ACS**: Assertion Consumer Service URL from Telnyx.
   - **Entity ID**: Service Provider Entity ID from Telnyx.
   - **Identifier**: *Email*.
   - **SAML signature method**: *SHA256*.
   - **Sign Response**: Enable.

   ![LastPass app configuration](_images/cf44f7b59b1a2595.png)

   ![App configuration user assigning settings](_images/8a5848f5c9a6bd0e.png)
3. Click **Save & Assign to users**.
4. Click **Assign users, groups and roles**.

   ![Users, groups and roles section](_images/07922ce733cda7fe.png)
5. Select the appropriate users and click **Assign**.

   ![Users, groups and roles settings](_images/d128af3a2b06702d.png)
6. In the Telnyx Mission Control Portal, click **Enable Single Sign-On** and **Save Changes**.

   ![Enabling single sign on](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of LastPass features at [status.lastpass.com](https://status.lastpass.com/).

## Azure AD SAML Identity Setup

[Azure Active Directory (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/#overview) provides single sign-on and multi-factor authentication to help protect your users from cybersecurity attacks.

### Create and Configure a SAML Toolkit Application on Microsoft Azure

1. Log into your [Microsoft Azure Admin Portal](https://portal.azure.com/#home).
2. From the left-hand navigation, click **Microsoft Entra ID**.

   ![](_images/b765e60cc06fb401.png)
3. On the Active Directory Overview page, click **Enterprise Applications** in the left-hand navigation.

   ![](_images/91646f69c7355a50.png)
4. Click **New Application** in the top left.
5. On the **Browse Microsoft Entra App Gallery** menu, search for **Microsoft Extra SAML toolkit**.
6. Click the result to create the app.
7. Fill in a name of your choice.

   ![](_images/7b7f994021be2667.png)
8. Click **Create**.
9. On the new application page, find the **Getting Started** section and click **Set up single sign on**.

   ![Overview of Telnyx Test section.](_images/fb96b577869ccaa7.png)
10. Select the **SAML** card.
11. Copy the **App Federation Metadata URL** and the **Thumbprint** from card 3.

    ![SAML-based Sign-on.](_images/d3315e43fea0eafd.png)

### Configure Telnyx with Azure AD

1. In the Telnyx Mission Control Portal, navigate to **Single Sign-On** and click **Enable Single Sign-On**.

   ![](_images/d02d06a926680886.png)
2. Enter an **Authentication Provider Name** and **Short Name**.
3. Paste the **App Federation Metadata URL** into the **IdP Metadata URL** field.

   ![](_images/db48b75a4f18ba66.png)
4. Click **Import IdP Settings & Save**.
5. Replace the "not found" value in the **IdP Certificate Fingerprint** field with the **Thumbprint** from Azure.

   ![IdP Certificate Fingerprint section.](_images/13750d2a1a52541c.png)
6. Click **Save Changes**.
7. Note the **Assertion Consumer Service URL**, **Service Provider Entity ID**, and **Name Identifier Format** from the **Authentication Provider Generated Config** section.

   ![Authentication provider generated configuration.](_images/bd0d9086a2a125d8.png)

### Complete the Setup in Azure

1. In the Azure AD portal, click **Edit** in the top right of card 1 (**Basic SAML Configuration**).
2. Remove the default **Identifier (Entity ID)** value.
3. Paste the **Service Provider Entity ID** from Telnyx into the **Identifier (Entity ID)** field.
4. Paste the **Assertion Consumer Service URL** from Telnyx into the **Reply URL (Assertion Consumer Service URL)** field.
5. Paste `https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME` into the **Sign on URL** field.
6. Fill in `https://portal.telnyx.com/` in the **Relay State** field.

   ![SAML configurations section.](_images/2b98299db48c26c6.png)
7. Click **Save**.

### Enable SSO on Telnyx

1. In the Telnyx Mission Control Portal, check **Enable Single Sign-On** and click **Save Changes**.

   ![Single sign-on changes section.](_images/a521794ca2f3529a.png)

If you experience technical difficulties, check the status of Azure features at [azure.status.microsoft](https://azure.status.microsoft/en-us/status).
