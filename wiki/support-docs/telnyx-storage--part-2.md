---
title: Telnyx Storage
summary: Telnyx Storage is a high-performance, S3-compatible cloud storage service
  offering 11 nines of durability, zero egress fees, and seamless integration with
  a wide range of third-party tools. This page explains how to create and manage storage
  buckets, use the built-in AI features for summarization and inference, and configure
  popular S3 clients and backup utilities to work with Telnyx Storage.
sources:
- url: https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6964272-use-rclone-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide
- url: https://support.telnyx.com/en/collections/3840515-telnyx-storage
updated_at: 2026-08-05T13:37:50Z
---

# Telnyx Storage

*Part 2 of 3 — see also: [Part 1](telnyx-storage--part-1.md), [Part 3](telnyx-storage--part-3.md)*

Telnyx Storage is a high-performance, S3-compatible cloud storage service offering 11 nines of durability, zero egress fees, and seamless integration with a wide range of third-party tools. This page explains how to create and manage storage buckets, use the built-in AI features for summarization and inference, and configure popular S3 clients and backup utilities to work with Telnyx Storage.

## Configure S3-compatible clients

The following guides walk through configuring popular S3-compatible tools to work with Telnyx Storage. Each tool uses the common configuration values above.

### MSP360 Cloudberry Explorer

