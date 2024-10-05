from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class UploadedFilesView(viewsets.ModelViewSet):
    queryset = UploadedFiles.objects.all()
    serializer_class = UploadedFilesSerializer

class UploadedAudioView(viewsets.ModelViewSet):
    queryset = UploadedAudio.objects.all()
    serializer_class = UploadedAudioSerializer
