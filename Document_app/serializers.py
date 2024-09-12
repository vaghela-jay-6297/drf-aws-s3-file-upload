from rest_framework import serializers
from .models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['local_path', 'aws_url', 'storage_type', 'uploaded_at']

    # def validate_storage_type(self, value):
    #     if value != 'aws' or value != 'local':
    #         raise serializers.ValidationError("please select storage type!")    
    #     return super().validate(value)

