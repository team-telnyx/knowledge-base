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

*Part 1 of 3 — see also: [Part 2](telnyx-storage--part-2.md), [Part 3](telnyx-storage--part-3.md)*

Telnyx Storage is a high-performance, S3-compatible cloud storage service offering zero egress fees, 11 nines of durability, and built-in AI inference capabilities. It integrates with a wide range of third-party file transfer, backup, synchronization, and mounting tools through its S3-compatible API.

## Overview

Telnyx Storage is a cloud storage service built on distributed storage technology for storing and managing unstructured data. It offers speedy data retrieval, exceptional durability (11 nines of reliability), and an S3-compatible API that enables seamless integration with third-party tools and applications.

Key differentiators include:

- **Zero egress fees** — unlike providers such as Google Cloud Storage, Telnyx does not charge for data egress.
- **~70% cost savings** compared to Google Cloud Storage across Class A and B operations.
- **S3-compatible API** — point existing S3-centric applications at Telnyx endpoints for easy migration.
- **Built-in AI features** — summarize and embed stored objects for use in inference workflows.

## Storage Buckets

A storage bucket is the fundamental unit of storage within Telnyx Storage. You can create up to 100 buckets at no additional cost (contact sales if you need more). Buckets can be created through the [Telnyx portal](https://portal.telnyx.com/#/app/storage/buckets) or via API.

### Creating a Bucket

1. Navigate to the **Storage** section in the [Telnyx portal](https://portal.telnyx.com/#/app/storage/buckets).
2. Click **Get Started** (first time) or the create button.
3. Enter a unique bucket name (3–65 characters, lowercase letters, numbers, dots, or hyphens only).
4. Click **Create**.

Bucket names are globally shared across all users. If a name is already taken, you will receive an error: *The requested bucket name is not available. The bucket namespace is shared by all users of the system. Specify a different name and try again.*

### Uploading Objects

1. Click into your bucket from the portal.
2. Click **Upload Object** or **Upload Folder**.
3. Drag and drop files or click **Browse Files**.
4. Optionally specify tags as key-value pairs.
5. Click **Upload Object**.

Telnyx Storage accepts virtually any file type, including text files, images, videos, audio, documents, and archives. There are no file type restrictions, but you must have the necessary rights to store and distribute any data you upload.

### Deleting a Bucket

You can delete a bucket by clicking the trash icon in the **Actions** column. A bucket can only be deleted when it is empty — all associated objects must be removed first.

### Access Control

Currently, storage buckets can only be accessed by the organization owner who created them. Sub-members' buckets are not accessible to the organization owner, and vice versa. Shared access to buckets is planned for a future release.

## AI and Inference Features

Telnyx Storage includes built-in AI capabilities for objects stored in your buckets.

### Summarize File

Click the **Summarize File** button on a supported object to generate an AI summary of its contents. Supported file types include:

- `pdf`, `html`, `txt`/unstructured text, `json`, `csv`
- Audio/video: `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, `webm` (max 20 MB)

### Embed Content

Click the **Embed** button to embed your content for use within the AI Playground. Only supported file types will be embedded.

### AI Playground

The [AI Playground](https://portal.telnyx.com/#/app/aiPlayground) lets you run inference against embedded content in your buckets. You can:

- Select from multiple language models (OpenAI GPT variants and open-source models such as Mistral and Llama).
- If using an OpenAI model, provide your OpenAI API Key.
- Choose a bucket as the knowledge source.
- Set a **system prompt** and **user message**.
- Adjust **temperature** (higher = more random, lower = more focused) and **max tokens**.

Available models include `openai/gpt-4`, `openai/gpt-3.5-turbo`, `mistralai/Mistral-7B-Instruct-v0.1`, `meta-llama/Llama-2-13b-chat-hf`, and others.

### Why Embed and Infer

Embedding and inferring on bucket objects enables several use cases:

- **Content-based recommendation** — generate embeddings to recommend similar items.
- **Semantic search** — find semantically related documents beyond exact keyword matching.
- **Image/video recognition** — classify, detect objects, or find visually similar content.
- **Data clustering and organization** — group similar items in large datasets.
- **Anomaly detection** — identify entries that deviate from the norm in logs or transactions.
- **Reduced latency** — process data in-place without moving it to a separate processing location.

API endpoints for programmatic embedding and inference are planned for future release.

## Common Configuration Parameters

All third-party tool integrations share a common configuration pattern because Telnyx Storage exposes an S3-compatible API. The key parameters are:

| Parameter | Value |
|---|---|
| **Connection Type** | Amazon S3 / S3 Compatible |
| **Endpoint (Server/Host)** | One of the available [Telnyx API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints) |
| **Port** | 443 |
| **Access Key ID** | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) |
| **Secret Access Key** | Not used by Telnyx Storage — enter any placeholder without spaces, quotes, or special characters |
| **Region** | The region matching your endpoint (e.g., `us-central-1` for `https://us-central-1.telnyxstorage.com`) |
| **Signature Version** | AWS4 (V4) |

> **Important:** The Secret Access Key field is required by most S3-compatible tools but is not used by Telnyx Storage. Enter any placeholder value that contains no spaces, quotes, or special characters.

## File Transfer Clients

### Cyberduck

[Cyberduck](https://cyberduck.io/) is a free, open-source file transfer client for macOS and Windows supporting upload, download, metadata management, versioning, and lifecycle policies.

1. Download and install [Cyberduck](https://cyberduck.io/download/).
2. Open Cyberduck and click **Open Connection**.
3. Select **Amazon S3** as the connection type.
4. Enter: **Server** = Telnyx API Endpoint, **Port** = 443, **Access Key ID** = Telnyx API Key, **Secret Access Key** = any placeholder.
5. Click **Connect**.

For more details, see the [Cyberduck documentation](https://docs.cyberduck.io/cyberduck/).

### WinSCP

[WinSCP](https://winscp.net/eng/index.php) is an open-source SFTP/FTP/SCP client for Windows with file synchronization, scripting, and remote editing capabilities.

1. Download and install [WinSCP](https://winscp.net/eng/index.php).
2. Click **New Session**.
3. Set **File Protocol** to `Amazon S3`.
4. Enter: **Host name** = Telnyx API Endpoint, **Port number** = 443, **Access key ID** = Telnyx API Key, **Secret access key** = any placeholder.
5. Click **Login**.

For more details, see the [WinSCP documentation](https://winscp.net/eng/docs/start).

### CrossFTP

[CrossFTP](https://www.crossftp.com) is an FTP client supporting multi-threading, synchronization, and encryption.

1. Download and install [CrossFTP](https://www.crossftp.com/download.htm).
2. Click **File** → **Site Connect**.
3. Set **Protocol** to `S3/HTTPS`.
4. Enter: **Host** = Telnyx API Endpoint, **Port** = 433, **Access Key** = Telnyx API Key, **Secret** = any placeholder, **Remote Path** = bucket name.
5. Click **Connect**.

For more details, see the [CrossFTP features page](https://www.crossftp.com/features.htm).
