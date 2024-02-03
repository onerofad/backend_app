from rest_framework import serializers
from .models import Register, Sample, LocalTransfer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sample

class LocalTransferSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = LocalTransfer