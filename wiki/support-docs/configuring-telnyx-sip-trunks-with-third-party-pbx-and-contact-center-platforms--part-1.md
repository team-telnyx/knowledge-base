---
title: Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms
summary: This page consolidates Telnyx guidance for configuring SIP trunks between
  the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact
  center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both
  IP-based and credentials-based authentication, dialplan setup, outbound and inbound
  campaign configuration, and lead import for contact center use cases, alongside
  notes on reseller support, call center service availability, Linksys ATA dialplan
  syntax, and the deprecation of the legacy Access Control List feature.
sources:
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
updated_at: 2026-08-05T13:28:15Z
---

# Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms

*Part 1 of 4 — see also: [Part 2](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-2.md), [Part 3](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-3.md), [Part 4](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-4.md)*

This page consolidates Telnyx guidance for configuring SIP trunks between the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both IP-based and credentials-based authentication, dialplan setup, outbound and inbound campaign configuration, and lead import for contact center use cases, alongside notes on reseller support, call center service availability, Linksys ATA dialplan syntax, and the deprecation of the legacy Access Control List feature.

## Overview

Telnyx supports SIP trunking integrations with a variety of third-party PBX, dialer, and contact center platforms. The most common platforms documented here include Avaya IP Office, Vicidial, OSDial, and GOautodial. Each integration follows a similar pattern: configure the Telnyx Mission Control Portal (purchase a DID, create a connection, provision the number, and create an outbound profile), then configure the third-party platform to register or peer with `sip.telnyx.com`.

Before starting any integration, ensure that your Telnyx Mission Control Portal account is set up correctly. It is also recommended to enable TLS to encrypt your traffic.

## Avaya IP Trunk Configuration

### Configuring an Avaya IP Trunk

To configure an Avaya IP trunk with Telnyx, complete the Avaya installation and telecommunication-applications deployment, configure the Telnyx Mission Control Portal, and provision a DID from Telnyx.

Under **IP Offices/Line**, add a SIP line with the following configurations:

**SIP Line**

```
Line Number: 100 (whichever number you have available)
ITSP Domain Name: sip.telnyx.com
URI Type: SIP
Location: Cloud
Prefix: 1 (whichever prefix you'd like to add)
In service: Enable
Check OOS: Enable
Refresh Method: Auto
Timer (seconds): On Demand
```

**Transport**

```
ITSP Proxy Address: sip.telnyx.com
Layer 4 Protocol: UDP
Send Port: 5060
Use Network Topology Info: LAN 2 (whichever LAN you have configured for SIP trunking)
Explicit DNS Server(s): Add your DNS Server
```

**SIP URI** — add a channel with the following configurations:

```
Via: 1.2.3.4 (1.2.3.4 = your public IP)
Local URI: *
Contact: *
Display Name: *
PAI: *
Registration: 0:
Incoming Group: 100 (Number added on SIP Line)
Outgoing Group: 100 (Number added on SIP Line)
Max Calls per Channel: 10
```

**Dial Plan** — under **IP Offices/Short Code**, add a Short Code with the following configurations:

```
Code: 9N; (you can use 9 or whatever number you want to dial to differentiate Telnyx trunk)
Feature: Dial
Telephone Number: 1N
Line Group: 100 (number added on SIP Line)
Locale: United States (US English)
```

To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. See the caller ID number policy for information on enabling a caller ID override from within the Telnyx portal.

