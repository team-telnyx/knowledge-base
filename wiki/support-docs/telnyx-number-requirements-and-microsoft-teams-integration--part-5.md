---
title: Telnyx Number Requirements and Microsoft Teams Integration
summary: This page consolidates Telnyx documentation covering DID number requirements
  for Reunion, Australia, and New Zealand, Australian emergency services and IPND,
  and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP
  warnings, Operator Connect, and emergency call routing.
sources:
- url: https://support.telnyx.com/en/articles/13720024-reunion-did-requirements
- url: https://support.telnyx.com/en/articles/3505912-australia-did-requirements
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/5466823-new-zealand-did-requirements
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-07-17T09:09:12Z
---

# Telnyx Number Requirements and Microsoft Teams Integration

*Part 5 of 6 — see also: [Part 1](telnyx-number-requirements-and-microsoft-teams-integration--part-1.md), [Part 2](telnyx-number-requirements-and-microsoft-teams-integration--part-2.md), [Part 3](telnyx-number-requirements-and-microsoft-teams-integration--part-3.md), [Part 4](telnyx-number-requirements-and-microsoft-teams-integration--part-4.md), [Part 6](telnyx-number-requirements-and-microsoft-teams-integration--part-6.md)*

This page consolidates Telnyx documentation covering DID number requirements for Reunion, Australia, and New Zealand, Australian emergency services and IPND, and Microsoft Teams integration guides including Direct Routing, Call2Teams, TLS/SIP warnings, Operator Connect, and emergency call routing.

## TLS & SIP Warnings for Teams

If you already have Microsoft Teams Direct Routing configured with an SBC, you may encounter warnings related to TLS connectivity and SIP Options status. While these warnings do not impact call quality or reliability, we recommend implementing the following setup to address any potential configuration issues and ensure an optimal experience.

First, you will need to have PowerShell installed. To install PowerShell on your Microsoft Windows computer, follow [this](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.4&viewFallbackFrom=powershell-7.3) article. To install PowerShell on your Mac, follow [this](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-macos?view=powershell-7.4&viewFallbackFrom=powershell-7.3) article.

### Run PowerShell in Microsoft Windows

Run *cmd.exe* and execute the following command:

```
PowerShell
```

### Run PowerShell in Mac

Run Mac Terminal and execute the following command:

```
pwsh
```

In PowerShell, import the Microsoft Teams module if you don't already have it by running the following command:

```
Import-Module MicrosoftTeams
```

Connect to the Customer tenant using the Teams module:

```
Connect-MicrosoftTeams
```

A window will pop up for the credentials to be inserted as any other time we login into the desired account.

### Add a new Online PSTN Usage

Execute the following command:

```
Set-CsOnlinePstnUsage -Identity Global -Usage @{Add="Telnyx"}
```

Verify that the usage was created by entering:

```
Get-CSOnlinePSTNUsage
```

### Add a new voice profile

Which uses the subdomain previously verified on the account. In this step, we are going to associate the existing subdomain auto-generated in the Telnyx SIP connection to the new Voice Profile.

Run the following command (tailored to your configuration):

```
New-CsOnlineVoiceRoute -Name "Multi-Tenant" -Priority 1 -OnlinePSTNUsage "Telnyx" -OnlinePSTNGatewayList <string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech -NumberPattern '^(\+1[0-9]{10})$' -Description "Telnyx"
```

From now on, on the customer tenant there are no OPTIONS to check, just the voice route.

### Add a new Routing Policy

To add a new Routing Policy run the following command (tailored to your configuration):

```
New-CsOnlineVoiceRoutingPolicy "Telnyx" -OnlinePstnUsages "Telnyx"
```

```
Grant-CsOnlineVoiceRoutingPolicy -Identity "<user_email>" -PolicyName "Telnyx"
```

To verify the Voice Routing Policy was correctly created and attached to the user you specified, run the following command:

```
Get-CsOnlineUser "<your_user>@<string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech" | select OnlineVoiceRoutingPolicy
```

### User Policy

- **CallingPolicy: Allow Calling** — Create a new Calling Policy in **Voice** > **Calling Policies** according to your needs. To associate a calling policy to a user go to **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned policies** > **Calling policy** > <**Name_of_your_Calling_Policy**>.
- **DialPlan:** Create a new Dialplan in **Voice** > **Dial Plans** according to your needs. Then associate it to the desired user in **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned policies** > **Dial plan** > <**Your_Dial_Plan_Name**>.
- **Voice routing policy:** This one is the one we created in PowerShell, which can also be consulted in **Voice** > **Voice Routing Policies**. Associate it to the user in **Users** > Select the user you want to allow to make calls > **Policies** > **Assigned policies** > **Voice Routing Policy** > <**Your_Voice_Routing_Policy_Name**>.

Ensure the user is enabled for Enterprise Voice with a Direct Routing Phone Number. To ensure that the user which you intend to make calls over Direct Routing has all the proper configurations in place, run the following command in PowerShell:

```
Get-CsOnlineUser -Identity "<user_email>"
```

It may take up to 30 minutes for the changes to be fully implemented and take effect.
