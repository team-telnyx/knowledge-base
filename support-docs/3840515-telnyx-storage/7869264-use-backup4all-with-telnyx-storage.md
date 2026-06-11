---
source_url: https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage
scraped: 2026-06-11
---

Use Backup4all with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use Backup4all with Telnyx Storage

Learn how to set up Backup4all, a comprehensive backup software, with Telnyx Storage for automated and reliable data backup and recovery.

Written by Telnyx Engineering

July 11, 2024

Table of contents

Backup4all is a comprehensive backup software that enables users to securely and efficiently backup their data to various storage locations such as cloud services, network drives, and external hard drives. It offers a range of features including full, differential, and incremental backups, compression, encryption, scheduling, and backup verification.

---

# How to configure Cyberduck to work with Telnyx Storage

1. Download and install the latest version of Backup4all [here](https://www.backup4all.com/)!
2. Click `File` and `New` to create a new backup job
3. For `Destination`, select **Online** on the left navigation bar and then select **S3 Compatible** from the dropdown menu

   [![S3 Compatible button.](https://downloads.intercomcdn.com/i/o/735629568/22b6ed3363098bf26e081037/step3.JPG?expires=1781168400&signature=dfe6d6aff03c6498d9d2763fadde521245dc2e49650306de1927fec7da2e8289&req=cyMiEMt3mIdXFb4f3HP0gPBBCfM%2BAZ6WDDdWXFfw0sw8bm5N1l1ic4U9kfEN%0AtnE%3D%0A)](https://downloads.intercomcdn.com/i/o/735629568/22b6ed3363098bf26e081037/step3.JPG?expires=1781168400&signature=dfe6d6aff03c6498d9d2763fadde521245dc2e49650306de1927fec7da2e8289&req=cyMiEMt3mIdXFb4f3HP0gPBBCfM%2BAZ6WDDdWXFfw0sw8bm5N1l1ic4U9kfEN%0AtnE%3D%0A)
4. For the remainder of the configuration window, enter the following and then click `Next`:

   1. **Endpoint:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   2. **Access ID**: Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
   3. **Secret Key**: The secret access key is not used by TelnyxStorage, but Backup4all will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
   4. **Region:** leave as `default`
   5. **Signature:** Version 4
   6. **Bucket:** the name of the bucket you want your data stored inSelect the sources that you wish to backup  
      ​

      [![Backup sources settings section. ](https://downloads.intercomcdn.com/i/o/885777639/90e718bf99ae435a1785ec25/Screenshot_from_2023-11-16_12-17-06.jpg?expires=1781168400&signature=22f3356a8082a094d7d20e9d56b29d07cb2eb838ab182481ae1570f42380a194&req=fCgiEc55m4JWFb4f3HP0gAqQviXPm0NFtC1LkxjeaUewSpAnQAoXRjNeFH8a%0A1hM%3D%0A)](https://downloads.intercomcdn.com/i/o/885777639/90e718bf99ae435a1785ec25/Screenshot_from_2023-11-16_12-17-06.jpg?expires=1781168400&signature=22f3356a8082a094d7d20e9d56b29d07cb2eb838ab182481ae1570f42380a194&req=fCgiEc55m4JWFb4f3HP0gAqQviXPm0NFtC1LkxjeaUewSpAnQAoXRjNeFH8a%0A1hM%3D%0A)

And that's all there is to it! You can continue the flow creating your backup job, and once finished your data will be backed up to Telnyx Storage!

---

**Additional Resources**

For more information on how to use Backup4all, check out their [product resources here](https://www.backup4all.com/table-of-contents-help.html).  
​

---

Related Articles

[Use Arq Backup with Telnyx Storage](https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage)[Use Duplicati with Telnyx Storage](https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage)[Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
