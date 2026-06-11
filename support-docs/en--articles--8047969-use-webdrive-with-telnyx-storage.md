---
source_url: https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage
scraped: 2026-06-11
---

Use WebDrive with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use WebDrive with Telnyx Storage

Learn how to integrate WebDrive, a powerful file transfer client, with Telnyx Storage for seamless file management and storage.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[WebDrive](https://southrivertech.com/) is a feature-rich file transfer client that enables users to easily access and manage files stored on various remote servers, including cloud storage services. It offers a user-friendly interface and supports a wide range of protocols, making it a versatile tool for file management and transfer.

---

# **How to configure WebDrive to work with Telnyx Storage**

## Step 1

Download and install the latest version of WebDrive [here!](https://southrivertech.com/webdrive/)

## Step 2

Launch the WebDrive application and click on the **"+"** button to create a new connection.  
​

[![WebDrive homepage. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451299/464b8f300bb598c59e6b1c26/wlud6x0DHpaElpqQ3QdRRasfb0GvjNGD_1e8XOdgciiu0OrefVhZelQAgrBhPkoDyo2_REwKLzGhg3FDfDDcSvpBJAyvV6_-07aB7xTIDl-BdUSho5buU6wAwHZ-CiK278viaXzQfwRXKhE8rPfkgg?expires=1781168400&signature=ec9cc8cdeb48ce6aadd843b877724ed1ab2a003ea5df3639adbbc6d21b6a13ab&req=cycnEsx%2Fn4hWFb4f3HP0gFIO5T8YWLIAGGxMNgBd60uInUYAgEt1C1oJ6VZi%0AuuInrbWN3gtJjL27kw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451299/464b8f300bb598c59e6b1c26/wlud6x0DHpaElpqQ3QdRRasfb0GvjNGD_1e8XOdgciiu0OrefVhZelQAgrBhPkoDyo2_REwKLzGhg3FDfDDcSvpBJAyvV6_-07aB7xTIDl-BdUSho5buU6wAwHZ-CiK278viaXzQfwRXKhE8rPfkgg?expires=1781168400&signature=ec9cc8cdeb48ce6aadd843b877724ed1ab2a003ea5df3639adbbc6d21b6a13ab&req=cycnEsx%2Fn4hWFb4f3HP0gFIO5T8YWLIAGGxMNgBd60uInUYAgEt1C1oJ6VZi%0AuuInrbWN3gtJjL27kw%3D%3D%0A)

## Step 3

Select “**Amazon S3”** as the connection type.  
​

[![Amazon S3 setup. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451303/9480f696ff90b6602c39d5bb/rLt62wrPeXFuWDaajeHih_2-bMpJQdosGeUw1Iwu7ziQlOyt7xQpoUMwjMkXr9rIl26TdUdqxG3xG-AdOVGrUdSAo4YY-CBSpDQqJR2eA22bXutdddokR8oHTQNy_60IShlhyaPq6FG4Aoz3Oub3qg?expires=1781168400&signature=fd761505ae89b4a2b0d7606bc53404235bfd916a15c57b4674c748f904c20370&req=cycnEsx%2FnoFcFb4f3HP0gDvBxPxN2hjGcADEXQ1EnbsP3LaymhdfNYBdKqQQ%0APGQPQLTDZViaVtIjmQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451303/9480f696ff90b6602c39d5bb/rLt62wrPeXFuWDaajeHih_2-bMpJQdosGeUw1Iwu7ziQlOyt7xQpoUMwjMkXr9rIl26TdUdqxG3xG-AdOVGrUdSAo4YY-CBSpDQqJR2eA22bXutdddokR8oHTQNy_60IShlhyaPq6FG4Aoz3Oub3qg?expires=1781168400&signature=fd761505ae89b4a2b0d7606bc53404235bfd916a15c57b4674c748f904c20370&req=cycnEsx%2FnoFcFb4f3HP0gDvBxPxN2hjGcADEXQ1EnbsP3LaymhdfNYBdKqQQ%0APGQPQLTDZViaVtIjmQ%3D%3D%0A)

## Step 4

In the connections settings window, enter the following information and then click “**Save”**.

1. **Connection Name:** Give the connection a name, which could be your nickname.
2. **Access Key:** Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
3. **Secret Key:** Although not used by Telnyx Storage, provide a value without spaces, quoting, or special characters.
4. **Bucket:** You can enter the bucket name on your [Telnyx storage](https://portal.telnyx.com/#/app/storage/buckets) or leave it blank.
5. **Drive Letter:** Enter the letter on your local storage drive.
6. **Advanced Settings:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints) as the custom server URL.  
   ​

   [![Connection Settings section. ](https://downloads.intercomcdn.com/i/o/885890506/8cd59f7f4b0948920e3c5caa/Screenshot+2023-11-16+at+2.47.04%E2%80%AFPM+%281%29.jpg?expires=1781168400&signature=43660cd16a1a7473f8c581cff81b1ae7652224baefb66b69beca61ae7c4100ea&req=fCgiHsB%2BmIFZFb4f3HP0gHzzmcSuyuG3wXLUzmh4JK6NULfQ0enE%2FnDhsGLG%0Aquo%3D%0A)](https://downloads.intercomcdn.com/i/o/885890506/8cd59f7f4b0948920e3c5caa/Screenshot+2023-11-16+at+2.47.04%E2%80%AFPM+%281%29.jpg?expires=1781168400&signature=43660cd16a1a7473f8c581cff81b1ae7652224baefb66b69beca61ae7c4100ea&req=fCgiHsB%2BmIFZFb4f3HP0gHzzmcSuyuG3wXLUzmh4JK6NULfQ0enE%2FnDhsGLG%0Aquo%3D%0A)

## Step 5

1. Once you have configured the settings, click on the **"Save"** button to save the connection.  
   ​

   [![Save button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451315/01d5acc5bd447f983279aecd/R4L7sXWnrtZwGoBgexeU3ftmu3_GTTWUwhKCmwfPASRT2iNrfjdK2vgbK_ZNt9yY3eGCPxazxxV2PBF4vNkRmPyA2E0KGvd2jlVrlP0Q9ENfJCkkii6se4GqK_WUlYrjGCAU-bWem_mVD1FAETSCnQ?expires=1781168400&signature=4158a20215aa73efd194038f9c54e8539b691600bd1c333cdb3a06282bf67b9e&req=cycnEsx%2FnoBaFb4f3HP0gMWT7ymVOi3%2BlNNeCiORqurQi%2BuhsYTbfzHe72Im%0Au3k%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451315/01d5acc5bd447f983279aecd/R4L7sXWnrtZwGoBgexeU3ftmu3_GTTWUwhKCmwfPASRT2iNrfjdK2vgbK_ZNt9yY3eGCPxazxxV2PBF4vNkRmPyA2E0KGvd2jlVrlP0Q9ENfJCkkii6se4GqK_WUlYrjGCAU-bWem_mVD1FAETSCnQ?expires=1781168400&signature=4158a20215aa73efd194038f9c54e8539b691600bd1c333cdb3a06282bf67b9e&req=cycnEsx%2FnoBaFb4f3HP0gMWT7ymVOi3%2BlNNeCiORqurQi%2BuhsYTbfzHe72Im%0Au3k%3D%0A)

   ​
2. Select the newly created connection from the list and click on the ***box*** object button to connect with Telnyx Storage.  
   ​

   [![Box object button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451317/75fcd730cd753b1e56f81ad2/MPsbkjAVtnvBzZT6GwbVTwVstwtFrWXVX33qRvQjOUJ3XOf1a8R8aBNHSdMdCnGAja_MX4zR1b6nuh7HU_qZ4nuABgI_UsplDFyFVS8VQnUEa1f5CZDZGxGsJ3iN5aUlF9o6oJmV5OhbqjizGij_7Q?expires=1781168400&signature=245bf315e4618fdd7c06b85499adbffbab0839707893719a9725eb852f81012e&req=cycnEsx%2FnoBYFb4f3HP0gMpZ63AosGjioiaAvU%2FyKlpmTC10ekQ3ZntHx%2FfX%0AxO0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770451317/75fcd730cd753b1e56f81ad2/MPsbkjAVtnvBzZT6GwbVTwVstwtFrWXVX33qRvQjOUJ3XOf1a8R8aBNHSdMdCnGAja_MX4zR1b6nuh7HU_qZ4nuABgI_UsplDFyFVS8VQnUEa1f5CZDZGxGsJ3iN5aUlF9o6oJmV5OhbqjizGij_7Q?expires=1781168400&signature=245bf315e4618fdd7c06b85499adbffbab0839707893719a9725eb852f81012e&req=cycnEsx%2FnoBYFb4f3HP0gMpZ63AosGjioiaAvU%2FyKlpmTC10ekQ3ZntHx%2FfX%0AxO0%3D%0A)

Now you can easily manage your files stored in Telnyx Storage using WebDrive. Simply access the connected drive through WebDrive's interface, and you can perform various file operations such as uploading, downloading, renaming, and deleting files seamlessly.

---

**Additional Resources**

For more detailed information and advanced configurations, refer to the WebDrive [blog.](https://southrivertech.com/blog/)  
​

---

Related Articles

[Use Cyberduck with Telnyx Storage](https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage)[Use CrossFTP with Telnyx Storage](https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use NetDrive3 with Telnyx Storage](https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
