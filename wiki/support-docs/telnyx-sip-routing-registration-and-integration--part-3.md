---
title: Telnyx SIP Routing, Registration, and Integration
summary: This page consolidates Telnyx documentation on SIP routing, registration,
  and integration. It covers how Telnyx handles SRV records for SIP calls, the components
  and flow of SIP registration, round-robin load balancing across connection IPs,
  the role of Via and Record-Route headers in preventing call drops, and step-by-step
  configuration guides for connecting Skype for Business, Voice Elements, and Genesys
  Cloud to Telnyx SIP trunks.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-07-17T09:00:56Z
---

# Telnyx SIP Routing, Registration, and Integration

*Part 3 of 4 — see also: [Part 1](telnyx-sip-routing-registration-and-integration--part-1.md), [Part 2](telnyx-sip-routing-registration-and-integration--part-2.md), [Part 4](telnyx-sip-routing-registration-and-integration--part-4.md)*

This page consolidates Telnyx documentation on SIP routing, registration, and integration. It covers how Telnyx handles SRV records for SIP calls, the components and flow of SIP registration, round-robin load balancing across connection IPs, the role of Via and Record-Route headers in preventing call drops, and step-by-step configuration guides for connecting Skype for Business, Voice Elements, and Genesys Cloud to Telnyx SIP trunks.

## Configuring Skype for Business Server with Telnyx

Skype for Business was an enterprise software application for instant messaging and videotelephony developed by Microsoft as part of the Microsoft Office suite, designed for use with the on-premises Skype for Business Server software and a SaaS version offered as part of Office 365.

### Prerequisites

- Telnyx Portal correctly set up and configured for use.
- SIP credentials (username/password for the main SIP account or SIP sub-account).
- Access to Skype for Business Topology Builder.
- Firewall configured to allow Telnyx SIP trunk traffic.

### Connect Skype to a Telnyx SIP Trunk

1. Start Skype for Business Topology Builder.
2. Navigate to **Skype for Business Server > [your site name] > Shared Components**.
3. Right-click the **PSTN gateways** node and click **New IP/PSTN Gateway**.
4. On the **Define New IP/PSTN Gateway** screen, type `sip.telnyx.com` and click **Next**.
5. Leave **IPv4 – Use all configured IP addresses** with its default value and click **Next**.
6. Define the root trunk for the PSTN gateway:
   - **Listening Port for IP/PSTN Gateway:** `5060`
   - **SIP Transport Protocol:** `TCP`
   - **Associated Mediation Server:** select the Mediation Server pool to associate with the root trunk
   - **Associated Mediation Server Port:** `5068` (default)
7. Click **Finish**.
8. Right-click the **Skype for Business Server** node and click **Publish Topology**.

### Create a Dial Plan

A PowerShell script example is provided that adds a PSTN usage (`US-Basic-PSTN-Usage`), sets the dial plan, adds US normalization rules (national, service, international), sets the voice policy, adds a voice route (`US-Basic-Voice-Route`) using `sip.telnyx.com` as the PSTN gateway, and updates the trunk configuration (MaxEarlyDialogs 20, SRTPMode Optional, ConcentratedTopology true, EnableReferSupport false). Save the script with a `.ps1` extension and run it from the Skype for Business Management Shell.

### (Optional) Deploy Cloud Connector Edition

If deploying CCE, specify the following in the `.ini` file:

- **Voice Gateway 1 Make and Model:** Telnyx Telephony Engine
- **Voice Gateway 1 Name:** `sip.telnyx.com`
- **Voice Gateway 1 IP Address:** `192.76.120.10`
- **Voice Gateway 1 Port #:** `5060`
- **Voice Gateway 1 Protocol for SIP Traffic:** `TCP`
- **Enable REFER support:** `$false`
- Remove the section in the `.ini` file for the second gateway.

## Configuring Voice Elements with Telnyx

Voice Elements is a Microsoft .NET development environment for building automated telephone systems, released by Inventive Labs Corporation in 2008. It is used by software developers working in C#, VB.NET, or Delphi to write telephony-based applications such as IVR systems, voice dialers, auto attendants, and call centers.

### Prerequisites

- Telnyx Portal correctly set up and configured for use.
- Voice Elements downloaded and installed.
- (Optional) TLS encryption enabled in the Telnyx portal if using TLS.

### Create a Telnyx SIP Trunk in Voice Elements

