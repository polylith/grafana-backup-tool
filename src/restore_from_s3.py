import boto3
import os

if __name__ == "__main__":
    bucket = os.getenv("AWS_S3_BACKUP_BUCKET", None)
    if bucket is None:
        exit("AWS_S3_BACKUP_BUCKET must be set")

    s3 = boto3.client('s3')
    s3.download_file(bucket, 'archive-latest.tar.gz', 'archive-latest.tar.gz')
