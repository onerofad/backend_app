from django.contrib import admin
from .models import Register, LocalTransfer

admin.site.register({Register, LocalTransfer})
