---
title: Telnyx Mission Control Account Setup and Messaging
summary: This page covers how to sign up for a Telnyx Mission Control account, configure
  it for voice and messaging, send SMS and Alphanumeric SMS via Postman using API
  v1 and v2, understand global Alphanumeric Sender ID capabilities by country, and
  access useful Mission Control resources.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
updated_at: 2026-07-17T09:08:16Z
---

# Telnyx Mission Control Account Setup and Messaging

*Part 1 of 5 — see also: [Part 2](telnyx-mission-control-account-setup-and-messaging--part-2.md), [Part 3](telnyx-mission-control-account-setup-and-messaging--part-3.md), [Part 4](telnyx-mission-control-account-setup-and-messaging--part-4.md), [Part 5](telnyx-mission-control-account-setup-and-messaging--part-5.md)*

This page covers how to sign up for a Telnyx Mission Control account, configure it for voice and messaging, send SMS and Alphanumeric SMS via Postman using API v1 and v2, understand global Alphanumeric Sender ID capabilities by country, and access useful Mission Control resources.

## Signing Up for a Telnyx Account

The Telnyx sign-up landing page is at [telnyx.com/sign-up](https://telnyx.com/sign-up). Users have two options for account creation:

1. Single Sign-On with Gmail or Microsoft using the provided buttons.
2. Direct sign-up using the form.

Enter your email address, full name, and desired password into the provided text boxes. If you have a promo code, click the link below the password field to apply it. Use the check-box to opt in or out of receiving emails from Telnyx. Click **Create Account**.

**Note:** A business email address is required to create or sign up for a new account, as certain free email providers are disallowed.

### Know Your Customer

As part of creating a trustworthy environment, Telnyx has integrated a Know Your Customer (KYC) procedure into the sign-up process. You may be prompted to follow an identity check before your account can be created. This helps prevent identity theft, financial fraud, money laundering, and other forms of misuse.

### Email Verification

Once you have confirmed your details, an email will be sent to the address you provided to activate your account. Navigate to your inbox and open the "Verify Your Account" email. If you do not see it, check your spam folder. If it is still not present, click the green **Resend verification email** link. Click the blue **Verify email address** button.

Once your email is verified, you may be required to submit **phone verification** by receiving a one-time pass-code. After submitting the pass-code, your phone number will be verified and you will have access to your account.

### Use Case

After activating your account, you will be prompted to fill in information about your use case. Begin by providing your organization's name in the pop-up field. Click **Continue** to proceed. A list of Telnyx features will be displayed; choose all the relevant options for your use case and click **Continue.** The menu will expand further to show the option to specify **I'm a Developer** along with additional details such as your company size and preferred contact number.

### Currency Limitation

- New users signing up from 18 October 2022 onward can no longer choose currencies outside of USD.
- Existing accounts with more than one month of spend cannot have their account currency changed.

Once your information has been entered, click **Complete account setup.** Depending on the features you chose, you will be redirected to the relevant introductory tools:

- **SMS Use Cases** are redirected to the [Learn & Build](https://portal.telnyx.com/#/app/messaging/learn-and-build) section, which provides an introduction to sending your first SMS with Telnyx, including purchasing a number and creating a messaging profile.
- **SIP Trunking Use Cases** receive a number (purchased using free sign-up credit), a SIP Connection, and an Outbound Voice Profile. The Outbound Voice Profile is assigned to the SIP Connection, and the Connection is assigned to the number.

### Single Sign-On

Business accounts can take advantage of Single Sign-On (SSO) using one of several SAML providers, including [Auth0](https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx), [Microsoft Azure Active Directory](https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup), [Okta](https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup), [Google GSuite](https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx), [OneLogin](https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup), and [LastPass](https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup).

To begin using SSO, you must first create an Organization within your portal. From your Telnyx Portal homepage, navigate to **My Account → Single Sign-On** and click **Enable Single Sign-On.** Enter the relevant details from your SAML provider into the fields provided and click **Import IdP Settings & Save.** After saving, scroll down to note the values for **Assertion Consumer Service URL**, **Service Provider Entity ID**, and **Name Identifier Format**, which must be provided within your SAML app. Once you have provided the details from your Telnyx Portal to your provider, click the "Enable Single Sign-On" box and click **Save Changes.**

All users in your organization will receive an email informing them that SSO is now enabled. Users can still log in using username/password for the next 72 hours; after that, they will be required to use SSO.

### Logging In with SSO

To log in with your newly saved Single Sign-On service, navigate to the [sign-in](https://portal.telnyx.com/#/login/sign-in) page and click on the **Single Sign-On** tab. Enter your relevant login details.

### Trial Credit

Telnyx may provide free trial credit from time to time for certain products; however, at this moment there are no promotions that provide free trial credit.

### Notes

- If the login button is disabled, verify that your browser is not blocking Google scripts for reCAPTCHA verification.
- If you receive the error "You cannot sign in as your identity verification was rejected," email [support@telnyx.com](mailto:support@telnyx.com) for assistance.

## Getting Started with a Mission Control Account

After signing up, four (or five) requirements are needed to set up your Telnyx Mission Control Portal account so that it is ready to be configured to your PBX phone system, softphone client, or softswitch of your choice.

### 1. Level 1 Verification

In order to assign a connection or messaging profile on a DID, or a connection on an outbound voice profile, you must be Level 1 verified. See [Account Verification](account-verification.md) for more information.

### 2. Connection Setup

A connection is needed to authenticate your client with the Telnyx SIP proxy at [sip.telnyx.com](https://sip.telnyx.com/). Three authentication options are available on the portal: **Credentials**, **IP Address**, and **FQDN**. You must select one of the authentication methods to whitelist your server to the [sip.telnyx.com](https://sip.telnyx.com/) domain. See [SIP Connection Types](sip-connection-types.md) for more details.

### 3. DIDs

A DID is required in order to receive inbound calls to your client. Once you have purchased a DID on your account, you must assign the connection you wish to receive inbound calls to. See [Search and Buy Numbers](search-and-buy-numbers.md) for the number search feature, and [How to Setup a DID to SIP Connection](how-to-setup-a-did-to-sip-connection.md) for assigning DIDs to a connection and DID features.

### 4. Outbound Voice Profile

An outbound voice profile is required in order to make outbound calls. See [More About Outbound Voice Profiles](more-about-outbound-voice-profiles.md) for more information on creating an outbound profile and its features.

### 5. Payments

You will need to add a payment method to your account in order to top up your balance. This is necessary to purchase numbers, send messages, and make/receive calls. See [Billing Setup & Billing Groups](billing-setup-billing-groups.md) for further details on adding a payment method.

Additional information that may be needed for configuring your client, such as a list of Telnyx signalling and media IPs to the SIP proxy, can be found at [sip.telnyx.com](https://sip.telnyx.com/).
