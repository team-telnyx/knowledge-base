---
title: Telnyx Porting, Messaging Compliance, and Account Management
summary: This page consolidates Telnyx guidance on porting numbers from Skype and
  VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts,
  configuring Skype for Business SIP trunks, toll-free messaging verification and
  opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling
  toll-free carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-08-05T13:26:16Z
---

# Telnyx Porting, Messaging Compliance, and Account Management

*Part 2 of 5 — see also: [Part 1](telnyx-porting-messaging-compliance-and-account-management--part-1.md), [Part 3](telnyx-porting-messaging-compliance-and-account-management--part-3.md), [Part 4](telnyx-porting-messaging-compliance-and-account-management--part-4.md), [Part 5](telnyx-porting-messaging-compliance-and-account-management--part-5.md)*

This page consolidates Telnyx guidance on porting numbers from Skype and VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts, configuring Skype for Business SIP trunks, toll-free messaging verification and opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling toll-free carrier rejections.

## Configuring Skype for Business Server SIP Trunk with Telnyx

Skype for Business was an enterprise software application for instant messaging and videotelephony developed by Microsoft as part of the Microsoft Office suite, designed for use with the on-premises Skype for Business Server software and a SaaS version offered as part of Office 365.

### Pre-requisites

- Your Telnyx Portal must be correctly set up and configured for use
- Have your SIP credentials (username/password for your main SIP account or SIP sub-account)
- Have access to Skype for Business Topology Builder
- Allow Telnyx SIP trunk traffic on your firewall

### Step 1: Connect Skype to a Telnyx SIP Trunk

1. Start Skype for Business Topology Builder (Start > type *Skype for Business Server* > click the application).
2. Navigate to Skype for Business Server > [your site name] > Shared Components.
3. Right-click the PSTN gateways node and select **New IP/PSTN Gateway**.
4. On the Define New IP/PSTN Gateway screen, type `sip.telnyx.com` and click **Next**.
5. Leave IPv4 – Use all configured IP addresses with its default value and click **Next**.
6. Define a root trunk for the PSTN gateway with the following values:
   - **Listening Port for IP/PSTN Gateway:** `5060`
   - **SIP Transport Protocol:** `TCP`
   - **Associated Mediation Server:** select the Mediation Server pool to associate with the root trunk
   - **Associated Mediation Server Port:** `5068` (default)
7. Click **Finish**.
8. Right-click the Skype for Business Server node and select **Publish Topology**.

### Step 2: Create a Dial Plan

Create a dial plan, voice policy, call route, PSTN usage, and trunk configuration. A custom configuration based on your location and company policies is recommended; the provided script is a basic example for a default environment with no voice settings.

Before running the script, ensure a PSTN gateway has been defined in your topology for the selected site and that your existing Enterprise Voice configuration has been backed up.

Save the following script with a `.ps1` extension and run it from Skype for Business Management Shell:

```
Write-Host "Starting Telnyx Enterprise Voice example settings..."

#Add PSTN Usage
Write-Host "Adding PSTN Usage..."
Set-CsPstnUsage -Force -Usage @{add="US-Basic-PSTN-Usage"}  | Out-Null

#Set Dial In Conference Region
Write-Host "Setting Dial Plan..."
Set-CsDialPlan -Identity "Global" -SimpleName "Global" -DialinConferencingRegion "US"  | Out-Null

#Add Normalization Rules
Write-Host "Adding Normalization Rules..."
New-CsVoiceNormalizationRule -Name 'US-National' -Parent Global -Pattern '^1?([2-9]\d\d[2-9]\d{6})\d*(\D+\d+)?$' -Translation '+1$1' -Priority 0 -Description "National number normalization for United States" -WarningAction:SilentlyContinue | Out-Null
New-CsVoiceNormalizationRule -Name 'US-Service' -Parent Global -Pattern '^([2-9]11)$' -Translation '$1' -Priority 1 -Description "Service number normalization for United States" -WarningAction:SilentlyContinue | Out-Null
New-CsVoiceNormalizationRule -Name 'US-International' -Parent Global -Pattern '^(?:\+|011)(1|7|2[07]|3[0-46]|39\d|4[013-9]|5[1-8]|6[0-6]|8[1246]|9[0-58]|2[1235689]\d|24[013-9]|242\d|3[578]\d|42\d|5[09]\d|6[789]\d|8[035789]\d|9[679]\d)(?:0)?(\d{6,14})(\D+\d+)?$' -Translation '+$1$2' -Priority 2 -Description "International number normalization for United States" -WarningAction:SilentlyContinue | Out-Null

#Set Voice Policy
Write-Host "Setting Voice Policy..."
Set-CsVoicePolicy -Identity Global -AllowCallForwarding $true -AllowPSTNReRouting $true -AllowSimulRing $true -EnableBWPolicyOverride $false -EnableCallPark $true -EnableCallTransfer $true -EnableDelegation $true -EnableMaliciousCallTracing $true -EnableTeamCall $true -PstnUsages @{add="US-Basic-PSTN-Usage"}  | Out-Null

#Add Voice Route
Write-Host "Adding Voice Route..."
New-CsVoiceRoute -Identity "US-Basic-Voice-Route" -NumberPattern ^+ -PstnGatewayList @{add="PstnGateway:sip.telnyx.com"} -PstnUsages @{add="US-Basic-PSTN-Usage"} -WarningAction:SilentlyContinue | Out-Null

#Update Trunk Configuration
Write-Host "Updating Trunk Configuration..."
Set-CsTrunkConfiguration -Identity Global -MaxEarlyDialogs 20 -SRTPMode "Optional" -ConcentratedTopology $true -EnableReferSupport $false  | Out-Null

#Job is done
Write-Host "Configuration is done!"
```

### Step 3: (Optional) Deploy Cloud Connector Edition

If deploying CCE, follow Microsoft's documentation before proceeding. In the `.ini` file, specify:

- **Voice Gateway 1 Make and Model:** Telnyx Telephony Engine
- **Voice Gateway 1 Name:** `sip.telnyx.com`
- **Voice Gateway 1 IP Address:** `192.76.120.10`
- **Voice Gateway 1 Port #:** `5060`
- **Voice Gateway 1 Protocol for SIP Traffic:** TCP
- **Enable REFER support:** `$false`
- Remove the section in the `.ini` file for the second gateway
