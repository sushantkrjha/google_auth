from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .utils import upload_file_to_drive, list_drive_files, download_drive_file

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
    access_token = request.headers.get("Authorization").split(" ")[1]
    file_content = download_drive_file(access_token, file_id)
    response = Response(file_content, content_type="application/octet-stream")
    response['Content-Disposition'] = f'attachment; filename="{file_id}.bin"'
    return response
