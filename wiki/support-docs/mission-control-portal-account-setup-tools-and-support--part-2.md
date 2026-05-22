---
title: 'Mission Control Portal: Account Setup, Tools, and Support'
summary: A concise guide to creating and configuring your Telnyx Mission Control Portal
  account, organizing users and permissions, enabling security and notifications,
  using dashboards and debugging tools, requesting features or reporting bugs, contacting
  support, and understanding freemium, SSO, and configuration propagation.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
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
