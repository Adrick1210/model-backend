from django.shortcuts import render
from .models import Model
from rest_framework import viewsets, permissions
from .serializers import ModelSerializer

# Create your views here.
class ModelViewSet(viewsets.ModelViewSet):
    queryset=Model.objects.all()
    serializer_class=ModelSerializer
    permission_classes=[permissions.AllowAny]