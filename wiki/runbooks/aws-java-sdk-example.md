---
title: AWS Java SDK Example
summary: 'AWS Java SDK example for Telnyx Cloud Storage. For versions 2.30+, disable checksum calculation and verification.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/java/index
    content_hash: 2c78b265b37bd645cce4feabf7b803b73dad0aa0f2a8d449284bf4f97aad7a85
updated_at: 2026-04-10T00:00:00Z
---

# AWS Java SDK Example

<Callout type="warning">
  **For versions 2.30+, make sure you disable checksum calculation and verification.**

The following example shows how AWS Java SDK can be used to interact with Telnyx Cloud Storage.

## Add Dependency

```
<dependency>
	<groupId>software.amazon.awssdk</groupId>
	<artifactId>s3</artifactId>
	<version>2.20.0</version> <!--  Or any 2.x version -->
</dependency>
```

## Create S3 Bucket

```
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;

public class CreateBucket {

	public static void main(String[] args) {
    	String bucketName = "--your-bucket-name--";
    	Region region = Region.US_EAST_1;
    	String telnyxUrl = "https://us-central-1.telnyxcloudstorage.com";
    	String telnyxApiKey = "-- api key --";

    	// Create an S3 client
    	S3Client s3 = S3Client.builder()
            	.region(region)
            	.endpointOverride(URI.create(telnyxUrl))
                // Only perform CRC checks `when_required`
                .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
                .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
            	.credentialsProvider(
                    	StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
            	.build();

    	// create bucket
    	CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
            	.bucket(bucketName)
            	.build();

    	s3.createBucket(createBucketRequest);
    	System.out.println("Bucket created successfully: " + bucketName);

    	// Close the S3 client
    	s3.close();
	}

}
```

## Upload an Object

```
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.net.URI;
import java.nio.file.Paths;

public class UploadObjectToS3 {

	public static void main(String[] args) {
    	String bucketName = "--your-bucket-name--";
    	String keyName = "your-object-key";
    	String filePath = "--path to file for upload--";

    	Region region = Region.US_EAST_1;
    	String telnyxUrl = "https://us-central-1.telnyxcloudstorage.com";
    	String telnyxApiKey = "--your api key --";

    	// Create an S3 client
    	S3Client s3 = S3Client.builder()
            	.region(region)
            	.endpointOverride(URI.create(telnyxUrl))
            	.credentialsProvider(
                    	StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
            	.build();

    	// upload object
    	PutObjectRequest putObjectRequest = PutObjectRequest.builder()
            	.bucket(bucketName)
            	.key(keyName)
            	.build();

    	// Upload the file to S3
    	s3.putObject(putObjectRequest, RequestBody.fromFile(Paths.get(filePath)));

    	// Close the S3 client
    	s3.close();
	}

}
```

## List Objects

```
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;

import java.net.URI;

public class ListObjects {

	public static void main(String[] args) {
    	String bucketName = "--your-bucket-name--";
    	Region region = Region.US_EAST_1;
    	String telnyxUrl = "https://us-central-1.telnyxcloudstorage.com";
    	String telnyxApiKey = "--your api key --";

    	// Create an S3 client
    	S3Client s3 = S3Client.builder()
            	.region(region)
            	.endpointOverride(URI.create(telnyxUrl))
            	.credentialsProvider(
                    	StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
            	.build();
    	// Create a ListObjectsV2Request
    	ListObjectsV2Request listObjectsRequest = ListObjectsV2Request.builder()
            	.bucket(bucketName)
            	.build();

    	// Get the list of objects in the bucket
    	ListObjectsV2Response listObjectsResponse = s3.listObjectsV2(listObjectsRequest);

    	for (S3Object s3Object : listObjectsResponse.contents()) {
        	System.out.println( s3Object.key());
    	}

    	// Close the S3 client
    	s3.close();
	}

}
```

## Download Object

```
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;

public class DownloadObject {

	public static void main(String[] args) throws IOException {
    	String bucketName = "--your-bucket-name--";
    	Region region = Region.US_EAST_1;
    	String telnyxUrl = "https://us-central-1.telnyxcloudstorage.com";
    	String telnyxApiKey = "--your api key --";
    	String keyName = "your-object-key";

    	S3Client s3 = S3Client.builder()
            	.region(region)
            	.endpointOverride(URI.create(telnyxUrl))
            	.credentialsProvider(
                    	StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
            	.build();

    	// Create a GetObjectRequest
    	GetObjectRequest getObjectRequest = GetObjectRequest.builder()
            	.bucket(bucketName)
            	.key(keyName)
            	.build();

    	// Download the object and transform the response to a byte array
    	ResponseBytes objectBytes = s3.getObject(getObjectRequest, ResponseTransformer.toBytes());

    	// Write the file to the specified path
    	File downloadedFile = new File("-- path to where to save the file --");
    	try (FileOutputStream fos = new FileOutputStream(downloadedFile)) {
        	fos.write(objectBytes.asByteArray());
        	System.out.println("File downloaded successfully to -- path to where to save the file --");
    	}

    	// Close the S3 client
    	s3.close();
	}

}
```

## Generate Presigned URLs for Upload and Download

In order for this part to work, we will need to add json decoding library and http client. Any libraries will do, but for this example we picked: gson and okhttp3.

```
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

```
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import okhttp3.*;

import java.io.IOException;
import java.util.Map;

public class GeneratePresignedURLAndDownloadObject {

	public static void main(String[] args) throws IOException {
    	OkHttpClient httpClient = new OkHttpClient();
    	Gson gson = new Gson();

    	String presignedUrlRequestJson = gson.toJson(Map.of("TTL", 30));
    	RequestBody presignedUrlRequestBody = RequestBody.create(MediaType.parse("application/json"), presignedUrlRequestJson);

    	Request presignedUrlRequest = new Request.Builder()
            	.url("https://api.telnyx.com/v2/storage/buckets/-- name of the bucket --/--name of the object--/presigned_url")
            	.header("Authorization", "Bearer --your api key---")
            	.post(presignedUrlRequestBody)
            	.build();

    	try (Response response = httpClient.newCall(presignedUrlRequest).execute()) {
        	if (!response.isSuccessful()) {
            	throw new IOException("Failed to create presigned URL: " + response);
        	}
        	String responseBody = response.body().string();
        	Map<String, Object> responseBodyMap = gson.fromJson(responseBody, new TypeToken<Map<String, Object>>() {}.getType());
        	String presignedUrl = ((Map<String, String>) responseBodyMap.get("data")).get("presigned_url");

        	System.out.println("Presigned URL: " + presignedUrl);

        	// 6. Download the file using the presigned URL
        	Request downloadRequest = new Request.Builder()
                	.url(presignedUrl)
                	.build();

        	try (Response downloadResponse = httpClient.newCall(downloadRequest).execute()) {
            	if (!downloadResponse.isSuccessful()) {
                	throw new IOException("Failed to download file using presigned URL: " + downloadResponse);
            	}
            	System.out.println("Downloaded via presigned URL: " + downloadResponse.body().string());
        	}
    	}
	}
}
```


## Related Pages

- [AWS PHP SDK Example](../runbooks/aws-php-sdk-example.md)
- [AWS Golang SDK Example](../runbooks/aws-golang-sdk-example.md)
- [AWS .Net SDK Example](../runbooks/aws-net-sdk-example.md)
- [AWS Node.js SDK Example](../runbooks/aws-node-js-sdk-example.md)
- [AWS Elixir SDK Example](../runbooks/aws-elixir-sdk-example.md)
