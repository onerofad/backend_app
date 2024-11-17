from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Member

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Member})
