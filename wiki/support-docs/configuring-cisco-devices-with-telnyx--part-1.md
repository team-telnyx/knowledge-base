---
title: Configuring Cisco Devices with Telnyx
summary: Learn how to configure Cisco SPA112/122 ATA adapters and Cisco 68xx/88xx
  series IP phones to work with Telnyx, including SIP registration, NAT traversal,
  codec selection, and optional TLS encryption.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
updated_at: 2026-06-11T11:26:53Z
---

# Configuring Cisco Devices with Telnyx

*Part 1 of 2 — see also: [Part 2](configuring-cisco-devices-with-telnyx--part-2.md)*

Learn how to configure Cisco SPA112/122 ATA adapters and Cisco 68xx/88xx series IP phones to work with Telnyx, including SIP registration, NAT traversal, codec selection, and optional TLS encryption.

## Prerequisites

Before configuring your Cisco device, ensure the following:

- Your device is running the latest firmware. For the SPA112/122, download updates from [Cisco SPA112](https://software.cisco.com/download/home/283998771/type) or [Cisco SPA122](https://software.cisco.com/download/home/283998793/type). For 68xx/88xx phones, check the [Status tab → System Information](https://www.cisco.com/c/en/us/support/docs/smb/unified-communications/cisco-small-business-voice-gateways-and-atas/smb2676-firmware-upgrade-on-spa112-and-spa122.html) on the device.
- You have a [phone number](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) in your Telnyx account.
- You have [configured a connection](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection) and [assigned your number to it](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection).
- You have [configured an outbound voice profile](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles) and assigned your connection to it.
- Your [Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) is properly set up.

> **Note on the SPA112/122:** This product reached its end-of-sale date with end-of-life announced by Cisco in 2019. Basic support continues until 2025. See [Cisco's SPA end-of-life documentation](https://www.cisco.com/c/en/us/products/collateral/unified-communications/small-business-voice-gateways-ata/eos-eol-notice-c51-743206.html) for details.

> **Browser note:** Issues have been reported when using Firefox to configure the SPA112/122. Use Chrome or Internet Explorer instead.

## Accessing the Device Configuration

### Cisco SPA112/122 ATA

1. Physically connect the device to your network through your router.
2. Open a web browser (Chrome or IE) and navigate to your router's admin page (typically `192.168.0.1` or `192.168.1.1`). Log in with your router credentials.
3. Find the list of connected devices and locate the Cisco SPA112 or SPA122 entry. Note its internal IP address.
4. Enter that IP address in your browser to open the Phone Adapter Configuration Utility.
5. Log in with the default credentials — **Username:** `admin`, **Password:** `admin` — and change these immediately.

> **Note:** For the SPA122, if one IP address does not open the Configuration Utility or opens it with limited functionality, try the other listed address.

### Cisco 68xx/88xx IP Phone

1. On the phone, press the **Menu** button and navigate to **Network Status > IPv4 Address**. Note the IP address.
2. On a computer on the same network, open a browser and enter `http://` followed by the phone's IP address.
3. On first login, you can skip the credentials by pressing **Skip**.

## Configuring Telnyx Mission Control Portal (SPA112/122)

For the SPA112/122, you must adjust inbound settings so that the ATA receives calls correctly:

1. Log into the [Telnyx Mission Control Portal](https://portal.telnyx.com/#/app/connections).
2. Navigate to your connection's **Inbound** tab on the **Connection Options** screen.
3. Set **Number Format (DNIS):** to **SIP Username**. ATAs require inbound calls to be sent to the username configured on the device. Since Telnyx does not support phone numbers as connection usernames, sending calls to the alphanumeric username of the connection ensures they reach your ATA.
4. Click **Save**.

## SIP and Proxy Settings

### Cisco SPA112/122 ATA — Quick Setup and SIP Tab

1. Go to the **Voice** tab → **SIP** sub-tab and set:
   - **STUN Enable:** Yes
   - **STUN Server:** `stun.telnyx.com`
   - **STUN Test Enable:** Yes
   - Click **Submit**.

2. Go to the **Quick Setup** tab and set:
   - **Proxy:** `sip.telnyx.com`
   - **Display Name:** Your DID (e.g., `12245181471`). Some firmware versions incorrectly send the Display Name in the registration; if registration fails, clear this field and configure a Caller ID override on your connection's outbound settings instead.
   - **User ID:** Your SIP username (matching the connection in your portal).
   - **Password:** Your SIP password (matching the connection in your portal).
   - **Dial Plan:** See [Linksys Dialplan for ATAs](linksys-dialplan-for-atas.md).
   - Click **Submit**.

3. On the **Voice** tab → **Line 1** (or your chosen line), under **Proxy and Registration**, set:
   - **Proxy:** `sip.telnyx.com`
   - **Register Expires:** 300
   - **Proxy Fallback Intvl:** 300
   - **Register:** Yes
   - **Use DNS SRV:** No
   - **DNS SRV Auto Prefix:** No

### Cisco 68xx/88xx — SIP Extension

1. Go to the **Voice** tab and click the extension you want to configure.
2. Under **Proxy and Registration**, set:
   - **Proxy:** `sip.telnyx.com`
   - **Outbound Proxy:** `sip.telnyx.com`
   - **Register:** Yes
   - **Register Expires:** 300
3. Under **Subscriber Information**, set:
   - **Display Name:** Your caller ID. Use capital letters for visibility, no special characters (spaces allowed), and keep it under 15 characters for Canadian provider compatibility.
   - **User ID:** Your Telnyx account ID
   - **Password:** Your Telnyx account password
   - **Auth ID:** Your Telnyx account ID

## NAT Settings

Both device families require NAT settings if your environment uses NAT.

- **NAT Mapping Enable:** Yes
- **NAT Keep Alive Enable:** Yes

If your environment does not use NAT, leave these disabled.

For the SPA112/122, these are found under **Voice** → **Line 1** → **NAT Settings**. For the 68xx/88xx, they are under **Voice** → **Extension** → **General and NAT Settings**.

Also ensure **Line Enable** is set to **Yes** on both device types.

## SIP Port and Transport

- **Without TLS:** SIP Transport = UDP or TCP, SIP Port = `5060`
- **With TLS:** SIP Transport = TLS, SIP Port = `5061`

## Audio Codecs

Both device families support the following [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality), listed in recommended priority:

1. g711u (ulaw)
2. g711a (alaw)
3. g722
4. g729

On the SPA112/122, verify codecs under **Voice** → **Line 1** → **Audio Configuration**. On the 68xx/88xx, configure them under **Voice** → **Extension** → **Audio Configuration** in your preferred priority order.

### T.38 Fax (SPA112/122 Only)

If you need fax support on the SPA112/122, stay on the **Voice** tab and under **Audio Configuration** set **Fax Enable T38:** Yes.

## Dial Plan (SPA112/122 Only)

On the SPA112/122, verify the dial plan under **Voice** → **Line 1** → **Dial Plan** matches what you configured in the Quick Setup tab. Refer to [Linksys Dialplan for ATAs](linksys-dialplan-for-atas.md) for details.

## Optional: Audio Optimization (SPA112/122 Only)

Cisco's default SIP T1 value (0.5 sec) and RTP packet size (0.030) can cause choppy audio over high-latency connections. To mitigate:

1. Under **Voice** → **SIP Timer Values (sec)**, set **SIP T1:** 1
2. Under **RTP Parameters**, set:
   - **RTP Packet Size:** 0.02
   - **RTP Port Min:** 10000
   - **RTP Port Max:** 20000
