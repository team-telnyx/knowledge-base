---
title: Telnyx Compliance, Security, and Platform Reference
summary: A comprehensive reference for Telnyx regulatory compliance obligations, security
  certifications, privacy practices, and key platform operational details — covering
  STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers
  Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
  content_hash: 67ee5a4378cda34b22669a4edc5f1925fb15b17fb7d3df43185bfd41478988d4
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
  content_hash: 2b00e4c40be23e8f5e6d8b498837c82ac949e40bf00070dafa1b2855e5b545d6
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
  content_hash: 056e70a4c1d28bc5d0d9d3df1ccdbf278417fe9bf3ba3ed4050e840cc711fe77
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
  content_hash: 8c00b9aa07357e8d25a598fbdf4427471e341bc0884ddfc96abd5d756eb2cad8
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
  content_hash: c5df94264f27b812390ce017f8ef890db223f16fca99b9434ec0d8ea51d4a2d1
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
  content_hash: 52b9cee458ba618dd725be8b39606bb73124227173e321b447a07b61e0fd2b48
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
  content_hash: 3ed45bcc93c15873a6b90d4faa89b4c1848b163dd9f3183fa9ab31f0860dbd45
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
  content_hash: 8e5e86140d4a3301f5ae5a654f92de4fdbc0631efe3a1f4b50e599e6a89b36f8
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
  content_hash: c7f2d8d7965abfc1368a2b9ca731972644ec147a989d7d4c14bd0c1615163242
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
  content_hash: d9cee1dd07e51e4df40626dbca4595f63c0bfa52827c904524a8a59c8cdf6554
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
  content_hash: 531786ea6bae25ec05258db23e53bb7eebaeac53bcaff8eddadaf61dd2b6040f
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
  content_hash: 86b9d3397acf1f7f2d3720fd46fcb02ce272d955298f4e81764795dd321fb8b7
updated_at: 2026-06-11T11:44:06Z
---

# Telnyx Compliance, Security, and Platform Reference

*Part 3 of 3 — see also: [Part 1](telnyx-compliance-security-and-platform-reference--part-1.md), [Part 2](telnyx-compliance-security-and-platform-reference--part-2.md)*

A comprehensive reference for Telnyx regulatory compliance obligations, security certifications, privacy practices, and key platform operational details — covering STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.

## HIPAA and the Conduit Exception

The Health Insurance Portability & Accountability Act (HIPAA) governs the confidentiality and security of personal health information (PHI) for covered entities and their business associates. HIPAA generally requires covered entities to enter into a Business Associate Agreement (BAA) with third-party vendors who access, receive, transmit, or store PHI.

However, some vendors fall within the HIPAA **conduit exception** — individuals or organizations that "act merely as a conduit for protected health information." Temporarily storing PHI incident to a transmission does not disqualify an entity from this exception ([78 FR 5571-72](https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf)).

In general, Telnyx's services fall within the conduit exception under HIPAA, and therefore **no BAA is required**. For questions, contact [sales@telnyx.com](mailto:sales@telnyx.com).

## P2P SMS Traffic and 10DLC Exemption

### P2P Definition

P2P (Person-to-Person) SMS traffic is the exchange of text messages between individuals using regular mobile phone numbers. Key characteristics:

1. **Individual use** — messages are sent from one individual to another, not from a business or application.
2. **Two-way communication** — conversation-like flow with both parties able to send and receive.
3. **Phone numbers** — uses regular mobile numbers, not short codes or alphanumeric sender IDs.
4. **Non-commercial** — not used for marketing, notifications, automated alerts, or anything on behalf of a business.
5. **Standard SMS rates** — standard carrier messaging fees apply.
6. **Different regulatory treatment** — carriers treat P2P more leniently than A2P (Application-to-Person) messaging.

If a P2P exemption is approved, there is no requirement to register with The Campaign Registry for campaigns.

### P2P Exemption Qualification

To qualify for a P2P exemption from 10DLC requirements, all of the following must apply:

