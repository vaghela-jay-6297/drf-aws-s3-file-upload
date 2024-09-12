import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import FileUploadSerializer
from .models import FileUpload
import boto3
from botocore.exceptions import NoCredentialsError

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        storage_type = request.data.get('storage_type', 'local')  # 'local' or 'aws'
        
        if storage_type == 'local':
            # Save file locally
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            # Save file path in the database
            upload = FileUpload(local_path=file_path, storage_type=FileUpload.LOCAL)
            upload.save()
            serializer = FileUploadSerializer(upload)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif storage_type == 'aws':
            # Upload to AWS S3
            s3 = boto3.client('s3', 
                              aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                              aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
            
            try:
                s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
                file_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file.name}"
                
                # Save file URL in the database
                upload = FileUpload(aws_url=file_url, storage_type=FileUpload.AWS)
                upload.save()
                serializer = FileUploadSerializer(upload)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            except NoCredentialsError:
                return Response({'error': 'AWS credentials not available'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'error': 'Invalid storage type'}, status=status.HTTP_400_BAD_REQUEST)
