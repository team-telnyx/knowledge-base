---
source_url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
title: "OneLogin: SAML Identity Setup"
description: "This article will outline how to use OneLogin with Telnyx to facilitate Singe Sign-On capabilities. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 581471d5f9e535f2368a69687c14af7409bb531ccbe0a71a42b4b04511dc4b0d
---







# OneLogin: SAML Identity Setup

This article will outline how to use OneLogin with Telnyx to facilitate Singe Sign-On capabilities. See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_38772a9ead)

[The OneLogin platform](https://www.onelogin.com/) is an identity management system that uses single sign-on (SSO) and a cloud directory to enable organizations to manage user access to on-premises and cloud applications. It offers such identity management solutions as [Smart Factor Authentication](https://www.onelogin.com/solutions/eliminate-passwords), [Single sign-on (SSO) features](https://www.onelogin.com/solutions/identity-chaos), and [Identity Access Management (IAM) for your workforce](https://www.onelogin.com/solutions/workforce-iam).

In this article we will outline setting up Onelogin as a SAML Identity Provider so that we can utilize Telnyx's Single Sign-On feature.

Additional resources:

* [OneLogin developer portal](https://developers.onelogin.com/)
* [OneLogin's SAML quickstart guide](https://developers.onelogin.com/quickstart/saml)
* [OneLogin videos](https://www.onelogin.com/resource-center#f:language=%5BEnglish%5D)

---

## Instructions for setting up OneLogin with Telnyx

In this activity you will:

1. [Create an SSO app on OneLogin](#h_2ef052f2bf)
2. [Obtain organization configuration details from Telnyx](#h_1d9e34cf91)
3. [Add your Telnyx Organization details to your OneLogin SSO app](#h_d548ae2fac)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Create an Organization in the [Organization](https://portal.telnyx.com/#/app/advanced-features/organizations) section of the Telnyx Mission Control Portal and make sure you record the **Assertion Consumer Service URL**

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for OneLogin/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Create an SSO app on OneLogin

In this section, you will create an SSO app on OneLogin that you'll use to configure SSO authentication through Telnyx.

1. Log into your [OneLogin admin panel](https://telnyxtest.onelogin.com/login2/?return=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmkiOiJodHRwczovL3RlbG55eHRlc3Qub25lbG9naW4uY29tL2FkbWluIiwiaXNzIjoiTU9OT1JBSUwiLCJicmFuZF9pZCI6Im1hc3RlciIsImZmX211bHRpcGxlX2JyYW5kcyI6bnVsbCwiZXhwIjoxNjkzMjM4MzUzLCJwYXJhbXMiOnt9LCJtZXRob2QiOiJnZXQiLCJhdWQiOiJBQ0NFU1MifQ.QOGHEv3GnLfZrA1jOVbpV-vcLR-V0-IBOgp0LQ4tvm8#app=).
2. From the top naviation, click the **Applications** drop-down and select **Applications.**
3. Click on the blue **Add App** button in the top right corner.

   ![OneLogin Applications interface. ](_images/40770c30e40c5abd.png)
4. On the Find Applications page, search for *SAML test* and select the **SAML Test Connector (Advanced)** option.

   ![Application selector on OneLogin. ](_images/0b86512fdc61ba3f.png)
5. On the following page, enter your desired **Display Name**.

   ![SAML Test Connector administration portal. ](_images/359a531f62155cda.png)
6. Click the blue **Save** button in the top right corner.
7. After you have saved your changes, click the **SSO** tab from the left-hand side menu.

   ![The SSO tab. ](_images/b80b4a76941c95a1.png)
8. From the SSO page, copy the **Issuer URL** link. This link should resemble the following example: *<https://app.onelogin.com/saml/metadata/<onelogin-idp-id>>*

   ![A screenshot of the SSO tab with a highlighted issuer link. ](_images/e92dee2c89448c7c.png)

[Back to Top](#h_38772a9ead)

## 2. Obtain Organization configuration details from Telnyx

In this section, you'll log into your Telnyx portal and get the necessary configuration details to finish setting up your OneLogin SSO app.

1. Log into your Telnyx Mission Control Portal.
2. If you did not complete this step as part of your [pre-requisite activities](#h_3ec72f94d7), navigate to your [Organization](https://portal.telnyx.com/#/app/advanced-features/organizations) section of the Telnyx Mission Control Portal to create an Organization.
3. Once created, navigate to the [Single Sign-On](https://portal.telnyx.com/#/app/advanced-features/managed-accounts) section of the portal and click the green **Enable Single Sign-On** button.

   ![Singe Sign-On section of the Telnyx Mission Control Portal](_images/ec3e582b986cf3cf.png)
4. You will be presented with the following fields:

   1. **Authentication Provider name** and **Short Name:** Enter the values that make sense for you here.
      ​
      ​***Please note*** *that the Short Name will be part of the SSO URLs.*
      ​
   2. **IdP Metadata URL:** Paste the Identity Provider Entity ID you obtained in step 9 of [section 1](#h_2ef052f2bf).

      ![Single Sign-On details including Authentication provider name and short name details](_images/5667381e10f6dc6b.png)
5. Click **Import IdP Settings & Save.**
6. Once settings have been saved, you'll be shown all of the authentication provider settings which will be filled in automatically.

   ![IdP settings and save page. ](_images/140de6dbfee4c4b7.png)
7. Scroll down to the **Authentication Provider Generated Config** section and take note of the values for the following, as you'll need them soon:

   1. **Assertion Consumer Service URL**
   2. **Service Provider Entity ID**

      ![Authentication provider page. ](_images/16507273ea29aea1.png)

[Back to Top](#h_38772a9ead)

## 3. Add your Telnyx Organization details to your OneLogin SSO app

In this final section, you'll return to OneLogin and provide the information you obtained from Telnyx in step 7 of [section 2](#h_1d9e34cf91).

1. Return to your OneLogin admin portal.
2. Click on the **Configuration** link in the left-hand menu and fill in the relevant information we just took note of above in the following fields:

   1. **Audience (Entity ID):** Paste the value you obtained from **Service Provider Entity ID** on the Telnyx Mission Control Portal (step 7, [section 2](#h_1d9e34cf91))
   2. **Recipient:** Paste the value you obtained from **Assertion Consumer Service URL** on the Telnyx Mission Control Portal (step 7, [section 2](#h_1d9e34cf91))
   3. **ACS (Consumer) URL\*:** Paste the value you obtained from **Assertion Consumer Service URL** on the Telnyx Mission Control Portal (step 7, [section 2](#h_1d9e34cf91))
   4. **ACS (Consumer) URL Validator\*:** fill in the ACS URL escaped in a regular expression format: *https:\/\/api\.telnyx\.com\/sso\/saml\/auth\/telnyxtest*
   5. **Login URL:** *<https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME>*
   6. **SAML nameID format:** Select *Email*.

      ![SAML Test Connector (Advanced). ](_images/a13da014027fc62a.png)

      ![OneLogin configuration page. ](_images/9268e21bd4f62181.png)

      ![SAML Test connector section.](_images/fb448cd641129548.png)

      ​
3. Once all of your configuration settings have been entered successfully, click the blue **Save** button in the top right-hand corner of the page.
4. Once you are ready to enable the configs, return to your Telnyx Mission Control Portal and select **Enable Single Sign-On**.

   ![Single sign-on button. ](_images/a521794ca2f3529a.png)
5. Click **Save Changes**.

Your chosen settings are now in effect! This will send all users in your organization an email informing them that SSO is now enabled. Your users will still be able to login using username/password for the next 72 hours. After that, they will be required to use SSO.

[Back to Top](#h_38772a9ead)

---

## Troubleshooting

**Q. I'm experiencing difficulty with this configuration!**

A. If you experience technical difficulties while attempting to set up your OneLogin SSO with Telnyx, its possible your provider is experiencing outages/maintenance. You can check the status of OneLogin's features at <https://www.onelogin.com/status>.
​

[Back to Top](#h_38772a9ead)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [OneLogin developer portal](https://developers.onelogin.com/)
* [OneLogin's SAML quickstart guide](https://developers.onelogin.com/quickstart/saml)
* [OneLogin videos](https://www.onelogin.com/resource-center#f:language=%5BEnglish%5D)

---

---

Related Articles

[Okta: SAML Identity Setup](https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup)[LastPass: SAML Identity Setup](https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup)[Azure AD: SAML Identity Setup](https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup)[Auth0 SSO Integration With Telnyx](https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx)[GSuite SSO Integration With Telnyx](https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx)

Did this answer your question?

😞😐😃
