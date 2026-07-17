---
title: Telnyx Storage
summary: Telnyx Storage is a high-performance, S3-compatible cloud storage service
  offering 11 nines of reliability, zero egress fees, and roughly 70% lower cost than
  Google Cloud Storage. This guide covers bucket creation and management, built-in
  AI features (summarization, embedding, and inference via the AI Playground), and
  step-by-step instructions for connecting a wide range of third-party S3-compatible
  tools — including rclone, MSP360 Cloudberry Explorer, S3 Browser, Syncovery, GoodSync,
  CloudMounter, DragonDisk, ExpanDrive, ODrive, WebDrive, NetDrive3, and AirExplorer
  — using your Telnyx API key and an available API endpoint.
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
updated_at: 2026-07-17T09:12:01Z
---

# Telnyx Storage

*Part 1 of 3 — see also: [Part 2](telnyx-storage--part-2.md), [Part 3](telnyx-storage--part-3.md)*

Telnyx Storage is a high-performance, S3-compatible cloud storage service offering 11 nines of reliability, zero egress fees, and roughly 70% lower cost than Google Cloud Storage. This guide covers bucket creation and management, built-in AI features (summarization, embedding, and inference via the AI Playground), and step-by-step instructions for connecting a wide range of third-party S3-compatible tools — including rclone, MSP360 Cloudberry Explorer, S3 Browser, Syncovery, GoodSync, CloudMounter, DragonDisk, ExpanDrive, ODrive, WebDrive, NetDrive3, and AirExplorer — using your Telnyx API key and an available API endpoint.

## Overview

Telnyx Storage is a high-performance cloud storage service for storing and managing large volumes of unstructured data. It offers 11 nines of reliability, fast data retrieval, and an S3-compatible API that allows you to point existing S3-centric applications at Telnyx endpoints for easy migration. Unlike many competing platforms, Telnyx Storage does not charge egress fees and is roughly 70% less expensive than Google Cloud Storage for both Class A and Class B operations. The service is built on distributed storage technology that delivers reliable, efficient storage at the edge, and is well suited to managed service providers and resellers who need to scale disaster recovery and backup/restore services across their client base.

## Storage Buckets

A storage bucket is the fundamental unit of storage within Telnyx Storage. You can create your first bucket in a few clicks from the Telnyx portal or with a simple API command, and there is no additional cost for creating additional buckets.

Key points about buckets:

