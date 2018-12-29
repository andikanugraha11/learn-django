from django.shortcuts import render
from .models import ApiExample
from .serializers import Api_exampleSerializer
from rest_framework import viewsets

class Api_exampleViewSet(viewsets.ModelViewSet):
    queryset = ApiExample.objects.all()
    serializer_class = Api_exampleSerializer
# Create your views here.
