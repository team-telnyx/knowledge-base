---
source_url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
scraped: 2026-07-08
content_hash: f5206df79d4e1fabceb3896d21a80285e6fea05fa494729dd58c7301ab41531b
---

Whitelisting Telnyx Media IP Addresses | Telnyx Help Center

[Skip to main content](#main-content)

# Whitelisting Telnyx Media IP Addresses

Read on to learn about SIP Media IPs and how we are working to enhance our connectivity offering.

Written by Telnyx Engineering

October 17, 2024

Table of contents

# **Overview**

To ensure uninterrupted service, keeping your firewall and security settings updated is crucial to allow traffic from Telnyx’s media IP addresses. This is particularly important if your network setup restricts inbound or outbound traffic based on IP ranges.

As Telnyx continues enhancing its connectivity offering, we will introduce new SIP media IP ranges. Failure to whitelist these IPs could lead to service disruptions, as your system may block voice traffic.

# **What are SIP media IP addresses?**

[SIP (Session Initiation Protocol)](https://telnyx.com/resources/sip-trunking-explained) media IP addresses are the public IPs used to handle the actual audio (media) streams of a VoIP call. While SIP signaling (the call setup, teardown, etc.) occurs over one set of IPs, the media stream–the voice conversation–occurs over a different range of IP addresses.

It is essential to whitelist these media stream IPs so that voice data packets are not blocked by your firewall.

## **Is there a list of Telnyx IP addresses?**

Yes, you can find the most up-to-date list of IP addresses at <https://sip.telnyx.com/#media>

# **Why is Telnyx adding new media IP addresses?**

Telnyx is continuously expanding its network to improve performance and redundancy.

Adding new media IP ranges enhances our ability to provide seamless voice services to our customers, ensuring better connectivity and service quality, particularly during periods of high demand or network maintenance.

# **What do I need to do to ensure my calls are not affected?**

If your organization uses firewalls or access control lists (ACLs) to manage network traffic, you must update these to allow traffic from Telnyx’s new media IP range. This will ensure that your VoIP media is not blocked and that your voice services continue uninterrupted.

# **What happens if I don’t update my Firewall or access control lists?**

Without updating your firewall to allow traffic from the new media IPs, your voice service could be interrupted, as calls routed through the new IP range may be blocked for media, resulting in One Way Audio (OWA). Whitelisting the new IP addresses guarantees that voice traffic is allowed, keeping your communication services running smoothly.

---

Related Articles

[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Whitelisting Telnyx IP Addresses](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses)[Guide to SIP AnchorSite® Settings](https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings)[ScopTEL IP PBX](https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx)[Voice Elements: Telnyx SIP](https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip)

Did this answer your question?

😞😐😃

Table of contents
