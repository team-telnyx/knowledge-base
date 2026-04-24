---
title: AWS .Net SDK Example
summary: Chunk encoding is not supported by the Cloud Storage API.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet/index
    content_hash: e29cf2f15809acf71c1b5d6c9c8a287aa7a362ff9c862d7e1549fdde0396d90d
updated_at: 2026-04-10T00:00:00Z
---

# AWS .Net SDK Example

<Callout type="warning">
  Chunk encoding is not supported by the Cloud Storage API. Please set `putObjectRequest.UseChunkEncoding = false`.

The following example shows how AWS .Net SDK can be used to interact with Telnyx Cloud Storage.

```csharp theme={null}
using System.Text;
using System.Text.Json;
using Amazon.Runtime;
using Amazon.S3;
using Amazon.S3.Model;

// 1. Configure and create Telnyx API Client

var apiKeyTelnyx = "API-KEY-HERE";
var bucketName = "BUCKET-NAME-HERE";
var objectName = "OBJECT-NAME-HERE";
var region = "us-central-1";

var s3Config = new AmazonS3Config
{
   ServiceURL = $"https://{region}.telnyxcloudstorage.com",
   ForcePathStyle = true,
   LogResponse = true,
   DisableLogging = false,
   SignatureVersion = "4",
};

var telnyxClient = new AmazonS3Client(
   new BasicAWSCredentials(apiKeyTelnyx, apiKeyTelnyx),
   s3Config
);

// 2. Create Bucket

var createBucketRequest = new PutBucketRequest
{
   BucketName = bucketName
};
var createBucketResponse = await telnyxClient.PutBucketAsync(createBucketRequest);

// 3. Upload object

var putObjectRequest = new PutObjectRequest
{
   BucketName = bucketName,
   Key = "objectName",
   FilePath = "/Users/yiuming/test.txt"
};
// IMPORTANT: chunk encoding is not supported by the Cloud Storage API.
putObjectRequest.UseChunkEncoding = false;
var putObjectResponse = await telnyxClient.PutObjectAsync(putObjectRequest);

// 4. List Objects

var listObjectRequest = new ListObjectsRequest
{
   BucketName = bucketName
};
var listObjectResponse = await telnyxClient.ListObjectsAsync(listObjectRequest);

// 5. List Buckets

var listBucketsRequest = new ListBucketsRequest { };
var listBucketsResponse = await telnyxClient.ListBucketsAsync(listBucketsRequest);

// 6. Download Object

var getObjectRequest = new GetObjectRequest
{
   BucketName = bucketName,
   Key = objectName
};
var getObjectResponse = await telnyxClient.GetObjectAsync(getObjectRequest);

// 7. Presigned URL Get
using (HttpClient client = new HttpClient())
{
   client.BaseAddress = new Uri("https://api.telnyx.com");
   var presignedUrlRequest = new Dictionary<string, object>
   {
       { "ttl", 200 }
   };
   var presignedUrlRequestJson = JsonSerializer.Serialize(presignedUrlRequest);
   var presignedUrlRequestContent = new StringContent(
       presignedUrlRequestJson,
       Encoding.UTF8,
       "application/json");

   client.DefaultRequestHeaders.Authorization =
       new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", apiKeyTelnyx);
   var presignedUrlResponse =
       await client.PostAsync($"/v2/storage/buckets/{bucketName}/{objectName}/presigned_url",
           presignedUrlRequestContent);
   var content = await presignedUrlResponse.Content.ReadAsStringAsync();
   Console.WriteLine(content);
}
```


## Related Pages

- [AWS PHP SDK Example](../runbooks/aws-php-sdk-example.md)
- [AWS Elixir SDK Example](../runbooks/aws-elixir-sdk-example.md)
- [AWS Golang SDK Example](../runbooks/aws-golang-sdk-example.md)
- [AWS Java SDK Example](../runbooks/aws-java-sdk-example.md)
- [AWS Node.js SDK Example](../runbooks/aws-node-js-sdk-example.md)
