---
title: Telnyx Device Configuration Guides
summary: Step-by-step instructions for configuring Telnyx SIP trunks on a range of
  supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station,
  Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door
  phones. Each guide covers prerequisites, device access, SIP server settings, and
  registration parameters required to connect the device to the Telnyx Mission Control
  Portal.
sources:
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-08-05T13:36:02Z
---

# Telnyx Device Configuration Guides

*Part 3 of 4 — see also: [Part 1](telnyx-device-configuration-guides--part-1.md), [Part 2](telnyx-device-configuration-guides--part-2.md), [Part 4](telnyx-device-configuration-guides--part-4.md)*

Step-by-step instructions for configuring Telnyx SIP trunks on a range of supported devices, including the Ribbon EdgeMarc 6000 SBC, Snom M100 KLE base station, Mitel 5320E/5330E/5340E and 6800/6900 SIP phones, and Alcatel SD601/SD602 SIP door phones. Each guide covers prerequisites, device access, SIP server settings, and registration parameters required to connect the device to the Telnyx Mission Control Portal.

## Mitel 6800/6900 SIP Setup

The Mitel 6800/6900 families include a wide range of executive and desk SIP/IP phones. See the [Mitel 6800 family](https://www.mitel.com/products/devices-accessories/sip-phones-peripherals) and [Mitel 6900 family](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/6900-ip-series) for product details.

Additional resources: [6800/6900 series admin manual](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/6800-series/6800-sip-phones/62sp1/en/mitel-6800-6900-series-sip-phones-administrator-guide), [Mitel Learning Center](https://www.mitel.com/support/learning-center), [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars), [Mitel user group](https://www.mitel.com/partners/mitel-user-group).

### Log Into the Mitel Web Configuration Tool

1. From the phone UI, navigate to **Phone Status**.
2. Find the IP address:
   - **IP&MAC Addresses** option (6863i, 6865i, 6905, 6910)
   - **Network > IP Address** (6867i, 6869i, 6873i, 6920, 6930, 6940, 6970)
3. Enter the IP address in a browser. Default credentials differ for admin and user:
   - **Admin:** Username `admin`, Password `22222`
   - **User:** Username `user`, Password blank

### Configure the SIP Trunk: Configuration Options

Settings can be configured via the Mitel Web UI, the IP Phone UI, or configuration files (`startup.cfg`, `<model>.cfg`, or `<mac>.cfg`). In the Web UI, use **Advanced Settings > Global SIP** for global parameters or **Advanced Settings > <Line>** for per-line parameters. See the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291) for parameter details.

### Configure the SIP Trunk: Global Parameters

**Global Authentication Parameters**

| IP Phone UI | Mitel Web UI | Config File | Value |
| --- | --- | --- | --- |
| Screen Name | Screen Name | `sip screen name` | Telnyx username |
| N/A | Screen Name 2 | `sip screen name 2` | Custom idle-screen text (up to 20 alphanumeric characters) |
| User Name | Phone Number | `sip user name` | Telnyx username |
| Display Name | Caller ID | `sip display name` | Caller ID (capital letters, no special characters, spaces allowed; some Canadian providers limit to 15 characters) |
| Auth Name | Authentication Name | `sip auth name` | Telnyx username |
| Password | Password | `sip password` | Telnyx password |
| N/A | BLA Number | `sip bla number` | Phone number assigned to BLA lines shared across phones |
| N/A | Line Mode | `sip mode` | Generic (0), BroadSoft SCA (1), Reserved (2), or BLA (3). Default: Generic (0) |
| N/A | Call Waiting | `call waiting` | Enables/disables call waiting |
| N/A | N/A | `sip vmail` | Voicemail number (e.g., `*97`) |

**Global Network Parameters**

| IP Phone UI | Mitel Web UI | Config File | Value |
| --- | --- | --- | --- |
| Proxy Server | Proxy Server | `sip proxy ip` | FQDN `sip.telnyx.com` or IP `192.761.120.10` (see [international addresses](https://sip.telnyx.com/#signaling-addresses)) |
| Proxy Port | Proxy Port | `sip proxy port` | `5060` for TCP/UDP, `5061` for TLS |
| N/A | Backup Proxy Server | `sip backup proxy ip` | `64.16.250.10` |
| N/A | Outbound Proxy Server | `sip outbound proxy` | FQDN `sip.telnyx.com` or IP `192.761.120.10` |
| Registrar Server | Backup Outbound Proxy | `sip backup outbound proxy` | `sip.telnyx.com` |

### Configure the SIP Trunk: Per-Line Parameters

**Per-Line Authentication Parameters**

| IP Phone UI | Mitel Web UI | Config File | Value |
| --- | --- | --- | --- |
| Screen Name | Screen Name | `sip lineN screen name` | Telnyx username |
| N/A | Screen Name 2 | `sip lineN screen name 2` | Custom idle-screen text (up to 20 alphanumeric characters) |
| User Name | Phone Number | `sip lineN user name` | Telnyx username |
| Display Name | Caller ID | `sip lineN display name` | Caller ID (capital letters, no special characters, spaces allowed; some Canadian providers limit to 15 characters) |
| Auth Name | Authentication Name | `sip lineN auth name` | Telnyx username |
| Password | Password | `sip lineN password` | Telnyx password |
| N/A | BLA Number | `sip lineN bla number` | Phone number assigned to BLA lines shared across phones |
| N/A | Line Mode | `sip lineN mode` | Generic (0), BroadSoft SCA (1), Reserved (2), or BLA (3). Default: Generic (0) |
| N/A | Call Waiting | `sip lineN call waiting` | Enables/disables call waiting |
| N/A | N/A | `sip lineN vmail` | Voicemail number per line (e.g., `*97`) |

**Per-Line Network Parameters**

| IP Phone UI | Mitel Web UI | Config File | Value |
| --- | --- | --- | --- |
| Proxy Server | Proxy Server | `sip lineN proxy ip` | FQDN `sip.telnyx.com` or IP `192.761.120.10` |
| Proxy Port | Proxy Port | `sip lineN proxy port` | `5060` for TCP/UDP, `5061` for TLS |
| N/A | Backup Proxy Server | `sip lineN backup proxy ip` | `64.16.250.10` |
| N/A | Outbound Proxy Server | `sip lineN outbound proxy` | FQDN `sip.telnyx.com` or IP `192.761.120.10` |
| Registrar Server | Backup Outbound Proxy | `sip lineN backup outbound proxy` | `sip.telnyx.com` |

### Configure TLS Transportation (Optional)

TLS and Persistent TLS ensure communication privacy between SIP phones and the internet. Only one Persistent TLS connection is allowed per phone. If Persistent TLS is configured, the Trusted Certificate file must be specified; Root and Intermediate Certificates, Local Certificate, and Private Key files are optional. See the [TLS and SRTP article](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) for required certificate values.

| IP Phone UI | Mitel Web UI | Config File | Value |
| --- | --- | --- | --- |
| N/A | Transport Protocol | `sip transport protocol` | Protocol for SIP data. Default `UDP`. If TLS is used, the phone checks `sips persistent tls`; if enabled, Persistent TLS is used, otherwise TLS. TLS requires Root/Intermediate Certificates, Local Certificate, Private Key, and Trusted Certificates |
| N/A | N/A | `sips persistent tls` | Enables Persistent TLS. Re-uses the registration connection for all calls. Trusted Certificates required; other certificates optional |
| N/A | N/A | `sip persistent tls keep alive` | Configures keep-alive pings for Persistent TLS connections (real interval varies between 80% and 100% of configured value) |
| N/A | N/A | `sip send sips over tls` | Manually configure SIP or SIPS URI scheme when TLS or Persistent TLS is enabled |
| N/A | Root and Intermediate Certificates Filename | `sips root and intermediate certificates` | Required for TLS, optional for Persistent TLS |
| N/A | Local Certificate Filename | `sips local certificate` | Required for TLS, optional for Persistent TLS |
| N/A | Private Key Filename | `sips private key` | Required for TLS, optional for Persistent TLS |
| N/A | Trusted Certificate Filename | `sips trusted certificate` | Required for TLS and Persistent TLS. Must contain CA root certificates for all servers the phone connects to |
