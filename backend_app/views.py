from rest_framework import viewsets
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Tutorial, Owner, Content, CartItems, Newfolder, MyLearning, UploadFileToFolder
from .serializers import RegisterSerializer, UploadedFilesSerializer, UploadedAudioSerializer, UploadedVideoSerializer, NotesSerializer, FormTemplateSerializer, UploadedTextFileSerializer, UploadedPdfFileSerializer, CommunitySerializer, MemberSerializer, CourseWebSerializer, AlarmSerializer, TutorialSerializer, OwnerSerializer, ContentSerializer, CartItemsSerializer, NewfolderSerializer, MyLearningSerializer, UploadFileToFolderSerializer

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

class TutorialView(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class OwnerView(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class CartItemsView(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer

class NewfolderView(viewsets.ModelViewSet):
    queryset = Newfolder.objects.all()
    serializer_class = NewfolderSerializer

class MyLearningView(viewsets.ModelViewSet):
    queryset = MyLearning.objects.all()
    serializer_class = MyLearningSerializer

class UploadFileToFolderView(viewsets.ModelViewSet):
    queryset = UploadFileToFolder.objects.all()
    serializer_class = UploadFileToFolderSerializer


