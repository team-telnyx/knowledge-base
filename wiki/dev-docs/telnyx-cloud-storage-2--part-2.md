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

*Part 2 of 3 — see also: [Part 1](telnyx-cloud-storage-2--part-1.md), [Part 3](telnyx-cloud-storage-2--part-3.md)*

Telnyx Cloud Storage is an S3-compatible object storage service with regional endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs, and third-party tools. It offers features such as multipart uploads, server-side encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and a migration API for moving data from AWS S3 without incurring egress charges.

## Migration from AWS S3

The migration API moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without incurring AWS data egress charges. This is currently supported only for buckets located in the US.

### How It Works

The pipeline has three components:

1. **Source bucket** — Your AWS S3 bucket in AWS Region X.
2. **Migration engine** — Telnyx's migration engine in the same AWS Region X.
3. **Direct Connect links** — Telnyx's Direct Connect with AWS used to transfer the data.

Cost minimization relies on two AWS billing practices:

- **Intra-region data transfer** between S3 and EC2 (within the same account or across different accounts) is free of charge. The API selects co-located migration engines based on the source bucket's region.
- **Data Transfer Out (DTO) over AWS Direct Connect** within the same geopolitical region is heavily discounted compared to DTO over the internet. Telnyx's multi-cloud infrastructure takes advantage of these discounted rates.

The migration API is free during its beta stage. In the future, a minimum storage duration will be required to offset the costs Telnyx incurs for DTO over Direct Connect.

### Checking Coverage

Before migrating, verify that the source bucket's region is supported:

```bash
curl https://api.telnyx.com/v2/storage/migration_source_coverage \
  -H 'Authorization: Bearer XXX'
```

Response example:

```json
{
  "data": [
    { "provider": "aws", "source_region": "us-west-1" },
    { "provider": "aws", "source_region": "us-east-1" },
    { "provider": "aws", "source_region": "us-east-2" }
  ]
}
```

### Defining a Migration Source

Only the standard storage class is supported. Restore data from Glacier before attempting migration. Create a read-only IAM user for the source credentials.

```bash
curl -X POST https://api.telnyx.com/v2/storage/migration_sources \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer XXX' \
  -d '{
    "provider": "aws",
    "provider_auth": { "access_key": "XXX", "secret_access_key": "XXX" },
    "bucket_name": "source-west-bucket-demo"
  }'
```

Possible errors:

- **Bucket doesn't exist** — error code `15005`
- **Access denied** (bucket you don't own) — error code `15025`
- **Bucket region not supported** — error code `15003`

### Creating a Migration

If the target bucket doesn't exist, the API will attempt to create it. The source and target bucket regions do not need to match. When `refresh` is `false`, a one-time migration is created; when `true`, the API periodically synchronizes the source and destination.

```bash
curl -X POST https://api.telnyx.com/v2/storage/migrations \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer XXX' \
  -d '{
    "source_id": "1c73c8d9-d65a-4f61-ab41-afa095324c5d",
    "target_bucket_name": "target-bucket-test-account",
    "target_region": "us-west-1",
    "refresh": false
  }'
```

### Checking Migration Progress

Poll the migration endpoint to check status:

```bash
curl https://api.telnyx.com/v2/storage/migrations/{migration_id} \
  -H 'Authorization: Bearer XXX'
```

The response includes `status`, `bytes_to_migrate`, `bytes_migrated`, and `speed`. Alternatively, monitor the target bucket's metrics — when it reaches the expected size, the migration is complete.

## Performance Benchmarks

Benchmark results achieved with the described test setup:

- **PutObject Aggregate: 2.029 GiB/s**
- **GetObject Aggregate: 2.714 GiB/s**

### Benchmark Environment

Eight bare-metal client machines with 100 Gbps uplinks to the public internet initiated requests to a regional endpoint:

| Type | Node Count | CPU | Memory | Storage | Network |
| --- | --- | --- | --- | --- | --- |
| Type 1 | 4 | 64 cores | 2 TiB | 4 × 6.4 TiB NVMe | 100 Gbps |
| Type 2 | 4 | 32 cores | 2 TiB | 1 × 960 GiB NVMe | 100 Gbps |

- **Software**: [s3-benchmark](https://github.com/wasabi-tech/s3-benchmark)
- **Setup**: Each client reads and writes to its own individual bucket.
- **Note**: Test clients were not subject to the standard API rate limits. Results are indicative of achievable throughput with the given hardware and are not exhaustive.
