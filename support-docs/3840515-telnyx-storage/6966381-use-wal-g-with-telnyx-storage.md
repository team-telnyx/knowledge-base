---
source_url: https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage
scraped: 2026-06-11
---

Use WAL-G with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use WAL-G with Telnyx Storage

Maximize the benefits of WAL-G, a robust backup tool for PostgreSQL, by following our guide to configure it with Telnyx Storage.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[WAL-G](https://github.com/wal-g/wal-g) is a backup and disaster recovery tool. It enables you to store and manage PostgreSQL WAL (write-ahead log) files on cloud storage services that implement the S3 API, including Amazon S3 and compatible services, ensuring that you have a secure and reliable backup of your PostgreSQL database.

---

# How to configure WAL-G to work with Telnyx Storage

1. Download and install the latest version of WAL-G [here](https://github.com/wal-g/wal-g#installation)!
2. Follow WAL-G’s guide to configure it with S3 Storage [here](https://github.com/wal-g/wal-g/blob/master/docs/STORAGES.md#s3). Enter in the following values for the configuration fields (in bold):

   1. **AWS\_ACCESS\_KEY\_ID**: copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
   2. **AWS\_ENDPOINT** = Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   3. **AWS\_REGION** = Copy and paste the matching region from [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For example, if you chose the <https://us-central-1.telnyxstorage.com> endpoint, you will use us-central-1 as the region.
   4. **AWS\_S3\_FORCE\_PATH\_STYLE** = true
   5. **AWS\_SECRET\_ACCESS\_KEY** = The secret access key is not used by TelnyxStorage, but WAL-G will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
   6. **WALE\_S3\_PREFIX** = Same format as with s3, but pointing to your bucket name. For example `s3://walg-poc/`
   7. **PGHOST** = Your Postgres host
   8. **PGPORT** = Your Postgres port

And that’s all there is to it! You can now start using WAL-G with Telnyx Storage!

---

**Additional Resources**

For more information on how to use WAL-G, check out their [developer documentation](https://github.com/wal-g/wal-g/tree/master/docs).

---

Related Articles

[Use MSP360 Cloudberry Explorer with Telnyx Storage](https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage)[Use S3 Browser with Telnyx Storage](https://support.telnyx.com/en/articles/6965267-use-s3-browser-with-telnyx-storage)[Use Backup4all with Telnyx Storage](https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage)[Use Duplicati with Telnyx Storage](https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
