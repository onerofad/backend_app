from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Student
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, StudentSerializer
from django.shortcuts import render, redirect

from rest_framework import renderers
from rest_framework.response import Response

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

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(StudentViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='home.html')
        return response