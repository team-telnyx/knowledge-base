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

*Part 3 of 3 — see also: [Part 1](telnyx-storage--part-1.md), [Part 2](telnyx-storage--part-2.md)*

Telnyx Storage is a high-performance, S3-compatible cloud storage service offering zero egress fees, 11 nines of durability, and built-in AI inference capabilities. It integrates with a wide range of third-party file transfer, backup, synchronization, and mounting tools through its S3-compatible API.

## Cloud Mounting Tools

### CloudMounter

[CloudMounter](https://cloudmounter.net/) mounts cloud storage services directly on your computer for seamless access and synchronization.

1. Download and install [CloudMounter](https://cloudmounter.net/).
2. Select **Amazon S3** as the storage type.
3. Enter: **Access Key** = Telnyx API Key, **Secret Key** = any placeholder, **Server Endpoint** = Telnyx API Endpoint, **Bucket** = bucket name.
4. Click **Mount**.

For more details, see the [CloudMounter blog](https://cloudmounter.net/blog/).

### ExpanDrive

[ExpanDrive](https://www.expandrive.com/) mounts cloud storage as a local drive, providing a unified interface across multiple providers.

1. Download and install [ExpanDrive](https://www.expandrive.com/desktop/).
2. Click **ExpanDrive** → **New Connection**.
3. Select **Amazon S3**.
4. Enter: **Server** = Telnyx API Endpoint, **Access Key** = Telnyx API Key, **Secret Key** = any placeholder, **Custom Region** = matching region, **Bucket** = bucket name (optional).
5. Click **Save**.

For more details, see the [ExpanDrive blog](https://www.expandrive.com/).

### ODrive

[ODrive](https://www.odrive.com/) is a synchronization tool that syncs files across multiple devices and cloud storage services.

1. Download and install [ODrive](https://docs.odrive.com/docs/odrive-usage-guide#install-desktop-sync).
2. Click **Link Storage**.
3. Select **Amazon S3/S3 Compatible**.
4. Enter: **Host** = Telnyx API Endpoint, **Bucket Name** = bucket name, **Access Key ID** = Telnyx API Key, **Secret Key ID** = any placeholder, **Default Storage Class** = `Standard`.
5. Authorize the connection.

For more details, see the [ODrive documentation](https://docs.odrive.com/docs).

### WebDrive

[WebDrive](https://southrivertech.com/) is a file transfer client supporting a wide range of protocols for accessing and managing remote files.

1. Download and install [WebDrive](https://southrivertech.com/webdrive/).
2. Click the **+** button to create a new connection.
3. Select **Amazon S3** as the connection type.
4. Enter: **Access Key** = Telnyx API Key, **Secret Key** = any placeholder (no spaces or special characters), **Bucket** = bucket name (optional).
5. In **Advanced Settings**, set the custom server URL to a Telnyx API Endpoint.
6. Click **Save**, then select the connection and click the connect button.

For more details, see the [WebDrive blog](https://southrivertech.com/blog/).

### NetDrive3

[NetDrive3](https://netdrive.net/) is a remote storage mapping tool that mounts cloud storage as a virtual drive.

1. Download and install [NetDrive3](https://netdrive.net/).
2. Click the **+** button to create a new connection.
3. Select **S3** as the storage type and click **Connect**.
4. Enter: **Server Address** = Telnyx API Endpoint, **Access ID** = Telnyx API Key, **Secret Key** = any placeholder (no spaces or special characters), **Bucket name** = bucket name.
5. Click **OK**, then **Connect**.

For more details, see the [NetDrive3 documentation](https://netdrive.net/support/).

## Managed Service Providers

For MSPs and resellers, Telnyx Storage can be used to scale disaster recovery and backup/restore services across your client base, leveraging the zero egress fee model and S3-compatible API for easy integration with existing tooling.
