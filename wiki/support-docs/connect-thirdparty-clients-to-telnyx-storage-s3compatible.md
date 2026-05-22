---
title: Connect third‑party clients to Telnyx Storage (S3‑compatible)
summary: A practical guide to preparing Telnyx Storage and configuring popular S3/S3‑compatible
  desktop clients to browse, sync, and back up data, plus notes on buckets, endpoints,
  AI features, and common settings that apply across tools.
sources:
- url: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage
  content_hash: 25b457ce3b4bcba2186d896d48fda8b1748c89a78d4bfaf8adffaf58bf1cfb2d
- url: https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage
  content_hash: 045a54282e986082f2ff7c41fe72e8e4ea931275a0479846db82a8bc1f1f5cdd
- url: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage
  content_hash: 4af9285f634f4888074e9ef1aa95b087a65ffe5ae92709237404956a5c9e84c8
- url: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage
  content_hash: ce5c71f381e3c1620f0ad253c3a223337c3d0776c3b51f28477bd39ecf092f1d
- url: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage
  content_hash: 259be86db73ed74d482aa5ffa3316c03ccf9f946c065c28a645d180a722b53e8
- url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
  content_hash: d7efda3acebfd8183598a4a046f432b895a42945792a10463b894bf9830a5822
- url: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage
  content_hash: d10d1a9931ef31bde4fd1842c8cec46120706f822fdbfee59897b4e4654708a6
- url: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage
  content_hash: 74c28647ddd4aa63b3a8cbb2efd29340f6a9077021c7de67cf044e42ca2d6f3f
- url: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage
  content_hash: 1cbcc4aba971b261e29522806c3f63f5f28ddb580beac1644762ee0ede74c30a
- url: https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage
  content_hash: c27a1ddf4869e8e9148bdcadaea24498119a924b7f41e930e26581447fde0f6b
- url: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide
  content_hash: 9780c06da142fc25485513b6e440819f8dabd90b04a0c5173481941829a49e50
- url: https://support.telnyx.com/en/collections/3840515-telnyx-storage
  content_hash: 7a63af21c82b4d5ae53db0b4d5f4da4045624795f28e56b6462da9454acd12a3
updated_at: 2026-05-20T15:30:48Z
---

# Connect third‑party clients to Telnyx Storage (S3‑compatible)

A practical guide to preparing Telnyx Storage and configuring popular S3/S3‑compatible desktop clients to browse, sync, and back up data, plus notes on buckets, endpoints, AI features, and common settings that apply across tools.

## Why Telnyx Storage for S3 clients
Telnyx Storage is a high‑performance, S3‑compatible object storage service designed for large volumes of unstructured data. It offers 11 nines of durability and no egress fees, delivering substantial cost savings versus providers like Google Cloud Storage. Because the API is S3‑compatible, most tools that speak “Amazon S3” or “S3‑compatible” will work by pointing them at a Telnyx endpoint.

Learn more: Get started, create buckets, upload objects, and explore AI features in the Telnyx portal at https://portal.telnyx.com and see API endpoints at https://developers.telnyx.com/docs/cloud-storage/api-endpoints.