Additional resources: [Avaya server support](https://support.avaya.com/products/P0956/common-servers).

### Configuring Telnyx SIP Trunking with Avaya IP Office 10

For Avaya IP Office 10 with the Avaya Session Border Controller for Enterprise Release 7.1 using UDP, Avaya has produced a detailed custom document for integration with Telnyx. If you experience difficulty with that document, reach out to Telnyx support.

Additional resources: [Avaya support](https://support.avaya.com/), [Avaya documentation](https://support.avaya.com/documents/), and [Avaya's Telnyx-specific documentation](https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf).

## Vicidial IP Trunk Configuration

Vicidial is an enterprise class, open source, contact center suite in use by many large call centers around the world, with over 14,000 registered installations in over 100 countries.

### Configure the Telnyx Mission Control Portal for Vicidial

**Purchase a number:**

1. Visit the **Numbers** page via the navigation menu on the left-hand side.
2. Select the **Search Numbers** tab.
3. Select your search type: NPA-NXX, Region, Toll Free, or Advanced.
4. Input your search criteria and click **Search**.
5. Results will display below.
6. Click **+ Add to Cart** to select the number(s) you'd like to purchase.
7. Click on the **Shopping Cart** to view your selected numbers and check out.
8. Once purchased, your numbers will be visible on the **My Numbers** tab within the **Numbers** page.

**Set up a connection:**

1. Visit the **Connections** page via the navigation menu on the left hand side.
2. Click the **Add Connection** button (located towards the top right corner).
3. Input a name for the connection.
4. Select **IP Address** for your Authentication Method and input the IP Address of your Vicidial instance. (For credentials-based authentication, select **Credentials** and input the desired user/password combination.)
5. Click the **Create** button to finish creating your connection.

**Provision your number (assign to a connection):**

1. Go back to the **Numbers** page via the navigation menu on the left hand side.
2. Select the **My Numbers** tab (you may have defaulted to this already).
3. Click the **Select Connection** drop-down next to your number. You should see the connection you just created — select it.
4. Your number is now all set on the portal.

**Create your outbound profile:**

1. Visit the Outbound section via the navigation menu on the left hand side.
2. Click the **+ Add Outbound Profile** button (located towards the top right corner).
3. Select the connection you created via the **Select Connection** drop-down.
4. Choose the **Traffic Type** and **Service Plan** that meets your needs.
5. Click **Add**.
6. You are now set up for outbound calling on the portal.

### Configure Vicidial

Log into the Vicidial web portal and go to **Admin → Carriers → Add new carrier**, then enter the following information:

1. **Carrier ID:** *TelnyxCarrier*
2. **Name:** *telnyxRegistration*
3. **String:** leave blank.
4. **Template ID:** *NONE*
5. **Account Entry:** *[telnyx]*
6. **Disallow:** All
7. **Allow:** *ulaw*
8. **Allow:** *g729*
9. **Type:** *peer* (for IP-based) or *friend* (for credentials-based)
10. **Insecure:** *port,invite* (IP-based only)
11. **Host:** [sip.telnyx.com](https://sip.telnyx.com)
12. **Username:** The username you set up in step 1 (credentials-based only)
13. **Password:** The password you set up in step 1 (credentials-based only)
14. **dtmf mode:** *rfc2833*
15. **Context:** *default*
16. **Protocol:** *SIP*
17. **Global String:** *Telnyx=SIP/telnyx*
18. **Dial Plan:**
    ```
    exten => _91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
    exten => _91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
    exten => _91NXXNXXXXXX,3,Hangup
    ```
    In this case, 9 is the prefix that will be dialed to send calls to Telnyx's trunk.

Depending on your phone configuration, you may also wish to configure an outbound caller ID to be in accordance with the caller ID number policy. This can be done on a per-user or per-campaign basis.

**To apply a per-user caller ID:**

1. Open the **Users** tab in the Vicidial administration portal.
2. Select **Modify** next to the relevant user.
3. Apply the desired outbound caller ID in the **Outbound CallerID** field.
4. Click **Submit**.

**To apply a caller ID on a campaign:**

1. Select the **Campaigns** tab in the Vicidial administration portal.
2. Select **Modify** next to the campaign you want to have the caller ID.
3. Click the **Detail** tab and apply the desired caller ID in the **Campaign CallerID** field.
4. Click **Submit**.

Additional resources: [Vicidial support](https://www.vicidial.com/?page_id=151), [Vicidial user manual](https://www.vicidial.org/download_survey.php) (free version; a [paid version](http://www.vicidial.org/store.php#MANAGER) is also available with higher resolution).
