from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_google_auth_url, get_google_access_token, get_google_user_info

@api_view(['GET'])
def google_login(request):
    return Response({"auth_url": get_google_auth_url()})

@api_view(['GET'])
def google_callback(request):
    auth_code = request.GET.get("code")
    token_response = get_google_access_token(auth_code)
    access_token = token_response.get("access_token")
    user_info = get_google_user_info(access_token)
    return Response({"user": user_info, "token": token_response})
