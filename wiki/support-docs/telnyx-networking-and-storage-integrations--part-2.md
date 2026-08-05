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

*Part 2 of 5 — see also: [Part 1](telnyx-networking-and-storage-integrations--part-1.md), [Part 3](telnyx-networking-and-storage-integrations--part-3.md), [Part 4](telnyx-networking-and-storage-integrations--part-4.md), [Part 5](telnyx-networking-and-storage-integrations--part-5.md)*

This page consolidates Telnyx support documentation covering Megaport network integration, Telnyx Storage configuration with third-party S3-compatible clients (Cyberduck, Arq Backup, Backup4all, Duplicati, WinSCP, CrossFTP), and Telnyx Networking setup across Global Edge Router, Ubuntu, Azure Linux VMs, Oracle VMs, and pfSense using WireGuard-based Cloud VPN.

## Telnyx Storage with S3-Compatible Clients

Telnyx Storage is an S3-compatible object storage service. The following third-party clients can be configured to work with Telnyx Storage by pointing them at a Telnyx [API endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints) and authenticating with a [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys). In every case, the secret access key is not used by Telnyx Storage, but the client will complain if it doesn't exist — type any value without spaces, quoting, or special characters.

### Cyberduck

[Cyberduck](https://cyberduck.io/) is a free, open-source file transfer client for macOS and Windows.

1. Download and install the latest version of [Cyberduck](https://cyberduck.io/download/).
2. Open Cyberduck and click **Open Connection**.

   ![Options dropdown of the Open Connection section of the Cyberduck application.](_images/bd5402deb4937df2.png)
3. Choose **Amazon S3** as the connection type.

   ![Cyberduck Amazon S3 interface.](_images/a9eaaf2c721269ce.png)
4. Enter the following:
   - **Server:** A Telnyx API endpoint.
   - **Port:** 443
   - **Access Key ID:** Your Telnyx API Key.
   - **Secret Access Key:** Any value without spaces, quoting, or special characters.
5. Click **Connect**. All of your buckets will appear in the Cyberduck UI.

For more information, see the [Cyberduck developer documentation](https://docs.cyberduck.io/cyberduck/).

### Arq Backup

[Arq Backup](https://www.arqbackup.com/) is a backup software designed for developers that securely backs up files to various storage providers, with features such as incremental backups, versioning, compression, and encryption.

1. Download and install the latest version of [Arq Backup](https://www.arqbackup.com/).
2. Open Arq Backup and click **New Storage Location**.

   ![New Storage Location button.](_images/7d31ff844def87be.png)
3. Select **S3-Compatible Server**.

   ![S3-Compatible Server button.](_images/d91b54b8b659799a.png)
4. Enter the following and click **Connect**:
   - **Server URL:** A Telnyx API endpoint.
   - **Access Key ID:** Your Telnyx API Key.
   - **Secret Access Key:** Any value without spaces, quoting, or special characters.
   - **Region:** The matching region from the API endpoints list (for example, `us-central-1` for `https://us-central-1.telnyxstorage.com`).

   ![Bucket name section.](_images/2cf3809694e214c3.jpg)
5. Choose an existing bucket or create a new one.

   ![Bucket creation section.](_images/a5f7ae7e179f6526.png)

   ![Telnyx storage section.](_images/62047945f6cb40f0.png)

For more information, see the [Arq Backup knowledge base](https://www.arqbackup.com/learn/).

### Backup4all

[Backup4all](https://www.backup4all.com/) is a comprehensive backup software that supports full, differential, and incremental backups, compression, encryption, scheduling, and backup verification.

1. Download and install the latest version of [Backup4all](https://www.backup4all.com/).
2. Click **File** and **New** to create a new backup job.
3. For **Destination**, select **Online** in the left navigation bar and then select **S3 Compatible** from the dropdown.

   ![S3 Compatible button.](_images/a79df60c63cddc8d.jpg)
4. Enter the following and click **Next**:
   - **Endpoint:** A Telnyx API endpoint.
   - **Access ID:** Your Telnyx API Key.
   - **Secret Key:** Any value without spaces, quoting, or special characters.
   - **Region:** `default`
   - **Signature:** Version 4
   - **Bucket:** The name of the bucket you want your data stored in.

   ![Backup sources settings section.](_images/7785c78728b2daa7.jpg)

For more information, see [Backup4all product resources](https://www.backup4all.com/table-of-contents-help.html).

### Duplicati

[Duplicati](https://duplicati.com/) is an open-source backup software that supports strong encryption, incremental and full backups, versioning, and scheduling.

1. Download and install the latest version of [Duplicati](https://duplicati.com/).
2. Open Duplicati, click **Add Backup**, select **Configure a new backup**, and click **Next**.

   ![New backup configuration settings.](_images/3c06a15e63bfa6a0.jpg)
3. In the **Storage Type** dropdown, select **S3 Compatible**.

   ![Storage type settings.](_images/1603ad57fd5f79ff.jpg)
4. Enter the following:
   - **Use SSL:** toggled on
   - **Server:** Select `Custom Server URL` and enter a Telnyx API endpoint.
   - **Bucket Name:** An existing bucket name or a new one to create.
   - **Bucket Create Region:** The matching region from the API endpoints list (for example, `us-central-1` for `https://us-central-1.telnyxstorage.com`).
   - **Storage class:** default
   - **AWS Access ID:** Your Telnyx API Key.
   - **AWS Access Key:** Any value without spaces, quoting, or special characters.
   - **Client library to use:** Amazon AWS SDK

   ![Backup destination settings.](_images/6535ef1efb562c7c.jpg)

For more information, see the [Duplicati manuals](https://duplicati.readthedocs.io/en/latest/).

### WinSCP

[WinSCP](https://winscp.net/eng/index.php) is an open-source SFTP, FTP, and SCP client for Windows.

1. Download and install the latest version of [WinSCP](https://winscp.net/eng/index.php).
2. Click **New Session**.

   ![WinSCP New session button.](_images/b1bc59e87ce5cac9.jpg)

   ![Modal for configuration.](_images/bcade6701ed8d465.jpg)
3. For **File Protocol**, select **Amazon S3**.

   ![File protocol settings page.](_images/b580b530cdc7f534.jpg)
4. Enter the following and click **Login**:
   - **Host name:** A Telnyx API endpoint.
   - **Port number:** 443
   - **Access key ID:** Your Telnyx API Key.
   - **Secret access key:** Any value without spaces, quoting, or special characters.

   ![Login fields.](_images/90921108b6041660.jpg)

For more information, see the [WinSCP support documentation](https://winscp.net/eng/docs/start).

### CrossFTP

[CrossFTP](https://www.crossftp.com) is a feature-rich FTP client that supports multi-threading, synchronization, and encryption.

1. Download and install the latest version of [CrossFTP](https://www.crossftp.com/download.htm).
2. Launch CrossFTP and click **File** → **Site Connect** to open the Site Manager.

   ![Site manager window.](_images/e9d4a420a306343f.png)
3. Select **S3** from the **Protocol** dropdown and fill in the fields:
   - **Protocol:** S3/HTTPS
   - **Label:** Any name (for example, your nickname).
   - **Host:** A Telnyx API endpoint.
   - **Port:** 443
   - **Access Key:** Your Telnyx API Key.
   - **Secret:** Any value without spaces, quoting, or special characters.
   - **Proxy/Firewall:** Use Global Setting.
   - **Remote Path:** The name of your bucket (available in the [Telnyx portal](https://portal.telnyx.com/#/app/storage/buckets)).
   - **Local Path:** A path from your local storage.
   - **CNAME:** Leave blank.
   - **Comments:** Optional.

   ![Site manager section.](_images/db980e535087acaf.jpg)
4. Click **Connect** to test the connection.

For more information, see [CrossFTP features](https://www.crossftp.com/features.htm).
