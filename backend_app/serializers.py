from rest_framework import serializers
from .models import Register, UploadedFiles, UploadedAudio, UploadedVideo, Notes, Form1

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

class Form1Serializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        label = ('First Name'),
        required = True,
        max_length = 255,
        style = {
            'input_type': 'text',
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "First Name is required.",
        }, 
    )
    last_name = serializers.CharField(
        label = ('last Name'),
        required = True,
        max_length = 255,
        style = {
            'input_type': 'text',
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "Last Name is required.",
        }, 
    )
    email = serializers.CharField(
        label = ('Email*'),
        required = True,
        max_length = 255,
        style = {
            'input_type': 'email',
            "autofocus": False,
            "autocomplete": "off",
            "required": True,
        },
        error_messages={
            "required": "This field is required.",
            "blank": "Email is required.",
        }, 
    )
    class Meta:
        model = Form1
        fields = ['first_name', 'last_name', 'email']



