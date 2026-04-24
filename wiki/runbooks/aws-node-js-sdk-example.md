---
title: AWS Node.js SDK Example
summary: 'AWS Node.js SDK example for Telnyx Cloud Storage. For SDK v3, set checksum options to WHEN_REQUIRED.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
    content_hash: fe45baf2ea131d8a620551282dedb0f77cd28fa1ba19c59931dcb51aada03b1e
updated_at: 2026-04-10T00:00:00Z
---

# AWS Node.js SDK Example

<Callout type="warning">
  **For AWS SDK v3, make sure you set all checksum calculation and validation options to `WHEN_REQUIRED`.**

The following example shows how the AWS Node.js SDK can be used to interact with Telnyx Cloud Storage.

```javascript theme={null}
const { S3Client, CreateBucketCommand, PutObjectCommand, ListObjectsCommand, GetObjectCommand } = require("@aws-sdk/client-s3");
const axios = require("axios");
const { v4: uuidv4 } = require("uuid");

const telnyxApiKey = process.env.TELNYX_API_KEY;

if (!telnyxApiKey) {
  console.error("TELNYX_API_KEY environment variable not set");
  process.exit(1);
}

const endpointUrl = "https://us-central-1.telnyxcloudstorage.com";

// 1. Initialize the AWS S3 client with specific options
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
  // 2. Create a bucket
  const bucketName = `my-test-bucket-${uuidv4()}`;
  await s3Client.send(new CreateBucketCommand({ Bucket: bucketName }));

  // 3. Upload two objects with random data
  for (let i = 0; i < 2; i++) {
    const name = `my-test-object-${i}`;
    const body = `Telnyx Cloud Storage ${i}`;
    await s3Client.send(new PutObjectCommand({ Bucket: bucketName, Key: name, Body: body }));
  }

  // 4. List objects in the bucket
  const listResult = await s3Client.send(new ListObjectsCommand({ Bucket: bucketName }));
  (listResult.Contents || []).forEach(obj => {
    console.log(obj.Key);
  });

  // 5. Download the first object
  const getResult = await s3Client.send(new GetObjectCommand({ Bucket: bucketName, Key: "my-test-object-0" }));
  const streamToString = (stream) => new Promise((resolve, reject) => {
    const chunks = [];
    stream.on("data", (chunk) => chunks.push(chunk));
    stream.on("error", reject);
    stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf-8")));
  });
  console.log(await streamToString(getResult.Body));

  // 6. Create a presigned URL for the first file
  const presignResponse = await axios.post(
    `https://api.telnyx.com/v2/storage/buckets/${bucketName}/my-test-object-0/presigned_url`,
    { TTL: 30 },
    { headers: { Authorization: `Bearer ${telnyxApiKey}` } }
  );
  console.log(presignResponse.data);

  // 7. Download the file using the presigned URL
  const fileResponse = await axios.get(presignResponse.data.data.presigned_url);
  console.log(fileResponse.data);
})();
```


## Related Pages

- [AWS .Net SDK Example](../runbooks/aws-net-sdk-example.md)
- [AWS Java SDK Example](../runbooks/aws-java-sdk-example.md)
- [AWS PHP SDK Example](../runbooks/aws-php-sdk-example.md)
- [AWS Elixir SDK Example](../runbooks/aws-elixir-sdk-example.md)
- [AWS Golang SDK Example](../runbooks/aws-golang-sdk-example.md)
