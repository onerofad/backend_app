from rest_framework import serializers
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, FormTemplate, UploadedTextFile, UploadedPdfFile, Member
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

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Member

