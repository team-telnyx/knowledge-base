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