## Core settings used by most clients
Use these values when a client asks for S3 fields. Field names vary by app (examples in parentheses):
- Endpoint / Server / Host / REST endpoint: choose a Telnyx Storage API Endpoint from https://developers.telnyx.com/docs/cloud-storage/api-endpoints (for example, https://us-central-1.telnyxstorage.com or https://storage.telnyx.com where applicable).
- Access Key / Access ID / Access Key ID / AWS Access Key: your Telnyx API key from https://portal.telnyx.com/#/app/api-keys
- Secret Key / Secret Access Key: Telnyx does not use this, but many clients require a value. Enter any non‑empty string without spaces, quotes, or special characters.
- Bucket / Bucket name / Remote path: your bucket name from https://portal.telnyx.com/#/app/storage/buckets (some clients let you leave this blank and pick later).
- Region: if requested, supply the region string that matches your chosen endpoint (for example, us-central-1 when using https://us-central-1.telnyxstorage.com).
- Protocol: choose S3 or S3/HTTPS, or S3‑compatible.

Tip: After entering settings, many apps provide a Test/Save or Connect button—use it to validate before proceeding.

## Create and manage buckets (portal quick start)
- Create: In the Telnyx portal Storage section, click Get Started or Create. Bucket names must be 3–65 chars, lowercase letters, numbers, dots, or hyphens; names are globally unique.
- Upload: Open the bucket and use Upload object/folder. Any file type can be stored; add optional key/value tags.
- Delete: Buckets must be empty before deletion (use the trash icon in the bucket list).

More detail: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide

## Client setup guides (quick steps)
Below are concise, tool‑specific mappings to Telnyx Storage. In all tools, select “Amazon S3” or “S3‑compatible” when prompted.

### Syncovery
- Protocol: S3; Provider: Custom
- Access ID: Telnyx API key; Secret key: any safe placeholder
- Endpoint: Telnyx API Endpoint (custom server)
- Choose local/remote folders, then save the profile
Reference: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage

### GoodSync
- Storage type: Amazon S3
- Server address: Telnyx API Endpoint
- AWS Access Key: Telnyx API key; AWS Secret Access Key: any safe placeholder
- Test, Save, then pick your bucket from the dropdown
Reference: https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage

### CloudMounter
- Storage type: Amazon S3
- Access Key: Telnyx API key; Secret Key: any safe placeholder
- Server Endpoint: Telnyx API Endpoint; Bucket: your bucket name
- Click Mount
Reference: https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage

### DragonDisk
- Provider: Other S3‑compatible service
- Service Endpoint: https://storage.telnyx.com (or use a regional endpoint as needed)
- Access Key: Telnyx API key; Secret Key: any safe placeholder
- Save the account
Reference: https://support.telnyx.com/en/articles/8047928-use-dragondisk-with-telnyx-storage

### CrossFTP
- Protocol: S3/HTTPS
- Host: Telnyx API Endpoint
- Access Key: Telnyx API key; Secret: any safe placeholder
- Remote Path: your bucket name; choose Local Path; Connect
Reference: https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage

### ExpanDrive
- Storage: Amazon S3
- Server: Telnyx API Endpoint; Access Key: Telnyx API key; Secret Key: any safe placeholder
- Custom Region: region matching your endpoint (e.g., us-central-1)
- Optional Bucket and Drive Letter; Save
Reference: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage

### ODrive
- Provider: Amazon S3 / S3 Compatible
- Host: Telnyx API Endpoint
- Bucket Name: your bucket; Access Key ID: Telnyx API key; Secret Key ID: any safe placeholder
- Leave Default Storage Class/Directory Structure at defaults; Link storage
Reference: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage

### WebDrive
- Connection type: Amazon S3
- Access Key: Telnyx API key; Secret Key: any safe placeholder
- Advanced Settings: set Custom Server URL to your Telnyx API Endpoint
- Optional Bucket and Drive Letter; Save and connect
Reference: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage

### NetDrive3
- Storage type: S3 (Add a Personal Drive)
- Server Address: Telnyx API Endpoint
- Access ID: Telnyx API key; Secret Key: any safe placeholder
- Bucket name: your bucket; Connect
Reference: https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage

### AirExplorer
- Cloud type: S3
- REST endpoint: Telnyx API Endpoint
- Access Key ID: Telnyx API key; Secret Access Key: any safe placeholder
- Bucket: your bucket; OK to verify and save
Reference: https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage

## AI features in Telnyx Storage (portal)
- Summarize: Generate summaries for supported object types (pdf, html, txt, json, csv, select audio/video up to 20 MB) from the bucket UI.
- Embed: Create embeddings for supported objects, then use AI Playground for inference.
- AI Playground: Pick a model (OpenAI and open‑source options supported), set prompts and parameters, and run inference against your embedded bucket content. If using OpenAI models, provide your OpenAI API key.
Reference: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide

## Access and bucket limits
- Up to 100 buckets can be created at no additional cost; contact Telnyx if you need more.
- Currently, only the organization owner can access the buckets they create (and vice‑versa for sub‑members). Expanded access controls are planned.
Reference: https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide

## Troubleshooting tips
- Authentication fails: Confirm you used your Telnyx API key as the Access Key and supplied a non‑empty “secret” placeholder with no spaces/quotes/special chars.
- Endpoint/region mismatch: If a client asks for Region, make sure it matches your chosen Telnyx endpoint (e.g., us-central-1 for https://us-central-1.telnyxstorage.com).
- Bucket not found: Verify the bucket exists in the portal and that you spelled its name exactly as created.
- Connectivity: Ensure you selected S3/HTTPS (or S3) and used the Endpoint in the correct “Server/Host/REST endpoint” field.

## More resources
- Telnyx Storage collection (many tool guides): https://support.telnyx.com/en/collections/3840515-telnyx-storage
- Specific tool articles: Syncovery, GoodSync, CloudMounter, DragonDisk, CrossFTP, ExpanDrive, ODrive, WebDrive, NetDrive3, AirExplorer (see references linked in each subsection above).
