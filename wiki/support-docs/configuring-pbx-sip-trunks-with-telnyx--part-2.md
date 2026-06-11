---
title: Configuring PBX SIP Trunks with Telnyx
summary: A consolidated guide for connecting enterprise PBX systems—including Cisco
  CUBE/CUCM, Cisco CME, Avaya, and Skype for Business—to Telnyx SIP trunks using either
  IP or credential-based authentication, covering dial-peer setup, codec preferences,
  NAT traversal, inbound routing, and platform-specific configuration steps.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
updated_at: 2026-06-11T11:24:50Z
---

# Configuring PBX SIP Trunks with Telnyx

*Part 2 of 2 — see also: [Part 1](configuring-pbx-sip-trunks-with-telnyx--part-1.md)*

A consolidated guide for connecting enterprise PBX systems—including Cisco CUBE/CUCM, Cisco CME, Avaya, and Skype for Business—to Telnyx SIP trunks using either IP or credential-based authentication, covering dial-peer setup, codec preferences, NAT traversal, inbound routing, and platform-specific configuration steps.

## Avaya

Telnyx supports SIP trunking with Avaya IP Office and Avaya Session Border Controller (SBC) for Enterprise. Avaya has published a [detailed custom integration document for Telnyx](https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf); if you experience difficulty, contact Telnyx support.

### Basic SIP Line Configuration (Avaya IP Office)

Under **IP Offices > Line**, add a SIP line with:

**SIP Line tab:**

- **Line Number:** 100 (or any available number)
- **ITSP Domain Name:** `sip.telnyx.com`
- **URI Type:** SIP
- **Location:** Cloud
- **Prefix:** 1 (or your preferred prefix)
- **In service:** Enabled
- **Check OOS:** Enabled
- **Refresh Method:** Auto
- **Timer (seconds):** On Demand

**Transport tab:**

- **ITSP Proxy Address:** `sip.telnyx.com`
- **Layer 4 Protocol:** UDP
- **Send Port:** 5060
- **Use Network Topology Info:** LAN 2 (or whichever LAN is configured for SIP trunking)
- **Explicit DNS Server(s):** Your DNS server

**SIP URI tab** — add a channel with:

- **Via:** Your public IP address
- **Local URI:** `*`
- **Contact:** `*`
- **Display Name:** `*`
- **PAI:** `*`
- **Registration:** 0
- **Incoming Group:** 100 (matches SIP Line number)
- **Outgoing Group:** 100 (matches SIP Line number)
- **Max Calls per Channel:** 10

**Dial Plan** — under **IP Offices > Short Code**, add:

- **Code:** `9N;` (or your chosen prefix to route via the Telnyx trunk)
- **Feature:** Dial
- **Telephone Number:** `1N`
- **Line Group:** 100
- **Locale:** United States (US English)

### Avaya IP Office 10 with SBC

