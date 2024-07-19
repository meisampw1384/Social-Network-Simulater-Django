from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import PostSerializer,CommentSerializer,LikeSerializer
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
        

class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get_post(self , post_pk):
        try:
            post = Post.objects.get(pk = post_pk)
        except Post.DoesNotExist:
            return False
    def get(self , request , post_pk):
        post = self.get_post(post_pk= post_pk)
        if not post :
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        comments = post.comments.filter(is_approved = True)
        serializer = CommentSerializer
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post (self , request , post_pk):
        post = self.get_post(post_pk=post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post , user = request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class LikeView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get_post(self,post_pk):
        try:
            return Post.objects.get(pk = post_pk)  
        except Post.DoesNotExist:
            return False
    
    def get(self, request , post_pk):
        post = self.get_post(post_pk=post_pk)
        
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        likes=post.likes.filter(is_liked = True).count()
        return Response ({'likes': likes})
    
    def post(self , request , post_pk):
        post = self.get_post(post_pk=post_pk)
        
        if not post :
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LikeSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save(post = post , user = request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            
        
       
            
    
