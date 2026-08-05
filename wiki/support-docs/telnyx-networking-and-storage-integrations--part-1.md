---
title: Telnyx Networking and Storage Integrations
summary: This page consolidates Telnyx support documentation covering Megaport network
  integration, Telnyx Storage configuration with third-party S3-compatible clients
  (Cyberduck, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP), and Telnyx Networking
  setup across Global Edge Router, Ubuntu, Azure Linux VMs, Oracle VMs, and pfSense
  using WireGuard-based Cloud VPN.
sources:
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
updated_at: 2026-08-05T13:35:29Z
---

# Telnyx Networking and Storage Integrations

*Part 1 of 5 — see also: [Part 2](telnyx-networking-and-storage-integrations--part-2.md), [Part 3](telnyx-networking-and-storage-integrations--part-3.md), [Part 4](telnyx-networking-and-storage-integrations--part-4.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md)*

This page consolidates Telnyx support documentation covering Megaport network integration, Telnyx Storage configuration with third-party S3-compatible clients (Cyberduck, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP), and Telnyx Networking setup across Global Edge Router, Ubuntu, Azure Linux VMs, Oracle VMs, and pfSense using WireGuard-based Cloud VPN.

## Megaport Configuration with Telnyx

[Megaport](https://www.megaport.com/) is a global Network as a Service provider that uses SDN to provision instant, dedicated access to AWS Direct Connect across hundreds of global locations. Configuring Megaport with Telnyx establishes a private network connection between the two platforms.

**Pre-requisites**

- Ensure that your Telnyx Mission Control Portal is configured properly.
- Recommended: enable TLS to encrypt your traffic.
- Megaport ports must be live on both ends.

**Create a connection between Telnyx and the Megaport portal**

1. Log into your Megaport portal account.
2. Click **+ Connection**.
3. Click **Enter Service Key**.

   ![Telnyx and the Megaport portal connection portal.](_images/f13082bb30c5ad76.png)

   ![Telnyx and the Megaport portal connection portal.](_images/057547cd742706d5.png)
4. Provide the following information:
   1. **Megaport Service Key ID:** Enter the service key provided by Telnyx. The data from this key will populate. If you did not receive a service key, or are unsure, contact Telnyx Support.

      ![Megaport service key ID credentials input tab.](_images/28e07903cb21fb6f.png)
5. Once you've entered your service key, the details on your screen will update.

   ![Megaport service key ID credentials input tab.](_images/41357a4279847fa4.png)
6. Click **Next**.
7. Confirm the following auto-filled details:
   1. **Name your connection:** Choose a name that helps you easily identify the connection and its purpose.
   2. **Rate limit:** Caps how often an action can be repeated within a certain timeframe, helping to mitigate malicious bot activity.
   3. **Preferred A-End VLAN:** Each VXC is delivered as a separate VLAN on your Port. This must be a unique VLAN ID on this Port and can range from 2 to 4093. If you specify a VLAN ID that is already in use, the system displays the next available VLAN number. The VLAN ID must be unique to proceed with the order. If you don't specify a value, Megaport will assign one.

      ![Preferred A-End VLAN tab.](_images/6b3c3ea3fb5f94b9.png)
8. Click **Next**.
9. Once you've confirmed all your details, click **Add VXC** to update your ordering cart.

   ![VXC addition tab.](_images/adad8cdfc526f83d.png)
10. View your cart and click **Order**. This sends an email to Telnyx for approval. Once Telnyx approves your connection, the VXC between your Megaport setup and Telnyx is created.

    ![Megaport configured services portal.](_images/0356891d589f268e.png)

Additional resources: [Megaport documentation](https://docs.megaport.com/), [Megaport support](https://docs.megaport.com/support/contact/), and [Megaport resource center](https://www.megaport.com/resources/).