For integrating Avaya IP Office 10 with Avaya Session Border Controller for Enterprise Release 7.1 using UDP, refer to [Avaya's Telnyx-specific documentation](https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf). Additional resources are available from [Avaya support](https://support.avaya.com/) and [Avaya documentation](https://support.avaya.com/documents/).

---

## Skype for Business

Skype for Business Server can be connected to a Telnyx SIP trunk using the Topology Builder. You need your SIP credentials, access to the [Skype for Business Topology Builder](https://learn.microsoft.com/en-us/skypeforbusiness/deploy/install/create-and-publish-new-topology), and must allow relevant traffic through your firewall.

### Connect Skype to a Telnyx SIP Trunk

1. Open **Skype for Business Server Topology Builder**.
2. Navigate to **Skype for Business Server > [your site name] > Shared Components**.
3. Right-click **PSTN gateways** and select **New IP/PSTN Gateway**.
4. On the **Define New IP/PSTN Gateway** screen, type `sip.telnyx.com` and click **Next**.
5. Leave **IPv4 – Use all configured IP addresses** at its default and click **Next**.
6. Define the root trunk with:
   - **Listening Port for IP/PSTN Gateway:** `5060`
   - **SIP Transport Protocol:** `TCP`
   - **Associated Mediation Server:** Select the Mediation Server pool
   - **Associated Mediation Server Port:** `5068` (default)
7. Click **Finish**.
8. Right-click the **Skype for Business Server** node and click **Publish Topology**.

### Create a Dial Plan

> **Important:** Back up your existing Enterprise Voice configuration before running any script. The example below is for a default environment with no existing voice settings.

Create a PowerShell script (`.ps1`) and run it in the Skype for Business Management Shell:

```powershell
Write-Host "Starting Telnyx Enterprise Voice example settings..."

# Add PSTN Usage
Write-Host "Adding PSTN Usage..."
Set-CsPstnUsage -Force -Usage @{add="US-Basic-PSTN-Usage"} | Out-Null

# Set Dial In Conference Region
Write-Host "Setting Dial Plan..."
Set-CsDialPlan -Identity "Global" -SimpleName "Global" -DialinConferencingRegion "US" | Out-Null

# Add Normalization Rules
Write-Host "Adding Normalization Rules..."
New-CsVoiceNormalizationRule -Name 'US-National' -Parent Global -Pattern '^1?([2-9]\d\d[2-9]\d{6})\d*(\D+\d+)?$' -Translation '+1$1' -Priority 0 -Description "National number normalization for United States" -WarningAction:SilentlyContinue | Out-Null
New-CsVoiceNormalizationRule -Name 'US-Service' -Parent Global -Pattern '^([2-9]11)$' -Translation '$1' -Priority 1 -Description "Service number normalization for United States" -WarningAction:SilentlyContinue | Out-Null
New-CsVoiceNormalizationRule -Name 'US-International' -Parent Global -Pattern '^(?:\+|011)(1|7|2[07]|3[0-46]|39\d|4[013-9]|5[1-8]|6[0-6]|8[1246]|9[0-58]|2[1235689]\d|24[013-9]|242\d|3[578]\d|42\d|5[09]\d|6[789]\d|8[035789]\d|9[679]\d)(?:0)?(\d{6,14})(\D+\d+)?$' -Translation '+$1$2' -Priority 2 -Description "International number normalization for United States" -WarningAction:SilentlyContinue | Out-Null

# Set Voice Policy
Write-Host "Setting Voice Policy..."
Set-CsVoicePolicy -Identity Global -AllowCallForwarding $true -AllowPSTNReRouting $true -AllowSimulRing $true -EnableBWPolicyOverride $false -EnableCallPark $true -EnableCallTransfer $true -EnableDelegation $true -EnableMaliciousCallTracing $true -EnableTeamCall $true -PstnUsages @{add="US-Basic-PSTN-Usage"} | Out-Null

# Add Voice Route
Write-Host "Adding Voice Route..."
New-CsVoiceRoute -Identity "US-Basic-Voice-Route" -NumberPattern ^+ -PstnGatewayList @{add="PstnGateway:sip.telnyx.com"} -PstnUsages @{add="US-Basic-PSTN-Usage"} -WarningAction:SilentlyContinue | Out-Null

# Update Trunk Configuration
Write-Host "Updating Trunk Configuration..."
Set-CsTrunkConfiguration -Identity Global -MaxEarlyDialogs 20 -SRTPMode "Optional" -ConcentratedTopology $true -EnableReferSupport $false | Out-Null

Write-Host "Configuration is done!"
```

### Deploy Cloud Connector Edition (Optional)

If deploying CCE, follow [Microsoft's CCE documentation](https://technet.microsoft.com/en-us/library/mt605228.aspx) and specify the following in the `.ini` file:

- **Voice Gateway 1 Make and Model:** Telnyx Telephony Engine
- **Voice Gateway 1 Name:** `sip.telnyx.com`
- **Voice Gateway 1 IP Address:** `192.76.120.10`
- **Voice Gateway 1 Port #:** `5060`
- **Voice Gateway 1 Protocol for SIP Traffic:** `TCP`
- **Enable REFER support:** `$false`
- Remove the section for the second gateway

For further reference, see [Microsoft support](https://www.microsoft.com/en-us/microsoft-365/support) and the [Skype for Business Topology documentation](https://learn.microsoft.com/en-us/skypeforbusiness/deploy/install/create-and-publish-new-topology).
