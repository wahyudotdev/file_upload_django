import os
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, filename, format=None):
        file_object = request.FILES["file"]
        file_name = str(file_object)
        print(f'[INFO] File Name: {file_name}')
        if (not os.path.exists("public")):
            os.mkdir("public")
        with open('public/'+file_name, 'wb+') as f:
            for chunk in file_object.chunks():
                f.write(chunk)
        return Response(status=204)
    
    def get(self, request, filename, format=None):
        file = open('public/'+filename, 'rb')
        response = FileResponse(file)
        return response