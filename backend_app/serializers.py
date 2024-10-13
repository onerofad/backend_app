from rest_framework import serializers
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes
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

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        label=('First Name* '), 
        required=True, 
        max_length=100,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
    )
    
    last_name = serializers.CharField(
        label=('Last Name* '),
        required=True, 
        max_length=100,
        style={
            "input_type": "text",
            "autofocus": False,
            "autocomplete": "off",
            "required": True, 
        },
      
    )
    
    email = serializers.EmailField(
        label=('Email* '),
        required=True, 
        max_length=100,
        style={
            "input_type": "email",
            "autofocus": False,
            "autocomplete": "off",
            "required": True, 
            }, 
    )
  