[MSP360 Cloudberry Explorer](https://www.msp360.com/explorer/) is a user-friendly file manager for transferring data to and from many cloud storage providers.

1. Download and install MSP360 Cloudberry Explorer from [msp360.com/explorer](https://www.msp360.com/explorer/).
2. Open the application and create a new **Connection**.

   ![MSP360 Cloudberry Explorer application page. ](_images/994fa05e4548026c.png)
3. Choose **S3 compatible** as the connection type.

   ![MSP360 Cloudberry Explorer application options for choosing connection type. ](_images/09f73d2eb4d3e6bb.png)
4. Enter the connection settings and click **OK**:
   - **Display Name** — any nickname you like.
   - **Access Key** — your Telnyx API Key.
   - **Secret Key** — any value without spaces, quotes, or special characters.
   - **Endpoint** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Signature Version** — `AWS4`.

   ![S3 compatible fields. ](_images/855259eec2500eb7.jpg)
5. The new connection appears in the navigation bar; clicking it lists your buckets.

   ![Various buckets in the S3 compatible fields. ](_images/607a7d8f55545286.png)

Additional resources: [MSP360 Explorer guides for Windows](https://help.msp360.com/explorer) and [MSP360 Explorer guides for Mac](https://help.msp360.com/explorer-for-macos).

### rclone

[Rclone](https://rclone.org/) is a command-line tool for synchronising files and directories to and from many cloud storage providers.

1. Install rclone from [rclone.org/install](https://rclone.org/install/).
2. Run `rclone config` and answer the prompts:
   - `n` — create a new remote.
   - **Name** — any name you like.
   - **Storage** — option `4` (Amazon S3 Compliant Storage Providers).
   - **Provider** — option `34` (Any other S3 compatible provider).
   - **env_auth** — option `1` (enter AWS credentials in the next step).

   ![Rclone terminal. ](_images/ace0c3036de3dccc.gif)
   - **access_key_id** — your Telnyx API Key.
   - **secret_access_key** — any value without spaces, quotes, or special characters.
   - **region** — option `1` (v4 signatures, empty region).
   - **endpoint** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **location_constraint** — leave empty, or enter a Telnyx region.
   - **acl** — option `1` (owner gets full control).
   - **Edit advanced config?** — `n`.
   - **Keep this remote?** — `y`.
3. Type `q` to quit the config.

Additional resources: [rclone S3 documentation](https://rclone.org/s3/).

### S3 Browser

[S3 Browser](https://s3browser.com/) is a GUI client for managing files on S3-compatible storage.

1. Download and install S3 Browser from [s3browser.com](https://s3browser.com/).
2. On first launch, the **Add New Account** window appears. Otherwise, click **Accounts → Add New Account**.

   !["Add new account" section of the S3 browser. ](_images/00f92ae7e033dd33.jpg)
3. Enter the account details and click **Add New Account**:
   - **Display Name** — any name you like.
   - **Account Type** — `S3 Compatible Storage`.
   - **REST Endpoint** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Access Key ID** — your Telnyx API Key.
   - **Secret Access Key** — any value without spaces, quotes, or special characters.

   !["Add new account" section of the S3 browser. ](_images/7a0b16f53373f98a.png)

Existing buckets appear in the application window once the account is added.

![Pictures of previously created buckets. ](_images/2c7efb9c91d62166.jpg)

Additional resources: [S3 Browser user guides](https://s3browser.com/help.aspx).

### Syncovery

[Syncovery](https://www.syncovery.com/) is a file synchronisation and backup tool.

1. Download and install Syncovery from [syncovery.com](https://www.syncovery.com/).
2. Launch Syncovery.

   ![Profile overview section of Syncovery. ](_images/263e26fd4404ba65.png)
3. Click the green **+** button to create a new profile.

   ![New Profile section of Syncovery. ](_images/567f14e127a5f906.png)
4. In the profile configuration window, click **Internet**.

   ![Source and destination profile section of Syncovery. ](_images/48547ad210e82f23.png)
5. In **Internet Protocol Settings**, enter:
   - **Protocol** — `S3`.
   - **Access ID** — your Telnyx API Key.
   - **Secret key** — any value without spaces, quotes, or special characters.
   - **Provider** — `custom`.
   - **Bucket** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Folder** — the local folder to back up.

   ![Internet protocol settings section. ](_images/d44de1d00f7fdd23.jpg)
6. Choose the destination path (**Browse…**, **Internet…**, or **Device**).

   ![Browse, internet, and device buttons. ](_images/e30741c2897b9ebf.png)
7. Click **OK** to save the profile.

   ![Okay button. ](_images/8c283a528946aed1.png)

Additional resources: [Syncovery documentation](https://www.syncovery.com/category/documentation/).

### GoodSync

[GoodSync](https://www.goodsync.com/) is a file backup and synchronisation tool.

1. Download and install GoodSync from [goodsync.com/download](https://www.goodsync.com/download) and create an account.
2. Click **New Job**.

   ![New job button. ](_images/7303af481195c2e1.png)
3. Enter a job name, set **Job type** to **Synchronize**, and click **OK**.

   ![Synchronize section. ](_images/7303af481195c2e1.png)
4. Click the folder icon to choose a folder.

   ![Testjob section. ](_images/9a621c2279c656c4.png)
5. Select **Amazon S3** from the list.

   ![Amazon S3 button. ](_images/7cae0b4a5ce00ed9.png)
6. Enter the bucket details:
   - **Server address** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **AWS Access key** — your Telnyx API Key.
   - **AWS Secret Access Key** — any value without spaces, quotes, or special characters.

   Click **Test** and **Save**.

   ![Amazon S3 section. ](_images/5ad146bf21f62498.jpg)
7. The bucket appears in the Amazon S3 folder dropdown.

   ![Amazon S3 Folder. ](_images/bccc72e665c80ce5.png)

Additional resources: [GoodSync documentation](https://www.goodsync.com/goodsync-storage).

### CloudMounter

[CloudMounter](https://cloudmounter.net/) mounts cloud storage as a local drive.

1. Download and install CloudMounter from [cloudmounter.net](https://cloudmounter.net/).
2. Launch the application.

   ![CloudMounter interface. ](_images/a5005a4bcb179bbe.png)
3. Select **Amazon S3** as the storage type.

   ![Amazon S3 interface. ](_images/a4f132e567392f47.png)
4. Fill in the connection details:
   - **Name** — your name.
   - **Access Key** — your Telnyx API Key.
   - **Secret Key** — any value without spaces, quotes, or special characters.
   - **Server Endpoint** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Bucket** — a bucket name from the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section of the Telnyx portal.

   ![Amazing S3 connections settings. ](_images/c8efefab684d7737.jpg)
5. Click **Mount** to connect.

Additional resources: [CloudMounter blog](https://cloudmounter.net/blog/).

### DragonDisk

[DragonDisk](http://www.s3-client.com/) is a file manager for S3-compatible storage.

1. Download and install DragonDisk from [s3-client.com](http://www.s3-client.com/download-s3-compatible-cloud-client.html).
2. Open DragonDisk, click **File → Accounts**.

   ![File section. ](_images/0cc197bf7008c26d.png)
3. In the **Accounts** window, click **New**.

   ![Accounts section. ](_images/0c160bcae415fb8e.png)
4. Select **Other S3 compatible service** from the **Provider** dropdown and fill in:
   - **Service Endpoint** — `https://storage.telnyx.com`.
   - **Account name** — any nickname.
   - **Comment** — any reminder text.
   - **Access Key** — your Telnyx API Key.
   - **Secret Key** — any value without spaces, quotes, or special characters.

   ![Advanced settings of the account section. ](_images/a8ef9c5705106fec.png)
5. Click **OK** to save.

Additional resources: [DragonDisk FAQ](http://www.s3-client.com/faq.html).

### ExpanDrive

[ExpanDrive](https://www.expandrive.com/) mounts cloud storage as a local drive.

1. Download and install ExpanDrive from [expandrive.com/desktop](https://www.expandrive.com/desktop/).
2. Launch ExpanDrive and click **ExpanDrive → New Connection**.

   ![ExpanDrive section. ](_images/ed62ee9807d50ecd.png)
3. Select **Amazon S3** from the storage options.

   ![Amazon s3 button. ](_images/3d5c0bf65065502a.png)
4. Fill in the storage options:
   - **Server** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Access Key** — your Telnyx API Key.
   - **Secret Key** — any value without spaces, quotes, or special characters.
   - **Custom Region** — the matching region from the [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints) page (for example, `us-central-1` for `https://us-central-1.telnyxstorage.com`).
   - **Nickname** — any name you like.
   - **Bucket** — a bucket name, or leave blank.
   - **Drive Letter** — any available local drive letter.

   ![Storage options section. ](_images/ad0927067aa545b9.jpg)
5. Click **Save**. ExpanDrive authenticates with Telnyx Storage using the API key.

   ![Telnyx Storage files section. ](_images/674fe6b4d0f52077.png)

Additional resources: [ExpanDrive blog](https://www.expandrive.com/).

### ODrive

[ODrive](https://www.odrive.com/) is a multi-cloud synchronisation tool.

1. Download and install ODrive from the [ODrive usage guide](https://docs.odrive.com/docs/odrive-usage-guide#install-desktop-sync).
2. Launch ODrive and click **Link Storage**.

   ![Link storage section. ](_images/590024570634230b.png)
3. Select **Amazon S3/S3 Compatible** from the list.

   ![Various storage choices. ](_images/db39768029440500.png)
4. Fill in the connection details:
   - **Name** — any nickname.
   - **Host** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Bucket Name** — a bucket from the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section of the Telnyx portal.
   - **Access Key ID** — your Telnyx API Key.
   - **Secret Key ID** — any value without spaces, quotes, or special characters.
   - **Default Storage Class** — `Standard`.
   - **Directory Structure** — `Simple` or `Delimited`.

   ![Directory structure. ](_images/14813d583656a3c7.jpg)
5. After authorising, ODrive links Telnyx Storage as a storage provider.

   ![ODrive App. ](_images/69033bb014159b50.png)

Additional resources: [ODrive documentation](https://docs.odrive.com/docs).

### WebDrive

[WebDrive](https://southrivertech.com/) is a file transfer client that supports many remote protocols.

1. Download and install WebDrive from [southrivertech.com/webdrive](https://southrivertech.com/webdrive/).
2. Launch WebDrive and click the **+** button to create a new connection.

   ![WebDrive homepage. ](_images/f592a7f32a0d5ef5.png)
3. Select **Amazon S3** as the connection type.

   ![Amazon S3 setup. ](_images/32fcd92b1541b9af.png)
4. Enter the connection settings and click **Save**:
   - **Connection Name** — any nickname.
   - **Access Key** — your Telnyx API Key.
   - **Secret Key** — any value without spaces, quotes, or special characters.
   - **Bucket** — a bucket name from the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section, or leave blank.
   - **Drive Letter** — a local drive letter.
   - **Advanced Settings** — set the custom server URL to a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).

   ![Connection Settings section. ](_images/7a4e4671480fa5bc.jpg)
5. Click **Save**, then select the new connection and click the **box** object button to connect.

   ![Save button. ](_images/65bd4844bb2aebe2.png)

   ![Box object button. ](_images/572934f8a5dcf383.png)

Additional resources: [WebDrive blog](https://southrivertech.com/blog/).

### NetDrive3

[NetDrive3](https://netdrive.net/) maps remote storage as a virtual drive.

1. Download and install NetDrive3 from [netdrive.net](https://netdrive.net/).
2. Launch NetDrive3 and click the **+** button to create a new connection.

   ![NetDrive3 start page. ](_images/fd46f50d5e1371f1.png)
3. In **Add a Personal Drive**, select **S3** as the storage type and click **Connect**.

   !["Add a Personal Drive" window. ](_images/2a716c80be2dd9cf.png)
4. Fill in the connection details:
   - **Server Address** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Access ID** — your Telnyx API Key.
   - **Secret Key** — any value without spaces or special characters.
   - **Bucket name** — a bucket from the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section.
5. After saving, **S3** appears as a storage type with a remote path based on the bucket name. Click **OK** to continue.

   ![Personal storage type addition section. ](_images/4456da3065a23210.png)
6. Click **Connect** to link NetDrive3 with Telnyx Storage.

   ![NetDrive3 - Telnyx connection setup. ](_images/377dede35e60841a.png)
7. Once connected, Telnyx Storage appears as a virtual drive.

   ![Telnyx storage on NetDrive3. ](_images/c73646827087e6e7.png)

Additional resources: [NetDrive3 documentation](https://netdrive.net/support/).

### AirExplorer

[AirExplorer](https://www.airexplorer.net/en/) is a multi-cloud file management application.

1. Download and install AirExplorer from [airexplorer.net](https://www.airexplorer.net/en/).
2. Launch AirExplorer and select **S3** from the cloud storage options.

   ![AirExplorer interface. ](_images/6c5511771e75dcf1.png)
3. Enter the configuration details and click **OK**:
   - **REST endpoint** — a Telnyx [API Endpoint](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   - **Access Key ID** — your Telnyx API Key.
   - **Secret Access Key** — any value without spaces, quotes, or special characters.
   - **Bucket** — a bucket from the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section.

   ![S3 login portal. ](_images/ec395d037a15a500.jpg)

Additional resources: [AirExplorer blog](https://www.airexplorer.net/en/blog/).
