from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, FormTemplateSerializer, UploadedTextFileSerializer, UploadedPdfFileSerializer


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

class UploadedTextFileView(viewsets.ModelViewSet):
    queryset = UploadedTextFile.objects.all()
    serializer_class = UploadedTextFileSerializer

class UploadedPdfFileView(viewsets.ModelViewSet):
    queryset = UploadedPdfFile.objects.all()
    serializer_class = UploadedPdfFileSerializer

class NoteView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class FormTemplateView(viewsets.ModelViewSet):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer

