from django.shortcuts import render
from rest_framework import status
from rest_framework import response 
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from .serializers import PostSerializer

from  .models import Post


class PostView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self , request):
        pass
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
