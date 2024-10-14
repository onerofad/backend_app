from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, FormTemplateSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class UploadedFilesView(viewsets.ModelViewSet):
    queryset = UploadedFiles.objects.all()
    serializer_class = UploadedFilesSerializer

class UploadedAudioView(viewsets.ModelViewSet):
    queryset = UploadedAudio.objects.all()
    serializer_class = UploadedAudioSerializer

class UploadedVideoView(viewsets.ModelViewSet):
    queryset = UploadedVideo.objects.all()
    serializer_class = UploadedVideoSerializer

class NoteView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class FormTemplateView(viewsets.ModelViewSet):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer