from rest_framework import serializers
from .models import Register, Sample, LocalTransfer, SaveAccount

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

class SaveAccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SaveAccount