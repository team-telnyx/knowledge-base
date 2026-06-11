---
source_url: https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage
scraped: 2026-06-11
---

Use WinSCP with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use WinSCP with Telnyx Storage

Discover how to set up WinSCP with Telnyx Storage for effortless file transfer and efficient storage management.

Written by Telnyx Engineering

June 6, 2024

Table of contents

WinSCP is a popular open-source SFTP, FTP, and SCP client for Windows, providing users with a secure and intuitive way to transfer files between local and remote servers. It offers a user-friendly interface, supports various protocols and encryption methods, and includes features such as file synchronization, scripting, and remote editing for efficient and seamless file management.

---

# How to configure WinSCP to work with Telnyx Storage

1. Download and install the latest version of WinSCP [here](https://winscp.net/eng/index.php)!
2. If you have used WinSCP before, click on the `New Session` button.

   [![WinSCP New session button. ](https://downloads.intercomcdn.com/i/o/742165939/95d906b3f7c753a96229f0c0/winscp+demo+3.JPG?expires=1781168400&signature=281bd4ab7cdd03205199709da73add2a26a90409b23ac543d333c9b5204f1d33&req=cyQlF897lIJWFb4f3HP0gNOwiDniAaLCgtAc6bQXr8XbKYKzL6HiQHKuhvk2%0AlUs%3D%0A)](https://downloads.intercomcdn.com/i/o/742165939/95d906b3f7c753a96229f0c0/winscp+demo+3.JPG?expires=1781168400&signature=281bd4ab7cdd03205199709da73add2a26a90409b23ac543d333c9b5204f1d33&req=cyQlF897lIJWFb4f3HP0gNOwiDniAaLCgtAc6bQXr8XbKYKzL6HiQHKuhvk2%0AlUs%3D%0A)

   A modal for configuring your new session will pop up

   [![Modal for configuration. ](https://downloads.intercomcdn.com/i/o/742166783/446866abb64947cf82681d2f/winscp4.JPG?expires=1781168400&signature=ecd2f267c673b8ae486f7cc76ab639c6519a4ec01fa566e2f38c5a3ef00707bc&req=cyQlF894molcFb4f3HP0gEhGlGHytwxDDeZAwaRYuCqt%2Fr83%2BhckAvZ0fD30%0AnB8%3D%0A)](https://downloads.intercomcdn.com/i/o/742166783/446866abb64947cf82681d2f/winscp4.JPG?expires=1781168400&signature=ecd2f267c673b8ae486f7cc76ab639c6519a4ec01fa566e2f38c5a3ef00707bc&req=cyQlF894molcFb4f3HP0gEhGlGHytwxDDeZAwaRYuCqt%2Fr83%2BhckAvZ0fD30%0AnB8%3D%0A)
3. For the **File Protocol** setting, select `Amazon S3` from the dropdown menu

   [![File protocol settings page. ](https://downloads.intercomcdn.com/i/o/742167257/2faacee5a69e67a53ccd5dbe/winscp+pic+1.JPG?expires=1781168400&signature=10bc7a3e46bbc5995181ca60d4923174ef2add771c82058b324eba974e7ffb3e&req=cyQlF895n4RYFb4f3HP0gFUyXmiMENRw%2Bc3wOINQEojdklbHLa4zKhb%2Fqd47%0ADa0%3D%0A)](https://downloads.intercomcdn.com/i/o/742167257/2faacee5a69e67a53ccd5dbe/winscp+pic+1.JPG?expires=1781168400&signature=10bc7a3e46bbc5995181ca60d4923174ef2add771c82058b324eba974e7ffb3e&req=cyQlF895n4RYFb4f3HP0gFUyXmiMENRw%2Bc3wOINQEojdklbHLa4zKhb%2Fqd47%0ADa0%3D%0A)
4. Enter the following information in the remaining fields, and then click **Login:**

   1. **Host name:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   2. **Port number:** 443
   3. **Access key ID:** copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
   4. **Secret access key:** The secret access key is not used by Telnyx Storage, but Arq will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.

      [![Login fields. ](https://downloads.intercomcdn.com/i/o/885876353/5f164cc2daef8193b43ecd80/image.jpg?expires=1781168400&signature=47d84c102c5933556b36aa732c8c23efaa978dfb18b1f9fb0fc7d40d2e4f80e9&req=fCgiHs54noRcFb4f3HP0gNT5U8NrRcH%2FwgF8dTty43CM9VjvwE0XLOnWvEc1%0Aekk%3D%0A)](https://downloads.intercomcdn.com/i/o/885876353/5f164cc2daef8193b43ecd80/image.jpg?expires=1781168400&signature=47d84c102c5933556b36aa732c8c23efaa978dfb18b1f9fb0fc7d40d2e4f80e9&req=fCgiHs54noRcFb4f3HP0gNT5U8NrRcH%2FwgF8dTty43CM9VjvwE0XLOnWvEc1%0Aekk%3D%0A)

And that's all there is to it! You can now use WinSCP to store and retrieve your files from Telnyx Storage.

---

**Additional Resources**

For more information on how to use WinSCP check out their support documentation [here](https://winscp.net/eng/docs/start).

---

Related Articles

[Use Cyberduck with Telnyx Storage](https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage)[Use Arq Backup with Telnyx Storage](https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage)[Use CrossFTP with Telnyx Storage](https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
