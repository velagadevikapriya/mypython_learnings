import boto3

# Initialize S3 client
s3 = boto3.client('s3') 

# Your S3 bucket name
BUCKET_NAME = "dpvtest123"
s3_key = "s3ex.csv"
local_file = "local_downloaded.csv"

# Upload a file to S3
try:
    s3.upload_file("Items1.csv", BUCKET_NAME, s3_key)
    print("File uploaded successfully!")
except Exception as e:
    print(f" Upload failed: {e}")

def download_file(s3_key, local_file):
    try:
        s3.download_file(BUCKET_NAME, s3_key, local_file)
        print(f"File '{s3_key}' downloaded as '{local_file}'.")
    except Exception as e:
        print(f"Download failed: {e}")


# List files in the S3 bucket
def list_files():
    # """List all files in the S3 bucket"""
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            print("Files in S3 Bucket:")
            for obj in response["Contents"]:
                print(f" - {obj['Key']}")
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Listing files failed: {e}")

# Delete a file from S3
def delete_file(s3_key):
    # """Delete a file from S3"""
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=s3_key)
        print(f"🗑️ File '{s3_key}' deleted from S3.")
    except Exception as e:
        print(f" Delete failed: {e}")

# Example Usage
