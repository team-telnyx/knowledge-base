---
title: AWS SDK Examples for Telnyx Cloud Storage
summary: Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used
  in any language to create buckets, upload and download objects, list contents, and
  generate presigned URLs. This page collects working examples for .NET, Elixir, Go,
  Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks
  (endpoint, credentials, checksum settings) each SDK requires.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
updated_at: 2026-08-05T13:40:27Z
---

# AWS SDK Examples for Telnyx Cloud Storage

*Part 3 of 4 — see also: [Part 1](aws-sdk-examples-for-telnyx-cloud-storage--part-1.md), [Part 2](aws-sdk-examples-for-telnyx-cloud-storage--part-2.md), [Part 4](aws-sdk-examples-for-telnyx-cloud-storage--part-4.md)*

Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used in any language to create buckets, upload and download objects, list contents, and generate presigned URLs. This page collects working examples for .NET, Elixir, Go, Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks (endpoint, credentials, checksum settings) each SDK requires.

## Java (AWS SDK for Java v2)

With AWS SDK for Java v2 version 2.30 or newer, request checksum calculation and response checksum validation must be set to `WHEN_REQUIRED` to avoid checksum errors against Cloud Storage.

Add the S3 dependency (any 2.x version works):

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.20.0</version>
</dependency>
```

### Create S3 bucket

```java
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;

import java.net.URI;

public class CreateBucket {
    public static void main(String[] args) {
        String bucketName = "--your-bucket-name--";
        Region region = Region.US_EAST_1;
        String telnyxUrl = "https://us-central-1.telnyxcloudstorage.com";
        String telnyxApiKey = "-- api key --";

        S3Client s3 = S3Client.builder()
            .region(region)
            .endpointOverride(URI.create(telnyxUrl))
            .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
            .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
            .credentialsProvider(
                StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
            .build();

        s3.createBucket(CreateBucketRequest.builder().bucket(bucketName).build());
        s3.close();
    }
}
```

### Upload an object

```java
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.net.URI;
import java.nio.file.Paths;

S3Client s3 = S3Client.builder()
    .region(region)
    .endpointOverride(URI.create(telnyxUrl))
    .credentialsProvider(
        StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
    .build();

PutObjectRequest putObjectRequest = PutObjectRequest.builder()
    .bucket(bucketName)
    .key(keyName)
    .build();

s3.putObject(putObjectRequest, RequestBody.fromFile(Paths.get(filePath)));
s3.close();
```

### List objects

```java
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;

ListObjectsV2Request listObjectsRequest = ListObjectsV2Request.builder()
    .bucket(bucketName)
    .build();

ListObjectsV2Response listObjectsResponse = s3.listObjectsV2(listObjectsRequest);
for (S3Object s3Object : listObjectsResponse.contents()) {
    System.out.println(s3Object.key());
}
```

### Download object

```java
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;

import java.io.File;
import java.io.FileOutputStream;

GetObjectRequest getObjectRequest = GetObjectRequest.builder()
    .bucket(bucketName)
    .key(keyName)
    .build();

ResponseBytes<GetObjectResponse> objectBytes = s3.getObject(getObjectRequest, ResponseTransformer.toBytes());

File downloadedFile = new File("-- path to where to save the file --");
try (FileOutputStream fos = new FileOutputStream(downloadedFile)) {
    fos.write(objectBytes.asByteArray());
}
```

### Generate presigned URLs for upload and download

Add `okhttp3` and `gson` for the HTTP and JSON helpers:

```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>4.9.2</version>
</dependency>
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.7</version>
</dependency>
```

```java
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import okhttp3.*;

import java.io.IOException;
import java.util.Map;

OkHttpClient httpClient = new OkHttpClient();
Gson gson = new Gson();

String presignedUrlRequestJson = gson.toJson(Map.of("ttl", 30));
RequestBody presignedUrlRequestBody = RequestBody.create(MediaType.parse("application/json"), presignedUrlRequestJson);

Request presignedUrlRequest = new Request.Builder()
    .url("https://api.telnyx.com/v2/storage/buckets/-- name of the bucket --/--name of the object--/presigned_url")
    .header("Authorization", "Bearer --your api key---")
    .post(presignedUrlRequestBody)
    .build();

try (Response response = httpClient.newCall(presignedUrlRequest).execute()) {
    String responseBody = response.body().string();
    Map<String, Object> responseBodyMap = gson.fromJson(responseBody, new TypeToken<Map<String, Object>>() {}.getType());
    String presignedUrl = ((Map<String, String>) responseBodyMap.get("data")).get("presigned_url");

    Request downloadRequest = new Request.Builder().url(presignedUrl).build();
    try (Response downloadResponse = httpClient.newCall(downloadRequest).execute()) {
        System.out.println("Downloaded via presigned URL: " + downloadResponse.body().string());
    }
}
```

## Node.js (AWS SDK for JavaScript v3)

Recent AWS SDK v3 versions work against Cloud Storage with default checksum settings. If a checksum error appears on an older v3 release, set all four checksum options to `WHEN_REQUIRED` as shown below.

```javascript
const { S3Client, CreateBucketCommand, PutObjectCommand, ListObjectsCommand, GetObjectCommand } = require("@aws-sdk/client-s3");
const axios = require("axios");
const { v4: uuidv4 } = require("uuid");

const telnyxApiKey = process.env.TELNYX_API_KEY;
if (!telnyxApiKey) {
  console.error("TELNYX_API_KEY environment variable not set");
  process.exit(1);
}

const endpointUrl = "https://us-central-1.telnyxcloudstorage.com";

const s3Client = new S3Client({
  endpoint: endpointUrl,
  region: "us-central-1",
  credentials: {
    accessKeyId: telnyxApiKey,
    secretAccessKey: telnyxApiKey
  },
  forcePathStyle: true,
  requestChecksumCalculation: 'WHEN_REQUIRED',
  requestChecksumValidation: 'WHEN_REQUIRED',
  responseChecksumCalculation: 'WHEN_REQUIRED',
  responseChecksumValidation: 'WHEN_REQUIRED'
});

(async () => {
  const bucketName = `my-test-bucket-${uuidv4()}`;
  await s3Client.send(new CreateBucketCommand({ Bucket: bucketName }));

  for (let i = 0; i < 2; i++) {
    const name = `my-test-object-${i}`;
    const body = `Telnyx Cloud Storage ${i}`;
    await s3Client.send(new PutObjectCommand({ Bucket: bucketName, Key: name, Body: body }));
  }

  const listResult = await s3Client.send(new ListObjectsCommand({ Bucket: bucketName }));
  (listResult.Contents || []).forEach(obj => console.log(obj.Key));

  const getResult = await s3Client.send(new GetObjectCommand({ Bucket: bucketName, Key: "my-test-object-0" }));
  const streamToString = (stream) => new Promise((resolve, reject) => {
    const chunks = [];
    stream.on("data", (chunk) => chunks.push(chunk));
    stream.on("error", reject);
    stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf-8")));
  });
  console.log(await streamToString(getResult.Body));

  const presignResponse = await axios.post(
    `https://api.telnyx.com/v2/storage/buckets/${bucketName}/my-test-object-0/presigned_url`,
    { ttl: 30 },
    { headers: { Authorization: `Bearer ${telnyxApiKey}` } }
  );
  console.log(presignResponse.data);

  const fileResponse = await axios.get(presignResponse.data.data.presigned_url);
  console.log(fileResponse.data);
})();
```
