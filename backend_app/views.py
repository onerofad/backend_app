from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, Sample, LocalTransfer
from .serializers import RegisterSerializer, SampleSerializer, LocalTransferSerializer

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class LocalTransferView(viewsets.ModelViewSet):
    queryset = LocalTransfer.objects.all()
    serializer_class = LocalTransferSerializer