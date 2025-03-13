import requests
from django.conf import settings

# Google Drive API URLs
UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"
LIST_URL = "https://www.googleapis.com/drive/v3/files"
DOWNLOAD_URL = "https://www.googleapis.com/drive/v3/files/{}?alt=media"


def upload_file_to_drive(access_token, file):
    """
    Upload a file to Google Drive.
    
    :param access_token: OAuth 2.0 Access Token
    :param file: File object from request
    :return: JSON response from Google Drive API
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    files = {"file": (file.name, file.read()), "type":"image/jpeg"}
    response = requests.post(UPLOAD_URL, headers=headers, files=files)
    return response.json()


def list_drive_files(access_token):
    """
    List all files in the user's Google Drive.
    
    :param access_token: OAuth 2.0 Access Token
    :return: JSON response containing file list
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(LIST_URL, headers=headers)
    return response.json()


def download_drive_file(access_token, file_id):
    """
    Download a file from Google Drive.
    
    :param access_token: OAuth 2.0 Access Token
    :param file_id: ID of the file to download
    :return: File content as bytes
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(DOWNLOAD_URL.format(file_id), headers=headers)
    return response.content


#def download_drive_file(access_token, file_id):
    """
    Download a file from Google Drive.

    :param access_token: OAuth 2.0 Access Token
    :param file_id: ID of the file to download
    :return: (file_content, mime_type) if successful, otherwise (None, None)
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    file_metadata_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?fields=name,mimeType"

    try:
        # Get file metadata to determine MIME type
        metadata_response = requests.get(file_metadata_url, headers=headers)
        if metadata_response.status_code != 200:
            return None, None

        mime_type = metadata_response.json().get("mimeType", "application/octet-stream")

        # Download the file
        response = requests.get(DOWNLOAD_URL.format(file_id), headers=headers, stream=True)

        if response.status_code == 200:
            return response.content, mime_type
        else:
            return None, None
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return None, None
