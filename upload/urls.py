from django.urls import path

from upload.views import UploadView

app_name = "upload"

urlpatterns = [path("", UploadView.as_view(), name="upload_page")]
