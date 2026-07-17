---
title: Telnyx SIP Trunking Configuration
summary: Telnyx SIP Trunking lets you use Telnyx as your inbound and outbound voice
  carrier with a compatible softphone, PBX, or contact center platform. This page
  consolidates the core configuration workflow (account setup, number purchase, SIP
  connection, authentication method, AnchorSite, and Outbound Voice Profile), explains
  the ~1–3 second configuration propagation window, and provides step-by-step integration
  guides for Avaya IP Office and Vicidial (both IP-based and credentials-based), along
  with pointers to the broader library of vendor configuration guides.
sources:
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
updated_at: 2026-07-17T09:03:27Z
---

# Telnyx SIP Trunking Configuration

*Part 2 of 3 — see also: [Part 1](telnyx-sip-trunking-configuration--part-1.md), [Part 3](telnyx-sip-trunking-configuration--part-3.md)*

Telnyx SIP Trunking lets you use Telnyx as your inbound and outbound voice carrier with a compatible softphone, PBX, or contact center platform. This page consolidates the core configuration workflow (account setup, number purchase, SIP connection, authentication method, AnchorSite, and Outbound Voice Profile), explains the ~1–3 second configuration propagation window, and provides step-by-step integration guides for Avaya IP Office and Vicidial (both IP-based and credentials-based), along with pointers to the broader library of vendor configuration guides.

## Avaya IP Trunk Configuration

Avaya is one of Telnyx's vendors that creates custom integration documentation. There are two supported approaches depending on your Avaya deployment.

### Configuring an Avaya IP Trunk (generic)

**Pre-requisites**

- Completed your Avaya installation and telecommunication-applications deployment.
- Configured your Telnyx Mission Control Portal.
- Provisioned a DID from Telnyx.

**Create your SIP line**

Under **IP Offices/Line**, add a SIP line with the following configurations.

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

> **Note:** To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.

### Configuring Telnyx SIP Trunking with Avaya IP Office 10 + Avaya SBC

This configuration covers Avaya IP Office 10 and Avaya Session Border Controller for Enterprise Release 7.1 using UDP.

**Pre-requisites**

- Ensure that your Telnyx Mission Control Portal is configured properly.
- Provision a DID from Telnyx.

> **Important:** Avaya has created a [detailed custom document for integration with Telnyx](https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf). If you experience difficulty with this document, please reach out to Telnyx support.

Additional resources:

- [Avaya support](https://support.avaya.com/)
- [Avaya documentation](https://support.avaya.com/documents/)
- [Avaya's Telnyx-specific documentation](https://www.dropbox.com/s/dswla4vbjbzdnfd/Application%20Notes%20for%20Configuring%20Telnyx%20SIP%20Trunking%20Service%20with%20Avaya%20IP%20Office%2010%20and%20Avaya%20Session%20Border%20Controller%20for%20Enterprise%20Release%207.1%20Using%20UDP.doc?dl=0)

## Vicidial IP Trunk Configuration

[Vicidial](https://www.vicidial.com/?p=470) is an enterprise-class, open-source contact center suite with over 14,000 registered installations in more than 100 countries. Telnyx supports both IP-based and credentials-based Vicidial trunks.

### Configure the Telnyx Mission Control Portal for Vicidial

**Purchase a number**

1. Visit the **Numbers** page via the left-hand navigation menu.
2. Select the **Search Numbers** tab.
3. Select your search type (NPA-NXX, Region, Toll Free, or Advanced).
4. Input your search criteria and click **Search**.
5. Click **+ Add to Cart** to select the number(s) you'd like to purchase.
6. Open the **Shopping Cart** to view your selected numbers and check out.
7. Once purchased, your numbers will be visible on the **My Numbers** tab.

**Set up a connection**

1. Visit the **Connections** page via the left-hand navigation menu.
2. Click the **Add Connection** button (top right).
3. Input a name for the connection.
4. For an **IP-based trunk**, select **IP Address** as the Authentication Method and input the IP address of your Vicidial instance. For a **credentials-based trunk**, select **Credentials** and input the desired username/password combination.
5. Click **Create**.

**Provision your number (assign to a connection)**

1. Go back to the **Numbers** page.
2. Select the **My Numbers** tab.
3. Click the **Select Connection** drop-down next to your number and select the connection you just created.

**Create your outbound profile**

1. Visit the **Outbound** section via the left-hand navigation menu.
2. Click the **+ Add Outbound Profile** button (top right).
3. Select the connection you created via the **Select Connection** drop-down.
4. Choose the **Traffic Type** and **Service Plan** that meet your needs.
5. Click **Add**.

### Configure Vicidial

Log into the Vicidial web portal and go to **Admin → Carriers → Add new carrier**, then enter the following information.

**IP-based trunk**

| Field | Value |
| --- | --- |
| Carrier ID | `TelnyxCarrier` |
| Name | `telnyxRegistration` |
| String | leave blank |
| Template ID | `NONE` |
| Account Entry | `[telnyx]` |
| Disallow | All |
| Allow | `ulaw` |
| Allow | `g729` |
| Type | `peer` |
| Insecure | `port,invite` |
| Host | `sip.telnyx.com` |
| dtmf mode | `rfc2833` |
| Context | `default` |
| Protocol | `SIP` |
| Global String | `Telnyx=SIP/telnyx` |

**Credentials-based trunk**

| Field | Value |
| --- | --- |
| Carrier ID | `TelnyxCarrier` |
| Name | `telnyxRegistration` |
| String | leave blank |
| Template ID | `NONE` |
| Account Entry | `[telnyx]` |
| Disallow | All |
| Allow | `ulaw` |
| Allow | `g729` |
| Type | `friend` |
| Host | `sip.telnyx.com` |
| Username | The username you set up in step 1 |
| Password | The password you set up in step 1 |
| dtmf mode | `rfc2833` |
| Context | `default` |
| Protocol | `SIP` |
| Global String | `Telnyx=SIP/telnyx` |

**Dial Plan (both variants)**

```
exten => _91NXXNXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _91NXXNXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _91NXXNXXXXXX,3,Hangup
```

In this case, `9` is the prefix that will be dialed to send calls to Telnyx's trunk.

### Outbound caller ID for Vicidial

Depending on your phone configuration, you may also wish to configure an outbound caller ID in accordance with the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy). You can do this on a per-user or per-campaign basis.

**Per-user caller ID**

1. Open the **Users** tab in the Vicidial administration portal.
2. Select **Modify** next to the relevant user.
3. Apply the desired outbound caller ID in the **Outbound CallerID** field.
4. Click **Submit**.

**Per-campaign caller ID**

1. Select the **Campaigns** tab in the Vicidial administration portal.
2. Select **Modify** next to the campaign you want to have the caller ID.
3. Click the **Detail** tab and apply the desired caller ID in the **Campaign CallerID** field.
4. Click **Submit**.
