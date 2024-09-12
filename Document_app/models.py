from django.db import models

class FileUpload(models.Model):
    LOCAL = 'local'
    AWS = 'aws'
    STORAGE_CHOICES = [
        (LOCAL, 'Local'),
        (AWS, 'AWS'),
    ]

    local_path = models.CharField(max_length=255, blank=True, null=True)  # File path for local
    aws_url = models.URLField(max_length=255, blank=True, null=True)    # URL for AWS
    storage_type = models.CharField(max_length=10, choices=STORAGE_CHOICES, default=LOCAL)
    uploaded_at = models.DateTimeField(auto_now_add=True)
