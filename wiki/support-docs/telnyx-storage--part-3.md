---
title: Telnyx Storage
summary: Telnyx Storage is a high-performance, S3-compatible cloud storage service
  offering zero egress fees, 11 nines of durability, and built-in AI inference capabilities.
  It integrates with a wide range of third-party file transfer, backup, synchronization,
  and mounting tools through its S3-compatible API.
sources:
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
  content_hash: ce856b087527454b12dcf9ffe18698cea283e88b51155b2ef8fca7672366a78e
- url: https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage
  content_hash: 8c3363d04af90383149fbe2f07d2972ecc406fad9df330382ccf59866d71f30a
- url: https://support.telnyx.com/en/articles/6964272-use-rclone-with-telnyx-storage
  content_hash: 6ccdc59ac5425a54897005a4a45b953f8e9239f5c4c3592c6397249ca73ec93e
- url: https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage
  content_hash: 1717adf9dbe35685300026b2acf08c68aed20fd5ad44d6ee8cc0c704c1531a26
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
  content_hash: fd1bdcd712ad3c97ee3f43068ebfdff51591857950e24cb90bcd4b9c22e1f3b9
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
  content_hash: f160519ca1bc4d9563ab1d450213839df15760009830435c8301bbbad1bff121
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
  content_hash: c338a8efbf3221be82b4d4d20e4e9092449005fe9865abfac43ad996d107928a
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
  content_hash: 03fc6df113ff9b1ba3217c16bf249474d8268499d1c32f086639ac21881553a6
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
  content_hash: 26b4929d4efed90980590836f05e4241e8a06378c5838fd383558a9340067308
- url: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage
  content_hash: d91d978d2dd83b93bf1b13c5288295f401b1d2eff8997a6cd59a3c5c4fb351c8
- url: https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage
  content_hash: 0e7318eb0e3558d3208ce11166feb95d69ae65e6938c622719f9bb565a7587d9
- url: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage
  content_hash: c921e5f591f586c7ac9b21069ced71abec87c457d7aaad0602b8ae432869938a
- url: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage
  content_hash: b7f5f792ce8d028b430de3145c55ec3c1ba4ad66d50479e604148bb7b178750d
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
  content_hash: 2c6dee4097bce1e48b1173c4654844974c6264c79b07a14edd54cf5b727541d8
- url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
  content_hash: 081dde242f1e42b5ad645456153225232ff9bcc784578d3d8c4b8e1ab282bd25
- url: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage
  content_hash: caffa5ee8e437c624df5bb05d454de3554514a262566ffec4cbda27e220e2645
- url: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage
  content_hash: 7607134056808935582a90d43a6347439dd0041cb1d444ac3235b796e8b22be4
- url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
  content_hash: a91f8aecc9dffe3abe1acfcb5313bdfbb6b81c9177271d763dc18c001405d5b6
- url: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide
  content_hash: e94257cf1f2641e30ab656b1783772881f51ab1200f6ca7b058ef119c41574bd
- url: https://support.telnyx.com/en/collections/3840515-telnyx-storage
  content_hash: a40e820e277805fadcdc719482b1dfadd9b561210b046d9f07f45d5750b4b959
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
