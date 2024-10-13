from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Student

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Student})
