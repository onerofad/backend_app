from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer
from django.shortcuts import render,redirect

from rest_framework.renderers import HTMLFormRenderer


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

class CustomViewSet(viewsets.ModelViewSet):

    def form(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        renderer = HTMLFormRenderer()
        form_html = renderer.render(serializer.data, renderer_context={
            'template': 'rest_framework/api_form.html',
            'request': request
        })
        return HttpResponse(form_html)

