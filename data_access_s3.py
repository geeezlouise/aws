#
# File: data_access_s3.py
# Auth: Martin Burolla
# Date: 7/26/2022
# Desc: Simple data access wrapper around AWS S3
#
import boto3

import main
from botocore.exceptions import ClientError


def upload_to_s3():
    """ Upload to S3 """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file("Exercise1.txt", 'siu-avb-bucket', 'upload-file-stu5.txt')
    except ClientError as e:
        print(e)
        return False
    return True


def download_from_s3():
    """ Download from S3 """
    try:
        s3_client = boto3.client('s3')
        s3_client.download_file('siu-avb-bucket', 'upload-file-stu5.txt', 'download-file.txt')
    except ClientError as e:
        print(e)
        return False
    return True;
