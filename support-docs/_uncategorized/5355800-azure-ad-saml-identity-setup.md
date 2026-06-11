---
source_url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
scraped: 2026-06-11
---

Azure AD: SAML Identity Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Azure AD: SAML Identity Setup

Learn how to set up Microsoft Azure Active Directory SAML to utilize Telnyx Portal Single Sign-on capabilities.

C

Written by Customer Success

Updated over 3 weeks ago

Table of contents

[Jump to Instructions](#h_5862e24a4f)

The [Azure Active Directory (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/#overview) enterprise identity service provides single sign-on and multi-factor authentication to help protect your users from 99.9 percent of cybersecurity attacks.

In this article we will outline setting up Microsoft Azure AD as a SAML Identity Provider so that we can utilize Telnyx's Single Sign-On feature. The Microsoft Azure AD platform is Microsoft's enterprise cloud-based identity and access management (IAM) solution. It is one of the many SAML providers that Telnyx supports for our SSO feature.

Additional resources:

* [Active Directory documentation](https://learn.microsoft.com/en-us/entra/fundamentals/whatis)
* [Microsoft support](https://support.microsoft.com/en-US)

---

# Instructions for configuring Azure Active Directory to work as a SAML Identity Provider for Telnyx

In this activity you will:

1. [Create and configure a SAML toolkit application on Microsoft Azure](#h_c722084032)
2. [Configure some additional settings on the Telnyx side](#h_deef98f57b)
3. [Complete the setup in Azure](#h_464e7183af)
4. [Enable your SSO configuration on Telnyx](#h_0fdc3234e3)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Create an Organization in the [Organization](https://portal.telnyx.com/#/advanced-features/members) section of the Telnyx Mission Control Portal

## 1. Create and configure a SAML toolkit application on Microsoft Azure

In this section, you will create a SAML toolkit application within Azure

1. Log into your [Microsoft Azure Admin Portal](https://portal.azure.com/#home).
2. From the left-had navigation, click on **Microsoft Entra ID.**

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329729459/cae88832ec655f42a188b9c73cdd/Screenshot+2026-04-28+112345.png?expires=1781168400&signature=b43a86bd87e35d9064f2605cc37373335acf7be88f1505aebdf83d2c346c11a2&req=diMlH858lIVaUPMW1HO4zXVtKZtvv5sNl6wrJZ1bzw9GynOrcuLK%2FLLLoLSB%0Ac7yQ%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329729459/cae88832ec655f42a188b9c73cdd/Screenshot+2026-04-28+112345.png?expires=1781168400&signature=b43a86bd87e35d9064f2605cc37373335acf7be88f1505aebdf83d2c346c11a2&req=diMlH858lIVaUPMW1HO4zXVtKZtvv5sNl6wrJZ1bzw9GynOrcuLK%2FLLLoLSB%0Ac7yQ%0A)
3. You will be redirected to the Active Directory page Overview. Click on **Enterprise Applications** in the left-hand navigation.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329733461/5c9804dc661717b2e340582e7bc4/Screenshot+2026-04-28+112449.png?expires=1781168400&signature=e2964b1fb039fed8e97d0596897a0c2f752055f3a9de771cef1ee7ff74910826&req=diMlH859noVZWPMW1HO4zRmyWBFo0%2FpVTvr7DEImamuEKERLiota%2FqWDqhIS%0A30db%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329733461/5c9804dc661717b2e340582e7bc4/Screenshot+2026-04-28+112449.png?expires=1781168400&signature=e2964b1fb039fed8e97d0596897a0c2f752055f3a9de771cef1ee7ff74910826&req=diMlH859noVZWPMW1HO4zRmyWBFo0%2FpVTvr7DEImamuEKERLiota%2FqWDqhIS%0A30db%0A)
4. Click on the **New Application** option in the top left of the following page.
5. On the **Browse Microsoft Entra App Gallery** menu search for **Microsoft Extra SAML toolkit**.
6. Click on the result to create the app.
7. Fill in a name of your choice into the field within the pop-out.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329739144/08e08555a70e4b8e5ad5388daf0f/Screenshot+2026-04-28+112932.png?expires=1781168400&signature=537d659469a84aba99a71fb8bc099667ac6be8aa8bd55f0bcf13c3bea0915496&req=diMlH859lIBbXfMW1HO4zeTsAxqdXovfDLR6VuyUqy67nUnvDWpp05uo3XX9%0AhvUy%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329739144/08e08555a70e4b8e5ad5388daf0f/Screenshot+2026-04-28+112932.png?expires=1781168400&signature=537d659469a84aba99a71fb8bc099667ac6be8aa8bd55f0bcf13c3bea0915496&req=diMlH859lIBbXfMW1HO4zeTsAxqdXovfDLR6VuyUqy67nUnvDWpp05uo3XX9%0AhvUy%0A)
8. Click the blue **Create** button at the bottom of the pop-out.
9. On the new application page, find the **Getting Started** section and click on the **Set up single sign on** card.

   [![Overview of Telnyx Test section.](https://downloads.intercomcdn.com/i/o/353989047/1a56f71dceab0c590f7c1e2f/image.png?expires=1781168400&signature=047c76be38b2672361d47ad2fc90e7cb0e62a0ab8def0ae1e5d17150005ba038&req=dyUkH8F3nYVYFb4f3HP0gHdGlCoFCGUdBFdGWSthP57eVroZ2Ovyzue8eZH%2B%0A608%3D%0A)](https://downloads.intercomcdn.com/i/o/353989047/1a56f71dceab0c590f7c1e2f/image.png?expires=1781168400&signature=047c76be38b2672361d47ad2fc90e7cb0e62a0ab8def0ae1e5d17150005ba038&req=dyUkH8F3nYVYFb4f3HP0gHdGlCoFCGUdBFdGWSthP57eVroZ2Ovyzue8eZH%2B%0A608%3D%0A)
10. You will be presented with various options on the next page, select the **SAML** card to proceed to the configuration section.
11. From here, copy the **App Federation Metadata URL** and the **Thumbprint** from card 3.

    [![SAML-based Sign-on. ](https://downloads.intercomcdn.com/i/o/353990273/0f047007431463d7c03b3139/image.png?expires=1781168400&signature=2c08f363e4201dc4e80a74c5a064755b7924c7efa12e512f604a6fa1a661ae52&req=dyUkH8B%2Bn4ZcFb4f3HP0gCeDaf1yov1ZyZqdapsyDA9dDv%2B0tRWWsZOP9heH%0ACPA%3D%0A)](https://downloads.intercomcdn.com/i/o/353990273/0f047007431463d7c03b3139/image.png?expires=1781168400&signature=2c08f363e4201dc4e80a74c5a064755b7924c7efa12e512f604a6fa1a661ae52&req=dyUkH8B%2Bn4ZcFb4f3HP0gCeDaf1yov1ZyZqdapsyDA9dDv%2B0tRWWsZOP9heH%0ACPA%3D%0A)

[Back to Top](#h_5862e24a4f)

## 2. Configure some additional settings on the Telnyx side

In this section, we will configure Telnyx to use the Active Directory app we created in [section 1](#h_c722084032).

1. If you have not yet created an Organization as part of your [pre-requisite activities](#h_7fefd7ee47), navigate to your [Organization](https://portal.telnyx.com/#/advanced-features/members) section of the Telnyx Mission Control Portal and create an Organization.
2. Once created, navigate to the **[Single Sign-On](https://portal.telnyx.com/#/advanced-features/single-sign-on)** section of the portal and click the green **Enable Single Sign-On** button.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329741416/74a93fe8e6b3ebac3899a8840740/Screenshot+2026-04-28+113032.png?expires=1781168400&signature=55875d117d36c018cbda8d46cce2f11950eb2035f376893eb51d3db9b767aefe&req=diMlH856nIVeX%2FMW1HO4zes1jnuE5xIBTGBGpqGHRn1aMqkJ%2FX3VU%2BEg2P3n%0AjsVx%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329741416/74a93fe8e6b3ebac3899a8840740/Screenshot+2026-04-28+113032.png?expires=1781168400&signature=55875d117d36c018cbda8d46cce2f11950eb2035f376893eb51d3db9b767aefe&req=diMlH856nIVeX%2FMW1HO4zes1jnuE5xIBTGBGpqGHRn1aMqkJ%2FX3VU%2BEg2P3n%0AjsVx%0A)
3. You will be presented with the following fields:

   1. **Authentication Provider Name** and **Short Name**: Provide values that make sense to you. ***Note*** *that the Short Name will be part of the SSO URLs.*
   2. **IdP Metadata URL**: Paste the **App Federation Metadata URL** we copied from the MS Azure Admin in step 11 of [section 1](#h_c722084032).

      [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329742233/afbe5ffa1e94caf77a58ef19c1ec/Screenshot+2026-04-28+113052.png?expires=1781168400&signature=2774aa948f5ca36aa4c38be0eb6c4d07db0a8e448db9ba1f38bab4f9187d8b65&req=diMlH856n4NcWvMW1HO4zYmBcyxz2o3VLPaUdsmOb%2FVe2e4Gc2aV7Bgl99ZQ%0Adj8%2F%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329742233/afbe5ffa1e94caf77a58ef19c1ec/Screenshot+2026-04-28+113052.png?expires=1781168400&signature=2774aa948f5ca36aa4c38be0eb6c4d07db0a8e448db9ba1f38bab4f9187d8b65&req=diMlH856n4NcWvMW1HO4zYmBcyxz2o3VLPaUdsmOb%2FVe2e4Gc2aV7Bgl99ZQ%0Adj8%2F%0A)
4. Click on **Import IdP Settings & Save.**
5. Once saved, your authentication provider settings should automatically fill in with exception of the **IdP Certificate Fingerprint.**

   1. Replace the "not found" within this field with the **Thumbprint** we copied from the Azure Admin portal in step 11 of [section 1](#h_c722084032).

      [![IdP Certificate Fingerprint section. ](https://downloads.intercomcdn.com/i/o/353993823/f499bb073a29bbbf5df9e01a/image.png?expires=1781168400&signature=d84160046a57d5a1c484be24b9d61f7d4ca39b9fc28ce0c29b801393dbda1d96&req=dyUkH8B9lYNcFb4f3HP0gKvoquxj3nRQxPdvqxy8FufWY8LK%2FXnTcKi%2BbVgU%0APfw%3D%0A)](https://downloads.intercomcdn.com/i/o/353993823/f499bb073a29bbbf5df9e01a/image.png?expires=1781168400&signature=d84160046a57d5a1c484be24b9d61f7d4ca39b9fc28ce0c29b801393dbda1d96&req=dyUkH8B9lYNcFb4f3HP0gKvoquxj3nRQxPdvqxy8FufWY8LK%2FXnTcKi%2BbVgU%0APfw%3D%0A)
   2. Click **Save Changes.**
6. After saving, scroll down to the bottom of the page and take note of the values for:

   1. **Assertion Consumer Service URL**
   2. **Service Provider Entity ID**
   3. **Name Identifier Format**.

      [![Authentication provider generated configuration. ](https://downloads.intercomcdn.com/i/o/353994527/31b2f6e717e201352d6e6510/image.png?expires=1781168400&signature=931b26704b456347973a93729f496aef963367da6c0e951346afb557cea933dd&req=dyUkH8B6mINYFb4f3HP0gOHMoZb%2FLBX9VB%2F%2BzVe8FK%2BTUGy9%2FU3mAp1CMn16%0A%2FLs%3D%0A)](https://downloads.intercomcdn.com/i/o/353994527/31b2f6e717e201352d6e6510/image.png?expires=1781168400&signature=931b26704b456347973a93729f496aef963367da6c0e951346afb557cea933dd&req=dyUkH8B6mINYFb4f3HP0gOHMoZb%2FLBX9VB%2F%2BzVe8FK%2BTUGy9%2FU3mAp1CMn16%0A%2FLs%3D%0A)

[Back to Top](#h_5862e24a4f)

## 3. Complete the setup in Azure

Now that you've gotten what you need from the Telnyx side, head back to Azure to complete the setup.

1. Navigate back to the Azure AD portal, and click the **Edit** option in the top right corner of card 1 (**Basic SAML Configuration**).
2. Remove the default value for **Identifier (Entity ID)** (something like *[https://samltookit.azurewebsites.net](https://samltoolkit.azurewebsites.net/)*) by clicking the trash icon.
3. Find the **Identifier (Entity ID)** field. Paste the value generated for **Service Provider Entity ID** that you obtained in step 6 of [section 2](#h_deef98f57b) into this field.
4. Find the **Reply URL (Assertion Consumer Service URL)** field. Paste the value generated for **Assertion Consumer Service URL** that you obtained in step 6 of [section 2](#h_deef98f57b) into this field.
5. Find the **Sign on URL** field. Paste *<https://api.telnyx.com/sso/saml/login/YOUR_SHORT_NAME>* that you obtained in step 3 of [section 2](#h_deef98f57b) into this field.
6. Find the **Relay State** field, fill in the following URL: *<https://portal.telnyx.com/>*

   [![SAML configurations section. ](https://downloads.intercomcdn.com/i/o/353998872/09b99590e2cf48fb32f0b04a/image.png?expires=1781168400&signature=2d86ee0ec36643c3c8c7a067838bb35776552dfd024bdddfea7f963ebe14f0bd&req=dyUkH8B2lYZdFb4f3HP0gCV2YGsidy%2Fw30Rhci%2BOXXOkv7UgdiIyGykintaV%0AWjk%3D%0A)](https://downloads.intercomcdn.com/i/o/353998872/09b99590e2cf48fb32f0b04a/image.png?expires=1781168400&signature=2d86ee0ec36643c3c8c7a067838bb35776552dfd024bdddfea7f963ebe14f0bd&req=dyUkH8B2lYZdFb4f3HP0gCV2YGsidy%2Fw30Rhci%2BOXXOkv7UgdiIyGykintaV%0AWjk%3D%0A)
7. Click **Save** to finalize your configuration settings.

[Back to Top](#h_5862e24a4f)

## 4. Enable your SSO configuration on Telnyx

And now, for the drum roll! Let's enable your SSO configuration and get things up and running!

1. Navigate back to y Telnyx Mission Control Portal and check the **Enable Single Sign-On** box.

   [![Single sign-on changes section. ](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)
2. Click **Save Changes.**

Your chosen settings are now in effect! This will send all users in your organization an email informing them that SSO is now enabled. Your users will still be able to login using username/password for the next 72 hours. After that, they will be required to use SSO.  
​

[Back to Top](#h_5862e24a4f)

---

## Troubleshooting

**Q. I'm experiencing difficulty with this configuration!**

A. If you experience technical difficulties while attempting to set up your MS Azure AD SSO with Telnyx, its possible your provider is experiencing outages/maintenance. You can check the status of Auth0's features at [https://status.azure.com/en-us/status](https://azure.status.microsoft/en-us/status).  
​

[Back to Top](#h_5862e24a4f)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Active Directory documentation](https://learn.microsoft.com/en-us/entra/fundamentals/whatis)
* [Microsoft support](https://support.microsoft.com/en-US)

---

---

Related Articles

[OneLogin: SAML Identity Setup](https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup)[Okta: SAML Identity Setup](https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup)[LastPass: SAML Identity Setup](https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup)[Auth0 SSO Integration With Telnyx](https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx)[GSuite SSO Integration With Telnyx](https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx)

Did this answer your question?

😞😐😃

Table of contents
