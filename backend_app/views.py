from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Profile
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, ProfileSerializer
from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
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

class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')
