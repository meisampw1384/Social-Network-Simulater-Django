from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

class PostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            posts = Post.objects.filter(is_active=True)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, post_pk):
        post=get_object_or_404(Post, pk = post_pk,user=request.user)
        serializer = PostSerializer(post)
        return Response(serializer.data,status = status.HTTP_200_OK)
        