1. Your messaging excludes business communication of any kind.
2. You are not a Cloud Communication Suite.
3. Traffic will be roughly symmetrical (1:1 to 1:3, user-to-user).
4. There are no automated text messages in your workflow.
5. You have a Telnyx contract.

If you meet the criteria and have a Telnyx contract, reach out to your Customer Success Manager to apply. If you do not yet have a contract, contact [sales@telnyx.com](mailto:sales@telnyx.com) to discuss a commercial agreement. Commercial agreements start at $1,000/month in spend with Telnyx for at least 12 months.

**Note:** Mobile operators impose strict P2P exemption requirements, and the approval process can take up to several months. Review the up-to-date TCR P2P requirements before applying.

## Configuration Propagation Delays

When changes are made in the Mission Control Portal or via the Telnyx API, updates must propagate across Telnyx's globally distributed infrastructure before taking full effect.

| Metric | Duration |
|--------|----------|
| Minimum | ~1 second |
| Average | ~1.5 seconds |
| Maximum | ~3 seconds |

This propagation window applies to all configuration updates, including creating or modifying SIP credentials, updating call control settings, modifying connection configurations, and editing messaging profiles or number settings. Design workflows accordingly — for example, adding a small delay before first use of newly created SIP credentials, or pre-creating credentials ahead of time, avoids authentication failures during propagation.

## BYOC: Telnyx & Genesys Cloud Integration

The Bring Your Own Carrier (BYOC) integration between Genesys Cloud and Telnyx uses SIP trunk connectivity. The following steps outline the configuration.

### Prerequisites

1. A Telnyx account with L2 verification completed.
2. A purchased number for voice calls.
3. BYOC option enabled in your Genesys Cloud organization.
4. Admin rights to set up trunks in Genesys Cloud.

### Telnyx Configuration

1. **Create a SIP Connection.** In Mission Control, navigate to Voice → SIP Trunking → Add SIP Connection. Name the connection, choose "FQDN" as the connection type, and provide the SIP URI matching your Genesys Cloud region. In the Outbound section, select "Credentials" and set a username and password for digest authentication. Save the connection.
2. **Create an Outbound Voice Profile.** Navigate to Voice → Outbound Voice Profiles → Add New Profile. Name it, select allowed countries/regions, and save.
3. **Assign the Profile.** Edit the SIP Connection, go to the Outbound tab, and select the new Outbound Voice Profile from the dropdown.
4. **Configure Inbound Settings.** In the SIP Connection's Inbound tab, adjust DNIS and ANI number formats to match your Genesys Cloud configuration and save.
5. **Assign Numbers.** Navigate to Numbers → My Numbers and assign the configured SIP Connection to your purchased number(s). Multiple numbers can share the same SIP connection.

### Genesys Cloud Configuration

1. **Create a SIP Trunk.** Go to Admin → Trunks, name the trunk, and choose "BYOC Carrier" as the type, then "Generic BYOC Carrier" as the subtype.
2. **Set Inbound SIP Termination Identifier.** This should match the FQDN configured in the Telnyx SIP Connection.
3. **Configure SIP Settings.** Provide the Telnyx SIP interface URL (e.g., `sip.telnyx.com`, `sip.telnyx.eu`) in "SIP Servers and Proxies." Enable Digest Authentication with the same URL as the realm. Enter the username and password configured in the Telnyx SIP Connection. Set the Caller ID to your purchased Telnyx number.
4. **SIP Access Control.** Add the IP addresses of your chosen Telnyx SIP endpoints (available at `sip.telnyx.com`).
5. **External Trunk Configuration.** Under Protocol → Outbound, add a custom SIP header `X-Telnyx-Username` with the same value as the Digest Authentication username.

### Troubleshooting

Debugging tools are available in Mission Control under Reporting → Debugging → SIP Call Flow Tool. Search CDRs by criteria, then select a call to review the SIP call flow with detailed request data. You can also inspect session info or export PCAP data for sharing with your team.
