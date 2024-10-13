from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Form1

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Form1})
