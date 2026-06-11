---
title: Telnyx Storage
summary: Telnyx Storage is a high-performance, S3-compatible cloud storage service
  offering zero egress fees, 11 nines of durability, and built-in AI inference capabilities.
  It integrates with a wide range of third-party file transfer, backup, synchronization,
  and mounting tools through its S3-compatible API.
sources:
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6964272-use-rclone-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide
- url: https://support.telnyx.com/en/collections/3840515-telnyx-storage
updated_at: 2026-06-11T11:40:26Z
---

# Telnyx Storage

*Part 2 of 3 — see also: [Part 1](telnyx-storage--part-1.md), [Part 3](telnyx-storage--part-3.md)*

Telnyx Storage is a high-performance, S3-compatible cloud storage service offering zero egress fees, 11 nines of durability, and built-in AI inference capabilities. It integrates with a wide range of third-party file transfer, backup, synchronization, and mounting tools through its S3-compatible API.

## File Managers and Browsers

### S3 Browser

[S3 Browser](https://s3browser.com/) is a Windows GUI for managing files on S3-compatible storage with support for metadata, versioning, and access control policies.

1. Download and install [S3 Browser](https://s3browser.com/).
2. Click **Accounts** → **Add New Account** (or the popup on first launch).
3. Set **Account Type** to `S3 Compatible Storage`.
4. Enter: **REST Endpoint** = Telnyx API Endpoint, **Access Key ID** = Telnyx API Key, **Secret Access Key** = any placeholder.
5. Click **Add New Account**.

For more details, see the [S3 Browser user guides](https://s3browser.com/help.aspx).

### MSP360 Cloudberry Explorer

[MSP360 Cloudberry Explorer](https://www.msp360.com/explorer/) is a file manager for cloud storage supporting upload, download, metadata, versioning, and access control.

1. Download and install [MSP360 Cloudberry Explorer](https://www.msp360.com/explorer/).
2. Open the application and select **New Connection**.
3. Choose **S3 Compatible** as the connection type.
4. Enter: **Access Key** = Telnyx API Key, **Secret Key** = any placeholder, **Endpoint** = Telnyx API Endpoint, **Signature Version** = `AWS4`.
5. Click **OK**.

For more details, see the [MSP360 guides for Windows](https://help.msp360.com/explorer) and [Mac](https://help.msp360.com/explorer-for-macos).

### DragonDisk

[DragonDisk](http://www.s3-client.com/) is a file manager for Amazon S3 and other S3 API-compatible cloud storage.

1. Download and install [DragonDisk](http://www.s3-client.com/download-s3-compatible-cloud-client.html).
2. Click **File** → **Accounts** → **New**.
3. Set **Provider** to `Other S3 compatible service`.
4. Enter: **Service Endpoint** = `https://storage.telnyx.com`, **Access Key** = Telnyx API Key, **Secret Key** = any placeholder.
5. Click **OK**.

For more details, see the [DragonDisk FAQ](http://www.s3-client.com/faq.html).

## Command-Line and Sync Tools

### rclone

[rclone](https://rclone.org/) is a command-line tool for synchronizing files and directories to/from cloud storage and local file systems, supporting server-side file modification times, partial syncs, and more.

1. Install [rclone](https://rclone.org/install/).
2. Run `rclone config`.
3. Choose `n` (new remote), enter a name.
4. For **Option Storage**, choose `4` (Amazon S3 Compliant Storage Providers).
5. For **Option provider**, choose `34` (Any other S3 compatible provider).
6. For **Option env_auth**, choose `1` (Enter AWS credentials in the next step).
7. Enter **access_key_id** = Telnyx API Key.
8. Enter **secret_access_key** = any placeholder (no spaces, quotes, or special characters).
9. For **Option region**, choose `1` (v4 signatures, empty region).
10. Enter **Option endpoint** = Telnyx API Endpoint.
11. For **Option location_constraint**, leave empty or enter your region.
12. For **Option acl**, choose `1` (Owner gets full control).
13. For **Edit advanced config?**, type `n`.
14. For **Keep this remote?**, type `y`.
15. Type `q` to quit config.

For more details, see the [rclone S3 documentation](https://rclone.org/s3/).

## Backup Tools

### Arq Backup

[Arq Backup](https://www.arqbackup.com/) is a backup application supporting incremental backups, versioning, compression, encryption, and customizable schedules.

1. Download and install [Arq Backup](https://www.arqbackup.com/).
2. Click **New Storage Location**.
3. Select **S3-Compatible Server**.
4. Enter: **Server URL** = Telnyx API Endpoint, **Access Key ID** = Telnyx API Key, **Secret Access Key** = any placeholder, **Region** = matching region from endpoint.
5. Click **Connect**, then choose or create a bucket for backups.

For more details, see the [Arq Backup knowledge base](https://www.arqbackup.com/learn/).

### Backup4all

[Backup4all](https://www.backup4all.com/) is a comprehensive backup software supporting full, differential, and incremental backups with compression, encryption, and scheduling.

1. Download and install [Backup4all](https://www.backup4all.com/).
2. Click **File** → **New** to create a backup job.
3. For **Destination**, select **Online** → **S3 Compatible**.
4. Enter: **Endpoint** = Telnyx API Endpoint, **Access ID** = Telnyx API Key, **Secret Key** = any placeholder, **Region** = `default`, **Signature** = `Version 4`, **Bucket** = target bucket name.
5. Click **Next** and continue configuring your backup job.

For more details, see the [Backup4all help](https://www.backup4all.com/table-of-contents-help.html).

### Duplicati

[Duplicati](https://duplicati.com/) is an open-source backup solution with strong encryption, incremental/full backups, versioning, and scheduling.

1. Download and install [Duplicati](https://duplicati.com/).
2. Click **Add Backup** → **Configure a new backup** → **Next**.
3. In Step 2 (Destination), set **Storage Type** to `S3 Compatible`.
4. Enter: **Use SSL** = on, **Server** = `Custom Server URL` + Telnyx API Endpoint, **Bucket Name** = target bucket, **Bucket Create Region** = matching region, **AWS Access ID** = Telnyx API Key, **AWS Access Key** = any placeholder, **Client library** = `Amazon AWS SDK`.
5. Complete the remaining backup configuration steps.

For more details, see the [Duplicati manuals](https://duplicati.readthedocs.io/en/latest/).

### WAL-G

[WAL-G](https://github.com/wal-g/wal-g) is a backup and disaster recovery tool for PostgreSQL, enabling storage of WAL files on S3-compatible services.

1. Install [WAL-G](https://github.com/wal-g/wal-g#installation).
2. Follow the [S3 storage configuration](https://github.com/wal-g/wal-g/blob/master/docs/STORAGES.md#s3) and set:
   - `AWS_ACCESS_KEY_ID` = Telnyx API Key
   - `AWS_ENDPOINT` = Telnyx API Endpoint
   - `AWS_REGION` = matching region (e.g., `us-central-1`)
   - `AWS_S3_FORCE_PATH_STYLE` = `true`
   - `AWS_SECRET_ACCESS_KEY` = any placeholder
   - `WALE_S3_PREFIX` = `s3://<bucket-name>/`
   - `PGHOST` = your Postgres host
   - `PGPORT` = your Postgres port

For more details, see the [WAL-G documentation](https://github.com/wal-g/wal-g/tree/master/docs).

### Syncovery

[Syncovery](https://www.syncovery.com/) is a file synchronization and backup software with powerful scheduling and filtering features.

1. Download and install [Syncovery](https://www.syncovery.com/).
2. Click the green plus button to create a new profile.
3. Click the **Internet** button in the profile configuration.
4. In Internet Protocol Settings, set: **Protocol** = `S3`, **Access ID** = Telnyx API Key, **Secret key** = any placeholder, **Provider** = `custom`, **Bucket** = Telnyx API Endpoint.
5. Click **OK** to save the profile.

For more details, see the [Syncovery documentation](https://www.syncovery.com/category/documentation/).

### GoodSync

[GoodSync](https://www.goodsync.com/) is a file backup and synchronization tool ensuring data integrity and security across platforms.

1. Download and install [GoodSync](https://www.goodsync.com/download).
2. Create a GoodSync account.
3. Click **New Job**, name it, and select **Synchronize**.
4. Click the folder icon and select **Amazon S3**.
5. Enter: **Server address** = Telnyx API Endpoint, **AWS Access key** = Telnyx API Key, **AWS Secret Access Key** = any placeholder.
6. Click **Test and Save**.

For more details, see the [GoodSync documentation](https://www.goodsync.com/goodsync-storage).
