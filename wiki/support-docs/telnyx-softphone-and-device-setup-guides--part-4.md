---
title: Telnyx Softphone and Device Setup Guides
summary: Consolidated Telnyx setup guides for popular SIP softphones and IP phones
  (Linphone, Yealink T Series, Zoiper 3/5/Communicator, Acrobits Softphone/Groundwire,
  MicroSIP) plus an ElevateAI proof-of-concept integration. Each section covers prerequisites,
  account creation, SIP connection details (using sip.telnyx.com), optional TLS/SRTP
  encryption, and caller ID configuration.
sources:
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
updated_at: 2026-07-17T09:06:02Z
---

# Telnyx Softphone and Device Setup Guides

*Part 4 of 4 — see also: [Part 1](telnyx-softphone-and-device-setup-guides--part-1.md), [Part 2](telnyx-softphone-and-device-setup-guides--part-2.md), [Part 3](telnyx-softphone-and-device-setup-guides--part-3.md)*

Consolidated Telnyx setup guides for popular SIP softphones and IP phones (Linphone, Yealink T Series, Zoiper 3/5/Communicator, Acrobits Softphone/Groundwire, MicroSIP) plus an ElevateAI proof-of-concept integration. Each section covers prerequisites, account creation, SIP connection details (using sip.telnyx.com), optional TLS/SRTP encryption, and caller ID configuration.

## Zoiper Communicator

[Zoiper Communicator](https://digitalvoice.ca/softphone_zoiper_dl.php) is a free IAX & SIP softphone combining voice, video, fax, instant messaging, and presence. The Zoiper Service enables free Zoiper-to-Zoiper communication.

> You can decline the Zoiper Service on initial startup by choosing "I don't want to use this service" or simply not logging in. Zoiper does not currently advertise or offer Zoiper Communicator, but it remains available via the link above.

Additional resources: [Zoiper help](https://www.zoiper.com/en/support/questions).

### Pre-requisites

- Configure the [Telnyx Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- Have your SIP credentials (main account or sub-account).
- Have [DIDs available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign.
- Run Windows and [download Zoiper Communicator](https://digitalvoice.ca/softphone_zoiper_dl.php).

### Adding Telnyx as your SIP provider

1. Start Zoiper Communicator and select **Settings**.
2. Select **Create New Account**.

   ![Settings section of the Zoiper Communicator. ](_images/3fb49e1c720698a3.png)
3. Enter a name for the account and click **OK**.

   ![Account name entry section of the Zoiper Communicator. ](_images/027d63e0f7f7e542.png)
4. On the **SIP Account Options** page, provide:
   - **Domain:** `sip.telnyx.com`
   - **Username:** Your main Telnyx account or sub-account username.
   - **Password:** Your main Telnyx account or sub-account password.
   - **Caller ID Name:** Your preferred name. Use capital letters, no special characters (spaces allowed), and keep under 15 characters for some Canadian providers.

   ![SIP Account Options page.](_images/9a06f8dae4238525.png)
5. Click **OK** to complete setup.

   ![SIP Account Options page to complete setup. ](_images/f0a398602bda56f2.png)

## ElevateAI Proof-of-Concept Setup

This guide demonstrates a sample application using Telnyx-Python transcription and recording with ElevateAI.

### Step 1: Create a Call Control Application in the Telnyx Portal

1. Log in to the Telnyx account.
2. Click **Voice** in the left menu, then **Programmable Voice**.
3. Click **Add new App** at the top right.

   ![Add new App section. ](_images/e62edad978fad8e2.png)
4. Enter the application name and webhook URL, then click **Save**.

   ![Voice API application.](_images/2a6ec9ac09086917.png)

### Step 2: Purchase a Telnyx Phone Number

1. Click **Numbers** in the left menu.

   ![Numbers tab section. ](_images/a16c7c4738714091.png)
2. Open the **Search & Buy Numbers** tab, choose the search type and region/area code, and click **Search Numbers**.

   ![Search &amp; Buy Numbers tab. ](_images/fb9ae0e20e752d4e.png)
3. Select a number, click **Add to Cart**, then click the **Cart** button.

   ![Add to Cart section. ](_images/0469442229288ca9.png)
4. Under **Connections or Applications**, select the ElevateAI call control application created in Step 1 and click **Place Order**.

   ![Connections or Applications section. ](_images/b30e62f64b2acd67.png)

### Step 3: Sign up for ElevateAI and get your API key

1. Go to [ElevateAI's website](https://www.elevateai.com/) and click **Get Started**.

   ![Sign Up button. ](_images/441f60395743ae0e.png)
2. Click **Sign Up** to register.

   ![Sign Up button.   ](_images/7d011627c10adea1.png)
3. Fill out the registration form and click **Sign Up**.

   ![Sign Up button. ](_images/82f54c217e09a070.png)
4. After verifying the account, log in and click **Manage Keys**.

   ![ Manage Keys section for inputing IP token. ](_images/0f4d0b386eb1ffb0.png)
5. Copy the API token for later use.

   ![ Manage Keys section for inputing API token. ](_images/d3e544f42e6f8f60.png)

### Step 4: Clone the PoC project

Clone the project from GitHub: <https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control> and follow the steps in the repository.

## Related Articles

- [Configuring an AVAYA IP trunk with Telnyx](configuring-an-avaya-ip-trunk-with-telnyx.md)
- [Configuring a Vicidial IP trunk with Telnyx](configuring-a-vicidial-ip-trunk-with-telnyx.md)
- [Configuring Grandstream GXP16XX with Telnyx](configuring-grandstream-gxp16xx-with-telnyx.md)
- [Configuring Bria Solo (a.k.a X-Lite)](configuring-bria-solo-a-k-a-x-lite.md)
- [Polycom: Setup with Telnyx](polycom-setup-with-telnyx.md)
- [Flyingvoice: Telnyx Setup](flyingvoice-telnyx-setup.md)
- [Grandstream HT802: Telnyx Setup](grandstream-ht802-telnyx-setup.md)
- [BuddyTalk BT110/BT120](buddytalk-bt110-bt120.md)
- [Grandstream Wave Lite (iPhone)](grandstream-wave-lite-iphone.md)
- [Grandstream Wave Lite (Android)](grandstream-wave-lite-android.md)
- [Algo 8xxx: Telnyx Endpoints](algo-8xxx-telnyx-endpoints.md)
- [Gigaset A510: Telnyx Setup](gigaset-a510-telnyx-setup.md)
- [Snom C520: Telnyx Setup](snom-c520-telnyx-setup.md)
- [Vtech VCS754: Telnyx Setup](vtech-vcs754-telnyx-setup.md)
- [Fanvil A32i: Telnyx Setup](fanvil-a32i-telnyx-setup.md)
- [SIP URI Calling](sip-uri-calling.md)
- [MS Teams: Call2Teams & Telnyx](ms-teams-call2teams-telnyx.md)
- [E911 Setup Guide](e911-setup-guide.md)
- [Bicom: PBXware Setup](bicom-pbxware-setup.md)
- [Configuring Telnyx with Microsoft Teams Direct Routing](configuring-telnyx-with-microsoft-teams-direct-routing.md)
- [Real-Time Transcription](real-time-transcription.md)
