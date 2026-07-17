---
title: Telnyx Networking and Storage Integrations
summary: This page consolidates Telnyx networking and storage integration guides,
  covering virtual cross connect (VXC) setup with AWS, Azure, Google Cloud, and Megaport,
  configuration of S3-compatible clients (Cyberduck, WAL-G, Arq Backup, Backup4all,
  Duplicati, WinSCP, CrossFTP) with Telnyx Storage, and a WireGuard-based Cloud VPN
  tutorial for connecting a Digital Ocean Ubuntu server to the Telnyx network.
sources:
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
updated_at: 2026-07-17T09:09:23Z
---

# Telnyx Networking and Storage Integrations

*Part 4 of 7 — see also: [Part 1](telnyx-networking-and-storage-integrations--part-1.md), [Part 2](telnyx-networking-and-storage-integrations--part-2.md), [Part 3](telnyx-networking-and-storage-integrations--part-3.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md), [Part 6](telnyx-networking-and-storage-integrations--part-6.md), [Part 7](telnyx-networking-and-storage-integrations--part-7.md)*

This page consolidates Telnyx networking and storage integration guides, covering virtual cross connect (VXC) setup with AWS, Azure, Google Cloud, and Megaport, configuration of S3-compatible clients (Cyberduck, WAL-G, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP) with Telnyx Storage, and a WireGuard-based Cloud VPN tutorial for connecting a Digital Ocean Ubuntu server to the Telnyx network.

## Megaport Configuration

[Megaport](https://www.megaport.com/) is a global leading Network as a Service provider transforming the way businesses connect to AWS Cloud. Their SDN and easy-to-use portal enable users to provision instant and dedicated access to AWS Direct Connect across hundreds of global locations.

**Pre-requisites**

- Ensure that your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- Megaport ports must be live on both ends

**Step 1: Create a connection between Telnyx and the Megaport portal**

In this section, you'll set up a configuration from the customer side to connect Telnyx to your Megaport portal. This needs to be done in order to use the service key provided by Telnyx.

1. Log into your Megaport portal account.
2. Click **+ Connection**.
3. Click **Enter Service Key**.

![Telnyx and the Megaport portal connection portal.](_images/f13082bb30c5ad76.png)

![Telnyx and the Megaport portal connection portal.](_images/057547cd742706d5.png)
4. Provide the following information:
   1. **Megaport Service Key ID:** Enter the service key provided by Telnyx. The data from this key will populate. If you did not receive a service key, or are unsure, contact Telnyx Support.

![Megaport service key ID credentials input tab.](_images/28e07903cb21fb6f.png)
5. Once you've entered your service key, you'll notice that the details have updated on your screen.

![Megaport service key ID credentials input tab.](_images/41357a4279847fa4.png)
6. Click **Next**.
7. You'll be taken to a form where you'll need to confirm the following auto-filled details:
   1. **Name your connection:** You can name this anything you like. We recommend something that can help you easily identify your connection and its purpose.
   2. **Rate limit:** This limits network traffic and puts a cap on how often someone can repeat an action within a certain timeframe – for instance, trying to log in to an account. Rate limiting can help stop certain kinds of malicious bot activity.
   3. **Preferred A-End VLAN:** Each VXC is delivered as a separate VLAN on your Port. This must be a unique VLAN ID on this Port and can range from 2 to 4093. If you specify a VLAN ID that is already in use, the system displays the next available VLAN number. The VLAN ID must be unique to proceed with the order. If you don't specify a value, Megaport will assign one.

![Preferred A-End VLAN tab.](_images/6b3c3ea3fb5f94b9.png)
8. Click **Next**.
9. Once you've confirmed all your details, click **Add VXC** to update your ordering cart.

![VXC addition tab.](_images/adad8cdfc526f83d.png)
10. When you're ready, view your cart and click on **Order**. This will send an email to Telnyx for approval. Once Telnyx approves your connection, this creates the VXC between your Megaport setup and Telnyx.

![Megaport configured services portal.](_images/0356891d589f268e.png)

**Additional resources**

- [Megaport documentation](https://docs.megaport.com/)
- [Megaport support](https://docs.megaport.com/support/contact/)
- [Megaport resource center](https://www.megaport.com/resources/)
