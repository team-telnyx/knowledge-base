---
title: Telnyx Microsoft Teams Integration
summary: 'Telnyx offers three methods to connect Microsoft Teams to the PSTN: Direct
  Routing via the Telnyx MS Teams SBC, the Call2Teams third-party add-on, and the
  Microsoft Operator Connect program. This page covers the setup procedures for each
  method, including prerequisites, step-by-step configuration, and troubleshooting
  for TLS and SIP Options warnings.'
sources:
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
  content_hash: 6c22049e56aeaf66305fdc6f791e3aad63069506ec6fdae47f5c1eb87a10f909
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
  content_hash: 92f97ce4469cd016a8dce219785a39266ac4804c29127c2d5795d706863fdff5
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
  content_hash: 88027e9394fea6ea14e98bd8746b70dcbc6bbfa80583984a6a9f5bb0ef8a7ed2
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
  content_hash: 28acc5d5e1ead9de17e8d34eb52b504d95abfd0702d87aea7eed635c00b3e504
updated_at: 2026-06-11T11:39:52Z
---

# Telnyx Microsoft Teams Integration

*Part 3 of 3 — see also: [Part 1](telnyx-microsoft-teams-integration--part-1.md), [Part 2](telnyx-microsoft-teams-integration--part-2.md)*

Telnyx offers three methods to connect Microsoft Teams to the PSTN: Direct Routing via the Telnyx MS Teams SBC, the Call2Teams third-party add-on, and the Microsoft Operator Connect program. This page covers the setup procedures for each method, including prerequisites, step-by-step configuration, and troubleshooting for TLS and SIP Options warnings.

## TLS and SIP Options Warnings (Direct Routing)

If you have an existing Direct Routing SBC setup, you may encounter warnings related to TLS connectivity and SIP Options status. These warnings do not impact call quality or reliability, but the following PowerShell-based configuration is recommended to resolve them.

### Prerequisites

Install PowerShell ([Windows instructions](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows), [macOS instructions](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-macos)).

### Connect to the Tenant

Launch PowerShell (run `PowerShell` in `cmd.exe` on Windows, or `pwsh` in Terminal on macOS), then:

```powershell
Import-Module MicrosoftTeams
Connect-MicrosoftTeams
```

A login window will prompt for credentials.

### Add PSTN Usage

```powershell
Set-CsOnlinePstnUsage -Identity Global -Usage @{Add="Telnyx"}
```

Verify with:

```powershell
Get-CSOnlinePSTNUsage
```

### Add a Voice Route

Replace `<string_from_the_telnyx_portal_connection>` with the subdomain shown in your Telnyx SIP connection:

```powershell
New-CsOnlineVoiceRoute -Name "Multi-Tenant" -Priority 1 -OnlinePSTNUsage "Telnyx" -OnlinePSTNGatewayList <string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech -NumberPattern '^(\+1[0-9]{10})$' -Description "Telnyx"
```

After this step, SIP OPTIONS checks on the tenant are replaced by the voice route.

### Add a Voice Routing Policy

```powershell
New-CsOnlineVoiceRoutingPolicy "Telnyx" -OnlinePstnUsages "Telnyx"
```

Grant the policy to a user:

```powershell
Grant-CsOnlineVoiceRoutingPolicy -Identity "<user_email>" -PolicyName "Telnyx"
```

Verify:

```powershell
Get-CsOnlineUser "<your_user>@<string_from_the_telnyx_portal_connection>.mstsbc.telnyx.tech" | select OnlineVoiceRoutingPolicy
```

### Configure User-Level Policies

In the Teams admin center, assign the following policies to each user:

- **Calling Policy** — Navigate to **Voice → Calling Policies**, create or select a policy, then assign it at **Users → [User] → Policies → Assigned policies → Calling policy**.
- **Dial Plan** — Navigate to **Voice → Dial Plans**, create or select a plan, then assign it at **Users → [User] → Policies → Assigned policies → Dial plan**.
- **Voice Routing Policy** — Navigate to **Voice → Voice Routing Policies**, then assign at **Users → [User] → Policies → Assigned policies → Voice Routing Policy** (use the policy created in PowerShell).

### Verify Enterprise Voice Status

Ensure the user is enabled for Enterprise Voice with a Direct Routing phone number:

```powershell
Get-CsOnlineUser -Identity "<user_email>"
```

Check that `EnterpriseVoiceEnabled` is `True` and `LineUri` contains the assigned phone number. It may take up to 30 minutes for changes to fully take effect.

---

## Testing and Validation

After completing setup with any integration method:

1. **Outbound test** — Call a PSTN number from the Microsoft Teams client. Confirm the call connects through Telnyx with two-way audio.
2. **Inbound test** — Call a Telnyx DID assigned to your Teams user from an external phone (e.g. a mobile). Confirm the call is received in Teams with two-way audio.
3. **Verify CDRs** — Check Call Detail Records in the **Reporting** section of the [Telnyx Mission Control Portal](https://portal.telnyx.com/) to validate both calls went through correctly.

If you encounter issues, contact [support@telnyx.com](mailto:support@telnyx.com) with the number dialled and the date/time.

---

## Additional Resources

- [Microsoft Teams Direct Routing documentation](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan)
- [Microsoft support](https://support.microsoft.com/en-US)
- [Call2Teams features and benefits for partners](https://www.call2teams.com/partners/)
- [E911 Setup Guide](e911-setup-guide.md)
- [Port your Microsoft MS Teams Numbers](port-your-microsoft-ms-teams-numbers.md)
