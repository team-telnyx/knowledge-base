---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported
  API operations, SSL certificate configuration, and third-party compatibility.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-06-11T10:25:44Z
---

# Telnyx Cloud Storage

*Part 2 of 3 — see also: [Part 1](telnyx-cloud-storage-3--part-1.md), [Part 3](telnyx-cloud-storage-3--part-3.md)*

Telnyx Cloud Storage is an S3-compatible object storage service that supports standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported API operations, SSL certificate configuration, and third-party compatibility.

## SDK Examples

### Node.js

```javascript
const { S3Client, CreateBucketCommand, PutObjectCommand, ListObjectsCommand, GetObjectCommand } = require("@aws-sdk/client-s3");
const axios = require("axios");
const { v4: uuidv4 } = require("uuid");

const telnyxApiKey = process.env.TELNYX_API_KEY;

const s3Client = new S3Client({
  endpoint: "https://us-central-1.telnyxcloudstorage.com",
  region: "us-central-1",
  credentials: { accessKeyId: telnyxApiKey, secretAccessKey: telnyxApiKey },
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
    await s3Client.send(new PutObjectCommand({ Bucket: bucketName, Key: `my-test-object-${i}`, Body: `Telnyx Cloud Storage ${i}` }));
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
    { TTL: 30 },
    { headers: { Authorization: `Bearer ${telnyxApiKey}` } }
  );
  const fileResponse = await axios.get(presignResponse.data.data.presigned_url);
  console.log(fileResponse.data);
})();
```

### Python

```python
import requests, uuid, os
from botocore.config import Config
import boto3

config = Config(
    request_checksum_calculation="when_required",
    response_checksum_validation="when_required",
)

telnyx_api_key = os.getenv("TELNYX_API_KEY")

client = boto3.client(
    "s3",
    endpoint_url="https://us-central-1.telnyxcloudstorage.com",
    aws_access_key_id=telnyx_api_key,
    aws_secret_access_key=telnyx_api_key,
    config=config,
)

bucket_name = f"my-test-bucket-{uuid.uuid4()}"
client.create_bucket(Bucket=bucket_name)

for i in range(2):
    client.put_object(Bucket=bucket_name, Key=f"my-test-object-{i}", Body=f"Telnyx Cloud Storage {i}")

for obj in client.list_objects(Bucket=bucket_name)["Contents"]:
    print(obj["Key"])

result = client.get_object(Bucket=bucket_name, Key="my-test-object-0")
print(result["Body"].read())

response = requests.post(
    f"https://api.telnyx.com/v2/storage/buckets/{bucket_name}/my-test-object-0/presigned_url",
    json={"TTL": 30},
    headers={"Authorization": f"Bearer {telnyx_api_key}"},
)
presigned_url = response.json()["data"]["presigned_url"]
print(requests.get(presigned_url).text)
```

### PHP

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

$telnyxAPIKey = getenv('TELNYX_API_KEY');
$region = 'us-central-1';
$endpoint = "https://{$region}.telnyxcloudstorage.com";

$s3Client = new S3Client([
    'region'  => $region,
    'version' => 'latest',
    'endpoint' => $endpoint,
    'credentials' => ['key' => $telnyxAPIKey, 'secret' => $telnyxAPIKey],
    'use_path_style_endpoint' => true,
]);

$bucketName = 'test-bucket-' . $region . '-' . date('H-i') . '-' . rand(0, 1000000);
$s3Client->createBucket(['Bucket' => $bucketName]);

for ($i = 0; $i < 2; $i++) {
    $content = random_bytes(1024 * 32);
    $s3Client->putObject(['Bucket' => $bucketName, 'Key' => "{$i}.txt", 'Body' => $content]);
}

$result = $s3Client->listObjects(['Bucket' => $bucketName]);
foreach ($result['Contents'] as $item) {
    echo $item['Key'] . PHP_EOL;
}

$result = $s3Client->getObject(['Bucket' => $bucketName, 'Key' => '1.txt']);
echo $result['Body']->getContents() . PHP_EOL;

// Presigned URL via Telnyx API
$url = "https://api.telnyx.com/v2/storage/buckets/{$bucketName}/1.txt/presigned_url";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['TTL' => 30]));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $telnyxAPIKey,
    'Content-Type: application/json',
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);
$presignedURL = json_decode($response, true)['data']['presigned_url'];

$ch = curl_init($presignedURL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
curl_close($ch);
?>
```

### Ruby

```ruby
require "aws-sdk-s3"
require "net/http"

telnyx_api_key = ENV["TELNYX_API_KEY"]

resource = Aws::S3::Resource.new(
  region: "us-central-1",
  endpoint: "https://us-central-1.telnyxcloudstorage.com",
  access_key_id: telnyx_api_key,
  secret_access_key: "doesn't matter",
)

bucket_name = "example-#{SecureRandom.hex(24)}"
bucket = resource.create_bucket(bucket: bucket_name)

# Upload a file
File.open("document.txt", "w+") { |f| f.write("This is a text document.\n") }
the_object = bucket.object("document.txt")
the_object.upload_file("document.txt")

# Download an object
the_object.download_file("a-local-file.txt")

# Presigned URL for upload
object_key = "important-document.txt"
uri = URI("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url")
response = Net::HTTP.post(uri, { ttl: 30 }.to_json, "Authorization" => "Bearer #{telnyx_api_key}")
presigned_url = JSON.parse(response.body)["data"]["presigned_url"]

# Upload via presigned URL
uri = URI(presigned_url)
request = Net::HTTP.new(uri.host)
request.put(uri, "This is an important text document.\n")

# Presigned URL for download
uri = URI("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url")
response = Net::HTTP.post(uri, { ttl: 30 }.to_json, "Authorization" => "Bearer #{telnyx_api_key}")
presigned_url = JSON.parse(response.body)["data"]["presigned_url"]
puts Net::HTTP.get(URI(presigned_url))

# Clean up
the_object.delete
bucket.object(object_key).delete
bucket.delete
File.delete("document.txt")
File.delete("a-local-file.txt")
```

## SSL Certificates

SSL certificates for custom domains are currently supported only for buckets located in the US. To serve bucket content over HTTPS with a custom domain:

1. **Create a bucket** whose name matches the desired subdomain (e.g., `asset.gardening-homes.com`).
2. **Make the bucket public** by applying a public read policy. See [Put Bucket Policy](put-bucket-policy.md) for details.
3. **Configure DNS** through your domain/DNS provider by setting up a CNAME alias to the bucket using virtual-hosted-style addressing (see [Bucket Addressing](bucket-addressing.md)).
4. **Upload the certificate and key** under the bucket's SSL/TLS settings in the Telnyx portal. When uploading:
   - The bucket name must exactly match one of the certificate's SNIs. A wildcard SNI like `*.example.com` matches `help.example.com` but **not** `example.com`.
   - Include any intermediate certificates in the certificate file, with the leaf certificate at the top.
   - The root certificate may be omitted (Telnyx verifies known roots automatically), but including it guarantees acceptance.
5. **Test** by navigating to `https://<your-bucket-name>/<object-key>` in a browser — the content should load and the browser should confirm a valid, secure connection.
