from django.shortcuts import render
from .models import ApiExample
from .serializers import Api_exampleSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# class Api_exampleViewSet(viewsets.ViewSet):
#       #List only
#     def list(self, request):
#         queryset = ApiExample.objects.all()
#         serializer = Api_exampleSerializer(queryset, many=True)
#         return Response(serializer.data)

class Api_exampleViewSet(viewsets.ModelViewSet):

    # list, create, retrieve, update, partial_update, destroy

    queryset = ApiExample.objects.all()
    serializer_class = Api_exampleSerializer

    @action(methods=['GET'], detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

