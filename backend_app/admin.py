from django.contrib import admin
from .models import Register, UploadedFiles

admin.site.register({Register, UploadedFiles})
