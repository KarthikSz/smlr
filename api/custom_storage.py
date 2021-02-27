import os

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = str(os.environ.get('AWS_STORAGE_BUCKET_NAME'))
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
    location = str(os.environ.get('AWS_LOCATION'))

class VideoStorage(S3Boto3Storage):
    bucket_name = str(os.environ.get('AWS_STORAGE_BUCKET_NAME'))
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
    location = str(os.environ.get('AWS_LOCATION'))