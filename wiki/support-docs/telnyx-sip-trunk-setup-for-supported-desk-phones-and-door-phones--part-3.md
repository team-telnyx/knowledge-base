---
title: Telnyx SIP Trunk Setup for Supported Desk Phones and Door Phones
summary: This page explains how to configure a Telnyx SIP trunk on several supported
  desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690,
  Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP
  door phones. Each section covers prerequisites, how to access the device's web interface,
  and the SIP trunk configuration values to enter.
sources:
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
updated_at: 2026-07-17T09:10:56Z
---

# Telnyx SIP Trunk Setup for Supported Desk Phones and Door Phones

*Part 3 of 4 — see also: [Part 1](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-1.md), [Part 2](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-2.md), [Part 4](telnyx-sip-trunk-setup-for-supported-desk-phones-and-door-phones--part-4.md)*

This page explains how to configure a Telnyx SIP trunk on several supported desk phones and door phones, including the Gigaset A510 IP, Gigaset A690/AS690, Gigaset DX800a, Dinstar C60, Mitel 6800/6900 series, and Alcatel SD601/SD602 SIP door phones. Each section covers prerequisites, how to access the device's web interface, and the SIP trunk configuration values to enter.

## Mitel 6800/6900 SIP

The Mitel 6800 and 6900 families include executive and desk phones for enterprise use. See the [Mitel 6800 family](https://www.mitel.com/products/devices-accessories/sip-phones-peripherals) and [Mitel 6900 family](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/6900-ip-series) product pages, the [6800/6900 series admin manual](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/6800-series/6800-sip-phones/62sp1/en/mitel-6800-6900-series-sip-phones-administrator-guide), the [Mitel Learning Center](https://www.mitel.com/support/learning-center), [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars), and the [Mitel user group](https://www.mitel.com/partners/mitel-user-group) for additional resources.

### Log into the Mitel Web Configuration Tool

1. From the phone UI, navigate to **Phone Status**.
2. Find the IP address:
   - **IP&MAC Addresses** option on 6863i, 6865i, 6905, and 6910 IP Phones.
   - **Network > IP Address** on 6867i, 6869i, 6873i, 6920, 6930, 6940, and 6970 IP Phones.
3. From a computer on the same network, open a browser and enter the phone's IP address.
4. Log in with the default credentials. Note that admin and user credentials are different:
   - **Admin:** Username `admin`, Password `22222`.
   - **User:** Username `user`, Password blank.

### Configure the SIP trunk: Configuration options

You can configure settings via the Mitel Web UI, the IP Phone UI, or configuration files. This document covers the Web UI and configuration files. See page 78 of the [Administrator Guide](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf) for model-specific UI details.

- **Web UI:** Go to **Advanced Settings > Global SIP** for global SIP parameters, or **Advanced Settings > <Line>** for individual line parameters.
- **Configuration files (administrators only):** Edit `startup.cfg`, `<model>.cfg`, or `<mac>.cfg` in a text editor. See page 95 of the Administrator Manual for parameter details, page 66 for configuration file precedence, and Appendix A (page 843) for parameter reference.

### Configure the SIP trunk: Global parameters

SIP parameters can be set globally or per-line. The following are the global authentication parameters:

| IP Phone UI | Mitel Web UI | Configuration File | Value |
| --- | --- | --- | --- |
| Screen Name | Screen Name | sip screen name | Your Telnyx username |
| N/A | Screen Name 2 | sip screen name 2 | Custom idle-screen text (up to 20 alphanumeric characters) |
| User Name | Phone Number | sip user name | Your Telnyx username |
| Display Name | Caller ID | sip display name | Your caller ID (capital letters, no special characters, under 15 characters for some Canadian providers) |
| Auth Name | Authentication Name | sip auth name | Your Telnyx username |
| Password | Password | sip password | Your Telnyx password |
| N/A | BLA Number | sip bla number | Phone number assigned to BLA lines shared across phones (see Administrator Manual page 538) |
| N/A | Line Mode | sip mode | Generic (0), BroadSoft SCA (1), Reserved (2), or BLA (3). Default is Generic (0) |
| N/A | Call Waiting | call waiting | Enables/disables call waiting (see Administrator Manual pages 312 and 397) |
| N/A | N/A | sip vmail | Voicemail number for the phone system (e.g., `*97`) |

Global network parameters:

| IP Phone UI | Mitel Web UI | Configuration File | Value |
| --- | --- | --- | --- |
| Proxy Server | Proxy Server | sip proxy ip | FQDN `sip.telnyx.com` or IP `192.761.120.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| Proxy Port | Proxy Port | sip proxy port | `5060` for TCP/UDP, `5061` for TLS |
| N/A | Backup Proxy Server | sip backup proxy ip | `64.16.250.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| N/A | Outbound Proxy Server | sip outbound proxy | FQDN `sip.telnyx.com` or IP `192.761.120.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| Registrar Server | Backup Outbound Proxy | sip backup outbound proxy | `sip.telnyx.com` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |

### Configure the SIP trunk: Per-line parameters

Per-line authentication parameters:

| IP Phone UI | Mitel Web UI | Configuration File | Value |
| --- | --- | --- | --- |
| Screen Name | Screen Name | sip lineN screen name | Your Telnyx username |
| N/A | Screen Name 2 | sip lineN screen name 2 | Custom idle-screen text (up to 20 alphanumeric characters) |
| User Name | Phone Number | sip lineN user name | Your Telnyx username |
| Display Name | Caller ID | sip lineN display name | Your caller ID (capital letters, no special characters, under 15 characters for some Canadian providers) |
| Auth Name | Authentication Name | sip lineN auth name | Your Telnyx username |
| Password | Password | sip lineN password | Your Telnyx password |
| N/A | BLA Number | sip lineN bla number | Phone number assigned to BLA lines shared across phones (see Administrator Manual page 538) |
| N/A | Line Mode | sip lineN mode | Generic (0), BroadSoft SCA (1), Reserved (2), or BLA (3). Default is Generic (0) |
| N/A | Call Waiting | sip lineN call waiting | Enables/disables call waiting (see Administrator Manual pages 312 and 397) |
| N/A | N/A | sip lineN vmail | Voicemail number for each line (e.g., `*97`) |

Per-line network parameters:

| IP Phone UI | Mitel Web UI | Configuration File | Value |
| --- | --- | --- | --- |
| Proxy Server | Proxy Server | sip lineN proxy ip | FQDN `sip.telnyx.com` or IP `192.761.120.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| Proxy Port | Proxy Port | sip lineN proxy port | `5060` for TCP/UDP, `5061` for TLS |
| N/A | Backup Proxy Server | sip lineN backup proxy ip | `64.16.250.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| N/A | Outbound Proxy Server | sip lineN outbound proxy | FQDN `sip.telnyx.com` or IP `192.761.120.10` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |
| Registrar Server | Backup Outbound Proxy | sip lineN backup outbound proxy | `sip.telnyx.com` (see [international signaling addresses](https://sip.telnyx.com/#signaling-addresses)) |

### (Optional) Configure TLS transport

TLS and Persistent TLS ensure communication privacy between SIP phones and the internet. This must be set up by an administrator, and only one Persistent TLS connection is supported per phone. If you configure Persistent TLS, you must also specify the Trusted Certificate file; Root and Intermediate Certificates, Local Certificate, and Private Key files are optional. See the [TLS and SRTP article](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) for the values you need. See page 692 of the Administrator Manual for Mitel's requirements and page 964 for TLS settings in config files.

| IP Phone UI | Mitel Web UI | Configuration File | Value |
| --- | --- | --- | --- |
| N/A | Transport Protocol | sip transport protocol | Protocol used for SIP data. Default is `UDP`. If TLS is used, the phone checks `sips persistent tls`; if enabled, Persistent TLS is used, otherwise TLS. If TLS is used, you must specify the [Root and Intermediate Certificates, Local Certificate, Private Key, and Trusted Certificates](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). |
| N/A | N/A | sips persistent tls | Enables/disables Persistent TLS. Persistent TLS sets up the connection once and reuses it for all calls. If Persistent TLS is used, you must specify the [Trusted Certificates](https://support.telnyx.com/en/articles/4404575-tls-and-srtp); Root and Intermediate Certificates, Local Certificate, and Private Key are optional. |
| N/A | N/A | sip persistent tls keep alive | Configures keep-alive pings for Persistent TLS connections. The real interval varies between 80% and 100% of the configured value. |
| N/A | N/A | sip send sips over tls | Manually configure the IP phones to use either the SIP or SIPS URI scheme when TLS or Persistent TLS is enabled. |
| N/A | Root and Intermediate Certificates Filename | sips root and intermediate certificates | Specifies the [Root and Intermediate Certificate files](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). Required for TLS, optional for Persistent TLS. |
| N/A | Local Certificate Filename | sips local certificate | Specifies the [Local Certificate file](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). Required for TLS, optional for Persistent TLS. |
| N/A | Private Key Filename | sips private key | Specifies the [Private Key file](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). Required for TLS, optional for Persistent TLS. |
| N/A | Trusted Certificate Filename | sips trusted certificate | Specifies the [Trusted Certificate files](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). Required for TLS or Persistent TLS. The trusted list must contain the CA root certificates for all servers the phone connects to. |
