---
source_url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
scraped: 2026-06-11
---

OneLogin: SAML Identity Setup | Telnyx Help Center

[Skip to main content](#main-content)

# OneLogin: SAML Identity Setup

This article will outline how to use OneLogin with Telnyx to facilitate Singe Sign-On capabilities.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_38772a9ead)

[The OneLogin platform](https://www.onelogin.com/) is an identity management system that uses single sign-on (SSO) and a cloud directory to enable organizations to manage user access to on-premises and cloud applications. It offers such identity management solutions as [Smart Factor Authentication](https://www.onelogin.com/solutions/eliminate-passwords), [Single sign-on (SSO) features](https://www.onelogin.com/solutions/identity-chaos), and [Identity Access Management (IAM) for your workforce](https://www.onelogin.com/solutions/workforce-iam).

In this article we will outline setting up Onelogin as a SAML Identity Provider so that we can utilize Telnyx's Single Sign-On feature.

Additional resources:

* [OneLogin developer portal](https://developers.onelogin.com/)
* [OneLogin's SAML quickstart guide](https://developers.onelogin.com/quickstart/saml)
* [OneLogin videos](https://www.onelogin.com/resource-center#f:language=%5BEnglish%5D)

---

# Instructions for setting up OneLogin with Telnyx

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

   [![OneLogin Applications interface. ](https://downloads.intercomcdn.com/i/o/347369311/abe683dc0cf363951e5f1433/image.png?expires=1781168400&signature=838fa08ea32714e3bc22cf3751e34224acf1871e75d3e4bf273454ef1a19af9b&req=dyQgFc93noBeFb4f3HP0gIyE0bsPrwAyjWWr%2FWBeEzGVJaJnZ%2B4buToT2Kcv%0ARL4%3D%0A)](https://downloads.intercomcdn.com/i/o/347369311/abe683dc0cf363951e5f1433/image.png?expires=1781168400&signature=838fa08ea32714e3bc22cf3751e34224acf1871e75d3e4bf273454ef1a19af9b&req=dyQgFc93noBeFb4f3HP0gIyE0bsPrwAyjWWr%2FWBeEzGVJaJnZ%2B4buToT2Kcv%0ARL4%3D%0A)
4. On the Find Applications page, search for *SAML test* and select the **SAML Test Connector (Advanced)** option.

   [![Application selector on OneLogin. ](https://downloads.intercomcdn.com/i/o/347369632/46c49b40cbb3dae604282da2/image.png?expires=1781168400&signature=57e8b7c9edd2f9e2ac6ca17e4b1e4029e7e187ec0c2d2b6a5836770828298c64&req=dyQgFc93m4JdFb4f3HP0gJxuyeRW4IbunFa12GP6EB32eH8G9Lx6I%2FrF98fV%0Ao18%3D%0A)](https://downloads.intercomcdn.com/i/o/347369632/46c49b40cbb3dae604282da2/image.png?expires=1781168400&signature=57e8b7c9edd2f9e2ac6ca17e4b1e4029e7e187ec0c2d2b6a5836770828298c64&req=dyQgFc93m4JdFb4f3HP0gJxuyeRW4IbunFa12GP6EB32eH8G9Lx6I%2FrF98fV%0Ao18%3D%0A)
5. On the following page, enter your desired **Display Name**.

   [![SAML Test Connector administration portal. ](https://downloads.intercomcdn.com/i/o/347370367/f844e611bc52237383c9f941/image.png?expires=1781168400&signature=6ada737f8fbe1c7665334b988160039cc49736a1bd743ed92b7754a4420b33dc&req=dyQgFc5%2BnodYFb4f3HP0gOegmzlesGblbTsvqyWmDosXJR86qtX1EoX6nj66%0AaoY%3D%0A)](https://downloads.intercomcdn.com/i/o/347370367/f844e611bc52237383c9f941/image.png?expires=1781168400&signature=6ada737f8fbe1c7665334b988160039cc49736a1bd743ed92b7754a4420b33dc&req=dyQgFc5%2BnodYFb4f3HP0gOegmzlesGblbTsvqyWmDosXJR86qtX1EoX6nj66%0AaoY%3D%0A)
6. Click the blue **Save** button in the top right corner.
7. After you have saved your changes, click the **SSO** tab from the left-hand side menu.

   [![The SSO tab. ](https://downloads.intercomcdn.com/i/o/347373873/3c8e672b0d557ad5b8744b60/image.png?expires=1781168400&signature=c71003da6f803329db34232a71f385c3f90d1315f897f9fe83de732685a89e69&req=dyQgFc59lYZcFb4f3HP0gGzNaz%2FvVCs%2BYjSiE%2BHxf1aVF3HkV5jo4tdVBc3l%0AKRU%3D%0A)](https://downloads.intercomcdn.com/i/o/347373873/3c8e672b0d557ad5b8744b60/image.png?expires=1781168400&signature=c71003da6f803329db34232a71f385c3f90d1315f897f9fe83de732685a89e69&req=dyQgFc59lYZcFb4f3HP0gGzNaz%2FvVCs%2BYjSiE%2BHxf1aVF3HkV5jo4tdVBc3l%0AKRU%3D%0A)
8. From the SSO page, copy the **Issuer URL** link. This link should resemble the following example: *<https://app.onelogin.com/saml/metadata/<onelogin-idp-id>>*

   [![A screenshot of the SSO tab with a highlighted issuer link. ](https://downloads.intercomcdn.com/i/o/347373608/0e1ae00b804b8e044dcc5ebf/image.png?expires=1781168400&signature=e734a7d31ff63edd1b6152aa931b71599bba9bc0edf08dea1a09f898c85bc037&req=dyQgFc59m4FXFb4f3HP0gIep%2FEmD6UGX%2FCdhXy5KrpKmPBmruPKbkNKlPXVQ%0APgA%3D%0A)](https://downloads.intercomcdn.com/i/o/347373608/0e1ae00b804b8e044dcc5ebf/image.png?expires=1781168400&signature=e734a7d31ff63edd1b6152aa931b71599bba9bc0edf08dea1a09f898c85bc037&req=dyQgFc59m4FXFb4f3HP0gIep%2FEmD6UGX%2FCdhXy5KrpKmPBmruPKbkNKlPXVQ%0APgA%3D%0A)

[Back to Top](#h_38772a9ead)

## 2. Obtain Organization configuration details from Telnyx

In this section, you'll log into your Telnyx portal and get the necessary configuration details to finish setting up your OneLogin SSO app.

1. Log into your Telnyx Mission Control Portal.
2. If you did not complete this step as part of your [pre-requisite activities](#h_3ec72f94d7), navigate to your [Organization](https://portal.telnyx.com/#/app/advanced-features/organizations) section of the Telnyx Mission Control Portal to create an Organization.
3. Once created, navigate to the [Single Sign-On](https://portal.telnyx.com/#/app/advanced-features/managed-accounts) section of the portal and click the green **Enable Single Sign-On** button.

   [![Singe Sign-On section of the Telnyx Mission Control Portal](https://downloads.intercomcdn.com/i/o/347377514/2d5412065ef7569c4a6bac81/image.png?expires=1781168400&signature=9cdcecb71b2a2b7f2d0428ff971b3ee510d23ddbd778e96f100a9338508849e8&req=dyQgFc55mIBbFb4f3HP0gPa%2FZJDspy0WpPMUN14Wz%2BC6k7jvdi1wqJnQruXR%0A9Vs%3D%0A)](https://downloads.intercomcdn.com/i/o/347377514/2d5412065ef7569c4a6bac81/image.png?expires=1781168400&signature=9cdcecb71b2a2b7f2d0428ff971b3ee510d23ddbd778e96f100a9338508849e8&req=dyQgFc55mIBbFb4f3HP0gPa%2FZJDspy0WpPMUN14Wz%2BC6k7jvdi1wqJnQruXR%0A9Vs%3D%0A)
4. You will be presented with the following fields:

   1. **Authentication Provider name** and **Short Name:** Enter the values that make sense for you here.  
      ​  
      ​***Please note*** *that the Short Name will be part of the SSO URLs.*  
      ​
   2. **IdP Metadata URL:** Paste the Identity Provider Entity ID you obtained in step 9 of [section 1](#h_2ef052f2bf).

      [![Single Sign-On details including Authentication provider name and short name details](https://downloads.intercomcdn.com/i/o/347386215/2c8f9dbfecc5def4cc7d190b/image.png?expires=1781168400&signature=d6bbfcac0d03a91ac3ffb4c8598cca0d45c78991c4222412c734dbcf3c451ec6&req=dyQgFcF4n4BaFb4f3HP0gNtd%2BMxhWhZCcNBb%2Feh6P0QqRYlJSCJ9E5icDG63%0Awuc%3D%0A)](https://downloads.intercomcdn.com/i/o/347386215/2c8f9dbfecc5def4cc7d190b/image.png?expires=1781168400&signature=d6bbfcac0d03a91ac3ffb4c8598cca0d45c78991c4222412c734dbcf3c451ec6&req=dyQgFcF4n4BaFb4f3HP0gNtd%2BMxhWhZCcNBb%2Feh6P0QqRYlJSCJ9E5icDG63%0Awuc%3D%0A)
5. Click **Import IdP Settings & Save.**
6. Once settings have been saved, you'll be shown all of the authentication provider settings which will be filled in automatically.

   [![IdP settings and save page. ](https://downloads.intercomcdn.com/i/o/347388974/acfc69b841d99cce04c5fd1e/image.png?expires=1781168400&signature=52130598f893becc0310a5a8e019781a2e01d13a5df5a2e0eeb8dfa1d64b3fc4&req=dyQgFcF2lIZbFb4f3HP0gLDliJ%2FIGHSh7QE0Eel3yVNQ0l6Ox%2FYMeElPs%2FiT%0AFjA%3D%0A)](https://downloads.intercomcdn.com/i/o/347388974/acfc69b841d99cce04c5fd1e/image.png?expires=1781168400&signature=52130598f893becc0310a5a8e019781a2e01d13a5df5a2e0eeb8dfa1d64b3fc4&req=dyQgFcF2lIZbFb4f3HP0gLDliJ%2FIGHSh7QE0Eel3yVNQ0l6Ox%2FYMeElPs%2FiT%0AFjA%3D%0A)
7. Scroll down to the **Authentication Provider Generated Config** section and take note of the values for the following, as you'll need them soon:

   1. **Assertion Consumer Service URL**
   2. **Service Provider Entity ID**

      [![Authentication provider page. ](https://downloads.intercomcdn.com/i/o/347390314/18defcac1099e3ec1ca4b6ff/image.png?expires=1781168400&signature=245089742d1337dcd7cd6ac1d58063577792099903058f6e7a46a59e3bf9360d&req=dyQgFcB%2BnoBbFb4f3HP0gAOPTHphi8puvppjepj%2Be8%2BFQDidTHniCKpZtFLK%0ADhE%3D%0A)](https://downloads.intercomcdn.com/i/o/347390314/18defcac1099e3ec1ca4b6ff/image.png?expires=1781168400&signature=245089742d1337dcd7cd6ac1d58063577792099903058f6e7a46a59e3bf9360d&req=dyQgFcB%2BnoBbFb4f3HP0gAOPTHphi8puvppjepj%2Be8%2BFQDidTHniCKpZtFLK%0ADhE%3D%0A)

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

      [![SAML Test Connector (Advanced). ](https://downloads.intercomcdn.com/i/o/351482755/d20a2464696f7f933bfd932f/image.png?expires=1781168400&signature=0be64a2f7abf8a42b04db3d8664639e7100ccb05ffea909c379401235c7b0b36&req=dyUmEsF8moRaFb4f3HP0gIDXhh7yhrLpkV3D3NaHaU1xMX8BuayDZ7FtAT49%0APRs%3D%0A)](https://downloads.intercomcdn.com/i/o/351482755/d20a2464696f7f933bfd932f/image.png?expires=1781168400&signature=0be64a2f7abf8a42b04db3d8664639e7100ccb05ffea909c379401235c7b0b36&req=dyUmEsF8moRaFb4f3HP0gIDXhh7yhrLpkV3D3NaHaU1xMX8BuayDZ7FtAT49%0APRs%3D%0A)

      [![OneLogin configuration page. ](https://downloads.intercomcdn.com/i/o/347397551/5f398b7638c57bbcf5bec6d0/image.png?expires=1781168400&signature=59b4aaaf656c797ba08fbcc4de9c58d8b5acd5dd08ca982779169cf0e253657b&req=dyQgFcB5mIReFb4f3HP0gNKBHGQBranCmCFFK%2Bo1G4pMKXT3GjGAVhA4O6de%0ASVs%3D%0A)](https://downloads.intercomcdn.com/i/o/347397551/5f398b7638c57bbcf5bec6d0/image.png?expires=1781168400&signature=59b4aaaf656c797ba08fbcc4de9c58d8b5acd5dd08ca982779169cf0e253657b&req=dyQgFcB5mIReFb4f3HP0gNKBHGQBranCmCFFK%2Bo1G4pMKXT3GjGAVhA4O6de%0ASVs%3D%0A)

      [![SAML Test connector section.](https://downloads.intercomcdn.com/i/o/347397783/8d7c65efb5eb518b00e97cf5/image.png?expires=1781168400&signature=4d81159036cc27de384f6b71578df0aab73c76aa154e011db99113398888734c&req=dyQgFcB5molcFb4f3HP0gO3qw7qKh3SQOvCUHZy9qjZqx4DasqvYGils2NA4%0Ap3w%3D%0A)](https://downloads.intercomcdn.com/i/o/347397783/8d7c65efb5eb518b00e97cf5/image.png?expires=1781168400&signature=4d81159036cc27de384f6b71578df0aab73c76aa154e011db99113398888734c&req=dyQgFcB5molcFb4f3HP0gO3qw7qKh3SQOvCUHZy9qjZqx4DasqvYGils2NA4%0Ap3w%3D%0A)

      ​
3. Once all of your configuration settings have been entered successfully, click the blue **Save** button in the top right-hand corner of the page.
4. Once you are ready to enable the configs, return to your Telnyx Mission Control Portal and select **Enable Single Sign-On**.

   [![Single sign-on button. ](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)
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

Table of contents
