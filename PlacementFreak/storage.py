from storages.backends.s3boto3 import S3Boto3Storage
import environ
env = environ.Env()
environ.Env.read_env()

class MediaStorage(S3Boto3Storage):
    bucket_name = env('AWS_STORAGE_BUCKET_NAME')
    location = env('AWS_MEDIA_ROOT')
    
class StaticStorage(S3Boto3Storage):
    bucket_name = env('AWS_STORAGE_BUCKET_NAME')
    location = env('AWS_STATIC_ROOT')