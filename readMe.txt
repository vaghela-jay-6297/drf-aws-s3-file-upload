DRF File Upload with AWS S3 and Local Storage

Overview:
This Django Rest Framework (DRF) project provides functionality for file uploads with support for two storage options: Amazon S3 and local storage. Depending on the user's choice, files are either uploaded to AWS S3 or stored locally. The file URL or path, along with the selected storage type, is then stored in the database.

Features:
Dual Storage Options: Users can choose between AWS S3 and local storage for file uploads.
AWS S3 Integration: Upload files to Amazon S3 and store the S3 URL in the database.
Local Storage: Upload files to a local directory and store the local file path in the database.
Dynamic Storage Handling: Store the chosen storage type and file reference in the database for easy retrieval.

Prerequisites:
Python 3.6+
Django 3.0+
Django Rest Framework 3.11+
boto3 (for AWS S3 integration)

Update Django Settings:
# settings.py
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
