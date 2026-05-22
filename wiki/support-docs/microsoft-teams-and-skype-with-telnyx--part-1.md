---
title: Microsoft Teams and Skype with Telnyx
summary: 'End-to-end guide to connect Microsoft Teams and Skype for Business to Telnyx
  for PSTN calling: Direct Routing via the Telnyx integrated SBC, Operator Connect,
  Call2Teams, Skype for Business SIP trunking, number porting from Skype/Teams, TLS/SIP
  warning remediation, and emergency calling behavior with Dynamic Location Routing.'
sources:
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-05-20T15:02:24Z
---

# Microsoft Teams and Skype with Telnyx

*Part 1 of 2 — see also: [Part 2](microsoft-teams-and-skype-with-telnyx--part-2.md)*

End-to-end guide to connect Microsoft Teams and Skype for Business to Telnyx for PSTN calling: Direct Routing via the Telnyx integrated SBC, Operator Connect, Call2Teams, Skype for Business SIP trunking, number porting from Skype/Teams, TLS/SIP warning remediation, and emergency calling behavior with Dynamic Location Routing.

## Prerequisites and licensing
- Telnyx Mission Control Portal account with at least one purchased number: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Microsoft 365 tenant with Global Administrator privileges.
- Licensing (minimums):
  - Direct Routing: Microsoft 365/Office 365 E5, or E1/E3/F3/A1/A3 + Phone System add-on.
  - Operator Connect: Microsoft Teams Phone license for at least one user.
- Teams Admin Center access: https://admin.teams.microsoft.com/

## Integration options at a glance
- Direct Routing (recommended for full control): Uses the Telnyx integrated SBC (subdomain under mstsbc.telnyx.tech) to connect Teams to the Telnyx telephony platform.
- Operator Connect: Native Microsoft integration; configure in Telnyx and Teams admin portals and assign numbers without SBC management.
- Call2Teams: Third-party add-on that bridges Teams to any PBX/SIP trunk, including Telnyx.
- Skype for Business Server (on‑prem): SIP trunk to Telnyx for legacy SfB deployments.

## Direct Routing with the Telnyx integrated SBC
Note: The Telnyx MS Teams SBC uses subdomains of mstsbc.telnyx.tech and token-based authentication: https://telnyx.com/resources/integrated-sbc-direct-routing

1) Create the MS Teams SBC SIP Connection in Telnyx
- Portal: Connections > Create SIP Connection > Type: MS Teams Direct Routing SBC. Note the auto-generated subdomain (xxxxx.mstsbc.telnyx.tech). Configure Authentication, Routing, and Inbound/Outbound settings as needed.
- Assign your Telnyx number to this connection in the Numbers section.

2) Verify the SBC subdomain in Microsoft 365
- Microsoft 365 Admin Center > Settings > Domains > Add domain: enter the auto-generated subdomain.
- Choose Add a TXT record instead, copy the TXT value Microsoft shows.
- Back in Telnyx SIP Connection > Domain Validation: paste the TXT value (do not include “.mstsbc.telnyx.tech” in TXT name fields).
- Save in Telnyx, then Verify in Microsoft 365. Skip DNS setup tasks and finish.
- Activate the domain: create a temporary user using the new subdomain and assign an E5 license (you can remove later once Direct Routing is active).

3) Add the SBC in Teams and create routing
- Teams Admin Center > Voice > Direct Routing > SBCs > Add:
  - FQDN: your subdomain.mstsbc.telnyx.tech
  - SIP signaling port: 5061
  - Enabled: On; Send SIP options: On; Forward P-Asserted-Identity: On (if you want anonymous calls to connect).
- Voice routes: Voice > Direct Routing > Voice routes > Add. Example patterns:
  - US: prepend 1, match NXXNXXXXXX; and match 1NXXNXXXXXX (no prepend).
  - International: prepend country prefix, match national pattern; and match with prefix included.
- Enroll SBC(s): Voice > Direct Routing > SBCs enrolled > Add SBCs.
- PSTN usage records: Voice > Direct Routing > PSTN usage records > Add (example allows ^(.*)$ for any destination; restrict as needed).
- Voice Routing Policy: Voice > Voice routing policies > Add (e.g., Name: Telnyx) and include the PSTN usage(s).
- Assign to users: Users > select user > Policies > set Dial plan (e.g., Telnyx) and Voice routing policy (Telnyx).
- Assign a Telnyx DID: Users > Manage users > select user > Account > Enable Enterprise Voice and Assign a primary phone number (LineURI).

4) Test
- Place outbound and inbound calls; confirm two‑way audio.
- Validate CDRs in the Telnyx portal Reporting section: https://portal.telnyx.com/

