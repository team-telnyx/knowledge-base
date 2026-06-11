---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring SIP trunks between Telnyx and various
  open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and
  FusionPBX — using either IP-based or credentials-based authentication.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
  content_hash: 3b217f8dcda4cc1ce92e979c87da493e275f46181a548436bafb888a7d4e6e9f
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
  content_hash: 571e092cc671b0ddd605cc1281e26d891dbd85c0d6033cefa49898d53fad873d
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
  content_hash: dfea424979422c26a7ec8400bf9e4d2b1045dd18b440b4801c1e125d85bf92df
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
  content_hash: 7cdea4830a2f059adcf4db9b5a3e8481185928acc9e2aa3616264dd74790a988
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
  content_hash: 142b9376b059e1523c0c1aafae30b5258a259e178de80247258eb56d134fd8df
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
  content_hash: 19ac2b8bc5e75f97b93e2c0de29ff181b685f28a56ffa1b1c036774e7a195f89
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
  content_hash: d2b04f8499ca8bd387a743c805e5d4aae159fa3771ac8a8fc509b304f68e3ad7
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
  content_hash: 344b4a78795bcc1488a0ae24c40ba79931762e9987ca74be9d7ac992dc156524
updated_at: 2026-06-11T11:25:51Z
---

# PBX SIP Trunk Configuration with Telnyx

*Part 3 of 3 — see also: [Part 1](pbx-sip-trunk-configuration-with-telnyx-2--part-1.md), [Part 2](pbx-sip-trunk-configuration-with-telnyx-2--part-2.md)*

Comprehensive guide for configuring SIP trunks between Telnyx and various open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and FusionPBX — using either IP-based or credentials-based authentication.

## FusionPBX

FusionPBX is a multi-tenant PBX built on FreeSWITCH. These instructions cover credentials-based authentication. Debian is the recommended operating system.

### Installation

Run the following commands as root to install FusionPBX, FreeSWITCH, and dependencies (NGINX, PHP-FPM, PostgreSQL, iptables, Fail2ban):

```bash
apt-get update && apt-get upgrade -y
apt-get install -y git lsb-release
cd /usr/src && git clone https://github.com/fusionpbx/fusionpbx-install.sh.git
cd /usr/src/fusionpbx-install.sh/debian
./install.sh
```

After the script finishes, open a browser to the server's IP address to complete the GUI-based setup (language selection, event socket settings, admin credentials, and database configuration).

### Gateway Configuration

1. Go to **Advanced → Upgrade**, tick **App Defaults**, and click **Execute**.
2. Go to **Accounts → Gateway** and fill in:
   - **Gateway:** Telnyx
   - **Username:** Your Telnyx credentials-based connection username
   - **Password:** Your Telnyx credentials-based connection password
   - **From User:** Your Telnyx credentials-based connection username
   - **From Domain:** sip.telnyx.com
   - **Proxy:** sip.telnyx.com
3. Click **Save**. The gateway should register with Telnyx.

### Extensions and Destinations

1. Go to **Accounts → Extensions** and click **Add** to create extensions.
2. Optionally configure an **Outbound Caller ID Number** for each extension. Keep in mind:
   - Use capital letters for the caller ID name.
   - Do not use special characters.
   - Some Canadian providers truncate names beyond 15 characters.
   - Spaces are allowed.
   - Comply with Telnyx's [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy).
3. Go to **Dialplan → Destinations** and click **Add** to link purchased DIDs to extensions (prepend `+1` to the number).

### Inbound and Outbound Routing

- **Inbound routes:** Navigate to **Dialplan → Inbound Routes**. Routes are typically created automatically from the destinations you configured. Ensure your Telnyx connection's number format is set to E.164.
- **Outbound routes:** Navigate to **Dialplan → Outbound Routes**, click **Add**, select the **Telnyx** gateway, choose a **Dialplan Expression** (e.g., North America), and click **Save**.

### Register Extensions with a Device

Go to **Status → Registrations** and register your extensions using a softphone (such as Zoiper or X-Lite). Registered devices will appear on this page. Once registered, internal calls work by dialing the extension number, and external calls route through the Telnyx trunk.

## Additional Resources

- [Telnyx Mission Control getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Asterisk community help](https://community.asterisk.org/)
- [Asterisk documentation book](http://www.asteriskdocs.org/)
- [Vicidial support](https://www.vicidial.com/?page_id=151)
- [OSDial support](https://osdial.com/support/)
- [FreeSWITCH documentation](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/)
- [FusionPBX documentation](https://docs.fusionpbx.com/en/latest/)
- [FusionPBX quick install guide](https://docs.fusionpbx.com/en/latest/getting_started/quick_install.html)
