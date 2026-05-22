---
title: Connect third-party tools to Telnyx Storage
summary: Configure popular S3-compatible clients and backup tools to work with Telnyx
  Storage. This guide lists common settings and step-by-step summaries for Cyberduck,
  MSP360 CloudBerry Explorer, rclone, S3 Browser, WAL-G, Arq Backup, Backup4all, Duplicati,
  and WinSCP.
sources:
- url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
  content_hash: 14bbd0a30fd5bf54916044a4e3ac88f64ea428dcb537788d4b9481308071b623
- url: https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage
  content_hash: 838254afd47d2fa20c96da6a3dced094cb08e6a5c27e55b58587e66836ef0f2e
- url: https://support.telnyx.com/en/articles/6964272-use-rclone-with-telnyx-storage
  content_hash: bf3572cbab83e26afb11e9b17a17f619bf83674fafbe21142a282ed9f5ef1cc7
- url: https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage
  content_hash: d469c09831ba98dfafbd64c36ae33051bdaff3b204896cc28ac1f96a5528422c
- url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
  content_hash: 75e4564237b050ee4783b643ca55f0ae3521d5c2b8a86d718e8b43b35b3bef90
- url: https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage
  content_hash: d9c9e17f9b6400fe5b852871b4e2350567825ddabd6eba14e4cc642aa1a1954a
- url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
  content_hash: 546c85033db76ebf3c21f3335098770230303a0ad35342638a6ee7fd3e00ad6d
- url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
  content_hash: c2b5fbec260bfb89e239a24adc76e990565de3a81d11f5451d47a07f849359f8
- url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
  content_hash: 61214763c75682a86363f642ee9a19e285e71d5fd304f8d5830bf268901df6c1
updated_at: 2026-05-20T15:29:02Z
---

# Connect third-party tools to Telnyx Storage

Configure popular S3-compatible clients and backup tools to work with Telnyx Storage. This guide lists common settings and step-by-step summaries for Cyberduck, MSP360 CloudBerry Explorer, rclone, S3 Browser, WAL-G, Arq Backup, Backup4all, Duplicati, and WinSCP.

## Before you start
- Telnyx API Key: create/copy from the Telnyx Portal (https://portal.telnyx.com/#/app/api-keys).
- Endpoint: choose a Telnyx Storage API endpoint (https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
- Buckets: you can use an existing bucket or create one during client setup (when supported).
- Networking: use HTTPS on port 443.
- Authentication: Telnyx Storage uses your Telnyx API Key as the Access Key/Access ID. A Secret Access Key is not used by Telnyx Storage, but many apps require a non-empty placeholder; enter any simple value without spaces, quotes, or special characters.
- Region: when prompted, use the region that matches your chosen endpoint (for example, endpoint https://us-central-1.telnyxstorage.com corresponds to region us-central-1). If a tool allows “default” or empty region with Signature V4, that also works.

## Common S3 configuration for Telnyx Storage
- Endpoint/Server/Host: your selected Telnyx Storage API endpoint.
- Port: 443 with SSL/TLS enabled.
- Access Key/Access ID: your Telnyx API Key.
- Secret Key: placeholder string (not used by Telnyx Storage; avoid spaces/quotes/special chars).
- Signature: AWS Signature Version 4.
- Region: matching the endpoint’s region (or leave empty/default if the client supports V4 without region).
- Path style: only set if the tool specifically requires it (e.g., WAL-G sets AWS_S3_FORCE_PATH_STYLE=true).

## Cyberduck setup
1) Open Cyberduck → Open Connection → choose Amazon S3.
2) Server: Telnyx Storage API endpoint. Port: 443.
3) Access Key ID: Telnyx API Key. Secret Access Key: placeholder string.
4) Connect to list and manage your buckets/objects.  
Downloads: https://cyberduck.io/download/

## MSP360 CloudBerry Explorer setup
1) Open CloudBerry Explorer → New Connection → choose S3 compatible.
2) Display Name: any. Access Key: Telnyx API Key. Secret Key: placeholder.
3) Endpoint: Telnyx Storage API endpoint. Signature Version: AWS4.
4) Save and open the connection to view your buckets.  
Product page: https://www.msp360.com/explorer/

