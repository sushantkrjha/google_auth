from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('google-drive/', include('drive.urls')),
]
