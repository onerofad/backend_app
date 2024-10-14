from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Profile

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Profile})
