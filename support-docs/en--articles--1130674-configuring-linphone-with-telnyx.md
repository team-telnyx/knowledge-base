---
source_url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
scraped: 2026-07-08
content_hash: 5a650a855a2422e3a1f1ca87d3d4effc3ab61c7de66d2d84f9237fc9e3a62b9d
---

Configuring Linphone with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring Linphone with Telnyx

In this article we will walk you through how to configure Linphone with the Telnyx Mission Control Portal.

Written by Telnyx Sales

March 3, 2024

Table of contents

[Jump to Instructions](#h_243a357b53)

[Linphone](https://www.linphone.org) is an open source VoIP softphone SIP client that supports audio and video calls through VoIP softswitches or IP-PBX. It also allows for instant messaging. Since it was launched in 2001, it has become very popular, especially within the open source community.

For Linphone documentation, see:

* Linphone vendor-side [technical documentation](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/)
* Linphone [support](https://www.linphone.org/contact)

---

# Instructions for Configuring Linphone with Telnyx

1. [Configuring your Linphone](#h_fbaa0b1c3d)
2. [Configuring your Linphone with encryption](#h_cc01cc6a37)
3. [Setting up Caller ID](#h_04e0aa8644)

**Pre-Requisites:**

* Have already created a credentials-based connection on your Telnyx Mission Control Panel account, have assigned this connection to a DID and outbound profile in order to make or receive calls
* Have [configured your Telnyx Mission Control Portal](https://portal.telnyx.com/)

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

## 1. Configuring your Linphone

1. Run your Linphone Softphone and follow the instructions on the wizard.
2. Once Linphone is up and running, click on the ACCOUNT ASSISTANT option.

   ![Linphone softphone account assistant wizard 2. ](_images/8b335edacfc3dc96.png)
3. From the Assistant screen, click on USE A SIP ACCOUNT.

   ![Linphone softphone account assistant wizard 2. ](_images/019b946dee183f15.png)
4. Fill in the form with the following information where:

   1. **Username:** Your auth username for the SIP connection in your portal.
   2. **Display Name:** Most Linphone versions use the Display name as the FROM field, so this needs to be your caller id. We have very strict policies about caller id format, which you can read [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy). If you are not using a Telnyx number you need to verify your number before using it as a caller id you can read more about that [here.](https://support.telnyx.com/en/articles/6988813-verified-numbers)
   3. **SIP Domain:** sip.telnyx.com
   4. **Password:** The auth password for the SIP connection in your portal
   5. **Transport:** UDP or TCP
5. ![SIP Account credentials form. ](_images/ce6604b2be2af738.png)
6. Click on the **USE** button.

Your Linphone should now be ready to make calls.

|  |
| --- |
| ***Note:*** *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. Please view our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.* |

[Back to Top](#h_243a357b53)

## 2. Configuring your Linphone with Encryption

1. Follow steps 1-4 of section 2.1 with the following exceptions:

   1. In the **SIP Domain** field, append port 5061 to the end of the server address (i.e.: sip.telnyx.com:5061)
   2. In the **Transport** field, select TLS.

      ![Linphone encryption configuration interface. ](_images/199007f6c0bcd3ad.png)
2. Click on the top right menu and select Preferences.

   ![Linphone encryption configuration interface 2. ](_images/5c88d2b750147f0e.png)
3. Click on the Call and Chat tab and enable SRTP.

   ![Linphone encryption configuration interface 3. ](_images/a93183304bd48a07.png)

[Back to Top](#h_243a357b53)

## 3. Setting up Caller ID

At Telnyx we have a very strict caller ID policy. You need to make sure your softphone or system is sending a valid caller id per our policies found [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy?q=verified+#h_986dcc6763) and the number you're using is either a number you have in your account with Telnyx or it's a number that has been previously verified with Telnyx. Instructions on how to verify a number can be found [here](https://support.telnyx.com/en/articles/6988813-verified-numbers).

If you are still getting a 403 error about an invalid caller id, the most usual issue is your softphone or system is not correctly passing the caller ID in one of the headers required. As a workaround you will need to setup a caller ID override in the outbound section of your sip connection settings. You can find the instructions in the caller id policy article [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy?q=verified+#h_986dcc6763).

[Back to Top](#h_243a357b53)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally check out:

* Linphone's [developer documentation](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/)
* Linphone [support](https://www.linphone.org/contact)

---

Related Articles

[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Zoiper 5 Pro: Telnyx Setup](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)

Did this answer your question?

😞😐😃

Table of contents
