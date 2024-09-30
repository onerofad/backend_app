from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, UploadedFiles
from .serializers import RegisterSerializer, UploadedFilesSerializer

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class UploadedFilesView(viewsets.ModelViewSet):
    queryset = UploadedFiles.objects.all()
    serializer_class = UploadedFilesSerializer
