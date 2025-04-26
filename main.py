import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
            )
        bucket_name = os.getenv("AWS_BUCKET_NAME")
        response = s3.list_objects_v2(Bucket=bucket_name)
        print("Files in bucket:")
        for obj in response.get('Contents', []):
            print(obj['Key'])
    except Exception as e:
        print(f"Error initializing S3 client: {e}")
        return


if __name__ == "__main__":
    main()
