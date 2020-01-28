import logging
import boto3
import sys
import os
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

if __name__ == "__main__":
    bucket = os.getenv("AWS_S3_BACKUP_BUCKET", None)
    if bucket is None:
        exit("AWS_S3_BACKUP_BUCKET must be set")

    result = upload_file(str(sys.argv[1]), bucket, "archive-latest.tar.gz")
    print(f"Upload result: {result}")

    result = upload_file(str(sys.argv[1]), bucket, str(sys.argv[1]))
    print(f"Upload result: {result}")
