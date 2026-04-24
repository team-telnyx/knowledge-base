---
title: AWS PHP SDK Example
summary: The following example shows how AWS PHP SDK can be used to interact with Telnyx Cloud Storage.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/php/index
    content_hash: 7f2fcc74321645c0e9847d7111905920ce5e8e1f9733af278017c88a48cba3f0
updated_at: 2026-04-10T00:00:00Z
---

# AWS PHP SDK Example

The following example shows how AWS PHP SDK can be used to interact with Telnyx Cloud Storage.

```php theme={null}
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Credentials\CredentialProvider;
use Aws\Exception\AwsException;

$telnyxAPIKey = getenv('TELNYX_API_KEY');
if (!$telnyxAPIKey) {
	die('TELNYX_API_KEY environment variable not set');
}

$region = 'us-central-1';
$endpoint = "https://{$region}.telnyxcloudstorage.com";

// 1. Initializing the AWS client with specific options
$s3Client = new S3Client([
	'region'  => $region,
	'version' => 'latest',
	'endpoint' => $endpoint,
	'credentials' => [
    	'key'	=> $telnyxAPIKey,
    	'secret' => $telnyxAPIKey,
	],
	'use_path_style_endpoint' => true
]);

$bucketName = "test-bucket-" . $region . '-' . date('H-i') . '-' . rand(0, 1000000);
echo "Generated bucket name: " . $bucketName . PHP_EOL;

// 2. Create a bucket
try {
	$s3Client->createBucket([
    	'Bucket' => $bucketName
	]);
	echo "Created bucket: {$bucketName}" . PHP_EOL;
} catch (AwsException $e) {
	die("Unable to create bucket: " . $e->getMessage());
}

// 3. Upload two objects with random data
for ($i = 0; $i < 2; $i++) {
	$content = random_bytes(1024 * 32); // 32KB of random data
	$objName = "{$i}.txt";
	try {
    	$s3Client->putObject([
        	'Bucket' => $bucketName,
        	'Key'	=> $objName,
        	'Body'   => $content
    	]);
    	echo "Uploaded file ({$objName}) to bucket: {$bucketName}" . PHP_EOL;
	} catch (AwsException $e) {
    	die("Unable to upload file ({$objName}): " . $e->getMessage());
	}
}

// 4. List objects in the bucket
try {
	$result = $s3Client->listObjects([
    	'Bucket' => $bucketName
	]);
	foreach ($result['Contents'] as $item) {
    	echo "Listed object: " . $item['Key'] . PHP_EOL;
	}
} catch (AwsException $e) {
	die("Unable to list objects: " . $e->getMessage());
}

// 5. Download the first object
try {
	$result = $s3Client->getObject([
    	'Bucket' => $bucketName,
    	'Key'	=> '1.txt'
	]);
	$data = $result['Body']->getContents();
	echo "Downloaded file size: " . strlen($data) . PHP_EOL;
} catch (AwsException $e) {
	die("Unable to download object: " . $e->getMessage());
}

// 6. Create a presigned URL for the first file
$url = "https://api.telnyx.com/v2/storage/buckets/{$bucketName}/1.txt/presigned_url";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['TTL' => 30]));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
	'Authorization: Bearer ' . $telnyxAPIKey,
	'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpcode != 200) {
	die("Unexpected status code: {$httpcode} | response: {$response}");
}

$presignedData = json_decode($response, true);
$presignedURL = $presignedData['data']['presigned_url'];
echo "Generated presigned URL: {$presignedURL}" . PHP_EOL;

// 7. Download the file using the presigned URL
$ch = curl_init($presignedURL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
curl_close($ch);

echo "Downloaded presigned URL data size: " . strlen($result) . PHP_EOL;
?>
```


## Related Pages

- [AWS .Net SDK Example](../runbooks/aws-net-sdk-example.md)
- [AWS Java SDK Example](../runbooks/aws-java-sdk-example.md)
- [AWS Elixir SDK Example](../runbooks/aws-elixir-sdk-example.md)
- [AWS Golang SDK Example](../runbooks/aws-golang-sdk-example.md)
- [AWS Node.js SDK Example](../runbooks/aws-node-js-sdk-example.md)
