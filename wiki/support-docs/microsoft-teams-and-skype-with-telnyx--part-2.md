---
title: Microsoft Teams and Skype with Telnyx
summary: 'End-to-end guide to connect Microsoft Teams and Skype for Business to Telnyx
  for PSTN calling: Direct Routing via the Telnyx integrated SBC, Operator Connect,
  Call2Teams, Skype for Business SIP trunking, number porting from Skype/Teams, TLS/SIP
  warning remediation, and emergency calling behavior with Dynamic Location Routing.'
sources:
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
  content_hash: 378ae17fe6711b7b883b9142039414a2d5924c6b3ed0352485555dee1cbf55bf
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
  content_hash: c6c29c49f44d2c985f38848316df4cf18ce3784f1b1e7a137cce1effc497ac54
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
  content_hash: c034af6464dc572700d98c3e766d37b0f188f857dcb7ae6b0aee7717b5d9e193
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
  content_hash: a53cdf6c710f579bfa94d1b61363317595daa6d70152dacb4f079cb75a53a77c
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
  content_hash: 397332393ca83ce0989c39668aebc3d5bf6feb3113a375c1033e35411769833d
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
  content_hash: ff5746ef68c059a8004079f51eddd2845aa76006d454aa7cc3932b0c04c62517
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
  content_hash: 0a1aca60663544144117dbd7da06eef3843562ae780781ef8c08edea4322ce34
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
  content_hash: a1bd01f179c424fdf697b8171432f7d27a98c6bec518d5de8d8d6bc22ef6831d
updated_at: 2026-05-20T15:02:24Z
---

# Microsoft Teams and Skype with Telnyx

*Part 2 of 2 — see also: [Part 1](microsoft-teams-and-skype-with-telnyx--part-1.md)*

End-to-end guide to connect Microsoft Teams and Skype for Business to Telnyx for PSTN calling: Direct Routing via the Telnyx integrated SBC, Operator Connect, Call2Teams, Skype for Business SIP trunking, number porting from Skype/Teams, TLS/SIP warning remediation, and emergency calling behavior with Dynamic Location Routing.

## Porting numbers from Skype and Microsoft
Porting from Skype to Telnyx
- Must be an active Skype Number (non‑Skype numbers or plain Skype IDs cannot be ported).
- Request a Porting Authorization Code (PAC) from Skype Support; ensure the number is in good standing.
- Submit a Telnyx port request with the Skype Number, PAC, and account details: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- Expect brief service disruption during cutover; keep the Skype account active until completion. Skype may charge a port-out fee; Telnyx does not charge Port‑In fees.

Porting from Microsoft Teams
- Set a porting PIN (10 digits) in Teams Admin Center: Voice > Phone numbers > Manage porting PIN.
- If no account number/BTN is provided, use one of the porting numbers.
- In the Telnyx port request comments, add: "PIN is <10-digit PIN>".
- Many orders auto-approve within ~1 business day (varies by underlying provider).
- For Microsoft Calling Plan numbers you want on Operator Connect, open a Telnyx ticket so Telnyx can coordinate with Microsoft. Provide: external connection ID, numbers to migrate, and assignment type (Calling User vs First Party App).

## Emergency calling with Teams and Telnyx (Dynamic Location Routing)
- Microsoft Teams includes PIDF‑LO location data in the SIP INVITE (MIME) for emergency calls in supported regions (methods LIS or ASSIST). Telnyx parses this to route the call to the correct PSAP quickly and accurately.
- Ensure Teams Emergency Calling policies are configured, Dynamic emergency calling is enabled, and a valid static fallback address exists. Telnyx E911 setup guide: https://support.telnyx.com/en/articles/1130683-e911-setup-guide

## Testing and troubleshooting
- After configuration, place outbound PSTN calls and inbound calls to the Telnyx DID assigned to a Teams user; confirm two‑way audio and that calls traverse Telnyx.
- Review Telnyx CDRs in the Reporting section for verification: https://portal.telnyx.com/
- If Direct Routing shows TLS/SIP warning banners, apply the PowerShell steps above.
- For porting questions or issues, contact Telnyx Support: https://support.telnyx.com/

## Key external references
- Microsoft Teams Direct Routing plan: https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan
- Microsoft Teams Dynamic Emergency Calling: https://learn.microsoft.com/en-us/microsoftteams/configure-dynamic-emergency-calling
- Microsoft 365 Admin Center: https://portal.office.com
- Teams Admin Center: https://admin.teams.microsoft.com/
