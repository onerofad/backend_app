from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile})
