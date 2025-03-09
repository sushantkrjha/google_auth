## Google Authentication and Google Drive Integration project

Google OAuth and Google Drive API Integration in Django REST Framework
This project demonstrates how to integrate Google OAuth authentication and Google Drive API functionalities (upload, list, and download files) in a Django REST Framework (DRF) application.

## Features
1. Google OAuth authentication
2. Upload files to Google Drive
3. List files from Google Drive
4. Download files from Google Drive

## Set Up Environment Variables
Configure the following variables in .env or settings.py

1. GOOGLE_CLIENT_ID = "your-google-client-id"
2. GOOGLE_CLIENT_SECRET = "your-google-client-secret"
3. GOOGLE_REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback/"
4. GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
5. GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
6. GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"


## Setup Instructions

1. Prerequisites
2. Python 3.8+
3. Django 4+
4. Django REST Framework
5. Google OAuth credentials (Client ID, Client Secret, Redirect URI)
6. Google Drive API enabled in Google Cloud Console

## Create a virtual environment
1. python -m venv venv
2. source venv/bin/activate

## Install dependencies
1. pip install -r requirements.txt

## Apply Migrations & Run the Server
    1. python manage.py migrate
    2. python manage.py runserver




## Usage

1. Authenticate with Google
Make a GET request to /auth/google/login/ to get the authentication URL.
Redirect users to the provided URL to authenticate with Google.
Upon successful authentication, Google redirects to /auth/google/callback/ with an authorization code.

2. Upload a File
Send a POST request to /google-drive/upload/ with an Authorization header containing the access token and a file in the request body.

3. List Files
Send a GET request to /google-drive/files/ with an Authorization header containing the access token.

4. Download a File
Send a GET request to /google-drive/download/<file_id>/ with an Authorization header containing the access token.



## 1.1 Login with Google OAuth
    Request:
    GET http://127.0.0.1:8000/auth/google/login/

        Response:
        {
            "auth_url": "https://accounts.google.com/o/oauth2/auth?response_type=code&..."
        }

## 1.2 OAuth Callback
    Google will redirect the user to this endpoint with a code parameter.
    Request:
    GET http://127.0.0.1:8000/auth/google/callback/?code=AUTH_CODE

    Response:
        {
            "user": {
                "id": "123456789",
                "email": "user@example.com",
                "name": "John Doe"
            },
            "token": {
                "access_token": "ya29.a0AfH6...",
                "expires_in": 3600,
                "refresh_token": "1//0g5..."
            }
        }



## 2.1 Upload a File
    Request:
    POST http://127.0.0.1:8000/google-drive/upload/
    Authorization: Bearer ACCESS_TOKEN
    Content-Type: multipart/form-data

    Body:
        {
        "file": "<upload_file>"
    }


    Response:
        {
            "id": "1HfPq...",
            "name": "uploaded_file.jpg"
        }



## 2.2 List Files
    Request:
        GET http://127.0.0.1:8000/google-drive/files/
        Authorization: Bearer ACCESS_TOKEN

## Response:
    {
        "files": [
            {"id": "1HfPq...", "name": "file1.jpg"},
            {"id": "2GfQd...", "name": "file2.png"}
        ]
    }

## 2.3 Download a File
    Request:
        GET http://127.0.0.1:8000/google-drive/download/1HfPq...
        Authorization: Bearer ACCESS_TOKEN


## Conclusion
This API provides a secure way to authenticate users using Google OAuth and interact with Google Drive for file operations.



