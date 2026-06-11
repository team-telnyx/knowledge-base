---
source_url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
scraped: 2026-06-11
---

Zoiper 3: Telnyx Setup (Linux) | Telnyx Help Center

[Skip to main content](#main-content)

# Zoiper 3: Telnyx Setup (Linux)

How to configure Zoiper 3 to work with the Telnyx Mission Control portal for a Linux operating system.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_2d3edf7a01)

[Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) is a cross-platform VoIP softphone solution that supports voice calling, video calling, and instant messaging. Zoiper is available for Windows, Mac and Linux and offers companion apps for iOS, Android, and Windows Phone. Zoiper secures voice, text, and video calls through a choice of several encryption protocols. Contacts are pulled from a variety of frequently-used contact lists and arranged in an easily searchable way. Additionally, Zoiper offers call center functionality with features such as auto-answer, call transfer, recording, provisioning, and click-2-dial CRM integration. One of the powers of Zoiper is its ability to facilitate direct calls from email clients or web browsers.

For Zoiper documentation, see:

* [Zoiper 3 user guide](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3)

---

# Instructions for Configuring Zoiper 3 with Telnyx

1. [Create your VoIP account on Zoiper 3](#h_4c7b969580)
2. [Troubleshooting](#h_ce63df2bf2)

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

**Pre-Requisites:**

* Ensure you have [properly configured your Telnyx Mission Control Panel](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have created a [credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive outbound calls. This provides you with the username and password you will use to register Zoiper 3 with Telnyx

## 1. Create your VoIP account on Zoiper 3

|  |
| --- |
| ***Note:*** *Visit [https://oem.zoiper.com](https://oem.zoiper.com/) for more information about providing your users with a preconfigured/pre-provisioned Zoiper. This will allow the end user to bypass all the configuration steps and set them up to make calls immediately after they finish installation.* |

1. Download and install Zoiper and run the software.
2. If you have a business license, follow these steps. If not, move on to step 3.

   1. An activation screen will appear when you first run Zoiper. The first step is a login screen. Log in with the **email address you used to purchase your Zoiper license** and the **password that Zoiper emailed to you** immediately following purchase.

      [![Zoiper activation page. ](https://downloads.intercomcdn.com/i/o/417010540/afb1cc3428755f5da2f51d99/activation-dialog.png?expires=1781168400&signature=c0fc3b6902d5c92ce422c1d0b97c370cfebe664ae0284c596ea351d3a3ef99aa&req=cCEgFsh%2BmIVfFb4f3HP0gBs0abEUO1HrKq3vyLGKZVFWHZGihC8vW%2Fm%2FJ%2FrY%0AIo4%3D%0A)](https://downloads.intercomcdn.com/i/o/417010540/afb1cc3428755f5da2f51d99/activation-dialog.png?expires=1781168400&signature=c0fc3b6902d5c92ce422c1d0b97c370cfebe664ae0284c596ea351d3a3ef99aa&req=cCEgFsh%2BmIVfFb4f3HP0gBs0abEUO1HrKq3vyLGKZVFWHZGihC8vW%2Fm%2FJ%2FrY%0AIo4%3D%0A)
   2. **Activating online:** click the **Activate online** button and Zoiper will do the rest. .
   3. **Activating offline:** There may be circumstances where you can't activate online, such as a firewall or other security settings blocking activation. In this case, click the Activate offline button. This will generate a file named **Zoiper<ComputerName>.certificate** that contains information about your version of Zoiper and some details about your computer. You can find the certificate folder at **~/.Zoiper**.
   4. Send the **Zoiper<ComputerName>.certificate** to [register4@shop.zoiper.com](mailto:register5@shop.zoiper.com) who will send you back a certificate back.
   5. Save this certificate in the same folder as 2.c.
3. You can now create your VoIP account on your new Zoiper softphone. Click on the **Settings** menu and select **Create a new account**.

   [![Zoiper Account Creation page. ](https://downloads.intercomcdn.com/i/o/417012135/e2b02355f45cd00122a3db48/zoiper1.png?expires=1781168400&signature=7e533763d1c66f0e42e43c9094f0a774ded93e7bfb129eb91f92c7f0cc3a3fc1&req=cCEgFsh8nIJaFb4f3HP0gOV7mPnNtpuWZ09WRx9m6LDMVhCE9YTenQBjo0pv%0AfC4%3D%0A)](https://downloads.intercomcdn.com/i/o/417012135/e2b02355f45cd00122a3db48/zoiper1.png?expires=1781168400&signature=7e533763d1c66f0e42e43c9094f0a774ded93e7bfb129eb91f92c7f0cc3a3fc1&req=cCEgFsh8nIJaFb4f3HP0gOV7mPnNtpuWZ09WRx9m6LDMVhCE9YTenQBjo0pv%0AfC4%3D%0A)
4. The wizard will ask you what type of account you want to create. You'll need to select SIP here, as Telnyx doesn't support IAX or XMPP. Click **Next**.

   [![Zoiper account type for Telnyx. ](https://downloads.intercomcdn.com/i/o/417012498/7501c3b730bc062014cb4f30/sip.png?expires=1781168400&signature=2dca1695bfaa942f4394f90166ede051af4181835b4f1ebadd055249497a1fbd&req=cCEgFsh8mYhXFb4f3HP0gDuje8PNtH94TGswolMqYGraaAUiJjDeyk%2B5ZWMg%0Al90%3D%0A)](https://downloads.intercomcdn.com/i/o/417012498/7501c3b730bc062014cb4f30/sip.png?expires=1781168400&signature=2dca1695bfaa942f4394f90166ede051af4181835b4f1ebadd055249497a1fbd&req=cCEgFsh8mYhXFb4f3HP0gDuje8PNtH94TGswolMqYGraaAUiJjDeyk%2B5ZWMg%0Al90%3D%0A)
5. You will be asked to provide your user credentials. These will be your *Telnyx* credentials. **Domain/outbound proxy** will be sip.telnyx.com. Click **Next**.

   [![Zoiper user credentials. ](https://downloads.intercomcdn.com/i/o/417012777/8112e2bbd3b962096d5c6978/accountcreds.png?expires=1781168400&signature=4b9d98dd3f15fe1f72c35d7e6c9d274fc91dfcf1207839811fda798aff163321&req=cCEgFsh8moZYFb4f3HP0gFgQ4LoQZbwd9DA6TJ7EeC40EMtikvZ%2BGGwXWO0s%0AxXU%3D%0A)](https://downloads.intercomcdn.com/i/o/417012777/8112e2bbd3b962096d5c6978/accountcreds.png?expires=1781168400&signature=4b9d98dd3f15fe1f72c35d7e6c9d274fc91dfcf1207839811fda798aff163321&req=cCEgFsh8moZYFb4f3HP0gFgQ4LoQZbwd9DA6TJ7EeC40EMtikvZ%2BGGwXWO0s%0AxXU%3D%0A)
6. Next, you will provide a name to identify this account. You can give any name you wish here. When you're satisfied, click on **Next**.

   [![Account identifier creation. ](https://downloads.intercomcdn.com/i/o/417013205/2d582613212c15501c179d4c/acctname.png?expires=1781168400&signature=1f3a5020b6610b229c6c2fd56abf3265c1c9aab1499bc8bed1d10f76a1c4f387&req=cCEgFsh9n4FaFb4f3HP0gAkcW4dUXf%2FkbdAkMAV95jtwN%2FehmI3UxdH2YYCD%0Aghw%3D%0A)](https://downloads.intercomcdn.com/i/o/417013205/2d582613212c15501c179d4c/acctname.png?expires=1781168400&signature=1f3a5020b6610b229c6c2fd56abf3265c1c9aab1499bc8bed1d10f76a1c4f387&req=cCEgFsh9n4FaFb4f3HP0gAkcW4dUXf%2FkbdAkMAV95jtwN%2FehmI3UxdH2YYCD%0Aghw%3D%0A)
7. Once you've clicked Next, Zoiper will do the rest to connect to the Telnyx server. This may take time, but the wizard will keep you apprised.

   [![Zoiper's Connection to Telnyx loading. ](https://downloads.intercomcdn.com/i/o/417013475/8858b39e6cf37bbd3c89591f/account-wizard-configuring-account-dialog.png?expires=1781168400&signature=275e1958ad3bbcc5ac56fe8684f48b2c3ecc4d7e06b52aca8083e62399e017d3&req=cCEgFsh9mYZaFb4f3HP0gBdblF1xy%2FUH02GNBMkBLRV7EnP87Tlo4ul5bhFH%0AMMg%3D%0A)](https://downloads.intercomcdn.com/i/o/417013475/8858b39e6cf37bbd3c89591f/account-wizard-configuring-account-dialog.png?expires=1781168400&signature=275e1958ad3bbcc5ac56fe8684f48b2c3ecc4d7e06b52aca8083e62399e017d3&req=cCEgFsh9mYZaFb4f3HP0gBdblF1xy%2FUH02GNBMkBLRV7EnP87Tlo4ul5bhFH%0AMMg%3D%0A)

[Back to Top](#h_2d3edf7a01)

## 2. Troubleshooting

If Zoiper is unable to configure your account, make sure:

* The server hostname is correct, and exists (Check spelling and periods versus commas etc.)
* The username or password is incorrect.
* The server is not responsive for some reason.
* A firewall or other security settings are blocking access. See Step 2 for the option to activate offline.
* The account needs additional configuration work in order to be registered.

If you've verified all the information is correct, you can save the information and complete the remainder of the configuration manually. To do this, select the **I know what I am doing, save this information anyway** radio option and click **NEXT**.

[![Account Wizard. ](https://downloads.intercomcdn.com/i/o/417013918/651ebe5765849b86d1b7efb0/account-wizard-troubleshooting-dialog.png?expires=1781168400&signature=0c2f1e455b1dd9e994573febc8aa01ffc316279c033383b94a7fc815e8c1ffd2&req=cCEgFsh9lIBXFb4f3HP0gPlqcW%2FHKYOk5G7m3dd7iXTDCHr9RjbLPK%2BWWMW4%0Af5oH0Qxw9u1k6TIj2w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/417013918/651ebe5765849b86d1b7efb0/account-wizard-troubleshooting-dialog.png?expires=1781168400&signature=0c2f1e455b1dd9e994573febc8aa01ffc316279c033383b94a7fc815e8c1ffd2&req=cCEgFsh9lIBXFb4f3HP0gPlqcW%2FHKYOk5G7m3dd7iXTDCHr9RjbLPK%2BWWMW4%0Af5oH0Qxw9u1k6TIj2w%3D%3D%0A)

That's it, you've now completed the configuration of your Zoiper 3 softphone client and can now make and receive calls by using Telnyx as the SIP provider.

[Back to Top](#h_2d3edf7a01)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Check out the [Zoiper 3](https://www.zoiper.com/en/support/home/article/34/Installation_%26_configuration_manuals_Zoiper_3) user guide.

---

Related Articles

[Configuring Bria Solo (a.k.a X-Lite)](https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite)[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Zoiper 5 Pro: Telnyx Setup](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup)[Zoiper 3: Telnyx Setup (Mac)](https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)

Did this answer your question?

😞😐😃

Table of contents
