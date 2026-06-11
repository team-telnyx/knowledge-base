---
title: SBC Setup with Telnyx
summary: Configuration guides for integrating Session Border Controllers with Telnyx
  SIP trunks, covering Oracle Acme Packet, AudioCodes, Ribbon EdgeMarc 6000, and Sansay
  VSXi platforms.
sources:
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
updated_at: 2026-06-11T11:43:59Z
---

# SBC Setup with Telnyx

*Part 2 of 2 — see also: [Part 1](sbc-setup-with-telnyx--part-1.md)*

Configuration guides for integrating Session Border Controllers with Telnyx SIP trunks, covering Oracle Acme Packet, AudioCodes, Ribbon EdgeMarc 6000, and Sansay VSXi platforms.

## Ribbon EdgeMarc 6000 Configuration

The [Ribbon EdgeMarc 6000](https://ribboncommunications.com/solutions/enterprise-solutions/secure-cloud-communications-solutions/microsoft-solutions-teams-direct-routing) is a demarcation and control point with physical telephony ports and VNF support. This guide is also compatible with EdgeMarc VOS 15.7.

### Configure SIP Settings

1. Log into the EdgeMarc portal.
2. Navigate to **VoIP > SIP**.
3. In the **SIP protocol settings** section, set:
   - **SIP Server Address:** `sip.telnyx.com`
   - **SIP Server Port:** `5060`
   - **SIP Server Transport:** `UDP`
   - **Use Custom Domain:** Checked
   - **SIP Server Domain:** `sip.telnyx.com`
   - **Limit Inbound to listed Proxies:** Checked
   - **Limit Outbound to listed Proxies:** Checked

### Define SIP Trunk Registration

1. Navigate to **VoIP > SIP > B2BUA**.
2. In the **Trunking Devices** section, click **New Row** and provide:
   - **Name:** Identifies your trunking device
   - **Model:** Select your PBX from the drop-down
   - **IP:** Select the IP radio button and enter your PBX IP address
   - **Transport:** `TLS` if encrypting, otherwise `UDP` or `TCP`
   - **Port:** `5060` (or `5061` if using TLS)
3. Click **Update**, then **Submit** to push the configuration.

### Configure Inbound Rules

1. Navigate to **VoIP > SIP > B2BUA** and click the **Match** tab.
2. Click **New Row** and set:
   - **Direction:** `Inbound`
   - **Mode:** `BothModes`
   - **Default:** Select the radio button
   - **Action:** `Inbound`

### Configure Outbound Rules

1. On the same **Match** tab, click **New Row** and set:
   - **Direction:** `Outbound`
   - **Mode:** `BothModes`
   - **Pattern:** Select radio button, then choose `Calling` from the drop-down
   - **Called/Calling Party:** Enter `.` to allow all callers, or pattern-match on partial numbers (e.g., `1312270X`)
   - **Source:** `Any`
   - **Action:** `Outbound`
2. Click **Update**, then **Submit**.

For more information, see [EdgeMarc 6000 documentation](https://rbbn.my.site.com/Support/login), [Ribbon support](https://ribboncommunications.com/services/ribbon-support-portal), and [EdgeMarc VoIP settings overview](https://rbbn.my.site.com/Partners/login).

## Sansay VSXi SBC Configuration

The [Sansay VSXi session controller](https://www.sansay.com/products/vsxi/) is a high-performance software-based SBC providing security, DDoS protection, NAT, protocol interworking, and traffic management. Configuration is done through the Sansay portal.

### Create Resources

1. Log into the Sansay portal and select **Resources** from the navigation.
2. Create two new resources: one for inbound and one for outbound.

### Inbound Trunk Configuration

Set the following on the first resource:

- **Resource Type:** `Inbound` / `Peering`
- **Protocol:** `SIP`
- **SIP Profile:** `SIP_Peering:0`

Under **General Info:**

| Setting | Value |
|---|---|
| SIP Trunk ID | 1000 |
| Trunk Name | Telnyx Inbound |
| Company Name | Telnyx |
| Route Table | *:0 |
| Remote Port | 5060 |
| Service Port | SIP Public Default 1:1 |
| Aggregate Capacity | 1200 |
| Average CPS Limit | 500 |
| Authorized RPS | 500 |
| Unauthorized RPS | 500 |
| Group Policy | Round Robin |
| Digit Mapping Table | no-translation:0 |
| Min Call Duration | 0 |
| Max Call Duration | 43200 |
| RTP TOS | B8 |
| Direction | Both |
| Service State | inservice |
| Allow Direct Media | No |
| No Answer Timeout | 120 |
| No Ring Timeout | 30 |
| Option Poll | Disable |
| Cause Code Profile | Default:0 |
| Stop Route Profile | Default:0 |
| PAI | Disable |

Under **Digit Translation & RN Handling:**

- **Ingress & Egress:** `all`
- **Outbound ANI:** `pass`
- **Tech Prefix:** `default`

Under **Codec Info:**

- **Policy:** `enforced`
- **Codec 1:** `g711u64k` (Codecs 2–8: `None`)

Under **Fqdns Info:**

- Add Telnyx signalling and media IP addresses appropriate for your location. Refer to [Telnyx signalling IP addresses](https://sip.telnyx.com/#signaling-addresses) and [media IP addresses](https://sip.telnyx.com/#media).

Click **Save as** then **Submit**.

### Outbound Trunk Configuration

Set the following on the second resource:

- **Resource Type:** `Outbound` / `Peering`
- **Protocol:** `SIP`
- **SIP Profile:** `SIP_Peering:0`

Under **General Info:**

| Setting | Value |
|---|---|
| SIP Trunk ID | 1001 |
| Trunk Name | Telnyx Outbound |
| Company Name | Telnyx |
| Route Table | *:0 |
| Remote Port | 5060 |
| Service Port | SIP Public Default 1:1 |
| Aggregate Capacity | 1200 |
| Average CPS Limit | 500 |
| Authorized RPS | 500 |
| Unauthorized RPS | 500 |
| Group Policy | Round Robin |
| Digit Mapping Table | no-translation:0 |
| Min Call Duration | 0 |
| Max Call Duration | 43200 |
| RTP TOS | B8 |
| Direction | Both |
| Service State | inservice |
| Allow Direct Media | No |
| No Answer Timeout | 120 |
| No Ring Timeout | 30 |
| Option Poll | Disable |
| Cause Code Profile | Default:0 |
| Stop Route Profile | Default:0 |
| PAI | Disable |

Under **Digit Translation & RN Handling**, **Codec Info**, and **Fqdns Info**, use the same settings as the inbound trunk (with `g711u64k` as Codec 1 and Telnyx signalling/media IPs in Fqdns Info).

Click **Save as & Submit** to push the configuration.

For more information, see the [VSXi datasheet](https://www.sansay.com/wp-content/uploads/2013/05/Sansay_VSXi_Session-Controller_9_2013.pdf), [VSXi REST API](https://support.sansay.com/t/36d6tz/vsxi-rest-api), and [Sansay contact](https://www.sansay.com/contact-us/).

## Common Telnyx SBC Connection Details

Across all SBC platforms, the core Telnyx connection parameters are:

- **SIP Server / Hostname:** `sip.telnyx.com`
- **SIP Port:** `5060` (UDP) or `5061` (TLS)
- **Transport:** `UDP` (default); `TLS` recommended for encryption
- **Default Codec:** G.711 μ-law (PCMU / `g711u64k`)
- **Caller ID Format:** +E.164 required for calling numbers

Review Telnyx [signalling IP addresses](https://sip.telnyx.com/#signaling-addresses) and [media IP addresses](https://sip.telnyx.com/#media) when configuring firewall rules or FQDN-based routing.
