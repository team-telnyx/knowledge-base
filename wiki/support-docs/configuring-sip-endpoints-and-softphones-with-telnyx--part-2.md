---
title: Configuring SIP Endpoints and Softphones with Telnyx
summary: Step-by-step instructions for registering a variety of SIP-compatible softphones,
  IP phones, and hardware endpoints (Linphone, Yealink, Zoiper variants, Algo 8xxx,
  NCH Express Talk, Zoiper Communicator) with the Telnyx Mission Control Portal, including
  credential setup, encryption (TLS/SRTP), caller ID configuration, and voicemail
  enablement.
sources:
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
updated_at: 2026-08-05T13:31:36Z
---

# Configuring SIP Endpoints and Softphones with Telnyx

*Part 2 of 3 — see also: [Part 1](configuring-sip-endpoints-and-softphones-with-telnyx--part-1.md), [Part 3](configuring-sip-endpoints-and-softphones-with-telnyx--part-3.md)*

Step-by-step instructions for registering a variety of SIP-compatible softphones, IP phones, and hardware endpoints (Linphone, Yealink, Zoiper variants, Algo 8xxx, NCH Express Talk, Zoiper Communicator) with the Telnyx Mission Control Portal, including credential setup, encryption (TLS/SRTP), caller ID configuration, and voicemail enablement.

## Zoiper

