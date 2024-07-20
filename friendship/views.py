from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import UserListSerializer
from .models import Friendship

User = get_user_model()
class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        users=User.objects.filter(is_superuser = False , is_staff = False, is_active = True)
        serializer = UserListSerializer(users , many =True)
        return Response(serializer.data)
    
class RequestView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        user_id = request.data.get('user') #user that is want get the message from me
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail':'user does not exist'},status = status.HTTP_400_BAD_REQUEST)
        
        Friendship.objects.get_or_create(request_from = request.user , request_to = user)
        
        return Response({'detail': 'Request sent'},status = status.HTTP_201_CREATED)
        

