---
title: 'Telnyx SIP Connections: Failover, Routing, and Integrations'
summary: This page consolidates Telnyx SIP Connection configuration, failover, and
  retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection
  types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration
  (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware
  and sipXecs.
sources:
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
updated_at: 2026-07-17T09:07:44Z
---

# Telnyx SIP Connections: Failover, Routing, and Integrations

*Part 6 of 7 — see also: [Part 1](telnyx-sip-connections-failover-routing-and-integrations--part-1.md), [Part 2](telnyx-sip-connections-failover-routing-and-integrations--part-2.md), [Part 3](telnyx-sip-connections-failover-routing-and-integrations--part-3.md), [Part 4](telnyx-sip-connections-failover-routing-and-integrations--part-4.md), [Part 5](telnyx-sip-connections-failover-routing-and-integrations--part-5.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## Bicom PBXware Setup

[Bicom Systems](https://www.bicomsystems.com/) is a software suite that includes PBXware (an open standards turnkey telephony platform), SERVERware (server virtualization), sipPROT (SIP protection), gloCOM and gloCOM GO (unified communication apps), and sipMON (network packet sniffer for SIP and RTP). The SMS feature on Bicom PBXware allows users to select Telnyx as a provider in their configuration so that messaging service is fully utilized.

### Prerequisites

- Configure your Telnyx Mission Control Panel (set up a connection, provision a DID from Telnyx, create an outbound voice profile).
- Port your number to Telnyx.
- Set up hosted SMS with Telnyx.

### Configuration

Bicom Systems has created a [detailed custom document for integration with Telnyx](https://go.telnyx.com/rs/telnyx/images/Content_Guide_BicomPBXwareTelnyxconfiguration.pdf). If you experience difficulty with that document, contact Telnyx support.

## sipXecs PBX Setup

[SIPfoundry's sipXecs](http://www.sipfoundry.org/) is an open source unified communications and collaboration project — an all-software, open-source, modern communications PBX solution that scales to mid-size and large enterprise. This guide explains how to install a single server system; the first server can be extended into a large cluster later using the admin UI.

### Prerequisites

- Your Telnyx Portal must be correctly set up and configured for use.
- Have your SIP credentials (the username/password for your main SIP account or SIP sub-account).
- Have DIDs available to assign.
- Installed/configured a computer or virtual server to use as a test server:
  - **Physical server:** Dual or quad core CPU, 4 GB RAM (minimum), 40 GB hard drive (minimum), 1 network card. Install a minimum version of CentOS 6 or RHEL 6.
  - **Virtual machine:** Clean VM (e.g., Google or Amazon; avoid instances with CPanel such as VPS from Bluehost). Two compute cores, 2 to 4 GB RAM, 16 GB storage (excluding voicemail). Start from a minimum image of CentOS 6 or RHEL 6.
- A network segment — preferably a separate routed network segment so sipXecs can install and run its own DHCP server for phone auto-discovery and provisioning. If you can't do this, manually configure sipXecs as the FTP server on each phone.
- Phone hardware:
  - **Desk phones:** Polycom is preferred, but many other options exist.
  - **Softphones:** Counterpath Bria is preferred; Counterpath X-Lite, Linphone, and Jitsi also work.
  - **Mobile:** Counterpath Bria smartphone and tablet app (iPhone and Android); CSipSimple and SIPdroid also work.
- (Optional) PSTN connectivity via a PSTN gateway (Audiocodes is preferred) or with a SIP trunk.
- (Optional) Firewall for internet connectivity. For SIP trunking or connectivity to devices connected via the Internet, use a firewall/SBC. sipXecs Canary and newer no longer includes a built-in SBC for SIP trunking; Sangoma SBC is recommended for production deployments. Ingate, Audiocodes, and ACME Packet are also good choices.

### Step 1 — Install sipXecs

1. Log into your system as root or sudo to root.
2. Install sipXecs by running:

   ```
   bash -c "$(curl -L http://rpms.sipfoundry.org/canary-release/sipxecs-install)"
   ```

   Alternatively, use the `.repo` file to install the software. Install the repo file into `/etc/yum.repos.d`, then install the EPEL repository:

   ```
   yum install -y epel-release
   ```

   Then run:

   ```
   yum install sipxecs
   ```

   Once completed, run the `/usr/bin/sipxecs-setup` script.

### Step 2 — Configure Your First SIP Trunk

Run the `/usr/bin/sipxecs-setup` configuration script. You'll need to provide:

- **IP Address:** Make sure to take note of this — you'll need it in the next section.
- **Configure network:** *No* (if your network is configured already)
- **First server:** *Yes*
- **Host name:** Choose the hostname you'd like to use (e.g., `sipxecs`)
- **Domain:** `sip.telnyx.com`
- **SIP Domain:** `sip.telnyx.com`
- **SIP Realm:** Enter the name of the realm to which the SIP interface is connected

### Step 3 — Log Into the Admin Console

1. Open a browser and enter the IP address from Step 2 and hit **Enter**. Your browser will present a certificate warning — acknowledge it to go to the login screen.
2. Assign a password for the superadmin user, then log in as superadmin.

> **Note:** You'll need to enable the services your organization will require. Most services are disabled by default when you first log in. Navigate to **System → Servers** and enable the settings you'll need. You'll also need to add at least one user in order to start adding phones — navigate to **Users → Users** and click **Add New User**.

### Step 4 — Add Phones to sipXecs

> **Note:** You can add a phone to sipXecs but in order to make calls with it, it must be assigned to a user.

1. In the admin portal, navigate to **Users → Users** and click on the user you want to assign a phone.
2. From the user screen, click **Phones** in the lefthand menu.
3. If you configured sipXecs on an isolated subnet during installation, enabled the DHCP service, and enabled the Phone Auto-Provisioning service, you are all set for auto-discovery of supported devices. Reset the configuration of a phone (if it's not new), and plug it into the network segment. It should automatically pick up a default configuration and come up with a provisional line configured and registered. If you did not configure these settings, skip to step 6.
   - To find your auto-discovered devices, navigate to **Devices → Phones**.
4. Next, go to **Users → Phones** to provision a phone to a user and choose an existing but unassigned phone for the user by opening the **Add New Phone** dropdown dialogue and selecting the desired phone from the list.
   - sipXecs now generates a configuration profile with default parameters that make sense for this particular user.
5. Plug the phone into the network and restart it. Make sure the phone has the sipXecs server configured as its FTP server if DHCP does not provide it, and make sure the FTP service is enabled. The phone will now load the configuration profile.
   - Make sure you press the **Send Profile** button to generate the phone profile.
6. To manually configure a phone, go to the phone's configuration manager. The necessary parameters are typically:
   - **Account Name:** A friendly name for the account that only you see.
   - **User ID:** The user's numeric extension.
   - **Domain:** `sip.telnyx.com`
   - **Password:** The Telnyx account or sub-account password.
   - **Display Name:** This will end up being the caller ID. The name should be in capital letters, must not use special characters (spaces are allowed), and some Canadian providers will not show more than 15 characters.
   - **Auth Name:** The user's numeric extension.

### Step 5 — Add Supported Codecs

sipXecs supports any codec, so your only restriction is to use a Telnyx-supported codec:

- **Audio:** ulaw (g711u), alaw (g711a), g722, g729
- **Video:** H264

### Troubleshooting

If a manually configured phone isn't working, you likely have a DNS issue. Perform DNS tests by going to **System → DNS** and then selecting **Advisor**.
