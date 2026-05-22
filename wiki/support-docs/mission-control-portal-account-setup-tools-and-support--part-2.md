---
title: 'Mission Control Portal: Account Setup, Tools, and Support'
summary: A concise guide to creating and configuring your Telnyx Mission Control Portal
  account, organizing users and permissions, enabling security and notifications,
  using dashboards and debugging tools, requesting features or reporting bugs, contacting
  support, and understanding freemium, SSO, and configuration propagation.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
  content_hash: c1f6b9295dceced12b4d96995d177f30fbe57bffd58072c2f9980ef3d0e08f51
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
  content_hash: bbf28680ff8760a1f14ee3df8569507e4a5e98636a6ad3c452b77e01aed09fd5
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
  content_hash: ad7238abea6ed8da96bd972277eb0d27db5427016cc58799915a0240041e8dba
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
  content_hash: 111c330be50d02cfdc634c4dc91198d310e6f9ec71c152893e0d19ace3796d6f
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
  content_hash: e160624d3124b9e0697cea0fdcead0d8219eb13008d3800bffd40ba00c43f548
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
  content_hash: 7388e098d638dd123873988c33d4646887e1d392f36eda09faa4bf61549da160
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
  content_hash: 32ed8068d019e62b11977e4401281e9b07c5a7ecafd23804d9a970e80e6135f2
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
  content_hash: 291896c9b7a5965da2f138c68f40a5c29b8c396861f8efc5c297b2118ffc0b59
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
  content_hash: 6cd80b1c0a9f4d06768643a3bde55ec7a89825fa599ceda6c12596b566b4a154
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
  content_hash: f3cf8b058ed120365707d074423f1ad90e2c3e1f7a8c4e1208849cf612596fa5
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
  content_hash: 95a65977c104669376cf655e1f22345bf0997bcaacdf8fdfc7123caf1bb707bc
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
  content_hash: 27cc6f25ac936fc30aef96c96b1319fe0aa6cf0c33f85bd31caef42cdf814a41
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
  content_hash: b25cfcb5acba8fc1bb69445405a100cf5c0dac5a01baf7a6952058b028d5016e
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
  content_hash: bfc52e1e583bfcf9e7e95e563ad8be64d2bcd251c00fbcd3e53aaafc0ef2478f
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
  content_hash: c667c393f1df782562bfc1e2ca6cea1b70708cad9e215a1ef5a8c7c441f96f35
updated_at: 2026-05-20T14:42:57Z
---

# Mission Control Portal: Account Setup, Tools, and Support

*Part 2 of 2 — see also: [Part 1](mission-control-portal-account-setup-tools-and-support--part-1.md)*

A concise guide to creating and configuring your Telnyx Mission Control Portal account, organizing users and permissions, enabling security and notifications, using dashboards and debugging tools, requesting features or reporting bugs, contacting support, and understanding freemium, SSO, and configuration propagation.

## Support and Escalation
- NOC availability: 24/7/365.
- Contact methods: Chat (Portal bottom‑left “chat with us”), Email support@telnyx.com, Phone +1‑888‑980‑9750 (US/CA) and international lines (Estonia, Finland, Ireland, Israel, Mexico, Netherlands, New Zealand, Philippines, Poland, Singapore, UK). You’ll receive a ticket number for tracking.
- Call failure example for triage: SIP Connection name & ID, direction (in/out), CLI (source), CLD (destination), date/time with timezone, and if possible a Call ID/Unique CDR ID/UUID. Telnyx can typically troubleshoot within 72h of occurrence; for carrier escalations provide examples within 48h; if non‑reproducible, within 24h.
- Messaging example: Messaging Profile name & ID, direction, From (number or alphanumeric), To, timestamp with timezone, and any error code (see https://developers.telnyx.com/api/errors).
- API issues: share issue summary, exact endpoint URLs, timestamp with timezone, request payload, response payload, and whether reproducible. You can also test at https://developers.telnyx.com.
- Portal issues: send screenshots and/or console/network logs. If emails to support land in spam, ensure proper SPF/DMARC, avoid spammy content, and add support@telnyx.com to safe senders; Telnyx also reviews spam‑foldered emails daily.

## AI Chat Support Assistant
- Access “Ask our AI Assistant” from the Portal’s left nav. It answers from Support Center, Developer Docs, and telnyx.com, with read‑only access to relevant account resources to help troubleshoot.
- If it can’t resolve, choose “Chat to Support” to reach an agent. Provide specific, product‑named questions for best results. Available 24/7; occasional third‑party degradation may occur.
- Data and privacy: use implies consent to processing per https://telnyx.com/privacy-policy and transfer to a US subprocessor (OpenAI) for answer generation. Responses may occasionally be incorrect/outdated; verify with Support when in doubt.

## Configuration Propagation
- Changes in the Portal or API generally propagate worldwide in ~1–3 seconds (avg ~1.5s) across Telnyx infrastructure. Design workflows to accommodate this brief delay (e.g., wait before first registration with newly created SIP credentials, or pre‑provision configuration ahead of use).

## Useful Resources
- Support Center: https://support.telnyx.com/
- Developer Docs: https://developers.telnyx.com/
- Release Notes: https://telnyx.com/release-notes
- System Status: https://status.telnyx.com/
- Resource Center: https://telnyx.com/resources