## rclone setup
1) Install rclone and run: rclone config → n (new remote) → name (any).
2) Storage: Amazon S3 compliant providers (option 4).
3) Provider: Any other S3 compatible provider (option 34).
4) env_auth: Enter AWS credentials in the next step (option 1).
5) access_key_id: Telnyx API Key. secret_access_key: placeholder.
6) region: Will use v4 signatures and empty region (option 1).
7) endpoint: Telnyx Storage API endpoint.
8) location_constraint: empty or matching region. acl: Owner full control (default).
9) Keep remote (y) → quit (q).  
Docs: https://rclone.org/s3/  
Install: https://rclone.org/install/

## S3 Browser setup
1) Open S3 Browser → Accounts → Add New Account.
2) Display Name: any. Account Type: S3 Compatible Storage.
3) REST Endpoint: Telnyx Storage API endpoint.
4) Access Key ID: Telnyx API Key. Secret Access Key: placeholder.
5) Add and browse your buckets.  
Site: https://s3browser.com/

## WAL-G setup
1) Install WAL-G (https://github.com/wal-g/wal-g#installation).
2) Configure S3 storage variables per WAL-G docs (https://github.com/wal-g/wal-g/blob/master/docs/STORAGES.md#s3):
   - AWS_ACCESS_KEY_ID = your Telnyx API Key
   - AWS_SECRET_ACCESS_KEY = placeholder
   - AWS_ENDPOINT = your Telnyx Storage API endpoint
   - AWS_REGION = region matching the endpoint (e.g., us-central-1)
   - AWS_S3_FORCE_PATH_STYLE = true
   - WALE_S3_PREFIX = s3://your-bucket/
   - PGHOST / PGPORT = your PostgreSQL connection settings

## Arq Backup setup
1) Open Arq → New Storage Location → S3-Compatible Server.
2) Server URL: Telnyx Storage API endpoint.
3) Access Key ID: Telnyx API Key. Secret Access Key: placeholder.
4) Region: region matching the endpoint.
5) Select or create the destination bucket and finish.  
Site: https://www.arqbackup.com/

## Backup4all setup
1) Backup4all → File → New (backup job).
2) Destination: Online → S3 Compatible.
3) Endpoint: Telnyx Storage API endpoint.
4) Access ID: Telnyx API Key. Secret Key: placeholder.
5) Region: default. Signature: Version 4. Bucket: your target bucket.
6) Choose sources/settings and complete the job.  
Site: https://www.backup4all.com/

## Duplicati setup
1) Duplicati → Add backup → Configure a new backup.
2) Step 2 (Destination): Storage Type = S3 Compatible.
3) Use SSL: on. Server: Custom Server URL → Telnyx Storage API endpoint.
4) Bucket Name: existing or new. Bucket Create Region: matches endpoint region.
5) AWS Access ID: Telnyx API Key. AWS Access Key (secret): placeholder.
6) Client library: Amazon AWS SDK. Complete remaining steps to create the backup.  
Site: https://duplicati.com/  
Manuals: https://duplicati.readthedocs.io/en/latest/

## WinSCP setup
1) WinSCP → New Session.
2) File protocol: Amazon S3.
3) Host name: Telnyx Storage API endpoint. Port: 443.
4) Access key ID: Telnyx API Key. Secret access key: placeholder.
5) Login to browse and transfer files.  
Site: https://winscp.net/eng/index.php

## External documentation
- Telnyx Storage API endpoints: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
- Cyberduck docs: https://docs.cyberduck.io/cyberduck/
- MSP360 Explorer guides: https://help.msp360.com/explorer and https://help.msp360.com/explorer-for-macos
- rclone S3 backend: https://rclone.org/s3/
- S3 Browser help: https://s3browser.com/help.aspx
- WAL-G docs: https://github.com/wal-g/wal-g/tree/master/docs
- Arq knowledge base: https://www.arqbackup.com/learn/
- Backup4all help: https://www.backup4all.com/table-of-contents-help.html
- Duplicati manuals: https://duplicati.readthedocs.io/en/latest/
- WinSCP docs: https://winscp.net/eng/docs/start
