---
source_url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
scraped: 2026-06-11
---

GSuite SSO Integration With Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# GSuite SSO Integration With Telnyx

Learn how to set up Auth0 as a SAML Identity Provider so that we can utilize Telnyx's Single Sign-On feature.

C

Written by Customer Success

Updated over 3 weeks ago

Table of contents

[Jump to Instructions](#h_8bdd96afc4)

[GSuite](https://workspace.google.com/) is a collection of business, productivity, collaboration, and education software developed and powered by Google.It is one of the many SAML providers that Telnyx supports for use with its SSO feature. Now learn how to set up Auth0 as a SAML Identity Provider so that we can utilize Telnyx's Single Sign-On feature.

Additional resources:

* [GSuite FAQ](https://workspace.google.com/faq/)
* [GSuite support](https://workspace.google.com/support/)
* [GSuite troubleshooting](https://workspace.google.com/support/#google-workspace-trouble-shooting)
* [GSuite admin help community](https://support.google.com/a/community?hl=en)
* [GSuite learning center (Documentation)](https://support.google.com/a/users/?hl=en#topic=9917952)

|  |
| --- |
| ***Note:*** *If you experience technical difficulties while attempting to set up your GSuite SSO with Telnyx, its possible your provider is experiencing outages/maintenance. You can always [check the status of GSuite's features](https://www.google.com/appsstatus/dashboard/#hl=en&v=status).* |

---

# Instructions for setting up Google GSuite SAML Identity Provider with Telnyx

In this activity you will:

1. [Add a SAML app to GSuite](#h_0f4cffeea0)
2. [Enable SSO for your organization](#h_fdd6d61754)
3. [Configure Telnyx as your SSO provider](#h_a3a3a03459)
4. [Enable your SSO configuration on your Telnyx account](#h_7da55f3b64)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* (OPTIONAL) You can [configure an Organization in your Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/account/organizations) before beginning. Otherwise, you'll have to do this during this activity.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for GSuite/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Add a SAML app to GSuite

In this activity,

1. Open Google GSuite admin portal, log in, and click on the **Apps** icon as shown below.

   [![Google Gsuite admin portal](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084230/864cdf43244c7fa91217289f/b862a21a-67fd-4c3a-bad4-16c4f3b90054?expires=1781168400&signature=fff7d704a446b106591a66297816435822c405f103961948feebb48c14d2fbfb&req=dyUiFsF6n4JfFb4f3HP0gEUBldry%2BD9je65iIo3pn3chd1BvAu0U6U0r%2FeJQ%0ALA0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084230/864cdf43244c7fa91217289f/b862a21a-67fd-4c3a-bad4-16c4f3b90054?expires=1781168400&signature=fff7d704a446b106591a66297816435822c405f103961948feebb48c14d2fbfb&req=dyUiFsF6n4JfFb4f3HP0gEUBldry%2BD9je65iIo3pn3chd1BvAu0U6U0r%2FeJQ%0ALA0%3D%0A)
2. On the next page click on the **Web and mobile apps** tile.

   [![Web and mobile apps tile.](https://downloads.intercomcdn.com/i/o/359947262/b528c9571a862804aa701508/image.png?expires=1781168400&signature=2e048a981190d69c4d9722f4582e0246061b77f3fdfe6a88d086e7020c8dc539&req=dyUuH815n4ddFb4f3HP0gMOYjRIMIjGyqeVokNhAOQmgNrhwr8AoE8jElZaj%0ATsM%3D%0A)](https://downloads.intercomcdn.com/i/o/359947262/b528c9571a862804aa701508/image.png?expires=1781168400&signature=2e048a981190d69c4d9722f4582e0246061b77f3fdfe6a88d086e7020c8dc539&req=dyUuH815n4ddFb4f3HP0gMOYjRIMIjGyqeVokNhAOQmgNrhwr8AoE8jElZaj%0ATsM%3D%0A)
3. You will be brought to the Web & Mobile apps page where you can click the **Add Apps** drop down menu and select **Add custom SAML app.**

   [![image.png](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084249/85ea481a4c3b8686f3ef250f/16a1ab7a-8018-42ba-b4ba-e8b8a14bcf7c?expires=1781168400&signature=e83df81741dd6f8ddfa673d5ecd9fce5b3c343547c00fb889a9b7bb36f3b5d9d&req=dyUiFsF6n4VWFb4f3HP0gANyVHIb8JMlsp7avWl%2B%2FgKpumCwYjw09Y9QsOml%0AbeI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084249/85ea481a4c3b8686f3ef250f/16a1ab7a-8018-42ba-b4ba-e8b8a14bcf7c?expires=1781168400&signature=e83df81741dd6f8ddfa673d5ecd9fce5b3c343547c00fb889a9b7bb36f3b5d9d&req=dyUiFsF6n4VWFb4f3HP0gANyVHIb8JMlsp7avWl%2B%2FgKpumCwYjw09Y9QsOml%0AbeI%3D%0A)
4. On the next page, fill in an app name of your choice and click **Continue.**

   [![image.png](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084256/98ec3f8e40dd85f636d4efbc/411d326b-def5-428f-8281-4bdf7c184cf4?expires=1781168400&signature=3c0e643e850791b1d1a115872584a907c61a11b2c5a1b694fd7f0a784d5ac807&req=dyUiFsF6n4RZFb4f3HP0gHsD0xART%2FqKs9IGnR%2FK15%2BvId1c7udlqQxKfTT0%0Ata0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084256/98ec3f8e40dd85f636d4efbc/411d326b-def5-428f-8281-4bdf7c184cf4?expires=1781168400&signature=3c0e643e850791b1d1a115872584a907c61a11b2c5a1b694fd7f0a784d5ac807&req=dyUiFsF6n4RZFb4f3HP0gHsD0xART%2FqKs9IGnR%2FK15%2BvId1c7udlqQxKfTT0%0Ata0%3D%0A)
5. In the step 2 section of the Google Identity Provider details page, make note of the values for SSO URL, Entity ID and SHA-256 fingerprint.

   [![image.png](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084262/049078b7fa6c1d90212fe4a4/bb406e46-035a-4baa-8b03-c85e1c590679?expires=1781168400&signature=a5cfdd2d483a2137bc3486c71ee28149dac41c52c31fb9fb9b3395d7cd47f541&req=dyUiFsF6n4ddFb4f3HP0gK6jEeb3MT9Q4MgGeKmFPfkk4eohK4QgOyu8lW7t%0AgwQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084262/049078b7fa6c1d90212fe4a4/bb406e46-035a-4baa-8b03-c85e1c590679?expires=1781168400&signature=a5cfdd2d483a2137bc3486c71ee28149dac41c52c31fb9fb9b3395d7cd47f541&req=dyUiFsF6n4ddFb4f3HP0gK6jEeb3MT9Q4MgGeKmFPfkk4eohK4QgOyu8lW7t%0AgwQ%3D%0A)

[Back to Top](#h_8bdd96afc4)

## 2. Enable SSO for your organization

1. Log into your Telnyx Mission Control Portal and navigate to your [Organization](https://portal.telnyx.com/#/advanced-features/members) section where you will create an Organization if you have not already.
2. Now navigate to the **[Single Sign-On](https://portal.telnyx.com/#/advanced-features/single-sign-on)** section of the portal and click the green **Enable Single Sign-On** button.

   [![Singe Sign-On section of the Telnyx Mission Control Portal](https://downloads.intercomcdn.com/i/o/347377514/2d5412065ef7569c4a6bac81/image.png?expires=1781168400&signature=9cdcecb71b2a2b7f2d0428ff971b3ee510d23ddbd778e96f100a9338508849e8&req=dyQgFc55mIBbFb4f3HP0gPa%2FZJDspy0WpPMUN14Wz%2BC6k7jvdi1wqJnQruXR%0A9Vs%3D%0A)](https://downloads.intercomcdn.com/i/o/347377514/2d5412065ef7569c4a6bac81/image.png?expires=1781168400&signature=9cdcecb71b2a2b7f2d0428ff971b3ee510d23ddbd778e96f100a9338508849e8&req=dyQgFc55mIBbFb4f3HP0gPa%2FZJDspy0WpPMUN14Wz%2BC6k7jvdi1wqJnQruXR%0A9Vs%3D%0A)
3. Provide the following information:

   1. **Authentication Provider Name:** Provide a value of your choice
   2. **Short Name** Provide a value of your choice, but note that the **Short Name** will be part of the SSO URLs.
   3. **Manually enter configuration:** Select this
   4. **IdP Certificate Fingerprint**: Enter the SHA-256 fingerprint that you copied from GSuite.
   5. **IdP Certificate Fingerprint Algorithm**: Select *sha256*.
   6. **IdP Entity ID:** Enter the Entity ID that you copied from GSuite.
   7. **IdP SSO Target URL:** Enter the SSO URL that you copied from GSuite.

      [![image.png](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084275/c71cf31d8fb5da4dd88c6a33/8b9d3557-e091-4f50-8cb9-84e1aeb06c8a?expires=1781168400&signature=fd7ff4c52c7ff41e2589753e0f8d67e76ca6fb548c4f8cdd59200eb325d9f723&req=dyUiFsF6n4ZaFb4f3HP0gDA7K6IGiFr%2BYtGGo3l5g5%2BSetRQy%2F9hX33Zqmqf%0A7%2Bs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084275/c71cf31d8fb5da4dd88c6a33/8b9d3557-e091-4f50-8cb9-84e1aeb06c8a?expires=1781168400&signature=fd7ff4c52c7ff41e2589753e0f8d67e76ca6fb548c4f8cdd59200eb325d9f723&req=dyUiFsF6n4ZaFb4f3HP0gDA7K6IGiFr%2BYtGGo3l5g5%2BSetRQy%2F9hX33Zqmqf%0A7%2Bs%3D%0A)
4. Click **Save Changes**.
5. Scroll down to the **Authentication Provider Generated Config** section and take note of the values for:

   1. **Assertion Consumer Service URL**
   2. **Service Provider Entity ID**
   3. **Name Identifier Format**

      [![Authentication Provider Generated Config section.](https://downloads.intercomcdn.com/i/o/354015051/34a67eae53bafe6abd38ef61/image.png?expires=1781168400&signature=a4d621caab7506417545cad2cb4eb6cfdc2fc5804dedf9bf473a36b634d33a8c&req=dyUjFsh7nYReFb4f3HP0gBefACbGOhNPZ5EjZ557AN%2FFi0Gosg9fNL5toOIS%0AGws%3D%0A)](https://downloads.intercomcdn.com/i/o/354015051/34a67eae53bafe6abd38ef61/image.png?expires=1781168400&signature=a4d621caab7506417545cad2cb4eb6cfdc2fc5804dedf9bf473a36b634d33a8c&req=dyUjFsh7nYReFb4f3HP0gBefACbGOhNPZ5EjZ557AN%2FFi0Gosg9fNL5toOIS%0AGws%3D%0A)
6. Return to GSuite and click **Continue**.

[Back to Top](#h_8bdd96afc4)

## 3. Configure Telnyx as the SSO Provider

In this step, you'll configure Telnyx to act as your SSO provider

1. On the **Service Provider Details** page, provide the following information:

   1. **ACS URL:** Use the value generated for **Assertion Consumer Service URL** on the Telnyx Mission Control Portal
   2. **Entity ID:** Use the value generated for **Service Provider Entity ID** on the Telnyx Mission Control Portal
   3. **Start URL:** Fill in the following URL: <https://portal.telnyx.com>
   4. **Name ID format**: select *EMAIL*.
   5. **Name ID:** Select *Basic Information > Primary email*.

      [![image.png](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084291/02f9d039ea6030311da81d59/9468ad28-b180-41d8-8980-5d3acb8d93bf?expires=1781168400&signature=1a23c602554250b9f06297543e0536e2b3ac54212bcd1d4b19a4305b9058cb08&req=dyUiFsF6n4heFb4f3HP0gJwNZK9Kf74SFh%2BvfmeS1IvRGWsQoEHa3jLlfW%2B3%0Api4%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/355084291/02f9d039ea6030311da81d59/9468ad28-b180-41d8-8980-5d3acb8d93bf?expires=1781168400&signature=1a23c602554250b9f06297543e0536e2b3ac54212bcd1d4b19a4305b9058cb08&req=dyUiFsF6n4heFb4f3HP0gJwNZK9Kf74SFh%2BvfmeS1IvRGWsQoEHa3jLlfW%2B3%0Api4%3D%0A)
2. Click **Continue** at the bottom of the page. On the next page, click **Finish**.

[Back to Top](#h_8bdd96afc4)

## 4. Enable your SSO configuration on your Telnyx account

In this section, you'll enable your SSO configuration on your Telnyx Mission Control Portal.

1. Log back into your Telnyx Mission Control Portal.
2. Check the **Enable Single-Sign-On** box.
3. Click **Save Changes**.

   [![Single sign-on section.](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)](https://downloads.intercomcdn.com/i/o/350443408/947b2fcfb531c0eed803470d/image.png?expires=1781168400&signature=2eb60c908af7365b1d49fbe47b28b02811724b6a678c59e91aad45a71050abdd&req=dyUnEs19mYFXFb4f3HP0gKwb40%2BeAa%2BzVjFzN5uIj9Cb3LzdGDKXra2E%2B1TA%0AbFE%3D%0A)

Your chosen settings are now in effect! This will send all users in your organization an email informing them that SSO is now enabled. Your users will still be able to login using username/password for the next 72 hours. After that, they will be required to use SSO.

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [GSuite FAQ](https://workspace.google.com/faq/)
* [GSuite support](https://workspace.google.com/support/)
* [GSuite troubleshooting](https://workspace.google.com/support/#google-workspace-trouble-shooting)
* [GSuite admin help community](https://support.google.com/a/community?hl=en)
* [GSuite learning center (Documentation)](https://support.google.com/a/users/?hl=en#topic=9917952)

---

---

Related Articles

[OneLogin: SAML Identity Setup](https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup)[Okta: SAML Identity Setup](https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup)[LastPass: SAML Identity Setup](https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup)[Azure AD: SAML Identity Setup](https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup)[Auth0 SSO Integration With Telnyx](https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx)

Did this answer your question?

😞😐😃

Table of contents