[Zoiper](https://www.zoiper.com) is a cross-platform VoIP softphone supporting voice, video, and instant messaging on Windows, Mac, Linux, iOS, Android, and Windows Phone. It supports multiple encryption protocols and offers call-center features such as auto-answer, call transfer, recording, provisioning, and click-2-dial CRM integration.

### Zoiper 5 Pro

Pre-requisites: a [Zoiper 5 Pro license](https://www.zoiper.com/en/shop/buy/zoiper5?cid=main-nav) and a Telnyx credentials-based connection.

1. Click **Activate your Premium license** and follow the activation wizard. Activation credentials come from Zoiper, not Telnyx.

   ![Activate a Zoiper 5 Pro license](_images/ab2faebf79be1904.png)
2. On the login screen, click **Activate online** (or offline if needed).

   ![Zoiper activation login scene.](_images/994e9225e28427b4.png)
3. Click **Create account**.

   ![Account creation wizard interface.](_images/d2923deb71af4b98.png)
4. Choose your location, select your country, type "Telnyx" to filter providers, and select Telnyx.

   ![Account creation interface to filter Telnyx out.](_images/51eb3e2398f651e6.png)
5. Click **Next** to accept the auto-detected protocols.

   ![Tab to test various possible configurations.](_images/85fe2abe8bde394d.png)
6. Configure sound, video, and microphone settings (see the [Zoiper 5 user guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf), page 16).

   ![Sound, video, and microphone settings interface on Zoiper.](_images/d4583e8dc7eead0a.png)
7. Click the account name to open account settings.

   ![Account settings page.](_images/115568accc4cdca5.png)

#### Activating Zoiper 5 Pro Offline

1. From the login screen, click **Activate offline**.

   ![Offline activation button on the login screen.](_images/dc5293f1bfbebdec.png)
2. A file named `Zoiper<ComputerName>.certificate` is generated. Locations:
   - All-users install: `\Zoiper5\` folder.
   - Current-user install: `%USERPROFILE%\AppData\Romaing\Zoiper5` on Windows, or `~/Library/Application Support` or `~/Library/Preferences` on Mac.
3. Email the certificate to [register5@shop.zoiper.com](mailto:register5@shop.zoiper.com) and save the returned certificate in the same folder.

> Windows may hide known file extensions or auto-append one. Right-click the file, choose **Properties**, and remove any extension Windows added.

#### Zoiper 5 Advanced Settings

Click **Advanced** from the account settings view.

![Advanced settings in the Accounts section.](_images/95131278827aef84.png)

**Audio Codecs:** Scroll to the Audio Codecs section and use the arrows to move desired codecs to the right.

![Selected Codecs of the Audio codecs section.](_images/ff9158ad76fe3288.png)

**Network Settings:** In the Network Related section, set:
- **Registration expire mode:** Custom
- **Registration expiry:** 300
- **NAT keep alive time-out:** Custom
- **Keep alive custom interval:** 30

![Network settings page.](_images/84d86afd02091975.png)

**Call Encryption (TLS/SRTP):**
1. Enable **Encrypted SIP Traffic** on the account. If enabled while the device sends UDP/TCP or RTP, calls will be rejected with error code 488.

   ![Account settings page.](_images/fabe58b8465fee0c.png)
2. For sub-accounts, enable in **Sub accounts > Manage sub-accounts > Advanced Options**.

   ![Sub accounts > Manage sub-accounts > Advanced Options page.](_images/46be213d74533507.png)
3. In **Advanced > SIP Credentials**, set:
   - **Domain:** `sip.telnyx.com`
   - **Username:** Account/sub-account name.
   - **Password:** SIP password.
4. In **Network Related**, set **Transport:** TLS.
5. In **Encryption**, set **SRTP Key Negotiation:** SDES.

   ![Encryption settings page.](_images/da416151da669e21.png)

A green closed padlock next to the call profile indicates a secure call.

![Call profile showing "secured" icon sign.](_images/6c80da70a6374a35.png)

### Zoiper 3 (Mac)

1. Download, install, and run Zoiper.
2. If you have a business license, log in with the email used to purchase and the password Zoiper emailed you.
   - **Activate online:** click **Activate online**.
   - **Activate offline:** click **Activate offline** to generate `Zoiper<ComputerName>.certificate` in `~/Library/Zoiper3/`. Email it to [register4@shop.zoiper.com](mailto:register5@shop.zoiper.com) and save the returned certificate in the same folder.
3. Open **Settings > Create a new account**.

   ![Account creation button.](_images/94ec962cd16b396e.png)
4. Select **SIP** (Telnyx does not support IAX or XMPP) and click **Next**.

   ![SIP account button for Telnyx.](_images/f9d97b98ebc02c56.png)
5. Enter your Telnyx credentials. **Domain/outbound proxy:** `sip.telnyx.com`. Click **Next**.

   ![SIP user credentials settings.](_images/68802395521c7372.png)
6. Provide an account name and click **Next**.

   ![Provider Name tab.](_images/4e435eded5c23de8.png)
7. Zoiper connects to the Telnyx server.

   ![A loading Zoiper configuration.](_images/9a4bfa7076839a6f.png)

### Zoiper 3 (Linux)

The Linux flow mirrors the Mac flow with these differences:
- The offline certificate folder is `~/.Zoiper`.
- The activation email is [register4@shop.zoiper.com](mailto:register5@shop.zoiper.com).

![Zoiper activation page.](_images/512af175414d2397.png)
![Zoiper Account Creation page.](_images/47845af19341311d.png)
![Zoiper account type for Telnyx.](_images/1136d35cb2da07a4.png)
![Zoiper user credentials.](_images/938ce0b03c016ad2.png)
![Account identifier creation.](_images/2b179cbc60f034a6.png)
![Zoiper's Connection to Telnyx loading.](_images/88e7962d815110fe.png)

### Zoiper Communicator

[Zoiper Communicator](https://digitalvoice.ca/softphone_zoiper_dl.php) is a free IAX & SIP softphone for Windows combining voice, video, fax, instant messaging, and presence. The Zoiper Service is optional and can be skipped at startup.

1. Open **Settings** and select **Create New Account**.

   ![Settings section of the Zoiper Communicator.](_images/3fb49e1c720698a3.png)
2. Enter an account name and click **OK**.

   ![Account name entry section of the Zoiper Communicator.](_images/027d63e0f7f7e542.png)
3. On the **SIP Account Options** page, enter:
   - **Domain:** `sip.telnyx.com`
   - **Username:** Main Telnyx account or sub-account username.
   - **Password:** Main Telnyx account or sub-account password.
   - **Caller ID Name:** Preferred name (see caller ID conventions below).

   ![SIP Account Options page.](_images/9a06f8dae4238525.png)
4. Click **OK**.

   ![SIP Account Options page to complete setup.](_images/f0a398602bda56f2.png)

For Zoiper 3, see the [Zoiper 3 user guide](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3).

### Zoiper Troubleshooting

If Zoiper cannot configure the account, verify:
- The server hostname is correct (spelling, periods vs. commas).
- The username and password are correct.
- The server is responsive.
- A firewall or security settings are not blocking access (use offline activation if needed).
- The account needs additional configuration.

If everything is correct, select **I know what I am doing, save this information anyway** and click **NEXT** to complete configuration manually.

![Troubleshooting page.](_images/a18ea65676e0d628.png)
