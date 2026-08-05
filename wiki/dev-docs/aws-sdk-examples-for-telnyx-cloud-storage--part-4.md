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

*Part 4 of 4 — see also: [Part 1](aws-sdk-examples-for-telnyx-cloud-storage--part-1.md), [Part 2](aws-sdk-examples-for-telnyx-cloud-storage--part-2.md), [Part 3](aws-sdk-examples-for-telnyx-cloud-storage--part-3.md)*

Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used in any language to create buckets, upload and download objects, list contents, and generate presigned URLs. This page collects working examples for .NET, Elixir, Go, Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks (endpoint, credentials, checksum settings) each SDK requires.

## PHP (AWS SDK for PHP)

The PHP SDK is configured with `use_path_style_endpoint => true` and the Telnyx API key supplied as both the key and secret. The example uses `curl` for the presigned URL request and download.

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

$telnyxAPIKey = getenv('TELNYX_API_KEY');
if (!$telnyxAPIKey) {
    die('TELNYX_API_KEY environment variable not set');
}

$region = 'us-central-1';
$endpoint = "https://{$region}.telnyxcloudstorage.com";

$s3Client = new S3Client([
    'region'  => $region,
    'version' => 'latest',
    'endpoint' => $endpoint,
    'credentials' => [
        'key'    => $telnyxAPIKey,
        'secret' => $telnyxAPIKey,
    ],
    'use_path_style_endpoint' => true
]);

$bucketName = "test-bucket-" . $region . '-' . date('H-i') . '-' . rand(0, 1000000);

$s3Client->createBucket(['Bucket' => $bucketName]);

for ($i = 0; $i < 2; $i++) {
    $content = random_bytes(1024 * 32);
    $objName = "{$i}.txt";
    $s3Client->putObject([
        'Bucket' => $bucketName,
        'Key'    => $objName,
        'Body'   => $content
    ]);
}

$result = $s3Client->listObjects(['Bucket' => $bucketName]);
foreach ($result['Contents'] as $item) {
    echo "Listed object: " . $item['Key'] . PHP_EOL;
}

$result = $s3Client->getObject([
    'Bucket' => $bucketName,
    'Key'    => '1.txt'
]);
$data = $result['Body']->getContents();
echo "Downloaded file size: " . strlen($data) . PHP_EOL;

$url = "https://api.telnyx.com/v2/storage/buckets/{$bucketName}/1.txt/presigned_url";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['ttl' => 30]));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $telnyxAPIKey,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$presignedData = json_decode($response, true);
$presignedURL = $presignedData['data']['presigned_url'];

