from django.shortcuts import render
from rest_framework import viewsets
from .models import Register, Sample, LocalTransfer, SaveAccount
from .serializers import RegisterSerializer, SampleSerializer, LocalTransferSerializer, SaveAccountSerializer
from datetime import date

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class LocalTransferView(viewsets.ModelViewSet):
    queryset = LocalTransfer.objects.all()
    serializer_class = LocalTransferSerializer

class TransferHistoryView(viewsets.ModelViewSet):
    queryset = LocalTransfer.objects.filter(trans_date = date.today()).values()
    serializer_class = LocalTransferSerializer

class SaveAccountView(viewsets.ModelViewSet):
    queryset = SaveAccount.objects.all()
    serializer_class = SaveAccountSerializer