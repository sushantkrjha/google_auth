from django.urls import path
from .views import upload_file, list_files, download_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('files/', list_files, name='list_files'),
    path('download/<str:file_id>/', download_file, name='download_file'),
]
