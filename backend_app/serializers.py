from rest_framework import serializers
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Community, Member, CourseWebUser, Alarm, Tutorial, Owner, Content, CartItems
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class UploadedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UploadedFiles

class UploadedAudioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UploadedAudio

class UploadedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UploadedVideo

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Notes

class FormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FormTemplate

class UploadedTextFileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UploadedTextFile

class UploadedPdfFileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UploadedPdfFile

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Community

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Member

class CourseWebSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CourseWebUser

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Alarm

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tutorial

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Owner

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Content

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CartItems

