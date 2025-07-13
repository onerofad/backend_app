from django.contrib import admin
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Tutorial, Owner, Content, CartItems, Newfolder, MyLearning, UploadFileToFolder, Support, TableData, Groups, GroupMembers, GroupUpload

admin.site.register({Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Tutorial, Owner, Content, CartItems, Newfolder, MyLearning, UploadFileToFolder, Support, TableData, GroupUpload, Groups, GroupMembers})
