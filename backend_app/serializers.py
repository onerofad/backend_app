from rest_framework import serializers
from .models import Register, Sample

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sample
