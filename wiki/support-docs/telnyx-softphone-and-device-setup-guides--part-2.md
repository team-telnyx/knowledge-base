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

*Part 2 of 4 — see also: [Part 1](telnyx-softphone-and-device-setup-guides--part-1.md), [Part 3](telnyx-softphone-and-device-setup-guides--part-3.md), [Part 4](telnyx-softphone-and-device-setup-guides--part-4.md)*

Consolidated Telnyx setup guides for popular SIP softphones and IP phones (Linphone, Yealink T Series, Zoiper 3/5/Communicator, Acrobits Softphone/Groundwire, MicroSIP) plus an ElevateAI proof-of-concept integration. Each section covers prerequisites, account creation, SIP connection details (using sip.telnyx.com), optional TLS/SRTP encryption, and caller ID configuration.

## Zoiper 5 Pro

[Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) is a cross-platform VoIP softphone for Windows, Mac, Linux, iOS, Android, and Windows Phone. It supports voice, video, instant messaging, and several encryption protocols. See the [Zoiper 5 user guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf).

> This guide covers Zoiper 5 Pro. For the free version, see the [Zoiper free user guide](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/5717568/show). Compare free and pro features [here](https://www.zoiper.com/en/products/zoiper5/features).

### Pre-requisites

- Obtain a [Zoiper 5 Pro license](https://www.zoiper.com/en/shop/buy/zoiper5?cid=main-nav).
- Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on the Telnyx Mission Control Portal, assign it to a DID and outbound profile.

### Creating a VoIP account

1. Click **Activate your Premium license** and follow the activation wizard. Activation credentials come from Zoiper, not Telnyx.

   ![Activate a Zoiper 5 Pro license](_images/ab2faebf79be1904.png)
2. On the login screen, click **Activate online** (or see offline activation below).

   ![Zoiper activation login scene. ](_images/994e9225e28427b4.png)
3. Click **Create account** in the wizard.

   ![Account creation wizard interface. ](_images/d2923deb71af4b98.png)
4. Choose your location and country, enter "Telnyx" to filter providers, then select Telnyx.

   ![Account creation interface to filter Telnyx out. ](_images/51eb3e2398f651e6.png)
5. The wizard auto-detects protocols. Click **Next**.

   ![Tab to test various possible configurations. ](_images/85fe2abe8bde394d.png)
6. After authentication, configure sound, video, and microphone settings (see the [Zoiper 5 user guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf), page 16).

   ![Sound, video, and microphone settings interface on Zoiper. ](_images/d4583e8dc7eead0a.png)
7. Click the account name to open account settings.

   ![Account settings page. ](_images/115568accc4cdca5.png)

To add more accounts, click **Add** and repeat steps 3–6.

### Offline activation

If you cannot reach the Zoiper activation server:

1. Click **Activate offline** on the login screen.

   ![Offline activation button on the login screen. ](_images/dc5293f1bfbebdec.png)
2. A file named `Zoiper<ComputerName>.certificate` is generated. Find it in:
   - All-users install: the `\Zoiper5\` folder.
   - Current-user install: `%USERPROFILE%\AppData\Romaing\Zoiper5` on Windows, or `~/Library/Application Support` or `~/Library/Preferences` on Mac.
3. Email the certificate to [register5@shop.zoiper.com](mailto:register5@shop.zoiper.com) and save the returned certificate in the same folder.

> Windows may hide known extensions and append one automatically. Right-click the file, choose **Properties**, and remove any added extension.

### Advanced settings

Open **Advanced** from the account settings view.

![Advanced settings in the Accounts section. ](_images/95131278827aef84.png)

**Audio codecs:** Scroll to the [Audio Codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality) section and use the arrows to move desired codecs to the right.

![Selected Codecs of the Audio codecs section. ](_images/ff9158ad76fe3288.png)

**Network settings:** In the **Network Related** section, set:

- **Registration expire mode:** Custom
- **Registration expiry:** 300
- **NAT keep alive time-out:** Custom
- **Keep alive custom interval:** 30

![Network settings page. ](_images/84d86afd02091975.png)

**Call encryption (TLS/SRTP):**

1. Enable **Encrypted SIP Traffic** on the account. If this is enabled but the device sends UDP/TCP or RTP, the change is rejected with error code 488.

   ![Account settings page. ](_images/fabe58b8465fee0c.png)
2. For sub-accounts, enable it under **Sub accounts > Manage sub-accounts > Advanced Options**.

   ![ub accounts>Manage sub-accounts>Advanced Options page. ](_images/46be213d74533507.png)
3. In **Advanced > SIP Credentials**, fill in:
   - **Domain:** `sip.telnyx.com`
   - **Username:** Account or sub-account name
   - **Password:** SIP password
4. In **Network Related**, set **Transport:** TLS.
5. In **Encryption**, set **SRTP Key Negotiation:** SDES.

   ![Encryption settings page. ](_images/da416151da669e21.png)

A green closed padlock next to the call profile indicates a secure call.

![Call profile showing "secured" icon sign. ](_images/6c80da70a6374a35.png)

### Caller ID

Telnyx enforces a strict caller ID policy. Most softphones do not directly control the FROM header; sometimes the Display Name variable is used as the caller ID. The number must belong to your Telnyx account or be a [verified number](verified-numbers.md). If you still receive a 403 error after setting a valid caller ID, configure a caller ID override in the outbound section of your SIP connection (see the [Caller ID Number Policy](caller-id-number-policy.md)).

## Zoiper 3 (Mac)

See the [Zoiper 3 user guide](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3) for vendor documentation.

### Pre-requisites

- Configure the [Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) and assign it to a DID and outbound profile.

### Creating a VoIP account

> Visit [https://oem.zoiper.com](https://oem.zoiper.com/) for information on preconfigured/pre-provisioned Zoiper builds that bypass these steps.

1. Download, install, and run Zoiper.
2. If you have a business license:
   - Log in with the email used to purchase the license and the password Zoiper emailed you.
   - **Activating online:** click **Activate online**. Zoiper uses Mac OS proxy settings by default.
   - **Activating offline:** click **Activate offline**. A `Zoiper<ComputerName>.certificate` file is generated in `~/Library/Zoiper3/`. Email it to [register4@shop.zoiper.com](mailto:register5@shop.zoiper.com) and save the returned certificate in the same folder.
3. Open **Settings** and select **Create a new account**.

   ![Account creation button. ](_images/94ec962cd16b396e.png)
4. Select **SIP** (Telnyx does not support IAX or XMPP) and click **Next**.

   ![SIP account button for Telnyx. ](_images/f9d97b98ebc02c56.png)
5. Enter your Telnyx credentials. **Domain/outbound proxy:** `sip.telnyx.com`. Click **Next**.

   ![SIP user credentials settings. ](_images/68802395521c7372.png)
6. Provide a name for the account and click **Next**.

   ![Provider Name tab. ](_images/4e435eded5c23de8.png)
7. Zoiper connects to the Telnyx server.

   ![A loading Zoiper configuration. ](_images/9a4bfa7076839a6f.png)

### Troubleshooting

If Zoiper cannot configure the account, verify:

- The server hostname is correct (check spelling, periods vs commas).
- The username and password are correct.
- The server is responsive.
- No firewall or security settings are blocking access (use offline activation if needed).
- The account does not need additional configuration.

If everything is correct, select **I know what I am doing, save this information anyway** and click **NEXT** to finish manually.

![Troubleshooting page. ](_images/a18ea65676e0d628.png)
