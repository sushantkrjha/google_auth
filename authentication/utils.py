import requests
from django.conf import settings

# Fetch OAuth credentials from Django settings
GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = settings.GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI = settings.GOOGLE_REDIRECT_URI

# Ensure credentials are set properly
if not all([GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI]):
    raise ValueError("Google OAuth credentials are missing in settings.py!")

def get_google_auth_url():
    """Generate Google OAuth authorization URL."""
    params = {
        "response_type": "code",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "scope": "openid email profile https://www.googleapis.com/auth/drive.file",
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"{settings.GOOGLE_AUTH_URL}?{requests.compat.urlencode(params)}"

def get_google_access_token(auth_code):
    """Exchange authorization code for access token."""
    data = {
        "code": auth_code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    response = requests.post(settings.GOOGLE_TOKEN_URL, data=data)
    response.raise_for_status()
    return response.json()

def get_google_user_info(access_token):
    """Fetch user profile information using access token."""
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(settings.GOOGLE_USERINFO_URL, headers=headers)
    response.raise_for_status()
    return response.json()