## Resolve TLS connectivity and SIP OPTIONS warnings (PowerShell)
If Teams shows TLS or SIP OPTIONS warnings for an existing SBC, configure routing via PowerShell (does not impact call quality but removes warnings):
- Install PowerShell and the MicrosoftTeams module (see Microsoft docs). In PowerShell:
  - Import-Module MicrosoftTeams
  - Connect-MicrosoftTeams
  - Set-CsOnlinePstnUsage -Identity Global -Usage @{Add="Telnyx"}
  - New-CsOnlineVoiceRoute -Name "Multi-Tenant" -Priority 1 -OnlinePSTNUsage "Telnyx" -OnlinePSTNGatewayList <your_subdomain>.mstsbc.telnyx.tech -NumberPattern '^(\+1[0-9]{10})$' -Description "Telnyx"
  - New-CsOnlineVoiceRoutingPolicy "Telnyx" -OnlinePstnUsages "Telnyx"
  - Grant-CsOnlineVoiceRoutingPolicy -Identity "<user_email>" -PolicyName "Telnyx"
- In Teams Admin Center, ensure the user has:
  - Calling policy allowing calling (Voice > Calling policies; assign to user).
  - Appropriate Dial plan (Voice > Dial plans; assign to user).
  - Voice routing policy (the one created above; assign to user).
- Verify the user is Enterprise Voice enabled and has a Direct Routing LineURI:
  - Get-CsOnlineUser -Identity "<user_email>" and confirm EnterpriseVoiceEnabled: True and a tel:+ E.164 LineUri.

## Operator Connect with Telnyx
- In Telnyx Mission Control Portal, go to Microsoft Teams and start the Operator Connect wizard.
- In Teams Admin Center > Voice > Operator Connect, ensure Telnyx is listed and that the Operator contact email matches your Telnyx portal email. Confirm “Yes” in the Telnyx wizard to start synchronization (can take up to 24 hours).
- Add numbers to your Operator Connect connection in Telnyx, assign an Emergency address, and submit. Use Number History to track readiness (orange = provisioning, green = ready).
- In Teams Admin > Phone numbers: assign numbers to users (Edit > assign to user > Apply).
- Emergency tips: set and assign an Emergency Calling policy; enable Dynamic emergency calling; set a valid static emergency address fallback in Teams.

## Call2Teams with Telnyx SIP trunks
Use Call2Teams to bridge Teams to Telnyx when you prefer a service-managed connector.
- Log into the Call2Teams portal with a Microsoft 365 global admin; grant “Connect on behalf of your organization.”
- Service > Trunk > Add New Trunk > select Custom (Telnyx may not be listed as a prebuilt profile); proceed with unsupported configuration.
- Example trunk settings:
  - Service Name: Telnyx Trunk 1; SIP Domain: sip.telnyx.com
  - Authenticate Type: Registration
  - Username/Auth Username/Password: your Telnyx SIP credentials
  - Protocol: UDP or TCP; Encrypt Media: No
  - DID Ranges: enter E.164 (+<countrycode><number>); add multiple ranges as needed
  - REFER propagation: Yes for call-center use cases; otherwise No to improve consultative transfers
  - E.164 translation: Outbound international prefix 011 (US example); adjust to locale
  - From header: SIP Identifier; P-Asserted-Identity: Passthrough or Trunk User Number
- Add users in Call2Teams and associate DIDs and the trunk; Sync Now.

## Skype for Business Server SIP trunking to Telnyx
1) Define the gateway in Topology Builder
- Skype for Business Server > Site > Shared Components > PSTN gateways > New IP/PSTN Gateway.
- FQDN: sip.telnyx.com; Transport: TCP; Listening port: 5060.
- Associate a Mediation Server pool (listening port 5068 by default). Publish Topology.

2) Create Enterprise Voice components (example)
- Create a Global dial plan and normalization rules (e.g., US-National, US-Service, US-International).
- Add PSTN usage (e.g., US-Basic-PSTN-Usage) and a Voice Route targeting PstnGateway:sip.telnyx.com with pattern ^+.
- Set a Voice Policy that includes the PSTN usage.
- Trunk configuration: e.g., SRTPMode Optional, MaxEarlyDialogs 20, ConcentratedTopology True, EnableReferSupport False.
- Run via Skype for Business Management Shell; back up existing config before changes.

3) Optional: Cloud Connector Edition (CCE) example INI values
- Gateway Make/Model: Telnyx Telephony Engine
- Name: sip.telnyx.com; IP: 192.76.120.10; Port: 5060; Protocol: TCP
- REFER support: $false; remove second gateway section
