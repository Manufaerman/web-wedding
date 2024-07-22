import dj_database_url
from decouple import config
import os

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

#AMAZON AWS DATABASE FOR STATICFILES
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_URL = 'https://weddin-page-bucket.s3.eu-north-1.amazonaws.com/'

AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = "virtual"