- **Creation**: Buckets can be created through the [Telnyx portal](https://portal.telnyx.com/#/app/storage/buckets) or via an API command.
- **Limit**: Up to 100 storage buckets can be created at no additional cost. Contact sales if you need more than 100.
- **S3-compatible API**: You can point S3-centric applications at Telnyx endpoints for easy migration.
- **Use cases**: Store multi-modal raw data for embeddings and fine-tuning datasets, and access that data with zero egress fees.

### Creating a Bucket

Once signed in, open the [Storage](https://portal.telnyx.com/#/app/storage/buckets) section in the left navigation bar. On first use, click **Get Started** to begin.

Give the bucket a unique name (required). The name must be 3–65 characters long and may contain only lowercase letters, numbers, dots (`.`), or hyphens (`-`). If the name is already in use, you will see the error:

> The requested bucket name is not available. The bucket namespace is shared by all users of the system. Specify a different name and try again.

Click **Create** to finish, then you can begin adding objects to the bucket.

### Adding Objects

When the bucket is created, click into the bucket row to access settings or upload an object. Use the **Upload Object** or **Upload Folder** button in the middle of the page the first time, and the **Upload Object** button in the top right for subsequent uploads. Drag and drop a file, or click **Browse Files** to select one. You can attach tags to objects as key/value pairs, then click **Upload Object** to start the upload. A progress bar indicates completion; click **Done** when finished.

Telnyx Storage accepts virtually any file type, including:

- Text files (`.txt`, `.csv`, `.json`, `.xml`, etc.)
- Image files (`.jpg`, `.png`, `.gif`, etc.)
- Video files (`.mp4`, `.mov`, `.avi`, etc.)
- Audio files (`.mp3`, `.wav`, `.aac`, etc.)
- Document files (`.pdf`, `.docx`, `.xlsx`, etc.)
- Archive files (`.zip`, `.tar`, `.rar`, etc.)

There are no restrictions on file types, but you are responsible for ensuring you have the rights and permissions to store and distribute any data uploaded.

### Deleting a Bucket

Click the trash icon under the **Actions** column to delete a bucket. A bucket can only be deleted when it is empty; all objects must be removed first.

## AI Features on Stored Objects

Telnyx Storage includes built-in AI features that operate directly on objects in your bucket.

### Summarize File

Click the **Summarize File** button to generate a summary of an object's contents.

![Summarize file button.](_images/e201aa9a0f33d520.png)

The following file types are currently supported for AI features:

- `pdf`
- `html`
- `txt` / unstructured text files
- `json`
- `csv`
- Audio/video: `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, `webm` (max 20 MB)

When the summary is ready, a popup window displays the result.

![Bucket summary popup.](_images/6daf8ea8c79b27b0.png)

### Embedding Objects

Click the **Embed** button to embed an object's content so it can be used within the AI Playground (inference). Only supported file types can be embedded.

![Embed button.](_images/2720b644898ea1d4.png)

## AI Playground and Inference

Once files are embedded, switch to the [AI Playground](https://portal.telnyx.com/#/app/aiPlayground) sub-tab next to the bucket sub-tab.

![AI Playground entry point.](_images/8b1cffba05540018.png)

You can select from several supported language models to run inference, including OpenAI GPT-4 and various open-source models. If you select an OpenAI model, supply your OpenAI API key in the field that appears.

### Supported Language Models

- `openai/gpt-3.5-turbo-0613`
- `openai/gpt-3.5-turbo-0125`
- `openai/gpt-4-turbo-preview`
- `openai/gpt-4-1106-preview`
- `openai/gpt-4-32k-0314`
- `openai/gpt-3.5-turbo-1106`
- `openai/gpt-4`
- `openai/gpt-4-0314`
- `openai/gpt-4-32k`
- `openai/gpt-3.5-turbo`
- `openai/gpt-3.5-turbo-16k`
- `openai/gpt-3.5-turbo-16k-0613`
- `openai/gpt-3.5-turbo-0301`
- `openai/gpt-4-0125-preview`
- `openai/gpt-4-32k-0613`
- `openai/gpt-4-0613`
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`
- `TheBloke/zephyr-7B-beta-GPTQ`
- `meta-llama/Llama-2-13b-chat-hf`
- `mistralai/Mistral-7B-Instruct-v0.1`

### Running Inference

To run inference against content in your bucket, select the desired bucket, then specify a **System Prompt** and one or more **User Messages**. Click **Send** to trigger the completion request.

- **Temperature**: Controls output randomness. Higher values produce more random output; lower values produce more focused output.
- **Max Tokens**: Sets the maximum number of tokens generated for the chat completion.

### Why Embed and Infer on Objects?

Embedding and inferring on objects in your buckets unlocks several use cases:

- **Content-based recommendation**: Generate embeddings for catalog items (products, movies, books) and recommend similar items based on user interactions.
- **Semantic search**: Find documents semantically related to a query, even when exact keywords are absent.
- **Image or video recognition**: Use embeddings to classify images, detect objects, or find visually similar content.
- **Data clustering and organization**: Cluster similar items together to make large, varied buckets easier to manage and retrieve.
- **Anomaly detection**: Capture the essence of log or transaction entries as embeddings, then build models to detect anomalous entries.
- **Reduced latency**: Infer directly on objects in place, without moving data to a separate processing location.

## Common Configuration Values for Third-Party Tools

Most S3-compatible third-party tools can be connected to Telnyx Storage using the same set of core values. Across the integrations documented in this collection, the following fields are used:

- **Access Key / Access Key ID / Access ID**: Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys).
- **Secret Key / Secret Access Key**: Not used by Telnyx Storage, but most clients require a value. Enter any string without spaces, quoting, or special characters.
- **Endpoint / REST Endpoint / Server Address / Service Endpoint**: One of the available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For DragonDisk, the documented endpoint is `https://storage.telnyx.com`.
- **Bucket**: The name of an existing bucket on your [Telnyx Storage](https://portal.telnyx.com/#/app/storage/buckets) account (optional in some clients).
- **Region / Location Constraint / Custom Region**: For rclone, leave empty or use one of the available regions. For ExpanDrive, set the custom region to match the chosen endpoint (for example, `us-central-1` for `https://us-central-1.telnyxstorage.com`).
- **Signature Version**: For MSP360 Cloudberry Explorer, select `AWS4`.
