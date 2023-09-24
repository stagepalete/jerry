from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import TestSerializer
# Create your views here.

class ListUsers(RetrieveAPIView):
    '''
    Home View
    
    * Do nothing
    * Just for test
    '''
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)
