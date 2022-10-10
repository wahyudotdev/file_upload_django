from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        file_object = request.FILES["file"]
        file_name = str(file_object)
        print(f'[INFO] File Name: {file_name}')
        with open('public/'+file_name, 'wb+') as f:
            for chunk in file_object.chunks():
                f.write(chunk)
        return Response(status=204)
    
    def get(self, request, filename, format=None):
        file = open('public/tes.jpg', 'rb')
        response = FileResponse(file)
        return response