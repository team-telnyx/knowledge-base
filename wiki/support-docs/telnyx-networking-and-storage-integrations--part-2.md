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

*Part 2 of 7 — see also: [Part 1](telnyx-networking-and-storage-integrations--part-1.md), [Part 3](telnyx-networking-and-storage-integrations--part-3.md), [Part 4](telnyx-networking-and-storage-integrations--part-4.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md), [Part 6](telnyx-networking-and-storage-integrations--part-6.md), [Part 7](telnyx-networking-and-storage-integrations--part-7.md)*

This page consolidates Telnyx networking and storage integration guides, covering virtual cross connect (VXC) setup with AWS, Azure, Google Cloud, and Megaport, configuration of S3-compatible clients (Cyberduck, WAL-G, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP) with Telnyx Storage, and a WireGuard-based Cloud VPN tutorial for connecting a Digital Ocean Ubuntu server to the Telnyx network.

## Azure Virtual Cross Connect

This section provides instructions, technical details, and guidelines for integrating a [Microsoft Azure Cloud](https://azure.microsoft.com/en-us/) environment with the Telnyx network backbone.

**Pre-requisites**

- A Microsoft Azure cloud environment

**Step 1: Prepare your Microsoft account for an Azure Express Route**

1. Log into your [Azure Portal](https://portal.azure.com/#home).

![The Azure portal interface.](_images/afe3599b4c90ce84.png)
2. Perform a search for *express route* and click on **Express Route Circuits**.

![An open search tab for express route circuits.](_images/473d679738f44aa7.png)
3. Click **Add → Provider**. This provider *must* be *Equinix*. Do **NOT** select *Allow Classic Operations*. Rename other fields at your discretion.

![Provider addition tab.](_images/04bdee9281839c58.png)

![Microsoft Azure dashboard.](_images/a886509000445920.png)
4. Click **OK**.
5. Once the deployment completes, you will see your newly-provisioned Azure Express Route.

![Newly-provisioned Azure express route.](_images/1e223319babbed1a.png)

**Step 2: Set up the VXC in your Telnyx Mission Control Portal**

1. Log into your [Telnyx Mission Control Portal](https://portal.telnyx.com).
2. Click on **Networking** in the left-hand menu.

![Telnyx Mission Control Portal.](_images/ce72b790e3013644.png)
3. Click on the **Create New Network** button on the top-right.

!["Create New Network" button.](_images/aba0e7768d0e3e8c.png)
4. Give your network a name and click on the **Create Network** button.

!["Create Network" button.](_images/4fae7e1732e14348.png)
5. Once the Network is created, click on the **Add a Site** button.

!["Add a site" button.](_images/9a18ec397d061afe.png)
6. Choose the Telnyx Backbone Network you want to peer with.

![Telnyx Backbone Network selection table.](_images/16177156943b6a23.png)
7. Add the VXC by clicking on **Create VXC**.

!["Create VXC" add button.](_images/7bcf4a962b2792c9.png)
8. Create an Azure Express Route.

> **Note:** In order to complete this section, Stage 1 needs to have been completed.

![Azure Express Route creation portal.](_images/5bc7392afdc7fb42.png)
9. Key in the Azure Service Key and Microsoft Azure ASN. Typically it is **12076**.

![Azure Service Key and Microsoft Azure ASN credentials input.](_images/3ff1230ce0a8f6e8.png)

![Sample Service Key and ASN display.](_images/46792623108fd182.png)
10. Now create your VXC and submit it to the Telnyx Network team.

![VXC creation portal and submission button.](_images/23933c5d9b4429ba.png)

> Connection acceptance will be performed by the Telnyx Network Team.

![Routing and NAT configuration interface.](_images/ddeefdc918a0304c.png)

> **IMPORTANT:** Do NOT enable Routing status via the slider. This step has to be coordinated in sync with the Telnyx Network Team, as enabling this without backend configuration may blackhole your voice traffic.

**Step 3: Turn up routing and NAT configuration**

1. Arrange a maintenance activity and coordinate with Telnyx Network Engineering to turn on the routing. Please [contact Telnyx Support](https://telnyx.com/contact-us) to assist with this.

> **Note:** This activity has to be coordinated with the Network team to complete back-end configuration during the maintenance window.

2. Once you enable the circuit using the Routing Status slider, you should see a routing table in Express Route similar to the following:

![Routing and NAT configuration interface.](_images/d1b96d106ae67bb7.png)

Once enabled with routing, you'll see Telnyx public ranges via the Express Route Circuit. This will ensure that these are preferred over the Internet Routing Table.

![Routing table display.](_images/e5a1be5db1b8f53b.png)

**Additional documentation**

- [Microsoft Azure technical documentation](https://learn.microsoft.com/en-us/)
