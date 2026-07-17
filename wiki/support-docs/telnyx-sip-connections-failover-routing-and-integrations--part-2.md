---
title: 'Telnyx SIP Connections: Failover, Routing, and Integrations'
summary: This page consolidates Telnyx SIP Connection configuration, failover, and
  retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection
  types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration
  (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware
  and sipXecs.
sources:
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
updated_at: 2026-07-17T09:07:44Z
---

# Telnyx SIP Connections: Failover, Routing, and Integrations

*Part 2 of 7 — see also: [Part 1](telnyx-sip-connections-failover-routing-and-integrations--part-1.md), [Part 3](telnyx-sip-connections-failover-routing-and-integrations--part-3.md), [Part 4](telnyx-sip-connections-failover-routing-and-integrations--part-4.md), [Part 5](telnyx-sip-connections-failover-routing-and-integrations--part-5.md), [Part 6](telnyx-sip-connections-failover-routing-and-integrations--part-6.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## AnchorSite® Settings

The **AnchorSite®** setting allows you to select the media server Telnyx uses to route your call's media packets. It is configured in the settings of your connections/applications at [Voice → Connections](https://portal.telnyx.com/#/voice/connections).

No matter which AnchorSite® option you choose (latency or a specific site), should an issue arise Telnyx will always re-route calls to the next closest AnchorSite®.

### Latency

When **Latency** is selected, Telnyx chooses the optimal Point of Presence (PoP) to route your call so media packets get off the internet as fast as possible. Telnyx regularly and proactively pings your Connection or Device using ICMP ping messages to calculate round trip timings from all Telnyx available sites. The site with the lowest latency is chosen as the AnchorSite® where your media will be anchored.

### Selecting the AnchorSite® Yourself

If you prefer not to receive pings from Telnyx and want to manually anchor calls in the PoP you feel is best, select one of the available PoPs. This is recommended when your media IP address is not located in the same area as the signalling, since Telnyx determines latency between its sites and your signalling IP address.

There are limitations to selecting the AnchorSite® yourself if you do not whitelist all Telnyx media IP addresses. In the rare event of unplanned maintenance or an outage at the selected AnchorSite®, media traffic is re-routed through the next closest available site to ensure calls remain connected without interruption.

**Latency** is the default setting for AnchorSite® when SIP Connections are created.

### Special Notes

There are limitations to selecting **latency** depending on your SIP Connection's authentication type:

- For **IP-based or FQDN-based** authentication, if Telnyx cannot determine round trip times to your IP addresses, calls may be anchored on a media server further away than is optimal. Whitelist Telnyx [media IP addresses](https://sip.telnyx.com/#media) on your firewall.
- For **credential-based** SIP Connections, include the SIP Connection's **username** in the contact header in your **first** SIP INVITE. This allows the SIP Proxy to identify the settings associated with your SIP Connection and ensure the correct AnchorSite® is chosen. If the username is not included in the first SIP INVITE, there is no way to identify the optimal media server. Alternatively, if you cannot modify the contact header, include a new header in the first SIP INVITE: `X-Telnyx-Username: <username>`.
- For **applications**, the IP address associated with your webhook URL is used to determine which site has the lowest latency reaching you.
