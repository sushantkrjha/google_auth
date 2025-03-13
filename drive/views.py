from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .utils import upload_file_to_drive, list_drive_files, download_drive_file
from django.http import HttpResponse 
import mimetypes

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    access_token = request.headers.get("Authorization").split(" ")[1]
    file = request.FILES['file']
    response = upload_file_to_drive(access_token, file)
    return Response(response)

@api_view(['GET'])
def list_files(request):
    access_token = request.headers.get("Authorization").split(" ")[1]
    response = list_drive_files(access_token)
    return Response(response)

@api_view(['GET'])
def download_file(request, file_id):
    #import pdb;pdb.set_trace()
    access_token = request.headers.get("Authorization").split(" ")[1]
    file_content, file_mime_type = download_drive_file(access_token, file_id)
    print(file_mime_type)
    file_extension = mimetypes.guess_extension(file_mime_type) or ".bin"
    filename = f"{file_id}{file_extension}"

    response = HttpResponse(file_content, content_type=file_mime_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
