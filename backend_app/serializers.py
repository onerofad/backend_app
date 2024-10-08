from rest_framework import serializers
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes

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