1. Open the Voice Elements wizard and select the **Connectivity** tab.
2. In the **Carrier/Gateway/Devices** section, select **Other**.
3. In the **Location** section, select **External IP Authentication (SIP Carrier - Preferred)**.
4. Enter Telnyx's connection information:
   - **Destination IP/URL:** `sip.telnyx.com` (in the USA; use the appropriate top-level domain for other countries)
   - Public and local IPs will be populated automatically.
5. Provide additional information:
   - **Registrar IP/URL:** `sip:sip.telnyx.com`
   - **AuthURI:** `your_telnyx_username@sip.telnyx.com`
   - **Username:** the SIP connection username
   - **Pwd:** the SIP connection password
   - **Ports:** use port 5060 for UDP or TCP; use port 5061 for TLS (and ensure the portal is configured accordingly).

### Test the Firewall

Using a firewall with any external service is critical. SIP sniffers are bots that seek out SIP servers on the internet and try to break in hoping to find weaknesses that would allow them to place free calls. It is highly recommended to only permit Telnyx IP addresses to have access to the SIP port.

## Configuring BYOC with Telnyx and Genesys Cloud

This guide provides instructions and technical details for configuring SIP trunk connectivity between Genesys Cloud and Telnyx.

### Prerequisites

- A Telnyx account.
- Completed L2 verification.
- A purchased number to be used for voice calls.

### Creating a SIP Connection in Telnyx

1. In the Telnyx Mission Control Portal, navigate to the **Voice** tab and select **SIP Trunking**.
2. Click **Add SIP Connection**.
3. Name the SIP connection for easy identification.
4. Choose **FQDN** as the SIP connection type and provide the SIP URI to the Genesys Cloud organization. The domain should match the region of the Genesys Cloud deployment. Click **have FQDN** to update the FQDN setting.
5. In the **Outbound** section, choose **Credentials** and provide a username and password for digest authentication.
6. Click **Save & Finish Editing**.

### Creating an Outbound Voice Profile

1. Navigate to the **Outbound Voice Profiles** tab in the **Voice** section.
2. Click **Add New Profile**.
3. Provide a name and click **Create**.
4. Select individual countries or regions to be allowed for voice calls and click **Save**.
5. Return to the SIP Connection, edit the configuration, select the **Outbound** tab, and choose the newly created Outbound Voice Profile from the dropdown.
6. Switch to the **Inbound** tab and adjust DNIS and ANI number formats to match the Genesys Cloud configuration, then save.

### Number Configuration

In the **Numbers** section under **My Numbers**, select a configured SIP Connection from the dropdown for the purchased number. The same SIP connection can be assigned to multiple numbers.

### Configuration in Genesys Cloud

Before starting, ensure that:

- The BYOC option is enabled in the Genesys Cloud organization.
- You have admin rights to set up Trunks.
- A number is purchased and added to DID Numbers and routed correctly (for example, to the Architect flow).

#### Create a SIP Trunk

1. Go to **Admin** and select **Trunks**.
2. Provide a name for the SIP trunk and choose **BYOC Carrier** as the SIP trunk type.
3. Select **Generic BYOC Carrier** as the subtype.
4. Provide a name for the SIP Trunk and the Inbound SIP Termination Identifier. This name should match the one configured in the Telnyx SIP Connection for the FQDN option.
5. Provide the Telnyx SIP interface URL in **SIP Servers and Proxies** based on the chosen region (e.g. `sip.telnyx.com`, `sip.telnyx.eu`).
6. Enable **Digest Authentication** and provide the same URL in the **Realm** field as used for the SIP proxy.
7. Provide the **User Name** and **Password** configured in the Telnyx SIP Connection.
8. Set **Caller ID** with a number purchased on the Telnyx platform.
9. In the **SIP Access Control** section, provide the IP addresses of the chosen Telnyx SIP endpoints.
10. Under **External Trunk Configuration**, expand the **Protocol** menu, scroll to **Outbound**, and add a custom SIP header `X-Telnyx-Username` with the same value as set for Digest Authentication.

### Troubleshooting

Debugging tools are available in the Telnyx Mission Control Portal to troubleshoot SIP trunk communication, including SIP call flows, QoS stats, and webhook communication.

1. Navigate to **Debugging** under **Reporting** in the sidebar.
2. Select **SIP Call Flow Tool** in the top bar.
3. Specify search criteria and click **Search CDRs**.
4. From the list of calls, select one with the **Call Data Debugging** button to review the SIP Call Flow with detailed data for each SIP Request.
5. Check **Session Info** on the next tab or export PCAP data on the **Export** tab for sharing with the team.
