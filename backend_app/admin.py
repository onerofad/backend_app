from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Course, CourseDetails

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Course, CourseDetails})