$ch = curl_init($presignedURL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
curl_close($ch);

echo "Downloaded presigned URL data size: " . strlen($result) . PHP_EOL;
?>
```

## Python (boto3)

Recent boto3 versions (1.36+) work against Cloud Storage with default checksum settings. If a checksum error appears, disable checksum calculation and verification with the `Config` shown below.

```python
import requests
import uuid
import os
from botocore.config import Config
import boto3

config = Config(
    request_checksum_calculation="when_required",
    response_checksum_validation="when_required",
)

telnyx_api_key = os.getenv("TELNYX_API_KEY")
if not telnyx_api_key:
    print("TELNYX_API_KEY environment variable not set")
    exit(1)

client = boto3.client(
    "s3",
    endpoint_url="https://us-central-1.telnyxcloudstorage.com",
    aws_access_key_id=telnyx_api_key,
    aws_secret_access_key=telnyx_api_key,
    config=config
)

bucket_name = f"my-test-bucket-{uuid.uuid4()}"
client.create_bucket(Bucket=bucket_name)

for i in range(2):
    name = f"my-test-object-{i}"
    body = f"Telnyx Cloud Storage {i}"
    client.put_object(Bucket=bucket_name, Key=name, Body=body)

for obj in client.list_objects(Bucket=bucket_name)["Contents"]:
    print(obj["Key"])

result = client.get_object(Bucket=bucket_name, Key="my-test-object-0")
print(result["Body"].read())

response = requests.post(
    f"https://api.telnyx.com/v2/storage/buckets/{bucket_name}/my-test-object-0/presigned_url",
    json={"ttl": 30},
    headers={"Authorization": f"Bearer {telnyx_api_key}"},
)
body = response.json()
print(body)

response = requests.get(body["data"]["presigned_url"])
print(response.text)
```

## Ruby (AWS SDK for Ruby)

The Ruby example uses `Aws::S3::Resource` and demonstrates the full lifecycle: create bucket, list buckets, upload, download, generate a presigned URL, upload via the presigned URL, list objects, generate a download presigned URL, download via that URL, and finally clean up by deleting objects and the bucket.

```ruby
require "aws-sdk-s3"
require "net/http"
require "securerandom"
require "json"

telnyx_api_key = ENV["TELNYX_API_KEY"]

resource = Aws::S3::Resource.new(
  region: "us-central-1",
  endpoint: "https://us-central-1.telnyxcloudstorage.com",
  access_key_id: telnyx_api_key,
  secret_access_key: "doesn't matter"
)

bucket_name = "example-#{SecureRandom.hex(24)}"
bucket = resource.create_bucket(bucket: bucket_name)

resource.buckets.each { |b| puts " - #{b.name}" }

File.open("document.txt", "w+") { |f| f.write("This is a text document.\n") }

bucket = resource.bucket(bucket_name)
the_object = bucket.object("document.txt")
the_object.upload_file("document.txt")

file_name = "a-local-file.txt"
the_object.download_file(file_name)
puts "Contents of #{file_name}: #{File.read(file_name).inspect}"

# Presigned URL for upload
object_key = "important-document.txt"
uri = URI("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url")
response = Net::HTTP.post(uri, { ttl: 30 }.to_json, "Authorization" => "Bearer #{telnyx_api_key}")
raise "Bad response creating presigned URL" unless response.code == "200"

presigned_url = JSON.parse(response.body)["data"]["presigned_url"]

# Upload via the presigned URL
uri = URI(presigned_url)
request = Net::HTTP.new(uri.host)
response = request.put(uri, "This is an important text document.\n")
raise "Couldn't upload file using presigned URL" unless response.code == "200"

# List objects
bucket.objects.each { |o| puts " * #{o.key}" }

# Presigned URL for download
uri = URI("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url")
response = Net::HTTP.post(uri, { ttl: 30 }.to_json, "Authorization" => "Bearer #{telnyx_api_key}")
raise "Bad response creating presigned URL" unless response.code == "200"

presigned_url = JSON.parse(response.body)["data"]["presigned_url"]

# Download via the presigned URL
uri = URI(presigned_url)
response = Net::HTTP.get(uri)
puts "Downloaded object contents from presigned URL: #{response.inspect}"

# Cleanup
File.delete("document.txt")
File.delete("a-local-file.txt")
the_object.delete
bucket.object(object_key).delete
bucket.delete
```

## SDK-specific configuration notes

A few quirks are worth keeping in mind when porting these examples to other AWS SDKs:

- **Endpoint**: always `https://<region>.telnyxcloudstorage.com` (for example `us-central-1`).
- **Credentials**: the Telnyx API key is used as both the access key ID and the secret access key. The secret value is ignored, so any non-empty string is acceptable.
- **Path-style addressing**: required by the .NET, Node.js, and PHP SDKs (`ForcePathStyle = true`, `forcePathStyle: true`, `use_path_style_endpoint => true`).
- **Chunk encoding (.NET)**: must be disabled on every `PutObjectRequest` via `putObjectRequest.UseChunkEncoding = false`.
- **Checksums (Java, Node.js, Python)**: AWS SDK for Java v2 (2.30+), older AWS SDK for JavaScript v3, and older boto3 versions can fail with checksum errors. Set request checksum calculation and response checksum validation to `WHEN_REQUIRED` (or `when_required`) to avoid them.
- **Presigned URLs**: not generated by the AWS SDKs themselves — they are requested from the Telnyx REST API at `POST https://api.telnyx.com/v2/storage/buckets/{bucket}/{object}/presigned_url` with a JSON body of `{"ttl": <seconds>}` and a `Bearer` token header. The returned `data.presigned_url` can be used with any HTTP client for both upload and download.
