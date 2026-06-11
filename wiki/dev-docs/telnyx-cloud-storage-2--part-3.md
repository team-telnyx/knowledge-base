---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service with regional
  endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs,
  and third-party tools. It offers features such as multipart uploads, server-side
  encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and
  a migration API for moving data from AWS S3 without incurring egress charges.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/limits
  content_hash: 24f49c9582d0c5a30ffa575a68049c87b6e5b6cb2a5d0567d6ee90f9ea1cea3c
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
  content_hash: f9f9a5deb4bdb660bb5f6386138544fa93595dc7fed90f1ad21b29aedb28da63
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
  content_hash: d24656b29d4d25319ed19e019faa1502bd63241ee8caa34245566a30a9ae2d9f
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
  content_hash: e50545d8ccb7bdbb7078d5a723f8f56b5f8c2f6b5f2daa4b795bcee24897f61f
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
  content_hash: 498cc4adc4dc9424830f642f7e1e9acf41a1954d23d1df14c77f001875a52cc9
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
  content_hash: 06c1cbf807e85d60eb6a9a2ea29cdba014ed3604bfeaad734b50fc4be138b895
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
  content_hash: 408b9104b09add8d303a178ac4a326a7db9ba4cd863efe20a46f94fb37bd2167
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
  content_hash: 93a31249f40112b3a310daf212d8e288c2f43af5f00c00b6119900103e07d993
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
  content_hash: a261305feaf573eba7a5910a73e23ae760af8e6f495b4c8186a787a1f3e81461
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
  content_hash: 4ad324916691dae831f9f1db6e1af180cba46d72f13906f6537fa8bc95f03dfa
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
  content_hash: 214b3b4c17a4e1d1b536f2747838add56b73d5484cdd4ecce46aecb50780e25b
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
  content_hash: c32c9c35943b00a259ad917b228e7d9baa10b798c35f6364d1fb7bdc7a5449bb
updated_at: 2026-06-11T10:25:05Z
---

# Telnyx Cloud Storage

*Part 3 of 3 — see also: [Part 1](telnyx-cloud-storage-2--part-1.md), [Part 2](telnyx-cloud-storage-2--part-2.md)*

Telnyx Cloud Storage is an S3-compatible object storage service with regional endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs, and third-party tools. It offers features such as multipart uploads, server-side encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and a migration API for moving data from AWS S3 without incurring egress charges.

## SDK Examples

### Common Configuration Notes

- Use your Telnyx API key as both the access key ID and secret access key when configuring AWS SDK credentials.
- Set the endpoint to `https://{region}.telnyxcloudstorage.com`.
- **Chunk encoding is not supported** by the Cloud Storage API. In the .NET SDK, set `putObjectRequest.UseChunkEncoding = false`.
- **For AWS Java SDK v2.30+**, disable checksum calculation and verification by setting `requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)` and `responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)`.
- Presigned URLs must be generated via the Telnyx API, not via the SDK's built-in presigned URL methods.

### Go (AWS SDK for Go v2)

```go
package main

import (
    "bytes"
    "context"
    crand "crypto/rand"
    "encoding/json"
    "fmt"
    "io"
    "log"
    "math/rand"
    "net/http"
    "os"
    "time"

    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
    ctx := context.Background()
    randSeq := rand.Intn(1_000_000)

    telnyxAPIKey := os.Getenv("TELNYX_API_KEY")
    if telnyxAPIKey == "" {
        log.Fatal("TELNYX_API_KEY environment variable not set")
    }

    region := "us-central-1"
    endpoint := fmt.Sprintf("https://%s.telnyxcloudstorage.com", region)

    cfg, err := config.LoadDefaultConfig(ctx,
        config.WithRegion(region),
        config.WithCredentialsProvider(aws.CredentialsProviderFunc(
            func(context.Context) (aws.Credentials, error) {
                return aws.Credentials{
                    AccessKeyID:     telnyxAPIKey,
                    SecretAccessKey: telnyxAPIKey,
                }, nil
            })),
        config.WithS3UseARNRegion(true),
        config.WithS3DisableExpressAuth(true),
        config.WithS3DisableMultiRegionAccessPoints(true),
    )
    if err != nil {
        log.Fatalf("s3 configuration error: %v", err)
    }
    cfg.BaseEndpoint = aws.String(endpoint)

    s3Client := s3.NewFromConfig(cfg)

    // Create bucket, upload objects, list objects, download objects, and
    // generate presigned URLs via the Telnyx API as shown in the full example.
    _ = s3Client
    _ = randSeq
}
```

Run with `TELNYX_API_KEY=_YOUR_API_KEY go run main.go`.

### Java (AWS SDK for Java v2)

Add the dependency:

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.20.0</version>
</dependency>
```

Create an S3 client:

```java
S3Client s3 = S3Client.builder()
    .region(Region.US_EAST_1)
    .endpointOverride(URI.create("https://us-central-1.telnyxcloudstorage.com"))
    .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
    .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
    .credentialsProvider(
        StaticCredentialsProvider.create(
            AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
    .build();
```

For presigned URLs, call the Telnyx API directly using an HTTP client (e.g., OkHttp) with a JSON body `{"TTL": 30}` to `POST /v2/storage/buckets/{bucket}/{key}/presigned_url`.

### .NET (AWS SDK for .NET)

```csharp
var s3Config = new AmazonS3Config
{
    ServiceURL = $"https://{region}.telnyxcloudstorage.com",
    ForcePathStyle = true,
    SignatureVersion = "4",
};

var telnyxClient = new AmazonS3Client(
    new BasicAWSCredentials(apiKeyTelnyx, apiKeyTelnyx),
    s3Config
);
```

**Important**: Set `putObjectRequest.UseChunkEncoding = false` since chunk encoding is not supported.

For presigned URLs, use `HttpClient` to call `POST /v2/storage/buckets/{bucket}/{key}/presigned_url` with a JSON body `{"ttl": 200}` and a Bearer authorization header.

### Elixir (AWS Elixir SDK)

Add dependencies to `mix.exs`:

```elixir
{:aws, "~> 1.0.0"},
{:hackney, "~> 1.18"}
```

Create the client:

```elixir
telnyx_storage_client =
  AWS.Client.create(
    System.fetch_env!("TELNYX_V2_API_KEY"),
    "",  # secret access key can be left blank
    System.get_env("TELNYX_STORAGE_REGION", "us-east-1")
  )
  |> AWS.Client.put_endpoint(fn options -> "#{options.region}.telnyxcloudstorage.com" end)
```

For presigned URLs, use the `Req` library with `Jason` to call the Telnyx API:

```elixir
{:ok, %{body: %{"data" => %{"presigned_url" => presigned_url}}}} =
  Req.post("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url",
    headers: %{"authorization" => "Bearer #{api_key}"},
    json: %{"ttl" => 30}
  )
```
