---
title: Cisco and Third-Party Voice Device Configuration
summary: This page consolidates Telnyx configuration guides for Cisco CUBE/CUCM IP
  and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and
  the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the
  Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback
  process.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
updated_at: 2026-07-17T09:02:19Z
---

# Cisco and Third-Party Voice Device Configuration

*Part 4 of 4 — see also: [Part 1](cisco-and-third-party-voice-device-configuration--part-1.md), [Part 2](cisco-and-third-party-voice-device-configuration--part-2.md), [Part 3](cisco-and-third-party-voice-device-configuration--part-3.md)*

This page consolidates Telnyx configuration guides for Cisco CUBE/CUCM IP and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback process.

## BuddyTalk BT110/BT120

[BuddyTalk](https://www.innomedia.com/buddytalk-product-family/), powered by the Amazon Alexa Voice Service (AVS) and Alexa Communication (ACM), is an intelligent speakerphone and smartspeaker which can be configured to allow a VoIP subscription to deliver incoming and outgoing calls. BuddyTalk is equipped with advanced audio processing and has VoIP capability, all while delivering calling flexibility, superior voice quality, and strong security.

> Note: For an even more rich experience with your BuddyTalk BT product, consider the BuddyTalk Mobile App after you have completed this setup.

### Pre-requisites

- Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers)).
- Recommended: [Enable TLS if you want to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).
- An Amazon account with Comm. enabled.
- The Alexa app enabled.
- The BuddyTalk Setup App:
  - **Android App:** Google Play Store. The App is supported on phones and tablets running Android 4.4.4 and above.
  - **iOS App:** [Apple App Store](https://apps.apple.com/us/app/buddytalk-setup/id1434349567). The Setup App is supported on phones and tablets running iOS version 12 and above.
- Appropriate network setup: ensure that your firewall is open for SIP communication on port 5060.
- Make sure you can access the [BuddyTalk web console](https://www.innomedia.com/buddytalk-product-family/).

### Set Up Your BuddyTalk Profile

1. Open your BuddyTalk Setup App and work through the first two setup steps.
2. On the third step, you will be taken to the **Setup Telephony** screen. Provide the following information:
   - **Name:** Enter your outbound Caller ID name. Use the following naming conventions:
     - Caller ID Name should be in **capital letters**. This will appear more clearly/visible on some devices.
     - You **must NOT use any special characters**, as they will not be displayed. Spaces are allowed.
     - Some regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapting your caller ID.
   - **Account ID:** Your Telnyx SIP account ID
   - **Auth ID:** Your Telnyx SIP account ID
   - **Password:** Your Telnyx SIP account password
   - **Domain:** *sip.telnyx.com*
   - **Outbound proxy (optional):** Toggle this switch to enable outbound proxy
   - **Proxy (optional):** *sip.telnyx.com*
   - **Local SIP Port:** *5060*
   - **Preferred Transport:** *UDP* (default). Note that if you are planning to encrypt calls and have set up call encryption on your Telnyx portal, you should choose *TLS*.

   ![Telnyx account in BuddyTalk](_images/5aaf56564f032ccf.png)

3. After your SIP registration is complete, you should see the phone icon in the upper left corner turn green. Additionally, the phone LED on top of your device will change from red, to green, before turning off.

### Optional: Encrypt Traffic by Enabling TLS

1. Log into the [BuddyTalk Web Console](https://www.innomedia.com/buddytalk-product-family/).
2. Click on **Telephony** in the top navigation.
3. In the left-hand menu, click **Profile Config**.
4. Find the profile you just created and click the edit link (the pencil icon).

   ![Telephony section of the BuddyTalk Web Console.](_images/d983adcf92e05431.png)

5. On the **Edit** screen, find the **SIP Proxy Server** section.
6. Find the **Preferred Transport Protocol** field and select *TLS*.

   ![SIP Server Setting Section.](_images/bb0ffb00ec54a1e8.png)

7. In the left-hand menu, click on **Port Config**.
8. Find the profile you just created and click the edit link (the pencil icon).
9. On the **Edit** screen, find the **Line Setting > Line Options** section.
10. Find the **Secure RTP** field and select *SDES*.

    ![Port configuration settings.](_images/645086169e785a93.jpg)

### Alexa Voice Commands

Now that you're set up and ready to go, try some useful Alexa voice commands:

- Calling (dialing a number): *"Alexa call (some number)"*
- Calling (by contact): *"Alexa, call (name)"*
- Answer a call: *"Alexa, answer call."*
- Disconnect a call: *"Alexa, hang up."*

You can also use all your other [Alexa skills and commands](https://www.amazon.com/alexa-skills/b?ie=UTF8&node=13727921011), even if they're not related to making or managing calls.

## Access Control List (Deprecated)

The [Access Control List](https://portal.telnyx.com/#/app/allowed-ips/ip-addresses) has been deprecated and is no longer active. No users can add or modify any IPs to the ACL at this moment. This is regardless of the account level.

## Accessible Canada Act (ACA) Feedback Process

The Canadian Radio-television and Telecommunications Commission ("CRTC") has implemented rules, the Accessible Canada Act ("ACA") dictating accessibility requirements for telecommunications companies licensed and operating in Canada. In compliance with the ACA, Telnyx enables its customers to provide feedback regarding accessibility to our services.

Should a customer have feedback, please send an email to [acafeedback@telnyx.com](mailto:acafeedback@telnyx.com) with the subject line: "ACA: Feedback." In the email, please share the following:

- Name
- Phone number
- Email
- Relation to Telnyx
- Description of the ACA feedback

## Additional Resources

- [Getting started with a Mission Control account](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Cisco CUBE/CUCM integration documentation](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html)
- [Cisco CME admin guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html)
- [Cisco CME SIP trunking configuration example](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html)
- [Cisco SPA 112/122 product documentation](https://www.cisco.com/c/en/us/support/unified-communications/spa122-ata-router/model.html)
- [Cisco SPA 112/122 end-of-life documentation](https://www.cisco.com/c/en/us/products/collateral/unified-communications/small-business-voice-gateways-ata/eos-eol-notice-c51-743206.html)
- [BT110 user documentation](https://www.innomedia.com/buddytalk-product-family/)
- [BT120 user documentation](https://www.innomedia.com/buddytalk-product-family/)
- [BuddyTalk setup page](https://www.innomedia.com/buddytalk-product-family/)
- [Caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)
- [Dial Plan for Linksys ATAs](https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas)
