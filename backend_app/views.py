from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Course, Tutor, CourseContent
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, FormTemplateSerializer, UploadedTextFileSerializer, UploadedPdfFileSerializer, CommunitySerializer, MemberSerializer, CourseWebSerializer, AlarmSerializer, CourseSerializer, TutorSerializer, CourseContentSerializer


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

class SilaView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = Register

class CommunityView(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class CourseWebUserView(viewsets.ModelViewSet):
    queryset = CourseWebUser.objects.all()
    serializer_class = CourseWebSerializer

class AlarmView(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TutorView(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class CourseContentView(viewsets.ModelViewSet):
    queryset = CourseContent.objects.all()
    serializer_class = CourseContentSerializer

