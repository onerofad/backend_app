from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio

admin.site.register({Register, UploadedFiles, UploadedAudio})
