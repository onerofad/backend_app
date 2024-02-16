from django.contrib import admin
from .models import Register, LocalTransfer, SaveAccount

admin.site.register({Register, LocalTransfer, SaveAccount})
